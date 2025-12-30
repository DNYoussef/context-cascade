/*============================================================================*/
/* REASONINGBANK ADAPTIVE LEARNING WITH AGENTDB SKILL :: VERILINGUA x VERIX EDITION                      */
/*============================================================================*/

---
name: ReasoningBank Adaptive Learning with AgentDB
version: 1.0.0
description: |
  [assert|neutral] ReasoningBank Adaptive Learning with AgentDB skill for agentdb workflows [ground:given] [conf:0.95] [state:confirmed]
category: agentdb
tags:
- general
author: system
cognitive_frame:
  primary: evidential
  goal_analysis:
    first_order: "Execute ReasoningBank Adaptive Learning with AgentDB workflow"
    second_order: "Ensure quality and consistency"
    third_order: "Enable systematic agentdb processes"
---

/*----------------------------------------------------------------------------*/
/* S0 META-IDENTITY                                                            */
/*----------------------------------------------------------------------------*/

[define|neutral] SKILL := {
  name: "ReasoningBank Adaptive Learning with AgentDB",
  category: "agentdb",
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
  keywords: ["ReasoningBank Adaptive Learning with AgentDB", "agentdb", "workflow"],
  context: "user needs ReasoningBank Adaptive Learning with AgentDB capability"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S3 CORE CONTENT                                                             */
/*----------------------------------------------------------------------------*/

# ReasoningBank Adaptive Learning with AgentDB

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



## Overview

Implement ReasoningBank adaptive learning with AgentDB's 150x faster vector database for trajectory tracking, verdict judgment, memory distillation, and pattern recognition. Build self-learning agents that improve decision-making through experience.

## SOP Framework: 5-Phase Adaptive Learning

### Phase 1: Initialize ReasoningBank (1-2 hours)
- Setup AgentDB with ReasoningBank
- Configure trajectory tracking
- Initialize verdict system

### Phase 2: Track Trajectories (2-3 hours)
- Record agent decisions
- Store reasoning paths
- Capture context and outcomes

### Phase 3: Judge Verdicts (2-3 hours)
- Evaluate decision quality
- Score reasoning paths
- Identify successful patterns

### Phase 4: Distill Memory (2-3 hours)
- Extract learned patterns
- Consolidate successful strategies
- Prune ineffective approaches

### Phase 5: Apply Learning (1-2 hours)
- Use learned patterns in decisions
- Improve future reasoning
- Measure improvement

## Quick Start

```typescript
import { AgentDB, ReasoningBank } from 'reasoningbank-agentdb';

// Initialize
const db = new AgentDB({
  name: 'reasoning-db',
  dimensions: 768,
  features: { reasoningBank: true }
});

const reasoningBank = new ReasoningBank({
  database: db,
  trajectoryWindow: 1000,
  verdictThreshold: 0.7
});

// Track trajectory
await reasoningBank.trackTrajectory({
  agent: 'agent-1',
  decision: 'action-A',
  reasoning: 'Because X and Y',
  context: { state: currentState },
  timestamp: Date.now()
});

// Judge verdict
const verdict = await reasoningBank.judgeVerdict({
  trajectory: trajectoryId,
  outcome: { success: true, reward: 10 },
  criteria: ['efficiency', 'correctness']
});

// Learn patterns
const patterns = await reasoningBank.distillPatterns({
  minSupport: 0.1,
  confidence: 0.8
});

// Apply learning
const decision = await reasoningBank.makeDecision({
  context: currentContext,
  useLearned: true
});
```

## ReasoningBank Components

### Trajectory Tracking
```typescript
const trajectory = {
  agent: 'agent-1',
  steps: [
    { state: s0, action: a0, reasoning: r0 },
    { state: s1, action: a1, reasoning: r1 }
  ],
  outcome: { success: true, reward: 10 }
};

await reasoningBank.storeTrajectory(trajectory);
```

### Verdict Judgment
```typescript
const verdict = await reasoningBank.judge({
  trajectory: trajectory,
  criteria: {
    efficiency: 0.8,
    correctness: 0.9,
    novelty: 0.6
  }
});
```

### Memory Distillation
```typescript
const distilled = await reasoningBank.distill({
  trajectories: recentTrajectories,
  method: 'pattern-mining',
  compression: 0.1 // Keep top 10%
});
```

### Pattern Application
```typescript
const enhanced = await reasoningBank.enhance({
  query: newProblem,
  patterns: learnedPatterns,
  strategy: 'case-based'
});
```

## Success Metrics
- [assert|neutral] Trajectory tracking accuracy > 95% [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] Verdict judgment accuracy > 90% [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] Pattern learning efficiency [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] Decision quality improvement over time [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] 150x faster than traditional approaches [ground:acceptance-criteria] [conf:0.90] [state:provisional]

## MCP Requirements

This skill operates using AgentDB's npm package and API only. No additional MCP servers required.

All AgentDB/ReasoningBank operations are performed through:
- npm CLI: `npx agentdb@latest`
- TypeScript/JavaScript API: `import { AgentDB, ReasoningBank } from 'reasoningbank-agentdb'`

## Additional Resources

- Full docs: SKILL.md
- ReasoningBank Guide: https://reasoningbank.dev
- AgentDB Integration: https://agentdb.dev/docs/reasoningbank

---

## Core Principl

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
  pattern: "skills/agentdb/ReasoningBank Adaptive Learning with AgentDB/{project}/{timestamp}",
  store: ["executions", "decisions", "patterns"],
  retrieve: ["similar_tasks", "proven_patterns"]
} [ground:system-policy] [conf:1.0] [state:confirmed]

[define|neutral] MEMORY_TAGGING := {
  WHO: "ReasoningBank Adaptive Learning with AgentDB-{session_id}",
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

[commit|confident] <promise>REASONINGBANK ADAPTIVE LEARNING WITH AGENTDB_VERILINGUA_VERIX_COMPLIANT</promise> [ground:self-validation] [conf:0.99] [state:confirmed]
