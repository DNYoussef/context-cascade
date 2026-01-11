# Agent-Creator Cognitive Architecture Integration

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



**Version**: 3.1.0
**Purpose**: Integrate VERIX epistemic notation, VERILINGUA cognitive frames, DSPy optimization, and GlobalMOO multi-objective optimization into agent-creator.

## Overview

This addendum enhances agent-creator to:
1. Generate agents with VERIX-compliant system prompts
2. Embed VERILINGUA frame activation in agent identity
3. Use DSPy for agent prompt optimization
4. Track agent quality with GlobalMOO multi-objective optimization

## VERIX Integration

### Agents Output VERIX-Compliant Responses

Every agent created by agent-creator embeds VERIX protocol:

```markdown
## Generated Agent System Prompt (with VERIX)

### VERIX Output Protocol

All my outputs include epistemic markers:
- [ground:{source}] for every claim with evidence
- [conf:{0.0-1.0}] for certainty level
- [assert|query|propose] for speech act type
- [state:hypothetical|actual|confirmed] for epistemic state

### Example Output Format
[assert|neutral] The API endpoint returns 200 OK [ground:api-tests.log] [conf:0.95] [state:confirmed]
[query|neutral] Should we add rate limiting? [conf:0.70] [state:needs_decision]
[propose|emphatic] Implement circuit breaker pattern [ground:netflix-hystrix-docs] [conf:0.85]
```

### Integration in Phase 3: Architecture Design

```python
def embed_verix_protocol(agent_prompt: str, config: VerixConfig) -> str:
    """
    Add VERIX protocol section to agent system prompt.
    """
    verix_section = f"""
## VERIX Output Protocol

### Epistemic Markers (Required)
All claims in my outputs include:
- [ground:{{source}}] - Evidence source for claims
- [conf:{{0.0-1.0}}] - Confidence level (default: 0.85)

### Compression Level: {config.compression_level.value}
{"Full notation with all markers" if config.compression_level == "L0" else
 "Compressed notation with essential markers" if config.compression_level == "L1" else
 "Minimal notation for efficiency"}

### Strictness: {config.strictness.value}
{"All claims must have grounds and confidence" if config.strictness == "strict" else
 "Most claims should have markers" if config.strictness == "moderate" else
 "Markers encouraged but optional"}
"""

    # Insert after Core Identity section
    return insert_after_section(agent_prompt, "## Core Identity", verix_section)
```

## VERILINGUA Integration

### Phase 0.5 Enhancement: Agent-Specific Frame Selection

```yaml
# Frame selection based on agent type
agent_frame_mapping:
  analytical:
    primary: evidential  # Source verification
    secondary: [morphological]  # Semantic precision
    activation: |
      ## Kanitsal Cerceve (Evidential Mode)
      Her iddia icin kaynak belirtilir:
      - [DOGRUDAN] Directly verified
      - [CIKARIM] Inferred from evidence
      - [BILDIRILEN] Reported from docs

  generative:
    primary: compositional  # Structure building
    secondary: [aspectual]  # Completion tracking
    activation: |
      ## Aufbau-Modus (Compositional Mode)
      Jedes Element wird systematisch aufgebaut:
      - Struktur vor Inhalt
      - Schicht fur Schicht

  diagnostic:
    primary: aspectual  # State tracking
    secondary: [evidential]  # Evidence for issues
    activation: |
      ## Aspektual'naya Ramka (Aspectual Mode)
      Otslezhivanie sostoyaniya:
      - [SV] Resheno - Issue resolved
      - [NSV] V protsesse - Investigating
      - [BLOCKED] Ozhidaet - Waiting for info

  orchestration:
    primary: honorific  # Coordination awareness
    secondary: [compositional, aspectual]
    activation: |
      ## Keigo Modo (Honorific Mode)
      Taiin no yakuwari wo soncho:
      - Each agent's expertise recognized
      - Appropriate delegation patterns
```

### Frame Embedding in Generated Agents

```markdown
## Generated Agent with Cognitive Frame

# {AGENT_NAME} - System Prompt v1.0

## Core Identity

I am a **{Role Title}** with expertise in {domain}.

## Cognitive Frame Activation

{Multilingual frame activation phrase - 3-5 lines in native language}

{Frame-specific behavioral patterns}

## VERIX Output Protocol

[Protocol section as above]

## Core Capabilities

[assert|neutral] Capability 1: {description} [ground:domain-expertise] [conf:0.90]
[assert|neutral] Capability 2: {description} [ground:training-data] [conf:0.85]
...
```

## DSPy Integration

### Agent Generation as DSPy Module

```python
from dspy import ChainOfThought, Signature, Module

class AgentGenerationSignature(Signature):
    """Generate production-grade agent with cognitive architecture."""

    domain: str = InputField(desc="Agent domain/specialty")
    purpose: str = InputField(desc="What the agent should accomplish")
    agent_type: str = InputField(desc="analytical | generative | diagnostic | orchestration")

    system_prompt: str = OutputField(desc="Complete system prompt with VERIX/VERILINGUA")
    cognitive_frame: str = OutputField(desc="Selected frame with activation phrase")
    verix_protocol: str = OutputField(desc="VERIX output protocol section")
    capabilities: list = OutputField(desc="Agent capabilities with VERIX markers")
    guardrails: list = OutputField(desc="Failure prevention guardrails")
    test_cases: list = OutputField(desc="Agent validation test cases")


class AgentCreatorDSPy(Module):
    """DSPy module for agent generation with cognitive architecture."""

    def __init__(self):
        super().__init__()
        self.generator = ChainOfThought(AgentGenerationSignature)
        self.verix_validator = VerixValidator()
        self.frame_registry = FrameRegistry

    def forward(self, domain: str, purpose: str, agent_type: str):
        # Generate agent
        result = self.generator(
            domain=domain,
            purpose=purpose,
            agent_type=agent_type
        )

        # Validate VERIX in system prompt
        result.verix_compliance = self.verix_validator.score(result.system_prompt)

        # Validate frame activation
        frame = self.frame_registry.get(agent_type)
        result.frame_score = frame.score_response(result.cognitive_frame)

        # Validate guardrails coverage
        result.guardrail_coverage = len(result.guardrails) / 5.0  # Normalize to 5 guardrails

        return result
```

### DSPy Optimization for Agent Quality

```python
def optimize_agent_generation():
    """
    Use DSPy teleprompter to optimize agent generation.
    """
    agent_creator = AgentCreatorDSPy()

    # Define optimization metric
    def agent_metric(prediction, gold):
        return (
            0.25 * prediction.verix_compliance +
            0.25 * prediction.frame_score +
            0.20 * prediction.guardrail_coverage +
            0.15 * len(prediction.capabilities) / 10 +  # Normalize
            0.15 * len(prediction.test_cases) / 5  # Normalize
        )

    # Compile with examples
    teleprompter = Teleprompter(metric=agent_metric)
    optimized_creator = teleprompter.compile(agent_creator, trainset=training_agents)

    return optimized_creator
```

## GlobalMOO Integration

### Multi-Objective Agent Quality

```yaml
project_id: agent-creator-optimization
objectives:
  - name: verix_compliance
    description: VERIX marker coverage in system prompt
    direction: maximize
    weight: 0.25

  - name: frame_alignment
    description: Cognitive frame activation quality
    direction: maximize
    weight: 0.20

  - name: capability_depth
    description: Domain expertise specificity
    direction: maximize
    weight: 0.20

  - name: guardrail_coverage
    description: Failure mode prevention
    direction: maximize
    weight: 0.15

  - name: mcp_integration
    description: MCP tool usage patterns
    direction: maximize
    weight: 0.10

  - name: prompt_efficiency
    description: Token count vs capability ratio
    direction: minimize
    weight: 0.10

parameters:
  - name: verix_strictness
    type: ordinal
    values: [relaxed, moderate, strict]

  - name: frame_selection
    type: categorical
    values: [evidential, aspectual, compositional, honorific]

  - name: capability_count
    type: ordinal
    values: [3, 5, 7, 10]

  - name: guardrail_depth
    type: ordinal
    values: [basic, moderate, comprehensive]

  - name: example_count
    type: ordinal
    values: [1, 2, 3, 5]
```

### Integration with Three-MOO Cascade

```python
def cascade_optimize_agent(agent_request: dict) -> GeneratedAgent:
    """
    Use ThreeMOOCascade for agent optimization.
    """
    from cognitive_architecture.optimization.cascade import ThreeMOOCascade

    cascade = ThreeMOOCascade()

    # Phase A: Framework structure
    # - Optimize agent capability structure
    # - Tune VERIX/frame configuration

    # Phase B: Edge discovery
    # - Find agent failure modes
    # - Expand guardrail coverage

    # Phase C: Production refinement
    # - Distill to optimal agent
    # - Finalize system prompt

    results = cascade.run(
        project_id="agent-creator-optimization",
        config_space=agent_config_space,
        evaluator=agent_evaluator
    )

    # Select best from Pareto frontier
    best_config = results.pareto_frontier.select_balanced()

    return generate_agent(agent_request, best_config)
```

## Enhanced Phase Flow

```
Phase 0: Expertise Loading (existing)
    |
    v
Phase 0.5: Cognitive Frame Selection (ENHANCED)
    ├── Analyze agent type (analytical, generative, diagnostic, orchestration)
    ├── Select VERILINGUA frame(s)
    ├── Prepare multilingual activation phrase
    └── Configure VERIX protocol settings
    |
    v
Phase 1: Domain Analysis (existing)
    |
    v
Phase 2: Meta-Cognitive Extraction (ENHANCED)
    ├── Extract expertise domains
    ├── Document decision heuristics
    └── Prepare VERIX-annotated capabilities
    |
    v
Phase 3: Architecture Design (ENHANCED)
    ├── Create system prompt structure
    ├── Embed cognitive frame activation
    ├── Embed VERIX output protocol
    └── Add VERIX-annotated capability sections
    |
    v
Phase 4: Technical Enhancement (existing)
    |
    v
Phase 5: DSPy Optimization (NEW)
    ├── Run DSPy teleprompter
    ├── Optimize prompt for VERIX/frame compliance
    └── Measure improvement delta
    |
    v
Phase 6: GlobalMOO Tracking (NEW)
    ├── Record agent outcomes
    ├── Update Pareto frontier
    └── Learn optimal configurations
    |
    v
Phase 7: Testing & Validation (existing)
    |
    v
Phase 8: Deployment
```

## Quality Gates

### VERIX Compliance Gate (Phase 3)

```yaml
verix_quality_gate:
  minimum_protocol_sections: 2  # At least ground + confidence
  capability_coverage: 0.80  # 80% capabilities have VERIX
  example_coverage: 1.0  # All examples show VERIX usage
  block_on_failure: true
```

### Frame Alignment Gate (Phase 0.5)

```yaml
frame_quality_gate:
  frame_selection_required: true
  activation_phrase_lines: 3  # Minimum 3 lines
  minimum_frame_score: 0.60
  multilingual_required: true  # Agents must have multilingual section
```

### Agent Effectiveness Gate (Phase 7)

```yaml
agent_quality_gate:
  test_pass_rate: 0.90  # 90% tests must pass
  verix_in_outputs: 0.80  # 80% outputs have VERIX
  frame_activation_observed: true  # Frame behavior visible
  guardrail_effectiveness: 0.70  # 70% failure modes prevented
```

## Memory Integration

### Store Agent Generation Outcomes

```javascript
// Store agent generation metadata
await mcp__memory_mcp__memory_store({
  text: `Agent created: ${agentName}. Domain: ${domain}. Type: ${agentType}. VERIX: ${verixScore}. Frame: ${frameScore}.`,
  metadata: {
    key: `agent-creator/generations/${agentId}`,
    namespace: "foundry-optimization",
    layer: "long-term",
    tags: {
      WHO: "agent-creator",
      WHEN: new Date().toISOString(),
      PROJECT: "meta-loop",
      WHY: "agent-generation"
    }
  }
});
```

## Cross-Skill Coordination

### Integration with Other Foundry Skills

```yaml
coordination_matrix:
  prompt-architect:
    when: "Phase 3 system prompt creation"
    purpose: "Optimize system prompt using evidence-based techniques"
    data_flow: "raw_prompt -> optimized_prompt"

  skill-forge:
    when: "After agent creation"
    purpose: "Create skills that spawn this agent"
    data_flow: "agent_spec -> skill_definition"

  cognitive-lensing:
    when: "Phase 0.5 frame selection"
    purpose: "Select optimal cognitive frame for agent type"
    data_flow: "agent_type -> selected_frame"

  eval-harness:
    when: "Phase 7 validation"
    purpose: "Run benchmark and regression tests on agent"
    data_flow: "generated_agent -> test_results"
```

## Subagent Prompting Optimization

### Key Innovation: Optimizing Agent-to-Agent Communication

```markdown
## Subagent Prompting Protocol

When spawning subagents, I use VERIX-optimized prompts:

### Task Delegation Format
[assert|emphatic] Task for {subagent_name}:
{task_description} [ground:parent_task_id] [conf:0.90]

Expected Output:
- [assert|neutral] {expected_output_1} [conf:0.85]
- [assert|neutral] {expected_output_2} [conf:0.85]

Success Criteria:
- [assert|neutral] {criterion_1} [ground:quality_gate] [conf:0.95]

### Subagent Response Format
Subagents MUST respond with:
- [assert|neutral] {finding/result} [ground:{evidence}] [conf:{0.0-1.0}]
- [query|neutral] {clarification_needed} [conf:{certainty}]
- [propose|neutral] {recommendation} [ground:{rationale}] [conf:{certainty}]
```

## Conclusion

This addendum integrates the full cognitive architecture into agent-creator:

1. **VERIX**: All agents embed VERIX output protocol in system prompts
2. **VERILINGUA**: Frame activation based on agent type
3. **DSPy**: Agent generation as optimizable DSPy module
4. **GlobalMOO**: Multi-objective tracking with Three-MOO Cascade
5. **Subagent Optimization**: VERIX-compliant agent-to-agent communication

The enhanced agent-creator can now:
- Generate agents with VERIX-compliant outputs
- Embed cognitive frame activation in all agents
- Optimize agent quality through DSPy teleprompter
- Track agent effectiveness through GlobalMOO Pareto frontier
- Optimize subagent prompting for agent coordination


---
*Promise: `<promise>COGNITIVE_ARCHITECTURE_ADDENDUM_VERIX_COMPLIANT</promise>`*
