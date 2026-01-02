# Doc Generator

Generate README/API/inline documentation from code with evidence and validation.

## Quick Start
1. Confirm doc type, audience, scope, and source files.
2. Gather constraints/terminology from code and existing docs.
3. Run generation (API/inline/README scripts) and draft content.
4. Validate against source, check links/examples, and note gaps.
5. Store outputs under `skills/tooling/when-documenting-code-use-doc-generator/{project}/{timestamp}` (mirror when nested) with confidence ceiling.

## Outputs
- Updated docs with paths, validation notes, and `Confidence: X.XX (ceiling: TYPE Y.YY)`.

## Guardrails
- Cite sources; avoid hallucinated APIs.
- Confidence ceilings enforced; flag uncertainties.
- Structure-first docs maintained; no secrets in output.

Confidence: 0.70 (ceiling: inference 0.70).
