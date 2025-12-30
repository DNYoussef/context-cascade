/*============================================================================*/
/* WHEN-COORDINATING-COLLECTIVE-INTELLIGENCE-USE-HIVE-MIND SKILL :: VERILINGUA x VERIX EDITION                      */
/*============================================================================*/

---
name: when-coordinating-collective-intelligence-use-hive-mind
version: 1.0.0
description: |
  [assert|neutral] Advanced Hive Mind collective intelligence for queen-led multi-agent coordination with consensus and memory [ground:given] [conf:0.95] [state:confirmed]
category: coordination
tags:
- hive-mind
- collective-intelligence
- consensus
- queen-coordinator
- distributed-memory
author: system
cognitive_frame:
  primary: evidential
  goal_analysis:
    first_order: "Execute when-coordinating-collective-intelligence-use-hive-mind workflow"
    second_order: "Ensure quality and consistency"
    third_order: "Enable systematic coordination processes"
---

/*----------------------------------------------------------------------------*/
/* S0 META-IDENTITY                                                            */
/*----------------------------------------------------------------------------*/

[define|neutral] SKILL := {
  name: "when-coordinating-collective-intelligence-use-hive-mind",
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
  keywords: ["when-coordinating-collective-intelligence-use-hive-mind", "coordination", "workflow"],
  context: "user needs when-coordinating-collective-intelligence-use-hive-mind capability"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S3 CORE CONTENT                                                             */
/*----------------------------------------------------------------------------*/

# Hive Mind Collective Intelligence SOP

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



## Overview

Implement advanced Hive Mind collective intelligence system with queen-led coordination, consensus mechanisms, persistent memory, and distributed decision-making.

## Agents & Responsibilities

### collective-intelligence-coordinator
**Role:** Coordinate collective intelligence processing
**Responsibilities:**
- Aggregate agent insights
- Synthesize collective knowledge
- Identify patterns across agents
- Facilitate group learning

### queen-coordinator
**Role:** Lead and direct hive activities
**Responsibilities:**
- Set strategic direction
- Prioritize tasks
- Resolve conflicts
- Make final decisions

### swarm-memory-manager
**Role:** Manage shared memory and knowledge base
**Responsibilities:**
- Store collective memory
- Synchronize agent states
- Maintain knowledge graph
- Ensure data consistency

## Phase 1: Initialize Hive Mind

### Objective
Establish Hive Mind infrastructure with queen and collective intelligence systems.

### Scripts

```bash
# Initialize Hive Mind
npx claude-flow@alpha hive init \
  --queen-enabled \
  --collective-intelligence \
  --consensus-mechanism "proof-of-intelligence" \
  --max-agents 20

# Spawn queen coordinator
npx claude-flow@alpha agent spawn \
  --type coordinator \
  --role "queen-coordinator" \
  --capabilities "strategic-direction,conflict-resolution,final-decisions"

# Spawn collective intelligence coordinator
npx claude-flow@alpha agent spawn \
  --type coordinator \
  --role "collective-intelligence-coordinator" \
  --capabilities "insight-aggregation,pattern-recognition,group-learning"

# Spawn memory manager
npx claude-flow@alpha agent spawn \
  --type coordinator \
  --role "swarm-memory-manager" \
  --capabilities "memory-storage,state-sync,knowledge-graph"

# Initialize shared memory
npx claude-flow@alpha memory init \
  --type "distributed" \
  --replication 3 \
  --consistency "strong"

# Verify Hive Mind status
npx claude-flow@alpha hive status --show-queen --show-collective
```

### Hive Mind Architecture

**Queen Layer:**
```
Queen Coordinator
    ↓
Strategic Direction
    ↓
Task Prioritization
    ↓
Final Decisions
```

**Collective Intelligence Layer:**
```
Agent 1 → Insights →┐
Agent 2 → Insights →├─ Collective Intelligence → Synthesis
Agent 3 → Insights →│
Agent N → Insights →┘
```

**Memory Layer:**
```
Local Memory ←→ Swarm Memory Manager ←→ Distributed Memory Store
```

### Memory Patterns

```bash
# Store hive configuration
npx claude-flow@alpha memory store \
  --key "hive/config" \
  --value '{
    "queenEnabled": true,
    "consensusMechanism": "proof-of-intelligence",
    "maxAgents": 20,
    "initialized": "'$(date -Iseconds)'"
  }'

# Initialize collective memory
npx claude-flow@alpha memory store \
  --key "hive/collective/insights" \
  --value '[]'

npx claude-flow@alpha memory store \
  --key "hive/collective/patterns" \
  --value '{}'
```

## Phase 2: Coordinate Agents

### Objective
Queen-led coordination of agent activities and task assignments.

### Scripts

```bash
# Spawn worker agents
for i in {1..5}; do
  npx claude-flow@alpha agent spawn \
    --type researcher \
    --hive-member \
    --report-to queen
done

for i in {1..5}; do
  npx claude-flow@alpha agent spawn \
    --type coder \
    --hive-member \
    --report-to queen
done

# Queen assigns tasks
npx claude-flow@alpha hive assign \
  --task "Analyze codebase" \
  --agents "researcher-*" \
  --priority high

npx claude-flow@alpha hive assign \
  --task "Implement features" \
  --agents "coder-*" \
  --priority high \
  --depends-on "Analyze codebase"

# Monitor coordination
npx claude-flow@alpha hive monitor \
  --show-assignments \
  --show-progress \
  --interval 10

# Queen reviews progress
npx claude-flow@alpha hive review \
  --by queen \
  --output review-report.json
```

### Queen Decision Process

```bash
#!/bin/bash
# queen-decision-process.sh

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
  pattern: "skills/coordination/when-coordinating-collective-intelligence-use-hive-mind/{project}/{timestamp}",
  store: ["executions", "decisions", "patterns"],
  retrieve: ["similar_tasks", "proven_patterns"]
} [ground:system-policy] [conf:1.0] [state:confirmed]

[define|neutral] MEMORY_TAGGING := {
  WHO: "when-coordinating-collective-intelligence-use-hive-mind-{session_id}",
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

[commit|confident] <promise>WHEN_COORDINATING_COLLECTIVE_INTELLIGENCE_USE_HIVE_MIND_VERILINGUA_VERIX_COMPLIANT</promise> [ground:self-validation] [conf:0.99] [state:confirmed]
