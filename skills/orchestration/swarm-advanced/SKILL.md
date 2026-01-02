---
name: swarm-advanced
description: Operate advanced swarms with adaptive routing, health-aware scaling, and validated convergence patterns.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
x-version: 3.2.0
x-category: orchestration
x-vcl-compliance: v3.2.0
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

## STANDARD OPERATING PROCEDURE

### Purpose
Manage sophisticated swarm behaviors—adaptive topologies, quorum decisions, failover, and convergence—while keeping evidence and confidence ceilings explicit.

### Trigger Conditions
- **Positive:** high-scale swarms, adaptive routing, quorum/consensus needs, burst control, health-based scaling.
- **Negative:** small fixed teams, prompt-only edits (route to prompt-architect), or new skill weaving (route to skill-forge).

### Guardrails
- **Skill-Forge structure-first:** keep `SKILL.md`, `examples/`, `tests/` current; add `resources/`/`references/` or log remediation.
- **Prompt-Architect hygiene:** capture HARD/SOFT/INFERRED constraints (scale, latency, resilience), use English-only outputs, and provide ceilinged confidence.
- **Swarm safety:** enforce registry, health probes, circuit breakers, and rollback; maintain hook latency budgets.
- **Adversarial validation:** test churn, partition, rate limits, and quorum failure; capture evidence and metrics.
- **MCP tagging:** log runs under WHO=`swarm-advanced-{session}` and WHY=`skill-execution`.

### Execution Playbook
1. **Intent & constraints:** define mission, scale, and SLOs; confirm inferred needs.
2. **Topology & health:** choose topology, set health probes, and autoscaling rules.
3. **Routing & delegation:** set sharding, retries, backoff, and escalation paths.
4. **Safety nets:** plan failover, rollback, and isolation; guard shared state.
5. **Validation loop:** run churn/partition drills, measure convergence and latency, and store evidence.
6. **Delivery:** provide topology, evidence, risks, and confidence ceiling.

### Output Format
- Swarm objective, constraints, and topology.
- Health model, routing rules, rollback/failover plan.
- Validation evidence (churn, partition, quorum) and risks.
- **Confidence:** `X.XX (ceiling: TYPE Y.YY) - rationale`.

### Validation Checklist
- Structure-first assets present or ticketed; examples/tests aligned to advanced swarm cases.
- Registry and health probes verified; rollback/failover documented; hook budgets met.
- Adversarial/COV runs stored with MCP tags; confidence ceiling declared; English-only output.

### Completion Definition
Swarm is stable when health and convergence targets are met, failover is validated, risks are owned, and evidence is persisted with MCP tags.

Confidence: 0.70 (ceiling: inference 0.70) - Advanced swarm SOP rebuilt with skill-forge scaffolding and prompt-architect evidence/confidence guardrails.
