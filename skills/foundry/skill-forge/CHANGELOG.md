---
name: skill-forge-changelog
description: Release history for Skill Forge updates
allowed-tools: [Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite]
model: claude-3-5-sonnet
x-version: 3.2.0
x-category: foundry/skill-forge
x-vcl-compliance: v3.1.1
---

### L1 Improvement
- Added English-first changelog summary with explicit triggers and confidence statement.
- Preserved legacy VCL changelog in the appendix for compliance history.

## STANDARD OPERATING PROCEDURE

### Purpose
Track Skill Forge release changes and surface the latest expectations for execution.

### Trigger Conditions
- When referencing historical updates or validating behavior against a specific version.
- Before applying SOP changes to ensure the current version is understood.

### Execution Phases
1. **Identify Version**
   - Note current release (v3.2.0) and prior ranges (v3.0.x–v2.x, v1.0.0).
2. **Review Highlights**
   - v3.2.0: Full VCL compliance, SKILL.md rewrite, self-application emphasis, mandatory adversarial+COV, updated templates, clarified MCP tagging.
   - v3.0.x–v2.x: Added recursive improvement, hooks, standardized structure, quality gates.
   - v1.0.0: Initial skill weaving SOP.
3. **Apply Guardrails**
   - Ensure current run aligns with latest requirements (adversarial+COV, structure templates, MCP tags).
   - Keep confidence statements within ceilings.

### Output Format
- Version referenced and highlights applied.
- Any backward-compatibility considerations or deviations.
- Confidence statement with ceiling syntax: `Confidence: X.XX (ceiling: TYPE Y.YY)` (ceilings: inference/report 0.70; research 0.85; observation/definition 0.95).

### Validation Checklist
- [ ] Correct version identified for the work.
- [ ] Latest guardrails applied.
- [ ] Deviations documented with rationale.
- [ ] Confidence statement included with explicit ceiling.

Confidence: 0.70 (ceiling: inference 0.70) - Changelog rewritten to English-first format with VCL history retained.

---

## VCL COMPLIANCE APPENDIX (Internal Reference)

<details>
<summary>Legacy content (verbatim)</summary>

[[HON:teineigo]] [[MOR:root:C-H-N]] [[COM:Degisim+Kaydi]] [[CLS:ge_changelog]] [[EVD:-DI<rapor>]] [[ASP:nesov.]] [[SPC:path:/skills/foundry/skill-forge/CHANGELOG-VCL]]
# Degisim Kaydi (Skill-Forge) – VCL

## v3.2.0 [[EVD:-DI<rapor>]] [[ASP:sov.]]
- Tam VCL uyumu; SKILL.md yeniden yazim; meta-beceri oz-uygulama vurgusu.  
- Adversarial test + COV zorunlu; yapisal sablonlar guncel.  
- MCP entegrasyon ve etiketleme aciklandi.

## v3.0.x–v2.x
- Recursive improvement ve hook rehberleri eklendi; dosya yapisi standartlasti; kalite kapilari tanimlandi.

## v1.0.0
- Temel beceri dokumasi SOP’u.

[[commit|confident]] <promise>CHANGELOG_SKILL_FORGE_VCL_COMPLIANT</promise> [ground:self-validation] [conf:0.88] [state:confirmed]

</details>
