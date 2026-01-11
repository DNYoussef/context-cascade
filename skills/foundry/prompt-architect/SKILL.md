/*============================================================================*/
/* PROMPT-ARCHITECT SKILL :: VERILINGUA x VERIX EDITION                      */
/*============================================================================*/

---
name: prompt-architect
version: 3.0.0
description: |
  [assert|neutral] [assert|neutral] Meta-loop skill for prompt optimization using VERILINGUA x VERIX [ground:witnessed] [conf:0.99] [state:confirmed]  [ground:given] [conf:0.95] [state:confirmed]
category: foundry
tags:
- general
author: system
cognitive_frame:
  primary: compositional
  goal_analysis:
    first_order: "Execute prompt-architect workflow"
    second_order: "Ensure quality and consistency"
    third_order: "Enable systematic foundry processes"
---

/*----------------------------------------------------------------------------*/
/* S0 META-IDENTITY                                                            */
/*----------------------------------------------------------------------------*/

[define|neutral] SKILL := {
  name: "prompt-architect",
  category: "foundry",
  version: "3.0.0",
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
  keywords: ["prompt-architect", "foundry", "workflow"],
  context: "user needs prompt-architect capability"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S3 CORE CONTENT                                                             */
/*----------------------------------------------------------------------------*/

/*============================================================================*/
/* PROMPT ARCHITECT v3.0.0 :: VERILINGUA x VERIX EDITION                      */
/*============================================================================*/

/*----------------------------------------------------------------------------*/
/* S0 META-IDENTITY                                                           */
/*----------------------------------------------------------------------------*/

[define|neutral] PROMPT_ARCHITECT := skill(
  name: "prompt-architect",
  role: "meta-loop-optimizer",
  phase: 2,
  layer: L1
) [ground:given] [conf:1.0] [state:confirmed]

[assert|confident] THIS_SKILL := bootstrap(
  cascade: commands -> agents -> skills -> playbooks,
  method: dogfooding,
  validation: self-application
) [ground:witnessed:design-doc] [conf:0.98] [state:confirmed]

[direct|emphatic] COMMUNICATION_LAYER := L1 [ground:system-policy] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S1 TRIGGER CONDITIONS                                                      */
/*----------------------------------------------------------------------------*/

[define|neutral] TRIGGER_POSITIVE := {
  keywords: [
    "improve prompt", "optimize prompt", "refine prompt",
    "create prompt", "design prompt", "build prompt",
    "prompt quality", "prompt engineering",
    "evidence-based prompting", "self-consistency"
  ],
  context: user_wants_better_prompts
} [ground:given] [conf:1.0] [state:confirmed]

[define|neutral] TRIGGER_NEGATIVE := {
  agent_system_prompts: use(agent-creator) OR use(prompt-forge),
  skill_creation: use(skill-creator-agent),
  this_skill_improvement: use(skill-forge),
  one_time_prompt: skip(direct_crafting_faster)
} [ground:given] [conf:1.0] [state:confirmed]

[assert|neutral] ROUTING_LOGIC := (
  (intent = agent_system_prompt) -> route(agent-creator) AND
  (intent = improve_system_prompt) -> route(prompt-forge) AND
  (intent = create_skill) -> route(skill-creator-agent) AND
  (intent = improve_this) -> route(skill-forge) AND
  (intent = user_prompt) -> route(prompt-architect)
) [ground:inferred:capability-matching] [conf:0.95] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S2 VERILINGUA COGNITIVE FRAMES (7 MANDATORY)                               */
/*----------------------------------------------------------------------------*/

[define|neutral] FRAME_EVIDENTIAL := {
  source: "Turkish -mis/-di",
  force: "How do you know?",
  markers: {
    witnessed: "directly observed/verified",
    reported: "learned from source",
    inferred: "deduced logically",
    assumed: "explicit assumption with confidence"
  },
  weight: 0.15,
  immutable_minimum: 0.30
} [ground:linguistic-research] [conf:0.95] [state:confirmed]

[define|neutral] FRAME_ASPECTUAL := {
  source: "Russian perfective/imperfective",
  force: "Complete or ongoing?",
  markers: {
    complete: "action finished",
    ongoing: "action in progress",
    habitual: "repeating regularly",
    attempted: "tried, outcome pending"
  },
  weight: 0.12
} [ground:linguistic-research] [conf:0.95] [state:confirmed]

[define|neutral] FRAME_MORPHOLOGICAL := {
  source: "Arabic trilateral roots",
  force: "What are the root components?",
  markers: {
    root: "semantic kernel",
    derived: "concept derived from root",
    composed: "components combined"
  },
  weight: 0.10
} [ground:linguistic-research] [conf:0.95] [state:confirmed]

[define|neutral] FRAME_COMPOSITIONAL := {
  source: "German compounding",
  force: "Build from primitives?",
  markers: {
    primitive: "basic building block",
    compound: "primitives combined",
    builds: "compositional hierarchy"
  },
  weight: 0.10
} [ground:linguistic-research] [conf:0.95] [state:confirmed]

[define|neutral] FRAME_HONORIFIC := {
  source: "Japanese keigo",
  force: "Who is the audience?",
  markers: {
    audience

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
  pattern: "skills/foundry/prompt-architect/{project}/{timestamp}",
  store: ["executions", "decisions", "patterns"],
  retrieve: ["similar_tasks", "proven_patterns"]
} [ground:system-policy] [conf:1.0] [state:confirmed]

[define|neutral] MEMORY_TAGGING := {
  WHO: "prompt-architect-{session_id}",
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

[commit|confident] <promise>PROMPT_ARCHITECT_VERILINGUA_VERIX_COMPLIANT</promise> [ground:self-validation] [conf:0.99] [state:confirmed]
