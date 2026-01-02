---
name: template-extractor
description: Extract reusable templates and patterns from source artifacts with structured prompts and validation checkpoints.
allowed-tools: [Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite]
model: claude-3-5-sonnet
x-version: 3.2.0
x-category: tooling
x-vcl-compliance: v3.1.1
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

### L1 Improvement
- Rebuilt the extractor SOP using Prompt Architect constraint ordering and Skill Forge structure-first guardrails.
- Added clear triggers, input/output contracts, and confidence ceilings with memory tagging.
- Clarified validation for fidelity (no hallucinations) and reusability.

## STANDARD OPERATING PROCEDURE

### Purpose
Identify, isolate, and package reusable templates (prompts, code snippets, docs, configs) from existing artifacts while preserving fidelity and context.

### Trigger Conditions
- **Positive:** requests to extract reusable templates/patterns, generate starter kits, or refactor repetitive content.
- **Negative:** net-new template design (route to prompt-architect/skill-forge) or full refactors without reuse focus.

### Guardrails
- Structure-first docs maintained (SKILL, README, improvement summary, references, scripts).
- Evidence-first extraction: cite source paths and lines; avoid hallucinated additions.
- Confidence ceilings mandatory; flag uncertain sections for review.
- Memory tagging for extracted templates and provenance.

### Execution Phases
1. **Intent & Scope** – Define artifact type (prompt/code/doc/config), success criteria, and allowed modifications.
2. **Source Collection** – Locate canonical files; gather context (dependencies, environment, licenses).
3. **Extraction** – Isolate template blocks with placeholders; annotate variables and constraints.
4. **Normalization** – Standardize structure (front matter, parameters, steps), add usage notes.
5. **Validation** – Verify fidelity against source; run lint/tests if applicable; check licensing.
6. **Delivery** – Provide template files, provenance, usage guidance, and confidence line.

### Output Format
- Template(s) with placeholders/parameters and usage instructions.
- Provenance (paths/lines), constraints, and compatibility notes.
- Validation results and open questions.
- Confidence: X.XX (ceiling: TYPE Y.YY) and memory keys used.

### Validation Checklist
- [ ] Source paths cited; no hallucinated content.
- [ ] Placeholders/parameters documented with defaults.
- [ ] Licensing/compatibility noted.
- [ ] Memory tagged and artifacts stored.
- [ ] Confidence ceiling declared.

### Integration
- **Scripts:** automation helpers in `scripts/`.
- **Memory MCP:** `skills/tooling/template-extractor/{project}/{timestamp}` for extracted templates and provenance.
- **Hooks:** follow Skill Forge latency bounds; integrate with validation tools as needed.

Confidence: 0.70 (ceiling: inference 0.70) – SOP aligned to Prompt Architect clarity and Skill Forge guardrails.

---

## VCL COMPLIANCE APPENDIX (Internal Reference)

[[HON:teineigo]] [[MOR:root:T-M-P]] [[COM:Sablon+Cikarim]] [[CLS:ge_skill]] [[EVD:-DI<gozlem>]] [[ASP:nesov.]] [[SPC:path:/skills/tooling/template-extractor]]
[define|neutral] TEMPLATE_EXTRACTOR := kaynak dogrulamalariyla tekrar kullanilabilir sablonlar cikartir; sahte icerik yasak. [ground:SKILL.md] [conf:0.84] [state:confirmed]

[[HON:teineigo]] [[MOR:root:F-D-L]] [[COM:Fidelity+Guard]] [[CLS:ge_rule]] [[EVD:-DI<gozlem>]] [[ASP:nesov.]] [[SPC:axis:quality]]
[direct|emphatic] FIDELITY_RULE := kaynaga referans (path+line) olmadan sablon yok; belirsiz kisimlar bayraklanir. [ground:SKILL.md] [conf:0.87] [state:confirmed]

[[HON:teineigo]] [[MOR:root:C-F-D]] [[COM:Ceiling+Guard]] [[CLS:ge_rule]] [[EVD:-DI<politika>]] [[ASP:nesov.]] [[SPC:coord:EVD-CONF]]
[direct|emphatic] GUVEN_TAVANI := {cikarim:0.70, rapor:0.70, arastirma:0.85, gozlem:0.95, tanim:0.95}; beyan zorunlu. [ground:PA/SkillForge] [conf:0.90] [state:confirmed]

[commit|confident] <promise>TEMPLATE_EXTRACTOR_VERIX_COMPLIANT</promise> [ground:self-check] [conf:0.85] [state:confirmed]
