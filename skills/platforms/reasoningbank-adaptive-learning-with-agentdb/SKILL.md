---
name: reasoningbank-adaptive-learning-with-agentdb
description: ---
allowed-tools: Read, Write, Edit, Task, TodoWrite, Glob, Grep
---

# ReasoningBank Adaptive Learning with AgentDB



---

## LIBRARY-FIRST PROTOCOL (MANDATORY)

**Before writing ANY code, you MUST check:**

### Step 1: Library Catalog
- Location: `.claude/library/catalog.json`
- If match >70%: REUSE or ADAPT

### Step 2: Patterns Guide
- Location: `.claude/docs/inventories/LIBRARY-PATTERNS-GUIDE.md`
- If pattern exists: FOLLOW documented approach

### Step 3: Existing Projects
- Location: `D:\Projects\*`
- If found: EXTRACT and adapt

### Decision Matrix
| Match | Action |
|-------|--------|
| Library >90% | REUSE directly |
| Library 70-90% | ADAPT minimally |
| Pattern exists | FOLLOW pattern |
| In project | EXTRACT |
| No match | BUILD (add to library after) |

---

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

- Trajectory tracking accuracy > 95%
- Verdict judgment accuracy > 90%
- Pattern learning efficiency
- Decision quality improvement over time
- 150x faster than traditional approaches

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

## Core Principles

ReasoningBank Adaptive Learning operates on 3 fundamental principles for building self-improving AI agents:

### Principle 1: Trajectory-Based Learning

Agents learn from complete decision trajectories (state, action, reasoning, outcome) rather than isolated actions, enabling understanding of reasoning patterns.

In practice:
- Track full trajectories with steps array containing state, action, reasoning for each decision point, not just final outcomes
- Store context alongside trajectories (input state, constraints, available options) to enable case-based reasoning later
- Record reasoning text explicitly ("Because X and Y") to make decision rationale visible for pattern mining and debugging
- Capture outcome metrics (success/failure, reward value, efficiency score) to enable trajectory evaluation and verdict judgment

### Principle 2: Verdict Judgment System

Evaluate decision quality across multiple criteria (efficiency, correctness, novelty) using structured judgment rather than binary success/failure.

In practice:
- Define multi-dimensional criteria for verdict judgment - efficiency (resource usage), correctness (goal achievement), novelty (exploration)
- Score trajectories on 0-1 scale per criterion with weighted aggregation to identify high-quality reasoning patterns
- Use verdict threshold (0.7 default) to filter trajectories for memory distillation - only learn from proven successful patterns
- Track verdict confidence scores to prioritize learning from high-confidence judgments over uncertain evaluations

### Principle 3: Memory Distillation for Pattern Recognition

Extract and consolidate successful reasoning patterns through pattern mining, pruning ineffective approaches to maintain lean memory.

In practice:
- Run pattern mining on recent trajectories with minimum support (0.1) and confidence (0.8) thresholds to identify frequent successful patterns
- Compress trajectory memory by keeping top 10% highest-scoring patterns, discarding low-value historical data to prevent memory bloat
- Store distilled patterns in AgentDB vector database for fast retrieval (150x faster than exhaustive search) during decision-making
- Apply learned patterns with case-based reasoning - find similar past contexts and reuse successful decision strategies

---

## Common Anti-Patterns

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| **Learning From All Trajectories** | Treating all decisions equally regardless of outcome quality creates noise in learned patterns, degrading decision-making over time | Implement verdict judgment (Phase 3) with threshold filtering (0.7 default) to learn only from high-quality trajectories, pruning ineffective approaches |
| **Storing Raw Trajectories Indefinitely** | Accumulating all historical trajectories without compression causes memory bloat, slow retrieval, and dilutes signal with obsolete patterns | Run memory distillation (Phase 4) periodically to extract patterns, keep top 10% by quality, and prune low-value historical data |
| **Ignoring Reasoning Context** | Recording only actions and outcomes without capturing reasoning and context makes patterns non-transferable to new situations | Store full trajectories with reasoning text and context state (Phase 2) to enable case-based reasoning and debugging decision-making |

---

## Conclusion

ReasoningBank Adaptive Learning with AgentDB provides a framework for building self-improving AI agents that learn from experience through trajectory tracking, verdict judgment, memory distillation, and pattern recognition. By capturing complete decision contexts, evaluating quality across multiple dimensions, and extracting proven patterns, it enables agents to continuously improve decision-making.

This skill excels at building meta-learning systems where agents need to improve over time, reinforcement learning applications requiring trajectory analysis, and decision support systems that learn from historical outcomes. Use this when agents face recurring decision scenarios where learning from past successes and failures can improve future performance.

The 5-phase framework (initialize ReasoningBank, track trajectories, judge verdicts, distill memory, apply learning) provides systematic progression from data collection to active learning. The integration with AgentDB's 150x faster vector search makes it suitable for production environments with real-time decision requirements and large trajectory datasets.