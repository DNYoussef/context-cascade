---
name: stream-chain
description: Chain streaming workflows with deterministic routing, backpressure controls, and evidence-backed checkpoints.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
x-version: 3.2.0
x-category: orchestration
x-vcl-compliance: v3.2.0
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

## STANDARD OPERATING PROCEDURE

### Purpose
Design and operate stream-first chains where partial outputs are consumed live, errors are contained, and confidence ceilings stay explicit.

### Trigger Conditions
- **Positive:** streaming pipelines, incremental emission, backpressure handling, live fan-out/fan-in, partial-result validation.
- **Negative:** batch-only flows, prompt-only edits (route to prompt-architect), or new skill weaving (route to skill-forge).

### Guardrails
- **Skill-Forge structure-first:** ensure `SKILL.md`, `examples/`, `tests/` exist; add `resources/`/`references/` or document remediation.
- **Prompt-Architect hygiene:** capture HARD/SOFT/INFERRED constraints (latency, chunk size, ordering), keep English-only outputs, and declare ceilings.
- **Streaming safety:** define buffering, ordering, and retry semantics; enforce registry use; keep hook latency budgets.
- **Adversarial validation:** simulate slow consumers, dropped chunks, and ordering skew; capture evidence.
- **MCP tagging:** store run logs with WHO=`stream-chain-{session}` and WHY=`skill-execution`.

### Execution Playbook
1. **Intent & constraints:** set latency/SLOs, chunk policy, and delivery guarantees; confirm inferred constraints.
2. **Chain design:** map stages, owners, and routing; define backpressure and retry rules.
3. **Implementation:** configure streaming hooks, health checks, and telemetry.
4. **Safety nets:** set circuit breakers, buffering thresholds, and rollback/compensation steps.
5. **Validation loop:** run adversarial drills for slow/failing nodes, check ordering, and log metrics.
6. **Delivery:** summarize design, evidence, risks, and confidence ceiling.

### Output Format
- Pipeline overview with constraints and routing.
- Backpressure/buffering policy and retry/rollback rules.
- Validation evidence (ordering, loss, latency) and risks.
- **Confidence:** `X.XX (ceiling: TYPE Y.YY) - rationale`.

### Validation Checklist
- Structure-first assets present or ticketed; examples/tests updated for streaming cases.
- Ordering, retry, and rollback behaviors defined; registry and hooks validated.
- Adversarial/COV runs captured with MCP tags; confidence ceiling stated; English-only output.

### Completion Definition
Stream chain is complete when live runs meet SLOs, failure modes are contained, evidence is stored, and risks are owned with follow-ups.

Confidence: 0.70 (ceiling: inference 0.70) - Stream-chain documentation aligned to skill-forge scaffolding and prompt-architect evidence/confidence rules.
