---
name: flow-nexus-swarm
description: Orchestrate cloud-ready swarms on Flow Nexus with adaptive scaling, secure messaging, and validated deployment steps.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
x-version: 3.2.0
x-category: orchestration
x-vcl-compliance: v3.2.0
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

## STANDARD OPERATING PROCEDURE

### Purpose
Deploy and manage Flow Nexus swarms with topology-aware scaling, secure channel setup, and resilience against cloud-specific failure modes.

### Trigger Conditions
- **Positive:** Flow Nexus deployments, cloud swarm tuning, scaling/rollback drills, secure channel provisioning, cross-region coordination.
- **Negative:** local-only swarms, non-Flow Nexus requests, or pure prompt shaping (route to prompt-architect).

### Guardrails
- **Skill-Forge structure-first:** ensure `SKILL.md`, `examples/`, `tests/` exist; add `resources/` and `references/` or log remediation.
- **Prompt-Architect clarity:** extract HARD/SOFT/INFERRED constraints (regions, quotas, compliance), use pure English, and declare confidence ceilings.
- **Platform safety:** enforce identity, network, and secret management policies; register agents; keep hook latency within budgets; define rollback for cluster actions.
- **Adversarial validation:** simulate region loss, quota exhaustion, and message drops; record evidence and metrics.
- **MCP tagging:** store swarm runs with WHO=`flow-nexus-swarm-{session}` and WHY=`skill-execution`.

### Execution Playbook
1. **Intent & constraints:** capture targets (capacity, latency, compliance) and confirm inferred platform limits.
2. **Topology & setup:** design swarm layout, provision channels, register agents, and configure autoscaling rules.
3. **Deployment plan:** stage rollout, health checks, and backoff/retry policies; set observability hooks.
4. **Safety nets:** pre-mortem failure points, define rollback and isolation controls; validate secrets and access scopes.
5. **Validation loop:** run adversarial drills (failover, rate limits), measure telemetry, and capture evidence.
6. **Delivery:** present deployment map, validation results, residual risks, and confidence ceiling.

### Output Format
- Deployment objective, constraints, and topology.
- Channel/security setup, autoscaling rules, and rollback paths.
- Validation artifacts (failover, latency, quota tests) and risk log.
- MCP references for persisted notes.
- **Confidence:** `X.XX (ceiling: TYPE Y.YY) - rationale`.

### Validation Checklist
- Structure-first assets present or ticketed; examples/tests updated or planned.
- Identity/secrets validated; registry and hooks healthy; rollback tested.
- Adversarial and COV runs logged with MCP tags; confidence ceiling stated; English-only output.

### Completion Definition
Swarm deployment is complete when topology is live, security and scaling controls are verified, evidence is stored, and remaining risks are owned with next actions.

Confidence: 0.70 (ceiling: inference 0.70) - Flow Nexus orchestration reframed with skill-forge structure and prompt-architect evidence rules for cloud resilience.
