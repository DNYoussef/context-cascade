---
name: reasoningbank-intelligence
description: Implement adaptive learning with ReasoningBank for pattern recognition, strategy optimization, and continuous improvement. Use when building self-learning agents, optimizing workflows, or implementing meta-cognitive systems.
---

## When NOT to Use This Skill

- Simple fact retrieval without reasoning chains
- Operations that do not require logical inference
- Tasks without complex multi-step reasoning needs
- Applications that do not benefit from reasoning trace storage

## Success Criteria

- Reasoning chain accuracy: >90% logically valid steps
- Retrieval relevance: Top-5 recall >0.85 for similar reasoning
- Storage efficiency: <1MB per 100 reasoning chains
- Query latency: <50ms for reasoning retrieval
- Integration success: Seamless connection with AgentDB backend

## Edge Cases & Error Handling

- **Invalid Reasoning Chains**: Validate logical consistency before storage
- **Retrieval Failures**: Fallback to alternative search strategies
- **Storage Limits**: Implement pruning strategies for old/low-quality chains
- **Embedding Mismatches**: Ensure consistent embedding models across storage/retrieval
- **Circular Reasoning**: Detect and prevent circular reference chains

## Guardrails & Safety

- NEVER store reasoning chains with sensitive or PII data
- ALWAYS validate reasoning quality before storage
- ALWAYS sanitize inputs to prevent prompt injection
- NEVER expose internal reasoning structures in public APIs
- ALWAYS implement access control for reasoning retrieval
- ALWAYS audit reasoning chains for bias and harmful content

## Evidence-Based Validation

- Verify reasoning quality: Check logical consistency and validity
- Validate retrieval: Test that similar reasoning is correctly retrieved
- Monitor storage: Track database size and query performance
- Test edge cases: Validate handling of complex/invalid reasoning chains
- Benchmark improvements: Measure reasoning quality vs baseline methods


# ReasoningBank Intelligence

## What This Skill Does

Implements ReasoningBank's adaptive learning system for AI agents to learn from experience, recognize patterns, and optimize strategies over time. Enables meta-cognitive capabilities and continuous improvement.

## Prerequisites

- agentic-flow v1.5.11+
- AgentDB v1.0.4+ (for persistence)
- Node.js 18+

## Quick Start

```typescript
import { ReasoningBank } from 'agentic-flow/reasoningbank';

// Initialize ReasoningBank
const rb = new ReasoningBank({
  persist: true,
  learningRate: 0.1,
  adapter: 'agentdb' // Use AgentDB for storage
});

// Record task outcome
await rb.recordExperience({
  task: 'code_review',
  approach: 'static_analysis_first',
  outcome: {
    success: true,
    metrics: {
      bugs_found: 5,
      time_taken: 120,
      false_positives: 1
    }
  },
  context: {
    language: 'typescript',
    complexity: 'medium'
  }
});

// Get optimal strategy
const strategy = await rb.recommendStrategy('code_review', {
  language: 'typescript',
  complexity: 'high'
});
```

## Core Features

### 1. Pattern Recognition
```typescript
// Learn patterns from data
await rb.learnPattern({
  pattern: 'api_errors_increase_after_deploy',
  triggers: ['deployment', 'traffic_spike'],
  actions: ['rollback', 'scale_up'],
  confidence: 0.85
});

// Match patterns
const matches = await rb.matchPatterns(currentSituation);
```

### 2. Strategy Optimization
```typescript
// Compare strategies
const comparison = await rb.compareStrategies('bug_fixing', [
  'tdd_approach',
  'debug_first',
  'reproduce_then_fix'
]);

// Get best strategy
const best = comparison.strategies[0];
console.log(`Best: ${best.name} (score: ${best.score})`);
```

### 3. Continuous Learning
```typescript
// Enable auto-learning from all tasks
await rb.enableAutoLearning({
  threshold: 0.7,        // Only learn from high-confidence outcomes
  updateFrequency: 100   // Update models every 100 experiences
});
```

## Advanced Usage

### Meta-Learning
```typescript
// Learn about learning
await rb.metaLearn({
  observation: 'parallel_execution_faster_for_independent_tasks',
  confidence: 0.95,
  applicability: {
    task_types: ['batch_processing', 'data_transformation'],
    conditions: ['tasks_independent', 'io_bound']
  }
});
```

### Transfer Learning
```typescript
// Apply knowledge from one domain to another
await rb.transferKnowledge({
  from: 'code_review_javascript',
  to: 'code_review_typescript',
  similarity: 0.8
});
```

### Adaptive Agents
```typescript
// Create self-improving agent
class AdaptiveAgent {
  async execute(task: Task) {
    // Get optimal strategy
    const strategy = await rb.recommendStrategy(task.type, task.context);

    // Execute with strategy
    const result = await this.executeWithStrategy(task, strategy);

    // Learn from outcome
    await rb.recordExperience({
      task: task.type,
      approach: strategy.name,
      outcome: result,
      context: task.context
    });

    return result;
  }
}
```

## Integration with AgentDB

```typescript
// Persist ReasoningBank data
await rb.configure({
  storage: {
    type: 'agentdb',
    options: {
      database: './reasoning-bank.db',
      enableVectorSearch: true
    }
  }
});

// Query learned patterns
const patterns = await rb.query({
  category: 'optimization',
  minConfidence: 0.8,
  timeRange: { last: '30d' }
});
```

## Performance Metrics

```typescript
// Track learning effectiveness
const metrics = await rb.getMetrics();
console.log(`
  Total Experiences: ${metrics.totalExperiences}
  Patterns Learned: ${metrics.patternsLearned}
  Strategy Success Rate: ${metrics.strategySuccessRate}
  Improvement Over Time: ${metrics.improvement}
`);
```

## Best Practices

1. **Record consistently**: Log all task outcomes, not just successes
2. **Provide context**: Rich context improves pattern matching
3. **Set thresholds**: Filter low-confidence learnings
4. **Review periodically**: Audit learned patterns for quality
5. **Use vector search**: Enable semantic pattern matching

## Troubleshooting

### Issue: Poor recommendations
**Solution**: Ensure sufficient training data (100+ experiences per task type)

### Issue: Slow pattern matching
**Solution**: Enable vector indexing in AgentDB

### Issue: Memory growing large
**Solution**: Set TTL for old experiences or enable pruning

## Learn More

- ReasoningBank Guide: agentic-flow/src/reasoningbank/README.md
- AgentDB Integration: packages/agentdb/docs/reasoningbank.md
- Pattern Learning: docs/reasoning/patterns.md
## Core Principles

1. **Meta-Cognitive Learning Loop**: ReasoningBank Intelligence enables agents to not just execute tasks, but observe their own execution patterns (meta-learning), creating second-order knowledge like "parallel execution is 3x faster for independent I/O tasks" that informs strategy selection across domains rather than task-specific solutions.

2. **Experience-Driven Strategy Optimization**: Instead of hardcoded heuristics, strategy recommendation is empirically derived from recorded outcomes - comparing tdd_approach vs debug_first for bug_fixing based on actual metrics (time_taken, bugs_found, false_positives) across 100+ experiences, selecting the proven best performer for given context (language, complexity).

3. **Bounded Auto-Learning with Confidence Thresholds**: Automatic pattern recording only activates for high-confidence outcomes (threshold 0.7), preventing noise accumulation from failed experiments or ambiguous results, while still capturing validated learnings that improve agent performance over time without manual curation.

## Anti-Patterns

| Anti-Pattern | Why It Fails | Correct Approach |
|--------------|--------------|------------------|
| Learning from every task outcome | Low-confidence experiences (debugging session that partially succeeded) pollute pattern library, reducing recommendation quality | Set learningRate threshold (0.7+), only record experiences with clear success/failure signals and measurable metrics |
| Applying domain knowledge without transfer validation | Blindly applying "code_review_javascript" patterns to "code_review_rust" ignores language differences (borrow checker, lifetimes), causing incorrect strategy selection | Use transferKnowledge() with similarity scoring (0.8+), validate transferred patterns against domain-specific constraints |
| Ignoring context in strategy comparison | Recommending "static_analysis_first" for high-complexity Rust code because it worked for simple JavaScript, despite different complexity demands | Always include context in recordExperience() (language, complexity, timeConstraints) and filter strategy recommendations by matching context |

## Conclusion

ReasoningBank Intelligence transforms agents from stateless executors to adaptive learners, accumulating strategic knowledge (not just data) through the recordExperience -> recommendStrategy -> metaLearn feedback loop. This creates compounding returns: an agent with 1000+ experiences can select optimal approaches in <50ms, while a fresh agent spends minutes exploring suboptimal strategies, multiplying this advantage across every task.

The critical success factor is pattern quality over quantity - 100 high-confidence, context-rich experiences (learningRate 0.8, detailed metrics) outperform 10,000 noisy records. When implementing adaptive agents, start with manual experience recording for the first 50 tasks, review learned patterns for correctness, then enable auto-learning only after validating the system learns true patterns (not spurious correlations like "bug fixes succeed more on Tuesdays"). The goal is not to record everything, but to capture the crystallized knowledge that makes future decisions measurably better - tracked via strategy success rate increasing over time (target >85% after 500+ experiences).