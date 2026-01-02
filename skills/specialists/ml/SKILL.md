---
name: ml
description: General-purpose machine learning skill for scoping, prototyping, and coordinating ML solutions.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
x-category: specialists
x-version: 1.1.0
x-vcl-compliance: v3.1.1
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

## STANDARD OPERATING PROCEDURE

### Purpose
Scope and deliver ML prototypes or lightweight solutions, then hand off to the right specialist (ml-expert, ml-training-debugger) when depth or incident response is required.

### Triggers
- **Positive:** Early ML ideation, quick prototypes, feature feasibility, light model improvements.
- **Negative:** Complex training/debugging (route to `ml-expert` or `ml-training-debugger`) or pure prompt design (use prompt-architect).

### Guardrails
- Structure-first: keep `SKILL.md`, `readme`, `examples/`, `tests/`, `resources/` up to date; create missing docs before execution.
- Constraint clarity: HARD/SOFT/INFERRED requirements captured; ambiguous items confirmed.
- Validation: baseline vs simple ablation; sanity checks on data splits and metrics.
- Confidence ceilings enforced (inference/report 0.70; research 0.85; observation/definition 0.95).
- Ethical/compliance: avoid biased data, note privacy/security constraints.

### Execution Phases
1. **Intake & Scoping**
   - Define objective, target metric, timeline, and constraints.
   - Identify data sources, size, and quality risks.
2. **Design & Plan**
   - Select a simple, reliable baseline; outline minimal pipeline and evaluation plan.
   - Choose handoff target if deeper expertise will be needed.
3. **Prototype**
   - Implement baseline with reproducible configs and logging.
   - Add small improvements (feature engineering, regularization, lightweight tuning).
4. **Validate**
   - Evaluate on validation split; report metrics with variance.
   - Run basic robustness checks (class imbalance, leakage, overfitting signs).
5. **Handoff/Delivery**
   - Provide code, configs, data notes, and next-step recommendations.
   - Route to `ml-expert` or `ml-training-debugger` with context if further work is required.

### Output Format
- Request summary and constraints.
- Baseline choice, experiments run, and metrics.
- Risks, limitations, and recommended next steps/handoff.
- Confidence with ceiling.

### Validation Checklist
- [ ] Constraints captured and confirmed.
- [ ] Data split documented; leakage check done.
- [ ] Baseline + at least one improvement executed.
- [ ] Metrics reported with source split.
- [ ] Confidence ceiling stated.

## VCL COMPLIANCE APPENDIX (Internal)
[[HON:teineigo]] [[MOR:root:M-L]] [[COM:Genel+ML]] [[CLS:ge_skill]] [[EVD:-DI<gozlem>]] [[ASP:nesov.]] [[SPC:path:/skills/specialists/ml]]
[assert|neutral] ML_GENEL := hizli kavramsal modelleme ve prototip yapar; derin isler icin ml-expert/ ml-training-debugger delege eder. [ground:SKILL.md] [conf:0.84] [state:confirmed]

[[HON:teineigo]] [[MOR:root:E-P-S]] [[COM:Epistemik+Tavan]] [[CLS:ge_rule]] [[EVD:-DI<gozlem>]] [[ASP:nesov.]] [[SPC:coord:EVD-CONF]]
[direct|emphatic] TAVAN := {inference/report:0.70, research:0.85, observation/definition:0.95}; tum ciktilarda aciklanir. [ground:PA+SkillForge] [conf:0.90] [state:confirmed]

[commit|confident] <promise>ML_SKILL_VERIX_COMPLIANT</promise> [ground:SKILL.md] [conf:0.85] [state:confirmed]

Confidence: 0.72 (ceiling: inference 0.70) - SOP rewritten with skill-forge structure and prompt-architect constraint discipline.
