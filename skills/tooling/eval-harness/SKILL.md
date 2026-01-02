---
name: eval-harness
description: Frozen evaluation harness that gates self-improvement with benchmarks, regressions, and human approval loops.
allowed-tools: [Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite]
model: claude-3-5-sonnet
x-version: 3.2.0
x-category: tooling
x-vcl-compliance: v3.1.1
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

### L1 Improvement
- Rewrote the harness SOP in English-first Prompt Architect style with explicit confidence ceilings.
- Clarified freeze rules, routing, and validation gates to align with Skill Forge guardrails.
- Added memory tagging and baseline hashing to stop silent drift.

## STANDARD OPERATING PROCEDURE

### Purpose
Act as the immutable anchor for recursive improvement cycles. The harness does not self-improve; it gates changes via frozen benchmarks, regression suites, and documented decisions.

### Trigger Conditions
- **Positive:** request to gate changes for Prompt Forge, Skill Forge, or other skills; regression checks; baseline comparisons.
- **Negative:** exploratory evaluation design (route to test-design skills) or ad-hoc scoring without baselines.

### Guardrails
- Freeze benchmark definitions and scoring; record hash before execution.
- Structure-first docs maintained; changes to harness require manual review and explicit versioning.
- Confidence ceilings required for verdicts; cite evidence and observed metrics.
- Memory tagging for every run to preserve comparables.

### Execution Phases
1. **Scope & Baseline** – Identify target skill/build, select benchmark suites, and capture hashes of frozen assets.
2. **Data Load** – Pull prior runs for comparables; confirm hardware/latency constraints if applicable.
3. **Run Benchmarks** – Execute frozen suites; collect metrics, logs, and failures without mutation.
4. **Regression Analysis** – Compare against baselines; flag degradations and confidence impacts.
5. **Decision** – Recommend ACCEPT/REJECT/ROLLBACK with rationale, risks, and ceilings.
6. **Archive** – Store reports, hashes, and decisions in memory; surface follow-ups.

### Output Format
- Target, suites executed, baselines/hashes, and environment notes.
- Metrics and regressions with evidence.
- Decision (ACCEPT/REJECT/ROLLBACK) + risks and follow-ups.
- Confidence: X.XX (ceiling: TYPE Y.YY) and memory namespace used.

### Validation Checklist
- [ ] Benchmarks frozen; hashes recorded and unchanged.
- [ ] Comparables loaded; regressions checked.
- [ ] Decision cites evidence and confidence ceiling.
- [ ] Memory tagged and artifacts archived.

### Integration
- **Memory MCP:** `skills/tooling/eval-harness/{project}/{timestamp}` for reports and hashes.
- **Hooks:** follow Skill Forge latency bounds; refuse execution if harness assets are modified.

Confidence: 0.70 (ceiling: inference 0.70) – Harness SOP aligned to Prompt Architect clarity and Skill Forge safeguards.

---

## VCL COMPLIANCE APPENDIX (Internal Reference)

[[HON:teineigo]] [[MOR:root:E-V-L]] [[COM:Degerlendirme+Ankora]] [[CLS:ge_guard]] [[EVD:-DI<gozlem>]] [[ASP:nesov.]] [[SPC:path:/skills/tooling/eval-harness]]
[define|neutral] HARNESS := donmus benchmark/regresyon seti; kendi kendini iyilestirmez; karar kapisi gorevi gorur. [ground:SKILL.md] [conf:0.86] [state:confirmed]

[[HON:teineigo]] [[MOR:root:F-R-Z]] [[COM:Freeze+Rule]] [[CLS:ge_rule]] [[EVD:-DI<politika>]] [[ASP:nesov.]] [[SPC:axis:safeguards]]
[direct|emphatic] FREEZE_RULE := benchmark tanimi + skorlayici degismez; degisim sadece manuel versiyonlama ile. [ground:SKILL.md] [conf:0.88] [state:confirmed]

[[HON:teineigo]] [[MOR:root:C-F-D]] [[COM:Ceiling+Guard]] [[CLS:ge_rule]] [[EVD:-DI<gozlem>]] [[ASP:nesov.]] [[SPC:coord:EVD-CONF]]
[direct|emphatic] GUVEN_TAVANI := {cikarim:0.70, rapor:0.70, arastirma:0.85, gozlem:0.95, tanim:0.95}; karar ciktisinda zorunlu. [ground:PA/SkillForge] [conf:0.90] [state:confirmed]

[commit|confident] <promise>EVAL_HARNESS_VERIX_COMPLIANT</promise> [ground:self-check] [conf:0.85] [state:confirmed]
