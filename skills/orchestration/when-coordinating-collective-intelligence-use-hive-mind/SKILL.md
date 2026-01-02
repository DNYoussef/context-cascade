---
name: when-coordinating-collective-intelligence-use-hive-mind
description: Coordinate collective-intelligence swarms with structured divergence/convergence, dissent capture, and evidence-backed synthesis.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
x-version: 3.2.0
x-category: orchestration
x-vcl-compliance: v3.2.0
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

## STANDARD OPERATING PROCEDURE

### Purpose
Run hive-mind style workflows that encourage diverse exploration, synthesize findings, and record dissent with explicit confidence ceilings.

### Trigger Conditions
- **Positive:** collective ideation, multi-perspective analysis, consensus formation, bias checking, and adjudication of conflicting views.
- **Negative:** single-expert responses, prompt-only edits (route to prompt-architect), or new skill weaving (route to skill-forge).

### Guardrails
- **Skill-Forge structure-first:** ensure `SKILL.md`, `examples/`, `tests/` exist; add `resources/`/`references/` or log remediation.
- **Prompt-Architect hygiene:** capture intent, HARD/SOFT/INFERRED constraints, and viewpoints; output in English with ceilinged confidence.
- **Collective safety:** assign roles for exploration/synthesis/adversarial review, prevent groupthink via dissent triggers, enforce registry and hook budgets.
- **Adversarial validation:** test dissent handling, tie-breaks, and bias checks; record evidence.
- **MCP tagging:** store runs under WHO=`hive-mind-{session}` and WHY=`skill-execution`.

### Execution Playbook
1. **Intent & framing:** define objective, diversity goals, and constraints; confirm inferred needs.
2. **Swarm setup:** assign roles, cadence, and evidence requirements; configure shared memory.
3. **Deliberation:** run diverge/converge rounds, capture dissent, and synthesize.
4. **Validation loop:** probe for missing perspectives, conflicts, and bias; log telemetry.
5. **Delivery:** present recommendation, dissent, risks, and confidence ceiling.

### Output Format
- Objective, constraints, and swarm roles/cadence.
- Evidence and dissent log with synthesis decision.
- Risks, mitigations, and follow-ups.
- **Confidence:** `X.XX (ceiling: TYPE Y.YY) - rationale`.

### Validation Checklist
- Structure-first assets present or ticketed; examples/tests match hive behaviors.
- Dissent and bias checks executed; registry and hooks verified.
- Adversarial/COV runs stored with MCP tags; confidence ceiling declared; English-only output.

### Completion Definition
Work is complete when synthesis and dissent are documented, risks are owned, evidence is stored, and MCP notes are tagged for reuse.

Confidence: 0.70 (ceiling: inference 0.70) - Collective-intelligence orchestration rewritten with skill-forge scaffolding and prompt-architect evidence/confidence rules.
