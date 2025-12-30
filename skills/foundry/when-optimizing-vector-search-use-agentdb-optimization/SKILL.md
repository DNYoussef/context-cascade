/*============================================================================*/
/* AGENTDB VECTOR SEARCH OPTIMIZATION SKILL :: VERILINGUA x VERIX EDITION                      */
/*============================================================================*/

---
name: AgentDB Vector Search Optimization
version: 1.0.0
description: |
  [assert|neutral] AgentDB Vector Search Optimization skill for agentdb workflows [ground:given] [conf:0.95] [state:confirmed]
category: agentdb
tags:
- general
author: system
cognitive_frame:
  primary: evidential
  goal_analysis:
    first_order: "Execute AgentDB Vector Search Optimization workflow"
    second_order: "Ensure quality and consistency"
    third_order: "Enable systematic agentdb processes"
---

/*----------------------------------------------------------------------------*/
/* S0 META-IDENTITY                                                            */
/*----------------------------------------------------------------------------*/

[define|neutral] SKILL := {
  name: "AgentDB Vector Search Optimization",
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
  keywords: ["AgentDB Vector Search Optimization", "agentdb", "workflow"],
  context: "user needs AgentDB Vector Search Optimization capability"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S3 CORE CONTENT                                                             */
/*----------------------------------------------------------------------------*/

# AgentDB Vector Search Optimization

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



## Overview

Optimize AgentDB performance with quantization (4-32x memory reduction), HNSW indexing (150x faster search), caching, and batch operations for scaling to millions of vectors.

## SOP Framework: 5-Phase Optimization

### Phase 1: Baseline Performance (1 hour)
- Measure current metrics (latency, throughput, memory)
- Identify bottlenecks
- Set optimization targets

### Phase 2: Apply Quantization (1-2 hours)
- Configure product quantization
- Train codebooks
- Apply compression
- Validate accuracy

### Phase 3: Implement HNSW Indexing (1-2 hours)
- Build HNSW index
- Tune parameters (M, efConstruction, efSearch)
- Benchmark speedup

### Phase 4: Configure Caching (1 hour)
- Implement query cache
- Set TTL and eviction policies
- Monitor hit rates

### Phase 5: Benchmark Results (1-2 hours)
- Run comprehensive benchmarks
- Compare before/after
- Validate improvements

## Quick Start

```typescript
import { AgentDB, Quantization, QueryCache } from 'agentdb-optimization';

const db = new AgentDB({ name: 'optimized-db', dimensions: 1536 });

// Quantization (4x memory reduction)
const quantizer = new Quantization({
  method: 'product-quantization',
  compressionRatio: 4
});
await db.applyQuantization(quantizer);

// HNSW indexing (150x speedup)
await db.createIndex({
  type: 'hnsw',
  params: { M: 16, efConstruction: 200 }
});

// Caching
db.setCache(new QueryCache({
  maxSize: 10000,
  ttl: 3600000
}));
```

## Optimization Techniques

### Quantization
- **Product Quantization**: 4-8x compression
- **Scalar Quantization**: 2-4x compression
- **Binary Quantization**: 32x compression

### Indexing
- **HNSW**: 150x faster, high accuracy
- **IVF**: Fast, partitioned search
- **LSH**: Approximate search

### Caching
- **Query Cache**: LRU eviction
- **Result Cache**: TTL-based
- **Embedding Cache**: Reuse embeddings

## Success Metrics
- [assert|neutral] Memory reduction: 4-32x [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] Search speedup: 150x [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] Accuracy maintained: > 95% [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] Cache hit rate: > 70% [ground:acceptance-criteria] [conf:0.90] [state:provisional]

## MCP Requirements

This skill operates using AgentDB's npm package and API only. No additional MCP servers required.

All AgentDB optimization operations are performed through:
- npm CLI: `npx agentdb@latest`
- TypeScript/JavaScript API: `import { AgentDB, Quantization, QueryCache } from 'agentdb-optimization'`

## Additional Resources

- Full docs: SKILL.md
- AgentDB Optimization: https://agentdb.dev/docs/optimization

## Core Principles

AgentDB Vector Search Optimization operates on 3 fundamental principles:

### Principle 1: Quantization - Trade Negligible Accuracy for Massive Memory Reduction

Vector databases face a fundamental constraint: high-dimensional embeddings (768-1536 dimensions) consume enormous memory at scale. Quantization techniques compress vectors by 4-32x through codebook encoding, enabling systems to hold millions of vectors in memory while maintaining 95%+ accuracy.

In practice:
- Apply product quantization (4-8x compression) for production workloads requiring high accuracy
- Use scalar quantization (2-4x compression) when exact distances matter for ranking
- Deploy binary quantization (32x compression) for massive-scale approximate search where recall > precision

### Principle 2: HNSW Indexing - Logarithmic Search Instead of Linear Scan

Brute-force vector search scales O(n) - doubling vectors doubles search time. HNSW (Hierarchical Navigable Small World) indexes create multi-layer graphs that enable O(log n) search, delivering 150x speedups with tunable accuracy trade-offs through the efSearch parameter.

In practice:
- Build HNSW indexes

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
  pattern: "skills/agentdb/AgentDB Vector Search Optimization/{project}/{timestamp}",
  store: ["executions", "decisions", "patterns"],
  retrieve: ["similar_tasks", "proven_patterns"]
} [ground:system-policy] [conf:1.0] [state:confirmed]

[define|neutral] MEMORY_TAGGING := {
  WHO: "AgentDB Vector Search Optimization-{session_id}",
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

[commit|confident] <promise>AGENTDB VECTOR SEARCH OPTIMIZATION_VERILINGUA_VERIX_COMPLIANT</promise> [ground:self-validation] [conf:0.99] [state:confirmed]
