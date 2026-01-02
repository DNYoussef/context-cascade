# Bootstrap Loop (Prompt Forge ↔ Skill Forge)

Purpose: orchestrate the recursive improvement cycle where Prompt Forge diagnoses, Skill Forge rebuilds, and the frozen eval harness gates changes. Follow the Prompt Architect style for clarity, explicit constraints, and confidence ceilings.

## When to Use
- Running cross-improvement between Prompt Forge and Skill Forge.
- Auditing meta-skills with a frozen evaluation anchor.
- Replaying prior cycles with regressions prevented by the harness.

## Inputs & Setup
- Target: `prompt-forge`, `skill-forge`, or `both`.
- Baselines: frozen eval suites + regression hashes recorded before execution.
- Memory: tag MCP entries with `WHO=bootstrap-loop-{session}`, `WHY=skill-execution`, `PROJECT=<name>`, `WHEN=<iso>`.

## Run Path (Skill Forge cadence)
1. Confirm triggers and blast radius; load prior runs from memory.
2. Freeze benchmarks; collect constraints via Prompt Architect.
3. Generate proposals with Prompt Forge; build with Skill Forge.
4. Gate with eval harness; compare deltas; decide accept/reject/rollback.
5. Archive artifacts, risks, and confidence with ceiling syntax.

## Outputs
- Cycle summary with decision, metrics, and regression status.
- Artifacts: proposals, diffs, eval reports, rollback notes.
- Confidence line: `Confidence: X.XX (ceiling: TYPE Y.YY) – rationale`.

## Quality Gates
- Harness unchanged and hashed.
- Evidence-backed proposals and decisions.
- Confidence ceilings respected; rollback if metrics drop.

Confidence: 0.70 (ceiling: inference 0.70) – README aligned to Prompt Architect + Skill Forge structure-first guardrails.
