---
name: skill-forge-expertise-addendum
description: Expertise loading rules and domain application guidance for Skill Forge
allowed-tools: [Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite]
model: claude-3-5-sonnet
x-version: 3.2.0
x-category: foundry/skill-forge
x-vcl-compliance: v3.1.1
---

### L1 Improvement
- Converted the expertise addendum to English-first SOP while retaining VCL details in the appendix.
- Clarified loading, application, and rule enforcement steps with explicit confidence ceilings.

## STANDARD OPERATING PROCEDURE

### Purpose
Define how to load and apply domain expertise packages before delivering a Skill Forge artifact.

### Trigger Conditions
- When a skill requires domain-specific knowledge, tests, or performance targets.
- Before distribution to ensure expertise packages are loaded and recorded.

### Execution Phases
1. **Load Expertise**
   - Bind domain documents, codebases, and policy sources.
   - Use `Task()` to populate memory; record SPC:path references.
2. **Apply Expertise**
   - Pull required expertise packages during skill setup.
   - Add evidence markers (`-mis` for research, `-DI` for observation).
   - Ensure domain-specific tests and performance goals are included.
3. **Enforce Rule**
   - Do not ship the skill without expertise loaded.
   - Keep confidence ≤ ceiling; output is L2 English; ensure registry entry is updated.

### Output Format
- Loaded sources and memory keys.
- Domain tests and performance targets added.
- Registry update status and any gaps.
- Confidence statement with ceiling syntax: `Confidence: X.XX (ceiling: TYPE Y.YY)` (ceilings: inference/report 0.70; research 0.85; observation/definition 0.95).

### Validation Checklist
- [ ] Domain sources bound and logged.
- [ ] Evidence markers applied.
- [ ] Domain tests/performance goals included.
- [ ] Registry updated and confidence within ceiling.
- [ ] Confidence statement included with explicit ceiling.

Confidence: 0.70 (ceiling: inference 0.70) - Expertise addendum rewritten to English-first SOP with all legacy guidance preserved in the appendix.

---

## VCL COMPLIANCE APPENDIX (Internal Reference)

<details>
<summary>Legacy content (verbatim)</summary>

[[HON:teineigo]] [[MOR:root:U-Z-M]] [[COM:Uzmanlik+Ek]] [[CLS:ge_addendum]] [[EVD:-DI<rapor>]] [[ASP:nesov.]] [[SPC:path:/skills/foundry/skill-forge/EXPERTISE-ADDENDUM-VCL]]
# Uzmanlik Ek (Skill-Forge) – VCL

## Yukleme
[[define|neutral]] LOAD := domain_docs + kod tabani + policy kaynaklarini baglama; Task() ile hafiza doldurma; SPC:path referansi. [ground:EXPERTISE-ADDENDUM.md] [conf:0.81] [state:confirmed]

## Uygulama
[[HON:teineigo]] [[MOR:root:A-N-L]] [[COM:Analiz+Ogren]] [[CLS:ge_protocol]] [[EVD:-dir<cikarim>]] [[ASP:nesov.]]
- Beceri kurulumunda uzmanlik paketlerini cek.  
- Kanit marker ekle (-mis arastirma, -DI gozlem).  
- Kapsam: domain-specific testler + performans hedefleri.

## Kural
[[direct|emphatic]] RULE := uzmanlik yuklemeden beceri dagitma; conf<=tavan; L2 cikti; registry kaydi. [ground:EXPERTISE-ADDENDUM.md] [conf:0.84] [state:confirmed]

</details>
