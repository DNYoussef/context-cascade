---
name: slash-command-encoder
description: Design and route slash-command workflows with clear schemas, safety rails, and validated handoffs.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
x-version: 3.2.0
x-category: orchestration
x-vcl-compliance: v3.2.0
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

## STANDARD OPERATING PROCEDURE

### Purpose
Create reliable slash-command experiences that encode intent, validate payloads, and orchestrate downstream actions with evidence-backed safety.

### Trigger Conditions
- **Positive:** defining new commands, updating schemas, routing commands to agents, permissioning, or adding validation/telemetry.
- **Negative:** generic prompt tweaks (route to prompt-architect) or new skill weaving (route to skill-forge).

### Guardrails
- **Skill-Forge structure-first:** maintain `SKILL.md`, `examples/`, `tests/`; add `resources/` and `references/` or log remediation tasks.
- **Prompt-Architect hygiene:** capture HARD/SOFT/INFERRED constraints (permissions, rate limits), keep English-only outputs, and state ceilings for confidence.
- **Command safety:** validate schemas, enforce authz/authn, rate limits, and idempotency; use registry-approved agents and honor hook latency budgets.
- **Adversarial validation:** fuzz inputs, test auth failures, and simulate replay attacks; capture evidence.
- **MCP tagging:** store command specs under WHO=`slash-command-encoder-{session}` and WHY=`skill-execution`.

### Execution Playbook
1. **Intent & scope:** define command purpose, permissions, and constraints; confirm inferred rules.
2. **Schema design:** draft payloads, defaults, validation rules, and error messages.
3. **Routing:** map commands to agents/actions, set retries/backoff, and logging/telemetry paths.
4. **Safety nets:** apply authz/authn, rate limits, idempotency keys, and rollback behavior.
5. **Validation loop:** fuzz and negative tests, latency checks, and audit logging; store evidence.
6. **Delivery:** share command spec, routing, risks, and confidence ceiling.

### Output Format
- Command summary (intent, permissions, payload schema).
- Routing plan, telemetry, and safety measures.
- Validation evidence (fuzz, auth, replay) and risk register.
- **Confidence:** `X.XX (ceiling: TYPE Y.YY) - rationale`.

### Validation Checklist
- Structure-first assets present or ticketed; examples/tests aligned to schema and routing.
- Authz/rate limits/idempotency validated; registry and hooks healthy.
- Adversarial/COV runs logged with MCP tags; confidence ceiling declared; English-only output.

### Completion Definition
Command is production-ready when schemas pass validation, routing is tested, risks are owned, and evidence is stored with MCP tags.

Confidence: 0.70 (ceiling: inference 0.70) - Slash-command SOP rewritten with skill-forge scaffolding and prompt-architect clarity plus explicit confidence ceilings.
