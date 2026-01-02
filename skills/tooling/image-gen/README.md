# Image Generation

Generate images using SDXL Lightning (local), OpenAI DALL·E, Replicate, or custom providers. Follow Prompt Architect constraint ordering and Skill Forge guardrails.

## Quick Start
1. Capture constraints: use case, aspect/size, style, privacy/cost limits.
2. List providers: `python scripts/multi-model/image-gen/cli.py --list`.
3. Setup chosen provider (e.g., `--setup local` for SDXL) and run generation with prompt + output path.
4. Record provider rationale, settings, and confidence ceiling; store outputs in memory.

## Inputs
- Prompt (structured if available), provider preference, size/aspect, count, safety requirements.

## Outputs
- Image file paths, provider + parameters, quality/safety notes, and confidence line `Confidence: X.XX (ceiling: TYPE Y.YY)`.
- Memory key: `skills/tooling/image-gen/{project}/{timestamp}`.

## Guardrails
- Respect safety/licensing; avoid unsafe content.
- Provider selection must be evidence-based (availability, cost, privacy).
- Confidence ceilings enforced; rerun if quality mismatch.

Confidence: 0.70 (ceiling: inference 0.70) – README aligned to Prompt Architect clarity.
