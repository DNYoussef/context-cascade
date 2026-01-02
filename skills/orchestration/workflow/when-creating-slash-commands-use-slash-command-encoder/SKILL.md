---
name: when-creating-slash-commands-use-slash-command-encoder
description: Build slash-command workflows with clear schemas, validation, and safe routing using the slash-command-encoder patterns.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
x-version: 3.2.0
x-category: orchestration
x-vcl-compliance: v3.2.0
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

## STANDARD OPERATING PROCEDURE

### Purpose
Create or update slash commands with explicit constraints, security checks, and evidence-backed routing while keeping confidence ceilings clear.

### Trigger Conditions
- **Positive:** new command design, schema updates, permission changes, routing to agents/actions, telemetry and validation additions.
- **Negative:** prompt-only edits (route to prompt-architect) or new skill weaving (route to skill-forge).

### Guardrails
- **Skill-Forge structure-first:** ensure `SKILL.md`, `examples/`, `tests/` exist; add `resources/`/`references/` or log remediation tasks.
- **Prompt-Architect hygiene:** capture HARD/SOFT/INFERRED constraints (auth, rate limits, payload rules), keep English-only outputs, and state ceilings.
- **Command safety:** validate payloads, enforce authz/authn, rate limits, idempotency, and rollback; registry-only agents and hook budgets apply.
- **Adversarial validation:** fuzz inputs, test auth failures, replay, and timeout scenarios; capture evidence.
- **MCP tagging:** store command plans under WHO=`slash-command-workflow-{session}` and WHY=`skill-execution`.

### Execution Playbook
1. **Intent & constraints:** define command purpose, permissions, and schema; confirm inferred requirements.
2. **Design:** draft payload schema, validation messages, and UX responses.
3. **Routing:** map to agents/actions with retries/backoff and telemetry.
4. **Safety nets:** set authz, rate limits, idempotency, and rollback/abort behavior.
5. **Validation loop:** run fuzzing, auth/replay tests, and latency checks; log evidence.
6. **Delivery:** summarize command spec, evidence, risks, and confidence ceiling.

### Output Format
- Command intent, schema, permissions, and routing.
- Safety controls and rollback/abort steps.
- Validation evidence and risk register.
- **Confidence:** `X.XX (ceiling: TYPE Y.YY) - rationale`.

### Validation Checklist
- Structure-first assets present or ticketed; examples/tests aligned to command behavior.
- Authz/rate limits/idempotency validated; registry and hooks within budgets.
- Adversarial/COV runs stored with MCP tags; confidence ceiling declared; English-only output.

### Completion Definition
Command workflow is ready when schemas and routing validate, risks are owned, evidence is stored, and MCP logs persist with session tags.

Confidence: 0.70 (ceiling: inference 0.70) - Slash-command workflow doc rewritten with skill-forge scaffolding and prompt-architect confidence discipline.
