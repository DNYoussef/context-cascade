# Template Extractor

Extract reusable templates (prompts, code, docs, configs) from existing artifacts with fidelity and clear provenance.

## Quick Start
1. Define scope (artifact type, success criteria, allowed edits).
2. Locate canonical sources; gather context (dependencies, environment, licenses).
3. Extract blocks with placeholders; annotate parameters and constraints.
4. Validate against source; add usage notes; record confidence ceiling.
5. Store templates and provenance under `skills/tooling/template-extractor/{project}/{timestamp}`.

## Inputs
- Target paths, template type, constraints, and required outputs.

## Outputs
- Template files/snippets, provenance (paths/lines), validation notes.
- Confidence line: `Confidence: X.XX (ceiling: TYPE Y.YY)`.

## Guardrails
- No hallucinated content—cite sources.
- Structure-first docs maintained (SKILL, README, improvement summary, references, scripts).
- Confidence ceilings enforced; flag uncertain sections.

Confidence: 0.70 (ceiling: inference 0.70) – README aligned to Prompt Architect clarity.
