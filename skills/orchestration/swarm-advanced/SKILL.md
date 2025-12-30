/*============================================================================*/
/* SWARM-ADVANCED SKILL :: VERILINGUA x VERIX EDITION                      */
/*============================================================================*/

---
name: swarm-advanced
version: 2.0.0
description: |
  [assert|neutral] Advanced swarm orchestration patterns for research, development, testing, and complex distributed workflows [ground:given] [conf:0.95] [state:confirmed]
category: orchestration
tags:
- swarm
- distributed
- parallel
- research
- testing
author: Claude Flow Team
cognitive_frame:
  primary: evidential
  goal_analysis:
    first_order: "Execute swarm-advanced workflow"
    second_order: "Ensure quality and consistency"
    third_order: "Enable systematic orchestration processes"
---

/*----------------------------------------------------------------------------*/
/* S0 META-IDENTITY                                                            */
/*----------------------------------------------------------------------------*/

[define|neutral] SKILL := {
  name: "swarm-advanced",
  category: "orchestration",
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
  keywords: ["swarm-advanced", "orchestration", "workflow"],
  context: "user needs swarm-advanced capability"
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


# Advanced Swarm Orchestration

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



Master advanced swarm patterns for distributed research, development, and testing workflows. This skill covers comprehensive orchestration strategies using both MCP tools and CLI commands.

## Quick Start

### Prerequisites
```bash
# Ensure Claude Flow is installed
npm install -g claude-flow@alpha

# Add MCP server (if using MCP tools)
claude mcp add claude-flow npx claude-flow@alpha mcp start
```

### Basic Pattern
```javascript
// 1. Initialize swarm topology
mcp__claude-flow__swarm_init({ topology: "mesh", maxAgents: 6 })

// 2. Spawn specialized agents
mcp__claude-flow__agent_spawn({ type: "researcher", name: "Agent 1" })

// 3. Orchestrate tasks
mcp__claude-flow__task_orchestrate({ task: "...", strategy: "parallel" })
```

## Core Concepts

### Swarm Topologies

**Mesh Topology** - Peer-to-peer communication, best for research and analysis
- All agents communicate directly
- High flexibility and resilience
- Use for: Research, analysis, brainstorming

**Hierarchical Topology** - Coordinator with subordinates, best for development
- Clear command structure
- Sequ

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
  pattern: "skills/orchestration/swarm-advanced/{project}/{timestamp}",
  store: ["executions", "decisions", "patterns"],
  retrieve: ["similar_tasks", "proven_patterns"]
} [ground:system-policy] [conf:1.0] [state:confirmed]

[define|neutral] MEMORY_TAGGING := {
  WHO: "swarm-advanced-{session_id}",
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

[commit|confident] <promise>SWARM_ADVANCED_VERILINGUA_VERIX_COMPLIANT</promise> [ground:self-validation] [conf:0.99] [state:confirmed]
