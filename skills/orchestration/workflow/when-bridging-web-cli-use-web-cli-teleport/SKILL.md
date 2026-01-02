---
name: when-bridging-web-cli-use-web-cli-teleport
description: Orchestrate workflows that bridge web and CLI contexts with secure session handoffs and validated state transfer.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
x-version: 3.2.0
x-category: orchestration
x-vcl-compliance: v3.2.0
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

## STANDARD OPERATING PROCEDURE

### Purpose
Enable reliable teleportation between web and CLI flows by preserving context, validating sessions, and controlling risks with explicit confidence ceilings.

### Trigger Conditions
- **Positive:** tasks requiring web-to-CLI or CLI-to-web transitions, session/state bridging, credential reuse, or hybrid automation.
- **Negative:** single-environment tasks, prompt-only edits (route to prompt-architect), or new skill weaving (route to skill-forge).

### Guardrails
- **Skill-Forge structure-first:** maintain `SKILL.md`, `examples/`, `tests/`; add `resources/`/`references/` or log remediation tasks.
- **Prompt-Architect hygiene:** capture HARD/SOFT/INFERRED constraints (security, state scope), keep English-only outputs, and state ceilings.
- **Bridge safety:** validate auth tokens, sanitize state transfer, set timeouts/backoff, and enforce registry-only agents with hook latency budgets.
- **Adversarial validation:** simulate stale sessions, replay, and permission drift; capture evidence.
- **MCP tagging:** store teleport runs under WHO=`web-cli-teleport-{session}` and WHY=`skill-execution`.

### Execution Playbook
1. **Intent & constraints:** define transition goal, security requirements, and state to carry; confirm inferred limits.
2. **Bridge design:** map handoff points, token handling, and data sanitization.
3. **Execution:** perform handoff with logging, retries, and TodoWrite checkpoints.
4. **Safety nets:** set expiry, rollback, and circuit breakers for failed transfers.
5. **Validation loop:** test replay, stale state, and permission changes; log evidence.
6. **Delivery:** summarize handoff, evidence, risks, and confidence ceiling.

### Output Format
- Transition summary, constraints, and handoff steps.
- Security/validation measures and rollback plan.
- Evidence (replay/stale/permission tests) and risk log.
- **Confidence:** `X.XX (ceiling: TYPE Y.YY) - rationale`.

### Validation Checklist
- Structure-first assets present or ticketed; examples/tests reflect bridge scenarios.
- Auth and state transfer validated; rollback defined; hooks within budgets.
- Adversarial/COV runs stored with MCP tags; confidence ceiling declared; English-only output.

### Completion Definition
Bridge is complete when handoff succeeds with validated security, evidence is stored, risks are owned, and MCP notes persist with session tags.

Confidence: 0.70 (ceiling: inference 0.70) - Web/CLI teleport orchestration rewritten with skill-forge scaffolding and prompt-architect confidence discipline.
