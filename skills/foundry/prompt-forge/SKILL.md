/*============================================================================*/
/* PROMPT-FORGE SKILL :: VERILINGUA x VERIX EDITION                      */
/*============================================================================*/

---
name: prompt-forge
version: 2.0.1
description: |
  [assert|neutral] Meta-prompt that generates improved prompts and templates. Can improve other prompts including Skill Forge and even itself. All improvements are gated by frozen eval harness. Use when optimizing promp [ground:given] [conf:0.95] [state:confirmed]
category: foundry
tags:
- meta-prompt
- self-improvement
- recursive
- dogfooding
- cognitive-frames
author: system
cognitive_frame:
  primary: compositional
  goal_analysis:
    first_order: "Execute prompt-forge workflow"
    second_order: "Ensure quality and consistency"
    third_order: "Enable systematic foundry processes"
---

/*----------------------------------------------------------------------------*/
/* S0 META-IDENTITY                                                            */
/*----------------------------------------------------------------------------*/

[define|neutral] SKILL := {
  name: "prompt-forge",
  category: "foundry",
  version: "2.0.1",
  layer: L1
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S1 COGNITIVE FRAME                                                          */
/*----------------------------------------------------------------------------*/

[define|neutral] COGNITIVE_FRAME := {
  frame: "Compositional",
  source: "German",
  force: "Build from primitives?"
} [ground:cognitive-science] [conf:0.92] [state:confirmed]

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.

/*----------------------------------------------------------------------------*/
/* S2 TRIGGER CONDITIONS                                                       */
/*----------------------------------------------------------------------------*/

[define|neutral] TRIGGER_POSITIVE := {
  keywords: ["prompt-forge", "foundry", "workflow"],
  context: "user needs prompt-forge capability"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S3 CORE CONTENT                                                             */
/*----------------------------------------------------------------------------*/

# Prompt Forge (Meta-Prompt)

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



## Purpose

Generate improved prompts and templates with:
- Explicit rationale for each change
- Predicted improvement metrics
- Risk assessment
- Actionable diffs

**Key Innovation**: Can improve Skill Forge prompts, then Skill Forge can improve Prompt Forge prompts - creating a recursive improvement loop.

## When to Use

- Optimizing existing prompts for better performance
- Creating prompt diffs with clear rationale
- Running the recursive improvement loop
- Auditing prompts for common issues

## MCP Requirements

### memory-mcp (Required)

**Purpose**: Store proposals, test results, version history

**Activation**:
```bash
claude mcp add memory-mcp npx @modelcontextprotocol/server-memory
```

---

## Core Operations

### Operation 1: Analyze Prompt

Before improving, deeply understand the target prompt.

```yaml
analysis:
  target: "{prompt_path}"

  structural_analysis:
    sections: [list of sections]
    flow: "How sections connect"
    dependencies: "What inputs/outputs exist"

  quality_assessment:
    clarity:
      score: 0.0-1.0
      issues: ["Ambiguous instruction in section X"]
    completeness:
      score: 0.0-1.0
      issues: ["Missing failure handling for case Y"]
    precision:
      score: 0.0-1.0
      issues: ["Vague success criteria in section Z"]

  pattern_detection:
    evidence_based_techniques:
      self_consistency: present|missing|partial
      program_of_thought: present|missing|partial
      plan_and_solve: present|missing|partial
    failure_handling:
      explicit_errors: present|missing|partial
      edge_cases: present|missing|partial
      uncertainty: present|missing|partial

  improvement_opportunities:
    - area: "Section X"
      issue: "Lacks explicit timeout handling"
      priority: high|medium|low
      predicted_impact: "+X% reliability"
```

### Operation 2: Generate Improvement Proposal

Create concrete, testable improvement proposals.

```yaml
proposal:
  id: "prop-{timestamp}"
  target: "{prompt_path}"
  type: "prompt_improvement"

  summary: "One-line description of improvement"

  changes:
    - section: "Section name"
      location: "Line X-Y"
      before: |
        Original text...
      after: |
        Improved text...
      rationale: "Why this change improves the prompt"
      technique: "Which evidence-based technique applied"

  predicted_improvement:
    primary_metric: "success_rate"
    expected_delta: "+5%"
    confidence: 0.8
    reasoning: "Based on similar improvements in prompt X"

  risk_assessment:
    regression_risk: low|medium|high
    affected_components:
      - "Component 1"
      - "Component 2"
    rollback_complexity: simple|moderate|complex

  test_plan:
    - test: "Run on benchmark task A"
      expected: "Improvement in clarity score"
    - test: "Check for regressions in task B"
      expected: "No degradation"
```

### Operation 3: Apply Evidence-Based Techniques

Systematically apply research-validated prompting patterns.

#### Self-Consistency Enhancement

```markdown
BEFORE:
"Analyze the code and report issues"

AFTER:
"Analyze the code from three perspectives:
1. Security perspective: What vulnerabilities exist?
2. Performance perspective: What bottlenecks exist?
3. Maintainability perspective: What code smells exist?

Cross-reference findings. Flag any inconsistencies between perspectives.
Provide confidence scores for each finding.
Return only findings that appear in 2+ perspectives OR have >80% confidence."
```

#### Program-of-Thought Enhancement

```markdown
BEFORE:
"Calculate the optimal configuration"

AFTER:
"Calculate the optimal configuration step by step:

Step 1: Identify all configuration parameters
  - List each parameter
  - Document valid ranges
  - Note dependencies between parameters

Step 2: Define optimization criteria
  - Primary metric: [what to maximize/minimize]
  - Constraints: [hard limits]
  - T

/*----------------------------------------------------------------------------*/
/* S4 SUCCESS CRITERIA                                                         */
/*----------------------------------------------------------------------------*/

[define|neutral] SUCCESS_CRITERIA := {
  primary: "Skill execution completes successfully",
  quality: "Output meets quality thresholds",
  verification: "Results validated against requirements"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S5 MCP INTEGRATION                                                          */
/*----------------------------------------------------------------------------*/

[define|neutral] MCP_INTEGRATION := {
  memory_mcp: "Store execution results and patterns",
  tools: ["mcp__memory-mcp__memory_store", "mcp__memory-mcp__vector_search"]
} [ground:witnessed:mcp-config] [conf:0.95] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S6 MEMORY NAMESPACE                                                         */
/*----------------------------------------------------------------------------*/

[define|neutral] MEMORY_NAMESPACE := {
  pattern: "skills/foundry/prompt-forge/{project}/{timestamp}",
  store: ["executions", "decisions", "patterns"],
  retrieve: ["similar_tasks", "proven_patterns"]
} [ground:system-policy] [conf:1.0] [state:confirmed]

[define|neutral] MEMORY_TAGGING := {
  WHO: "prompt-forge-{session_id}",
  WHEN: "ISO8601_timestamp",
  PROJECT: "{project_name}",
  WHY: "skill-execution"
} [ground:system-policy] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S7 SKILL COMPLETION VERIFICATION                                            */
/*----------------------------------------------------------------------------*/

[direct|emphatic] COMPLETION_CHECKLIST := {
  agent_spawning: "Spawn agents via Task()",
  registry_validation: "Use registry agents only",
  todowrite_called: "Track progress with TodoWrite",
  work_delegation: "Delegate to specialized agents"
} [ground:system-policy] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S8 ABSOLUTE RULES                                                           */
/*----------------------------------------------------------------------------*/

[direct|emphatic] RULE_NO_UNICODE := forall(output): NOT(unicode_outside_ascii) [ground:windows-compatibility] [conf:1.0] [state:confirmed]

[direct|emphatic] RULE_EVIDENCE := forall(claim): has(ground) AND has(confidence) [ground:verix-spec] [conf:1.0] [state:confirmed]

[direct|emphatic] RULE_REGISTRY := forall(agent): agent IN AGENT_REGISTRY [ground:system-policy] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* PROMISE                                                                     */
/*----------------------------------------------------------------------------*/

[commit|confident] <promise>PROMPT_FORGE_VERILINGUA_VERIX_COMPLIANT</promise> [ground:self-validation] [conf:0.99] [state:confirmed]
