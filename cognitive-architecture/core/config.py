"""
Configuration dataclasses for cognitive architecture.

Classes:
- FrameworkConfig: Frame toggles (evidential, aspectual, etc.)
- PromptConfig: VERIX settings (strictness, compression_level)
- FullConfig: Combined config
- VectorCodec: Stable config <-> vector mapping (14 dimensions)

This module is the FOUNDATION - all other modules depend on it.
"""

from dataclasses import dataclass, field
from typing import List, Tuple
from enum import Enum


class VerixStrictness(Enum):
    """VERIX compliance strictness levels."""
    RELAXED = 0    # Only illocution required
    MODERATE = 1   # Illocution + confidence required
    STRICT = 2     # All fields required


class CompressionLevel(Enum):
    """VERIX output compression levels."""
    L0_AI_AI = 0      # Emoji shorthand (machine-to-machine)
    L1_AI_HUMAN = 1   # Annotated format (human inspector)
    L2_HUMAN = 2      # Natural language (end user, lossy)


@dataclass
class FrameworkConfig:
    """
    Configuration for which cognitive frames are active.

    Each frame adds specific cognitive constraints from natural language:
    - evidential: Turkish -mis/-di (how do you know?)
    - aspectual: Russian pfv/ipfv (complete or ongoing?)
    - morphological: Arabic trilateral roots (semantic decomposition)
    - compositional: German compounding (primitives to compounds)
    - honorific: Japanese keigo (audience calibration)
    - classifier: Chinese measure words (object comparison)
    - spatial: Guugu Yimithirr absolute positioning (navigation)
    """
    evidential: bool = True
    aspectual: bool = True
    morphological: bool = False
    compositional: bool = False
    honorific: bool = False
    classifier: bool = False
    spatial: bool = False

    # Hofstadter recursion control (FR1.2, SYNTH-MECH-001)
    max_frame_depth: int = 3  # Base case: stop at depth 3
    frame_step_policy: str = "simpler"  # Each nested level must be "lighter"

    def active_frames(self) -> List[str]:
        """Return list of active frame names."""
        frames = []
        if self.evidential:
            frames.append("evidential")
        if self.aspectual:
            frames.append("aspectual")
        if self.morphological:
            frames.append("morphological")
        if self.compositional:
            frames.append("compositional")
        if self.honorific:
            frames.append("honorific")
        if self.classifier:
            frames.append("classifier")
        if self.spatial:
            frames.append("spatial")
        return frames

    def frame_count(self) -> int:
        """Return number of active frames."""
        return len(self.active_frames())

    def validate_nesting(self, frame_stack: List[str]) -> bool:
        """
        Ensure frame nesting follows Hofstadter recursion rules.

        Returns True if nesting is valid (within depth limit and follows
        simplification policy).
        """
        if len(frame_stack) > self.max_frame_depth:
            return False  # Hit base case limit

        if self.frame_step_policy == "simpler":
            # Each nested frame should be "lighter" (lower complexity)
            COMPLEXITY_ORDER = [
                "compositional", "morphological", "aspectual",
                "honorific", "classifier", "spatial", "evidential"
            ]
            for i in range(1, len(frame_stack)):
                if frame_stack[i] not in COMPLEXITY_ORDER or frame_stack[i-1] not in COMPLEXITY_ORDER:
                    continue
                prev_complexity = COMPLEXITY_ORDER.index(frame_stack[i-1])
                curr_complexity = COMPLEXITY_ORDER.index(frame_stack[i])
                if curr_complexity <= prev_complexity:
                    return False  # Not simplifying

        return True


@dataclass
class PromptConfig:
    """
    Configuration for VERIX epistemic notation requirements.

    Controls how strict the VERIX compliance checking is and
    what format the output should use.
    """
    verix_strictness: VerixStrictness = VerixStrictness.MODERATE
    compression_level: CompressionLevel = CompressionLevel.L1_AI_HUMAN
    require_ground: bool = True      # Require source/evidence citations
    require_confidence: bool = True  # Require confidence values

    # Hofstadter recursive claim limits (FR2.2)
    max_claim_depth: int = 3  # Maximum nested ground depth
    require_confidence_decrease: bool = True  # Confidence must decrease toward base

    def is_strict(self) -> bool:
        """Check if running in strict mode."""
        return self.verix_strictness == VerixStrictness.STRICT

    def is_relaxed(self) -> bool:
        """Check if running in relaxed mode."""
        return self.verix_strictness == VerixStrictness.RELAXED


@dataclass
class FullConfig:
    """
    Complete configuration combining framework and prompt settings.

    This is the primary config object passed to all components.
    """
    framework: FrameworkConfig = field(default_factory=FrameworkConfig)
    prompt: PromptConfig = field(default_factory=PromptConfig)

    def summary(self) -> str:
        """Return human-readable config summary."""
        frames = ", ".join(self.framework.active_frames()) or "none"
        return (
            f"Frames: [{frames}] | "
            f"VERIX: {self.prompt.verix_strictness.name} | "
            f"Compression: {self.prompt.compression_level.name}"
        )


class VectorCodec:
    """
    Stable mapping between FullConfig and float vectors.

    Vector Format (14 dimensions):
    [0-6]: Frame toggles (evidential, aspectual, morphological,
           compositional, honorific, classifier, spatial)
    [7]: verix_strictness (0, 1, 2)
    [8]: compression_level (0, 1, 2)
    [9]: require_ground (0, 1)
    [10]: require_confidence (0, 1)
    [11-13]: Reserved for expansion

    This codec is STABLE - the mapping NEVER changes once deployed.
    GlobalMOO optimization operates on these vectors.
    """

    VECTOR_SIZE = 14

    # Frame indices (0-6)
    IDX_EVIDENTIAL = 0
    IDX_ASPECTUAL = 1
    IDX_MORPHOLOGICAL = 2
    IDX_COMPOSITIONAL = 3
    IDX_HONORIFIC = 4
    IDX_CLASSIFIER = 5
    IDX_SPATIAL = 6

    # Prompt config indices (7-10)
    IDX_VERIX_STRICTNESS = 7
    IDX_COMPRESSION_LEVEL = 8
    IDX_REQUIRE_GROUND = 9
    IDX_REQUIRE_CONFIDENCE = 10

    # Reserved indices (11-13)
    IDX_RESERVED_1 = 11
    IDX_RESERVED_2 = 12
    IDX_RESERVED_3 = 13

    @staticmethod
    def encode(config: FullConfig) -> List[float]:
        """
        Convert FullConfig to 14-dimensional float vector.

        Args:
            config: The configuration to encode

        Returns:
            List of 14 floats representing the configuration
        """
        vector = [0.0] * VectorCodec.VECTOR_SIZE

        # Encode framework config (boolean -> 0.0 or 1.0)
        vector[VectorCodec.IDX_EVIDENTIAL] = 1.0 if config.framework.evidential else 0.0
        vector[VectorCodec.IDX_ASPECTUAL] = 1.0 if config.framework.aspectual else 0.0
        vector[VectorCodec.IDX_MORPHOLOGICAL] = 1.0 if config.framework.morphological else 0.0
        vector[VectorCodec.IDX_COMPOSITIONAL] = 1.0 if config.framework.compositional else 0.0
        vector[VectorCodec.IDX_HONORIFIC] = 1.0 if config.framework.honorific else 0.0
        vector[VectorCodec.IDX_CLASSIFIER] = 1.0 if config.framework.classifier else 0.0
        vector[VectorCodec.IDX_SPATIAL] = 1.0 if config.framework.spatial else 0.0

        # Encode prompt config (enum -> float value)
        vector[VectorCodec.IDX_VERIX_STRICTNESS] = float(config.prompt.verix_strictness.value)
        vector[VectorCodec.IDX_COMPRESSION_LEVEL] = float(config.prompt.compression_level.value)
        vector[VectorCodec.IDX_REQUIRE_GROUND] = 1.0 if config.prompt.require_ground else 0.0
        vector[VectorCodec.IDX_REQUIRE_CONFIDENCE] = 1.0 if config.prompt.require_confidence else 0.0

        # Reserved slots remain 0.0

        return vector

    @staticmethod
    def decode(vector: List[float]) -> FullConfig:
        """
        Convert 14-dimensional float vector to FullConfig.

        Args:
            vector: List of 14 floats

        Returns:
            FullConfig reconstructed from vector

        Raises:
            ValueError: If vector is wrong size or contains invalid values
        """
        if len(vector) != VectorCodec.VECTOR_SIZE:
            raise ValueError(
                f"Vector must have {VectorCodec.VECTOR_SIZE} dimensions, "
                f"got {len(vector)}"
            )

        # Decode framework config (threshold at 0.5 for booleans)
        framework = FrameworkConfig(
            evidential=vector[VectorCodec.IDX_EVIDENTIAL] >= 0.5,
            aspectual=vector[VectorCodec.IDX_ASPECTUAL] >= 0.5,
            morphological=vector[VectorCodec.IDX_MORPHOLOGICAL] >= 0.5,
            compositional=vector[VectorCodec.IDX_COMPOSITIONAL] >= 0.5,
            honorific=vector[VectorCodec.IDX_HONORIFIC] >= 0.5,
            classifier=vector[VectorCodec.IDX_CLASSIFIER] >= 0.5,
            spatial=vector[VectorCodec.IDX_SPATIAL] >= 0.5,
        )

        # Decode prompt config (round to nearest enum value)
        strictness_val = int(round(vector[VectorCodec.IDX_VERIX_STRICTNESS]))
        strictness_val = max(0, min(2, strictness_val))  # Clamp to valid range

        compression_val = int(round(vector[VectorCodec.IDX_COMPRESSION_LEVEL]))
        compression_val = max(0, min(2, compression_val))  # Clamp to valid range

        prompt = PromptConfig(
            verix_strictness=VerixStrictness(strictness_val),
            compression_level=CompressionLevel(compression_val),
            require_ground=vector[VectorCodec.IDX_REQUIRE_GROUND] >= 0.5,
            require_confidence=vector[VectorCodec.IDX_REQUIRE_CONFIDENCE] >= 0.5,
        )

        return FullConfig(framework=framework, prompt=prompt)

    @staticmethod
    def cluster_key(config: FullConfig) -> str:
        """
        Generate cluster key for DSPy Level 2 caching.

        The cluster key identifies a unique configuration "type" that
        should share compiled prompts. Two configs with the same
        cluster key will use the same cached DSPy artifacts.

        Format: "frames:{sorted_frames}|strict:{0-2}|compress:{0-2}"

        Args:
            config: Configuration to generate key for

        Returns:
            String key for cache lookup
        """
        frames = sorted(config.framework.active_frames())
        frames_str = "+".join(frames) if frames else "none"

        return (
            f"frames:{frames_str}|"
            f"strict:{config.prompt.verix_strictness.value}|"
            f"compress:{config.prompt.compression_level.value}"
        )

    @staticmethod
    def distance(v1: List[float], v2: List[float]) -> float:
        """
        Calculate Euclidean distance between two config vectors.

        Useful for finding similar configurations in the Pareto frontier.

        Args:
            v1: First vector
            v2: Second vector

        Returns:
            Euclidean distance
        """
        if len(v1) != len(v2):
            raise ValueError("Vectors must have same length")

        squared_diff_sum = sum((a - b) ** 2 for a, b in zip(v1, v2))
        return squared_diff_sum ** 0.5

    @staticmethod
    def interpolate(v1: List[float], v2: List[float], t: float) -> List[float]:
        """
        Linear interpolation between two config vectors.

        Useful for exploring the configuration space between
        two known good configurations.

        Args:
            v1: Start vector
            v2: End vector
            t: Interpolation factor (0.0 = v1, 1.0 = v2)

        Returns:
            Interpolated vector
        """
        if len(v1) != len(v2):
            raise ValueError("Vectors must have same length")

        t = max(0.0, min(1.0, t))  # Clamp to [0, 1]
        return [a + t * (b - a) for a, b in zip(v1, v2)]


# Default configurations for common use cases
DEFAULT_CONFIG = FullConfig()

MINIMAL_CONFIG = FullConfig(
    framework=FrameworkConfig(
        evidential=True,
        aspectual=False,
        morphological=False,
        compositional=False,
        honorific=False,
        classifier=False,
        spatial=False,
    ),
    prompt=PromptConfig(
        verix_strictness=VerixStrictness.RELAXED,
        compression_level=CompressionLevel.L2_HUMAN,
        require_ground=False,
        require_confidence=False,
    ),
)

STRICT_CONFIG = FullConfig(
    framework=FrameworkConfig(
        evidential=True,
        aspectual=True,
        morphological=True,
        compositional=True,
        honorific=True,
        classifier=True,
        spatial=True,
    ),
    prompt=PromptConfig(
        verix_strictness=VerixStrictness.STRICT,
        compression_level=CompressionLevel.L0_AI_AI,
        require_ground=True,
        require_confidence=True,
    ),
)
