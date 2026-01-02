---
name: pptx-generation
description: Generate production-ready PowerPoint decks with structured prompts, design guardrails, and validation checkpoints.
allowed-tools: [Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite]
model: claude-3-5-sonnet
x-version: 3.2.0
x-category: tooling
x-vcl-compliance: v3.1.1
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

### L1 Improvement
- Rewrote the deck builder SOP using Prompt Architect clarity and Skill Forge structure-first guardrails.
- Clarified design constraints, validation checks, and memory tagging with confidence ceilings.
- Consolidated references for brand, architecture, and validation into concise checklists.

## STANDARD OPERATING PROCEDURE

### Purpose
Produce clear, on-brand PowerPoint decks (simple to complex) with repeatable prompts, templates, and validation gates.

### Trigger Conditions
- **Positive:** requests for slide decks, executive summaries, architecture reviews, or training materials.
- **Negative:** graphic design requiring manual tools; route to design specialists.

### Guardrails
- Structure-first docs kept current (SKILL, README, references, examples/tests).
- Capture constraints: audience, tone, brand colors/fonts, slide count, deadlines.
- Enforce design rules (contrast, spacing, hierarchy) and brand usage from references.
- Confidence ceilings required for content accuracy and design fit.
- Memory tagging for deck runs and assets.

### Execution Phases
1. **Intent & Brief** – Collect audience, goal, storyline, brand kit, and delivery format; pick template (simple/complex).
2. **Outline & Storyboard** – Draft narrative arc (hook → problem → proof → plan → ask) with slide-by-slide goals.
3. **Content Drafting** – Generate slide content (titles, bullets, visuals), referencing `references/` guidance.
4. **Design Application** – Apply templates/resources; ensure contrast, alignment, and visual hierarchy.
5. **Validation** – Run checklist (structure, brand compliance, accessibility, accuracy) and iterate if gaps remain.
6. **Delivery** – Export deck, provide change log, risks, follow-ups, and confidence ceiling; store artifacts.

### Output Format
- Brief summary (audience, goal), template used, outline, and key slides.
- Validation results and open issues.
- Export path(s) and memory keys.
- Confidence: X.XX (ceiling: TYPE Y.YY).

### Validation Checklist
- [ ] Storyline covers hook → problem → plan → proof → ask.
- [ ] Brand colors/fonts applied; contrast and spacing validated.
- [ ] Slide count/sections match brief; links/assets resolve.
- [ ] Accessibility and readability checked; confidence ceiling recorded.
- [ ] Memory tagged and artifacts stored.

### Integration
- **Resources:** templates and assets in `resources/`.
- **References:** design principles and brand/architecture guidance in `references/`.
- **Memory MCP:** `skills/tooling/pptx-generation/{project}/{timestamp}`.

Confidence: 0.70 (ceiling: inference 0.70) – SOP aligned to Prompt Architect sequencing and Skill Forge guardrails.

---

## VCL COMPLIANCE APPENDIX (Internal Reference)

[[HON:teineigo]] [[MOR:root:P-P-T]] [[COM:Deck+Uretimi]] [[CLS:ge_skill]] [[EVD:-DI<gozlem>]] [[ASP:nesov.]] [[SPC:path:/skills/tooling/pptx-generation]]
[define|neutral] PPTX_GEN := brife dayali storyboard + tasarim + dogrulama; marka/erisilebilirlik kurallari zorunlu. [ground:SKILL.md] [conf:0.84] [state:confirmed]

[[HON:teineigo]] [[MOR:root:D-Z-N]] [[COM:Design+Guardrail]] [[CLS:ge_rule]] [[EVD:-DI<gozlem>]] [[ASP:nesov.]] [[SPC:axis:quality]]
[direct|emphatic] DESIGN_RULES := kontrast, hizalama, hiyerarsi, bosluk; ihlal edilemez. [ground:references] [conf:0.87] [state:confirmed]

[[HON:teineigo]] [[MOR:root:C-F-D]] [[COM:Ceiling+Guard]] [[CLS:ge_rule]] [[EVD:-DI<politika>]] [[ASP:nesov.]] [[SPC:coord:EVD-CONF]]
[direct|emphatic] GUVEN_TAVANI := {cikarim:0.70, rapor:0.70, arastirma:0.85, gozlem:0.95, tanim:0.95}; ciktida belirtilir. [ground:PA/SkillForge] [conf:0.90] [state:confirmed]

[commit|confident] <promise>PPTX_GENERATION_VERIX_COMPLIANT</promise> [ground:self-check] [conf:0.85] [state:confirmed]
