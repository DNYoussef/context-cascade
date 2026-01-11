# AgentDB Semantic Search - Process Guide

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



## Phase 1: Setup Vector Database

```typescript
const db = new AgentDB({
  name: 'semantic-search',
  dimensions: 1536, // OpenAI ada-002
  indexType: 'hnsw'
});

const embedder = new EmbeddingModel('openai/ada-002');
```

## Phase 2: Embed Documents

```typescript
for (const doc of documents) {
  const embedding = await embedder.embed(doc.text);
  await db.insert({
    id: doc.id,
    vector: embedding,
    metadata: {
      title: doc.title,
      content: doc.text,
      category: doc.category
    }
  });
}
```

## Phase 3: Build Search Index

```typescript
await db.createIndex({
  type: 'hnsw',
  params: { M: 16, efConstruction: 200 }
});
```

## Phase 4: Implement Query Interface

```typescript
app.post('/api/search', async (req, res) => {
  const { query, topK = 10, filter } = req.body;

  const queryEmbedding = await embedder.embed(query);
  const results = await db.search({
    vector: queryEmbedding,
    topK,
    filter
  });

  res.json({ results });
});
```

## Phase 5: Refine and Optimize

```typescript
// Re-ranking
const reranked = await reranker.rerank(results, query);

// Hybrid search
const hybrid = await db.hybridSearch({
  vector: queryEmbedding,
  keywords: query.split(' '),
  alpha: 0.7 // 70% vector, 30% keyword
});
```

## Success Criteria
- [assert|neutral] Accuracy > 90% [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] Latency < 100ms [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] Relevant results in top-10 [ground:acceptance-criteria] [conf:0.90] [state:provisional]

## Resources

- Full docs: SKILL.md
- AgentDB: https://agentdb.dev/docs/vector-search


---
*Promise: `<promise>PROCESS_VERIX_COMPLIANT</promise>`*
