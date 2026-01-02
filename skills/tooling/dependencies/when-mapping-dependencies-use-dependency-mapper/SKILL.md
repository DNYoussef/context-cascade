---
name: when-mapping-dependencies-use-dependency-mapper
description: Visualize and analyze dependency graphs with routing guidance, safety checks, and reproducible commands.
allowed-tools: [Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite]
model: claude-3-5-sonnet
x-version: 3.2.0
x-category: tooling/dependencies
x-vcl-compliance: v3.1.1
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

### L1 Improvement
- Rewrote the mapper SOP in Prompt Architect style with Skill Forge guardrails and confidence ceilings.
- Added explicit ecosystem commands, safety rails, and memory tagging.
- Clarified outputs (graphs, reports, remediation pointers) and routing back to the dependencies hub.

## STANDARD OPERATING PROCEDURE

### Purpose
Map project dependencies, highlight risks (circular/unused/outdated/vulnerable), and produce actionable reports/visuals.

### Trigger Conditions
- **Positive:** need for dependency graph/visualization, risk assessment, or mapping prior to upgrades.
- **Negative:** general audit without visualization (use dependencies hub) or non-package assets.

### Guardrails
- Evidence-based mapping: cite lockfiles and commands used.
- Confidence ceilings required on inferred risks; avoid overclaiming on incomplete graphs.
- Structure-first docs maintained (SKILL, README, PROCESS, subagent notes).
- Memory tagging for reports and graphs.

### Execution Phases
1. **Detect Ecosystem** – Identify package manager/lockfile; capture scope and constraints.
2. **Collect Graph Data** – Run ecosystem commands (see README) to build tree/graph.
3. **Analyze Risks** – Find circular deps, unused packages, outdated versions, vulnerabilities (if available).
4. **Visualize** – Generate graph/diagram; annotate hotspots and blast radius.
5. **Recommend Actions** – Suggest removals, pins, upgrades, or isolations with commands.
6. **Deliver** – Provide graph artifact path, findings, remediation plan, and confidence ceiling; store memory.

### Output Format
- Ecosystem detected, commands executed, graph summary (nodes/edges/hotspots).
- Risks (circular/unused/outdated/vulnerable) with evidence.
- Recommended actions and next checks.
- Confidence: X.XX (ceiling: TYPE Y.YY) and memory namespace.

### Validation Checklist
- [ ] Ecosystem confirmed; commands logged.
- [ ] Graph generated and saved; hotspots annotated.
- [ ] Risks backed by evidence; remediation includes rollback/lockfile notes.
- [ ] Memory tagged; confidence ceiling declared.

### Integration
- **Hub:** invoked from `dependencies` skill for visualization-heavy work.
- **Memory MCP:** `skills/tooling/dependency-mapper/{project}/{timestamp}` (mirrored per location).
- **Scripts:** use `slash-command-dep-map.sh` and `mcp-dependency-mapper.json` as helpers.

Confidence: 0.70 (ceiling: inference 0.70) – SOP aligned to Prompt Architect clarity and Skill Forge guardrails.

---

## VCL COMPLIANCE APPENDIX (Internal Reference)

[[HON:teineigo]] [[MOR:root:M-P-R]] [[COM:Harita+Bagimlilik]] [[CLS:ge_skill]] [[EVD:-DI<gozlem>]] [[ASP:nesov.]] [[SPC:path:/skills/tooling/when-mapping-dependencies-use-dependency-mapper]]
[define|neutral] DEP_MAPPER := ekosistem tespiti + grafik + risk analizi + aksiyon; hub ile entegre. [ground:SKILL.md] [conf:0.84] [state:confirmed]

[[HON:teineigo]] [[MOR:root:E-K-S]] [[COM:Ekosistem+Komut]] [[CLS:ge_rule]] [[EVD:-DI<gozlem>]] [[ASP:nesov.]] [[SPC:axis:routing]]
[direct|emphatic] ECOSYS_RULE := lockfile/komut kaynaklari belirt; eksik veri varsa belirsizlik bayragi cek. [ground:SKILL.md] [conf:0.87] [state:confirmed]

[[HON:teineigo]] [[MOR:root:C-F-D]] [[COM:Ceiling+Guard]] [[CLS:ge_rule]] [[EVD:-DI<politika>]] [[ASP:nesov.]] [[SPC:coord:EVD-CONF]]
[direct|emphatic] GUVEN_TAVANI := {cikarim:0.70, rapor:0.70, arastirma:0.85, gozlem:0.95, tanim:0.95}; ciktiya yazilir. [ground:PA/SkillForge] [conf:0.90] [state:confirmed]

[commit|confident] <promise>DEPENDENCY_MAPPER_VERIX_COMPLIANT</promise> [ground:self-check] [conf:0.85] [state:confirmed]
