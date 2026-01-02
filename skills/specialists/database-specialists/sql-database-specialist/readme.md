# SQL Database Specialist Guide

## Use Cases
- Query optimization and performance diagnostics
- Schema design/refactor and indexing strategies
- Migration planning with rollback safety

## Fast Path
1. Capture constraints (latency/throughput SLOs, downtime, storage budget, compliance).
2. Baseline with EXPLAIN/plan and metrics.
3. Propose schema/query changes + migration steps with rollback.
4. Validate on staging; measure before/after; document confidence with ceiling.

## Guardrails
- Maintain SKILL.md, examples, tests, resources.
- Always back up before migrations; prefer idempotent scripts.
- Confidence ceiling: inference/report 0.70; research 0.85; observation/definition 0.95.
- MCP tags: `WHO=sql-database-specialist-{session}`, `WHY=skill-execution`.

Confidence: 0.71 (ceiling: inference 0.70) - Guide aligned to refreshed SOP and safety rules.
