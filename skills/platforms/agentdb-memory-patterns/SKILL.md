/*============================================================================*/
/* AGENTDB-MEMORY-PATTERNS SKILL :: VERILINGUA x VERIX EDITION                      */
/*============================================================================*/

---
name: agentdb-memory-patterns
version: 1.0.0
description: |
  [assert|neutral] Apply persistent memory patterns for AI agents using AgentDB. Implement session memory, configure long-term storage, enable pattern learning, and manage context across sessions. Use when building stat [ground:given] [conf:0.95] [state:confirmed]
category: platforms
tags:
- platforms
- integration
- tools
author: ruv
cognitive_frame:
  primary: aspectual
  goal_analysis:
    first_order: "Execute agentdb-memory-patterns workflow"
    second_order: "Ensure quality and consistency"
    third_order: "Enable systematic platforms processes"
---

/*----------------------------------------------------------------------------*/
/* S0 META-IDENTITY                                                            */
/*----------------------------------------------------------------------------*/

[define|neutral] SKILL := {
  name: "agentdb-memory-patterns",
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
  keywords: ["agentdb-memory-patterns", "platforms", "workflow"],
  context: "user needs agentdb-memory-patterns capability"
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


# AgentDB Memory Patterns

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



## What This Skill Does

**Use this skill to** implement memory management patterns for AI agents using AgentDB's persistent storage and ReasoningBank integration. **Apply** these patterns to enable agents to remember conversations, learn from interactions, and maintain context across sessions. **Deploy** triple-layer retention (24h/7d/30d+) for optimal memory organization.

**Performance**: 150x-12,500x faster than traditional solutions with 100% backward compatibility.

## Prerequisites

**Install** Node.js 18+ and AgentDB v1.0.7+. **Ensure** you have AgentDB via agentic-flow or standalone. **Review** agent architecture patterns before implementing memory systems.

## Quick Start with CLI

### Initialize AgentDB

**Run** these commands to set up your AgentDB instance with memory patterns:

```bash
# Initialize vector database
npx agentdb@latest init ./agents.db

# Or with custom dimensions
npx agentdb@latest init ./agents.db --dimension 768

# Use preset configurations
npx agentdb@latest init ./agents.db --preset large

# In-memory database for testing
npx agentdb@latest init ./memory.db --in-memory
```

### Start MCP S

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
  pattern: "skills/platforms/agentdb-memory-patterns/{project}/{timestamp}",
  store: ["executions", "decisions", "patterns"],
  retrieve: ["similar_tasks", "proven_patterns"]
} [ground:system-policy] [conf:1.0] [state:confirmed]

[define|neutral] MEMORY_TAGGING := {
  WHO: "agentdb-memory-patterns-{session_id}",
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

[commit|confident] <promise>AGENTDB_MEMORY_PATTERNS_VERILINGUA_VERIX_COMPLIANT</promise> [ground:self-validation] [conf:0.99] [state:confirmed]
