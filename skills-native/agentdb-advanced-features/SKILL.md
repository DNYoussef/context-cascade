---
name: agentdb-advanced-features
description: Master advanced AgentDB features including QUIC synchronization, multi-database management, custom distance metrics, hybrid search, and distributed systems integration. Use when building distributed AI systems, multi-agent coordination, or advanced vector search applications.
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


# AgentDB Advanced Features

## What This Skill Does

Covers advanced AgentDB capabilities for distributed systems, multi-database coordination, custom distance metrics, hybrid search (vector + metadata), QUIC synchronization, and production deployment patterns. Enables building sophisticated AI systems with sub-millisecond cross-node communication and advanced search capabilities.

**Performance**: <1ms QUIC sync, hybrid search with filters, custom distance metrics.

## Prerequisites

- Node.js 18+
- AgentDB v1.0.7+ (via agentic-flow)
- Understanding of distributed systems (for QUIC sync)
- Vector search fundamentals



## Distance Metrics

### Cosine Similarity (Default)

Best for normalized vectors, semantic similarity:

```bash
# CLI
npx agentdb@latest query ./vectors.db "[0.1,0.2,...]" -m cosine

# API
const result = await adapter.retrieveWithReasoning(queryEmbedding, {
  metric: 'cosine',
  k: 10,
});
```

**Use Cases**:
- Text embeddings (BERT, GPT, etc.)
- Semantic search
- Document similarity
- Most general-purpose applications

**Formula**: `cos(θ) = (A · B) / (||A|| × ||B||)`
**Range**: [-1, 1] (1 = identical, -1 = opposite)

### Euclidean Distance (L2)

Best for spatial data, geometric similarity:

```bash
# CLI
npx agentdb@latest query ./vectors.db "[0.1,0.2,...]" -m euclidean

# API
const result = await adapter.retrieveWithReasoning(queryEmbedding, {
  metric: 'euclidean',
  k: 10,
});
```

**Use Cases**:
- Image embeddings
- Spatial data
- Computer vision
- When vector magnitude matters

**Formula**: `d = √(Σ(ai - bi)²)`
**Range**: [0, ∞] (0 = identical, ∞ = very different)

### Dot Product

Best for pre-normalized vectors, fast computation:

```bash
# CLI
npx agentdb@latest query ./vectors.db "[0.1,0.2,...]" -m dot

# API
const result = await adapter.retrieveWithReasoning(queryEmbedding, {
  metric: 'dot',
  k: 10,
});
```

**Use Cases**:
- Pre-normalized embeddings
- Fast similarity computation
- When vectors are already unit-length

**Formula**: `dot = Σ(ai × bi)`
**Range**: [-∞, ∞] (higher = more similar)

### Custom Distance Metrics

```typescript
// Implement custom distance function
function customDistance(vec1: number[], vec2: number[]): number {
  // Weighted Euclidean distance
  const weights = [1.0, 2.0, 1.5, ...];
  let sum = 0;
  for (let i = 0; i < vec1.length; i++) {
    sum += weights[i] * Math.pow(vec1[i] - vec2[i], 2);
  }
  return Math.sqrt(sum);
}

// Use in search (requires custom implementation)
```



## Multi-Database Management

### Multiple Databases

```typescript
// Separate databases for different domains
const knowledgeDB = await createAgentDBAdapter({
  dbPath: '.agentdb/knowledge.db',
});

const conversationDB = await createAgentDBAdapter({
  dbPath: '.agentdb/conversations.db',
});

const codeDB = await createAgentDBAdapter({
  dbPath: '.agentdb/code.db',
});

// Use appropriate database for each task
await knowledgeDB.insertPattern({ /* knowledge */ });
await conversationDB.insertPattern({ /* conversation */ });
await codeDB.insertPattern({ /* code */ });
```

### Database Sharding

```typescript
// Shard by domain for horizontal scaling
const shards = {
  'domain-a': await createAgentDBAdapter({ dbPath: '.agentdb/shard-a.db' }),
  'domain-b': await createAgentDBAdapter({ dbPath: '.agentdb/shard-b.db' }),
  'domain-c': await createAgentDBAdapter({ dbPath: '.agentdb/shard-c.db' }),
};

// Route queries to appropriate shard
function getDBForDomain(domain: string) {
  const shardKey = domain.split('-')[0];  // Extract shard key
  return shards[shardKey] || shards['domain-a'];
}

// Insert to correct shard
const db = getDBForDomain('domain-a-task');
await db.insertPattern({ /* ... */ });
```



## Context Synthesis

Generate rich context from multiple memories:

```typescript
const result = await adapter.retrieveWithReasoning(queryEmbedding, {
  domain: 'problem-solving',
  k: 10,
  synthesizeContext: true,  // Enable context synthesis
});

// ContextSynthesizer creates coherent narrative
console.log('Synthesized Context:', result.context);
// "Based on 10 similar problem-solving attempts, the most effective
//  approach involves: 1) analyzing root cause, 2) brainstorming solutions,
//  3) evaluating trade-offs, 4) implementing incrementally. Success rate: 85%"

console.log('Patterns:', result.patterns);
// Extracted common patterns across memories
```



## CLI Advanced Operations

### Database Import/Export

```bash
# Export with compression
npx agentdb@latest export ./vectors.db ./backup.json.gz --compress

# Import from backup
npx agentdb@latest import ./backup.json.gz --decompress

# Merge databases
npx agentdb@latest merge ./db1.sqlite ./db2.sqlite ./merged.sqlite
```

### Database Optimization

```bash
# Vacuum database (reclaim space)
sqlite3 .agentdb/vectors.db "VACUUM;"

# Analyze for query optimization
sqlite3 .agentdb/vectors.db "ANALYZE;"

# Rebuild indices
npx agentdb@latest reindex ./vectors.db
```



## Troubleshooting

### Issue: QUIC sync not working

```bash
# Check firewall allows UDP port 4433
sudo ufw allow 4433/udp

# Verify peers are reachable
ping host1

# Check QUIC logs
DEBUG=agentdb:quic node server.js
```

### Issue: Hybrid search returns no results

```typescript
// Relax filters
const result = await adapter.retrieveWithReasoning(queryEmbedding, {
  k: 100,  // Increase k
  filters: {
    // Remove or relax filters
  },
});
```

### Issue: Memory consolidation too aggressive

```typescript
// Disable automatic optimization
const result = await adapter.retrieveWithReasoning(queryEmbedding, {
  optimizeMemory: false,  // Disable auto-consolidation
  k: 10,
});
```



**Category**: Advanced / Distributed Systems
**Difficulty**: Advanced
**Estimated Time**: 45-60 minutes
## Core Principles

AgentDB Advanced Features operates on 3 fundamental principles:

### Principle 1: Distributed Consistency Through QUIC Synchronization
Achieve sub-millisecond cross-node synchronization with automatic retry, multiplexing, and TLS 1.3 encryption for distributed vector databases.

In practice:
- QUIC enables <1ms pattern synchronization across network boundaries with UDP + reliability layer
- Multiplexed streams allow simultaneous operations (queries, inserts, syncs) without head-of-line blocking
- Event-based broadcasting ensures eventual consistency with configurable sync intervals (1s default)

### Principle 2: Hybrid Search Combines Vector Similarity with Metadata Filtering
Merge semantic understanding (embeddings) with structured constraints (metadata filters) for precision retrieval beyond pure vector search.

In practice:
- Vector search finds semantically similar documents, metadata filters enforce business rules (date ranges, categories, permissions)
- MMR (Maximal Marginal Relevance) diversifies results to avoid redundancy while maintaining relevance
- Custom distance metrics (cosine, Euclidean, dot product) optimize for different embedding types (text vs images)

### Principle 3: Multi-Database Sharding Enables Horizontal Scaling
Partition vector data across databases by domain or tenant for independent scaling and isolation.

In practice:
- Separate databases per domain (knowledge.db, conversations.db, code.db) prevent cross-contamination
- Sharding by tenant or region enables geographic distribution and compliance (GDPR data residency)
- Independent optimization per shard (different quantization, cache sizes) based on access patterns

## Common Anti-Patterns

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| **Synchronous QUIC Sync** | Blocking operations wait for sync completion, causing 10-100ms latency spikes | Enable async sync with configurable intervals (1s), batch sync operations (100 patterns), use fire-and-forget pattern |
| **Over-Filtering Hybrid Search** | Too many metadata filters return empty results despite semantic matches | Start with k=100 for vector search, then apply filters; progressively relax filters if results <5 |
| **Single Monolithic Database** | One database for all domains causes index bloat, slow queries, and cross-domain contamination | Shard by domain or tenant; use separate databases with independent indices and optimization strategies |

## Conclusion

AgentDB Advanced Features unlocks production-grade distributed AI systems by extending core vector search with QUIC synchronization for multi-node deployments, hybrid search for combining semantic and structured queries, and flexible sharding for horizontal scaling. These capabilities transform AgentDB from a local vector database into a distributed platform capable of supporting multi-agent coordination, geographic distribution, and enterprise-scale applications.

Use this skill when building distributed AI systems requiring cross-node communication (<1ms QUIC sync), implementing RAG systems needing metadata filters beyond semantic search (hybrid search with date/category/permission constraints), or scaling beyond single-machine limits (multi-database sharding by domain/tenant). The key insight is architectural flexibility: QUIC enables distributed consistency, hybrid search adds precision to semantic retrieval, and sharding provides independent scaling per domain. Start with single-database deployment, add QUIC sync when distributing across nodes, enable hybrid search for complex filtering, and implement sharding only when hitting performance or isolation limits.