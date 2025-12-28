---
name: ReasoningBank Adaptive Learning with AgentDB
description: No description provided
---

# ReasoningBank Adaptive Learning with AgentDB

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