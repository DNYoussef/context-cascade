---
name: hive-mind-advanced
description: Coordinate collective-intelligence swarms with shared context, consensus patterns, and conflict-aware decisioning.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
x-version: 3.2.0
x-category: orchestration
x-vcl-compliance: v3.2.0
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

## STANDARD OPERATING PROCEDURE

### Purpose
Operate advanced hive-mind swarms that blend exploration and exploitation, maintain shared memory, and deliver consensus-backed outputs without overclaiming.

### Trigger Conditions
- **Positive:** collective reasoning, divergent/convergent rounds, consensus/selection, shared-memory swarms, conflict resolution among agents.
- **Negative:** isolated single-agent tasks, fixed pipelines without deliberation, or prompt-only edits (route to prompt-architect).

### Guardrails
- **Skill-Forge structure-first:** maintain `SKILL.md`, `examples/`, `tests/`; provision `resources/` and `references/` or document gaps.
- **Prompt-Architect hygiene:** collect intent, constraints, and perspectives; tag HARD/SOFT/INFERRED; output pure English with ceiling-noted confidence.
- **Collective safety:** define roles (scouts, synthesizers, judges), prevent groupthink via adversarial reviewer, and enforce registry use plus hook latency budgets.
- **Adversarial validation:** run dissent and tie-break drills, conflict resolution tests, and COV loops; capture evidence.
- **MCP tagging:** persist hive runs with WHO=`hive-mind-advanced-{session}` and WHY=`skill-execution`.

### Execution Playbook
1. **Intent & framing:** clarify objective, success metrics, and diversity requirements; confirm inferred constraints.
2. **Swarm design:** assign roles, cadence (diverge/converge), and memory layout; set evidence requirements.
3. **Deliberation rounds:** collect proposals, adversarial reviews, and synthesis; manage quotas and timeboxes.
4. **Decision & commit:** select outputs via criteria, record dissent, and define rollback/next-iteration triggers.
5. **Validation loop:** stress-test consensus, latency, and bias; run COV and store telemetry.
6. **Delivery:** summarize chosen path, dissenting views, evidence, residual risks, and confidence ceiling.

### Output Format
- Objective, constraints, and swarm roles.
- Deliberation cadence, decision criteria, and memory approach.
- Evidence log (supporting and dissenting), risks, and follow-ups.
- **Confidence:** `X.XX (ceiling: TYPE Y.YY) - rationale`.

### Validation Checklist
- Structure-first assets present or ticketed; examples/tests reflect hive patterns.
- Diversity and dissent enforced; registry and hooks verified; rollback/iteration rules documented.
- Adversarial/COV runs stored with MCP tags; confidence ceiling stated; English-only output.

### Completion Definition
Swarm decision is complete when consensus is reached (or documented disagreement), evidence is stored, risks are owned, and next actions or rollbacks are clear.

Confidence: 0.70 (ceiling: inference 0.70) - Hive-mind SOP now mirrors skill-forge rigor and prompt-architect evidence/confidence discipline.
