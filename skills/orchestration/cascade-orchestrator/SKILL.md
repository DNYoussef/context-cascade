/*============================================================================*/
/* CASCADE-ORCHESTRATOR SKILL :: VERILINGUA x VERIX EDITION                      */
/*============================================================================*/

---
name: cascade-orchestrator
version: 2.1.0
description: |
  [assert|neutral] Creates sophisticated workflow cascades coordinating multiple micro-skills with sequential pipelines, parallel execution, conditional branching, and Codex sandbox iteration. Enhanced with multi-model  [ground:given] [conf:0.95] [state:confirmed]
category: orchestration
tags:
- orchestration
- workflows
- cascades
- multi-model
- codex-integration
author: ruv
cognitive_frame:
  primary: evidential
  goal_analysis:
    first_order: "Execute cascade-orchestrator workflow"
    second_order: "Ensure quality and consistency"
    third_order: "Enable systematic orchestration processes"
---

/*----------------------------------------------------------------------------*/
/* S0 META-IDENTITY                                                            */
/*----------------------------------------------------------------------------*/

[define|neutral] SKILL := {
  name: "cascade-orchestrator",
  category: "orchestration",
  version: "2.1.0",
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
  keywords: ["cascade-orchestrator", "orchestration", "workflow"],
  context: "user needs cascade-orchestrator capability"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S3 CORE CONTENT                                                             */
/*----------------------------------------------------------------------------*/

## Aspektual'naya Ramka Orkestratsii (Workflow State Tracking)

### Tipy Sostoyaniya (State Types)

**Stage States:**
- [SV:COMPLETED] Zaversheno - Stage/task complete, outputs validated
- [NSV:IN_PROGRESS] V protsesse - Active work, currently executing
- [BLOCKED] Blokirovano - Waiting for dependency to complete
- [PARALLEL] Parallel'no - Concurrent execution with other stages
- [FAILED] Provaleno - Stage failed, requires intervention
- [PENDING] Ozhidayet - Queued, not yet started

**Agent States:**
- [IDLE] Gotov - Ready for task assignment
- [WORKING] Rabotayet - Executing assigned task
- [WAITING] Zhdet - Blocked on external dependency
- [DONE] Zavershen - Task completed successfully
- [ERROR] Oshibka - Encountered error, needs recovery

**Transition Rules:**
- Phase N [SV] -> Phase N+1 [NSV] (all stages in phase complete)
- Stage [BLOCKED] -> Stage [NSV] (dependency resolved)
- Stage [FAILED] -> Stage [NSV] (retry/fix applied)
- Agent [IDLE] -> Agent [WORKING] -> Agent [DONE] (successful path)

### Vizualizatsiya Sostoyaniya (State Visualization)

```
WORKFLOW: enhanced-data-pipeline
  |
  +-- PHASE 1: Extract [SV:COMPLETED]
  |     +-- STAGE: extract-data [SV] (Agent: data-engineer [DONE])
  |
  +-- PHASE 2: Validate [NSV:IN_PROGRESS]
  |     +-- STAGE: validate-schema [NSV] (Agent: validator [WORKING])
  |     +-- STAGE: codex-auto-fix [BLOCKED] (Agent: codex [WAITING])
  |
  +-- PHASE 3: Transform [PENDING]
  |     +-- STAGE: transform-data [PENDING] (Agent: transformer [IDLE])
  |
  +-- PHASE 4: Report [PENDING]
        +-- STAGE: generate-report [PENDING] (Agent: reporter [IDLE])

DEPENDENCIES:
  Phase 1 [SV] -> Phase 2 [NSV] -> Phase 3 [PENDING] -> Phase 4 [PENDING]
```

## Keigo Wakugumi (Hierarchical Work Structure)

### Workflow Hierarchy

```
WORKFLOW (最上位)
  |
  +-- PHASE (重要段階) - Major sequential stage
        |
        +-- STAGE (小段階) - Sub-phase grouping
              |
              +-- TASK (作業) - Individual work item
                    |
                    +-- SUBTASK (細分) - Atomic operation
```

**Hierarchy Levels:**
1. **WORKFLOW** - Overall orchestration (e.g., "Production Deployment Pipeline")
2. **PHASE** - Sequential major stage (e.g., "Build", "Test", "Deploy")
3. **STAGE** - Within-phase grouping (e.g., "Unit Tests", "Integration Tests")
4. **TASK** - Assignable work unit (e.g., "Run Jest suite")
5. **SUBTASK** - Atomic operation (e.g., "Execute test file X")

### Dependency Visualization with Hierarchy

```
PHASE 1: Foundation Setup [SV]
  |-- TASK A: Research best practices [SV]
  |     |-- SUBTASK A.1: Search documentation [SV]
  |     |-- SUBTASK A.2: Analyze patterns [SV]

PHASE 2: Parallel Implementation [NSV]
  |-- TASK B: Backend API [NSV] (PARALLEL GROUP: implementation)
  |     |-- SUBTASK B.1: Define routes [SV]
  |     |-- SUBTASK B.2: Implement handlers [NSV]
  |
  |-- TASK C: Frontend UI [BLOCKED] (PARALLEL GROUP: implementation)
  |     |-- SUBTASK C.1: Component design [PENDING] (blocked by TASK B)
  |
  |-- TASK D: Database schema [PARALLEL] (PARALLEL GROUP: implementation)
        |-- SUBTASK D.1: Schema design [SV]
        |-- SUBTASK D.2: Migrations [NSV]

PHASE 3: Integration & Validation [PENDING]
  |-- TASK E: Integration testing [PENDING]
        |-- SUBTASK E.1: API tests [PENDING]
        |-- SUBTASK E.2: E2E tests [PENDING]

HIERARCHY PROPERTIES:
  - PHASE level: Sequential dependencies (Phase 1 -> Phase 2 -> Phase 3)
  - TASK level: Parallel within phase (TASK B || TASK C || TASK D)
  - SUBTASK level: Sequential within task (SUBTASK B.1 -> B.2)
```

## Orchestration Skill Guidelines

### When to Use This Skill
- **Multi-stage workflows** requiring sequential, parallel, or conditional execution
- **Complex pipelines** coordinating multiple micro-skills or agents
- **Iterative processes** with Codex sandbox testing and auto-fix loops
- **Multi-model routing** requiring intelligent AI selection per stage
- **Production workflows** needing GitHub integration and memory p

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
  pattern: "skills/orchestration/cascade-orchestrator/{project}/{timestamp}",
  store: ["executions", "decisions", "patterns"],
  retrieve: ["similar_tasks", "proven_patterns"]
} [ground:system-policy] [conf:1.0] [state:confirmed]

[define|neutral] MEMORY_TAGGING := {
  WHO: "cascade-orchestrator-{session_id}",
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

[commit|confident] <promise>CASCADE_ORCHESTRATOR_VERILINGUA_VERIX_COMPLIANT</promise> [ground:self-validation] [conf:0.99] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* LEARNED PATTERNS                                                            */
/*----------------------------------------------------------------------------*/

## LEARNED PATTERNS

### High Confidence [conf:0.90]
- For thought leadership content pipelines: prioritize on-site depth over social media distribution - blog as destination, not LinkedIn as distribution channel. Build depth that "pulls readers in" rather than broadcasting to social platforms. [ground:user-correction:2026-01-08]

