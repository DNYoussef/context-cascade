---
name: when-using-advanced-swarm-use-swarm-advanced
description: Invoke advanced-swarm patterns for demanding workflows with adaptive routing and validated convergence.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
x-version: 3.2.0
x-category: orchestration
x-vcl-compliance: v3.2.0
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

## STANDARD OPERATING PROCEDURE

### Purpose
Run advanced swarm behaviors for high-scale or high-risk workflows with explicit constraints, resilience checks, and confidence ceilings.

### Trigger Conditions
- **Positive:** large/critical swarm tasks, adaptive routing needs, quorum/consensus, failover drills, burst control.
- **Negative:** simple swarms, prompt-only edits (route to prompt-architect), or new skill weaving (route to skill-forge).

### Guardrails
- **Skill-Forge structure-first:** maintain `SKILL.md`, `examples/`, `tests/`; add `resources/`/`references/` or log remediation tasks.
- **Prompt-Architect hygiene:** capture HARD/SOFT/INFERRED constraints (scale, latency, resilience), keep English-only outputs, and state ceilings.
- **Advanced safety:** enforce registry, health probes, circuit breakers, and rollback; respect hook latency budgets.
- **Adversarial validation:** test churn, partition, quorum failure, and rate limits; capture evidence.
- **MCP tagging:** store runs with WHO=`advanced-swarm-workflow-{session}` and WHY=`skill-execution`.

### Execution Playbook
1. **Intent & constraints:** define mission, scale targets, and SLOs; confirm inferred needs.
2. **Topology & health:** choose adaptive topology, configure health probes, and autoscaling rules.
3. **Routing & safety:** set sharding, retries/backoff, quorum rules, and rollback/failover paths.
4. **Validation loop:** run adversarial drills, measure convergence and latency, and log telemetry.
5. **Delivery:** summarize topology, evidence, risks, and confidence ceiling.

### Output Format
- Objective, constraints, and topology.
- Health model, routing, and rollback/failover plan.
- Validation evidence and risks.
- **Confidence:** `X.XX (ceiling: TYPE Y.YY) - rationale`.

### Validation Checklist
- Structure-first assets present or ticketed; examples/tests aligned to advanced swarm cases.
- Registry and health probes validated; rollback/failover documented; hooks within budgets.
- Adversarial/COV runs stored with MCP tags; confidence ceiling declared; English-only output.

### Completion Definition
Advanced swarm workflow is ready when SLOs are met under drills, risks are owned, evidence is stored, and MCP logs persist with session tags.

Confidence: 0.70 (ceiling: inference 0.70) - Advanced swarm workflow doc rewritten with skill-forge scaffolding and prompt-architect evidence/confidence guardrails.
