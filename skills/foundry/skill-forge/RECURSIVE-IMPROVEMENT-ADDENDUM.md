---
name: skill-forge-recursive-improvement-addendum
description: Recursive improvement loop and guardrails for Skill Forge
allowed-tools: [Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite]
model: claude-3-5-sonnet
x-version: 3.2.0
x-category: foundry/skill-forge
x-vcl-compliance: v3.1.1
---

### L1 Improvement
- Introduced an English-first SOP describing the recursive loop, controls, and memory tagging.
- Preserved VCL notation in the appendix for compliance and traceability.

## STANDARD OPERATING PROCEDURE

### Purpose
Maintain the Skill Forge recursive improvement loop with required controls and memory practices.

### Trigger Conditions
- When iterating on Skill Forge outputs or running dogfooding loops.
- Before final delivery to ensure adversarial validation and structure checks are complete.

### Execution Phases
1. **Run the Loop**
   - Sequence: design → weave/build → test → verify → observe → refine.
   - Keep ASP in non-terminal mode; record EVD/ASP each iteration.
2. **Apply Controls**
   - Adversarial testing required with COV measurement.
   - Structural validation: ensure `examples/`, `tests/`, `resources/`, `references/` exist.
   - Watch anti-patterns: skipping adversarial tests, missing structure, generic coordination, MCP neglect.
3. **Persist Memory**
   - Use MCP namespace `skills/foundry/skill-forge/{project}/{timestamp}`.
   - Tag WHO=`skill-forge-{session}` for traceability.

### Output Format
- Iteration summary with actions taken and findings.
- Validation results and anti-pattern checks.
- Memory keys used and status.
- Confidence statement with ceiling syntax: `Confidence: X.XX (ceiling: TYPE Y.YY)` (ceilings: inference/report 0.70; research 0.85; observation/definition 0.95).

### Validation Checklist
- [ ] Loop executed with evidence recorded.
- [ ] Adversarial + COV completed.
- [ ] Required structure validated.
- [ ] Anti-patterns checked and mitigated.
- [ ] MCP namespace tagged; confidence statement included.

Confidence: 0.70 (ceiling: inference 0.70) - Recursive improvement addendum rewritten to English-first SOP with legacy details retained.

---

## VCL COMPLIANCE APPENDIX (Internal Reference)

<details>
<summary>Legacy content (verbatim)</summary>

[[HON:teineigo]] [[MOR:root:R-K-R]] [[COM:Ozyinelemeli+Iyilestirme+Ek]] [[CLS:ge_addendum]] [[EVD:-DI<rapor>]] [[ASP:nesov.]] [[SPC:path:/skills/foundry/skill-forge/RECURSIVE-IMPROVEMENT-ADDENDUM-VCL]]
# Ozyinelemeli Iyilestirme Ek (Skill-Forge) – VCL

## Dongu
[[define|neutral]] LOOP := {tasarla→dok→test_et→dogrula→gozle→refine}. ASP:nesov. devam; her iterasyonda EVD/ASP kaydı. [ground:RECURSIVE-IMPROVEMENT-ADDENDUM.md] [conf:0.82] [state:confirmed]

## Kontroller
[[HON:teineigo]] [[MOR:root:K-N-T]] [[COM:Kontrol+Set]] [[CLS:ge_guardrail]] [[EVD:-DI<policy>]] [[ASP:nesov.]]
- Adversarial test zorunlu; COV ölç.  
- Yapı dogrulama: examples/tests/resources/references var.  
- Anti-kalip: dusmanca_test_atlama, eksik_yapi, genel_koordinasyon, MCP_ihmal.

## Hafiza
[[assert|neutral]] MCP namespace: skills/foundry/skill-forge/{proje}/{timestamp}; etiket WHO=skill-forge-{session}. [ground:RECURSIVE-IMPROVEMENT-ADDENDUM.md] [conf:0.78] [state:provisional]

</details>
