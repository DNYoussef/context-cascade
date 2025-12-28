---
name: agentdb
description: High-performance vector search and semantic memory for AI agents. Use when implementing RAG systems, semantic document retrieval, or persistent agent memory. Provides 150x faster vector search vs traditional databases with HNSW indexing and 384-dimensional embeddings.
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


# AgentDB - Vector Search & Semantic Memory

Ultra-fast vector database for AI agent memory, RAG systems, and semantic search applications.

## When to Use This Skill

Use when implementing retrieval-augmented generation (RAG), building semantic search engines, creating persistent agent memory systems, or optimizing vector similarity searches for production workloads.

## Core Capabilities

### Vector Search
- 150x faster than traditional databases
- HNSW (Hierarchical Navigable Small World) indexing
- 384-dimensional sentence embeddings
- Sub-millisecond query latency

### Semantic Memory
- Persistent cross-session storage
- Automatic embedding generation
- Similarity-based retrieval
- Metadata filtering and ranking

### Memory Patterns
- Short-term: Recent context (1-100 items)
- Long-term: Persistent knowledge (unlimited)
- Episodic: Timestamped experiences
- Semantic: Concept relationships

## Process

1. **Initialize vector store**
   - Configure embedding model (sentence-transformers)
   - Set up HNSW index parameters
   - Define metadata schema
   - Allocate storage backend

2. **Store information**
   - Generate embeddings automatically
   - Store with metadata tags
   - Index for fast retrieval
   - Maintain consistency

3. **Query semantically**
   - Embed query text
   - Perform vector similarity search
   - Apply metadata filters
   - Rank and return results

4. **Optimize performance**
   - Tune HNSW parameters (M, ef_construction)
   - Implement quantization (4-32x memory reduction)
   - Use batched operations
   - Monitor query latency

## Integration

- **Memory-MCP**: Triple-layer retention (24h/7d/30d+)
- **RAG Pipelines**: Document retrieval for LLM context
- **Agent Memory**: Cross-session state persistence
- **Knowledge Bases**: Semantic search for documentation
## Common Anti-Patterns

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| **Keyword-Based Filtering** | Treating vector search like SQL WHERE clauses ignores semantic similarity | Use metadata filters for exact matches, semantic search for concept retrieval |
| **Full-Precision Everything** | Storing unquantized vectors wastes memory and limits scale | Enable scalar quantization by default; use binary for >1M vectors |
| **Ignoring Dimension Mismatch** | Inserting vectors with wrong dimensions corrupts index and causes query failures | Validate embedding dimensions (384 for sentence-transformers) before insertion |
| **No Index Rebuilding** | Stale HNSW indices degrade performance as data distribution shifts | Rebuild indices monthly or after 10%+ data changes |
| **Unbounded Result Sets** | Returning all similar vectors exhausts memory and provides low-quality matches | Always set k (top-k results) and similarity thresholds |

---

## Conclusion

The AgentDB skill provides production-grade vector search infrastructure for AI agent memory and RAG systems. By combining HNSW indexing, sentence embeddings, and quantization, it delivers 150x faster search with 4-32x memory reduction compared to traditional databases.

Use this skill when implementing retrieval-augmented generation, building semantic search engines, or creating persistent agent memory systems. AgentDB excels at similarity search over large document corpora, cross-session agent state persistence, and real-time embedding-based retrieval where sub-millisecond latency matters.

Key takeaways: Trust HNSW for approximate search (exact results rarely needed), enable quantization for memory efficiency, and validate embeddings before insertion. The integration with Memory-MCP, ReasoningBank, and 9 reinforcement learning algorithms provides a complete memory and learning infrastructure for stateful AI agents.