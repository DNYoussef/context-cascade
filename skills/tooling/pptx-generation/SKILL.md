---
name: pptx-generation
description: Generate production-ready PowerPoint decks with structured prompts, design guardrails, and validation checkpoints.
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - Glob
  - Grep
  - Task
  - TodoWrite
model: claude-3-5-sonnet
x-version: 3.2.1
x-category: tooling
x-vcl-compliance: v3.1.1
x-cognitive-frames:
  - HON
  - MOR
  - COM
  - CLS
  - EVD
  - ASP
  - SPC
x-last-reflection: 2026-01-08T20:55:00Z
x-reflection-count: 1
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

## LEARNED PATTERNS

### High Confidence [conf:0.90]

- ALWAYS analyze existing document templates before generating new documents - capture fonts, colors, spacing, margins, and distinctive design elements [ground:user-correction:2026-01-08]
- When regenerating artifacts, ONLY replace the specific files with issues - do not bulk regenerate entire artifact directories [ground:user-explicit-rule:2026-01-08]
- If user rejects initial approach ("no that will be ugly"), immediately pivot to template-matching strategy rather than defending the approach [ground:user-correction:2026-01-08]

### Medium Confidence [conf:0.75]

- Prefer professional typography libraries (reportlab, LaTeX) over simple HTML-to-PDF converters (weasyprint) for portfolio-quality documents [ground:user-rejection-pattern:2026-01-08]
- Document generation workflow: Read template -> Extract style -> Generate matching output -> Verify content -> Deploy [ground:approval-pattern:2026-01-08]
- When system dependencies fail (GTK for weasyprint), fallback to pure Python alternatives (reportlab) rather than attempting system installs [ground:error-correction:2026-01-08]
- Content verification step using PyPDF2 or similar to confirm correctness before declaring task complete [ground:approval-pattern:2026-01-08]

### Low Confidence [conf:0.55]

- Build verification step should precede deployment for portfolio sites [ground:observation:2026-01-08]
- Git commit with descriptive message helps track artifact evolution [ground:observation:2026-01-08]
