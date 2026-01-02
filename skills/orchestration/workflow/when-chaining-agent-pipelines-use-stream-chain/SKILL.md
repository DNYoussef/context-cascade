---
name: when-chaining-agent-pipelines-use-stream-chain
description: Chain agent pipelines with streaming handoffs, backpressure controls, and validated ordering.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
x-version: 3.2.0
x-category: orchestration
x-vcl-compliance: v3.2.0
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

## STANDARD OPERATING PROCEDURE

### Purpose
Operate streaming agent pipelines where partial outputs flow across stages with deterministic routing, safety rails, and confidence ceilings.

### Trigger Conditions
- **Positive:** chaining agents with streaming outputs, incremental validation, backpressure handling, live fan-out/fan-in.
- **Negative:** batch-only flows, prompt-only edits (route to prompt-architect), or new skill weaving (route to skill-forge).

### Guardrails
- **Skill-Forge structure-first:** keep `SKILL.md`, `examples/`, `tests/` current; add `resources/`/`references/` or log remediation tasks.
- **Prompt-Architect hygiene:** capture HARD/SOFT/INFERRED constraints (latency, ordering, chunk size), keep English-only outputs, and declare ceilings.
- **Pipeline safety:** define buffering, retries, ordering guarantees, and rollback/compensation; enforce registry agents and hook budgets.
- **Adversarial validation:** test slow consumers, dropped chunks, and ordering skew; capture evidence.
- **MCP tagging:** save runs with WHO=`agent-stream-chain-{session}` and WHY=`skill-execution`.

### Execution Playbook
1. **Intent & constraints:** define SLOs and delivery guarantees; confirm inferred needs.
2. **Pipeline design:** map stages, routing, buffering, and backpressure rules.
3. **Execution:** configure hooks, health probes, and telemetry; manage retries/backoff.
4. **Safety nets:** set circuit breakers and rollback/compensation paths.
5. **Validation loop:** run adversarial drills for ordering, loss, and latency; log evidence.
6. **Delivery:** present design, validation, risks, and confidence ceiling.

### Output Format
- Pipeline summary with constraints and routing.
- Backpressure/buffering rules and rollback plan.
- Validation evidence and risks.
- **Confidence:** `X.XX (ceiling: TYPE Y.YY) - rationale`.

### Validation Checklist
- Structure-first assets present or ticketed; examples/tests reflect stream chaining.
- Ordering/backpressure/rollback validated; registry and hooks within budgets.
- Adversarial/COV runs stored with MCP tags; confidence ceiling declared; English-only output.

### Completion Definition
Pipeline is ready when streaming SLOs are met, failure modes are contained, evidence is stored, and risks are owned with MCP logs.

Confidence: 0.70 (ceiling: inference 0.70) - Stream-chain workflow doc aligned to skill-forge scaffolding and prompt-architect evidence/confidence rules.
