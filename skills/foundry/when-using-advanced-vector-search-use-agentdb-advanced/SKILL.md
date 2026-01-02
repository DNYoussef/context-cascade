---
name: agentdb-advanced
description: Apply advanced AgentDB vector search patterns such as hybrid retrieval, faceting, and multi-tenant isolation.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
x-version: 3.2.0
x-category: agentdb
x-vcl-compliance: v3.1.1
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

### L1 Improvement
- Reworked into Skill Forge required sections with explicit guardrails for complex vector search deployments.
- Added prompt-architect constraint capture, confidence ceilings, and integration notes for advanced features.

## STANDARD OPERATING PROCEDURE

### Purpose
Guide advanced AgentDB vector search implementations involving hybrid retrieval, multi-tenant isolation, faceted filters, and custom scoring.

### Trigger Conditions
- Positive: need hybrid dense+keyword retrieval, strict tenancy boundaries, advanced filters, or custom reranking.
- Negative/reroute: basic setup (agentdb-vector-search) or optimization only (agentdb-optimization).

### Guardrails
- Enforce tenant isolation and access controls for multi-tenant scenarios.
- Validate filter correctness and leakage with adversarial queries.
- Keep outputs English-only with explicit confidence ceilings; document assumptions.
- Monitor latency impacts of complex pipelines and set rollback thresholds.

### Execution Phases
1. **Requirements**: Capture tenancy model, filters, scoring rules, and constraints; classify HARD/SOFT/INFERRED.
2. **Design**: Choose hybrid strategy (dense+bm25), facet schema, isolation model, and reranking approach.
3. **Implementation**: Configure indexes, filters, and scoring functions; set up monitoring for leakage/latency.
4. **Validation**: Run multi-tenant and adversarial tests; evaluate relevance, isolation, and performance.
5. **Rollout**: Deploy with staged rollout, alerts, and rollback plans; document configs and ceilings.

### Pattern Recognition
- Multi-tenant SaaS → strict namespace/tag isolation and ACL checks.
- Domain with strong keywords → combine dense + keyword scoring with boosts.
- Compliance-heavy data → add audit logging and blocklists.

### Advanced Techniques
- Dynamic routing to hybrid vs dense-only based on query classification.
- Per-tenant embeddings or domain-adaptive rerankers.
- Faceted navigation with precomputed aggregations for speed.

### Common Anti-Patterns
- Missing isolation tests leading to cross-tenant leaks.
- Overly complex scoring without evaluation evidence.
- Ignoring latency impacts of chained rerankers.

### Practical Guidelines
- Version configs and scoring functions; keep changelogs.
- Use canary tenants or shadow traffic for risky changes.
- Document filter semantics and failure behaviors.

### Cross-Skill Coordination
- Upstream: agentdb-vector-search for basics; prompt-architect for query clarity.
- Parallel: agentdb-optimization for tuning; recursive-improvement for iterative fixes.
- Downstream: agent-creator/agent-selector embedding advanced configs into agents.

### MCP Requirements
- Requires AgentDB vector search MCP with support for filters and hybrid retrieval; tag WHO=agentdb-advanced-{session}, WHY=skill-execution.

### Input/Output Contracts
```yaml
inputs:
  tenancy_model: string  # required
  search_requirements: list[string]  # required advanced needs
  constraints: list[string]  # optional safety/performance constraints
outputs:
  design_doc: file  # architecture and configuration
  test_plan: file  # isolation/relevance/performance tests
  rollout_notes: summary  # deployment, monitoring, rollback
```

### Recursive Improvement
- Feed leakage events or performance regressions into recursive-improvement to adjust filters, scoring, or isolation.

### Examples
- Implement hybrid retrieval with bm25 + dense embeddings and per-tenant ACL checks.
- Add faceted search for product catalogs with latency budgets and monitoring.

### Troubleshooting
- Cross-tenant leakage → audit tags/ACLs and rerun isolation tests; rollback if needed.
- Latency regressions → simplify pipeline or cache facets.
- Irrelevant results on keyword-heavy queries → adjust boosts or rerankers.

### Completion Verification
- [ ] Isolation, relevance, and performance requirements documented and tested.
- [ ] Configurations versioned with changelog and ceilings.
- [ ] Rollout/rollback plan in place with monitoring hooks.
- [ ] Security and compliance considerations addressed.

Confidence: 0.70 (ceiling: inference 0.70) - AgentDB advanced search SOP rewritten with Skill Forge cadence and prompt-architect ceilings.
