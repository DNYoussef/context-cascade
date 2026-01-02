# ML Skill Guide

Lightweight ML scoping and prototyping with clean handoffs to deeper specialists.

## Quick Path
1. Capture HARD/SOFT/INFERRED constraints (goal metric, data limits, latency, compliance).
2. Pick a simple baseline and validation plan.
3. Run baseline + one improvement; report metrics with split context.
4. Recommend next steps or escalate to `ml-expert` / `ml-training-debugger` with context.

## Guardrails
- Maintain structure: SKILL.md, readme, examples, tests, resources.
- No train/test leakage; document data provenance.
- Confidence ceiling required (inference/report 0.70; research 0.85; observation/definition 0.95).
- MCP tags: `WHO=ml-{session}`, `WHY=skill-execution`.

Confidence: 0.71 (ceiling: inference 0.70) - Guide refreshed to mirror the updated SOP and guardrails.
