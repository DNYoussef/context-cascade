# Clarity Linter

Evaluate readability and cognitive load with a five-dimension rubric, then deliver minimal diffs backed by evidence and confidence ceilings.

## Quick Start
1. Identify scope (file or directory) and policy (strict|standard|lenient).
2. Run metrics collection and rubric evaluation; store outputs under `skills/tooling/clarity-linter/{project}/{timestamp}`.
3. Generate fixes and rerun metrics; accept only if clarity score improves.

## Inputs
- `target` path (file|directory), `policy` (default standard).
- Optional: `auto_fix`, `report_format` (md|json), `min_score_threshold`.

## Outputs
- Metrics snapshot + rubric scores + verdict.
- Ranked violations with evidence and proposed/applied patches.
- Confidence line: `Confidence: X.XX (ceiling: TYPE Y.YY)`.

## Guardrails
- Structure-first package (SKILL.md, README, examples/tests/references up to date).
- Frozen rubric + explicit thresholds; cite evidence per issue.
- Confidence ceilings enforced; rollback on regressions.

Confidence: 0.70 (ceiling: inference 0.70) – README aligned to Prompt Architect constraint-first flow.
