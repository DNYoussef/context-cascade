---
name: literature-synthesis
description: Synthesize multiple sources into coherent narratives with explicit evidence tracking and confidence ceilings.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
x-version: 3.2.0
x-category: research
x-vcl-compliance: v3.1.1
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

## STANDARD OPERATING PROCEDURE

### Purpose
- Combine findings across papers/articles into concise, evidence-backed syntheses.
- Expose constraints and assumptions clearly to avoid overgeneralization.
- Maintain structure-first artifacts for reuse and traceability.

### Trigger Conditions
- **Positive:** literature reviews, state-of-the-art summaries, related work sections.
- **Negative:** single-source summaries (use `academic-reading-workflow`), or prompt-only edits (`prompt-architect`).

### Guardrails
- Constraint buckets: HARD (scope, dates, domains), SOFT (style, depth), INFERRED (coverage, exclusions) with sources.
- Two-pass refinement: synthesis structure → epistemic audit with evidence and ceilings.
- Cite sources inline with links/pages; avoid claim aggregation without evidence.

### Inputs
- Research question and intended audience.
- Source list with metadata and access.
- Formatting needs (bullets, narrative, tables) and timebox.

### Workflow
1. **Scope & Constraints**: Define inclusion/exclusion criteria and outputs; confirm INFERRED assumptions.
2. **Source Mapping**: Group sources by theme and strength; note gaps or conflicts.
3. **Draft Synthesis**: Build outline, then fill with claims tied to sources and confidence ceilings.
4. **Epistemic Pass**: Check for overclaims, contradictions, and missing evidence; rebalance coverage.
5. **Deliver & Store**: Provide synthesized narrative plus evidence table; update references/examples.

### Validation & Quality Gates
- Every claim tied to at least one source with confidence ceiling.
- Coverage matches constraints and inclusion criteria.
- Conflicts highlighted with proposed resolutions or follow-ups.

### Response Template
```
**Scope & Constraints**
- HARD / SOFT / INFERRED.

**Key Themes**
- Theme → evidence → confidence ceiling.

**Conflicts / Gaps**
- ...

**Next Steps**
- ...

Confidence: 0.81 (ceiling: research 0.85) - based on cross-source synthesis and evidence tracking.
```

Confidence: 0.81 (ceiling: research 0.85) - reflects completed synthesis with evidence-linked claims.
