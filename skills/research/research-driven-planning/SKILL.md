/*============================================================================*/
/* SKILL SKILL :: VERILINGUA x VERIX EDITION                      */
/*============================================================================*/

---
name: SKILL
version: 1.0.0
description: |
  [assert|neutral] SKILL skill for research workflows [ground:given] [conf:0.95] [state:confirmed]
category: research
tags:
- general
author: system
cognitive_frame:
  primary: evidential
  goal_analysis:
    first_order: "Execute SKILL workflow"
    second_order: "Ensure quality and consistency"
    third_order: "Enable systematic research processes"
---

/*----------------------------------------------------------------------------*/
/* S0 META-IDENTITY                                                            */
/*----------------------------------------------------------------------------*/

[define|neutral] SKILL := {
  name: "SKILL",
  category: "research",
  version: "1.0.0",
  layer: L1
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S1 COGNITIVE FRAME                                                          */
/*----------------------------------------------------------------------------*/

[define|neutral] COGNITIVE_FRAME := {
  frame: "Evidential",
  source: "Turkish",
  force: "How do you know?"
} [ground:cognitive-science] [conf:0.92] [state:confirmed]

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.

/*----------------------------------------------------------------------------*/
/* S2 TRIGGER CONDITIONS                                                       */
/*----------------------------------------------------------------------------*/

[define|neutral] TRIGGER_POSITIVE := {
  keywords: ["SKILL", "research", "workflow"],
  context: "user needs SKILL capability"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S3 CORE CONTENT                                                             */
/*----------------------------------------------------------------------------*/

name: research-driven-planning
description: Loop 1 of the Three-Loop Integrated Development System. Research-driven
  requirements analysis with iterative risk mitigation through 5x pre-mortem cycles
  using multi-agent consensus. Feeds validated, risk-mitigated plans to parallel-swarm-implementation.
  Use when starting new features or projects requiring comprehensive planning with
  <3% failure confidence and evidence-based technology selection.
version: 1.0.0
category: research
tags:
- research
- analysis
- planning
author: ruv
---

# Research-Driven Planning (Loop 1)

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



## Purpose

Comprehensive planning with research-backed solutions and iterative risk mitigation that prevents 85-95% of problems before coding begins.

## Specialist Agent Coordination

I coordinate multi-agent research and planning swarms using **explicit agent SOPs** from Claude-Flow's 86-agent ecosystem.

**Methodology** (SOP: Specification → Research → Planning → Execution → Knowledge):
1. **Specification Phase**: Requirements capture with structured SPEC.md
2. **Research Phase**: 6-agent parallel research with self-consistency validation
3. **Planning Phase**: MECE task decomposition with research integration
4. **Execution Phase**: 8-agent Byzantine consensus pre-mortem (5 iterations)
5. **Knowledge Phase**: Planning package generation for Loop 2 integration

**Integration**: Loop 1 of 3. Feeds → `parallel-swarm-implementation` (Loop 2), Receives ← `cicd-intelligent-recovery` (Loop 3) failure patterns.

---

## When to Use This Skill

Activate this skill when:
- Starting a new feature or project requiring comprehensive planning
- Need to prevent problems before coding begins (85-95% failure prevention)
- Want research-backed solutions instead of assumptions (30-60% time savings)
- Require risk analysis with <3% failure confidence
- Building something complex with multiple failure modes
- Need evidence-based planning that feeds into implementation

**DO NOT** use this skill for:
- Quick fixes or trivial changes (use direct implementation)
- Well-understood repetitive tasks (use existing patterns)
- Emergency hotfixes (skip to Loop 2)

---

## Input Contract

```yaml
input:
  project_description: string (required)
    # High-level description of what needs to be built

  requirements:
    functional: array[string] (required)
      # Core features and capabilities
    non_functional: object (optional)
      performance: string
      security: string
      scalability: string

  constraints:
    technical: array[string] (stack, framework, dependencies)
    timeline: string (deadlines, milestones)
    resources: object (team, budget, infrastructure)

  options:
    research_depth: enum[quick, standard, comprehensive] (default: standard)
    premortem_iterations: number (default: 5, range: 3-10)
    failure_threshold: number (default: 3, target: <3%)
```

## Output Contract

```yaml
output:
  specification:
    spec_file: path  # SPEC.md location
    requirements_complete: boolean
    success_criteria: array[string]

  research:
    evidence_sources: number  # Total research sources
    recommendations: array[object]
      solution: string
      confidence: number (0-100)
      evidence: array[url]
    risk_landscape: array[object]
      risk: string
      severity: enum[low, medium, high, critical]
      mitigation: string

  planning:
    enhanced_plan: path  # plan-enhanced.json location
    total_tasks: number
    task_dependencies: object
    estimated_complexity: string

  risk_analysis:
    premortem_iterations: number
    final_failure_confidence: number  # Target: <3%
    critical_risks_mitigated: number
    defense_strategies: array[string]

  integration:
    planning_package: path  # loop1-planning-package.json
    memory_namespace: string  # integration/loop1-to-loop2
    ready_for_loop2: boolean
```

---

## SOP Phase 1: Specification

**Objective**: Define initial

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
  pattern: "skills/research/SKILL/{project}/{timestamp}",
  store: ["executions", "decisions", "patterns"],
  retrieve: ["similar_tasks", "proven_patterns"]
} [ground:system-policy] [conf:1.0] [state:confirmed]

[define|neutral] MEMORY_TAGGING := {
  WHO: "SKILL-{session_id}",
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

[commit|confident] <promise>SKILL_VERILINGUA_VERIX_COMPLIANT</promise> [ground:self-validation] [conf:0.99] [state:confirmed]
