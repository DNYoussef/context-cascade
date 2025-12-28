---
name: AgentDB Semantic Vector Search
description: No description provided
---

# AgentDB Semantic Vector Search

## Overview

Implement semantic vector search with AgentDB for intelligent document retrieval, similarity matching, and context-aware querying. Build RAG systems, semantic search engines, and knowledge bases.

## SOP Framework: 5-Phase Semantic Search

### Phase 1: Setup Vector Database (1-2 hours)
- Initialize AgentDB
- Configure embedding model
- Setup database schema

### Phase 2: Embed Documents (1-2 hours)
- Process document corpus
- Generate embeddings
- Store vectors with metadata

### Phase 3: Build Search Index (1-2 hours)
- Create HNSW index
- Optimize search parameters
- Test retrieval accuracy

### Phase 4: Implement Query Interface (1-2 hours)
- Create REST API endpoints
- Add filtering and ranking
- Implement hybrid search

### Phase 5: Refine and Optimize (1-2 hours)
- Improve relevance
- Add re-ranking
- Performance tuning

## Quick Start

```typescript
import { AgentDB, EmbeddingModel } from 'agentdb-vector-search';

// Initialize
const db = new AgentDB({ name: 'semantic-search', dimensions: 1536 });
const embedder = new EmbeddingModel('openai/ada-002');

// Embed documents
for (const doc of documents) {
  const embedding = await embedder.embed(doc.text);
  await db.insert({
    id: doc.id,
    vector: embedding,
    metadata: { title: doc.title, content: doc.text }
  });
}

// Search
const query = 'machine learning tutorials';
const queryEmbedding = await embedder.embed(query);
const results = await db.search({
  vector: queryEmbedding,
  topK: 10,
  filter: { category: 'tech' }
});
```

## Features

- **Semantic Search**: Meaning-based retrieval
- **Hybrid Search**: Vector + keyword search
- **Filtering**: Metadata-based filtering
- **Re-ranking**: Improve result relevance
- **RAG Integration**: Context for LLMs

## Success Metrics

- Retrieval accuracy > 90%
- Query latency < 100ms
- Relevant results in top-10: > 95%
- API uptime > 99.9%

## MCP Requirements

This skill operates using AgentDB's npm package and API only. No additional MCP servers required.

All AgentDB operations are performed through:
- npm CLI: `npx agentdb@latest`
- TypeScript/JavaScript API: `import { AgentDB } from 'agentdb-vector-search'`

## Additional Resources

- Full docs: SKILL.md
- AgentDB Vector Search: https://agentdb.dev/docs/vector-search

## Common Anti-Patterns

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| **Exhaustive Search Without Indexing** | Searching all vectors linearly has O(N) complexity, causing query latency to scale linearly with dataset size and becoming unusable at >10k documents | Build HNSW index (Phase 3) to enable approximate nearest neighbor search with O(log N) complexity, achieving <100ms queries at millions of documents |
| **Single-Model Embeddings** | Using only vector similarity ignores keyword signals and metadata, causing retrieval to miss exact matches and fail when embeddings don't capture query intent | Implement hybrid search combining vector similarity with keyword search (BM25) and metadata filtering to leverage multiple retrieval signals |
| **Ignoring Retrieval Metrics** | Deploying semantic search without measuring precision/recall creates invisible quality issues where search appears to work but returns irrelevant results | Establish retrieval accuracy baselines (>90% recall@10 target) with evaluation datasets and track metrics continuously to detect degradation |

---

## Conclusion

AgentDB Semantic Vector Search enables building production-grade document retrieval systems for RAG applications, knowledge bases, and search engines. By prioritizing meaning over keywords, leveraging HNSW indexing for performance, and implementing context-aware retrieval strategies, it provides the foundation for intelligent information retrieval.

This skill excels at building RAG systems where LLMs need relevant context, semantic search engines for large document collections, and recommendation systems based on content similarity. Use this when keyword search is insufficient because users search by concept rather than exact terms, or when you need to retrieve contextually relevant documents even when query phrasing differs from document text.

The 5-phase framework (setup database, embed documents, build index, implement query interface, refine optimization) provides a systematic path from initial prototype to production deployment with <100ms query latency and >90% retrieval accuracy at scale.