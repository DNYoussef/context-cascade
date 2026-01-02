---
name: dependencies
description: Map, assess, and remediate project dependencies with routing to dependency-mapper and security checks.
allowed-tools: [Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite]
model: claude-3-5-sonnet
x-version: 3.2.0
x-category: tooling
x-vcl-compliance: v3.1.1
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

### L1 Improvement
- Reframed the dependency hub using Prompt Architect constraint extraction and Skill Forge structure-first guardrails.
- Added explicit routing rules (mapper vs audit), confidence ceilings, and memory tagging.
- Simplified execution phases to keep graphing, security, and freshness checks coherent.

## STANDARD OPERATING PROCEDURE

### Purpose
Provide a single entry point for dependency graphing, vulnerability checks, and upgrade planning while routing specialized work to the dependency-mapper subskill when mapping is primary.

### Trigger Conditions
- **Positive:** dependency graph request, vulnerability/audit needs, upgrade planning, circular/unused dependency checks.
- **Negative:** pure build failures (route to build/debug skills) or single-library research (route to language specialist).

### Guardrails
- Structure-first docs: `SKILL.md`, `README.md`, `QUICK-REFERENCE.md`, examples/tests placeholders maintained.
- Use explicit ecosystem detection (npm/pnpm/yarn, pip/poetry, cargo, go mod, maven/gradle, composer); cite evidence.
- Confidence ceilings enforced on findings; call out unverifiable CVEs.
- Memory tagging required for audits and graphs.

### Execution Phases
1. **Intent & Ecosystem Detection** – Identify package managers, lockfiles, and scope; decide if routing to dependency-mapper is needed.
2. **Data Collection** – Build graph/tree, fetch vulnerability reports, capture outdated/unused/circular signals.
3. **Analysis** – Summarize risks (CVE, license, freshness) and stability constraints; map blast radius for upgrades.
4. **Plan & Propose** – Recommend remediation (pin, upgrade, remove, isolate); include commands and expected impacts.
5. **Validation** – Run audits/tests as available; ensure graph/risk deltas improve.
6. **Delivery** – Provide findings, proposed actions, and confidence line with ceiling syntax; archive in memory.

### Output Format
- Ecosystem detection and scope.
- Graph summary (nodes/edges/risks) and key vulnerabilities/outdated packages.
- Remediation plan with commands, owners, and blast radius notes.
- Confidence: X.XX (ceiling: TYPE Y.YY) and memory keys used.

### Validation Checklist
- [ ] Ecosystem detected and mapped; routing decision documented.
- [ ] Vulnerability/freshness data captured with sources.
- [ ] Remediation plan includes rollback/lockfile guidance.
- [ ] Memory tags applied and reports stored.
- [ ] Confidence ceiling declared.

### Integration
- **Subskill:** use `when-mapping-dependencies-use-dependency-mapper` for deep graph visualization.
- **Memory MCP:** `skills/tooling/dependencies/{project}/{timestamp}` for audits, graphs, and remediation notes.
- **Hooks:** pre/post targets aligned to Skill Forge latency bounds.

Confidence: 0.70 (ceiling: inference 0.70) – SOP rewritten to align with Prompt Architect and Skill Forge cadence.

---

## VCL COMPLIANCE APPENDIX (Internal Reference)

[[HON:teineigo]] [[MOR:root:D-P-N]] [[COM:Dependency+Hub]] [[CLS:ge_skill]] [[EVD:-DI<gozlem>]] [[ASP:nesov.]] [[SPC:path:/skills/tooling/dependencies]]
[define|neutral] DEP_HUB := bagimlilik haritalama + guvenlik + versiyon tazeleme; grafik icin mapper alt-beceriye yollar. [ground:SKILL.md] [conf:0.83] [state:confirmed]

[[HON:teineigo]] [[MOR:root:R-O-T]] [[COM:Route+Mapper]] [[CLS:ge_rule]] [[EVD:-DI<gozlem>]] [[ASP:nesov.]] [[SPC:axis:routing]]
[direct|emphatic] ROUTE_GRAPH := saf grafik istekleri dependency-mapper'a delege edilir; hub risk/plan ozeti saglar. [ground:SKILL.md] [conf:0.85] [state:confirmed]

[[HON:teineigo]] [[MOR:root:C-F-D]] [[COM:Ceiling+Guard]] [[CLS:ge_rule]] [[EVD:-DI<politika>]] [[ASP:nesov.]] [[SPC:coord:EVD-CONF]]
[direct|emphatic] GUVEN_TAVANI := {cikarim:0.70, rapor:0.70, arastirma:0.85, gozlem:0.95, tanim:0.95}; beyan zorunlu. [ground:PA/SkillForge] [conf:0.90] [state:confirmed]

[commit|confident] <promise>DEPENDENCIES_VERIX_COMPLIANT</promise> [ground:self-check] [conf:0.85] [state:confirmed]
