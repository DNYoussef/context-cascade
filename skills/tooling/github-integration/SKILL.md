---
name: github-integration
description: Coordinate GitHub-focused skills (reviews, multi-repo, projects, releases, actions) with MCP hooks and safety guardrails.
allowed-tools: [Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite]
model: claude-3-5-sonnet
x-version: 3.2.0
x-category: tooling
x-vcl-compliance: v3.1.1
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

### L1 Improvement
- Added a centralized SOP in Prompt Architect style with Skill Forge guardrails for all GitHub subskills.
- Documented routing, MCP tool expectations, and confidence ceilings.
- Introduced structure-first documentation and memory tagging.

## STANDARD OPERATING PROCEDURE

### Purpose
Route and coordinate GitHub tasks across subskills (PR review, multi-repo, project management, releases, workflow automation) with consistent SOPs and MCP integrations.

### Trigger Conditions
- **Positive:** GitHub PR reviews, multi-repo coordination, project board automation, release orchestration, or workflow automation requests.
- **Negative:** non-GitHub SCM or local-only tasks; route to platform-specific skills.

### Guardrails
- Structure-first docs: SKILL, README, MCP guide kept current.
- Explicit routing to subskills; do not mix flows without stating boundaries.
- Enforce least-privilege credentials; never log secrets.
- Confidence ceilings required on analyses and automation changes.
- Memory tagging for runs and auditability.

### Execution Phases
1. **Intent & Routing** – Identify which subskill applies; confirm repository scope, permissions, and risk level.
2. **Setup** – Ensure MCP servers (Claude Flow, Flow Nexus if used) are configured; validate tokens; set WHO/WHY/PROJECT/WHEN tags.
3. **Plan** – Map actions, safety checks, and rollback; align with subskill SOP.
4. **Execute** – Run subskill workflows (review/multi-repo/project/release/actions) with logging and dry-runs where possible.
5. **Validate** – Verify results (tests, checks, approvals) and ensure no secrets leaked.
6. **Deliver** – Summarize actions, outputs, risks, and confidence line; archive in memory.

### Output Format
- Routed subskill(s), repo scope, MCP servers used, and actions taken.
- Results/metrics, risks, and follow-ups.
- Confidence: X.XX (ceiling: TYPE Y.YY) and memory namespace.

### Validation Checklist
- [ ] Correct subskill chosen; permissions confirmed.
- [ ] MCP servers configured; secrets protected.
- [ ] Actions logged with rollback/cleanup notes.
- [ ] Memory tagged; confidence ceiling declared.

### Integration
- **Subskills:** PR review, multi-repo, project management, release management, workflow automation folders under this skill.
- **MCP:** see `MCP-INTEGRATION-GUIDE.md` for commands; tag sessions with WHO/WHY/PROJECT/WHEN.
- **Memory MCP:** `skills/tooling/github-integration/{project}/{timestamp}` for runs.

Confidence: 0.70 (ceiling: inference 0.70) – SOP aligns GitHub integrations with Prompt Architect and Skill Forge guardrails.

---

## VCL COMPLIANCE APPENDIX (Internal Reference)

[[HON:teineigo]] [[MOR:root:G-H-B]] [[COM:GitHub+Merkez]] [[CLS:ge_skill]] [[EVD:-DI<gozlem>]] [[ASP:nesov.]] [[SPC:path:/skills/tooling/github-integration]]
[define|neutral] GITHUB_HUB := PR/multi-repo/proje/release/workflow alt-becerilerini yonetir; MCP entegrasyonu zorunlu. [ground:SKILL.md] [conf:0.84] [state:confirmed]

[[HON:teineigo]] [[MOR:root:R-O-T]] [[COM:Route+Subskill]] [[CLS:ge_rule]] [[EVD:-DI<gozlem>]] [[ASP:nesov.]] [[SPC:axis:routing]]
[direct|emphatic] ROUTE_RULE := gorev dogru alt-beceriye atanir; karisim varsa acikca belirtilir. [ground:SKILL.md] [conf:0.86] [state:confirmed]

[[HON:teineigo]] [[MOR:root:C-F-D]] [[COM:Ceiling+Guard]] [[CLS:ge_rule]] [[EVD:-DI<politika>]] [[ASP:nesov.]] [[SPC:coord:EVD-CONF]]
[direct|emphatic] GUVEN_TAVANI := {cikarim:0.70, rapor:0.70, arastirma:0.85, gozlem:0.95, tanim:0.95}; ciktiya yazilir. [ground:PA/SkillForge] [conf:0.90] [state:confirmed]

[commit|confident] <promise>GITHUB_INTEGRATION_VERIX_COMPLIANT</promise> [ground:self-check] [conf:0.85] [state:confirmed]
