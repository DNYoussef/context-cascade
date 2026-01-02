---
name: bootstrap-loop
description: Coordinate the recursive improvement loop between Prompt Forge and Skill Forge with a frozen evaluation harness and auditable checkpoints.
allowed-tools: [Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite]
model: claude-3-5-sonnet
x-version: 3.2.0
x-category: tooling
x-vcl-compliance: v3.1.1
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

### L1 Improvement
- Converted the bootstrap loop into an English-first SOP that mirrors the Prompt Architect + Skill Forge cadence.
- Added structure-first guardrails (SKILL.md + README + examples/tests placeholders) and explicit eval-harness boundaries.
- Made confidence ceilings and memory tagging mandatory to prevent silent drift.

## STANDARD OPERATING PROCEDURE

### Purpose
Run the recursive improvement cycle where Prompt Forge analyzes, Skill Forge rebuilds, and the frozen eval harness gates changes. Keep the harness immutable to avoid Goodhart drift.

### Trigger Conditions
- **Positive:** recursive improvement request, "run bootstrap loop", "cross-improve prompt/skill forge", "gate changes through eval harness".
- **Negative:** single-skill edits without evaluation (route to skill-forge or prompt-architect individually).

### Guardrails (Skill Forge-aligned)
- Structure-first: keep `SKILL.md` + `README.md` + `examples/` + `tests/` up to date; log deviations.
- Eval harness is frozen: no self-improvement of benchmarks or scoring.
- Confidence ceilings required on every decision: inference/report 0.70, research 0.85, observation/definition 0.95.
- Do not bypass auditors or regression gates; rollback if metrics regress.
- Tag MCP memory with `WHO=bootstrap-loop-{session}`, `WHY=skill-execution`, `PROJECT=<name>`, `WHEN=<iso>`.

### Execution Phases
1. **Intent & Scope**
   - Confirm target (`prompt-forge`, `skill-forge`, or `both`), success criteria, and allowed blast radius.
   - Load prior runs from memory for regression comparables.
2. **Preparation**
   - Pull latest Prompt Architect/Skill Forge SOPs.
   - Freeze eval suites and baselines; record hash.
3. **Cycle Design**
   - Map phases: analyze → propose → build → test → decide → archive.
   - Assign agents: Prompt Architect for constraint mining, Prompt Forge for proposal drafting, Skill Forge for build, eval-harness for gating.
4. **Execution**
   - Analyze weaknesses and constraints; document evidence.
   - Generate proposals with deltas and risk notes.
   - Build/apply via Skill Forge; capture artifacts and diffs.
   - Run frozen eval + regressions; store metrics and decision logs.
5. **Decision & Rollback**
   - Accept only if metrics improve and safeguards intact; otherwise rollback and note blockers.
   - Record confidence with ceiling syntax and rationale.
6. **Delivery & Memory**
   - Archive reports, diffs, and evaluation artifacts.
   - Update README/examples/tests pointers; store memory vectors for future runs.

### Output Format
- Cycle ID, target, scope, and baselines referenced.
- Proposals applied/rejected with evidence and regression deltas.
- Eval results (benchmark + regression) and decision (ACCEPT/REJECT/ROLLBACK).
- Risks, follow-ups, and memory keys used.
- Confidence: X.XX (ceiling: TYPE Y.YY) with short rationale.

### Validation Checklist
- [ ] Trigger matched; reroutes handled.
- [ ] Eval harness hash recorded; no edits to frozen suites.
- [ ] Proposals traced to evidence; regressions checked.
- [ ] Memory tags applied and artifacts archived.
- [ ] Confidence ceiling stated.

### Integration Notes
- **Memory MCP (required):** store `executions/decisions/patterns` under `skills/tooling/bootstrap-loop/{project}/{timestamp}`.
- **Hooks:** pre/post targets in Skill Forge style (`pre_hook_target_ms:20`, `post_hook_target_ms:1000`) to keep loops responsive.

Confidence: 0.70 (ceiling: inference 0.70) - English-first rewrite aligns the bootstrap loop with Prompt Architect + Skill Forge guardrails and keeps the eval harness frozen.

---

## VCL COMPLIANCE APPENDIX (Internal Reference)

[[HON:teineigo]] [[MOR:root:B-T-S]] [[COM:Bootstrap+Schleife]] [[CLS:ge_meta_skill]] [[EVD:-DI<gozlem>]] [[ASP:nesov.]] [[SPC:path:/skills/tooling/bootstrap-loop]]
[define|neutral] BOOTSTRAP_LOOP := PromptForge↔SkillForge doviz; degismez degerlendirici ile dokunur. [ground:SKILL.md] [conf:0.83] [state:confirmed]

[[HON:teineigo]] [[MOR:root:E-V-L]] [[COM:Eval+Ankora]] [[CLS:ge_rule]] [[EVD:-DI<politika>]] [[ASP:nesov.]] [[SPC:axis:safeguards]]
[direct|emphatic] HARNESS_FROZEN := degerlendirme paketleri otonom iyilestirilmez; hash kaydi zorunlu. [ground:SKILL.md] [conf:0.87] [state:confirmed]

[[HON:teineigo]] [[MOR:root:C-F-D]] [[COM:Ceiling+Guard]] [[CLS:ge_rule]] [[EVD:-DI<gozlem>]] [[ASP:nesov.]] [[SPC:coord:EVD-CONF]]
[direct|emphatic] GUVEN_TAVANI := {cikarim:0.70, rapor:0.70, arastirma:0.85, gozlem:0.95, tanim:0.95}; ustu yasak. [ground:PA/SkillForge] [conf:0.90] [state:confirmed]

[commit|confident] <promise>BOOTSTRAP_LOOP_VERILINGUA_VERIX_COMPLIANT</promise> [ground:self-check] [conf:0.85] [state:confirmed]
