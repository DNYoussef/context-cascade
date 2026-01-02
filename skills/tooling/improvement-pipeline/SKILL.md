---
name: improvement-pipeline
description: Coordinate sequential improvement stages (analyze → propose → build → validate) with Prompt Architect clarity and Skill Forge guardrails.
allowed-tools: [Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite]
model: claude-3-5-sonnet
x-version: 3.2.0
x-category: tooling
x-vcl-compliance: v3.1.1
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

### L1 Improvement
- Simplified the pipeline into an English-first SOP aligned with Prompt Architect constraint ordering.
- Added structure-first documentation, confidence ceilings, and memory tagging per Skill Forge.
- Clarified validation gates and rollback expectations.

## STANDARD OPERATING PROCEDURE

### Purpose
Run disciplined improvement cycles for any artifact (prompt, skill, doc, script) across analyze → propose → build → validate → deliver.

### Trigger Conditions
- **Positive:** requests to improve/refine/upgrade an artifact with validation gates.
- **Negative:** net-new creation (route to creation skills) or emergency fixes without evaluation.

### Guardrails
- Maintain structure-first docs (SKILL, README, examples/tests/references). Log deviations.
- Confidence ceilings mandatory; cite evidence and baselines.
- No skipping validation; rollback if metrics regress or confidence < threshold.
- Memory tagging for each cycle.

### Execution Phases
1. **Intent & Constraints** – Use Prompt Architect style to extract objectives, constraints, and success metrics.
2. **Analysis** – Review current state, gather baselines, and capture risks.
3. **Proposals** – Generate options with deltas and blast radius notes; select path.
4. **Build** – Implement chosen changes with minimal diffs and rollback plan.
5. **Validation** – Run tests/benchmarks/lints; compare to baselines; document outcomes.
6. **Delivery** – Summarize changes, decisions, metrics, and confidence ceiling; archive artifacts.

### Output Format
- Target artifact, goals, constraints, and selected proposal.
- Changes applied with evidence of improvement vs baseline.
- Risks, follow-ups, and rollback info.
- Confidence: X.XX (ceiling: TYPE Y.YY) and memory keys used.

### Validation Checklist
- [ ] Constraints and success metrics captured.
- [ ] Baseline recorded; validation executed.
- [ ] Regression/impact analysis completed.
- [ ] Memory tagged and artifacts stored.
- [ ] Confidence ceiling declared.

### Integration
- **Memory MCP:** `skills/tooling/improvement-pipeline/{project}/{timestamp}`.
- **Hooks:** align with Skill Forge latency bounds; integrate with eval-harness when gating is required.

Confidence: 0.70 (ceiling: inference 0.70) – Pipeline rewritten to blend Prompt Architect clarity with Skill Forge delivery gates.

---

## VCL COMPLIANCE APPENDIX (Internal Reference)

[[HON:teineigo]] [[MOR:root:I-Y-I]] [[COM:Improvement+Hatti]] [[CLS:ge_pipeline]] [[EVD:-DI<gozlem>]] [[ASP:nesov.]] [[SPC:path:/skills/tooling/improvement-pipeline]]
[define|neutral] IMP_PIPE := analiz→oner→insaa→dogrula→teslim; atlama yasak. [ground:SKILL.md] [conf:0.83] [state:confirmed]

[[HON:teineigo]] [[MOR:root:G-R-L]] [[COM:Guardrail]] [[CLS:ge_rule]] [[EVD:-DI<politika>]] [[ASP:nesov.]] [[SPC:axis:safeguards]]
[direct|emphatic] VAL_GATES := dogrulama ve rollback planlari olmadan gecis yok; confidence tavani beyan edilir. [ground:SKILL.md] [conf:0.87] [state:confirmed]

[commit|confident] <promise>IMPROVEMENT_PIPELINE_VERIX_COMPLIANT</promise> [ground:self-check] [conf:0.85] [state:confirmed]
