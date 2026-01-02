---
name: coordination
description: Coordinate distributed agents with resilient topologies, synchronized state, and evidence-backed communication patterns.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
x-version: 3.2.0
x-category: orchestration
x-vcl-compliance: v3.2.0
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

## STANDARD OPERATING PROCEDURE

### Purpose
Deliver reliable multi-agent coordination across meshes, hierarchies, or hybrids while preventing state loss, deadlocks, and confidence overreach.

### Trigger Conditions
- **Positive:** topology design, agent registration, message routing, consensus or quorum work, partition/latency tolerance needs.
- **Negative:** single-threaded execution, non-coordinated batch work, or prompt-only refinement (route to prompt-architect).

### Guardrails
- **Skill-Forge structure-first:** keep `SKILL.md`, `examples/`, and `tests/` current; add `resources/` and `references/` or record remediation tasks.
- **Prompt-Architect clarity:** capture intent and constraints (HARD/SOFT/INFERRED), avoid VCL leakage, and state confidence with ceilings.
- **Coordination safety:** register every agent, validate topology (no orphaned nodes/cycles where forbidden), enforce health checks, and keep hooks within latency budgets.
- **Adversarial validation:** probe partitions, message loss, reconnects, and rate limits; document evidence.
- **MCP tagging:** persist coordination runs with WHO=`coordination-{session}` and WHY=`skill-execution`.

### Execution Playbook
1. **Intent & constraints:** define mission, scale, latency targets, and shared-state rules; confirm inferred needs.
2. **Topology & registry:** select topology, register agents, define namespaces, and configure routing keys.
3. **Delegation & messaging:** set task sharding rules, retries, ack/requeue policies, and escalation paths.
4. **Safety & resilience:** plan for partitions, backpressure, and failover; add circuit breakers and watchdogs.
5. **Validation loop:** run adversarial drills, measure latency/throughput, and verify state convergence.
6. **Delivery:** summarize topology, evidence, residual risks, and confidence ceiling.

### Output Format
- Intent, constraints, and chosen topology.
- Agent registry snapshot, routing schema, and health model.
- Operational plan (sharding, retries, escalation, rollback).
- Validation evidence with metrics; risks and follow-ups.
- **Confidence:** `X.XX (ceiling: TYPE Y.YY) - rationale`.

### Validation Checklist
- Structure-first assets present or queued; examples/tests reflect current patterns.
- Registry complete; health checks and latency budgets verified; rollback path defined.
- Adversarial/COV runs captured with MCP tags; confidence ceiling present; English-only output.

### Completion Definition
Coordination is complete when topology is stable, messaging meets SLOs, validation artifacts are stored, and remaining risks are owned with next steps logged.

Confidence: 0.70 (ceiling: inference 0.70) - Coordination SOP rewritten with skill-forge structure, prompt-architect constraint handling, and resilience guardrails.
