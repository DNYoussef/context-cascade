# Improvement Summary – Template Extractor (v3.2.0)

## What Changed
- English-first SOP aligned to Prompt Architect + Skill Forge with explicit constraints and guardrails.
- Confidence ceilings and memory tagging added to every run.
- Validation tightened: provenance required, licensing noted, and placeholders documented.

## Why It Matters
- Reduces hallucination risk and improves reuse fidelity.
- Makes extracted templates portable with clear parameters and usage notes.
- Ensures repeatable delivery with structure-first documentation.

## Next Steps
- Add worked examples in `examples/` and lightweight tests for template linting.
- Expand scripts to auto-collect provenance metadata.

Confidence: 0.70 (ceiling: inference 0.70).
