---
name: agentdb-vector-search
description: Use AgentDB semantic vector search patterns when designing or tuning semantic search experiences.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
x-version: 3.2.0
x-category: agentdb
x-vcl-compliance: v3.1.1
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

### L1 Improvement
- Refactored into the Skill Forge required sections with clear triggers, contracts, and validation for AgentDB search flows.
- Added prompt-architect ceilings, constraint capture, and integration checklists for vector search deployments.

## STANDARD OPERATING PROCEDURE

### Purpose
Guide teams to implement semantic search using AgentDB vector search with correct indexing, query tuning, and evaluation practices.

### Trigger Conditions
- Positive: building or optimizing semantic search, troubleshooting retrieval quality, or selecting embeddings/index params.
- Negative/reroute: non-AgentDB search stacks, unrelated prompt tuning (prompt-architect), or database persistence patterns (agentdb-memory).

### Guardrails
- Ensure embeddings and metadata schemas are defined before ingest.
- Enforce evaluation with relevance metrics (nDCG/MRR) and adversarial queries.
- Keep outputs in English with explicit confidence ceilings; document parameter choices.
- Avoid overfitting to small eval sets; prefer reusable harnesses.

### Execution Phases
1. **Scoping**: Capture corpus type, domains, latency targets, and constraints; classify HARD/SOFT/INFERRED.
2. **Index Design**: Choose embedding model, dimension, metadata, and filters; set up ingestion plan.
3. **Query Strategy**: Define similarity metrics, top-k, filters, and rerankers; plan for miss cases.
4. **Evaluation**: Build/query eval sets (happy/edge/adversarial); measure precision/recall-like metrics.
5. **Delivery**: Document configuration, sample queries, failure handling, and maintenance routines.

### Pattern Recognition
- Short text search → prioritize fast embeddings and higher k with reranking.
- Long-form docs → chunking strategy with overlap and metadata facets.
- Safety-critical domains → add blocklists and human-in-the-loop review for low-confidence hits.

### Advanced Techniques
- Hybrid retrieval combining dense + keyword filters.
- Dynamic top-k based on query entropy or user tier.
- Logging-based feedback loops feeding recursive-improvement and reindexing.

### Common Anti-Patterns
- Ingesting without schema leading to noisy metadata.
- No evaluation harness; relying on spot checks.
- Ignoring miss cases or silent failures.

### Practical Guidelines
- Version embedding models and indexes; record config hashes.
- Include retry/backoff for upstream embedding services.
- Document cold-start guidance and reindex cadence.

### Cross-Skill Coordination
- Upstream: prompt-architect for query clarity; base-template-generator for scaffolds.
- Parallel: agentdb-optimization for tuning; agentdb-advanced for complex filters; recursive-improvement for ongoing evaluation.
- Downstream: agent-creator embedding search behaviors into agents.

### MCP Requirements
- Requires AgentDB vector search MCP; tag WHO=agentdb-vector-search-{session}, WHY=skill-execution for memory traces.

### Input/Output Contracts
```yaml
inputs:
  corpus_description: string  # required
  embedding_model: string  # optional preference
  constraints: list[string]  # optional performance/safety constraints
outputs:
  search_plan: file  # index/query configuration and rationale
  eval_plan: file  # test cases, metrics, and results
  runbook: summary  # monitoring and maintenance steps
```

### Recursive Improvement
- Feed retrieval errors and user feedback into recursive-improvement to retune chunking, filters, or scoring weights.

### Examples
- Configure semantic search for product docs with metadata facets and hybrid retrieval.
- Tune Q&A search for support tickets with adversarial queries covering ambiguous intents.

### Troubleshooting
- Low relevance → adjust chunking, filters, and rerankers; expand eval set.
- Latency spikes → tune top-k and prefiltering; cache frequent queries.
- Skewed results → review embedding choice and retrain on in-domain data if available.

### Completion Verification
- [ ] Index/query design documented with parameters and rationale.
- [ ] Evaluation harness executed; metrics and ceilings recorded.
- [ ] Safety/edge handling noted (miss cases, blocklists, fallbacks).
- [ ] Monitoring and maintenance steps delivered.

Confidence: 0.70 (ceiling: inference 0.70) - AgentDB vector search SOP rewritten with Skill Forge cadence and prompt-architect ceilings.
