---
name: swarm-orchestration
description: Coordinate swarms end-to-end with clear roles, routing rules, and validated delivery checkpoints.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
x-version: 3.2.0
x-category: orchestration
x-vcl-compliance: v3.2.0
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

## STANDARD OPERATING PROCEDURE

### Purpose
Stand up and operate swarms for general tasks with explicit topology, delegation, safety rails, and confidence-aware reporting.

### Trigger Conditions
- **Positive:** general swarm activation, multi-agent task routing, role-based delegation, shared-state coordination.
- **Negative:** small sequential tasks, prompt-only edits (route to prompt-architect), or new skill weaving (route to skill-forge).

### Guardrails
- **Skill-Forge structure-first:** ensure `SKILL.md`, `examples/`, `tests/` exist; add `resources/`/`references/` or note remediation.
- **Prompt-Architect hygiene:** gather HARD/SOFT/INFERRED constraints, maintain English-only outputs, and state confidence ceilings.
- **Operational safety:** register agents, enforce health checks, rate limits, and rollback paths; honor hook latency budgets.
- **Adversarial validation:** test churn, message loss, and recovery; capture evidence and telemetry.
- **MCP tagging:** save swarm runs under WHO=`swarm-orchestration-{session}` and WHY=`skill-execution`.

### Execution Playbook
1. **Intent & constraints:** define objective, scale, latency targets, and inferred needs.
2. **Topology & roles:** choose structure, assign owners, and set communication cadence.
3. **Routing & controls:** set sharding, retries, backoff, and escalation; enforce registry usage.
4. **Safety nets:** define health probes, rollback/abort, and isolation for risky steps.
5. **Validation loop:** run adversarial drills, measure SLOs, and log evidence.
6. **Delivery:** provide swarm plan, validation summary, risks, and confidence ceiling.

### Output Format
- Swarm objective, constraints, and topology/roles.
- Routing rules, safety measures, and rollback plan.
- Validation evidence and risk register.
- **Confidence:** `X.XX (ceiling: TYPE Y.YY) - rationale`.

### Validation Checklist
- Structure-first assets present or ticketed; examples/tests aligned to current swarm pattern.
- Registry and health checks verified; rollback defined; hooks within budget.
- Adversarial/COV runs captured with MCP tags; confidence ceiling declared; English-only output.

### Completion Definition
Swarm is complete when roles and routing are live, validation is recorded, risks are owned, and MCP logs persist with session tags.

Confidence: 0.70 (ceiling: inference 0.70) - Swarm orchestration rewritten with skill-forge scaffolding and prompt-architect evidence/confidence practices.
