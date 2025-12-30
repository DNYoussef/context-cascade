/*============================================================================*/
/* HIVE-MIND-ADVANCED SKILL :: VERILINGUA x VERIX EDITION                      */
/*============================================================================*/

---
name: hive-mind-advanced
version: 1.0.0
description: |
  [assert|neutral] Advanced Hive Mind collective intelligence system for queen-led multi-agent coordination with consensus mechanisms and persistent memory [ground:given] [conf:0.95] [state:confirmed]
category: coordination
tags:
- hive-mind
- swarm
- queen-worker
- consensus
- collective-intelligence
author: Claude Flow Team
cognitive_frame:
  primary: evidential
  goal_analysis:
    first_order: "Execute hive-mind-advanced workflow"
    second_order: "Ensure quality and consistency"
    third_order: "Enable systematic coordination processes"
---

/*----------------------------------------------------------------------------*/
/* S0 META-IDENTITY                                                            */
/*----------------------------------------------------------------------------*/

[define|neutral] SKILL := {
  name: "hive-mind-advanced",
  category: "coordination",
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
  keywords: ["hive-mind-advanced", "coordination", "workflow"],
  context: "user needs hive-mind-advanced capability"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S3 CORE CONTENT                                                             */
/*----------------------------------------------------------------------------*/

## Orchestration Skill Guidelines

### When to Use This Skill
- **Queen-led coordination** requiring hierarchical multi-agent control
- **Consensus-driven decisions** needing Byzantine fault tolerance
- **Collective intelligence** tasks benefiting from shared memory
- **Strategic planning** with tactical execution delegation
- **Large-scale swarms** with 10+ specialized worker agents

### When NOT to Use This Skill
- **Single-agent tasks** with no coordination requirements
- **Simple workflows** without consensus needs
- **Flat topologies** where hierarchy adds no value
- **Ephemeral tasks** not needing collective memory

### Success Criteria
- [assert|neutral] *Queen successfully coordinates** all worker agents [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] *Consensus achieved** using configured algorithm (majority/weighted/Byzantine) [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] *Collective memory shared** across all agents with <10ms access time [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] *All workers complete tasks** with 100% assignment success [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] *Session state persisted** with checkpoint recovery capability [ground:acceptance-criteria] [conf:0.90] [state:provisional]

### Edge Cases to Handle
- **Queen failure** - Implement queen failover and re-election
- **Worker unresponsiveness** - Timeout detection and task reassignment
- **Consensus deadlock** - Fallback to weighted or majority consensus
- **Memory corruption** - Validate memory integrity with checksums
- **Session crash** - Resume from last checkpoint with full state recovery

### Guardrails (NEVER Violate)
- [assert|emphatic] NEVER: lose collective memory** - Persist to SQLite with WAL mode [ground:policy] [conf:0.98] [state:confirmed]
- [assert|neutral] ALWAYS: validate queen health** - Monitor queen heartbeat continuously [ground:policy] [conf:0.98] [state:confirmed]
- [assert|neutral] ALWAYS: track worker states** - Real-time worker status in shared memory [ground:policy] [conf:0.98] [state:confirmed]
- [assert|emphatic] NEVER: skip consensus** - Critical decisions require configured consensus [ground:policy] [conf:0.98] [state:confirmed]
- [assert|neutral] ALWAYS: checkpoint sessions** - Save state at key milestones [ground:policy] [conf:0.98] [state:confirmed]

### Evidence-Based Validation
- **Verify queen coordination** - Check queen issued commands to all workers
- **Validate consensus results** - Confirm vote counts meet algorithm threshold
- **Check memory consistency** - Query collective memory, verify no conflicts
- **Measure worker efficiency** - Calculate task completion rate per worker
- **Audit session recovery** - Test checkpoint restore, verify full state


# Hive Mind Advanced Skill

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



Master the advanced Hive Mind collective intelligence system for sophisticated multi-agent coordination using queen-led architecture, Byzantine consensus, and collective memory.

## Overview

The Hive Mind system represents the pinnacle of multi-agent coordination in Claude Flow, implementing a queen-led hierarchical architecture where a strategic queen coordinator directs specialized worker agents through collective decision-making and shared memory.

## Core Concepts

### Architecture Patterns

**Queen-Led Coordination**
- Strategic queen agents orchestrate high-level objectives
- Tactical queens manage mid-level execution
- Adaptive queens dynamically adjust strategies based on performance

**Worker Specialization**
- Researcher agents: Analysis and investigation
- Coder agents: Implementation and development
- Analyst agents: Data processing and metrics
- Tester agents: Quality assurance and validation
- Architect agents: System design and planning
- Reviewer agents: Code review and improvement
- Optimi

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
  pattern: "skills/coordination/hive-mind-advanced/{project}/{timestamp}",
  store: ["executions", "decisions", "patterns"],
  retrieve: ["similar_tasks", "proven_patterns"]
} [ground:system-policy] [conf:1.0] [state:confirmed]

[define|neutral] MEMORY_TAGGING := {
  WHO: "hive-mind-advanced-{session_id}",
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

[commit|confident] <promise>HIVE_MIND_ADVANCED_VERILINGUA_VERIX_COMPLIANT</promise> [ground:self-validation] [conf:0.99] [state:confirmed]
