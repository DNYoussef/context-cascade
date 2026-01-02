---
name: documentation
description: Plan, generate, and validate documentation using Prompt Architect clarity patterns and routing to doc-generator subskills.
allowed-tools: [Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite]
model: claude-3-5-sonnet
x-version: 3.2.0
x-category: tooling
x-vcl-compliance: v3.1.1
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

### L1 Improvement
- Converted the documentation hub to an English-first SOP with structure-first guardrails and explicit routing to doc-generator.
- Added constraint extraction (Prompt Architect) and validation hooks (Skill Forge) with confidence ceilings.
- Clarified outputs: user-facing docs, API references, and inline comment updates.

## STANDARD OPERATING PROCEDURE

### Purpose
Coordinate documentation requests—planning, drafting, and validation—while delegating inline/README/API generation to the `when-documenting-code-use-doc-generator` subskill when appropriate.

### Trigger Conditions
- **Positive:** new/updated README, API docs, inline comments, changelogs, or architecture notes.
- **Negative:** code-only fixes without doc impact; route to implementation skills first.

### Guardrails
- Structure-first docs: `SKILL.md`, `README.md`, `QUICK-REFERENCE.md`, examples/tests placeholders.
- Use Prompt Architect constraint extraction (audience, scope, domain terminology, success criteria).
- Enforce confidence ceilings and cite sources/observations; avoid hallucinated APIs.
- Memory tagging for doc runs; keep versioned outputs.

### Execution Phases
1. **Intent & Audience** – Identify doc type (README/API/inline/guide), target audience, and scope; route to subskill if generation-heavy.
2. **Source Collection** – Gather code references, existing docs, decisions, and style guides.
3. **Drafting** – Produce structured doc with headings, task flows, and examples; maintain progressive disclosure.
4. **Validation** – Check accuracy against code, run doc lints if available, and ensure consistency with terminology.
5. **Delivery** – Summarize changes, open risks, and follow-ups; include confidence with ceiling syntax and memory keys.

### Output Format
- Doc type and scope, key sources, and assumptions.
- Drafted content or updated sections with diffs/paths.
- Validation notes (accuracy checks, style compliance).
- Confidence: X.XX (ceiling: TYPE Y.YY) and memory namespace used.

### Validation Checklist
- [ ] Audience and intent confirmed; routing noted.
- [ ] Sources cited and verified against code.
- [ ] Style/terminology aligned; links and paths validated.
- [ ] Memory tagged and artifacts stored.
- [ ] Confidence ceiling declared.

### Integration
- **Subskill:** `when-documenting-code-use-doc-generator` for detailed generation flows.
- **Memory MCP:** `skills/tooling/documentation/{project}/{timestamp}` for drafts and approvals.
- **Hooks:** Skill Forge latency bounds respected for doc generation and review.

Confidence: 0.70 (ceiling: inference 0.70) – SOP aligned to Prompt Architect constraint-first drafting and Skill Forge validation gates.

---

## VCL COMPLIANCE APPENDIX (Internal Reference)

[[HON:teineigo]] [[MOR:root:D-K-M]] [[COM:Dokuman+Merkezi]] [[CLS:ge_skill]] [[EVD:-DI<gozlem>]] [[ASP:nesov.]] [[SPC:path:/skills/tooling/documentation]]
[define|neutral] DOC_HUB := README/API/inline ciktilar icin yonetim; agir uretim doc-generator'a delege edilir. [ground:SKILL.md] [conf:0.84] [state:confirmed]

[[HON:teineigo]] [[MOR:root:R-O-T]] [[COM:Route+Generator]] [[CLS:ge_rule]] [[EVD:-DI<gozlem>]] [[ASP:nesov.]] [[SPC:axis:routing]]
[direct|emphatic] ROUTE_DOC := agir uretim ve slash-komutlar doc-generator alt-becerisine aktarilir; hub planlama+dogrulama yapar. [ground:SKILL.md] [conf:0.85] [state:confirmed]

[[HON:teineigo]] [[MOR:root:C-F-D]] [[COM:Ceiling+Guard]] [[CLS:ge_rule]] [[EVD:-DI<politika>]] [[ASP:nesov.]] [[SPC:coord:EVD-CONF]]
[direct|emphatic] GUVEN_TAVANI := {cikarim:0.70, rapor:0.70, arastirma:0.85, gozlem:0.95, tanim:0.95}; beyan zorunlu. [ground:PA/SkillForge] [conf:0.90] [state:confirmed]

[commit|confident] <promise>DOCUMENTATION_VERIX_COMPLIANT</promise> [ground:self-check] [conf:0.85] [state:confirmed]
