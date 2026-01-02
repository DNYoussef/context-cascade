---
name: when-deploying-cloud-swarm-use-flow-nexus-swarm
description: Deploy Flow Nexus cloud swarms with secure channels, adaptive scaling, and validated failover paths.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
x-version: 3.2.0
x-category: orchestration
x-vcl-compliance: v3.2.0
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

## STANDARD OPERATING PROCEDURE

### Purpose
Guide cloud swarm deployments on Flow Nexus, ensuring topology, security, scaling, and rollback are evidence-backed with explicit confidence ceilings.

### Trigger Conditions
- **Positive:** Flow Nexus swarm creation, region/cluster rollouts, scaling policy updates, channel/secret setup, failover testing.
- **Negative:** local-only swarms, prompt-only edits (route to prompt-architect), or new skill weaving (route to skill-forge).

### Guardrails
- **Skill-Forge structure-first:** maintain `SKILL.md`, `examples/`, `tests/`; add `resources/`/`references/` or record remediation tasks.
- **Prompt-Architect hygiene:** capture HARD/SOFT/INFERRED constraints (regions, quotas, compliance), keep English-only outputs, and state ceilings.
- **Cloud safety:** enforce identity/secrets, network rules, quotas, and rollback strategies; registry-only agents and hook budgets apply.
- **Adversarial validation:** simulate region loss, quota exhaustion, and message drops; record evidence and telemetry.
- **MCP tagging:** persist runs with WHO=`cloud-swarm-flow-nexus-{session}` and WHY=`skill-execution`.

### Execution Playbook
1. **Intent & constraints:** define targets (capacity, latency, compliance) and confirm inferred platform limits.
2. **Topology & security:** design swarm layout, set channels/ACLs, and register agents.
3. **Deployment plan:** set rollout steps, health probes, autoscaling rules, and retries/backoff.
4. **Safety nets:** prepare rollback, isolation, and incident response; guard secrets and access scopes.
5. **Validation loop:** run failover/quota/latency drills; capture evidence and timings.
6. **Delivery:** share topology, validation results, risks, and confidence ceiling.

### Output Format
- Deployment objective, constraints, and topology.
- Security, autoscaling, and rollback plans.
- Validation evidence (failover, quota, latency) and risks.
- **Confidence:** `X.XX (ceiling: TYPE Y.YY) - rationale`.

### Validation Checklist
- Structure-first assets present or ticketed; examples/tests aligned to Flow Nexus cases.
- Identity, network, and rollback validated; registry and hooks within budgets.
- Adversarial/COV runs stored with MCP tags; confidence ceiling declared; English-only output.

### Completion Definition
Deployment is ready when swarms meet SLOs, security/scaling controls are validated, risks are owned, and evidence is persisted with MCP tags.

Confidence: 0.70 (ceiling: inference 0.70) - Cloud swarm orchestration rewritten with skill-forge scaffolding and prompt-architect evidence/confidence discipline.
