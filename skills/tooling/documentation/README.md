# Documentation Hub

Plan, draft, and validate documentation with Prompt Architect constraint ordering and Skill Forge delivery guardrails.

## Quick Start
1. Identify doc type (README, API, inline, changelog, guide) and audience.
2. Collect sources (code paths, decisions, style guides) and confirm terminology.
3. Draft with progressive disclosure; route heavy generation to the doc-generator subskill.
4. Validate accuracy, links, and style; state confidence ceiling and store artifacts.

## Inputs
- `doc_type`, `scope` (paths), `audience`, optional `style_guide` and `terminology`.

## Outputs
- Drafted/updated sections with file paths and diffs.
- Validation notes, risks, and follow-ups.
- Confidence line: `Confidence: X.XX (ceiling: TYPE Y.YY)` and memory namespace used.

## Guardrails
- Structure-first docs maintained (SKILL, README, quick reference, examples/tests placeholders).
- No hallucinated APIs—cite observed sources.
- Memory tagging: `skills/tooling/documentation/{project}/{timestamp}` with WHO/WHY/PROJECT/WHEN.

Confidence: 0.70 (ceiling: inference 0.70) – README aligned to Prompt Architect SOP.
