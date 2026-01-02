---
name: agentdb-optimization
description: Optimize AgentDB vector search configurations for relevance, latency, and cost with structured evaluation.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
x-version: 3.2.0
x-category: agentdb
x-vcl-compliance: v3.1.1
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

### L1 Improvement
- Reframed the optimization guidance into Skill Forge required sections with explicit evaluation and tuning loops.
- Added prompt-architect constraint capture, confidence ceilings, and safety rails for relevance experiments.

## STANDARD OPERATING PROCEDURE

### Purpose
Tune AgentDB vector search parameters (embeddings, chunking, filters, rerankers, caching) to improve relevance and latency with evidence.

### Trigger Conditions
- Positive: relevance issues, latency/cost concerns, or experiments on search quality.
- Negative/reroute: initial search setup (agentdb-vector-search) or non-AgentDB search stacks.

### Guardrails
- Run A/B or offline evaluations; do not deploy changes without evidence.
- Avoid simultaneous changes to multiple parameters; isolate variables.
- Keep outputs in English with explicit confidence ceilings; record configs and metrics.
- Monitor for regressions post-change with rollback plan.

### Execution Phases
1. **Baseline**: Capture current metrics, configs, constraints, and pain points; classify HARD/SOFT/INFERRED.
2. **Hypotheses**: Identify candidate changes (top-k, filters, models, rerankers, chunking) and expected impact.
3. **Experiments**: Run controlled tests (offline or shadow); collect relevance and latency metrics.
4. **Analysis**: Compare against baseline; flag trade-offs and ceilings.
5. **Deployment**: Roll out winning config with monitoring, rollback, and documentation.

### Pattern Recognition
- High latency → lower top-k, prefilter by metadata, or add caching.
- Poor relevance on specific intents → adjust chunking and embeddings, add domain-specific rerankers.
- Cost pressure → reduce index updates or batch processing.

### Advanced Techniques
- Adaptive top-k based on query difficulty or user tier.
- Reranking with lightweight models to balance cost/perf.
- Active learning loops to expand eval sets from misses.

### Common Anti-Patterns
- Deploying untested changes directly to production.
- Comparing results without consistent metrics or datasets.
- Not logging configuration versions, making rollbacks hard.

### Practical Guidelines
- Maintain a changelog with config hash, metrics, and ceilings.
- Use representative and adversarial queries in eval sets.
- Coordinate with caching and memory teams when changing schemas.

### Cross-Skill Coordination
- Upstream: agentdb-vector-search for baseline setup; prompt-architect for query clarity.
- Parallel: agentdb-advanced for complex filters; recursive-improvement for iterative tuning.
- Downstream: agent-creator embedding optimized settings into agents.

### MCP Requirements
- Requires AgentDB vector search MCP; tag WHO=agentdb-optimization-{session}, WHY=skill-execution during experiments.

### Input/Output Contracts
```yaml
inputs:
  baseline_metrics: object  # required
  constraints: list[string]  # required performance/safety constraints
  hypotheses: list[string]  # optional tuning ideas
outputs:
  experiment_plan: file  # tests, datasets, metrics
  results: file  # outcomes with ceilings
  rollout_plan: summary  # chosen config, monitoring, rollback
```

### Recursive Improvement
- Loop through recursive-improvement with new failures/misses to refine hypotheses and configs.

### Examples
- Reduce latency for Q&A search by adjusting top-k and adding metadata filters.
- Improve relevance for long-form docs with new chunking and reranker tuning.

### Troubleshooting
- Metrics inconclusive → increase sample size or narrow variables.
- Regression post-deploy → rollback to last good config and analyze logs.
- Unexpected costs → review embedding frequency and caching strategy.

### Completion Verification
- [ ] Baseline and hypotheses documented.
- [ ] Experiments run with metrics and ceilings recorded.
- [ ] Deployment plan includes monitoring and rollback.
- [ ] Changelog updated with configuration hash.

Confidence: 0.70 (ceiling: inference 0.70) - AgentDB optimization SOP rewritten with Skill Forge cadence and prompt-architect ceilings.
