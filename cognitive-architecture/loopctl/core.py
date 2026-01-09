"""
loopctl core - The single authority for Ralph loop decisions.

This module:
1. Finds artifacts produced by the iteration
2. Runs frozen eval harness to produce eval_report.json (authoritative)
3. Calls UnifiedBridge to decide block/allow
4. If block: updates runtime_config.json
5. Returns JSON decision for Ralph stop-hook

INVARIANTS:
- Harness is the ONLY source of truth for metrics
- Bridge is the ONLY writer of runtime_config.json
- Events are append-only
"""

import os
import sys
import json
import hashlib
import subprocess
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, Optional, Tuple


# =============================================================================
# EMERGENCY KILL SWITCH (Phase 0 Security Fix)
# =============================================================================
# This kill switch can be triggered by:
# 1. Creating a file named '.meta-loop-stop' in the current directory
# 2. Creating a file named '.meta-loop-stop' in the user's home directory
# 3. Setting environment variable META_LOOP_EMERGENCY_STOP=true
# =============================================================================

def check_emergency_stop() -> tuple:
    """
    Check for emergency stop signals.

    Returns:
        tuple: (should_stop: bool, reason: str)
    """
    # File-based kill switch - current directory
    if Path('.meta-loop-stop').exists():
        return True, "EMERGENCY_HALT: Kill switch file found in current directory"

    # File-based kill switch - home directory
    home_stop = Path(os.path.expanduser('~/.meta-loop-stop'))
    if home_stop.exists():
        return True, f"EMERGENCY_HALT: Kill switch file found at {home_stop}"

    # File-based kill switch - plugin directory
    plugin_stop = Path(__file__).parent.parent.parent / '.meta-loop-stop'
    if plugin_stop.exists():
        return True, f"EMERGENCY_HALT: Kill switch file found at {plugin_stop}"

    # Environment variable kill switch
    env_stop = os.environ.get('META_LOOP_EMERGENCY_STOP', '').lower()
    if env_stop in ('true', '1', 'yes', 'halt', 'stop'):
        return True, "EMERGENCY_HALT: Environment variable META_LOOP_EMERGENCY_STOP is set"

    return False, ""

# Add parent paths for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from integration.unified_bridge import (
    UnifiedBridge,
    BridgeInput,
    UnifiedEvent,
    DecisionIntent,
    Plane,
    Timescale,
)
from integration.telemetry_bridge import TelemetryBridge
from integration.connascence_bridge import ConnascenceBridge, ConnascenceResult


class FrozenHarness:
    """
    Wrapper for the frozen eval harness.

    The harness is the ONLY source of truth for metrics.
    It does NOT self-improve (Goodhart prevention).

    Evaluation Strategy (in order):
    1. CLI Evaluator (real LLM-based) - preferred
    2. Heuristic fallback - when CLI unavailable
    """

    def __init__(
        self,
        loop_dir: Path,
        harness_version: str = "1.0.0",
        use_cli_evaluator: bool = True,
        use_connascence: bool = True,
    ):
        self.loop_dir = Path(loop_dir)
        self.harness_version = harness_version
        self.use_cli_evaluator = use_cli_evaluator
        self.use_connascence = use_connascence
        self._harness_hash = self._compute_hash()
        self._cli_evaluator = None
        self._connascence_bridge = None

        # Try to initialize CLI evaluator
        if use_cli_evaluator:
            self._cli_evaluator = self._init_cli_evaluator()

        # Try to initialize Connascence bridge
        if use_connascence:
            self._connascence_bridge = self._init_connascence_bridge()

    def _init_cli_evaluator(self):
        """Initialize CLI evaluator if available."""
        try:
            # Import from sibling evals module
            eval_path = Path(__file__).parent.parent / "evals"
            if eval_path.exists():
                import sys
                sys.path.insert(0, str(eval_path.parent))
                from evals.cli_evaluator import ClaudeCLI
                cli = ClaudeCLI()
                if cli.is_available:
                    return cli
        except Exception as e:
            pass  # Silently fall back to heuristics
        return None

    def _init_connascence_bridge(self):
        """Initialize Connascence bridge for quality metrics."""
        try:
            bridge = ConnascenceBridge()
            return bridge
        except Exception as e:
            pass  # Connascence analysis is optional
        return None

    def _compute_hash(self) -> str:
        """Compute hash of harness for integrity verification."""
        # Hash actual harness code for integrity
        import hashlib
        harness_file = Path(__file__)
        if harness_file.exists():
            content = harness_file.read_bytes()
            file_hash = hashlib.sha256(content).hexdigest()[:12]
            return f"frozen_eval_harness_v{self.harness_version}_{file_hash}"
        return f"frozen_eval_harness_v{self.harness_version}"

    @property
    def current_hash(self) -> str:
        return self._harness_hash

    @property
    def evaluation_mode(self) -> str:
        """Return current evaluation mode."""
        return "cli_evaluator" if self._cli_evaluator else "heuristic"

    @property
    def connascence_mode(self) -> str:
        """Return current connascence analysis mode."""
        if self._connascence_bridge:
            return self._connascence_bridge.mode
        return "disabled"

    def verify_integrity(self, expected_hash: Optional[str]) -> bool:
        """Verify harness hasn't been modified."""
        if expected_hash is None:
            return True
        return self._harness_hash == expected_hash

    def grade(self, artifact_path: Path) -> Dict[str, Any]:
        """
        Grade an artifact and return metrics.

        Uses CLI evaluator (real LLM) when available,
        falls back to heuristics otherwise.
        Optionally includes connascence quality metrics.

        Returns metrics dict (NOT model-reported).
        """
        artifact_path = Path(artifact_path)

        if not artifact_path.exists():
            return {
                "task_accuracy": 0.0,
                "token_efficiency": 0.0,
                "edge_robustness": 0.0,
                "epistemic_consistency": 0.0,
                "overall": 0.0,
                "evaluation_mode": "none",
                "connascence_mode": "disabled",
            }

        # Read artifact content
        content = artifact_path.read_text(errors="ignore")

        # Try CLI evaluator first (real LLM-based)
        if self._cli_evaluator:
            try:
                metrics = self._grade_with_cli(content)
                metrics["evaluation_mode"] = "cli_evaluator"
            except Exception as e:
                # Log but continue to fallback
                metrics = self._grade_with_heuristics(content)
                metrics["evaluation_mode"] = "heuristic"
        else:
            # Fallback: heuristic grading
            metrics = self._grade_with_heuristics(content)
            metrics["evaluation_mode"] = "heuristic"

        # Add connascence quality metrics if enabled
        if self._connascence_bridge:
            connascence_result = self._grade_with_connascence(artifact_path)
            metrics["connascence_mode"] = self._connascence_bridge.mode
            metrics["connascence"] = {
                "sigma_level": connascence_result.sigma_level,
                "dpmo": connascence_result.dpmo,
                "nasa_compliance": connascence_result.nasa_compliance,
                "mece_score": connascence_result.mece_score,
                "theater_risk": connascence_result.theater_risk,
                "clarity_score": connascence_result.clarity_score,
                "violations_count": connascence_result.violations_count,
                "critical_violations": connascence_result.critical_violations,
                "passes_strict": connascence_result.passes_gate(strict=True),
                "passes_lenient": connascence_result.passes_gate(strict=False),
            }
            # Incorporate quality gate into overall score (10% weight)
            quality_factor = 1.0 if connascence_result.passes_gate(strict=False) else 0.9
            metrics["overall"] = metrics["overall"] * quality_factor
        else:
            metrics["connascence_mode"] = "disabled"

        return metrics

    def _grade_with_connascence(self, artifact_path: Path) -> ConnascenceResult:
        """
        Grade using Connascence Analyzer (7-Analyzer Suite).

        Returns ConnascenceResult with quality metrics.
        """
        try:
            if artifact_path.is_dir():
                return self._connascence_bridge.analyze_directory(artifact_path)
            else:
                return self._connascence_bridge.analyze_file(artifact_path)
        except Exception as e:
            # Return empty result on failure
            return ConnascenceResult(success=False, error=str(e))

    def _grade_with_cli(self, content: str) -> Dict[str, float]:
        """
        Grade using CLI evaluator (real LLM-as-judge).

        Sends content to Claude CLI for evaluation.
        """
        judge_prompt = f"""You are evaluating code/text quality. Score each dimension from 0.0 to 1.0.

CONTENT TO EVALUATE:
{content[:3000]}

Score these dimensions (0.0 to 1.0):
1. task_accuracy: Does the content accomplish the stated task correctly?
2. token_efficiency: Is the content concise without unnecessary verbosity?
3. edge_robustness: Does it handle edge cases and errors appropriately?
4. epistemic_consistency: Are claims properly qualified with confidence/evidence?

Respond in JSON format ONLY:
{{"task_accuracy": 0.0, "token_efficiency": 0.0, "edge_robustness": 0.0, "epistemic_consistency": 0.0}}"""

        result = self._cli_evaluator.send_message(judge_prompt, max_tokens=200)
        response = result.get("response", "")

        # Parse JSON from response
        import json
        start = response.find('{')
        end = response.rfind('}') + 1
        if start >= 0 and end > start:
            scores = json.loads(response[start:end])
            # Calculate overall
            weights = {
                "task_accuracy": 0.4,
                "token_efficiency": 0.2,
                "edge_robustness": 0.2,
                "epistemic_consistency": 0.2,
            }
            scores["overall"] = sum(
                scores.get(k, 0.5) * w for k, w in weights.items()
            )
            return scores

        raise ValueError("Failed to parse CLI evaluator response")

    def _grade_with_heuristics(self, content: str) -> Dict[str, float]:
        """Grade using heuristic rules (fallback)."""
        metrics = {
            "task_accuracy": self._grade_accuracy(content),
            "token_efficiency": self._grade_efficiency(content),
            "edge_robustness": self._grade_robustness(content),
            "epistemic_consistency": self._grade_epistemic(content),
        }

        # Overall is weighted average
        weights = {
            "task_accuracy": 0.4,
            "token_efficiency": 0.2,
            "edge_robustness": 0.2,
            "epistemic_consistency": 0.2,
        }
        metrics["overall"] = sum(
            metrics[k] * weights[k] for k in weights
        )

        return metrics

    def _grade_accuracy(self, content: str) -> float:
        """Grade task accuracy (simplified)."""
        # Check for completion indicators
        if not content:
            return 0.0
        if len(content) < 100:
            return 0.3
        if "[assert" in content.lower() or "[witnessed" in content.lower():
            return 0.8
        return 0.6

    def _grade_efficiency(self, content: str) -> float:
        """Grade token efficiency (simplified)."""
        # Shorter responses with same quality = more efficient
        word_count = len(content.split())
        if word_count < 50:
            return 0.9
        elif word_count < 200:
            return 0.8
        elif word_count < 500:
            return 0.7
        else:
            return 0.5

    def _grade_robustness(self, content: str) -> float:
        """Grade edge case handling (simplified)."""
        # Check for error handling indicators
        indicators = ["error", "exception", "edge case", "boundary", "validation"]
        count = sum(1 for i in indicators if i in content.lower())
        return min(0.9, 0.5 + count * 0.1)

    def _grade_epistemic(self, content: str) -> float:
        """Grade epistemic consistency (simplified)."""
        # Check for VERIX markers
        verix_markers = ["[assert", "[conf:", "[ground:", "[state:", "[witnessed", "[inferred"]
        count = sum(1 for m in verix_markers if m in content.lower())
        return min(0.95, 0.4 + count * 0.1)


def find_artifact(output_path: Optional[str], loop_dir: Path) -> Path:
    """Find the artifact to grade."""
    if output_path:
        return Path(output_path)

    # Look for common output patterns
    candidates = [
        loop_dir / "output" / "latest.txt",
        loop_dir / "output.txt",
        Path(".claude") / "output.txt",
    ]

    for candidate in candidates:
        if candidate.exists():
            return candidate

    # Return a non-existent path (harness will handle)
    return loop_dir / "output" / "latest.txt"


def get_git_head() -> Optional[str]:
    """Get current git HEAD hash."""
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"],
            capture_output=True,
            text=True,
            timeout=5,
        )
        if result.returncode == 0:
            return result.stdout.strip()
    except Exception:
        pass
    return None


def ralph_iteration_complete(
    state_path: str,
    loop_dir: str,
    output_path: Optional[str] = None,
    iteration: Optional[int] = None,
) -> Dict[str, Any]:
    """
    SINGLE AUTHORITY for Ralph loop decisions.

    This function:
    0. CHECK EMERGENCY KILL SWITCH FIRST
    1. Finds the artifact produced
    2. Grades with FROZEN harness (authoritative)
    3. Writes authoritative eval_report.json
    4. Asks bridge (NOT model) for decision
    5. If continue: updates runtime_config.json
    6. Appends event to events.jsonl
    7. Returns decision JSON for Ralph stop-hook

    Args:
        state_path: Path to Ralph state file
        loop_dir: Path to .loop/ directory
        output_path: Optional explicit artifact path
        iteration: Optional iteration number (reads from state if not provided)

    Returns:
        Decision JSON: {"decision": "block|allow", "reason": "..."}
    """
    # STEP 0: CHECK EMERGENCY KILL SWITCH BEFORE ANYTHING ELSE
    should_stop, stop_reason = check_emergency_stop()
    if should_stop:
        return {
            "decision": "allow",  # allow = stop the loop
            "reason": stop_reason,
            "emergency_halt": True,
        }

    loop_dir = Path(loop_dir)
    bridge = UnifiedBridge(loop_dir)

    # 1. Load current state
    current_config = bridge.load_runtime_config()
    policy = bridge.load_policy()
    history = bridge.load_history()

    # Get iteration from state or param
    if iteration is None:
        iteration = current_config.get("iteration", 0)

    # 2. Find artifact
    artifact_path = find_artifact(output_path, loop_dir)

    # 3. Grade with FROZEN harness (authoritative)
    harness = FrozenHarness(loop_dir)
    expected_hash = policy.get("harness_hash")

    if not harness.verify_integrity(expected_hash):
        return {
            "decision": "allow",
            "reason": "HALT: Harness integrity check failed",
        }

    harness_metrics = harness.grade(artifact_path)

    # 4. Write authoritative eval report
    eval_report = {
        "_comment": "EVIDENCE TRUTH - Written ONLY by Frozen Eval Harness",
        "_schema_version": "1.0.0",
        "iteration": iteration,
        "timestamp": datetime.now().isoformat(),
        "artifact_path": str(artifact_path),
        "artifact_hash": hashlib.sha256(
            artifact_path.read_bytes() if artifact_path.exists() else b""
        ).hexdigest()[:16],
        "metrics": harness_metrics,
        "harness_version": harness.harness_version,
        "harness_hash": harness.current_hash,
    }
    (loop_dir / "eval_report.json").write_text(json.dumps(eval_report, indent=2))

    # 5. Build bridge input
    task_metadata = {}
    task_meta_path = loop_dir / "task_metadata.json"
    if task_meta_path.exists():
        task_metadata = json.loads(task_meta_path.read_text())

    bridge_input = BridgeInput(
        iteration=iteration,
        artifact_path=str(artifact_path),
        eval_report=eval_report,
        history=history,
        policy=policy,
        task_metadata=task_metadata,
        current_config=current_config,
    )

    # 6. Ask bridge (NOT model) for decision
    next_config = bridge.propose_next_config(bridge_input)

    # 7. Build event
    event = UnifiedEvent(
        task_id=f"ralph_{iteration}",
        plane=Plane.EXECUTION.value,
        timescale=Timescale.MICRO.value,
        iteration=iteration,
        git_head=get_git_head(),
        config={
            "mode": next_config.mode,
            "vector14": next_config.vector14,
            "frames": list(k for k, v in next_config.frames.items() if v),
            "verix_strictness": next_config.verix.get("strictness", "MODERATE"),
        },
        metrics=harness_metrics,
        decision=next_config.decision_intent.value,
        reason="; ".join(next_config.reasons),
        grounds=f"[assert|confident] Decision based on harness metrics [ground:eval_report] [conf:0.95] [state:confirmed]",
    )

    # 8. Always append event (audit trail)
    bridge.append_event(event)

    # 9. Update history
    bridge.update_history(iteration, harness_metrics)

    # 10. Store telemetry to Memory MCP
    try:
        telemetry_bridge = TelemetryBridge(loop_dir)
        telemetry_result = telemetry_bridge.store_to_memory_mcp(iteration=iteration)
        # Add telemetry storage info to event (non-blocking)
    except Exception as e:
        # Telemetry storage is non-blocking - log but continue
        pass

    # 11. Make final decision
    if next_config.decision_intent == DecisionIntent.HALT:
        return {
            "decision": "allow",
            "reason": next_config.reasons[0] if next_config.reasons else "HALT",
        }

    if next_config.decision_intent == DecisionIntent.ESCALATE:
        return {
            "decision": "allow",
            "reason": f"ESCALATE: Human review required. Gates: {next_config.human_gates_triggered}",
        }

    # Continue iteration - write updated config
    bridge.write_config(next_config, iteration + 1, harness_metrics.get("overall", 0))

    return {
        "decision": "block",
        "reason": "CONTINUE_ITERATION",
        "iteration": iteration + 1,
        "metrics": harness_metrics,
    }


def get_status(loop_dir: str) -> Dict[str, Any]:
    """Get current loop status."""
    loop_dir = Path(loop_dir)
    bridge = UnifiedBridge(loop_dir)

    config = bridge.load_runtime_config()
    eval_report = bridge.load_eval_report()
    history = bridge.load_history()
    policy = bridge.load_policy()

    return {
        "current_iteration": config.get("iteration", 0),
        "mode": config.get("mode", "unknown"),
        "exploration_mode": config.get("exploration_mode", "unknown"),
        "last_score": eval_report.get("metrics", {}).get("overall", 0),
        "history_length": len(history),
        "max_iterations": policy.get("max_iterations", 50),
        "regression_threshold": policy.get("regression_threshold", 0.03),
    }


def reset_loop(loop_dir: str) -> Dict[str, Any]:
    """Reset loop state to defaults."""
    loop_dir = Path(loop_dir)
    bridge = UnifiedBridge(loop_dir)

    # Write default config
    default_config = bridge._default_config()
    (loop_dir / "runtime_config.json").write_text(json.dumps({
        "_comment": "CONTROL INPUT - Reset by loopctl",
        "_schema_version": "1.0.0",
        **default_config,
        "updated_at": datetime.now().isoformat(),
    }, indent=2))

    # Reset history
    (loop_dir / "history.json").write_text(json.dumps({
        "_comment": "ITERATION HISTORY - Reset by loopctl",
        "iterations": [],
    }, indent=2))

    return {"status": "reset", "message": "Loop state reset to defaults"}
