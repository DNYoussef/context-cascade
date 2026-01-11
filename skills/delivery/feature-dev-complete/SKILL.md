/*============================================================================*/
/* FEATURE-DEV-COMPLETE SKILL :: VERILINGUA x VERIX EDITION                      */
/*============================================================================*/

---
name: feature-dev-complete
version: 1.1.0
description: |
  [assert|neutral] Complete feature development lifecycle from research to deployment. Uses Gemini Search for best practices, architecture design, Codex prototyping, comprehensive testing, and documentation generation.  [ground:given] [conf:0.95] [state:confirmed]
category: delivery
tags:
- feature
- development
- lifecycle
- multi-model
- essential
author: ruv
cognitive_frame:
  primary: evidential
  goal_analysis:
    first_order: "Execute feature-dev-complete workflow"
    second_order: "Ensure quality and consistency"
    third_order: "Enable systematic delivery processes"
---

/*----------------------------------------------------------------------------*/
/* S0 META-IDENTITY                                                            */
/*----------------------------------------------------------------------------*/

[define|neutral] SKILL := {
  name: "feature-dev-complete",
  category: "delivery",
  version: "1.1.0",
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
  keywords: ["feature-dev-complete", "delivery", "workflow"],
  context: "user needs feature-dev-complete capability"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S3 CORE CONTENT                                                             */
/*----------------------------------------------------------------------------*/

# Feature Development Complete

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



## Aspektual'naya Ramka Aktivatsiya (Aspectual State Tracking)

Kazhdyy etap razvertyvaniya (Each stage of deployment):

### Tipy Sostoyaniya (State Types)

- **[SV:COMPLETED]** Polnost'yu zaversheno - Stage complete, move to next
- **[NSV:IN_PROGRESS]** V protsesse - Stage active, work ongoing
- **[BLOCKED]** Ozhidaet zavisimosti - Waiting for dependency
- **[INITIATED]** Nachato - Stage started, not yet in progress

### 12-Stage State Markers

Track each stage with explicit state markers:

1. **Stage 1 [RESEARCH]**: [SV|NSV|BLOCKED|INITIATED]
2. **Stage 2 [CODEBASE_ANALYSIS]**: [SV|NSV|BLOCKED|INITIATED]
3. **Stage 3 [SWARM_INIT]**: [SV|NSV|BLOCKED|INITIATED]
4. **Stage 4 [ARCHITECTURE]**: [SV|NSV|BLOCKED|INITIATED]
5. **Stage 5 [DIAGRAMS]**: [SV|NSV|BLOCKED|INITIATED]
6. **Stage 6 [PROTOTYPE]**: [SV|NSV|BLOCKED|INITIATED]
7. **Stage 7 [THEATER_DETECTION]**: [SV|NSV|BLOCKED|INITIATED]
8. **Stage 8 [TESTING]**: [SV|NSV|BLOCKED|INITIATED]
9. **Stage 9 [STYLE_POLISH]**: [SV|NSV|BLOCKED|INITIATED]
10. **Stage 10 [SECURITY]**: [SV|NSV|BLOCKED|INITIATED]
11. **Stage 11 [DOCUMENTATION]**: [SV|NSV|BLOCKED|INITIATED]
12. **Stage 12 [PRODUCTION_READY]**: [SV|NSV|BLOCKED|INITIATED]

### State Transition Rules

**Transition Protocols**:
- **[NSV->SV]**: All acceptance criteria met, tests passing, artifacts complete
- **[SV->NSV]**: Regression detected, failed tests, reopened for fixes
- **[*->BLOCKED]**: Missing dependency, external blocker, prerequisite incomplete
- **[BLOCKED->NSV]**: Blocker resolved, dependency met, work can resume
- **[INITIATED->NSV]**: Work has begun, active development underway

**Validation Checkpoints**:
Each transition requires evidence:
- Test results (for TESTING stage)
- Coverage reports (for quality gates)
- Security scan output (for SECURITY stage)
- Artifact existence (for DIAGRAMS, DOCUMENTATION)

## Keigo Wakugumi (Hierarchical Work Breakdown)

### Work Structure Hierarchy

```
EPIC: [Feature Name]
  |
  +-- STORY: User story 1 (Business value)
      |
      +-- TASK: Implementation task 1
          |
          +-- SUBTASK: Atomic work item 1.1
          +-- SUBTASK: Atomic work item 1.2
      |
      +-- TASK: Implementation task 2
          |
          +-- SUBTASK: Atomic work item 2.1
  |
  +-- STORY: User story 2 (Business value)
      |
      +-- TASK: Implementation task 3
```

### Hierarchy Levels Explained

1. **EPIC Level**: Overall feature (e.g., "User Authentication System")
2. **STORY Level**: User-facing value (e.g., "As a user, I can log in securely")
3. **TASK Level**: Technical implementation (e.g., "Implement JWT middleware")
4. **SUBTASK Level**: Atomic work units (e.g., "Write token validation function")

### Stage-to-Hierarchy Mapping

Each 12-stage workflow maps to hierarchical levels:

| Stage | Hierarchy Level | Example |
|-------|----------------|---------|
| 1-2 (Research) | EPIC planning | Define feature scope |
| 3-5 (Architecture) | STORY breakdown | User stories + design |
| 6-8 (Implementation) | TASK execution | Code, test, fix |
| 9-11 (Quality) | SUBTASK refinement | Polish, docs, security |
| 12 (Production) | EPIC completion | Deploy, validate |

## When to Use This Skill

- **Full Feature Development**: Complete end-to-end feature implementation
- **Greenfield Features**: Building new functionality from scratch
- **Research Required**: Features needing best practice research
- **Multi-Layer Changes**: Features spanning frontend, backend, database
- **Production Deployment**: Features requiring full testing and documentation
- **Architecture Design**: Features needing upfront design decisions

## When NOT to Use This Skill

- **Bug Fixes**: Use debugging or smart-bug-fix skills instead
- **Quick Prototypes**: Exploratory coding without production requirements
- **Refactoring**: Code restructuring without new features
- **Documentation Only**: Pure documen

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
  pattern: "skills/delivery/feature-dev-complete/{project}/{timestamp}",
  store: ["executions", "decisions", "patterns"],
  retrieve: ["similar_tasks", "proven_patterns"]
} [ground:system-policy] [conf:1.0] [state:confirmed]

[define|neutral] MEMORY_TAGGING := {
  WHO: "feature-dev-complete-{session_id}",
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

[commit|confident] <promise>FEATURE_DEV_COMPLETE_VERILINGUA_VERIX_COMPLIANT</promise> [ground:self-validation] [conf:0.99] [state:confirmed]
