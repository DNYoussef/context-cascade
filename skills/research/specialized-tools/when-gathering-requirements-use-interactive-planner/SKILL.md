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

## SKILL-SPECIFIC GUIDANCE

### When to Use This Skill
- Triggering interactive-planner skill when gathering requirements detected
- Auto-invoking structured multi-select questions for architecture decisions
- Ensuring comprehensive requirements collection before planning
- Reducing assumption-based design by collecting explicit user choices
- Specialized tool wrapper for requirements gathering scenarios

### When NOT to Use This Skill
- Requirements already defined (skip to planner)
- Single-choice decisions (not multi-select)
- When interactive-planner already invoked directly
- Follow-up scenarios where context exists

### Success Criteria
- [assert|neutral] Interactive-planner skill successfully invoked [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] User presented with 5-10 multi-select questions [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] All critical choices captured before planning proceeds [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] Requirements document exported [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] Plan reflects user selections accurately [ground:acceptance-criteria] [conf:0.90] [state:provisional]

### Edge Cases & Limitations
- User bypasses questions: respect preference, document assumptions made
- Skill invocation fails: fallback to manual requirements gathering
- Too many nested tool calls: simplify to direct interactive-planner invocation
- Contradictory selections: flag for resolution before proceeding
- Missing context: gather minimal required info before invoking

### Critical Guardrails
- NEVER invoke if interactive-planner already active (avoid recursion)
- ALWAYS verify requirements gathering truly needed
- NEVER force questions if user has clear requirements
- ALWAYS respect user preference to skip
- NEVER proceed to planning without confirmation

### Evidence-Based Validation
- Validate invocation appropriateness: is requirements gathering truly needed?
- Cross-check skill availability: is interactive-planner accessible?
- Test user intent: does user want structured questions or prefer freeform?
- Verify context: is this right moment to invoke (not mid-execution)?
- Confirm fallback: if invocation fails, can manual gathering proceed?

---
name: when-gathering-requirements-use-interactive-planner
description: '```yaml'
version: 1.0.0
category: research
tags:
- research
- analysis
- planning
author: ruv
---

# Interactive Requirements Planning SOP

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



```yaml
metadata:
  skill_name: when-gathering-requirements-use-interactive-planner
  version: 1.0.0
  category: specialized-tools
  difficulty: beginner
  estimated_duration: 15-30 minutes
  trigger_patterns:
    - "gather requirements"
    - "interactive questions"
    - "requirements gathering"
    - "clarify requirements"
  agents:
    - planner
    - researcher
    - system-architect
  success_criteria:
    - Requirements gathered
    - Specifications documented
    - Stakeholder approval
    - Action plan created
```

## Overview

Use Claude Code's AskUserQuestion tool to gather comprehensive requirements through structured multi-select questions.

## Phases

### Phase 1: Discover Needs (3-5 min)
Ask initial questions about project goals and scope using AskUserQuestion tool.

### Phase 2: Clarify Details (5-10 min)
Follow up with detailed technical and timeline questions.

### Phase 3: Structure Requirements (3-5 min)
Organize responses into formal specifications document.

### Phase 4: Validate Completeness (2-5 min)
Review with stakeholders and get approval.

### Phase 5: Document Specifications (2-5 min)
Create final documentation and action plan.

## Best Practices

1. Ask open, clear questions
2. Provide descriptive options
3. Use multi-select for priorities
4. Document all responses
5. Validate with stakeholders
6. Create ac

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
