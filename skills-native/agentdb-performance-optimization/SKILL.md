---
name: agentdb-performance-optimization
description: Apply quantization to reduce memory by 4-32x. Enable HNSW indexing for 150x faster search. Configure caching strategies and implement batch operations. Use when optimizing memory usage, improving search speed, or scaling to millions of vectors. Deploy these optimizations to achieve 12,500x performance gains.
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


# AgentDB Performance Optimization

## What This Skill Does

**Use this skill to** apply comprehensive performance optimization techniques for AgentDB vector databases. **Implement** quantization strategies (binary, scalar, product) to achieve 4-32x memory reduction. **Enable** HNSW indexing for 150x-12,500x performance improvements. **Configure** caching strategies and **deploy** batch operations to reduce memory usage while maintaining accuracy.

**Performance**: <100µs vector search, <1ms pattern retrieval, 2ms batch insert for 100 vectors.

## Prerequisites

**Install** Node.js 18+ and AgentDB v1.0.7+ via agentic-flow. **Verify** you have an existing AgentDB database or application ready for optimization.



## Quantization Strategies

**Select** the appropriate quantization strategy based on your memory and accuracy requirements.

### 1. Binary Quantization (32x Reduction)

**Apply** binary quantization for maximum memory reduction:

**Best For**: Large-scale deployments (1M+ vectors), memory-constrained environments
**Trade-off**: ~2-5% accuracy loss, 32x memory reduction, 10x faster

```typescript
const adapter = await createAgentDBAdapter({
  quantizationType: 'binary',
  // 768-dim float32 (3072 bytes) → 96 bytes binary
  // 1M vectors: 3GB → 96MB
});
```

**Use Cases**:
- Mobile/edge deployment
- Large-scale vector storage (millions of vectors)
- Real-time search with memory constraints

**Performance**:
- Memory: 32x smaller
- Search Speed: 10x faster (bit operations)
- Accuracy: 95-98% of original

### 2. Scalar Quantization (4x Reduction)

**Best For**: Balanced performance/accuracy, moderate datasets
**Trade-off**: ~1-2% accuracy loss, 4x memory reduction, 3x faster

```typescript
const adapter = await createAgentDBAdapter({
  quantizationType: 'scalar',
  // 768-dim float32 (3072 bytes) → 768 bytes (uint8)
  // 1M vectors: 3GB → 768MB
});
```

**Use Cases**:
- Production applications requiring high accuracy
- Medium-scale deployments (10K-1M vectors)
- General-purpose optimization

**Performance**:
- Memory: 4x smaller
- Search Speed: 3x faster
- Accuracy: 98-99% of original

### 3. Product Quantization (8-16x Reduction)

**Best For**: High-dimensional vectors, balanced compression
**Trade-off**: ~3-7% accuracy loss, 8-16x memory reduction, 5x faster

```typescript
const adapter = await createAgentDBAdapter({
  quantizationType: 'product',
  // 768-dim float32 (3072 bytes) → 48-96 bytes
  // 1M vectors: 3GB → 192MB
});
```

**Use Cases**:
- High-dimensional embeddings (>512 dims)
- Image/video embeddings
- Large-scale similarity search

**Performance**:
- Memory: 8-16x smaller
- Search Speed: 5x faster
- Accuracy: 93-97% of original

### 4. No Quantization (Full Precision)

**Best For**: Maximum accuracy, small datasets
**Trade-off**: No accuracy loss, full memory usage

```typescript
const adapter = await createAgentDBAdapter({
  quantizationType: 'none',
  // Full float32 precision
});
```



## Caching Strategies

### In-Memory Pattern Cache

```typescript
const adapter = await createAgentDBAdapter({
  cacheSize: 1000,  // Cache 1000 most-used patterns
});

// First retrieval: ~2ms (database)
// Subsequent: <1ms (cache hit)
const result = await adapter.retrieveWithReasoning(queryEmbedding, {
  k: 10,
});
```

**Cache Tuning**:
- Small applications: 100-500 patterns
- Medium applications: 500-2000 patterns
- Large applications: 2000-5000 patterns

### LRU Cache Behavior

```typescript
// Cache automatically evicts least-recently-used patterns
// Most frequently accessed patterns stay in cache

// Monitor cache performance
const stats = await adapter.getStats();
console.log('Cache Hit Rate:', stats.cacheHitRate);
// Aim for >80% hit rate
```



## Memory Optimization

### Automatic Consolidation

```typescript
// Enable automatic pattern consolidation
const result = await adapter.retrieveWithReasoning(queryEmbedding, {
  domain: 'documents',
  optimizeMemory: true,  // Consolidate similar patterns
  k: 10,
});

console.log('Optimizations:', result.optimizations);
// {
//   consolidated: 15,  // Merged 15 similar patterns
//   pruned: 3,         // Removed 3 low-quality patterns
//   improved_quality: 0.12  // 12% quality improvement
// }
```

### Manual Optimization

```typescript
// Manually trigger optimization
await adapter.optimize();

// Get statistics
const stats = await adapter.getStats();
console.log('Before:', stats.totalPatterns);
console.log('After:', stats.totalPatterns);  // Reduced by ~10-30%
```

### Pruning Strategies

```typescript
// Prune low-confidence patterns
await adapter.prune({
  minConfidence: 0.5,     // Remove confidence < 0.5
  minUsageCount: 2,       // Remove usage_count < 2
  maxAge: 30 * 24 * 3600, // Remove >30 days old
});
```



## Optimization Recipes

### Recipe 1: Maximum Speed (Sacrifice Accuracy)

```typescript
const adapter = await createAgentDBAdapter({
  quantizationType: 'binary',  // 32x memory reduction
  cacheSize: 5000,             // Large cache
  hnswM: 8,                    // Fewer connections = faster
  hnswEfSearch: 50,            // Low search quality = faster
});

// Expected: <50µs search, 90-95% accuracy
```

### Recipe 2: Balanced Performance

```typescript
const adapter = await createAgentDBAdapter({
  quantizationType: 'scalar',  // 4x memory reduction
  cacheSize: 1000,             // Standard cache
  hnswM: 16,                   // Balanced connections
  hnswEfSearch: 100,           // Balanced quality
});

// Expected: <100µs search, 98-99% accuracy
```

### Recipe 3: Maximum Accuracy

```typescript
const adapter = await createAgentDBAdapter({
  quantizationType: 'none',    // No quantization
  cacheSize: 2000,             // Large cache
  hnswM: 32,                   // Many connections
  hnswEfSearch: 200,           // High search quality
});

// Expected: <200µs search, 100% accuracy
```

### Recipe 4: Memory-Constrained (Mobile/Edge)

```typescript
const adapter = await createAgentDBAdapter({
  quantizationType: 'binary',  // 32x memory reduction
  cacheSize: 100,              // Small cache
  hnswM: 8,                    // Minimal connections
});

// Expected: <100µs search, ~10MB for 100K vectors
```



## Troubleshooting

### Issue: High memory usage

```bash
# Check database size
npx agentdb@latest stats .agentdb/vectors.db

# Enable quantization
# Use 'binary' for 32x reduction
```

### Issue: Slow search performance

```typescript
// Increase cache size
const adapter = await createAgentDBAdapter({
  cacheSize: 2000,  // Increase from 1000
});

// Reduce search quality (faster)
const result = await adapter.retrieveWithReasoning(queryEmbedding, {
  k: 5,  // Reduce from 10
});
```

### Issue: Low accuracy

```typescript
// Disable or use lighter quantization
const adapter = await createAgentDBAdapter({
  quantizationType: 'scalar',  // Instead of 'binary'
  hnswEfSearch: 200,           // Higher search quality
});
```

--------|-------------|-----------------|-----------|-------------|
| Search | 10K | 15ms | 100µs | 150x |
| Search | 100K | 150ms | 120µs | 1,250x |
| Search | 1M | 100s | 8ms | 12,500x |
| Batch Insert (100) | - | 1s | 2ms | 500x |
| Memory Usage | 1M | 3GB | 96MB | 32x (binary) |



**Category**: Performance / Optimization
**Difficulty**: Intermediate
**Estimated Time**: 20-30 minutes
## Core Principles

AgentDB Performance Optimization operates on 3 fundamental principles:

### Principle 1: Trade Memory for Speed Through Intelligent Quantization
Compress vectors by 4-32x with minimal accuracy loss (1-5%) using binary, scalar, or product quantization strategies.

In practice:
- Binary quantization reduces 768-dim vectors from 3GB to 96MB (32x) with 95-98% accuracy retention
- Scalar quantization achieves 4x reduction (3GB to 768MB) with 98-99% accuracy for production workloads
- Select quantization based on memory constraints vs accuracy requirements (mobile = binary, production = scalar)

### Principle 2: O(log n) Search Complexity via HNSW Indexing
Replace O(n) linear scans with hierarchical navigable small world graphs for 150-12,500x performance improvements.

In practice:
- HNSW automatically builds multi-layer proximity graphs during insertion
- Search navigates graph layers for sub-millisecond retrieval (100µs vs 15ms linear)
- Tune M (connections), efConstruction (build quality), efSearch (recall) for performance/accuracy balance

### Principle 3: Batch Operations and Caching Eliminate Redundant Work
Aggregate operations and cache frequent patterns to achieve 500x faster batch inserts and <1ms cache hits.

In practice:
- Batch insert 100 vectors in 2ms vs 1s for sequential inserts (500x speedup)
- LRU cache (1000-5000 patterns) serves 80%+ queries from memory (<1ms) vs database (2ms)
- Automatic pattern consolidation merges similar entries to reduce storage by 10-30%

## Common Anti-Patterns

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| **Sequential Inserts** | 1s for 100 vectors due to individual database writes and index updates | Use batch insert pattern: collect all patterns, insert in single transaction (2ms for 100 vectors) |
| **Full Precision Everywhere** | 3GB memory for 1M vectors causes OOM on mobile/edge devices | Apply binary quantization (96MB, 32x reduction) with <5% accuracy loss for memory-constrained environments |
| **Ignoring Cache Tuning** | Cache too small = low hit rate, too large = memory waste and eviction overhead | Set cacheSize based on workload: 100-500 (small), 500-2000 (medium), 2000-5000 (large). Monitor hit rate >80% |

## Conclusion

AgentDB Performance Optimization transforms vector search from memory-intensive, slow operations into production-ready systems capable of handling millions of vectors with sub-millisecond latency. By applying quantization strategies tailored to your accuracy requirements, enabling HNSW indexing for logarithmic search complexity, and implementing intelligent caching and batch operations, you achieve 150-12,500x performance improvements while reducing memory footprint by 4-32x.

Use this skill when scaling to large vector datasets (>10K vectors), deploying to memory-constrained environments (mobile, edge devices), or optimizing production systems requiring <10ms p99 latency. The key insight is strategic trade-offs: quantization trades minimal accuracy for massive memory savings, HNSW trades insertion time for exponentially faster search, and caching trades memory for latency reduction. Start with balanced configurations (scalar quantization, M=16, cacheSize=1000) and tune based on benchmarks for your specific workload.