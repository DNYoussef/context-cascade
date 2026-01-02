---
name: when-automating-workflows-use-hooks-automation
description: Automate workflow hooks safely with clear triggers, validation, and rollback-aware orchestration.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
x-version: 3.2.0
x-category: orchestration
x-vcl-compliance: v3.2.0
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

## STANDARD OPERATING PROCEDURE

### Purpose
Design and maintain hook-based automations (pre/post hooks, webhooks) with explicit constraints, monitoring, and confidence-aware delivery.

### Trigger Conditions
- **Positive:** creating/updating hooks, chaining systems via callbacks, adding validation to hook payloads, retry/backoff tuning, telemetry for hook events.
- **Negative:** manual single runs, prompt-only edits (route to prompt-architect), or new skill weaving (route to skill-forge).

### Guardrails
- **Skill-Forge structure-first:** keep `SKILL.md`, `examples/`, `tests/` in place; add `resources/`/`references/` or log remediation tasks.
- **Prompt-Architect hygiene:** capture HARD/SOFT/INFERRED constraints (auth, rate limits, payload schema), ensure English-only output, and declare ceilings.
- **Hook safety:** validate signatures, enforce idempotency, set timeouts/backoff, and define circuit breakers; honor registry-only agents and latency budgets.
- **Adversarial validation:** fuzz payloads, test retries, replay, and timeout scenarios; capture evidence.
- **MCP tagging:** store hook playbooks under WHO=`hooks-automation-{session}` and WHY=`skill-execution`.

### Execution Playbook
1. **Intent & constraints:** define hook purpose, endpoints, SLAs, and compliance; confirm inferred requirements.
2. **Design:** map triggers to actions, schema validation, auth methods, and telemetry.
3. **Safety nets:** configure retries/backoff, idempotency keys, and failure isolation with rollback.
4. **Validation loop:** fuzz and negative tests, replay/timeout drills, and timing checks; log evidence.
5. **Rollout:** stage deployment, monitor early signals, and prepare rollback.
6. **Delivery:** summarize design, evidence, risks, and confidence ceiling.

### Output Format
- Hook intent, triggers, endpoints, and schemas.
- Auth/idempotency controls, retries/backoff, and rollback plan.
- Validation evidence (fuzz, replay, timeout) and risk register.
- **Confidence:** `X.XX (ceiling: TYPE Y.YY) - rationale`.

### Validation Checklist
- Structure-first assets present or ticketed; examples/tests reflect hook cases.
- Auth, retries, and rollback validated; registry and hooks within latency budgets.
- Adversarial/COV runs logged with MCP tags; confidence ceiling declared; English-only output.

### Completion Definition
Hook automation is complete when validations pass, monitoring is in place, risks are owned, and evidence is persisted with MCP tags.

Confidence: 0.70 (ceiling: inference 0.70) - Hook automation doc rebuilt with skill-forge scaffolding and prompt-architect confidence and constraint discipline.
