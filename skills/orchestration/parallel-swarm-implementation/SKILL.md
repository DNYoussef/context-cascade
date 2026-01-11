/*============================================================================*/
/* PARALLEL-SWARM-IMPLEMENTATION SKILL :: VERILINGUA x VERIX EDITION                      */
/*============================================================================*/

---
name: parallel-swarm-implementation
version: 1.0.0
description: |
  [assert|neutral] Loop 2 of the Three-Loop Integrated Development System. META-SKILL that dynamically compiles Loop 1 plans into agent+skill execution graphs. Queen Coordinator selects optimal agents from 86-agent regi [ground:given] [conf:0.95] [state:confirmed]
category: orchestration
tags:
- orchestration
- coordination
- swarm
author: ruv
cognitive_frame:
  primary: evidential
  goal_analysis:
    first_order: "Execute parallel-swarm-implementation workflow"
    second_order: "Ensure quality and consistency"
    third_order: "Enable systematic orchestration processes"
---

/*----------------------------------------------------------------------------*/
/* S0 META-IDENTITY                                                            */
/*----------------------------------------------------------------------------*/

[define|neutral] SKILL := {
  name: "parallel-swarm-implementation",
  category: "orchestration",
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
  keywords: ["parallel-swarm-implementation", "orchestration", "workflow"],
  context: "user needs parallel-swarm-implementation capability"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S3 CORE CONTENT                                                             */
/*----------------------------------------------------------------------------*/

## Orchestration Skill Guidelines

### When to Use This Skill
- **Parallel multi-agent execution** requiring concurrent task processing
- **Complex implementation** with 6+ independent tasks
- **Theater-free development** requiring 0% tolerance validation
- **Dynamic agent selection** from 86+ agent registry
- **High-quality delivery** needing Byzantine consensus validation

### When NOT to Use This Skill
- **Single-agent tasks** with no parallelization benefit
- **Simple sequential work** completing in <2 hours
- **Planning phase** (use research-driven-planning first)
- **Trivial changes** to single files

### Success Criteria
- [assert|neutral] *Agent+skill matrix generated** with optimal assignments [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] *Parallel execution successful** with 8.3x speedup achieved [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] *Theater detection passes** with 0% theater detected [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] *Integration tests pass** at 100% rate [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] *All agents complete** with no orphaned workers [ground:acceptance-criteria] [conf:0.90] [state:provisional]

### Edge Cases to Handle
- **Agent failures** - Implement agent health monitoring and replacement
- **Task timeout** - Configure per-task timeout with escalation
- **Consensus failure** - Have fallback from Byzantine to weighted consensus
- **Resource exhaustion** - Limit max parallel agents, queue excess
- **Conflicting outputs** - Implement merge conflict resolution strategy

### Guardrails (NEVER Violate)
- [assert|emphatic] NEVER: lose agent state** - Persist agent progress to memory continuously [ground:policy] [conf:0.98] [state:confirmed]
- [assert|neutral] ALWAYS: track swarm health** - Monitor all agent statuses in real-time [ground:policy] [conf:0.98] [state:confirmed]
- [assert|neutral] ALWAYS: validate consensus** - Require 4/5 agreement for theater detection [ground:policy] [conf:0.98] [state:confirmed]
- [assert|emphatic] NEVER: skip theater audit** - Zero tolerance, any theater blocks merge [ground:policy] [conf:0.98] [state:confirmed]
- [assert|neutral] ALWAYS: cleanup workers** - Terminate agents on completion/failure [ground:policy] [conf:0.98] [state:confirmed]

### Evidence-Based Validation
- **Check all agent statuses** - Verify each agent completed successfully
- **Validate parallel execution** - Confirm tasks ran concurrently, not sequentially
- **Measure speedup** - Calculate actual speedup vs sequential baseline
- **Audit theater detection** - Run 6-agent consensus, verify 0% detection
- **Verify integration** - Execute sandbox tests, confirm 100% pass rate


# Parallel Swarm Implementation (Loop 2) - META-SKILL

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



## Purpose

**META-SKILL ORCHESTRATOR** that dynamically compiles Loop 1 planning packages into executable agent+skill graphs, then coordinates theater-free parallel implementation.

## Specialist Agent Coordination

I am **Queen Coordinator (Seraphina)** orchestrating the "swarm compiler" pattern.

**Meta-Skill Architecture**:
1. **Analyze** Loop 1 planning package
2. **Select** optimal agents from 86-agent registry per task
3. **Assign** skills to agents (when skills exist) OR generate custom instructions
4. **Create** agent+skill assignment matrix
5. **Execute** dynamically based on matrix with continuous monitoring
6. **Validate** theater-free execution through multi-agent consensus

**Methodology** (9-Step Adaptive SOP):
1. **Initialization**: Queen-led hierarchical topology with dual memory
2. **Analysis**: Queen analyzes Loop 1 plan and creates agent+skill matrix
3. **MECE Validation**: Ensure tasks are Mutually Exclusive, Collectively Exhaustive
4. **Dynamic Deployment**: Spawn agents with skills OR custom instructions per matrix
5. **T

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
  pattern: "skills/orchestration/parallel-swarm-implementation/{project}/{timestamp}",
  store: ["executions", "decisions", "patterns"],
  retrieve: ["similar_tasks", "proven_patterns"]
} [ground:system-policy] [conf:1.0] [state:confirmed]

[define|neutral] MEMORY_TAGGING := {
  WHO: "parallel-swarm-implementation-{session_id}",
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

[commit|confident] <promise>PARALLEL_SWARM_IMPLEMENTATION_VERILINGUA_VERIX_COMPLIANT</promise> [ground:self-validation] [conf:0.99] [state:confirmed]
