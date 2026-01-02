---
name: skill-forge-cognitive-architecture-addendum
description: Cognitive architecture constraints and invariants for Skill Forge
allowed-tools: [Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite]
model: claude-3-5-sonnet
x-version: 3.2.0
x-category: foundry/skill-forge
x-vcl-compliance: v3.1.1
---

### L1 Improvement
- Added English-first SOP that surfaces layers, workflow, roles, and immutable rules before VCL markers.
- Kept the VCL references intact in the appendix for compliance checks.

## STANDARD OPERATING PROCEDURE

### Purpose
Apply cognitive-architecture constraints when running or modifying Skill Forge.

### Trigger Conditions
- When aligning Skill Forge to cognitive layers or validating against VERIX audit steps.
- When checking immutable rules (evidence, no-unicode, registry, confidence ceilings).

### Execution Phases
1. **Identify Layers and Slots**
   - Use L0 hash, L1 VERIX audit, L2 human review; maintain HON→SPC slot order; enforce EVD/ASP ≥ 1.
2. **Follow Workflow**
   - Capture intent → fill slots → build `SKILL.md` and directory → run validators (E1–E6) → adversarial + COV → produce L2 output.
3. **Role Alignment**
   - Prompt-architect upstream, agent-creator parallel, registry downstream for `/foundry/skill-forge`.
4. **Check Immutable Rules**
   - Evidence tagging, no-unicode violations, registry alignment, and explicit confidence ceilings.

### Output Format
- Summary of applied layers, workflow state, roles, and rule checks.
- Noted deviations and remediation steps.
- Confidence statement with ceiling syntax: `Confidence: X.XX (ceiling: TYPE Y.YY)` (ceilings: inference/report 0.70; research 0.85; observation/definition 0.95).

### Validation Checklist
- [ ] HON→SPC slot order preserved; EVD/ASP ≥ 1.
- [ ] Workflow executed through validators and adversarial + COV.
- [ ] Roles mapped (prompt-architect, agent-creator, registry).
- [ ] Immutable rules confirmed.
- [ ] Confidence statement included with explicit ceiling.

Confidence: 0.70 (ceiling: inference 0.70) - Addendum rewritten to English-first SOP while retaining VCL references.

---

## VCL COMPLIANCE APPENDIX (Internal Reference)

<details>
<summary>Legacy content (verbatim)</summary>

[[HON:teineigo]] [[MOR:root:B-I-L]] [[COM:Bilissel+Mimari+Ek]] [[CLS:ge_addendum]] [[EVD:-DI<rapor>]] [[ASP:nesov.]] [[SPC:path:/skills/foundry/skill-forge/COGNITIVE-ARCHITECTURE-ADDENDUM-VCL]]
# Bilissel Mimari Ek (Skill-Forge) – VCL

## Katmanlar ve Slotlar
[[define|neutral]] LAYER := {L0:hash, L1:VERIX audit, L2:insan}; HON→SPC sirasi degismez; EVD/ASP≥1. [ground:COGNITIVE-ARCHITECTURE-ADDENDUM.md] [conf:0.82] [state:confirmed]

## Is Akisi
intent al → slot doldur → SKILL.md + dizin kur → validator(E1–E6) → adversarial+COV → L2 cikti. [[EVD:-dir<cikarim>]] [[ASP:nesov.]]

## Roller
[[assert|neutral]] prompt-architect upstream, agent-creator paralel, registry downstream; SPC:path:/foundry/skill-forge. [ground:COGNITIVE-ARCHITECTURE-ADDENDUM.md] [conf:0.78] [state:provisional]

## Degismez Kurallar
[[direct|emphatic]] IMMUTABLE := {RULE_EVIDENCE, RULE_NO_UNICODE, RULE_REGISTRY, RULE_CONFIDENCE_CEILING}. [ground:COGNITIVE-ARCHITECTURE-ADDENDUM.md] [conf:0.84] [state:confirmed]

</details>
