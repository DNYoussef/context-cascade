"""
PromptBuilder - THE THIN WAIST CONTRACT

This class implements the stable contract that NEVER changes:
    build(task, task_type) -> (system_prompt, user_prompt)

All optimization happens AROUND this contract, not inside it.
DSPy Level 2 caches compiled prompts keyed by cluster_key.
GlobalMOO optimizes configurations that feed into this builder.

THE CONTRACT:
- Input: task (str), task_type (str)
- Output: (system_prompt, user_prompt) tuple
- This signature NEVER changes
- All other code wraps around this contract

FIX-4 from REMEDIATION-PLAN.md:
- ModeSelector now integrated for runtime mode selection
- Modes are selected based on task context and applied before frame activation
"""

from typing import Tuple, List, Optional
from dataclasses import dataclass
import logging

from .config import FullConfig, VectorCodec, CompressionLevel
from .verix import VerixValidator, VerixStrictness
from .verilingua import FrameRegistry, CognitiveFrame, get_combined_activation_instruction
from .frame_validation_bridge import FrameValidationBridge, ValidationFeedback

# Import ModeSelector for FIX-4
# FIX: Import TelemetryAwareModeSelector for PB-TELEMETRY
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from modes.selector import ModeSelector, TelemetryAwareModeSelector, TaskContext, TaskDomain, select_mode
from modes.library import Mode

logger = logging.getLogger(__name__)


# Task type definitions with base instructions
TASK_TYPE_INSTRUCTIONS = {
    "reasoning": """
You are a precise reasoning assistant. Your responses should:
- Break down complex problems into clear steps
- Show your reasoning chain explicitly
- Validate each step before proceeding
- Acknowledge uncertainty when present
""",

    "coding": """
You are a code assistant. Your responses should:
- Provide working, tested code
- Follow best practices and style guidelines
- Include comments for complex logic
- Consider edge cases and error handling
""",

    "analysis": """
You are an analytical assistant. Your responses should:
- Examine data/information systematically
- Identify patterns and anomalies
- Provide evidence-based conclusions
- Consider alternative interpretations
""",

    "creative": """
You are a creative assistant. Your responses should:
- Generate novel and original content
- Consider multiple creative angles
- Balance creativity with relevance
- Iterate on ideas when helpful
""",

    "conversational": """
You are a helpful conversational assistant. Your responses should:
- Be clear and accessible
- Anticipate follow-up questions
- Provide context when helpful
- Maintain appropriate tone
""",

    "default": """
You are a helpful assistant. Your responses should be:
- Accurate and well-reasoned
- Clear and well-organized
- Appropriately detailed
- Honest about limitations
""",
}


@dataclass
class PromptComponents:
    """
    Internal structure for prompt components.

    Used to organize the parts before assembly.
    """
    base_instruction: str
    frame_activations: str
    verix_requirements: str
    output_format: str
    task_content: str


class PromptBuilder:
    """
    Build prompts with cognitive frame activation and VERIX requirements.

    This is the THIN WAIST - the contract that NEVER changes.
    DSPy Level 2 caches compiled prompts keyed by cluster_key.

    The build() method signature is FROZEN:
        build(task: str, task_type: str) -> Tuple[str, str]

    All optimization happens by:
    1. Changing the FullConfig passed to __init__
    2. Caching compiled prompts by cluster_key
    3. NOT by changing this class's interface

    FIX-4: Now includes ModeSelector for runtime mode selection.
    Modes are selected based on task context and applied before frame activation.

    FIX-5: Now includes FrameValidationBridge for bidirectional VERIX-VERILINGUA integration.
    Validation feedback is used to dynamically adjust frame weights.
    """

    def __init__(
        self,
        config: FullConfig,
        mode_selector: Optional[ModeSelector] = None,
        auto_select_mode: bool = True,
        enable_feedback_loop: bool = True,
    ):
        """
        Initialize builder with configuration.

        Args:
            config: FullConfig specifying frames and VERIX settings
            mode_selector: Optional ModeSelector for runtime mode selection
            auto_select_mode: If True, automatically select mode based on task
            enable_feedback_loop: If True, enable VERIX-VERILINGUA feedback loop (FIX-5)
        """
        self.config = config
        self.active_frames = FrameRegistry.get_active(config.framework)
        self.verix_validator = VerixValidator(config.prompt)
        self._cluster_key = VectorCodec.cluster_key(config)

        # FIX-4: Mode selection integration
        # FIX: Default to TelemetryAwareModeSelector for closed feedback loop (PB-TELEMETRY)
        if mode_selector is None:
            try:
                self.mode_selector = TelemetryAwareModeSelector()
            except Exception:
                # Graceful fallback if telemetry unavailable
                self.mode_selector = ModeSelector()
        else:
            self.mode_selector = mode_selector
        self.auto_select_mode = auto_select_mode
        self._selected_mode: Optional[Mode] = None
        self._mode_applied: bool = False

        # FIX-5: VERIX-VERILINGUA bidirectional bridge
        self.enable_feedback_loop = enable_feedback_loop
        self._validation_bridge: Optional[FrameValidationBridge] = None
        if enable_feedback_loop:
            self._validation_bridge = FrameValidationBridge(config, auto_adjust=True)
        self._last_task_type: str = "default"

    def build(self, task: str, task_type: str) -> Tuple[str, str]:
        """
        THE CONTRACT - NEVER CHANGES

        Build system and user prompts for the given task.

        Args:
            task: The specific task description
            task_type: Category of task (reasoning, coding, analysis, etc.)

        Returns:
            (system_prompt, user_prompt) tuple
        """
        # FIX-5: Track task type for feedback loop
        self._last_task_type = task_type

        # FIX-4: Select and apply mode based on task context
        if self.auto_select_mode and not self._mode_applied:
            self._select_and_apply_mode(task, task_type)

        # Gather components
        components = PromptComponents(
            base_instruction=self._base_instruction(task_type),
            frame_activations=self._frame_activations(),
            verix_requirements=self._verix_requirements(),
            output_format=self._output_format(),
            task_content=task,
        )

        # Assemble prompts
        system_prompt = self._assemble_system_prompt(components)
        user_prompt = self._assemble_user_prompt(components)

        # FIX: Reset mode selection for next build to prevent stale mode reuse (PB-STICKY-MODE)
        self._mode_applied = False

        return system_prompt, user_prompt

    def _select_and_apply_mode(self, task: str, task_type: str) -> None:
        """
        FIX-4: Select optimal mode based on task context and apply configuration.

        Args:
            task: Task description
            task_type: Task category
        """
        try:
            # FIX: Map task_type to domain for accurate mode selection (PB-TASKTYPE)
            task_type_to_domain = {
                "coding": TaskDomain.CODING,
                "research": TaskDomain.RESEARCH,
                "analysis": TaskDomain.ANALYSIS,
                "creative": TaskDomain.CREATIVE,
                "support": TaskDomain.SUPPORT,
                "security": TaskDomain.SECURITY,
                "documentation": TaskDomain.DOCUMENTATION,
                "reasoning": TaskDomain.ANALYSIS,  # Map reasoning to analysis
            }
            domain = task_type_to_domain.get(task_type.lower(), TaskDomain.GENERAL)

            # Create task context for mode selection with explicit domain
            context = TaskContext.from_task(task, domain=domain)

            # Select optimal mode
            self._selected_mode = self.mode_selector.select(context)

            # Apply mode configuration to current config
            self._apply_mode_config(self._selected_mode)

            # Log mode selection for telemetry
            logger.info(
                f"Mode selected: {self._selected_mode.name} "
                f"(type={self._selected_mode.mode_type.value}, "
                f"task_type={task_type})"
            )

            self._mode_applied = True

        except Exception as e:
            logger.warning(f"Mode selection failed: {e}, using default config")
            self._mode_applied = True  # Prevent retry

    def _apply_mode_config(self, mode: Mode) -> None:
        """
        Apply mode configuration to the current config.

        Updates frame activations and other settings based on selected mode.

        Args:
            mode: Selected mode to apply
        """
        # Apply mode's frame configuration (mode.config is a FullConfig)
        mode_config = mode.config

        # Update framework config based on mode
        if mode_config.framework:
            # Update frame toggles
            self.config.framework.evidential = mode_config.framework.evidential
            self.config.framework.aspectual = mode_config.framework.aspectual
            self.config.framework.morphological = mode_config.framework.morphological
            self.config.framework.compositional = mode_config.framework.compositional
            self.config.framework.honorific = mode_config.framework.honorific
            self.config.framework.classifier = mode_config.framework.classifier
            self.config.framework.spatial = mode_config.framework.spatial

            # Refresh active frames
            self.active_frames = FrameRegistry.get_active(self.config.framework)

        # Update prompt config if mode has prompt settings
        if mode_config.prompt:
            self.config.prompt = mode_config.prompt

        # Update cluster key after config change
        self._cluster_key = VectorCodec.cluster_key(self.config)

        logger.debug(f"Applied mode config: frames={[f.name for f in self.active_frames]}")

    def get_selected_mode(self) -> Optional[Mode]:
        """Return the currently selected mode, if any."""
        return self._selected_mode

    def set_mode(self, mode: Mode) -> None:
        """
        Manually set a mode (bypasses auto-selection).

        Args:
            mode: Mode to apply
        """
        self._selected_mode = mode
        self._apply_mode_config(mode)
        self._mode_applied = True

    def validate_response(
        self,
        response_text: str,
        task_type: Optional[str] = None,
    ) -> Tuple[float, List[str], Optional[ValidationFeedback]]:
        """
        FIX-5: Validate a response and feed results back to frame weights.

        This completes the bidirectional loop:
        1. build() generates prompts with frame activations
        2. Model generates response
        3. validate_response() checks VERIX compliance
        4. Feedback adjusts frame weights for future builds

        Args:
            response_text: The model's response to validate
            task_type: Task type (uses last build's type if not provided)

        Returns:
            (compliance_score, violations, feedback)
            feedback is None if feedback loop is disabled
        """
        task_type = task_type or self._last_task_type

        if self._validation_bridge:
            score, violations, feedback = self._validation_bridge.validate_and_feedback(
                response_text, task_type
            )

            # Refresh active frames after potential weight adjustment
            self.active_frames = FrameRegistry.get_active(self.config.framework)

            # Update cluster key if config changed
            self._cluster_key = VectorCodec.cluster_key(self.config)

            logger.info(
                f"Validation complete: score={score:.2f}, "
                f"violations={len(violations)}, feedback_loop=active"
            )

            return score, violations, feedback
        else:
            # Fallback to simple validation without feedback
            from .verix import VerixParser
            parser = VerixParser(self.config.prompt)
            claims = parser.parse(response_text)
            is_valid, violations = self.verix_validator.validate(claims)
            score = self.verix_validator.compliance_score(claims)
            return score, violations, None

    def get_frame_performance_report(self) -> Optional[dict]:
        """
        FIX-5: Get a report on frame performance based on validation feedback.

        Returns:
            Performance report dict, or None if feedback loop is disabled
        """
        if self._validation_bridge:
            return self._validation_bridge.get_frame_performance_report()
        return None

    def get_weight_suggestions(self) -> Optional[dict]:
        """
        FIX-5: Get suggested weight adjustments without applying them.

        Returns:
            Dict of suggested adjustments, or None if feedback loop is disabled
        """
        if self._validation_bridge:
            return self._validation_bridge.get_adjustment_suggestions()
        return None

    def cluster_key(self) -> str:
        """
        Return cluster key for DSPy Level 2 caching.

        Prompts with the same cluster key share cached artifacts.
        """
        return self._cluster_key

    def _base_instruction(self, task_type: str) -> str:
        """
        Get task-type specific base instruction.

        Args:
            task_type: Category of task

        Returns:
            Base instruction string
        """
        normalized_type = task_type.lower().strip()
        return TASK_TYPE_INSTRUCTIONS.get(
            normalized_type,
            TASK_TYPE_INSTRUCTIONS["default"]
        )

    def _frame_activations(self) -> str:
        """
        Build frame activation instructions.

        Returns:
            Combined activation instructions for all active frames
        """
        return get_combined_activation_instruction(self.config.framework)

    def _verix_requirements(self) -> str:
        """
        Build VERIX compliance requirements based on config.

        Returns:
            VERIX requirement instructions
        """
        strictness = self.config.prompt.verix_strictness
        compression = self.config.prompt.compression_level
        require_ground = self.config.prompt.require_ground
        require_confidence = self.config.prompt.require_confidence

        parts = ["# VERIX EPISTEMIC NOTATION REQUIREMENTS", ""]

        # Strictness level instructions
        if strictness == VerixStrictness.STRICT:
            parts.append("""
## STRICT VERIX MODE

You MUST format all claims using full VERIX notation:
[illocution|affect] content [ground:evidence] [conf:N.NN] [state:status]

Required fields:
- illocution: assert, query, direct, commit, or express
- affect: neutral, positive, negative, or uncertain
- content: the actual claim
- ground: source/evidence for the claim
- confidence: numeric 0.00-1.00
- state: provisional, confirmed, or retracted

Example:
[assert|neutral] The function handles null input correctly [ground:traced code path] [conf:0.95] [state:confirmed]
""")
        elif strictness == VerixStrictness.MODERATE:
            parts.append("""
## MODERATE VERIX MODE

Format significant claims using VERIX notation:
[illocution|affect] content [conf:N.NN]

Required fields:
- illocution: assert, query, direct, commit, or express
- affect: neutral, positive, negative, or uncertain
- confidence: numeric 0.00-1.00

Optional but encouraged: ground, state

Example:
[assert|neutral] The race condition occurs in the mutex lock [conf:0.85]
""")
        else:  # RELAXED
            parts.append("""
## RELAXED VERIX MODE

Use VERIX notation for key claims where confidence matters:
[illocution|affect] content

The minimal format marks speech act and stance.
Include confidence when uncertain: [conf:N.NN]

Example:
[assert|uncertain] The bug might be in the event handler [conf:0.60]
""")

        # Ground requirements
        if require_ground:
            parts.append("""
## EVIDENCE REQUIREMENT

All factual claims MUST include evidence/source:
- [ground:code_analysis] - from reading/tracing code
- [ground:documentation] - from official docs
- [ground:user_input] - from user's message
- [ground:inference] - from logical deduction
- [ground:assumption] - explicit assumption (state confidence)
""")

        # Confidence requirements
        if require_confidence:
            parts.append("""
## CONFIDENCE REQUIREMENT

Include confidence values [conf:N.NN] for:
- Uncertain claims (< 0.7 confidence)
- Inferences or assumptions
- Claims about future behavior
- Debugging hypotheses
""")

        # Compression level
        parts.append(f"""
## OUTPUT FORMAT

Compression Level: {compression.name}
""")

        if compression == CompressionLevel.L0_AI_AI:
            parts.append("""
Use compact L0 format for machine processing:
A.85:claim content (Assert, Neutral, 85% confidence)
?.60:question content (Query, Uncertain, 60%)
!+90:instruction (Direct, Positive, 90%)
""")
        elif compression == CompressionLevel.L1_AI_HUMAN:
            parts.append("""
Use annotated L1 format for human inspection:
[assert|neutral] claim content [ground:source] [conf:0.85] [state:confirmed]
""")
        else:  # L2_HUMAN
            parts.append("""
Use natural L2 format for end users:
Write in natural language, but maintain epistemic honesty.
Express uncertainty naturally: "I believe...", "It appears...", "Based on..."
""")

        return "\n".join(parts)

    def _output_format(self) -> str:
        """
        Build output format instructions.

        Returns:
            Output format requirements
        """
        active_frame_names = [f.name for f in self.active_frames]
        frame_list = ", ".join(active_frame_names) if active_frame_names else "none"

        return f"""
# OUTPUT REQUIREMENTS

Active Frames: [{frame_list}]
VERIX Strictness: {self.config.prompt.verix_strictness.name}
Compression: {self.config.prompt.compression_level.name}

Your response MUST:
1. Follow all active cognitive frame requirements
2. Use appropriate VERIX notation for claims
3. Mark evidence sources explicitly
4. Include confidence where relevant
"""

    def _assemble_system_prompt(self, components: PromptComponents) -> str:
        """
        Assemble final system prompt from components.

        Args:
            components: PromptComponents with all parts

        Returns:
            Complete system prompt string
        """
        sections = [
            components.base_instruction.strip(),
            "",
            components.frame_activations.strip() if components.frame_activations else "",
            "",
            components.verix_requirements.strip(),
            "",
            components.output_format.strip(),
        ]

        # Filter empty sections and join
        return "\n".join(s for s in sections if s)

    def _assemble_user_prompt(self, components: PromptComponents) -> str:
        """
        Assemble final user prompt from components.

        Args:
            components: PromptComponents with task content

        Returns:
            Complete user prompt string
        """
        return f"""
# TASK

{components.task_content}

---

Respond following all active cognitive frames and VERIX notation requirements.
"""


class PromptBuilderFactory:
    """
    Factory for creating PromptBuilder instances with common configurations.

    Provides convenient factory methods for standard use cases.
    """

    @staticmethod
    def default() -> PromptBuilder:
        """Create builder with default configuration."""
        return PromptBuilder(FullConfig())

    @staticmethod
    def minimal() -> PromptBuilder:
        """Create builder with minimal frame activation."""
        from .config import MINIMAL_CONFIG
        return PromptBuilder(MINIMAL_CONFIG)

    @staticmethod
    def strict() -> PromptBuilder:
        """Create builder with all frames and strict VERIX."""
        from .config import STRICT_CONFIG
        return PromptBuilder(STRICT_CONFIG)

    @staticmethod
    def from_vector(vector: List[float]) -> PromptBuilder:
        """
        Create builder from configuration vector.

        Used by GlobalMOO to test candidate configurations.

        Args:
            vector: 14-dimensional configuration vector

        Returns:
            PromptBuilder with decoded configuration
        """
        config = VectorCodec.decode(vector)
        return PromptBuilder(config)

    @staticmethod
    def for_task_type(task_type: str) -> PromptBuilder:
        """
        Create builder optimized for a specific task type.

        Adjusts default frames based on task type.

        Args:
            task_type: Category of task

        Returns:
            PromptBuilder with task-appropriate configuration
        """
        from .config import FrameworkConfig, PromptConfig, VerixStrictness

        # Task-specific frame configurations
        task_frames = {
            "reasoning": FrameworkConfig(
                evidential=True,
                aspectual=True,
                morphological=True,
                compositional=True,
                honorific=False,
                classifier=False,
                spatial=False,
            ),
            "coding": FrameworkConfig(
                evidential=True,
                aspectual=True,
                morphological=False,
                compositional=False,
                honorific=False,
                classifier=True,
                spatial=True,
            ),
            "analysis": FrameworkConfig(
                evidential=True,
                aspectual=True,
                morphological=True,
                compositional=False,
                honorific=False,
                classifier=True,
                spatial=False,
            ),
            "creative": FrameworkConfig(
                evidential=False,
                aspectual=False,
                morphological=False,
                compositional=True,
                honorific=True,
                classifier=False,
                spatial=False,
            ),
            "conversational": FrameworkConfig(
                evidential=False,
                aspectual=False,
                morphological=False,
                compositional=False,
                honorific=True,
                classifier=False,
                spatial=False,
            ),
        }

        framework = task_frames.get(
            task_type.lower(),
            FrameworkConfig()  # default
        )

        config = FullConfig(
            framework=framework,
            prompt=PromptConfig(
                verix_strictness=VerixStrictness.MODERATE,
            ),
        )

        return PromptBuilder(config)


def build_prompt(
    task: str,
    task_type: str = "default",
    config: Optional[FullConfig] = None,
) -> Tuple[str, str]:
    """
    Convenience function to build prompts without instantiating builder.

    This is a shortcut for simple use cases. For repeated builds with
    the same config, instantiate PromptBuilder directly.

    Args:
        task: The task description
        task_type: Category of task
        config: Optional configuration (uses default if not provided)

    Returns:
        (system_prompt, user_prompt) tuple
    """
    builder = PromptBuilder(config or FullConfig())
    return builder.build(task, task_type)
