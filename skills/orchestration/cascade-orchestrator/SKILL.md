---
name: cascade-orchestrator
description: Layered orchestration for staged workflows with gated handoffs, evidence capture, and rollback-aware routing.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
x-version: 3.2.0
x-category: orchestration
x-vcl-compliance: v3.2.0
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

## STANDARD OPERATING PROCEDURE

### Purpose
Design and operate cascaded workflows where each stage consumes prior outputs, enforces quality gates, and exposes controlled escape hatches for recovery.

### Trigger Conditions
- **Positive:** multi-stage pipelines, gated reviews, dependency-driven workflows, staged rollouts, evidence-capturing handoffs.
- **Negative:** single-step tasks, linear prompts without gating (route to prompt-architect), or new skill creation (route to skill-forge).

### Guardrails
- **Skill-Forge structure-first:** maintain `SKILL.md`, `examples/`, `tests/`; add `resources/` and `references/` or log follow-ups.
- **Prompt-Architect hygiene:** document intent, stage-by-stage HARD/SOFT/INFERRED constraints, and provide pure-English outputs with ceiling-aware confidence.
- **Stage safety:** define entry/exit criteria per stage, cache artifacts, and include rollback/skip rules that prevent cascading failure.
- **Adversarial validation:** simulate partial failures, retries, and out-of-order delivery; capture evidence and timing.
- **MCP tagging:** persist cascade runs with WHO=`cascade-orchestrator-{session}` and WHY=`skill-execution` for traceability.

### Execution Playbook
1. **Intent & constraints:** collect objective, success metrics, and required sequencing; confirm inferred dependencies.
2. **Stage design:** enumerate stages, owners, inputs/outputs, and gate criteria with timing budgets.
3. **Routing plan:** wire registry-approved agents, define escalation paths, and set retry/backoff rules per stage.
4. **Safety nets:** pre-mortem failure points, define rollback/skip logic, and guard shared state.
5. **Validation loop:** run dry-runs and adversarial drills; log evidence, timings, and deltas.
6. **Delivery:** present cascade map, gate outcomes, residual risks, and confidence ceiling.

### Output Format
- Cascade overview with stages, owners, and gate criteria.
- Constraint matrix (HARD/SOFT/INFERRED) and risk register.
- Routing rules (retries, rollbacks, escalation paths).
- Validation evidence with timings and artifacts; remaining risks/open items.
- **Confidence:** `X.XX (ceiling: TYPE Y.YY) - rationale`.

### Validation Checklist
- Structure-first assets ready or ticketed; examples/tests updated or queued.
- Gate criteria defined and met per stage; retries/backoffs verified.
- Registry-only agents used; hooks within latency budgets; rollback tested.
- Adversarial/COV results stored with MCP tags; confidence ceiling declared.

### Completion Definition
Workflow is complete when each stage passes gates, artifacts are persisted, recovery paths are validated, and cascade telemetry is recorded with MCP tags.

Confidence: 0.70 (ceiling: inference 0.70) - Document aligns cascade orchestration with skill-forge structure and prompt-architect evidence and confidence rules.
