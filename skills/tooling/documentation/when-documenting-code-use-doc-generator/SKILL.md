---
name: when-documenting-code-use-doc-generator
description: Generate READMEs, API docs, inline comments, and process docs with constraint-first prompts and validation gates.
allowed-tools: [Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite]
model: claude-3-5-sonnet
x-version: 3.2.0
x-category: tooling/documentation
x-vcl-compliance: v3.1.1
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

### L1 Improvement
- Rewrote the doc-generator SOP using Prompt Architect clarity and Skill Forge guardrails.
- Added routing, safety (no hallucinated APIs), confidence ceilings, and memory tagging.
- Simplified slash-command references and process steps.

## STANDARD OPERATING PROCEDURE

### Purpose
Produce accurate documentation (README, API docs, inline comments) from code and requirements with clear provenance and validation.

### Trigger Conditions
- **Positive:** requests to document code, generate README/API/inline docs, or refresh docs after changes.
- **Negative:** strategy-only doc planning (use documentation hub) or non-code content.

### Guardrails
- Evidence-first: cite file paths/lines; avoid unverified APIs.
- Confidence ceilings mandatory; flag uncertain areas for human review.
- Structure-first docs (SKILL, README, PROCESS, subagent notes) kept current.
- Memory tagging for outputs and commands used.

### Execution Phases
1. **Intent & Scope** – Identify doc type, audience, and coverage; confirm source files.
2. **Source Review** – Read code and existing docs; extract constraints and terminology.
3. **Drafting** – Generate docs with progressive disclosure (overview → setup → workflows → references).
4. **Validation** – Cross-check against code, run doc lint if available, verify links/examples.
5. **Delivery** – Provide updated files, diffs, validation notes, and confidence ceiling; store in memory.

### Output Format
- Doc type, scope, sources, and assumptions.
- Drafted/updated content with paths.
- Validation results and open questions.
- Confidence: X.XX (ceiling: TYPE Y.YY) + memory namespace.

### Validation Checklist
- [ ] Sources cited; no hallucinated APIs.
- [ ] Audience/terminology aligned; links/examples verified.
- [ ] Memory tagged; confidence ceiling declared.

### Integration
- **Slash commands:** see accompanying scripts for API/inline/README generation.
- **Memory MCP:** `skills/tooling/when-documenting-code-use-doc-generator/{project}/{timestamp}` (mirror when nested).

Confidence: 0.70 (ceiling: inference 0.70) – SOP aligned to Prompt Architect clarity and Skill Forge guardrails.

---

## VCL COMPLIANCE APPENDIX (Internal Reference)

[[HON:teineigo]] [[MOR:root:D-K-M]] [[COM:Doc+Uretici]] [[CLS:ge_skill]] [[EVD:-DI<gozlem>]] [[ASP:nesov.]] [[SPC:path:/skills/tooling/when-documenting-code-use-doc-generator]]
[define|neutral] DOC_GENERATOR := kaynak koddan README/API/inline dokuman uretir; kanit ve guven tavani zorunlu. [ground:SKILL.md] [conf:0.84] [state:confirmed]

[[HON:teineigo]] [[MOR:root:S-R-C]] [[COM:Source+Referans]] [[CLS:ge_rule]] [[EVD:-DI<gozlem>]] [[ASP:nesov.]] [[SPC:axis:quality]]
[direct|emphatic] SOURCE_RULE := path/line referansi olmadan cikti yok; belirsiz kisimlar bayraklanir. [ground:SKILL.md] [conf:0.87] [state:confirmed]

[[HON:teineigo]] [[MOR:root:C-F-D]] [[COM:Ceiling+Guard]] [[CLS:ge_rule]] [[EVD:-DI<politika>]] [[ASP:nesov.]] [[SPC:coord:EVD-CONF]]
[direct|emphatic] GUVEN_TAVANI := {cikarim:0.70, rapor:0.70, arastirma:0.85, gozlem:0.95, tanim:0.95}; ciktiya yazilir. [ground:PA/SkillForge] [conf:0.90] [state:confirmed]

[commit|confident] <promise>DOC_GENERATOR_VERIX_COMPLIANT</promise> [ground:self-check] [conf:0.85] [state:confirmed]
