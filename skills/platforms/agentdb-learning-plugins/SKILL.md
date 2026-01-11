---
name: agentdb-learning-plugins
description: Create AI learning plugins using AgentDBs 9 reinforcement learning algorithms. Train Decision Transformer, Q-Learning, SARSA, and Actor-Critic models. Deploy these plugins to build self-learning agents, implement RL workflows, and optimize agent behavior through experience. Apply offline RL for safe learning from logged data.
allowed-tools: Read, Write, Edit, Bash, Task, TodoWrite, Glob, Grep, WebFetch
---



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

---

## Quick Start with CLI

### Create Learning Plugin

```bash
# Interactive wizard
npx agentdb@latest create-plugin

# Use specific template
npx agentdb@latest create-plugin -t decision-transformer -n my-agent

# Preview without creating
npx agentdb@latest create-plugin -t q-learning --dry-run

# Custom output directory
npx agentdb@latest create-plugin -t actor-critic -o ./plugins
```

### List Available Templates

```bash
# Show all plugin templates
npx agentdb@latest list-templates

# Available templates:
# - decision-transformer (sequence modeling RL - recommended)
# - q-learning (value-based learning)
# - sarsa (on-policy TD learning)
# - actor-critic (policy gradient with baseline)
# - curiosity-driven (exploration-based)
```

### Manage Plugins

```bash
# List installed plugins
npx agentdb@latest list-plugins

# Get plugin information
npx agentdb@latest plugin-info my-agent

# Shows: algorithm, configuration, training status
```

---

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

---

## Available Learning Algorithms (9 Total)

### 1. Decision Transformer (Recommended)

**Type**: Offline Reinforcement Learning
**Best For**: Learning from logged experiences, imitation learning
**Strengths**: No online interaction needed, stable training

```bash
npx agentdb@latest create-plugin -t decision-transformer -n dt-agent
```

**Use Cases**:
- Learn from historical data
- Imitation learning from expert demonstrations
- Safe learning without environment interaction
- Sequence modeling tasks

**Configuration**:
```json
{
  "algorithm": "decision-transformer",
  "model_size": "base",
  "context_length": 20,
  "embed_dim": 128,
  "n_heads": 8,
  "n_layers": 6
}
```

### 2. Q-Learning

**Type**: Value-Based RL (Off-Policy)
**Best For**: Discrete action spaces, sample efficiency
**Strengths**: Proven, simple, works well for small/medium problems

```bash
npx agentdb@latest create-plugin -t q-learning -n q-agent
```

**Use Cases**:
- Grid worlds, board games
- Navigation tasks
- Resource allocation
- Discrete decision-making

**Configuration**:
```json
{
  "algorithm": "q-learning",
  "learning_rate": 0.001,
  "gamma": 0.99,
  "epsilon": 0.1,
  "epsilon_decay": 0.995
}
```

### 3. SARSA

**Type**: Value-Based RL (On-Policy)
**Best For**: Safe exploration, risk-sensitive tasks
**Strengths**: More conservative than Q-Learning, better for safety

```bash
npx agentdb@latest create-plugin -t sarsa -n sarsa-agent
```

**Use Cases**:
- Safety-critical applications
- Risk-sensitive decision-making
- Online learning with exploration

**Configuration**:
```json
{
  "algorithm": "sarsa",
  "learning_rate": 0.001,
  "gamma": 0.99,
  "epsilon": 0.1
}
```

### 4. Actor-Critic

**Type**: Policy Gradient with Value Baseline
**Best For**: Continuous actions, variance reduction
**Strengths**: Stable, works for continuous/discrete actions

```bash
npx agentdb@latest create-plugin -t actor-critic -n ac-agent
```

**Use Cases**:
- Continuous control (robotics, simulations)
- Complex action spaces
- Multi-agent coordination

**Configuration**:
```json
{
  "algorithm": "actor-critic",
  "actor_lr": 0.001,
  "critic_lr": 0.002,
  "gamma": 0.99,
  "entropy_coef": 0.01
}
```

### 5. Active Learning

**Type**: Query-Based Learning
**Best For**: Label-efficient learning, human-in-the-loop
**Strengths**: Minimizes labeling cost, focuses on uncertain samples

**Use Cases**:
- Human feedback incorporation
- Label-efficient training
- Uncertainty sampling
- Annotation cost reduction

### 6. Adversarial Training

**Type**: Robustness Enhancement
**Best For**: Safety, robustness to perturbations
**Strengths**: Improves model robustness, adversarial defense

**Use Cases**:
- Security applications
- Robust decision-making
- Adversarial defense
- Safety testing

### 7. Curriculum Learning

**Type**: Progressive Difficulty Training
**Best For**: Complex tasks, faster convergence
**Strengths**: Stable learning, faster convergence on hard tasks

**Use Cases**:
- Complex multi-stage tasks
- Hard exploration problems
- Skill composition
- Transfer learning

### 8. Federated Learning

**Type**: Distributed Learning
**Best For**: Privacy, distributed data
**Strengths**: Privacy-preserving, scalable

**Use Cases**:
- Multi-agent systems
- Privacy-sensitive data
- Distributed training
- Collaborative learning

### 9. Multi-Task Learning

**Type**: Transfer Learning
**Best For**: Related tasks, knowledge sharing
**Strengths**: Faster learning on new tasks, better generalization

**Use Cases**:
- Task families
- Transfer learning
- Domain adaptation
- Meta-learning

---

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

---

## Advanced Training Techniques

### Experience Replay

```typescript
// Store experiences in buffer
const replayBuffer = [];

// Sample random batch for training
const batch = sampleRandomBatch(replayBuffer, batchSize: 32);

// Train on batch
await adapter.train({
  data: batch,
  epochs: 1,
  batchSize: 32,
});
```

### Prioritized Experience Replay

```typescript
// Store experiences with priority (TD error)
await adapter.insertPattern({
  // ... standard fields
  confidence: tdError,  // Use TD error as confidence/priority
  // ...
});

// Retrieve high-priority experiences
const highPriority = await adapter.retrieveWithReasoning(queryEmbedding, {
  domain: 'task-domain',
  k: 32,
  minConfidence: 0.7,  // Only high TD-error experiences
});
```

### Multi-Agent Training

```typescript
// Collect experiences from multiple agents
for (const agent of agents) {
  const experience = await agent.step();

  await adapter.insertPattern({
    // ... store experience with agent ID
    domain: `multi-agent/${agent.id}`,
  });
}

// Train shared model
await adapter.train({
  epochs: 50,
  batchSize: 64,
});
```

---

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

---

## Integration with Reasoning Agents

Combine learning with reasoning for better performance:

```typescript
// Train learning model
await adapter.train({ epochs: 50, batchSize: 32 });

// Use reasoning agents for inference
const result = await adapter.retrieveWithReasoning(queryEmbedding, {
  domain: 'decision-making',
  k: 10,
  useMMR: true,              // Diverse experiences
  synthesizeContext: true,    // Rich context
  optimizeMemory: true,       // Consolidate patterns
});

// Make decision based on learned experiences + reasoning
const decision = result.context.suggestedAction;
const confidence = result.memories[0].similarity;
```

---

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

---

## Troubleshooting

### Issue: Training not converging
```typescript
// Reduce learning rate
await adapter.train({
  epochs: 100,
  batchSize: 32,
  learningRate: 0.0001,  // Lower learning rate
});
```

### Issue: Overfitting
```typescript
// Use validation split
await adapter.train({
  epochs: 50,
  batchSize: 64,
  validationSplit: 0.2,  // 20% validation
});

// Enable memory optimization
await adapter.retrieveWithReasoning(queryEmbedding, {
  optimizeMemory: true,  // Consolidate, reduce overfitting
});
```

### Issue: Slow training
```bash
# Enable quantization for faster inference
# Use binary quantization (32x faster)
```

---

## Learn More

- **Algorithm Papers**: See docs/algorithms/ for detailed papers
- **GitHub**: https://github.com/ruvnet/agentic-flow/tree/main/packages/agentdb
- **MCP Integration**: `npx agentdb@latest mcp`
- **Website**: https://agentdb.ruv.io

---

**Category**: Machine Learning / Reinforcement Learning
**Difficulty**: Intermediate to Advanced
**Estimated Time**: 30-60 minutes
## Core Principles

AgentDB Learning Plugins operates on 3 fundamental principles:

### Principle 1: Offline Reinforcement Learning Enables Safe Learning from Logged Data
Train agents from historical experiences without environment interaction using Decision Transformers for imitation learning and policy optimization.

In practice:
- Decision Transformers model behavior as sequence prediction (states, actions, rewards) without online exploration
- Safe learning from expert demonstrations or logged trajectories prevents catastrophic failures during training
- Offline RL achieves 80-95% of online RL performance while eliminating exploration risks and environment costs

### Principle 2: Algorithm Selection Determines Learning Efficiency and Safety
Match RL algorithm to problem structure: value-based (discrete actions), policy gradients (continuous control), or hybrid approaches.

In practice:
- Q-Learning for discrete decisions (navigation, resource allocation) with sample-efficient off-policy learning
- Actor-Critic for continuous control (robotics, simulations) with variance reduction via value baseline
- SARSA for safety-critical applications requiring on-policy conservative exploration

### Principle 3: Experience Replay and Batch Training Accelerate Convergence
Store experiences in vector database for efficient sampling, prioritization, and multi-agent training across distributed nodes.

In practice:
- Prioritized experience replay focuses on high TD-error transitions (unexpected outcomes) for faster learning
- Batch training (32-128 samples) reduces variance and enables GPU acceleration (10-100x speedup)
- Vector similarity enables retrieval of relevant past experiences for transfer learning and few-shot adaptation

## Common Anti-Patterns

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| **Online Training Without Replay Buffer** | Each experience used once then discarded, requiring 10-100x more environment interactions | Store experiences in AgentDB with embeddings; sample random batches (32-64) for training; reuse high-value transitions |
| **Wrong Algorithm for Problem Type** | Q-Learning on continuous actions requires discretization (action space explosion), Actor-Critic on small discrete spaces wastes capacity | Match algorithm to action space: Q-Learning/SARSA for discrete (<100 actions), Actor-Critic/PPO for continuous, Decision Transformer for offline |
| **Ignoring Confidence and Usage Tracking** | All experiences weighted equally despite varying quality and relevance | Store confidence (reward-based or TD-error), increment usage_count/success_count; prioritize high-confidence experiences; prune low-quality patterns |

## Conclusion

AgentDB Learning Plugins transforms static vector databases into self-improving AI systems by integrating 9 reinforcement learning algorithms with persistent memory for experience accumulation and retrieval. By storing experiences as embeddings in AgentDB, agents learn from past successes and failures, retrieve similar patterns for transfer learning, and continuously improve through offline RL without risking catastrophic exploration.

Use this skill when building autonomous agents requiring continuous improvement (chatbots, recommendation systems, game AI), implementing safe learning from historical data (medical diagnosis, financial trading), or enabling multi-agent knowledge sharing through federated learning. The key insight is persistence: unlike traditional RL where experiences are discarded after training, AgentDB stores them permanently for retrieval, reuse, and transfer across tasks. Start with Decision Transformer for safe offline learning from logged data, add experience replay for sample efficiency, and enable distributed training when scaling to multiple agents or environments.