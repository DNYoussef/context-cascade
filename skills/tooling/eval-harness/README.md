# Eval Harness

Frozen benchmark and regression gate for all self-improvement work. The harness never self-modifies; it only reports pass/fail decisions with evidence and confidence ceilings.

## Quick Start
1. Identify target skill/build and select suites; record hashes of benchmarks and scoring scripts.
2. Load prior runs for comparables; confirm environment.
3. Execute frozen suites; capture metrics and logs.
4. Compare against baselines; decide ACCEPT/REJECT/ROLLBACK with rationale.
5. Archive reports and confidence line using memory tags.

## Inputs
- Target identifier, selected suites, environment notes.
- Optional: latency budgets, hardware constraints.

## Outputs
- Metrics/regressions, decision, risks, and follow-ups.
- Confidence line: `Confidence: X.XX (ceiling: TYPE Y.YY)`.
- Memory namespace: `skills/tooling/eval-harness/{project}/{timestamp}`.

## Guardrails
- Benchmarks and scoring remain frozen; edits require manual versioning.
- Evidence-first reporting; no silent threshold changes.
- Confidence ceilings enforced on all verdicts.

Confidence: 0.70 (ceiling: inference 0.70) – README aligned to Prompt Architect clarity + Skill Forge safeguards.
