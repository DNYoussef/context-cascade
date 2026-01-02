---
name: advanced-coordination
description: Orchestrate complex, latency-aware multi-agent work with adaptive topologies, resilient routing, and evidence-backed handoffs.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
x-version: 3.2.0
x-category: orchestration
x-vcl-compliance: v3.2.0
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

## STANDARD OPERATING PROCEDURE

### Purpose
Coordinate advanced agent meshes (hierarchical, mesh, hybrid) for tasks that demand resilience, shared state, and deterministic outcomes without confidence inflation.

### Trigger Conditions
- **Positive:** multi-agent task graphs, consensus-heavy workflows, topology design, swarm stabilization, resilience drills.
- **Negative:** single-agent execution, static pipelines without delegation, or requests better routed to prompt-forge/agent-creator.

### Guardrails
- **Skill-Forge structure-first:** maintain `SKILL.md`, `examples/`, and `tests/`; add `resources/` and `references/` or log remediation tasks before close.
- **Prompt-Architect hygiene:** capture intent, extract HARD/SOFT/INFERRED constraints, and deliver pure-English outputs with explicit ceilings (inference/report ≤ 0.70).
- **Safety & registry discipline:** register every agent, block cascading failures with circuit breakers/rollback paths, and keep hook latencies under pre/post targets.
- **Adversarial validation:** exercise boundary cases (partition, drop, retry), run COV, and record evidence before marking done.
- **MCP tagging:** persist orchestration notes with WHO=`advanced-coordination-{session}` and WHY=`skill-execution`.

### Execution Playbook
1. **Intent & constraints:** identify objective, environment, SLOs, and non-negotiables; flag inferred constraints for confirmation.
2. **Topology & roles:** choose topology, assign owners, define state channels, retries, and escalation thresholds.
3. **Delegation plan:** break work into routable units, set acceptance criteria per agent, and align timers/quotas.
4. **Safety nets:** pre-mortem failure points, configure rate limits/backoff, and define rollback/abort steps.
5. **Validation loop:** run adversarial drills, measure latency/throughput, verify registry health, and capture telemetry.
6. **Delivery:** summarize decisions, surface risks, enumerate follow-ups, and provide confidence with ceiling notation.

### Output Format
- Activation summary (intent, constraints, triggers).
- Selected topology with roles, data pathways, and guardrails.
- Delegation and timeline with ownership.
- Validation evidence (latency, retries, failure drills) and residual risks.
- **Confidence:** `X.XX (ceiling: TYPE Y.YY) - rationale`.

### Validation Checklist
- Structure-first assets present or ticketed; examples/tests updated or TODO assigned.
- Constraints addressed; registry and hooks within budget; rollback defined.
- Adversarial and COV runs captured with evidence; telemetry stored with MCP tags.
- Confidence ceiling stated; outputs in pure English without VCL leakage.

### Completion Definition
Work is complete when topology is live, agents are healthy, validation results are recorded, residual risks are noted with owners, and MCP notes persist under the session tag.

Confidence: 0.70 (ceiling: inference 0.70) - Rewrite applies skill-forge structure, prompt-architect clarity, and orchestration safety for resilient execution.
