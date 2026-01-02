---
name: meta-loop-orchestrator
description: Run nested improvement loops with guardrails for iteration planning, validation, and convergence tracking.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
x-version: 3.2.0
x-category: orchestration
x-vcl-compliance: v3.2.0
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

## STANDARD OPERATING PROCEDURE

### Purpose
Coordinate iterative improvement loops (e.g., RICE, dogfooding, COV) to refine deliverables while preventing endless iteration or confidence drift.

### Trigger Conditions
- **Positive:** recursive improvement, self-critique loops, A/B iteration planning, convergence checks, dogfooding cycles.
- **Negative:** single-pass edits, straightforward prompt cleanups (route to prompt-architect), or new skill weaving (route to skill-forge).

### Guardrails
- **Skill-Forge structure-first:** keep `SKILL.md`, `examples/`, `tests/` updated; add `resources/`/`references/` or document gaps.
- **Prompt-Architect hygiene:** extract HARD/SOFT/INFERRED goals per iteration, define stop criteria, and state ceilings for confidence.
- **Loop safety:** set iteration caps, convergence thresholds, and rollback checkpoints; enforce registry-only agents and hook latencies.
- **Adversarial validation:** challenge assumptions every loop, run boundary tests, and record evidence plus deltas.
- **MCP tagging:** log loops with WHO=`meta-loop-orchestrator-{session}` and WHY=`skill-execution`.

### Execution Playbook
1. **Intent & target:** define improvement goal, metrics, and stop criteria; confirm inferred needs.
2. **Loop design:** select frameworks (COV, dogfooding), assign roles, and timebox iterations.
3. **Execution:** run iteration, collect evidence, compute delta; keep artifacts versioned.
4. **Adversarial check:** probe edge cases, challenge assumptions, and update risk register.
5. **Convergence decision:** compare delta to threshold; decide continue, pivot, or stop.
6. **Delivery:** summarize iterations, evidence, residual risks, and confidence ceiling.

### Output Format
- Improvement goal, metrics, and stop rule.
- Iteration log (changes, evidence, deltas).
- Risk/assumption register and next steps.
- **Confidence:** `X.XX (ceiling: TYPE Y.YY) - rationale`.

### Validation Checklist
- Structure-first assets present or ticketed; examples/tests reflect current best version.
- Iteration caps and stop rules respected; registry and hooks validated.
- Adversarial/COV evidence stored with MCP tags; confidence ceiling declared; English-only output.

### Completion Definition
Loop concludes when delta falls below threshold or stop rule triggers, evidence is stored, risks are owned, and a ready-to-use version is documented with confidence ceiling.

Confidence: 0.70 (ceiling: inference 0.70) - Meta-loop SOP aligned to skill-forge scaffolding and prompt-architect clarity with explicit convergence controls.
