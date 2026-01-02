# System Design Architect Guide

Use this skill to produce architecture docs, capacity plans, and reliability strategies.

## How to Engage
1. Capture HARD/SOFT/INFERRED constraints (SLOs, scale, cost, compliance, timelines).
2. Ask for existing architecture/assets; identify integration boundaries.
3. Produce candidate designs with tradeoffs, then pick a direction with validation plan.

## Guardrails
- Maintain SKILL.md plus examples/tests; fill gaps before delivery.
- Plan observability, rollout/rollback, and failure tests.
- Declare confidence with ceiling (inference/report 0.70; research 0.85; observation/definition 0.95).
- MCP tags: `WHO=system-design-architect-{session}`, `WHY=skill-execution`.

## Standard Outputs
- Architecture diagram + rationale
- Data model/storage/caching plan
- Validation (load/chaos/rollback) and runbook notes

Confidence: 0.71 (ceiling: inference 0.70) - Guide aligned with the refreshed SOP.
