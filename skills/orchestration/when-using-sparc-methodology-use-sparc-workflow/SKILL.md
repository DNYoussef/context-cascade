---
name: when-using-sparc-methodology-use-sparc-workflow
description: Orchestrate SPARC (Scope, Plan, Act, Review, Consolidate) workflows with gated checkpoints and explicit confidence ceilings.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
x-version: 3.2.0
x-category: orchestration
x-vcl-compliance: v3.2.0
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

## STANDARD OPERATING PROCEDURE

### Purpose
Run SPARC methodology end-to-end with clear intent capture, stage gates, evidence-backed reviews, and confidence-aware delivery.

### Trigger Conditions
- **Positive:** structured problem solving using SPARC, stage-gated delivery, retrospectives, consolidation of learnings.
- **Negative:** ad-hoc single-pass tasks, prompt-only edits (route to prompt-architect), or new skill weaving (route to skill-forge).

### Guardrails
- **Skill-Forge structure-first:** maintain `SKILL.md`, `examples/`, `tests/`; add `resources/`/`references/` or log remediation tasks.
- **Prompt-Architect hygiene:** capture HARD/SOFT/INFERRED constraints per SPARC stage, keep English-only outputs, and declare ceilings.
- **Stage safety:** set entry/exit criteria for Scope/Plan/Act/Review/Consolidate, enforce registry usage, and keep hook latency budgets.
- **Adversarial validation:** challenge assumptions each stage, run COV, and document evidence and deltas.
- **MCP tagging:** store SPARC runs with WHO=`sparc-workflow-{session}` and WHY=`skill-execution`.

### Execution Playbook
1. **Scope:** define objective, constraints, and success metrics; confirm inferred assumptions.
2. **Plan:** design approach, assign owners, and set timelines plus rollback points.
3. **Act:** execute tasks with monitoring, TodoWrite updates, and guardrails.
4. **Review:** validate outcomes, run adversarial checks, and log evidence.
5. **Consolidate:** capture learnings, decisions, and next actions.
6. **Delivery:** summarize SPARC path, evidence, risks, and confidence ceiling.

### Output Format
- SPARC stage summary with constraints and decisions.
- Evidence log, risks, and follow-ups.
- **Confidence:** `X.XX (ceiling: TYPE Y.YY) - rationale`.

### Validation Checklist
- Structure-first assets present or ticketed; examples/tests reflect SPARC flow.
- Stage gates and rollback points defined; registry and hooks validated.
- Adversarial/COV runs stored with MCP tags; confidence ceiling declared; English-only output.

### Completion Definition
Workflow is done when SPARC stages complete with evidence, risks are owned, learnings captured, and MCP logs tagged for reuse.

Confidence: 0.70 (ceiling: inference 0.70) - SPARC workflow doc rewritten with skill-forge scaffolding and prompt-architect constraint/confidence discipline.
