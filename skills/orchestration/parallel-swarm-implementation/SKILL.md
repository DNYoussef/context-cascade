---
name: parallel-swarm-implementation
description: Launch and manage parallel swarms with synchronized milestones, resource controls, and verified aggregation paths.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
x-version: 3.2.0
x-category: orchestration
x-vcl-compliance: v3.2.0
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

## STANDARD OPERATING PROCEDURE

### Purpose
Execute concurrent swarm tracks that coordinate via shared checkpoints, avoid contention, and converge into validated outputs without overconfidence.

### Trigger Conditions
- **Positive:** parallel tracks for large tasks, multi-lane feature delivery, concurrent research/build/test efforts, shard/merge workflows.
- **Negative:** sequential single-lane tasks, prompt-only edits (route to prompt-architect), or new skill creation (route to skill-forge).

### Guardrails
- **Skill-Forge structure-first:** ensure `SKILL.md`, `examples/`, `tests/` exist; add `resources/` and `references/` or log remediation.
- **Prompt-Architect hygiene:** capture HARD/SOFT/INFERRED constraints per lane, define merge criteria, and present pure-English outputs with ceilings.
- **Parallel safety:** prevent resource contention, define isolation and merge windows, and enforce registry agents plus hook latency budgets.
- **Adversarial validation:** test merge conflicts, data skew, and race conditions; run COV and capture evidence.
- **MCP tagging:** store run artifacts with WHO=`parallel-swarm-implementation-{session}` and WHY=`skill-execution`.

### Execution Playbook
1. **Intent & lanes:** identify goals, shard plan, and constraints; confirm inferred dependencies.
2. **Topology & roles:** assign lanes with owners, milestones, and communication cadence; define merge gates.
3. **Execution controls:** allocate quotas, set retries/backoff, and monitor health per lane.
4. **Safety nets:** plan contention avoidance, rollback paths per lane, and conflict resolution rules.
5. **Validation loop:** dry-run merges, test failure injection, measure latency/throughput, and log evidence.
6. **Delivery:** summarize lane outputs, merge decisions, residual risks, and confidence ceiling.

### Output Format
- Lane map with owners, milestones, and merge criteria.
- Constraint matrix and risk register.
- Validation evidence (merge tests, conflict handling) and telemetry.
- **Confidence:** `X.XX (ceiling: TYPE Y.YY) - rationale`.

### Validation Checklist
- Structure-first assets present or ticketed; examples/tests aligned to parallel patterns.
- Merge/rollback rules defined; registry and hook budgets validated.
- Adversarial/COV runs stored with MCP tags; confidence ceiling declared; English-only output.

### Completion Definition
Parallel work is complete when lanes deliver outputs, merge tests pass, conflicts are resolved, evidence is stored, and risks are owned with next steps.

Confidence: 0.70 (ceiling: inference 0.70) - Parallel swarm SOP rewritten with skill-forge scaffolding and prompt-architect constraint/evidence discipline.
