---
name: image-gen
description: Generate images via local SDXL Lightning, OpenAI DALL·E, Replicate, or custom providers with structured prompts and safety checks.
allowed-tools: [Bash, Read, Write, Task, TodoWrite, Glob, Grep]
model: claude-3-5-sonnet
x-version: 3.2.0
x-category: tooling
x-vcl-compliance: v3.1.1
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

### L1 Improvement
- Recast the image generation SOP using Prompt Architect clarity and Skill Forge structure-first guardrails.
- Added provider selection rules, confidence ceilings, and memory tagging.
- Clarified integration with visual-art-composition and safety constraints.

## STANDARD OPERATING PROCEDURE

### Purpose
Select the best image provider (local or API) for the request, generate assets with structured prompts, and deliver reproducible outputs with safety and cost visibility.

### Trigger Conditions
- **Positive:** requests for illustrations, banners, UI mockups, diagrams, or concept art.
- **Negative:** vector/icon design requiring manual tools; route to design specialists.

### Guardrails
- Structure-first docs maintained; scripts/resources referenced.
- Provider selection uses evidence: availability, cost, latency, privacy.
- Respect safety filters and license terms; avoid unsafe content.
- Confidence ceilings declared for prompt-to-image fit; cite provider used.
- Memory tagging for prompts/results to enable reuse.

### Execution Phases
1. **Intent & Constraints** – Capture use case, size/aspect, style, privacy/cost limits. Pull structured prompt from visual-art-composition if available.
2. **Provider Selection** – Choose SDXL (local, private), DALL·E (quality), Replicate (cost), or custom; log rationale.
3. **Setup/Validation** – Ensure provider credentials/models ready; note latency/VRAM needs.
4. **Generation** – Run prompt with seed/size/options; generate 1–N variants.
5. **Review & Safety** – Check for content/safety violations and quality fit; rerun if needed.
6. **Delivery** – Save paths, provider, settings, and confidence line; store in memory.

### Output Format
- Provider + rationale, prompt used, parameters (size, seed, steps), and file paths.
- Quality/safety notes and follow-ups.
- Confidence: X.XX (ceiling: TYPE Y.YY) with source of certainty (observation vs inference).

### Validation Checklist
- [ ] Constraints captured; provider rationale logged.
- [ ] Credentials/models verified; no unsafe content.
- [ ] Outputs saved with deterministic params when possible.
- [ ] Memory tagged; confidence ceiling declared.

### Integration
- **Pipeline:** combine with `visual-art-composition` for structured prompts.
- **Scripts:** `scripts/multi-model/image-gen/cli.py` with `--list`, `--setup <provider>`, and generation commands.
- **Memory MCP:** `skills/tooling/image-gen/{project}/{timestamp}` for prompts/results.

Confidence: 0.70 (ceiling: inference 0.70) – SOP aligned to Prompt Architect clarity and Skill Forge delivery.

---

## VCL COMPLIANCE APPENDIX (Internal Reference)

[[HON:teineigo]] [[MOR:root:I-M-G]] [[COM:Gorsel+Uretim]] [[CLS:ge_skill]] [[EVD:-DI<gozlem>]] [[ASP:nesov.]] [[SPC:path:/skills/tooling/image-gen]]
[define|neutral] IMAGE_GEN := saglayici-secim + prompt-uygulama + guvenlik kontrolu; SDXL/DALL·E/Replicate/custom destekli. [ground:SKILL.md] [conf:0.84] [state:confirmed]

[[HON:teineigo]] [[MOR:root:P-R-V]] [[COM:Provider+Secim]] [[CLS:ge_rule]] [[EVD:-DI<gozlem>]] [[ASP:nesov.]] [[SPC:axis:routing]]
[direct|emphatic] PROVIDER_RULE := gizlilik->local; GPU yok->API; maliyet kritik->Replicate; kalite yuksek->DALL·E veya SDXL. [ground:SKILL.md] [conf:0.87] [state:confirmed]

[[HON:teineigo]] [[MOR:root:C-F-D]] [[COM:Ceiling+Guard]] [[CLS:ge_rule]] [[EVD:-DI<politika>]] [[ASP:nesov.]] [[SPC:coord:EVD-CONF]]
[direct|emphatic] GUVEN_TAVANI := {cikarim:0.70, rapor:0.70, arastirma:0.85, gozlem:0.95, tanim:0.95}; ciktida belirtilir. [ground:PA/SkillForge] [conf:0.90] [state:confirmed]

[commit|confident] <promise>IMAGE_GEN_VERIX_COMPLIANT</promise> [ground:self-check] [conf:0.85] [state:confirmed]
