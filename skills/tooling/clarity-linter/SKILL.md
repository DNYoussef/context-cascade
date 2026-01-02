---
name: clarity-linter
description: Evaluate and improve code clarity and cognitive load with rubric-driven scoring and targeted fixes.
allowed-tools: [Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite]
model: claude-3-5-sonnet
x-version: 3.2.0
x-category: tooling
x-vcl-compliance: v3.1.1
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

### L1 Improvement
- Rewrote the clarity linter as an English-first SOP with Prompt Architect-style constraint surfacing.
- Added structure-first guardrails, adversarial validation hooks, and confidence ceilings per Skill Forge.
- Consolidated input/output contracts into a single execution path for faster dogfooding.

## STANDARD OPERATING PROCEDURE

### Purpose
Assess readability and cognitive load, then deliver fixes with rubric-backed evidence.

### Trigger Conditions
- **Positive:** "clarity audit", "reduce cognitive load", "naming/readability review", "thin helper detection".
- **Negative:** coupling-only analysis (use connascence-analyzer), security/performance scans, or quick lint (use quick-quality-check).

### Guardrails
- Structure-first package: `SKILL.md`, `README.md`, `examples/`, `tests/`, `references/` kept current.
- Use explicit clarity rubric (size, indirection, call depth, duplication, explanation quality) and cite evidence.
- Apply confidence ceilings; do not overclaim automated fixes without human review when confidence <0.80.
- Store runs in memory with WHO/WHY/WHEN/PROJECT tags for traceability.

### Execution Phases
1. **Intent & Scope** – Confirm language, repo area, and goal (audit vs fix). Load domain expertise if available.
2. **Metrics Collection** – Gather size, nesting, call depth, duplication, naming signals, and comment density.
3. **Rubric Evaluation** – Score five dimensions; classify verdict (ACCEPT ≥0.80, REFINE 0.60–0.79, REJECT <0.60).
4. **Fix Planning** – Rank violations by impact; propose minimal-change patches.
5. **Fix Generation** – Apply or draft patches; keep diffs small and reversible.
6. **Validation** – Rerun metrics; ensure clarity score improves and tests still pass.
7. **Delivery** – Summarize findings, decisions, diffs, and confidence ceiling.

### Input Contract (minimum)
- `target`: file|directory with path.
- `policy`: strict|standard|lenient (defaults to standard thresholds).
- Flags: `auto_fix` (default false), `report_format` (md|json), `min_score_threshold` (default 0.60).

### Output Format
- Metrics snapshot, rubric scores, verdict, and top violations with evidence.
- Fix plan and applied/queued patches.
- Risks, follow-ups, and memory keys used.
- Confidence: X.XX (ceiling: TYPE Y.YY).

### Validation Checklist
- [ ] Trigger confirmed; correct domain expertise loaded.
- [ ] Rubric applied; evidence attached for each violation.
- [ ] If auto-fix enabled, regressions and tests rerun.
- [ ] Memory tagged and report stored.
- [ ] Confidence ceiling declared.

### Integration
- **Memory MCP:** `skills/tooling/clarity-linter/{project}/{timestamp}` for reports and diffs.
- **Hooks:** keep evaluation under `post_hook_max_ms:1000`; fail fast if metrics worsen.

Confidence: 0.70 (ceiling: inference 0.70) – SOP aligned to Prompt Architect constraint extraction and Skill Forge structure-first delivery.

---

## VCL COMPLIANCE APPENDIX (Internal Reference)

[[HON:teineigo]] [[MOR:root:C-L-R]] [[COM:Clarity+Rubrik]] [[CLS:ge_skill]] [[EVD:-DI<gozlem>]] [[ASP:nesov.]] [[SPC:path:/skills/tooling/clarity-linter]]
[define|neutral] CLARITY_LINTER := bes boyutlu rubric + fix jenerasyonu; dogrulama zorunlu. [ground:SKILL.md] [conf:0.84] [state:confirmed]

[[HON:teineigo]] [[MOR:root:R-B-R]] [[COM:Rubrik+Skor]] [[CLS:ge_rule]] [[EVD:-DI<gozlem>]] [[ASP:nesov.]] [[SPC:axis:quality]]
[direct|emphatic] RUBRIC_DIM := {indirection, function_size, call_depth, duplication, explanation}; verdict {ACCEPT, REFINE, REJECT}. [ground:SKILL.md] [conf:0.86] [state:confirmed]

[[HON:teineigo]] [[MOR:root:E-P-S]] [[COM:Ceiling+Guard]] [[CLS:ge_rule]] [[EVD:-DI<politika>]] [[ASP:nesov.]] [[SPC:coord:EVD-CONF]]
[direct|emphatic] GUVEN_TAVANI := {cikarim:0.70, rapor:0.70, arastirma:0.85, gozlem:0.95, tanim:0.95}; ifade zorunlu. [ground:PA/SkillForge] [conf:0.90] [state:confirmed]

[commit|confident] <promise>CLARITY_LINTER_VERIX_COMPLIANT</promise> [ground:self-check] [conf:0.85] [state:confirmed]
