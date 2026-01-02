# Documentation Hub – Quick Reference (v3.2.0)

Purpose: plan, draft, and validate docs with Prompt Architect constraint ordering and Skill Forge delivery gates.

## Triggers
- README/API/inline/changelog/architecture doc updates.
- Route heavy generation to `when-documenting-code-use-doc-generator`.

## Fast Path
1. Confirm doc type, audience, scope, and constraints (style guide, terminology, links).
2. Collect sources: code paths, existing docs, decisions, API schemas.
3. Draft with progressive disclosure: overview → setup → workflows → references.
4. Validate accuracy vs code; run doc lint or link checks when available.
5. Deliver with risks, follow-ups, and confidence line (ceiling syntax).

## Inputs
- `doc_type`: README|API|inline|changelog|guide.
- `scope`: files/paths; `audience`: dev|ops|pm|user.
- Options: `style_guide`, `terminology`, `report_format`.

## Outputs
- Drafted/updated sections with file paths and diffs.
- Validation notes and outstanding questions.
- Memory keys used and confidence line: `Confidence: X.XX (ceiling: TYPE Y.YY)`.

## Validation Checklist
- Audience/intent confirmed; routing noted.
- Sources cited and verified.
- Style and terminology consistent; links valid.
- Confidence ceiling declared; memory tagged.

Confidence: 0.70 (ceiling: inference 0.70) – Quick reference rewritten to match Prompt Architect sequencing.
