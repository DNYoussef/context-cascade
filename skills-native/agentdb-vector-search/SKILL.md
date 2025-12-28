---
name: agentdb-vector-search
description: Implement semantic vector search with AgentDB for intelligent document retrieval, similarity matching, and context-aware querying. Use when building RAG systems, semantic search engines, or intelligent knowledge bases.
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


# AgentDB Vector Search

## What This Skill Does

Implements vector-based semantic search using AgentDB's high-performance vector database with **150x-12,500x faster** operations than traditional solutions. Features HNSW indexing, quantization, and sub-millisecond search (<100µs).

## Prerequisites

- Node.js 18+
- AgentDB v1.0.7+ (via agentic-flow or standalone)
- OpenAI API key (for embeddings) or custom embedding model

## Quick Start with CLI

### Initialize Vector Database

```bash
# Initialize with default dimensions (1536 for OpenAI ada-002)
npx agentdb@latest init ./vectors.db

# Custom dimensions for different embedding models
npx agentdb@latest init ./vectors.db --dimension 768  # sentence-transformers
npx agentdb@latest init ./vectors.db --dimension 384  # all-MiniLM-L6-v2

# Use preset configurations
npx agentdb@latest init ./vectors.db --preset small   # <10K vectors
npx agentdb@latest init ./vectors.db --preset medium  # 10K-100K vectors
npx agentdb@latest init ./vectors.db --preset large   # >100K vectors

# In-memory database for testing
npx agentdb@latest init ./vectors.db --in-memory
```

### Query Vector Database

```bash
# Basic similarity search
npx agentdb@latest query ./vectors.db "[0.1,0.2,0.3,...]"

# Top-k results
npx agentdb@latest query ./vectors.db "[0.1,0.2,0.3]" -k 10

# With similarity threshold (cosine similarity)
npx agentdb@latest query ./vectors.db "0.1 0.2 0.3" -t 0.75 -m cosine

# Different distance metrics
npx agentdb@latest query ./vectors.db "[...]" -m euclidean  # L2 distance
npx agentdb@latest query ./vectors.db "[...]" -m dot        # Dot product

# JSON output for automation
npx agentdb@latest query ./vectors.db "[...]" -f json -k 5

# Verbose output with distances
npx agentdb@latest query ./vectors.db "[...]" -v
```

### Import/Export Vectors

```bash
# Export vectors to JSON
npx agentdb@latest export ./vectors.db ./backup.json

# Import vectors from JSON
npx agentdb@latest import ./backup.json

# Get database statistics
npx agentdb@latest stats ./vectors.db
```

## Quick Start with API

```typescript
import { createAgentDBAdapter, computeEmbedding } from 'agentic-flow/reasoningbank';

// Initialize with vector search optimizations
const adapter = await createAgentDBAdapter({
  dbPath: '.agentdb/vectors.db',
  enableLearning: false,       // Vector search only
  enableReasoning: true,       // Enable semantic matching
  quantizationType: 'binary',  // 32x memory reduction
  cacheSize: 1000,             // Fast retrieval
});

// Store document with embedding
const text = "The quantum computer achieved 100 qubits";
const embedding = await computeEmbedding(text);

await adapter.insertPattern({
  id: '',
  type: 'document',
  domain: 'technology',
  pattern_data: JSON.stringify({
    embedding,
    text,
    metadata: { category: "quantum", date: "2025-01-15" }
  }),
  confidence: 1.0,
  usage_count: 0,
  success_count: 0,
  created_at: Date.now(),
  last_used: Date.now(),
});

// Semantic search with MMR (Maximal Marginal Relevance)
const queryEmbedding = await computeEmbedding("quantum computing advances");
const results = await adapter.retrieveWithReasoning(queryEmbedding, {
  domain: 'technology',
  k: 10,
  useMMR: true,              // Diverse results
  synthesizeContext: true,    // Rich context
});
```

## Core Features

### 1. Vector Storage
```typescript
// Store with automatic embedding
await db.storeWithEmbedding({
  content: "Your document text",
  metadata: { source: "docs", page: 42 }
});
```

### 2. Similarity Search
```typescript
// Find similar documents
const similar = await db.findSimilar("quantum computing", {
  limit: 5,
  minScore: 0.75
});
```

### 3. Hybrid Search (Vector + Metadata)
```typescript
// Combine vector similarity with metadata filtering
const results = await db.hybridSearch({
  query: "machine learning models",
  filters: {
    category: "research",
    date: { $gte: "2024-01-01" }
  },
  limit: 20
});
```

## Advanced Usage

### RAG (Retrieval Augmented Generation)
```typescript
// Build RAG pipeline
async function ragQuery(question: string) {
  // 1. Get relevant context
  const context = await db.searchSimilar(
    await embed(question),
    { limit: 5, threshold: 0.7 }
  );

  // 2. Generate answer with context
  const prompt = `Context: ${context.map(c => c.text).join('\n')}
Question: ${question}`;

  return await llm.generate(prompt);
}
```

### Batch Operations
```typescript
// Efficient batch storage
await db.batchStore(documents.map(doc => ({
  text: doc.content,
  embedding: doc.vector,
  metadata: doc.meta
})));
```

## MCP Server Integration

```bash
# Start AgentDB MCP server for Claude Code
npx agentdb@latest mcp

# Add to Claude Code (one-time setup)
claude mcp add agentdb npx agentdb@latest mcp

# Now use MCP tools in Claude Code:
# - agentdb_query: Semantic vector search
# - agentdb_store: Store documents with embeddings
# - agentdb_stats: Database statistics
```

## Performance Benchmarks

```bash
# Run comprehensive benchmarks
npx agentdb@latest benchmark

# Results:
# ✅ Pattern Search: 150x faster (100µs vs 15ms)
# ✅ Batch Insert: 500x faster (2ms vs 1s for 100 vectors)
# ✅ Large-scale Query: 12,500x faster (8ms vs 100s at 1M vectors)
# ✅ Memory Efficiency: 4-32x reduction with quantization
```

## Quantization Options

AgentDB provides multiple quantization strategies for memory efficiency:

### Binary Quantization (32x reduction)
```typescript
const adapter = await createAgentDBAdapter({
  quantizationType: 'binary',  // 768-dim → 96 bytes
});
```

### Scalar Quantization (4x reduction)
```typescript
const adapter = await createAgentDBAdapter({
  quantizationType: 'scalar',  // 768-dim → 768 bytes
});
```

### Product Quantization (8-16x reduction)
```typescript
const adapter = await createAgentDBAdapter({
  quantizationType: 'product',  // 768-dim → 48-96 bytes
});
```

## Distance Metrics

```bash
# Cosine similarity (default, best for most use cases)
npx agentdb@latest query ./db.sqlite "[...]" -m cosine

# Euclidean distance (L2 norm)
npx agentdb@latest query ./db.sqlite "[...]" -m euclidean

# Dot product (for normalized vectors)
npx agentdb@latest query ./db.sqlite "[...]" -m dot
```

## Advanced Features

### HNSW Indexing
- **O(log n) search complexity**
- **Sub-millisecond retrieval** (<100µs)
- **Automatic index building**

### Caching
- **1000 pattern in-memory cache**
- **<1ms pattern retrieval**
- **Automatic cache invalidation**

### MMR (Maximal Marginal Relevance)
- **Diverse result sets**
- **Avoid redundancy**
- **Balance relevance and diversity**

## Performance Tips

1. **Enable HNSW indexing**: Automatic with AgentDB, 10-100x faster
2. **Use quantization**: Binary (32x), Scalar (4x), Product (8-16x) memory reduction
3. **Batch operations**: 500x faster for bulk inserts
4. **Match dimensions**: 1536 (OpenAI), 768 (sentence-transformers), 384 (MiniLM)
5. **Similarity threshold**: Start at 0.7 for quality, adjust based on use case
6. **Enable caching**: 1000 pattern cache for frequent queries

## Troubleshooting

### Issue: Slow search performance
```bash
# Check if HNSW indexing is enabled (automatic)
npx agentdb@latest stats ./vectors.db

# Expected: <100µs search time
```

### Issue: High memory usage
```bash
# Enable binary quantization (32x reduction)
# Use in adapter: quantizationType: 'binary'
```

### Issue: Poor relevance
```bash
# Adjust similarity threshold
npx agentdb@latest query ./db.sqlite "[...]" -t 0.8  # Higher threshold

# Or use MMR for diverse results
# Use in adapter: useMMR: true
```

### Issue: Wrong dimensions
```bash
# Check embedding model dimensions:
# - OpenAI ada-002: 1536
# - sentence-transformers: 768
# - all-MiniLM-L6-v2: 384

npx agentdb@latest init ./db.sqlite --dimension 768
```

## Database Statistics

```bash
# Get comprehensive stats
npx agentdb@latest stats ./vectors.db

# Shows:
# - Total patterns/vectors
# - Database size
# - Average confidence
# - Domains distribution
# - Index status
```

## Performance Characteristics

- **Vector Search**: <100µs (HNSW indexing)
- **Pattern Retrieval**: <1ms (with cache)
- **Batch Insert**: 2ms for 100 vectors
- **Memory Efficiency**: 4-32x reduction with quantization
- **Scalability**: Handles 1M+ vectors efficiently
- **Latency**: Sub-millisecond for most operations

## Learn More

- GitHub: https://github.com/ruvnet/agentic-flow/tree/main/packages/agentdb
- Documentation: node_modules/agentic-flow/docs/AGENTDB_INTEGRATION.md
- MCP Integration: `npx agentdb@latest mcp` for Claude Code
- Website: https://agentdb.ruv.io
- CLI Help: `npx agentdb@latest --help`
- Command Help: `npx agentdb@latest help <command>`
## Core Principles

AgentDB Vector Search operates on 3 fundamental principles:

### Principle 1: Semantic Similarity Through Embedding-Based Retrieval
Transform unstructured data (text, images, code) into high-dimensional vectors where similar concepts cluster together for intelligent search.

In practice:
- Embeddings map semantic meaning to geometric space (cosine similarity measures conceptual closeness)
- "quantum computer" and "qubit processor" retrieve similar results despite different keywords
- HNSW indexing provides O(log n) search complexity for sub-millisecond retrieval (<100µs) on millions of vectors

### Principle 2: Quantization Trades Minimal Accuracy for Massive Memory Reduction
Compress vectors by 4-32x with <5% accuracy loss using binary, scalar, or product quantization for scalable deployments.

In practice:
- Binary quantization (32x reduction) enables 1M vectors in 96MB vs 3GB (mobile/edge deployments)
- Scalar quantization (4x reduction) balances memory and accuracy for production systems (98-99% original accuracy)
- Select quantization based on constraints: binary for memory limits, scalar for accuracy, none for maximum precision

### Principle 3: Hybrid Search Combines Vector Similarity with Metadata Filtering
Merge semantic understanding (embeddings) with structured constraints (metadata) for precision beyond pure vector search.

In practice:
- Vector search finds semantically relevant documents, metadata filters enforce business rules (date ranges, categories, permissions)
- MMR (Maximal Marginal Relevance) diversifies results to avoid redundancy while maintaining relevance
- RAG pipelines combine vector retrieval with LLM generation for context-aware answers

## Common Anti-Patterns

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| **Mismatched Embedding Dimensions** | Inserting 1536-dim (OpenAI) vectors into 768-dim database causes dimension mismatch errors | Initialize database with correct dimensions: `--dimension 1536` (OpenAI ada-002), `--dimension 768` (sentence-transformers), `--dimension 384` (MiniLM) |
| **Low Similarity Threshold** | Threshold 0.3 returns irrelevant results; too high (0.95) misses near-matches | Start with 0.7 for quality; lower to 0.5-0.6 for exploratory search; raise to 0.8-0.9 for high-precision retrieval |
| **Ignoring Quantization** | Full precision (float32) uses 3GB for 1M vectors causing OOM on constrained environments | Apply binary quantization (32x reduction to 96MB) for mobile/edge; scalar (4x to 768MB) for production; benchmark accuracy vs memory trade-offs |

## Conclusion

AgentDB Vector Search provides production-ready semantic search infrastructure with 150-12,500x performance improvements over naive implementations through HNSW indexing, quantization, and hybrid search capabilities. By transforming unstructured data into embeddings and leveraging vector similarity, you enable intelligent retrieval that understands meaning rather than keyword matching, powering RAG systems, semantic search engines, and intelligent knowledge bases.

Use this skill when building applications requiring semantic understanding (chatbots finding relevant context, document search beyond keywords), scaling to large datasets (>10K documents with sub-10ms latency), or deploying to memory-constrained environments (mobile apps, edge devices with quantization). The key insight is embedding choice determines quality: OpenAI embeddings (1536-dim) provide best semantic understanding, sentence-transformers (768-dim) balance quality and speed, MiniLM (384-dim) optimizes for resource constraints. Start with cosine similarity and scalar quantization, benchmark retrieval quality, and tune threshold/quantization based on accuracy requirements.