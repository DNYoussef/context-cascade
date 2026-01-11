/*============================================================================*/
/* MICRO-SKILL-CREATOR SKILL :: VERILINGUA x VERIX EDITION                      */
/*============================================================================*/

---
name: micro-skill-creator
version: 2.0.0
description: |
  [assert|neutral] Rapidly creates atomic, focused skills optimized with evidence-based prompting, specialist agents, and systematic testing. Each micro-skill does one thing exceptionally well using self-consistency, pr [ground:given] [conf:0.95] [state:confirmed]
category: foundry
tags:
- skill-creation
- atomic
- modular
- evidence-based
- specialist-agents
author: ruv
cognitive_frame:
  primary: evidential
  goal_analysis:
    first_order: "Execute micro-skill-creator workflow"
    second_order: "Ensure quality and consistency"
    third_order: "Enable systematic foundry processes"
---

/*----------------------------------------------------------------------------*/
/* S0 META-IDENTITY                                                            */
/*----------------------------------------------------------------------------*/

[define|neutral] SKILL := {
  name: "micro-skill-creator",
  category: "foundry",
  version: "2.0.0",
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
  keywords: ["micro-skill-creator", "foundry", "workflow"],
  context: "user needs micro-skill-creator capability"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S3 CORE CONTENT                                                             */
/*----------------------------------------------------------------------------*/

<!-- SKILL SOP IMPROVEMENT v1.0 -->
## Skill Execution Criteria

### When to Use This Skill
- Building atomic, reusable workflow components
- Creating focused skills that do one thing exceptionally well
- Establishing building blocks for cascade orchestration
- Developing domain-specific micro-capabilities
- When repeatability and composability are critical

### When NOT to Use This Skill
- For complex multi-step workflows (use cascade-orchestrator instead)
- For one-off exploratory tasks without reuse value
- When task is too simple to benefit from skill abstraction
- When external tools already handle the capability better

### Success Criteria
- [assert|neutral] primary_outcome: "Atomic skill with single responsibility, clean interface, specialist agent, and systematic validation" [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] quality_threshold: 0.95 [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] verification_method: "Skill executes successfully in isolation, composes cleanly with other skills, passes functionality-audit validation" [ground:acceptance-criteria] [conf:0.90] [state:provisional]

### Edge Cases
- case: "Skill scope creep (trying to do too much)"
  handling: "Decompose into multiple micro-skills with clear interfaces, apply Unix philosophy"
- case: "Unclear input/output contract"
  handling: "Define explicit schema, add validation, document expected formats"
- case: "Skill depends on external state"
  handling: "Make dependencies explicit parameters, document preconditions, add state validation"

### Skill Guardrails
NEVER:
  - "Create skills with multiple responsibilities (violates atomic principle)"
  - "Use generic agents instead of domain specialists"
  - "Skip validation testing (functionality-audit required)"
  - "Create skills without clear composability in mind"
ALWAYS:
  - "Follow single responsibility principle (one skill, one purpose)"
  - "Design specialist agent with evidence-based prompting (self-consistency, program-of-thought, plan-and-solve)"
  - "Define clean input/output contracts with validation"
  - "Test in isolation AND in composition with other skills"
  - "Integrate with neural training for continuous improvement"

### Evidence-Based Execution
self_consistency: "After skill creation, execute multiple times with same input to verify deterministic behavior and consistent quality"
program_of_thought: "Decompose creation into: 1) Define single responsibility, 2) Design specialist agent, 3) Build input/output contract, 4) Implement core logic, 5) Validate systematically, 6) Test composability"
plan_and_solve: "Plan: Identify atomic operation + specialist expertise -> Execute: Build agent + validate -> Verify: Isolation test + composition test + neural training integration"
<!-- END SKILL SOP IMPROVEMENT -->

# Micro-Skill Creator (Enhanced)

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



## Trigger Keywords

**USE WHEN user mentions:**
- "create micro-skill", "atomic skill", "small skill", "focused skill"
- "single-purpose skill", "one task skill"
- "building block", "composable skill", "cascade component"
- "reusable [domain] skill", "skill for [specific task]"
- "Unix philosophy skill", "do one thing well"
- "skill using [evidence technique]" (self-consistency, program-of-thought, plan-and-solve)

**DO NOT USE when:**
- User wants COMPLEX multi-step skill - use skill-creator-agent
- User wants to create AGENT (not skill) - use agent-creator
- User wants to IMPROVE existing skill - use recursive-improvement or skill-forge
- User wants to optimize PROMPTS - use prompt-architect
- Task is one-off without reuse value - direct implementation faster
- Task already handled by external tools - integration better than recreation

**Instead use:**
- skill-creator-agent when skill needs multiple coordinated agents or complex workflow
- agent-creator when goal is standalone agent (no skill wrapper need

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
  pattern: "skills/foundry/micro-skill-creator/{project}/{timestamp}",
  store: ["executions", "decisions", "patterns"],
  retrieve: ["similar_tasks", "proven_patterns"]
} [ground:system-policy] [conf:1.0] [state:confirmed]

[define|neutral] MEMORY_TAGGING := {
  WHO: "micro-skill-creator-{session_id}",
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

[commit|confident] <promise>MICRO_SKILL_CREATOR_VERILINGUA_VERIX_COMPLIANT</promise> [ground:self-validation] [conf:0.99] [state:confirmed]
