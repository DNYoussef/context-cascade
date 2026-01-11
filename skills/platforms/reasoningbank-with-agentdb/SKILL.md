---
name: reasoningbank-with-agentdb
description: Implement ReasoningBank adaptive learning with AgentDBs 150x faster vector database. Includes trajectory tracking, verdict judgment, memory distillation, and pattern recognition. Use when building self-learning agents, optimizing decision-making, or implementing experience replay systems.
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


# ReasoningBank with AgentDB

## What This Skill Does

Provides ReasoningBank adaptive learning patterns using AgentDB's high-performance backend (150x-12,500x faster). Enables agents to learn from experiences, judge outcomes, distill memories, and improve decision-making over time with 100% backward compatibility.

**Performance**: 150x faster pattern retrieval, 500x faster batch operations, <1ms memory access.

## Prerequisites

- Node.js 18+
- AgentDB v1.0.7+ (via agentic-flow)
- Understanding of reinforcement learning concepts (optional)

---

## Quick Start with CLI

### Initialize ReasoningBank Database

```bash
# Initialize AgentDB for ReasoningBank
npx agentdb@latest init ./.agentdb/reasoningbank.db --dimension 1536

# Start MCP server for Claude Code integration
npx agentdb@latest mcp
claude mcp add agentdb npx agentdb@latest mcp
```

### Migrate from Legacy ReasoningBank

```bash
# Automatic migration with validation
npx agentdb@latest migrate --source .swarm/memory.db

# Verify migration
npx agentdb@latest stats ./.agentdb/reasoningbank.db
```

---

## Quick Start with API

```typescript
import { createAgentDBAdapter, computeEmbedding } from 'agentic-flow/reasoningbank';

// Initialize ReasoningBank with AgentDB
const rb = await createAgentDBAdapter({
  dbPath: '.agentdb/reasoningbank.db',
  enableLearning: true,      // Enable learning plugins
  enableReasoning: true,      // Enable reasoning agents
  cacheSize: 1000,            // 1000 pattern cache
});

// Store successful experience
const query = "How to optimize database queries?";
const embedding = await computeEmbedding(query);

await rb.insertPattern({
  id: '',
  type: 'experience',
  domain: 'database-optimization',
  pattern_data: JSON.stringify({
    embedding,
    pattern: {
      query,
      approach: 'indexing + query optimization',
      outcome: 'success',
      metrics: { latency_reduction: 0.85 }
    }
  }),
  confidence: 0.95,
  usage_count: 1,
  success_count: 1,
  created_at: Date.now(),
  last_used: Date.now(),
});

// Retrieve similar experiences with reasoning
const result = await rb.retrieveWithReasoning(embedding, {
  domain: 'database-optimization',
  k: 5,
  useMMR: true,              // Diverse results
  synthesizeContext: true,    // Rich context synthesis
});

console.log('Memories:', result.memories);
console.log('Context:', result.context);
console.log('Patterns:', result.patterns);
```

---

## Core ReasoningBank Concepts

### 1. Trajectory Tracking

Track agent execution paths and outcomes:

```typescript
// Record trajectory (sequence of actions)
const trajectory = {
  task: 'optimize-api-endpoint',
  steps: [
    { action: 'analyze-bottleneck', result: 'found N+1 query' },
    { action: 'add-eager-loading', result: 'reduced queries' },
    { action: 'add-caching', result: 'improved latency' }
  ],
  outcome: 'success',
  metrics: { latency_before: 2500, latency_after: 150 }
};

const embedding = await computeEmbedding(JSON.stringify(trajectory));

await rb.insertPattern({
  id: '',
  type: 'trajectory',
  domain: 'api-optimization',
  pattern_data: JSON.stringify({ embedding, pattern: trajectory }),
  confidence: 0.9,
  usage_count: 1,
  success_count: 1,
  created_at: Date.now(),
  last_used: Date.now(),
});
```

### 2. Verdict Judgment

Judge whether a trajectory was successful:

```typescript
// Retrieve similar past trajectories
const similar = await rb.retrieveWithReasoning(queryEmbedding, {
  domain: 'api-optimization',
  k: 10,
});

// Judge based on similarity to successful patterns
const verdict = similar.memories.filter(m =>
  m.pattern.outcome === 'success' &&
  m.similarity > 0.8
).length > 5 ? 'likely_success' : 'needs_review';

console.log('Verdict:', verdict);
console.log('Confidence:', similar.memories[0]?.similarity || 0);
```

### 3. Memory Distillation

Consolidate similar experiences into patterns:

```typescript
// Get all experiences in domain
const experiences = await rb.retrieveWithReasoning(embedding, {
  domain: 'api-optimization',
  k: 100,
  optimizeMemory: true,  // Automatic consolidation
});

// Distill into high-level pattern
const distilledPattern = {
  domain: 'api-optimization',
  pattern: 'For N+1 queries: add eager loading, then cache',
  success_rate: 0.92,
  sample_size: experiences.memories.length,
  confidence: 0.95
};

await rb.insertPattern({
  id: '',
  type: 'distilled-pattern',
  domain: 'api-optimization',
  pattern_data: JSON.stringify({
    embedding: await computeEmbedding(JSON.stringify(distilledPattern)),
    pattern: distilledPattern
  }),
  confidence: 0.95,
  usage_count: 0,
  success_count: 0,
  created_at: Date.now(),
  last_used: Date.now(),
});
```

---

## Integration with Reasoning Agents

AgentDB provides 4 reasoning modules that enhance ReasoningBank:

### 1. PatternMatcher

Find similar successful patterns:

```typescript
const result = await rb.retrieveWithReasoning(queryEmbedding, {
  domain: 'problem-solving',
  k: 10,
  useMMR: true,  // Maximal Marginal Relevance for diversity
});

// PatternMatcher returns diverse, relevant memories
result.memories.forEach(mem => {
  console.log(`Pattern: ${mem.pattern.approach}`);
  console.log(`Similarity: ${mem.similarity}`);
  console.log(`Success Rate: ${mem.success_count / mem.usage_count}`);
});
```

### 2. ContextSynthesizer

Generate rich context from multiple memories:

```typescript
const result = await rb.retrieveWithReasoning(queryEmbedding, {
  domain: 'code-optimization',
  synthesizeContext: true,  // Enable context synthesis
  k: 5,
});

// ContextSynthesizer creates coherent narrative
console.log('Synthesized Context:', result.context);
// "Based on 5 similar optimizations, the most effective approach
//  involves profiling, identifying bottlenecks, and applying targeted
//  improvements. Success rate: 87%"
```

### 3. MemoryOptimizer

Automatically consolidate and prune:

```typescript
const result = await rb.retrieveWithReasoning(queryEmbedding, {
  domain: 'testing',
  optimizeMemory: true,  // Enable automatic optimization
});

// MemoryOptimizer consolidates similar patterns and prunes low-quality
console.log('Optimizations:', result.optimizations);
// { consolidated: 15, pruned: 3, improved_quality: 0.12 }
```

### 4. ExperienceCurator

Filter by quality and relevance:

```typescript
const result = await rb.retrieveWithReasoning(queryEmbedding, {
  domain: 'debugging',
  k: 20,
  minConfidence: 0.8,  // Only high-confidence experiences
});

// ExperienceCurator returns only quality experiences
result.memories.forEach(mem => {
  console.log(`Confidence: ${mem.confidence}`);
  console.log(`Success Rate: ${mem.success_count / mem.usage_count}`);
});
```

---

## Legacy API Compatibility

AgentDB maintains 100% backward compatibility with legacy ReasoningBank:

```typescript
import {
  retrieveMemories,
  judgeTrajectory,
  distillMemories
} from 'agentic-flow/reasoningbank';

// Legacy API works unchanged (uses AgentDB backend automatically)
const memories = await retrieveMemories(query, {
  domain: 'code-generation',
  agent: 'coder'
});

const verdict = await judgeTrajectory(trajectory, query);

const newMemories = await distillMemories(
  trajectory,
  verdict,
  query,
  { domain: 'code-generation' }
);
```

---

## Performance Characteristics

- **Pattern Search**: 150x faster (100µs vs 15ms)
- **Memory Retrieval**: <1ms (with cache)
- **Batch Insert**: 500x faster (2ms vs 1s for 100 patterns)
- **Trajectory Judgment**: <5ms (including retrieval + analysis)
- **Memory Distillation**: <50ms (consolidate 100 patterns)

---

## Advanced Patterns

### Hierarchical Memory

Organize memories by abstraction level:

```typescript
// Low-level: Specific implementation
await rb.insertPattern({
  type: 'concrete',
  domain: 'debugging/null-pointer',
  pattern_data: JSON.stringify({
    embedding,
    pattern: { bug: 'NPE in UserService.getUser()', fix: 'Add null check' }
  }),
  confidence: 0.9,
  // ...
});

// Mid-level: Pattern across similar cases
await rb.insertPattern({
  type: 'pattern',
  domain: 'debugging',
  pattern_data: JSON.stringify({
    embedding,
    pattern: { category: 'null-pointer', approach: 'defensive-checks' }
  }),
  confidence: 0.85,
  // ...
});

// High-level: General principle
await rb.insertPattern({
  type: 'principle',
  domain: 'software-engineering',
  pattern_data: JSON.stringify({
    embedding,
    pattern: { principle: 'fail-fast with clear errors' }
  }),
  confidence: 0.95,
  // ...
});
```

### Multi-Domain Learning

Transfer learning across domains:

```typescript
// Learn from backend optimization
const backendExperience = await rb.retrieveWithReasoning(embedding, {
  domain: 'backend-optimization',
  k: 10,
});

// Apply to frontend optimization
const transferredKnowledge = backendExperience.memories.map(mem => ({
  ...mem,
  domain: 'frontend-optimization',
  adapted: true,
}));
```

---

## CLI Operations

### Database Management

```bash
# Export trajectories and patterns
npx agentdb@latest export ./.agentdb/reasoningbank.db ./backup.json

# Import experiences
npx agentdb@latest import ./experiences.json

# Get statistics
npx agentdb@latest stats ./.agentdb/reasoningbank.db
# Shows: total patterns, domains, confidence distribution
```

### Migration

```bash
# Migrate from legacy ReasoningBank
npx agentdb@latest migrate --source .swarm/memory.db --target .agentdb/reasoningbank.db

# Validate migration
npx agentdb@latest stats .agentdb/reasoningbank.db
```

---

## Troubleshooting

### Issue: Migration fails
```bash
# Check source database exists
ls -la .swarm/memory.db

# Run with verbose logging
DEBUG=agentdb:* npx agentdb@latest migrate --source .swarm/memory.db
```

### Issue: Low confidence scores
```typescript
// Enable context synthesis for better quality
const result = await rb.retrieveWithReasoning(embedding, {
  synthesizeContext: true,
  useMMR: true,
  k: 10,
});
```

### Issue: Memory growing too large
```typescript
// Enable automatic optimization
const result = await rb.retrieveWithReasoning(embedding, {
  optimizeMemory: true,  // Consolidates similar patterns
});

// Or manually optimize
await rb.optimize();
```

---

## Learn More

- **AgentDB Integration**: node_modules/agentic-flow/docs/AGENTDB_INTEGRATION.md
- **GitHub**: https://github.com/ruvnet/agentic-flow/tree/main/packages/agentdb
- **MCP Integration**: `npx agentdb@latest mcp`
- **Website**: https://agentdb.ruv.io

---

**Category**: Machine Learning / Reinforcement Learning
**Difficulty**: Intermediate
**Estimated Time**: 20-30 minutes
## Core Principles

1. **Vector Semantic Retrieval Over Exact Matching**: ReasoningBank with AgentDB leverages 150x faster vector search (100us vs 15ms) through semantic embeddings, retrieving similar trajectories even when keywords differ, enabling agents to learn from experiences described differently but contextually identical.

2. **Adaptive Memory Consolidation**: Memory distillation consolidates 100+ granular experiences (e.g., "fixed NPE in UserService", "added null check to AuthService") into higher-level patterns ("defensive null checks prevent pointer exceptions"), reducing memory footprint while preserving learned knowledge and avoiding pattern redundancy.

3. **Confidence-Weighted Experience Replay**: Verdict judgment retrieves patterns filtered by confidence (>0.8) and success rate, prioritizing proven trajectories over experimental ones, preventing agents from repeating failed approaches while still allowing exploration of medium-confidence strategies (0.5-0.8) when explicitly needed.

## Anti-Patterns

| Anti-Pattern | Why It Fails | Correct Approach |
|--------------|--------------|------------------|
| Storing raw text without embeddings | Pattern retrieval becomes keyword search, missing semantically similar experiences ("optimize query" vs "speed up database") | Always compute embeddings via computeEmbedding() before insertion, enabling semantic similarity matching |
| Skipping memory distillation | 10,000+ micro-experiences (every bug fix stored separately) bloat database to >2GB, slowing retrieval to >500ms | Run automatic consolidation (optimizeMemory: true) or manual distillation after 100+ experiences in same domain |
| Using trajectory outcomes without confidence scores | Agent treats single successful case (confidence 0.6) as proven pattern, repeating approaches that succeeded by luck | Only apply patterns with confidence >0.8 and usage_count >3, mark experimental patterns as "needs validation" |

## Conclusion

ReasoningBank with AgentDB transforms agent learning from ephemeral task execution to persistent experience accumulation, enabling agents to judge new trajectories against historical patterns (verdict judgment), consolidate granular learnings into reusable strategies (memory distillation), and retrieve contextually relevant experiences through 150x faster vector search. This creates a flywheel effect - each task improves the pattern library, making future similar tasks faster and more accurate.

The key to production success is maintaining the 70% survival threshold for pattern updates: adversarial validation must challenge new learnings (e.g., "does this null check pattern apply to async contexts?") and only accept patterns that survive scrutiny. Without this rigor, confident drift accumulates - the agent becomes certain of incorrect patterns, degrading performance over time. When tracking learning delta, measure not just task completion rate, but pattern quality (success_rate / usage_count) - a high-quality ReasoningBank enables 10x faster task execution through proven trajectory reuse.