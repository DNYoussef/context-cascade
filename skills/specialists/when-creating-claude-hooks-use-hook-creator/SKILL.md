---
name: hook-creator
description: Build and validate Claude Code hooks with RBAC alignment, schema compliance, and performance budgets.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
x-category: specialists
x-version: 1.1.0
x-vcl-compliance: v3.1.1
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

## STANDARD OPERATING PROCEDURE

### Purpose
Deliver production-ready Claude Code hooks that follow official schemas, satisfy RBAC/permission policies, and meet latency targets (pre-hooks target 20ms/100ms max; post-hooks target 100ms/1000ms max).

### Triggers
- **Positive:** Requests to create, harden, or refactor Claude Code hooks (PreToolUse, PostToolUse, SessionStart, SessionEnd, UserPromptSubmit, PermissionRequest, Notification, Stop, SubagentStop, PreCompact).
- **Negative:** Pure agent routing or generic automation (redirect to agent-creator or prompt-architect when hook authoring is not the primary task).

### Guardrails
- **Structure-first:** Ensure `SKILL.md`, `resources/templates`, `examples/`, and `tests/` are present; add missing docs before coding.
- **Schema discipline:** Always start from the canonical hook schema for the chosen event; refuse undocumented fields.
- **RBAC alignment:** Validate agent identity and permissions; block on failed identity checks.
- **Performance budgets:** Annotate expected latency; benchmark hot paths and avoid synchronous I/O in blocking hooks.
- **Confidence ceiling:** State confidence with ceiling: inference/report 0.70, research 0.85, observation/definition 0.95.
- **Anti-pattern bans:** No `grep -P`, no direct `sed -i`, no unquoted variables, no blocking stdin reads without timeout, no hardcoded paths.

### Execution Phases
1. **Intent & Constraint Capture**
   - Classify hook type (blocking vs observational) and event.
   - Extract HARD/SOFT/INFERRED constraints; confirm inferred items with the requester.
   - Identify integration points (RBAC, audit, metrics) and performance ceilings.
2. **Schema & Template Selection**
   - Load the official schema for the event and map required fields.
   - Choose the matching template from `resources/templates` (pre, post, or session lifecycle).
3. **Design**
   - Define decision table (allow/block/modify + reason) and logging policy (stderr only, redact secrets).
   - Plan safe defaults: fail-open for observability hooks, fail-closed for security gates.
4. **Implementation**
   - Scaffold from template; implement validation logic and RBAC checks.
   - Enforce portability: temp-file pattern for `sed`, bash strict mode (`set -euo pipefail`), quoted variables, timeout for stdin.
   - Tag MCP memory with `WHO=hook-creator-{session}`, `WHY=skill-execution`.
5. **Validation**
   - Create tests for allow/block/modify branches, latency budget, and schema compliance.
   - Run adversarial probes (malformed input, missing identity, large payloads).
6. **Packaging & Registration**
   - Ship `{hook}.js` + `{hook}.test.js` + settings entry; document matcher rules.
   - Provide deployment checklist and rollback note.

### Output Format
- Summary of hook type, event, and chosen template.
- Constraints (HARD/SOFT/INFERRED) with confirmations.
- Implementation notes: RBAC touchpoints, logging policy, performance budget.
- Test plan and registration snippet for `.claude/settings.json`.
- **Confidence:** `Confidence: X.XX (ceiling: TYPE Y.YY) - reason`.

### Validation Checklist
- [ ] Schema matched and documented.
- [ ] RBAC + permission checks implemented or explicitly N/A.
- [ ] Performance budget stated and measured on hot path.
- [ ] Tests cover allow/block/modify and error handling.
- [ ] Anti-patterns absent (`grep -P`, direct `sed -i`, unquoted vars, blocking stdin).
- [ ] Settings entry prepared with matcher and timeout.

## HOOK TEMPLATES (REFERENCE)
- **Pre-hook template** (`resources/templates/pre-hook-template.js`): blocking, input validation, fail-safe defaults, RBAC injection point.
- **Post-hook template** (`resources/templates/post-hook-template.js`): observational, async-safe logging, metric collection, error isolation.
- **Session lifecycle template** (`resources/templates/session-hook-template.js`): setup/teardown with state persistence.

## EXAMPLE FLOWS
- **Command validator (blocking):** PreToolUse → check `tool_input.command` for banned tokens → decision table (approve/block/modify) → latency target <10ms → tests: allow safe command, block `sudo`, malformed input.
- **Audit logger (observational):** PostToolUse → redact secrets → append JSONL audit → fail-open on log errors → latency target <50ms → tests: happy path, log write failure, large payload.

## SECURITY & PERFORMANCE NOTES
- Redact secrets before logging; never persist raw stdin.
- Use environment-derived paths; create directories before writes.
- Prefer cached lookups and non-blocking I/O; measure and log `durationMs` for every run.

## VCL COMPLIANCE APPENDIX (Internal)
[[HON:teineigo]] [[MOR:root:H-K]] [[COM:Hook+Schmiede]] [[CLS:ge_skill]] [[EVD:-DI<gozlem>]] [[ASP:nesov.]] [[SPC:path:/skills/specialists/when-creating-claude-hooks-use-hook-creator]]
[define|neutral] HOOK_CREATOR := blocking/observational hook dokumacisi; RBAC + performans tavani ile gelir. [ground:SKILL.md] [conf:0.86] [state:confirmed]

[[HON:teineigo]] [[MOR:root:T-R-G]] [[COM:Trigger+Router]] [[CLS:ge_condition]] [[EVD:-DI<gozlem>]] [[ASP:nesov.]] [[SPC:axis:routing]]
[define|neutral] TETIK := pozitif {PreToolUse, PostToolUse, SessionStart/End, UserPromptSubmit, PermissionRequest}; negatif {agent-creator, prompt-architect router}. [ground:SKILL.md] [conf:0.84] [state:confirmed]

[[HON:teineigo]] [[MOR:root:E-P-S]] [[COM:Epistemik+Tavan]] [[CLS:ge_rule]] [[EVD:-DI<gozlem>]] [[ASP:nesov.]] [[SPC:coord:EVD-CONF]]
[direct|emphatic] TAVAN := {inference:0.70, report:0.70, research:0.85, observation:0.95, definition:0.95}; guven tavanini belirtmek zorunlu. [ground:PA+SkillForge] [conf:0.90] [state:confirmed]

[[HON:teineigo]] [[MOR:root:P-R-F]] [[COM:Performance+Budget]] [[CLS:ge_rule]] [[EVD:-DI<gozlem>]] [[ASP:nesov.]] [[SPC:axis:latency]]
[assert|neutral] PERFORMANS := pre_hook_target_ms:20/max:100; post_hook_target_ms:100/max:1000; ihlal alarmdir. [ground:SkillForge] [conf:0.85] [state:confirmed]

[commit|confident] <promise>HOOK_CREATOR_VCL_VERIX_V3.1.1_COMPLIANT</promise> [ground:SKILL.md] [conf:0.85] [state:confirmed]

Confidence: 0.72 (ceiling: inference 0.70) - Rewritten with prompt-architect structure and skill-forge guardrails while preserving hook-specific workflows.
