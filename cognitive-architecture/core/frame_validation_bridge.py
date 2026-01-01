"""
FrameValidationBridge - VERIX-VERILINGUA Bidirectional Integration.

FIX-5 from REMEDIATION-PLAN.md:
Creates a bidirectional bridge between VERIX epistemic validation and
VERILINGUA cognitive frame activation.

Current Flow (unidirectional):
    VERILINGUA frames -> PromptBuilder -> VERIX validation -> output

New Flow (bidirectional):
    VERILINGUA frames -> PromptBuilder -> VERIX validation
                  ^                              |
                  |______ feedback loop _________|

The bridge:
1. Collects VERIX validation results (compliance scores, violations)
2. Analyzes which frames correlate with better/worse compliance
3. Adjusts frame weights dynamically based on feedback
4. Enforces the evidential minimum floor (cannot go below 0.30)

This creates a self-improving system where frame configurations
evolve based on actual output quality.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple
from collections import deque
from enum import Enum
import logging
import time
import json
import threading
from pathlib import Path

from .verix import VerixClaim, VerixValidator, VerixParser
from .verilingua import FRAME_WEIGHTS, EVIDENTIAL_MINIMUM, FrameWeightViolation
from .config import FrameworkConfig, PromptConfig, FullConfig

logger = logging.getLogger(__name__)


class FeedbackSignal(Enum):
    """Feedback signals from VERIX validation."""
    STRONG_POSITIVE = "strong_positive"    # Compliance >= 0.9
    POSITIVE = "positive"                   # Compliance 0.7-0.9
    NEUTRAL = "neutral"                     # Compliance 0.5-0.7
    NEGATIVE = "negative"                   # Compliance 0.3-0.5
    STRONG_NEGATIVE = "strong_negative"    # Compliance < 0.3


@dataclass
class ValidationFeedback:
    """
    Captures feedback from a single VERIX validation run.

    Used to correlate frame configurations with compliance outcomes.
    """
    timestamp: float
    active_frames: List[str]
    frame_weights: Dict[str, float]
    compliance_score: float
    violation_count: int
    violations: List[str]
    signal: FeedbackSignal
    task_type: str = "default"

    def to_dict(self) -> Dict:
        return {
            "timestamp": self.timestamp,
            "active_frames": self.active_frames,
            "frame_weights": self.frame_weights,
            "compliance_score": self.compliance_score,
            "violation_count": self.violation_count,
            "violations": self.violations,
            "signal": self.signal.value,
            "task_type": self.task_type,
        }

    @classmethod
    def from_dict(cls, data: Dict) -> "ValidationFeedback":
        return cls(
            timestamp=data["timestamp"],
            active_frames=data["active_frames"],
            frame_weights=data["frame_weights"],
            compliance_score=data["compliance_score"],
            violation_count=data["violation_count"],
            violations=data["violations"],
            signal=FeedbackSignal(data["signal"]),
            task_type=data.get("task_type", "default"),
        )


@dataclass
class FrameCorrelation:
    """
    Tracks correlation between a frame and compliance outcomes.

    Positive delta means the frame correlates with better compliance.
    Negative delta means the frame correlates with worse compliance.
    """
    frame_name: str
    activation_count: int = 0
    total_compliance: float = 0.0
    avg_compliance: float = 0.0
    weight_delta: float = 0.0  # Suggested weight adjustment

    def update(self, compliance: float):
        """Update correlation with new compliance data."""
        self.activation_count += 1
        self.total_compliance += compliance
        self.avg_compliance = self.total_compliance / self.activation_count


class FrameValidationBridge:
    """
    Bidirectional bridge between VERIX validation and VERILINGUA frames.

    Collects validation feedback and uses it to dynamically adjust
    frame weights, creating a feedback loop for self-improvement.

    Key features:
    - Tracks frame-compliance correlations
    - Suggests weight adjustments based on outcomes
    - Enforces evidential minimum floor
    - Persists feedback history for cross-session learning
    """

    # Learning rate for weight adjustments (conservative)
    LEARNING_RATE = 0.05

    # Minimum samples before adjusting weights
    MIN_SAMPLES_FOR_ADJUSTMENT = 10

    # Maximum adjustment per update (prevents wild swings)
    MAX_ADJUSTMENT = 0.10

    def __init__(
        self,
        config: FullConfig,
        feedback_dir: Optional[Path] = None,
        auto_adjust: bool = True,
    ):
        """
        Initialize the bridge.

        Args:
            config: Current FullConfig
            feedback_dir: Directory to persist feedback history
            auto_adjust: If True, automatically apply weight adjustments
        """
        self.config = config
        self.auto_adjust = auto_adjust

        if feedback_dir is None:
            feedback_dir = Path(__file__).parent.parent / "storage" / "frame-feedback"
        self.feedback_dir = Path(feedback_dir)
        self.feedback_dir.mkdir(parents=True, exist_ok=True)

        # Validation components
        self.verix_validator = VerixValidator(config.prompt)
        self.verix_parser = VerixParser(config.prompt)

        # FIX: Thread safety lock for shared state (FVB-RACE)
        self._lock = threading.Lock()

        # FIX: Bounded feedback history to prevent memory leak (FVB-MEM)
        # Using deque with maxlen=1000 to match persistence policy
        self.feedback_history: deque = deque(maxlen=1000)

        # Frame correlations
        self.correlations: Dict[str, FrameCorrelation] = {
            frame: FrameCorrelation(frame_name=frame)
            for frame in FRAME_WEIGHTS.keys()
        }

        # Baseline for comparison (no frames active)
        self.baseline_compliance: Optional[float] = None

        # Load persisted history
        self._load_history()

    def _signal_from_score(self, score: float) -> FeedbackSignal:
        """Convert compliance score to feedback signal."""
        if score >= 0.9:
            return FeedbackSignal.STRONG_POSITIVE
        elif score >= 0.7:
            return FeedbackSignal.POSITIVE
        elif score >= 0.5:
            return FeedbackSignal.NEUTRAL
        elif score >= 0.3:
            return FeedbackSignal.NEGATIVE
        else:
            return FeedbackSignal.STRONG_NEGATIVE

    def validate_and_feedback(
        self,
        response_text: str,
        task_type: str = "default",
    ) -> Tuple[float, List[str], ValidationFeedback]:
        """
        Validate a response and record feedback.

        This is the main entry point for the bidirectional flow.

        Args:
            response_text: The model's response to validate
            task_type: Type of task for correlation tracking

        Returns:
            (compliance_score, violations, feedback)
        """
        # Parse claims from response
        claims = self.verix_parser.parse(response_text)

        # Validate claims
        is_valid, violations = self.verix_validator.validate(claims)
        compliance_score = self.verix_validator.compliance_score(claims)

        # Get current frame configuration
        active_frames = self.config.framework.active_frames()
        current_weights = self.config.framework.frame_weights.copy()

        # Create feedback record
        feedback = ValidationFeedback(
            timestamp=time.time(),
            active_frames=active_frames,
            frame_weights=current_weights,
            compliance_score=compliance_score,
            violation_count=len(violations),
            violations=violations,
            signal=self._signal_from_score(compliance_score),
            task_type=task_type,
        )

        # FIX: Use lock for thread-safe shared state mutation (FVB-RACE)
        with self._lock:
            # Record feedback
            self.feedback_history.append(feedback)

            # Update correlations
            self._update_correlations(feedback)

            # Auto-adjust if enabled and enough samples
            if self.auto_adjust and len(self.feedback_history) >= self.MIN_SAMPLES_FOR_ADJUSTMENT:
                self._apply_adjustments()

            # Persist feedback periodically
            if len(self.feedback_history) % 10 == 0:
                self._save_history()

        logger.info(
            f"Validation feedback: score={compliance_score:.2f}, "
            f"signal={feedback.signal.value}, frames={active_frames}"
        )

        return compliance_score, violations, feedback

    def _update_correlations(self, feedback: ValidationFeedback):
        """Update frame-compliance correlations with new feedback."""
        # Update correlations for active frames
        for frame_name in feedback.active_frames:
            if frame_name in self.correlations:
                self.correlations[frame_name].update(feedback.compliance_score)

        # Track baseline (when minimal frames active)
        if len(feedback.active_frames) <= 1:
            if self.baseline_compliance is None:
                self.baseline_compliance = feedback.compliance_score
            else:
                # Exponential moving average
                self.baseline_compliance = (
                    0.9 * self.baseline_compliance + 0.1 * feedback.compliance_score
                )

    def _calculate_weight_deltas(self) -> Dict[str, float]:
        """
        Calculate suggested weight adjustments based on correlations.

        Frames with above-average compliance get positive delta.
        Frames with below-average compliance get negative delta.
        """
        deltas = {}

        # Calculate global average compliance
        all_scores = [f.compliance_score for f in self.feedback_history]
        if not all_scores:
            return deltas

        global_avg = sum(all_scores) / len(all_scores)

        for frame_name, corr in self.correlations.items():
            if corr.activation_count < 5:
                # Not enough data for this frame
                deltas[frame_name] = 0.0
                continue

            # Compare frame's average to global average
            diff = corr.avg_compliance - global_avg

            # Scale by learning rate, clamp to max adjustment
            delta = diff * self.LEARNING_RATE
            delta = max(-self.MAX_ADJUSTMENT, min(self.MAX_ADJUSTMENT, delta))

            deltas[frame_name] = delta
            corr.weight_delta = delta

        return deltas

    def _apply_adjustments(self):
        """Apply calculated weight adjustments to config."""
        deltas = self._calculate_weight_deltas()

        for frame_name, delta in deltas.items():
            if abs(delta) < 0.01:
                continue  # Skip negligible adjustments

            current_weight = self.config.framework.frame_weights.get(frame_name, 0.5)
            new_weight = current_weight + delta

            # Clamp to valid range [0.0, 1.0]
            new_weight = max(0.0, min(1.0, new_weight))

            # Enforce evidential minimum
            if frame_name == "evidential":
                new_weight = max(EVIDENTIAL_MINIMUM, new_weight)

            # Only update if actually changed
            if abs(new_weight - current_weight) >= 0.01:
                try:
                    self.config.framework.set_frame_weight(frame_name, new_weight)
                    logger.info(
                        f"Adjusted {frame_name} weight: {current_weight:.2f} -> {new_weight:.2f}"
                    )
                except (ValueError, FrameWeightViolation) as e:
                    logger.warning(f"Could not adjust {frame_name}: {e}")

    def get_adjustment_suggestions(self) -> Dict[str, Dict]:
        """
        Get weight adjustment suggestions without applying them.

        Returns:
            Dict mapping frame names to adjustment info
        """
        deltas = self._calculate_weight_deltas()
        suggestions = {}

        for frame_name, delta in deltas.items():
            current = self.config.framework.frame_weights.get(frame_name, 0.5)
            corr = self.correlations.get(frame_name)

            suggestions[frame_name] = {
                "current_weight": current,
                "suggested_delta": delta,
                "suggested_weight": max(0.0, min(1.0, current + delta)),
                "activation_count": corr.activation_count if corr else 0,
                "avg_compliance": corr.avg_compliance if corr else 0.0,
                "confidence": min(1.0, (corr.activation_count / 50)) if corr else 0.0,
            }

        return suggestions

    def get_frame_performance_report(self) -> Dict:
        """
        Generate a report on frame performance.

        Returns:
            Dict with performance metrics per frame
        """
        report = {
            "total_validations": len(self.feedback_history),
            "baseline_compliance": self.baseline_compliance,
            "frames": {},
            "task_type_breakdown": {},
        }

        # Frame performance
        for frame_name, corr in self.correlations.items():
            report["frames"][frame_name] = {
                "activation_count": corr.activation_count,
                "avg_compliance": corr.avg_compliance,
                "current_weight": self.config.framework.frame_weights.get(frame_name, 0.5),
                "weight_delta": corr.weight_delta,
            }

        # Task type breakdown
        task_scores: Dict[str, List[float]] = {}
        for fb in self.feedback_history:
            if fb.task_type not in task_scores:
                task_scores[fb.task_type] = []
            task_scores[fb.task_type].append(fb.compliance_score)

        for task_type, scores in task_scores.items():
            report["task_type_breakdown"][task_type] = {
                "count": len(scores),
                "avg_compliance": sum(scores) / len(scores) if scores else 0.0,
            }

        return report

    def reset_correlations(self):
        """Reset all correlations (useful for retraining)."""
        for frame_name in self.correlations:
            self.correlations[frame_name] = FrameCorrelation(frame_name=frame_name)
        self.baseline_compliance = None
        logger.info("Frame correlations reset")

    def _save_history(self):
        """Save feedback history to disk."""
        history_file = self.feedback_dir / "feedback_history.json"

        # FIX: Create immutable snapshot for thread-safe persistence (FVB-RACE)
        # deque already bounds to 1000, just copy for thread safety
        recent_history = list(self.feedback_history)

        data = {
            "history": [fb.to_dict() for fb in recent_history],
            "correlations": {
                name: {
                    "activation_count": corr.activation_count,
                    "total_compliance": corr.total_compliance,
                    "avg_compliance": corr.avg_compliance,
                    "weight_delta": corr.weight_delta,
                }
                for name, corr in self.correlations.items()
            },
            "baseline_compliance": self.baseline_compliance,
            "saved_at": time.time(),
        }

        # FIX: Wrap I/O in try/except for defensive programming (FVB-IO)
        try:
            with open(history_file, "w") as f:
                json.dump(data, f, indent=2)
        except (IOError, OSError, json.JSONEncodeError) as e:
            logger.warning(f"Could not save feedback history: {e}")

    def _load_history(self):
        """Load feedback history from disk."""
        history_file = self.feedback_dir / "feedback_history.json"

        if not history_file.exists():
            return

        try:
            with open(history_file) as f:
                data = json.load(f)

            # FIX: Populate deque properly (FVB-MEM)
            loaded_entries = [
                ValidationFeedback.from_dict(fb)
                for fb in data.get("history", [])
            ]
            self.feedback_history.clear()
            self.feedback_history.extend(loaded_entries)

            for name, corr_data in data.get("correlations", {}).items():
                if name in self.correlations:
                    self.correlations[name].activation_count = corr_data.get("activation_count", 0)
                    self.correlations[name].total_compliance = corr_data.get("total_compliance", 0.0)
                    self.correlations[name].avg_compliance = corr_data.get("avg_compliance", 0.0)
                    self.correlations[name].weight_delta = corr_data.get("weight_delta", 0.0)

            self.baseline_compliance = data.get("baseline_compliance")

            logger.info(f"Loaded {len(self.feedback_history)} feedback entries from history")

        except (json.JSONDecodeError, KeyError) as e:
            logger.warning(f"Could not load feedback history: {e}")


def create_bridge(config: Optional[FullConfig] = None) -> FrameValidationBridge:
    """
    Factory function to create a FrameValidationBridge.

    Args:
        config: Optional FullConfig (uses default if not provided)

    Returns:
        Configured FrameValidationBridge instance
    """
    return FrameValidationBridge(config or FullConfig())


# Convenience function for one-shot validation with feedback
def validate_with_feedback(
    response_text: str,
    config: Optional[FullConfig] = None,
    task_type: str = "default",
) -> Tuple[float, List[str]]:
    """
    Validate a response and record feedback (stateless convenience function).

    Args:
        response_text: The response to validate
        config: Optional configuration
        task_type: Type of task

    Returns:
        (compliance_score, violations)
    """
    bridge = create_bridge(config)
    score, violations, _ = bridge.validate_and_feedback(response_text, task_type)
    return score, violations
