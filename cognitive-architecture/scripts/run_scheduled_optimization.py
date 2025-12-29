#!/usr/bin/env python3
"""
Scheduled Optimization Runner

Runs every 3 days to:
1. Load telemetry from memory-mcp
2. Run dual MOO (GlobalMOO -> PyMOO)
3. Distill named modes
4. Trigger cascade language update

Usage:
    python run_scheduled_optimization.py [--days 3] [--cascade]

Schedule (Windows Task Scheduler or cron):
    # Windows (run every 3 days at 3 AM)
    schtasks /create /tn "CognitiveArchMOO" /tr "python run_scheduled_optimization.py --cascade" /sc daily /mo 3 /st 03:00

    # Linux/Mac (crontab)
    0 3 */3 * * cd /path/to/cognitive-architecture && python scripts/run_scheduled_optimization.py --cascade
"""

import os
import sys
import json
import argparse
from datetime import datetime
from pathlib import Path

# Add parent to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from optimization.two_stage_optimizer import run_with_telemetry, distill_named_modes


def trigger_cascade_update(modes_path: str, dry_run: bool = False) -> bool:
    """
    Trigger cascade language update with new modes.

    Calls real_cascade_optimizer to apply MOO-optimized modes to:
    commands -> agents -> skills -> playbooks

    Args:
        modes_path: Path to named_modes.json from two-stage optimization
        dry_run: If True, analyze but don't write files

    Returns:
        True if successful, False otherwise
    """
    print("\n[CASCADE] Triggering language update with MOO modes...")

    try:
        from scripts.real_cascade_optimizer import apply_modes_from_optimization

        results = apply_modes_from_optimization(
            modes_path=modes_path,
            levels=["commands", "agents", "skills", "playbooks"],
            dry_run=dry_run,
        )

        if "error" in results:
            print(f"[CASCADE] Error: {results['error']}")
            return False

        # Log summary
        total_files = sum(
            level.get("final_metrics", {}).get("total_files", 0)
            for level in results.get("levels", {}).values()
        )
        print(f"[CASCADE] Update complete: {total_files} files processed")
        return True

    except Exception as e:
        print(f"[CASCADE] Error: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    parser = argparse.ArgumentParser(description="Run scheduled MOO optimization")
    parser.add_argument("--days", type=int, default=3, help="Days of telemetry to load")
    parser.add_argument("--cascade", action="store_true", help="Trigger cascade update after optimization")
    parser.add_argument("--dry-run", action="store_true", help="Don't save results")
    args = parser.parse_args()

    print("=" * 70)
    print("SCHEDULED COGNITIVE ARCHITECTURE OPTIMIZATION")
    print(f"Started: {datetime.utcnow().isoformat()}Z")
    print(f"Telemetry window: {args.days} days")
    print("=" * 70)

    # Run optimization
    result = run_with_telemetry(days=args.days)

    if "error" in result:
        print(f"\n[ERROR] Optimization failed: {result['error']}")
        sys.exit(1)

    # Print summary
    print("\n--- Optimization Summary ---")
    print(f"Telemetry records: {result['telemetry_stats'].get('total_records', 0)}")
    print(f"Stage 1 solutions: {result['stage1_count']}")
    print(f"Stage 2 solutions: {result['stage2_count']}")
    print(f"Output: {result['output_dir']}")

    print("\n--- Named Modes ---")
    for name, outcomes in result['modes'].items():
        print(f"  {name}: acc={outcomes['task_accuracy']:.3f}, "
              f"eff={outcomes['token_efficiency']:.3f}")

    # Trigger cascade if requested
    if args.cascade:
        modes_path = Path(result['output_dir']) / "named_modes.json"
        if modes_path.exists():
            trigger_cascade_update(str(modes_path), dry_run=args.dry_run)
        else:
            print("[WARN] Modes file not found, skipping cascade")

    # Log completion
    log_dir = Path(__file__).parent.parent / "storage" / "optimization_logs"
    log_dir.mkdir(parents=True, exist_ok=True)

    log_file = log_dir / f"run_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}.json"
    with open(log_file, 'w') as f:
        json.dump({
            "timestamp": datetime.utcnow().isoformat(),
            "days": args.days,
            "cascade": args.cascade,
            "result": result,
        }, f, indent=2)

    print(f"\n[LOG] Saved to: {log_file}")
    print("\nDone.")


if __name__ == "__main__":
    main()
