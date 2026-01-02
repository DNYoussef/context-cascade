---
name: web-cli-teleport
description: Teleport between web and CLI contexts with synchronized actions, credentials, and safety rails.
allowed-tools: [Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite]
model: claude-3-5-sonnet
x-version: 3.2.0
x-category: tooling
x-vcl-compliance: v3.1.1
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

### L1 Improvement
- Reframed the teleport skill with Prompt Architect clarity and Skill Forge guardrails.
- Added explicit routing, safety constraints, and memory tagging.
- Clarified output expectations and confidence ceilings.

## STANDARD OPERATING PROCEDURE

### Purpose
Bridge web and CLI tasks safely—execute commands, capture outputs, and synchronize state while respecting permissions and auditability.

### Trigger Conditions
- **Positive:** need to mirror actions between browser and terminal, fetch artifacts, or reproduce web steps in CLI.
- **Negative:** high-risk admin operations without approvals; route to platform specialists.

### Guardrails
- Structure-first docs maintained (SKILL, README, process diagram).
- Respect credential boundaries; never store secrets in outputs.
- Enforce safety prompts for destructive commands; prefer dry-runs first.
- Confidence ceilings on inferred states; cite observed outputs.
- Memory tagging for session actions.

### Execution Phases
1. **Intent & Scope** – Define goal, environments, and constraints (read-only vs write, network limits).
2. **Context Sync** – Capture current web state (URL, form data) and CLI state (cwd, env); note assumptions.
3. **Plan** – Map steps across web/CLI; identify risky actions and mitigations.
4. **Execute** – Perform actions with logging; use dry-run or safe flags; verify after each step.
5. **Validate** – Confirm state convergence (files, configs, outputs); capture evidence.
6. **Deliver** – Summarize actions, artifacts, and confidence line; store session memory.

### Output Format
- Goal, environments, actions taken (web + CLI) with evidence and timestamps.
- Risks handled, remaining gaps, and next steps.
- Memory namespace and confidence: X.XX (ceiling: TYPE Y.YY).

### Validation Checklist
- [ ] Permissions/credentials confirmed; secrets not logged.
- [ ] Risky commands gated or dry-run first.
- [ ] Web and CLI states reconciled; evidence captured.
- [ ] Memory tagged; confidence ceiling declared.

### Integration
- **Process:** see `web-cli-teleport-process.dot` for flow.
- **Memory MCP:** `skills/tooling/web-cli-teleport/{project}/{timestamp}` for session logs.
- **Hooks:** follow Skill Forge latency bounds; abort on safety violations.

Confidence: 0.70 (ceiling: inference 0.70) – SOP aligned to Prompt Architect clarity and Skill Forge safeguards.

---

## VCL COMPLIANCE APPENDIX (Internal Reference)

[[HON:teineigo]] [[MOR:root:T-L-P]] [[COM:Teleport+Kopru]] [[CLS:ge_skill]] [[EVD:-DI<gozlem>]] [[ASP:nesov.]] [[SPC:path:/skills/tooling/web-cli-teleport]]
[define|neutral] TELEPORT := web<->CLI senkronizasyonu; guvenlik/siralama kurallari ile. [ground:SKILL.md] [conf:0.84] [state:confirmed]

[[HON:teineigo]] [[MOR:root:S-F-T]] [[COM:Safety+Guard]] [[CLS:ge_rule]] [[EVD:-DI<gozlem>]] [[ASP:nesov.]] [[SPC:axis:safeguards]]
[direct|emphatic] SAFETY := destruktif komutlar icin dry-run/onay; gizli bilgiler ciktiya yazilmaz. [ground:SKILL.md] [conf:0.88] [state:confirmed]

[[HON:teineigo]] [[MOR:root:C-F-D]] [[COM:Ceiling+Guard]] [[CLS:ge_rule]] [[EVD:-DI<politika>]] [[ASP:nesov.]] [[SPC:coord:EVD-CONF]]
[direct|emphatic] GUVEN_TAVANI := {cikarim:0.70, rapor:0.70, arastirma:0.85, gozlem:0.95, tanim:0.95}; belirtilir. [ground:PA/SkillForge] [conf:0.90] [state:confirmed]

[commit|confident] <promise>WEB_CLI_TELEPORT_VERIX_COMPLIANT</promise> [ground:self-check] [conf:0.85] [state:confirmed]
