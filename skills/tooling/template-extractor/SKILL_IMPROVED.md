# Template Extractor – Improvement Snapshot (v3.2.0)

- Converted to Prompt Architect constraint-first flow with Skill Forge guardrails (structure-first docs, confidence ceilings, memory tagging).
- Clarified triggers (reuse-focused extraction) and routing (net-new templates go to prompt-architect/skill-forge).
- Added fidelity safeguards: cite source paths/lines, flag uncertainties, and validate licensing.
- Standardized output format: templates + provenance + validation notes + `Confidence: X.XX (ceiling: TYPE Y.YY)`.
- Memory namespace: `skills/tooling/template-extractor/{project}/{timestamp}` for reuse patterns.
