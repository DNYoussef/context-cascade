---
name: when-orchestrating-swarm-use-swarm-orchestration
description: Apply swarm-orchestration patterns to general workflows with clear topology, routing, and validation.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
x-version: 3.2.0
x-category: orchestration
x-vcl-compliance: v3.2.0
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

## STANDARD OPERATING PROCEDURE

### Purpose
Stand up swarms for workflow tasks with explicit roles, routing, safety rails, and confidence-aware reporting.

### Trigger Conditions
- **Positive:** multi-agent orchestration, shared-state workflows, health-aware routing, and delegated task trees.
- **Negative:** single-agent tasks, prompt-only edits (route to prompt-architect), or new skill weaving (route to skill-forge).

### Guardrails
- **Skill-Forge structure-first:** keep `SKILL.md`, `examples/`, `tests/` updated; add `resources/`/`references/` or log remediation.
- **Prompt-Architect hygiene:** gather HARD/SOFT/INFERRED constraints, maintain English-only outputs, and declare ceilings.
- **Swarm safety:** enforce registry, health checks, rate limits, and rollback paths; honor hook latency budgets.
- **Adversarial validation:** test churn, loss, and recovery; capture evidence.
- **MCP tagging:** store runs under WHO=`swarm-orchestration-workflow-{session}` and WHY=`skill-execution`.

### Execution Playbook
1. **Intent & constraints:** define objective, scale, and SLOs; confirm inferred needs.
2. **Topology & roles:** select structure, assign owners, and set communication cadence.
3. **Routing & safety:** configure sharding, retries/backoff, rollback, and escalation paths.
4. **Validation loop:** run adversarial drills, measure SLOs, and log telemetry.
5. **Delivery:** present topology, evidence, risks, and confidence ceiling.

### Output Format
- Objective, constraints, and swarm topology/roles.
- Routing rules, safety measures, and rollback plan.
- Validation evidence and risks.
- **Confidence:** `X.XX (ceiling: TYPE Y.YY) - rationale`.

### Validation Checklist
- Structure-first assets present or ticketed; examples/tests reflect swarm workflow.
- Registry and health checks verified; rollback defined; hooks within budgets.
- Adversarial/COV runs stored with MCP tags; confidence ceiling declared; English-only output.

### Completion Definition
Workflow swarm is complete when routing is live, validation passes, risks are owned, and MCP logs persist with session tags.

Confidence: 0.70 (ceiling: inference 0.70) - Swarm workflow doc aligned to skill-forge scaffolding and prompt-architect evidence/confidence rules.
