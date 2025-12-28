---
name: agentdb-learning-plugins
description: Create AI learning plugins using AgentDB's 9 reinforcement learning algorithms. Train Decision Transformer, Q-Learning, SARSA, and Actor-Critic models. Deploy these plugins to build self-learning agents, implement RL workflows, and optimize agent behavior through experience. Apply offline RL for safe learning from logged data.
---

## When NOT to Use This Skill

- Local-only operations with no vector search needs
- Simple key-value storage without semantic similarity
- Real-time streaming data without persistence requirements
- Operations that do not require embedding-based retrieval

## Success Criteria

- Vector search query latency: <10ms for 99th percentile
- Embedding generation: <100ms per document
- Index build time: <1s per 1000 vectors
- Recall@10: >0.95 for similar documents
- Database connection success rate: >99.9%
- Memory footprint: <2GB for 1M vectors with quantization

## Edge Cases & Error Handling

- **Rate Limits**: AgentDB local instances have no rate limits; cloud deployments may vary
- **Connection Failures**: Implement retry logic with exponential backoff (max 3 retries)
- **Index Corruption**: Maintain backup indices; rebuild from source if corrupted
- **Memory Overflow**: Use quantization (4-bit, 8-bit) to reduce memory by 4-32x
- **Stale Embeddings**: Implement TTL-based refresh for dynamic content
- **Dimension Mismatch**: Validate embedding dimensions (384 for sentence-transformers) before insertion

## Guardrails & Safety

- NEVER expose database connection strings in logs or error messages
- ALWAYS validate vector dimensions before insertion
- ALWAYS sanitize metadata to prevent injection attacks
- NEVER store PII in vector metadata without encryption
- ALWAYS implement access control for multi-tenant deployments
- ALWAYS validate search results before returning to users

## Evidence-Based Validation

- Verify database health: Check connection status and index integrity
- Validate search quality: Measure recall/precision on test queries
- Monitor performance: Track query latency, throughput, and memory usage
- Test failure recovery: Simulate connection drops and index corruption
- Benchmark improvements: Compare against baseline metrics (e.g., 150x speedup claim)


# AgentDB Learning Plugins

## What This Skill Does

**Use this skill to** create, train, and deploy learning plugins for autonomous agents using AgentDB's 9 reinforcement learning algorithms. **Implement** offline RL (Decision Transformer) for safe learning from logged experiences. **Apply** value-based learning (Q-Learning) for discrete actions. **Deploy** policy gradients (Actor-Critic) for continuous control. **Enable** agents to improve through experience with WASM-accelerated neural inference.

**Performance**: Train models 10-100x faster with WASM-accelerated neural inference.

## Prerequisites

- Node.js 18+
- AgentDB v1.0.7+ (via agentic-flow)
- Basic understanding of reinforcement learning (recommended)



## Quick Start with API

```typescript
import { createAgentDBAdapter } from 'agentic-flow/reasoningbank';

// Initialize with learning enabled
const adapter = await createAgentDBAdapter({
  dbPath: '.agentdb/learning.db',
  enableLearning: true,       // Enable learning plugins
  enableReasoning: true,
  cacheSize: 1000,
});

// Store training experience
await adapter.insertPattern({
  id: '',
  type: 'experience',
  domain: 'game-playing',
  pattern_data: JSON.stringify({
    embedding: await computeEmbedding('state-action-reward'),
    pattern: {
      state: [0.1, 0.2, 0.3],
      action: 2,
      reward: 1.0,
      next_state: [0.15, 0.25, 0.35],
      done: false
    }
  }),
  confidence: 0.9,
  usage_count: 1,
  success_count: 1,
  created_at: Date.now(),
  last_used: Date.now(),
});

// Train learning model
const metrics = await adapter.train({
  epochs: 50,
  batchSize: 32,
});

console.log('Training Loss:', metrics.loss);
console.log('Duration:', metrics.duration, 'ms');
```



## Training Workflow

### 1. Collect Experiences

```typescript
// Store experiences during agent execution
for (let i = 0; i < numEpisodes; i++) {
  const episode = runEpisode();

  for (const step of episode.steps) {
    await adapter.insertPattern({
      id: '',
      type: 'experience',
      domain: 'task-domain',
      pattern_data: JSON.stringify({
        embedding: await computeEmbedding(JSON.stringify(step)),
        pattern: {
          state: step.state,
          action: step.action,
          reward: step.reward,
          next_state: step.next_state,
          done: step.done
        }
      }),
      confidence: step.reward > 0 ? 0.9 : 0.5,
      usage_count: 1,
      success_count: step.reward > 0 ? 1 : 0,
      created_at: Date.now(),
      last_used: Date.now(),
    });
  }
}
```

### 2. Train Model

```typescript
// Train on collected experiences
const trainingMetrics = await adapter.train({
  epochs: 100,
  batchSize: 64,
  learningRate: 0.001,
  validationSplit: 0.2,
});

console.log('Training Metrics:', trainingMetrics);
// {
//   loss: 0.023,
//   valLoss: 0.028,
//   duration: 1523,
//   epochs: 100
// }
```

### 3. Evaluate Performance

```typescript
// Retrieve similar successful experiences
const testQuery = await computeEmbedding(JSON.stringify(testState));
const result = await adapter.retrieveWithReasoning(testQuery, {
  domain: 'task-domain',
  k: 10,
  synthesizeContext: true,
});

// Evaluate action quality
const suggestedAction = result.memories[0].pattern.action;
const confidence = result.memories[0].similarity;

console.log('Suggested Action:', suggestedAction);
console.log('Confidence:', confidence);
```



## Performance Optimization

### Batch Training

```typescript
// Collect batch of experiences
const experiences = collectBatch(size: 1000);

// Batch insert (500x faster)
for (const exp of experiences) {
  await adapter.insertPattern({ /* ... */ });
}

// Train on batch
await adapter.train({
  epochs: 10,
  batchSize: 128,  // Larger batch for efficiency
});
```

### Incremental Learning

```typescript
// Train incrementally as new data arrives
setInterval(async () => {
  const newExperiences = getNewExperiences();

  if (newExperiences.length > 100) {
    await adapter.train({
      epochs: 5,
      batchSize: 32,
    });
  }
}, 60000);  // Every minute
```



## CLI Operations

```bash
# Create plugin
npx agentdb@latest create-plugin -t decision-transformer -n my-plugin

# List plugins
npx agentdb@latest list-plugins

# Get plugin info
npx agentdb@latest plugin-info my-plugin

# List templates
npx agentdb@latest list-templates
```



## Learn More

- **Algorithm Papers**: See docs/algorithms/ for detailed papers
- **GitHub**: https://github.com/ruvnet/agentic-flow/tree/main/packages/agentdb
- **MCP Integration**: `npx agentdb@latest mcp`
- **Website**: https://agentdb.ruv.io

-----------|---------|----------|
| **Online Training Without Replay Buffer** | Each experience used once then discarded, requiring 10-100x more environment interactions | Store experiences in AgentDB with embeddings; sample random batches (32-64) for training; reuse high-value transitions |
| **Wrong Algorithm for Problem Type** | Q-Learning on continuous actions requires discretization (action space explosion), Actor-Critic on small discrete spaces wastes capacity | Match algorithm to action space: Q-Learning/SARSA for discrete (<100 actions), Actor-Critic/PPO for continuous, Decision Transformer for offline |
| **Ignoring Confidence and Usage Tracking** | All experiences weighted equally despite varying quality and relevance | Store confidence (reward-based or TD-error), increment usage_count/success_count; prioritize high-confidence experiences; prune low-quality patterns |

## Conclusion

AgentDB Learning Plugins transforms static vector databases into self-improving AI systems by integrating 9 reinforcement learning algorithms with persistent memory for experience accumulation and retrieval. By storing experiences as embeddings in AgentDB, agents learn from past successes and failures, retrieve similar patterns for transfer learning, and continuously improve through offline RL without risking catastrophic exploration.

Use this skill when building autonomous agents requiring continuous improvement (chatbots, recommendation systems, game AI), implementing safe learning from historical data (medical diagnosis, financial trading), or enabling multi-agent knowledge sharing through federated learning. The key insight is persistence: unlike traditional RL where experiences are discarded after training, AgentDB stores them permanently for retrieval, reuse, and transfer across tasks. Start with Decision Transformer for safe offline learning from logged data, add experience replay for sample efficiency, and enable distributed training when scaling to multiple agents or environments.