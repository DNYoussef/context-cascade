# PPTX Generation

Build on-brand decks with structured prompts and validation gates.

## Quick Start
1. Gather brief: audience, goal, storyline, brand kit, slide count, due date.
2. Choose template from `resources/`; create outline (hook → problem → plan → proof → ask).
3. Draft slides using references for design/brand/architecture.
4. Validate against checklist (structure, brand, accessibility, links) and export.
5. Store artifacts under `skills/tooling/pptx-generation/{project}/{timestamp}` with confidence ceiling.

## Inputs
- Brief (audience, goal, tone, brand colors/fonts), desired template, slide count, export format.

## Outputs
- Deck path(s), outline, validation notes, risks, and confidence line `Confidence: X.XX (ceiling: TYPE Y.YY)`.

## Guardrails
- Structure-first docs maintained; use references for design principles and brand usage.
- Apply Prompt Architect constraint ordering; avoid hallucinated data—cite sources.
- Enforce accessibility (contrast, font size) and brand integrity.

Confidence: 0.70 (ceiling: inference 0.70) – README aligned to Skill Forge guardrails.
