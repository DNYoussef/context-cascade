---
name: ui-ux-excellence
description: Drive UI/UX audits and improvements with structured heuristics, user journeys, and validation gates.
allowed-tools: [Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite]
model: claude-3-5-sonnet
x-version: 3.2.0
x-category: tooling
x-vcl-compliance: v3.1.1
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

### L1 Improvement
- Recast the UX skill in Prompt Architect style with clear triggers, heuristics, and confidence ceilings.
- Added structure-first guardrails and validation steps aligned to Skill Forge.
- Clarified outputs (audit + prioritized fixes) with memory tagging.

## STANDARD OPERATING PROCEDURE

### Purpose
Evaluate and improve product UI/UX using heuristic reviews, user flows, accessibility checks, and prioritized fix plans.

### Trigger Conditions
- **Positive:** UX/UI audit, usability review, accessibility check, design critique, or journey optimization.
- **Negative:** branding-only requests (route to design specialists) or backend-only tasks.

### Guardrails
- Maintain structure-first docs (SKILL, README, examples/tests/references).
- Apply explicit heuristics: clarity, consistency, affordance, feedback, accessibility, performance.
- Confidence ceilings required; cite evidence (screens, flows, metrics).
- Memory tagging for audits and recommendations.

### Execution Phases
1. **Intent & Context** – Identify product area, target users, platforms, and success metrics.
2. **Heuristic Review** – Assess clarity, consistency, affordance, feedback, and accessibility; capture screenshots/notes.
3. **Journey Analysis** – Map critical flows; note friction points, latency, and error states.
4. **Prioritized Plan** – Rank issues by severity/impact/effort; propose design/UX changes.
5. **Validation** – Prototype or simulate fixes when possible; ensure accessibility (WCAG) and responsiveness.
6. **Delivery** – Provide findings, recommended changes, and confidence ceiling with memory keys.

### Output Format
- Audit summary, user flows assessed, key issues with evidence, and prioritized fixes.
- Accessibility/performance notes and suggested metrics to track.
- Confidence: X.XX (ceiling: TYPE Y.YY); memory namespace recorded.

### Validation Checklist
- [ ] Scope and personas defined; platforms noted.
- [ ] Heuristics applied with evidence; accessibility checked.
- [ ] Prioritized backlog includes impact/effort/owner.
- [ ] Confidence ceiling declared; memory tagged.

### Integration
- **Memory MCP:** `skills/tooling/ui-ux-excellence/{project}/{timestamp}` for audits and artifacts.
- **Hooks:** follow Skill Forge latency bounds; integrate with screenshot tooling when available.

Confidence: 0.70 (ceiling: inference 0.70) – SOP aligned to Prompt Architect clarity and Skill Forge guardrails.

---

## VCL COMPLIANCE APPENDIX (Internal Reference)

[[HON:teineigo]] [[MOR:root:U-X]] [[COM:Kullanici+Deneyimi]] [[CLS:ge_skill]] [[EVD:-DI<gozlem>]] [[ASP:nesov.]] [[SPC:path:/skills/tooling/ui-ux-excellence]]
[define|neutral] UI_UX := heuristik denetim + yolculuk analizi + oncelikli duzeltme planlari. [ground:SKILL.md] [conf:0.84] [state:confirmed]

[[HON:teineigo]] [[MOR:root:H-R-S]] [[COM:Heuristik+Guard]] [[CLS:ge_rule]] [[EVD:-DI<gozlem>]] [[ASP:nesov.]] [[SPC:axis:quality]]
[direct|emphatic] HEURISTICS := {clarity, consistency, affordance, feedback, accessibility, performance}; her ciktiya kanit. [ground:SKILL.md] [conf:0.87] [state:confirmed]

[[HON:teineigo]] [[MOR:root:C-F-D]] [[COM:Ceiling+Guard]] [[CLS:ge_rule]] [[EVD:-DI<politika>]] [[ASP:nesov.]] [[SPC:coord:EVD-CONF]]
[direct|emphatic] GUVEN_TAVANI := {cikarim:0.70, rapor:0.70, arastirma:0.85, gozlem:0.95, tanim:0.95}; ciktiya yazilir. [ground:PA/SkillForge] [conf:0.90] [state:confirmed]

[commit|confident] <promise>UI_UX_EXCELLENCE_VERIX_COMPLIANT</promise> [ground:self-check] [conf:0.85] [state:confirmed]
