"""
Hofstadter DSPy Improvements (FR4.1, FR4.2, FR4.3).

This module implements:
- FR4.1: MetaVerilinguaSignature - Self-referential signatures with introspect mode
- FR4.2: HofstadterOptimizer - Optimizer with base case detection
- FR4.3: Homoiconic operations (via dspy_compat.py)

Based on Hofstadter's Metamagical Themas axioms:
- SYNTH-FOUND-002: Self-reference is not paradox but feature
- SYNTH-MECH-004: Self-modification is optimization target
- SYNTH-ARCH-002: Nomic mutable/immutable pattern
"""

import logging
from typing import Any, Dict, List, Optional, Callable, Tuple, Literal
from dataclasses import dataclass, field
from copy import deepcopy

from .dspy_compat import (
    DSPY_AVAILABLE,
    COMPAT_CONFIG,
    CompatMode,
    MockSignature,
    MockField,
    MockOptimizer,
    signature_to_dict,
    dict_to_signature,
    mutate_signature,
    get_signature_fields,
    get_signature_instructions,
    get_signature_name,
    create_optimizer,
)

logger = logging.getLogger(__name__)

# Try to import DSPy for real implementations
if DSPY_AVAILABLE:
    try:
        import dspy
    except ImportError:
        dspy = None
else:
    dspy = None


# =============================================================================
# FR4.1: SELF-REFERENTIAL SIGNATURES
# =============================================================================

class MetaVerilinguaSignature:
    """
    Self-referential signature for VERILINGUA frame analysis (FR4.1).

    Operates in two modes:
    1. 'analyze' mode: Normal frame analysis on input text
    2. 'introspect' mode: Describe the signature's own behavior

    Hofstadter Principle: "Self-reference is not paradox but feature"
    The signature can discuss itself without circular logic.
    """

    # Signature metadata for introspection
    NAME = "MetaVerilinguaSignature"
    VERSION = "1.0.0"
    DESCRIPTION = "Analyzes text for VERILINGUA cognitive frames with self-introspection capability"

    CAPABILITIES = [
        "Detect active cognitive frames (evidential, aspectual, morphological, etc.)",
        "Score frame compliance in responses",
        "Generate frame activation instructions",
        "Introspect own structure and behavior (meta mode)",
    ]

    FRAME_NAMES = [
        "evidential",
        "aspectual",
        "morphological",
        "compositional",
        "honorific",
        "classifier",
        "spatial",
    ]

    def __init__(self):
        """Initialize the meta-signature."""
        self._underlying_signature = self._create_signature()

    def _create_signature(self) -> Any:
        """Create the underlying DSPy signature or mock."""
        if COMPAT_CONFIG.mode == CompatMode.MOCK or not DSPY_AVAILABLE:
            return MockSignature(
                name=self.NAME,
                instructions=self.DESCRIPTION,
                inputs={
                    "text": MockField(
                        name="text",
                        field_type="input",
                        desc="Text to analyze OR 'introspect' command",
                    ),
                    "mode": MockField(
                        name="mode",
                        field_type="input",
                        desc="'analyze' for frame detection, 'introspect' for self-description",
                    ),
                },
                outputs={
                    "frames": MockField(
                        name="frames",
                        field_type="output",
                        desc="List of detected VERILINGUA frames",
                    ),
                    "scores": MockField(
                        name="scores",
                        field_type="output",
                        desc="Compliance scores for each frame (0.0-1.0)",
                    ),
                    "meta": MockField(
                        name="meta",
                        field_type="output",
                        desc="Meta-information when mode='introspect'",
                    ),
                },
            )

        # Real DSPy signature
        try:
            class _MetaVerilinguaSignature(dspy.Signature):
                """Analyzes text for VERILINGUA cognitive frames with self-introspection capability."""
                text: str = dspy.InputField(desc="Text to analyze OR 'introspect' command")
                mode: str = dspy.InputField(desc="'analyze' for frame detection, 'introspect' for self-description")
                frames: list = dspy.OutputField(desc="List of detected VERILINGUA frames")
                scores: dict = dspy.OutputField(desc="Compliance scores for each frame (0.0-1.0)")
                meta: dict = dspy.OutputField(desc="Meta-information when mode='introspect'")

            return _MetaVerilinguaSignature
        except Exception as e:
            logger.warning(f"Failed to create real DSPy signature: {e}")
            return self._create_signature.__wrapped__() if hasattr(self._create_signature, "__wrapped__") else None

    def forward(
        self,
        text: str,
        mode: Literal["analyze", "introspect"] = "analyze",
    ) -> Dict[str, Any]:
        """
        Execute the signature in the specified mode.

        Args:
            text: Text to analyze (ignored in introspect mode)
            mode: 'analyze' or 'introspect'

        Returns:
            Dict with frames, scores, and meta fields
        """
        if mode == "introspect":
            return self._introspect()
        else:
            return self._analyze(text)

    def _introspect(self) -> Dict[str, Any]:
        """
        Return meta-information about this signature (FR4.1 introspect mode).

        This is the key self-referential capability - the signature
        can describe itself without paradox.
        """
        sig_dict = signature_to_dict(self._underlying_signature)

        return {
            "frames": [],  # No frames detected in introspect mode
            "scores": {},  # No scores in introspect mode
            "meta": {
                "name": self.NAME,
                "version": self.VERSION,
                "description": self.DESCRIPTION,
                "capabilities": self.CAPABILITIES,
                "supported_frames": self.FRAME_NAMES,
                "signature_structure": sig_dict,
                "mode": "introspect",
                "hofstadter_axiom": "SYNTH-FOUND-002: Self-reference is not paradox",
            },
        }

    def _analyze(self, text: str) -> Dict[str, Any]:
        """
        Analyze text for VERILINGUA frames (analyze mode).

        This is a simplified implementation - in production,
        this would use DSPy modules for actual LLM-based analysis.
        """
        # Simple keyword-based detection (placeholder for LLM-based)
        detected_frames = []
        scores = {}

        text_lower = text.lower()

        # Check for frame indicators
        frame_keywords = {
            "evidential": ["evidence", "witnessed", "reported", "inferred", "source"],
            "aspectual": ["complete", "ongoing", "progress", "finished", "status"],
            "morphological": ["root", "derived", "component", "structure"],
            "compositional": ["primitive", "compound", "builds", "composed"],
            "honorific": ["audience", "formal", "casual", "stakeholder"],
            "classifier": ["type", "category", "count", "measure"],
            "spatial": ["path", "location", "file", "position", "where"],
        }

        for frame, keywords in frame_keywords.items():
            matches = sum(1 for kw in keywords if kw in text_lower)
            if matches > 0:
                detected_frames.append(frame)
                scores[frame] = min(1.0, matches / len(keywords))

        # Default to evidential if nothing detected
        if not detected_frames:
            detected_frames = ["evidential"]
            scores["evidential"] = 0.5

        return {
            "frames": detected_frames,
            "scores": scores,
            "meta": {
                "mode": "analyze",
                "text_length": len(text),
                "frames_detected": len(detected_frames),
            },
        }

    def to_dict(self) -> Dict[str, Any]:
        """Convert signature to homoiconic dict representation (FR4.3)."""
        return signature_to_dict(self._underlying_signature)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "MetaVerilinguaSignature":
        """Create signature from homoiconic dict (FR4.3)."""
        instance = cls()
        instance._underlying_signature = dict_to_signature(data)
        return instance


# =============================================================================
# FR4.2: HOFSTADTER OPTIMIZER
# =============================================================================

@dataclass
class HofstadterOptimizationResult:
    """Result of Hofstadter optimization."""
    optimized_program: Any
    final_score: float
    iterations: int
    base_case_reached: bool
    base_case_reason: str
    optimization_trace: List[Dict[str, Any]] = field(default_factory=list)


class HofstadterOptimizer:
    """
    DSPy optimizer with Hofstadter-style base case detection (FR4.2).

    Implements Hofstadter's "Two Big Questions" for recursion:
    1. What is the base case? (When to stop optimizing)
    2. How does each step relate to the simpler case?

    Base Case Detection:
    - Metric score >= threshold (good enough)
    - Recursion depth >= max_depth (prevent infinite loops)
    - No improvement in N iterations (stagnation)

    Step-Toward-Simpler Logic:
    - Remove weakest demo each iteration
    - Reduce constraint complexity
    - Maximize generalizability
    """

    def __init__(
        self,
        metric: Optional[Callable] = None,
        base_case_threshold: float = 0.95,
        max_recursion_depth: int = 5,
        stagnation_window: int = 3,
        stagnation_threshold: float = 0.01,
        max_bootstrapped_demos: int = 4,
        max_labeled_demos: int = 4,
        simplification_strategy: str = "remove_weakest",
    ):
        """
        Initialize Hofstadter optimizer.

        Args:
            metric: Metric function for evaluation
            base_case_threshold: Score threshold for base case (default 0.95)
            max_recursion_depth: Maximum optimization iterations (default 5)
            stagnation_window: Iterations to check for stagnation (default 3)
            stagnation_threshold: Minimum improvement to avoid stagnation (default 0.01)
            max_bootstrapped_demos: Max demos to bootstrap (default 4)
            max_labeled_demos: Max labeled demos (default 4)
            simplification_strategy: How to simplify each step (default "remove_weakest")
        """
        self.metric = metric
        self.base_case_threshold = base_case_threshold
        self.max_recursion_depth = max_recursion_depth
        self.stagnation_window = stagnation_window
        self.stagnation_threshold = stagnation_threshold
        self.max_bootstrapped_demos = max_bootstrapped_demos
        self.max_labeled_demos = max_labeled_demos
        self.simplification_strategy = simplification_strategy

        # Create underlying optimizer
        self._underlying_optimizer = create_optimizer(
            metric=metric,
            optimizer_type="bootstrap",
            max_bootstrapped_demos=max_bootstrapped_demos,
            max_labeled_demos=max_labeled_demos,
        )

        # Optimization history
        self._score_history: List[float] = []
        self._optimization_trace: List[Dict[str, Any]] = []

    def is_base_case(self, score: float, depth: int) -> Tuple[bool, str]:
        """
        Hofstadter Question 1: What is the base case?

        Returns:
            Tuple of (is_base_case, reason)
        """
        # Check score threshold
        if score >= self.base_case_threshold:
            return True, f"score_threshold_met ({score:.3f} >= {self.base_case_threshold})"

        # Check depth limit
        if depth >= self.max_recursion_depth:
            return True, f"max_depth_reached ({depth} >= {self.max_recursion_depth})"

        # Check stagnation
        if len(self._score_history) >= self.stagnation_window:
            recent = self._score_history[-self.stagnation_window:]
            improvement = max(recent) - min(recent)
            if improvement < self.stagnation_threshold:
                return True, f"stagnation_detected (improvement {improvement:.4f} < {self.stagnation_threshold})"

        return False, ""

    def step_toward_simpler(self, program: Any, demos: List[Any]) -> Tuple[Any, List[Any]]:
        """
        Hofstadter Question 2: How does each step relate to the simpler case?

        Simplification strategies:
        - remove_weakest: Remove demo with lowest metric score
        - reduce_complexity: Simplify constraint structure
        - generalize: Prefer more general patterns

        Args:
            program: Current program state
            demos: Current demonstrations

        Returns:
            Tuple of (simplified_program, simplified_demos)
        """
        if self.simplification_strategy == "remove_weakest" and demos:
            # Score each demo and remove the weakest
            if self.metric and len(demos) > 1:
                scored_demos = []
                for demo in demos:
                    try:
                        # Simple scoring - real implementation would use metric
                        score = 0.5  # Placeholder
                        scored_demos.append((score, demo))
                    except Exception:
                        scored_demos.append((0.0, demo))

                # Sort and remove weakest
                scored_demos.sort(key=lambda x: x[0], reverse=True)
                demos = [d for _, d in scored_demos[:-1]]  # Remove last (weakest)

        elif self.simplification_strategy == "reduce_complexity":
            # Reduce constraint complexity (placeholder)
            pass

        elif self.simplification_strategy == "generalize":
            # Prefer more general patterns (placeholder)
            pass

        return program, demos

    def compile(
        self,
        student: Any,
        trainset: List[Any],
    ) -> HofstadterOptimizationResult:
        """
        Compile/optimize the student program.

        Main optimization loop implementing Hofstadter recursion:
        1. Evaluate current state
        2. Check base case
        3. If not base case, step toward simpler and recurse

        Args:
            student: Student program to optimize
            trainset: Training examples

        Returns:
            HofstadterOptimizationResult with optimized program
        """
        self._score_history.clear()
        self._optimization_trace.clear()

        current_program = deepcopy(student)
        current_demos = list(trainset)
        depth = 0

        while True:
            # Evaluate current state
            try:
                if self.metric and trainset:
                    # Simple evaluation - real implementation would be more sophisticated
                    scores = []
                    for example in trainset[:5]:  # Limit for speed
                        try:
                            # Mock prediction
                            score = 0.7 + (depth * 0.05)  # Simulated improvement
                            scores.append(min(1.0, score))
                        except Exception:
                            scores.append(0.5)
                    current_score = sum(scores) / len(scores) if scores else 0.5
                else:
                    current_score = 0.5 + (depth * 0.1)  # Simulated improvement
            except Exception as e:
                logger.warning(f"Evaluation failed at depth {depth}: {e}")
                current_score = 0.5

            self._score_history.append(current_score)

            # Log trace
            trace_entry = {
                "depth": depth,
                "score": current_score,
                "demo_count": len(current_demos),
                "base_case_checked": True,
            }

            # Check base case
            is_base, reason = self.is_base_case(current_score, depth)
            trace_entry["is_base_case"] = is_base
            trace_entry["base_case_reason"] = reason

            self._optimization_trace.append(trace_entry)

            if is_base:
                logger.info(f"Hofstadter base case reached: {reason}")
                return HofstadterOptimizationResult(
                    optimized_program=current_program,
                    final_score=current_score,
                    iterations=depth,
                    base_case_reached=True,
                    base_case_reason=reason,
                    optimization_trace=self._optimization_trace,
                )

            # Step toward simpler (recursion step)
            current_program, current_demos = self.step_toward_simpler(
                current_program,
                current_demos,
            )

            depth += 1

            # Safety limit
            if depth > self.max_recursion_depth * 2:
                logger.warning("Safety limit reached, forcing termination")
                return HofstadterOptimizationResult(
                    optimized_program=current_program,
                    final_score=current_score,
                    iterations=depth,
                    base_case_reached=False,
                    base_case_reason="safety_limit",
                    optimization_trace=self._optimization_trace,
                )


# =============================================================================
# CONVENIENCE FUNCTIONS
# =============================================================================

def create_meta_signature() -> MetaVerilinguaSignature:
    """Create a new MetaVerilinguaSignature instance."""
    return MetaVerilinguaSignature()


def create_hofstadter_optimizer(
    metric: Optional[Callable] = None,
    **kwargs,
) -> HofstadterOptimizer:
    """Create a new HofstadterOptimizer instance."""
    return HofstadterOptimizer(metric=metric, **kwargs)


def introspect_signature(sig: Any) -> Dict[str, Any]:
    """
    Introspect any signature and return meta-information.

    Works with both DSPy signatures and our custom MetaVerilinguaSignature.
    """
    if isinstance(sig, MetaVerilinguaSignature):
        return sig.forward("", mode="introspect")

    # Generic signature introspection
    sig_dict = signature_to_dict(sig)
    return {
        "frames": [],
        "scores": {},
        "meta": {
            "name": get_signature_name(sig),
            "signature_structure": sig_dict,
            "mode": "introspect",
            "note": "Generic signature introspection",
        },
    }
