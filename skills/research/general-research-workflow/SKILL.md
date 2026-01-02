---
name: general-research-workflow
description: Core research loop for scoping, searching, analyzing, and reporting with explicit constraints and validation.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
x-version: 3.2.0
x-category: research
x-vcl-compliance: v3.1.1
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

## STANDARD OPERATING PROCEDURE

### Purpose
- Provide a default research workflow when no specialized skill is specified.
- Ensure constraint clarity, evidence hygiene, and confidence ceilings.
- Maintain skill-forge structure: SKILL + README + examples + references.

### Trigger Conditions
- **Positive:** open-ended research tasks, quick investigations, or shaping a plan before deeper pipelines.
- **Negative:** heavy orchestration (use `deep-research-orchestrator`) or prompt-only work (`prompt-architect`).

### Guardrails
- Extract HARD / SOFT / INFERRED constraints with sources; confirm INFERRED items early.
- Two-pass refinement on deliverables: structure/coverage then epistemic validation.
- Keep outputs in English, cite evidence, and state confidence with ceilings.

### Inputs
- Research question or decision to support.
- Time constraints, depth expectations, and deliverable format.
- Starting sources (if any) and exclusions.

### Workflow
1. **Frame & Constraints**: Capture the question, decision, and constraint buckets.
2. **Search & Collect**: Gather high-signal sources; log provenance.
3. **Analyze**: Extract claims, compare sources, and note conflicts or gaps.
4. **Synthesize**: Organize findings into themes tied to the question and constraints.
5. **Validate**: Check coverage vs. constraints, source quality, and confidence ceilings.
6. **Deliver**: Provide summary, evidence table, risks, and next steps; store references/examples.

### Validation & Quality Gates
- Minimum two passes completed with documented changes.
- Evidence linked to sources; conflicting evidence surfaced.
- Confidence ceilings aligned to evidence type.
- Deliverables stored with project tags.

### Response Template
```
**Question & Constraints**
- HARD: ...
- SOFT: ...
- INFERRED (confirm): ...

**Findings**
- Claim → evidence → confidence ceiling.

**Gaps / Risks**
- ...

**Next Steps**
- ...

Confidence: 0.78 (ceiling: inference 0.70) - based on gathered evidence and validation checks.
```

Confidence: 0.78 (ceiling: inference 0.70) - Default setting after completing the SOP.
