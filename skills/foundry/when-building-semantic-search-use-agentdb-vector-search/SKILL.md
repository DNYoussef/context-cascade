/*============================================================================*/
/* AGENTDB SEMANTIC VECTOR SEARCH SKILL :: VERILINGUA x VERIX EDITION                      */
/*============================================================================*/

---
name: AgentDB Semantic Vector Search
version: 1.0.0
description: |
  [assert|neutral] AgentDB Semantic Vector Search skill for agentdb workflows [ground:given] [conf:0.95] [state:confirmed]
category: agentdb
tags:
- general
author: system
cognitive_frame:
  primary: evidential
  goal_analysis:
    first_order: "Execute AgentDB Semantic Vector Search workflow"
    second_order: "Ensure quality and consistency"
    third_order: "Enable systematic agentdb processes"
---

/*----------------------------------------------------------------------------*/
/* S0 META-IDENTITY                                                            */
/*----------------------------------------------------------------------------*/

[define|neutral] SKILL := {
  name: "AgentDB Semantic Vector Search",
  category: "agentdb",
  version: "1.0.0",
  layer: L1
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S1 COGNITIVE FRAME                                                          */
/*----------------------------------------------------------------------------*/

[define|neutral] COGNITIVE_FRAME := {
  frame: "Evidential",
  source: "Turkish",
  force: "How do you know?"
} [ground:cognitive-science] [conf:0.92] [state:confirmed]

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.

/*----------------------------------------------------------------------------*/
/* S2 TRIGGER CONDITIONS                                                       */
/*----------------------------------------------------------------------------*/

[define|neutral] TRIGGER_POSITIVE := {
  keywords: ["AgentDB Semantic Vector Search", "agentdb", "workflow"],
  context: "user needs AgentDB Semantic Vector Search capability"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S3 CORE CONTENT                                                             */
/*----------------------------------------------------------------------------*/

# AgentDB Semantic Vector Search

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



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
- [assert|neutral] Retrieval accuracy > 90% [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] Query latency < 100ms [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] Relevant results in top-10: > 95% [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] API uptime > 99.9% [ground:acceptance-criteria] [conf:0.90] [state:provisional]

## MCP Requirements

This skill operates using AgentDB's npm package and API only. No additional MCP servers required.

All AgentDB operations are performed through:
- npm CLI: `npx agentdb@latest`
- TypeScript/JavaScript API: `import { AgentDB } from 'agentdb-vector-search'`

## Additional Resources

- Full docs: SKILL.md
- AgentDB Vector Search: https://agentdb.dev/docs/vector-search

---

## Core Principles

AgentDB Semantic Vector Search operates on 3 fundamental principles for building intelligent document retrieval systems:

### Principle 1: Meaning Over Keywords

Semantic search retrieves documents based on meaning similarity rather than exact keyword matching, enabling context-aware retrieval.

In practice:
- Generate embeddings for documents using models like OpenAI ada-002 (1536 dimensions) to capture semantic meaning
- Store vectors with rich metadata (title, content, category, tags) to enable hybrid search combining semantic and keyword filters
- Search using query embeddings to find semantically similar documents even when exact keywords differ
- Implement distance metrics (cosine similarity, euclidean) to rank results by semantic relevance rather than keyword frequency

### Principle 2: Performance Through Indexing

Build HNSW indexes for 150x faster vector search compared to exhaustive search, essential for production-scale retrieval.

In practice:
- Create HNSW (Hierarchical Navigable Small World) indexes after document ingestion to enable fast approximate nearest neighbor search
- Optimize search parameters (ef_construction, M) based on accuracy vs speed tradeoffs for your use case
- Test retrieval accuracy with evaluation datasets to en

/*----------------------------------------------------------------------------*/
/* S4 SUCCESS CRITERIA                                                         */
/*----------------------------------------------------------------------------*/

[define|neutral] SUCCESS_CRITERIA := {
  primary: "Skill execution completes successfully",
  quality: "Output meets quality thresholds",
  verification: "Results validated against requirements"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S5 MCP INTEGRATION                                                          */
/*----------------------------------------------------------------------------*/

[define|neutral] MCP_INTEGRATION := {
  memory_mcp: "Store execution results and patterns",
  tools: ["mcp__memory-mcp__memory_store", "mcp__memory-mcp__vector_search"]
} [ground:witnessed:mcp-config] [conf:0.95] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S6 MEMORY NAMESPACE                                                         */
/*----------------------------------------------------------------------------*/

[define|neutral] MEMORY_NAMESPACE := {
  pattern: "skills/agentdb/AgentDB Semantic Vector Search/{project}/{timestamp}",
  store: ["executions", "decisions", "patterns"],
  retrieve: ["similar_tasks", "proven_patterns"]
} [ground:system-policy] [conf:1.0] [state:confirmed]

[define|neutral] MEMORY_TAGGING := {
  WHO: "AgentDB Semantic Vector Search-{session_id}",
  WHEN: "ISO8601_timestamp",
  PROJECT: "{project_name}",
  WHY: "skill-execution"
} [ground:system-policy] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S7 SKILL COMPLETION VERIFICATION                                            */
/*----------------------------------------------------------------------------*/

[direct|emphatic] COMPLETION_CHECKLIST := {
  agent_spawning: "Spawn agents via Task()",
  registry_validation: "Use registry agents only",
  todowrite_called: "Track progress with TodoWrite",
  work_delegation: "Delegate to specialized agents"
} [ground:system-policy] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S8 ABSOLUTE RULES                                                           */
/*----------------------------------------------------------------------------*/

[direct|emphatic] RULE_NO_UNICODE := forall(output): NOT(unicode_outside_ascii) [ground:windows-compatibility] [conf:1.0] [state:confirmed]

[direct|emphatic] RULE_EVIDENCE := forall(claim): has(ground) AND has(confidence) [ground:verix-spec] [conf:1.0] [state:confirmed]

[direct|emphatic] RULE_REGISTRY := forall(agent): agent IN AGENT_REGISTRY [ground:system-policy] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* PROMISE                                                                     */
/*----------------------------------------------------------------------------*/

[commit|confident] <promise>AGENTDB SEMANTIC VECTOR SEARCH_VERILINGUA_VERIX_COMPLIANT</promise> [ground:self-validation] [conf:0.99] [state:confirmed]
