/*============================================================================*/
/* AGENTDB SKILL :: VERILINGUA x VERIX EDITION                      */
/*============================================================================*/

---
name: agentdb
version: 1.0.0
description: |
  [assert|neutral] High-performance vector search and semantic memory for AI agents. Use when implementing RAG systems, semantic document retrieval, or persistent agent memory. Provides 150x faster vector search vs trad [ground:given] [conf:0.95] [state:confirmed]
category: platforms
tags:
- platforms
- integration
- tools
author: ruv
cognitive_frame:
  primary: aspectual
  goal_analysis:
    first_order: "Execute agentdb workflow"
    second_order: "Ensure quality and consistency"
    third_order: "Enable systematic platforms processes"
---

/*----------------------------------------------------------------------------*/
/* S0 META-IDENTITY                                                            */
/*----------------------------------------------------------------------------*/

[define|neutral] SKILL := {
  name: "agentdb",
  category: "platforms",
  version: "1.0.0",
  layer: L1
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S1 COGNITIVE FRAME                                                          */
/*----------------------------------------------------------------------------*/

[define|neutral] COGNITIVE_FRAME := {
  frame: "Aspectual",
  source: "Russian",
  force: "Complete or ongoing?"
} [ground:cognitive-science] [conf:0.92] [state:confirmed]

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.

/*----------------------------------------------------------------------------*/
/* S2 TRIGGER CONDITIONS                                                       */
/*----------------------------------------------------------------------------*/

[define|neutral] TRIGGER_POSITIVE := {
  keywords: ["agentdb", "platforms", "workflow"],
  context: "user needs agentdb capability"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S3 CORE CONTENT                                                             */
/*----------------------------------------------------------------------------*/

## When NOT to Use This Skill

- Local-only operations with no vector search needs
- Simple key-value storage without semantic similarity
- Real-time streaming data without persistence requirements
- Operations that do not require embedding-based retrieval

## Success Criteria
- [assert|neutral] Vector search query latency: <10ms for 99th percentile [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] Embedding generation: <100ms per document [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] Index build time: <1s per 1000 vectors [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] Recall@10: >0.95 for similar documents [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] Database connection success rate: >99.9% [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] Memory footprint: <2GB for 1M vectors with quantization [ground:acceptance-criteria] [conf:0.90] [state:provisional]

## Edge Cases & Error Handling

- **Rate Limits**: AgentDB local instances have no rate limits; cloud deployments may vary
- **Connection Failures**: Implement retry logic with exponential backoff (max 3 retries)
- **Index Corruption**: Maintain backup indices; rebuild from source if corrupted
- **Memory Overflow**: Use quantization (4-bit, 8-bit) to reduce memory by 4-32x
- **Stale Embeddings**: Implement TTL-based refresh for dynamic content
- **Dimension Mismatch**: Validate embedding dimensions (384 for sentence-transformers) before insertion

## Guardrails & Safety
- [assert|emphatic] NEVER: expose database connection strings in logs or error messages [ground:policy] [conf:0.98] [state:confirmed]
- [assert|neutral] ALWAYS: validate vector dimensions before insertion [ground:policy] [conf:0.98] [state:confirmed]
- [assert|neutral] ALWAYS: sanitize metadata to prevent injection attacks [ground:policy] [conf:0.98] [state:confirmed]
- [assert|emphatic] NEVER: store PII in vector metadata without encryption [ground:policy] [conf:0.98] [state:confirmed]
- [assert|neutral] ALWAYS: implement access control for multi-tenant deployments [ground:policy] [conf:0.98] [state:confirmed]
- [assert|neutral] ALWAYS: validate search results before returning to users [ground:policy] [conf:0.98] [state:confirmed]

## Evidence-Based Validation

- Verify database health: Check connection status and index integrity
- Validate search quality: Measure recall/precision on test queries
- Monitor performance: Track query latency, throughput, and memory usage
- Test failure recovery: Simulate connection drops and index corruption
- Benchmark improvements: Compare against baseline metrics (e.g., 150x speedup claim)


# AgentDB - Vector Search & Semantic Memory

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



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
  pattern: "skills/platforms/agentdb/{project}/{timestamp}",
  store: ["executions", "decisions", "patterns"],
  retrieve: ["similar_tasks", "proven_patterns"]
} [ground:system-policy] [conf:1.0] [state:confirmed]

[define|neutral] MEMORY_TAGGING := {
  WHO: "agentdb-{session_id}",
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

[commit|confident] <promise>AGENTDB_VERILINGUA_VERIX_COMPLIANT</promise> [ground:self-validation] [conf:0.99] [state:confirmed]
