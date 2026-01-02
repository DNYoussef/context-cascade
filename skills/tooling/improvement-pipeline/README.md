# Improvement Pipeline

A structured loop (analyze → propose → build → validate → deliver) for improving prompts, skills, docs, or scripts with explicit guardrails.

## Quick Start
1. Capture intent, constraints, and success metrics.
2. Analyze current state and baselines.
3. Generate proposals with deltas; pick one with rationale.
4. Implement minimal diffs; keep rollback plan ready.
5. Validate vs baselines; summarize results with confidence ceiling.

## Inputs
- Target artifact, goals, constraints, success metrics.
- Options: validation suites to run, risk tolerance, report format.

## Outputs
- Applied changes, validation results, risks, follow-ups.
- Confidence line: `Confidence: X.XX (ceiling: TYPE Y.YY)` and memory namespace used (`skills/tooling/improvement-pipeline/{project}/{timestamp}`).

## Guardrails
- Structure-first docs maintained.
- No skipping validation; rollback on regressions.
- Confidence ceilings enforced; evidence cited.

Confidence: 0.70 (ceiling: inference 0.70) – README aligned to Prompt Architect + Skill Forge cadence.
