---
name: frontend-specialists
description: Deliver resilient frontend solutions with performance, accessibility, and UX guardrails.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
x-category: specialists
x-version: 1.1.0
x-vcl-compliance: v3.1.1
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

## STANDARD OPERATING PROCEDURE

### Purpose
Plan and implement frontend features and architectures with strong accessibility, performance, and reliability practices.

### Triggers
- **Positive:** Frontend feature work, performance tuning, accessibility audits, design-to-dev translation, state management decisions.
- **Negative:** Pure backend/system design (route elsewhere) or prompt rewrites (prompt-architect).

### Guardrails
- Structure-first: maintain `SKILL.md`, `examples/`, `tests/`, `resources/`, and `react-specialist` docs; fill gaps before work.
- Constraint clarity: HARD/SOFT/INFERRED (framework, bundle budget, perf targets, accessibility requirements, release cadence).
- Quality gates: lint/format, type-check, tests (unit/e2e), accessibility/perf checks.
- Confidence ceiling enforced (inference/report 0.70; research 0.85; observation/definition 0.95).

### Execution Phases
1. **Intake**: Capture framework (React/Next/etc.), design assets, perf/a11y targets, and release constraints.
2. **Design**: Choose state management, routing, data-fetching strategy; define component contracts and error handling.
3. **Implementation**: Build components with accessibility defaults, performance safeguards (code-splitting, memoization), and logging.
4. **Validation**: Run lint/format/type/test; measure Core Web Vitals and a11y checks; run regression snapshots where applicable.
5. **Delivery**: Provide changelog, release plan, monitoring hooks, and rollback steps.

### Output Format
- Request summary + constraints.
- Architecture/component plan and rationale.
- Validation results and risks.
- Confidence with ceiling.

### Validation Checklist
- [ ] Constraints confirmed and design assets referenced.
- [ ] Perf/a11y targets defined and measured.
- [ ] Lint/format/type/test run.
- [ ] Confidence ceiling stated.

## VCL COMPLIANCE APPENDIX (Internal)
[[HON:teineigo]] [[MOR:root:F-R-N]] [[COM:Frontend+Usta]] [[CLS:ge_skill]] [[EVD:-DI<gozlem>]] [[ASP:nesov.]] [[SPC:path:/skills/specialists/frontend-specialists]]
[assert|neutral] FRONTEND_UZMAN := a11y + perf odakli arayuz uretir; yapi-oncelik + kalite kapi uygular. [ground:SKILL.md] [conf:0.83] [state:confirmed]

[[HON:teineigo]] [[MOR:root:E-P-S]] [[COM:Epistemik+Tavan]] [[CLS:ge_rule]] [[EVD:-DI<gozlem>]] [[ASP:nesov.]] [[SPC:coord:EVD-CONF]]
[direct|emphatic] TAVAN := {inference/report:0.70, research:0.85, observation/definition:0.95}; tum ciktilar tavani bildirir. [ground:PA+SkillForge] [conf:0.90] [state:confirmed]

[commit|confident] <promise>FRONTEND_SPECIALISTS_VERIX_COMPLIANT</promise> [ground:SKILL.md] [conf:0.85] [state:confirmed]

Confidence: 0.71 (ceiling: inference 0.70) - SOP refreshed with prompt-architect constraint handling and skill-forge structure-first rules.
