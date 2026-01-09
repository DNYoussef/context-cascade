"""
loopctl CLI entry point.

Usage:
    python -m loopctl ralph_iteration_complete --state <statefile> --loop-dir .loop
    python -m loopctl status --loop-dir .loop
    python -m loopctl reset --loop-dir .loop
    python -m loopctl self-test --loop-dir .loop
"""

import argparse
import json
import sys
from pathlib import Path

from .core import ralph_iteration_complete, get_status, reset_loop, FrozenHarness


def main():
    parser = argparse.ArgumentParser(
        description="loopctl - Single Authority for Loop Control",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    # Process Ralph iteration completion
    python -m loopctl ralph_iteration_complete --state .claude/ralph-loop.local.md --loop-dir .loop

    # Get current status
    python -m loopctl status --loop-dir .loop

    # Reset loop state
    python -m loopctl reset --loop-dir .loop
        """,
    )

    subparsers = parser.add_subparsers(dest="command", help="Command to run")

    # ralph_iteration_complete command
    ralph_parser = subparsers.add_parser(
        "ralph_iteration_complete",
        help="Process a Ralph iteration completion",
    )
    ralph_parser.add_argument(
        "--state",
        required=True,
        help="Path to Ralph state file",
    )
    ralph_parser.add_argument(
        "--loop-dir",
        required=True,
        help="Path to .loop/ directory",
    )
    ralph_parser.add_argument(
        "--output",
        help="Path to artifact output file",
    )
    ralph_parser.add_argument(
        "--iteration",
        type=int,
        help="Iteration number (reads from state if not provided)",
    )

    # status command
    status_parser = subparsers.add_parser(
        "status",
        help="Show current loop status",
    )
    status_parser.add_argument(
        "--loop-dir",
        required=True,
        help="Path to .loop/ directory",
    )

    # reset command
    reset_parser = subparsers.add_parser(
        "reset",
        help="Reset loop state to defaults",
    )
    reset_parser.add_argument(
        "--loop-dir",
        required=True,
        help="Path to .loop/ directory",
    )

    # self-test command
    test_parser = subparsers.add_parser(
        "self-test",
        help="Run FrozenHarness self-test",
    )
    test_parser.add_argument(
        "--loop-dir",
        default=".",
        help="Path to .loop/ directory (default: current)",
    )
    test_parser.add_argument(
        "--no-cli",
        action="store_true",
        help="Force heuristic mode (skip CLI evaluator)",
    )

    args = parser.parse_args()

    if args.command == "ralph_iteration_complete":
        result = ralph_iteration_complete(
            state_path=args.state,
            loop_dir=args.loop_dir,
            output_path=args.output,
            iteration=args.iteration,
        )
        print(json.dumps(result))

    elif args.command == "status":
        result = get_status(args.loop_dir)
        print(json.dumps(result, indent=2))

    elif args.command == "reset":
        result = reset_loop(args.loop_dir)
        print(json.dumps(result, indent=2))

    elif args.command == "self-test":
        print("=" * 60)
        print("FrozenHarness Self-Test")
        print("=" * 60)

        # Initialize harness
        harness = FrozenHarness(
            Path(args.loop_dir),
            use_cli_evaluator=not args.no_cli,
        )

        print(f"\nHarness Version: {harness.harness_version}")
        print(f"Harness Hash: {harness.current_hash}")
        print(f"Evaluation Mode: {harness.evaluation_mode}")
        print(f"CLI Evaluator: {'AVAILABLE' if harness._cli_evaluator else 'NOT AVAILABLE'}")

        # Create test artifact
        import tempfile
        test_content = """
[assert|confident] This is a test artifact for FrozenHarness evaluation.
[ground:self-test] The content demonstrates VERIX compliance.

## Implementation
The following code handles edge cases:
```python
def safe_divide(a, b):
    if b == 0:
        raise ValueError("Division by zero")
    return a / b
```

[conf:0.85] [state:confirmed] Test complete.
"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
            f.write(test_content)
            test_path = Path(f.name)

        print(f"\nTest Artifact: {test_path}")
        print("\nGrading...")

        # Grade the test artifact
        metrics = harness.grade(test_path)

        print("\n--- Results ---")
        for key, value in metrics.items():
            if isinstance(value, float):
                print(f"  {key}: {value:.4f}")
            else:
                print(f"  {key}: {value}")

        # Cleanup
        test_path.unlink()

        # Verify thresholds
        print("\n--- Verification ---")
        passed = True
        if metrics.get("overall", 0) < 0.5:
            print("  WARN: Overall score below 0.5")
            passed = False
        if metrics.get("epistemic_consistency", 0) < 0.6:
            print("  WARN: Epistemic consistency below 0.6")
            passed = False

        status = "PASS" if passed else "NEEDS REVIEW"
        print(f"\nStatus: {status}")

        sys.exit(0 if passed else 1)

    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
