# Prompt-Architect Cognitive Architecture Integration

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



**Version**: 2.3.0
**Purpose**: Integrate VERIX epistemic notation, VERILINGUA cognitive frames, DSPy optimization, and GlobalMOO multi-objective optimization into prompt-architect.

## Overview

This addendum enhances prompt-architect to:
1. Output prompts with VERIX epistemic markers
2. Use VERILINGUA frames for cognitive precision
3. Apply DSPy optimization to prompt refinement
4. Use GlobalMOO for multi-objective prompt optimization

## VERIX Integration

### All Prompt Outputs Include Epistemic Markers

```yaml
# Every claim in generated prompts includes:
epistemic_markers:
  ground: "[ground:{source}]"  # Where the claim comes from
  confidence: "[conf:{0.0-1.0}]"  # Certainty level
  illocution: "[assert|query|propose]"  # Type of speech act
  state: "[hypothetical|actual|confirmed]"  # Epistemic state
```

### Example: VERIX-Enhanced Prompt Output

**Before (baseline)**:
```
Create a REST API for user authentication. Use JWT tokens.
The endpoint should handle login and registration.
```

**After (VERIX-enhanced)**:
```
## Task
[assert|emphatic] Create a REST API for user authentication [ground:requirements.md] [conf:0.95]

## Requirements
- [assert|neutral] Use JWT tokens for session management [ground:security-policy.md] [conf:0.90]
- [propose|neutral] Consider refresh token rotation [ground:OWASP] [conf:0.85]

## Expected Behavior
- [assert|neutral] Login endpoint returns JWT [ground:api-spec.md] [conf:0.95] [state:confirmed]
- [query|neutral] Should registration require email verification? [conf:0.70] [state:needs_clarification]
```

### Integration Points

```python
# In prompt-architect Phase 5: Add VERIX enrichment
def enrich_with_verix(prompt: str, verix_config: VerixConfig) -> str:
    """
    Post-process prompt to add epistemic markers.

    Args:
        prompt: The refined prompt from Phase 4
        verix_config: VERIX configuration (strictness, required markers)

    Returns:
        VERIX-enhanced prompt with ground, confidence, illocution markers
    """
    from cognitive_architecture.core.verix import VerixParser, VerixAnnotator

    parser = VerixParser()
    annotator = VerixAnnotator(strictness=verix_config.strictness)

    # Parse claims from prompt
    claims = parser.parse(prompt)

    # Add epistemic markers
    annotated_claims = []
    for claim in claims:
        # Ground sources (where possible)
        if claim.requires_grounding:
            claim.ground = infer_ground(claim.content)

        # Add confidence based on claim type
        claim.confidence = estimate_confidence(claim)

        annotated_claims.append(claim)

    return annotator.render(annotated_claims)
```

## VERILINGUA Integration

### Frame Selection for Prompt Types

| Prompt Type | Primary Frame | Activation |
|-------------|---------------|------------|
| Research prompts | Evidential (Turkish) | Source verification mode |
| Build prompts | Aspectual (Russian) | Completion tracking mode |
| Analysis prompts | Morphological (Arabic) | Semantic precision mode |
| Documentation prompts | Compositional (German) | Structure building mode |
| User-facing prompts | Honorific (Japanese) | Audience calibration mode |

### Frame Activation in Prompt Output

```markdown
## Cognitive Frame Activation

### For Research Prompts (Evidential Frame)
Kaynak dogrulama modu etkin.
Every claim requires source verification:
- [DIRECT] Personally verified claims
- [INFERRED] Claims derived from evidence
- [REPORTED] Claims from documentation

### For Build Prompts (Aspectual Frame)
Sostoyanie zavershenia aktivirovano.
Track completion state for each step:
- [SV] Completed - fully finished
- [NSV] In progress - ongoing work
- [BLOCKED] Waiting - dependencies pending
```

### Integration Points

```python
# In prompt-architect Phase 0.5: Add frame selection
def select_cognitive_frame(intent: AnalyzedIntent) -> CognitiveFrame:
    """
    Select optimal cognitive frame based on prompt intent.

    Uses VERILINGUA frame registry from cognitive architecture.
    """
    from cognitive_architecture.core.verilingua import FrameRegistry

    # Map intent categories to frames
    frame_mapping = {
        "research": "evidential",
        "analysis": "morphological",
        "build": "aspectual",
        "documentation": "compositional",
        "user_facing": "honorific",
    }

    frame_name = frame_mapping.get(intent.category, "evidential")
    return FrameRegistry.get(frame_name)
```

## DSPy Integration

### Prompt Optimization as DSPy Module

```python
from dspy import ChainOfThought, Signature, InputField, OutputField

class PromptOptimizationSignature(Signature):
    """Optimize a prompt using evidence-based techniques."""

    original_prompt: str = InputField(desc="The prompt to optimize")
    task_type: str = InputField(desc="Type of task (research, build, analysis)")
    constraints: list = InputField(desc="Optimization constraints")

    optimized_prompt: str = OutputField(desc="The optimized prompt with VERIX markers")
    techniques_applied: list = OutputField(desc="Evidence-based techniques used")
    quality_scores: dict = OutputField(desc="Clarity, completeness, precision scores")
    verix_compliance: float = OutputField(desc="VERIX marker compliance score")
    frame_alignment: float = OutputField(desc="VERILINGUA frame alignment score")


class PromptOptimizerDSPy(ChainOfThought):
    """DSPy module for prompt optimization with cognitive architecture."""

    def __init__(self):
        super().__init__(signature=PromptOptimizationSignature)
        self.verix_parser = VerixParser()
        self.frame_registry = FrameRegistry

    def forward(self, original_prompt: str, task_type: str, constraints: list):
        # Run chain-of-thought optimization
        result = super().forward(
            original_prompt=original_prompt,
            task_type=task_type,
            constraints=constraints
        )

        # Validate VERIX compliance
        claims = self.verix_parser.parse(result.optimized_prompt)
        result.verix_compliance = self._score_verix(claims)

        # Validate frame alignment
        frame = self.frame_registry.get(task_type)
        result.frame_alignment = frame.score_response(result.optimized_prompt)

        return result
```

### DSPy Optimization Loop

```python
# After Phase 7 (validation), run DSPy optimization
def dspy_optimize_prompt(prompt: str, config: OptimizationConfig) -> OptimizedPrompt:
    """
    Use DSPy to find optimal prompt configuration.

    Optimizes for:
    - Clarity score (0-1)
    - VERIX compliance (0-1)
    - Frame alignment (0-1)
    - Token efficiency (0-1)
    """
    from dspy import Teleprompter

    optimizer = PromptOptimizerDSPy()

    # Train on examples
    teleprompter = Teleprompter(
        metric=lambda pred, gold: (
            0.3 * pred.quality_scores["clarity"] +
            0.3 * pred.verix_compliance +
            0.3 * pred.frame_alignment +
            0.1 * (1.0 - pred.token_count / config.max_tokens)
        )
    )

    optimized = teleprompter.compile(optimizer, trainset=config.examples)

    return optimized(prompt, config.task_type, config.constraints)
```

## GlobalMOO Integration

### Multi-Objective Prompt Optimization

```yaml
project_id: prompt-architect-optimization
objectives:
  - name: clarity
    description: Prompt clarity score (no ambiguity)
    direction: maximize
    weight: 0.25

  - name: completeness
    description: All required elements present
    direction: maximize
    weight: 0.25

  - name: verix_compliance
    description: VERIX epistemic marker coverage
    direction: maximize
    weight: 0.25

  - name: frame_alignment
    description: VERILINGUA frame activation success
    direction: maximize
    weight: 0.15

  - name: token_efficiency
    description: Tokens used vs target
    direction: minimize
    weight: 0.10

parameters:
  - name: verix_strictness
    type: ordinal
    values: [relaxed, moderate, strict]

  - name: frame_selection
    type: categorical
    values: [evidential, aspectual, morphological, compositional, honorific, classifier, spatial]

  - name: compression_level
    type: ordinal
    values: [L0_full, L1_compressed, L2_minimal]

  - name: technique_set
    type: categorical
    values: [self_consistency, program_of_thought, plan_and_solve, few_shot, chain_of_thought]
```

### Integration Points

```python
# In prompt-architect Phase 8: Track with GlobalMOO
def track_optimization(prompt: str, outcomes: dict) -> None:
    """
    Record prompt optimization outcome for GlobalMOO learning.
    """
    from cognitive_architecture.optimization.globalmoo_client import GlobalMOOClient

    client = GlobalMOOClient()

    client.record_outcome(
        project_id="prompt-architect-optimization",
        config_vector={
            "verix_strictness": outcomes["verix_strictness"],
            "frame_selection": outcomes["frame"],
            "compression_level": outcomes["compression"],
            "technique_set": outcomes["techniques"],
        },
        outcomes={
            "clarity": outcomes["clarity_score"],
            "completeness": outcomes["completeness_score"],
            "verix_compliance": outcomes["verix_score"],
            "frame_alignment": outcomes["frame_score"],
            "token_efficiency": 1.0 - (outcomes["tokens"] / 1000),
        }
    )


def get_optimal_config(task_type: str) -> dict:
    """
    Get optimal prompt configuration from GlobalMOO Pareto frontier.
    """
    from cognitive_architecture.optimization.globalmoo_client import GlobalMOOClient

    client = GlobalMOOClient()

    # Get Pareto-optimal configurations
    frontier = client.get_pareto_frontier("prompt-architect-optimization")

    # Select configuration based on task type
    if task_type == "research":
        # Prioritize VERIX compliance for research
        return frontier.select_by_objective("verix_compliance")
    elif task_type == "build":
        # Prioritize clarity for build tasks
        return frontier.select_by_objective("clarity")
    else:
        # Use balanced configuration
        return frontier.select_balanced()
```

## Enhanced Phase Flow

```
Phase 0: Expertise Loading
    |
    v
Phase 0.5: Cognitive Frame Selection (NEW)
    ├── Analyze intent category
    ├── Select VERILINGUA frame
    └── Prepare frame activation phrase
    |
    v
Phase 1-4: Core Optimization (existing)
    |
    v
Phase 5: VERIX Enrichment (NEW)
    ├── Parse claims from prompt
    ├── Add epistemic markers
    └── Validate ground and confidence
    |
    v
Phase 6-7: Validation (existing)
    |
    v
Phase 8: GlobalMOO Tracking (NEW)
    ├── Record outcomes
    ├── Update Pareto frontier
    └── Learn optimal configurations
    |
    v
Phase 9: DSPy Optimization Loop (NEW)
    ├── Run teleprompter optimization
    ├── Measure improvement delta
    └── Store optimized prompt
```

## Quality Gates

### VERIX Compliance Gate

```yaml
verix_quality_gate:
  minimum_ground_coverage: 0.70  # 70% claims must have grounds
  minimum_confidence_coverage: 0.80  # 80% claims must have confidence
  allowed_ungrounded: ["queries", "proposals"]  # These can skip grounding
```

### Frame Alignment Gate

```yaml
frame_quality_gate:
  minimum_frame_score: 0.60  # 60% frame marker coverage
  required_activation: true  # Frame activation phrase must be present
  multilingual_required: false  # Optional for v2.3
```

### GlobalMOO Convergence Gate

```yaml
moo_quality_gate:
  minimum_iterations: 50  # At least 50 optimization iterations
  convergence_threshold: 0.01  # Pareto frontier stable
  pareto_points_required: 5  # At least 5 points on frontier
```

## Memory Integration

### Store Optimized Prompts

```javascript
// Store in memory-mcp for learning
await mcp__memory_mcp__memory_store({
  text: `Prompt optimization result. Task: ${taskType}. Clarity: ${clarity}. VERIX: ${verixScore}. Frame: ${frameScore}.`,
  metadata: {
    key: `prompt-architect/optimizations/${promptId}`,
    namespace: "foundry-optimization",
    layer: "long-term",
    tags: {
      WHO: "prompt-architect",
      WHEN: new Date().toISOString(),
      PROJECT: "meta-loop",
      WHY: "prompt-optimization"
    }
  }
});
```

## Conclusion

This addendum integrates the full cognitive architecture into prompt-architect:

1. **VERIX**: All outputs include epistemic markers (ground, confidence, illocution)
2. **VERILINGUA**: Frame selection based on prompt intent category
3. **DSPy**: Optimization loop for continuous improvement
4. **GlobalMOO**: Multi-objective tracking and Pareto frontier

The enhanced prompt-architect can now be used to optimize other foundry skills (skill-forge, agent-creator) and subsequently all commands, agents, skills, and playbooks.


---
*Promise: `<promise>COGNITIVE_ARCHITECTURE_ADDENDUM_VERIX_COMPLIANT</promise>`*
