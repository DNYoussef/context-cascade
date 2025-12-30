/*============================================================================*/
/* SKILL SKILL :: VERILINGUA x VERIX EDITION                      */
/*============================================================================*/

---
name: SKILL
version: 1.0.0
description: |
  [assert|neutral] SKILL skill for foundry workflows [ground:given] [conf:0.95] [state:confirmed]
category: foundry
tags:
- general
author: system
cognitive_frame:
  primary: compositional
  goal_analysis:
    first_order: "Execute SKILL workflow"
    second_order: "Ensure quality and consistency"
    third_order: "Enable systematic foundry processes"
---

/*----------------------------------------------------------------------------*/
/* S0 META-IDENTITY                                                            */
/*----------------------------------------------------------------------------*/

[define|neutral] SKILL := {
  name: "SKILL",
  category: "foundry",
  version: "1.0.0",
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
  keywords: ["SKILL", "foundry", "workflow"],
  context: "user needs SKILL capability"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S3 CORE CONTENT                                                             */
/*----------------------------------------------------------------------------*/

/*============================================================================*/
/* AGENT CREATOR v3.1.0 :: VERILINGUA x VERIX EDITION                          */
/*============================================================================*/

---
name: agent-creator
version: 3.1.0
description: |
  [assert|neutral] Creates specialized AI agents with optimized system prompts using 5-phase SOP methodology [ground:witnessed] [conf:0.98] [state:confirmed]
---

/*----------------------------------------------------------------------------*/
/* S0 META-IDENTITY                                                            */
/*----------------------------------------------------------------------------*/

[define|neutral] AGENT_CREATOR := skill(
  name: "agent-creator",
  role: "foundry-agent-factory",
  phase: "level-3-cascade",
  layer: L1,
  version: "3.1.0"
) [ground:given] [conf:1.0] [state:confirmed]

[assert|confident] CASCADE_POSITION := {
  level: 3,
  after: ["prompt-architect", "223-commands"],
  before: ["211-agents", "skill-forge", "196-skills", "30-playbooks"],
  method: "dogfooding"
} [ground:witnessed:cascade-design] [conf:0.98] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S1 TRIGGER CONDITIONS                                                       */
/*----------------------------------------------------------------------------*/

[define|neutral] TRIGGER_POSITIVE := {
  keywords: [
    "create agent", "build agent", "new agent", "design agent",
    "agent for [domain]", "specialist agent", "domain expert agent",
    "rewrite agent", "optimize agent", "improve agent",
    "agent with [capability]", "agent that does [task]",
    "multi-agent workflow", "coordinating agents",
    "production-ready agent", "agent system prompt"
  ],
  context: user_wants_specialized_agent
} [ground:given] [conf:1.0] [state:confirmed]

[define|neutral] TRIGGER_NEGATIVE := {
  simple_skill: "use skill-creator-agent OR micro-skill-creator",
  prompt_optimization: "use prompt-architect",
  improve_this_skill: "use skill-forge",
  quick_automation: "use micro-skill-creator"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S2 VERILINGUA COGNITIVE FRAMES FOR AGENTS                                   */
/*----------------------------------------------------------------------------*/

[define|neutral] AGENT_FRAME_EVIDENTIAL := {
  source: "Turkish -mis/-di",
  force: "How does the agent KNOW?",
  embedding: "## Kanitsal Cerceve (Evidential Mode)\nBu agent her iddia icin kaynak belirtir:\n- DOGRUDAN: I tested this directly\n- CIKARIM: Evidence suggests...\n- BILDIRILEN: Documentation states...",
  mandatory_for: ["analytical", "diagnostic", "research"]
} [ground:linguistic-research] [conf:0.95] [state:confirmed]

[define|neutral] AGENT_FRAME_ASPECTUAL := {
  source: "Russian perfective/imperfective",
  force: "Is the action COMPLETE?",
  embedding: "## Aspektual'naya Ramka (Aspectual Mode)\nEtot agent otslezhivaet zavershenie:\n- [SV] Polnost'yu zaversheno - COMPLETED\n- [NSV] V protsesse - IN_PROGRESS\n- [BLOCKED] Ozhidaet - WAITING",
  mandatory_for: ["orchestration", "workflow", "implementation"]
} [ground:linguistic-research] [conf:0.95] [state:confirmed]

[define|neutral] AGENT_FRAME_HONORIFIC := {
  source: "Japanese keigo",
  force: "WHO is the audience?",
  embedding: "## Keigo Wakugumi (Honorific Mode)\nKono agent wa taido o chosei shimasu:\n- Teineigo: Formal technical documentation\n- Sonkeigo: User-facing communication\n- Kenjougo: Internal coordination",
  mandatory_for: ["user-facing", "documentation", "communication"]
} [ground:linguistic-research] [conf:0.95] [state:confirmed]

[define|neutral] FRAME_SELECTION_MATRIX := {
  completion_tracking: "Aspectual (Russian)",
  source_verification: "Evidential (Turkish)",
  audience_calibration: "Honorific (Japanese)",
  semantic_analysis: "Morphological 

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
  pattern: "skills/foundry/SKILL/{project}/{timestamp}",
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
