# ML Expert Skill Guide

Use `ml-expert` when you need production-quality ML implementation: architecture selection, training pipelines, optimization, and deployment readiness.

## Quick Use
1. Capture HARD/SOFT/INFERRED constraints (metrics, latency, memory, data rules).
2. Confirm data sources and privacy/compliance requirements.
3. Plan baseline + ablations; align with validation checklist.

## Guardrails (Skill-Forge + Prompt-Architect)
- Structure-first: maintain SKILL.md, examples, tests, resources, agents.
- No data leakage; hold out test data until final evaluation.
- Explicit confidence ceiling on findings (inference/report 0.70; research 0.85; observation/definition 0.95).
- MCP tags: `WHO=ml-expert-{session}`, `WHY=skill-execution`.

## Standard Deliverables
- Architecture and training plan (with configs and seeds).
- Experiment matrix and validated metrics.
- Deployment+rollback checklist with monitoring plan.

Confidence: 0.72 (ceiling: inference 0.70) - Guide aligned to the updated SOP and validation guardrails.
