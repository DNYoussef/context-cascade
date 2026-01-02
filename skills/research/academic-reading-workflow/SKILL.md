---
name: academic-reading-workflow
description: Systematic blueprint for reading and annotating academic papers with searchable notes, explicit constraints, and quality gates.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
x-version: 3.2.0
x-category: research
x-vcl-compliance: v3.1.1
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

## STANDARD OPERATING PROCEDURE

### Purpose
- Run a disciplined, repeatable paper-reading workflow that produces searchable annotations and evidence for downstream writing.
- Apply prompt-architect refinements to surface constraints, guard against overclaiming, and keep outputs English-only with explicit ceilings.
- Preserve skill-forge structure-first requirements: SKILL.md + README + examples + references; log any gaps.

### Trigger Conditions
- **Positive:** requests to read, digest, or annotate academic papers/books; build citation-ready notes; turn readings into evidence.
- **Negative:** casual skimming or non-research entertainment; route targeted prompt crafting to `prompt-architect`.

### Guardrails
- Extract constraints in three classes: **HARD** (must satisfy), **SOFT** (should), **INFERRED** (flag for confirmation) with sources cited.
- Run the two-pass refinement loop: (1) structure/coverage; (2) epistemic/confidence calibration.
- Enforce confidence ceilings: inference/report 0.70; research 0.85; observation/definition 0.95. State ceiling explicitly in every response.
- Maintain evidential trail: cite sections/pages for each insight; avoid verbatim quotes unless necessary.

### Inputs
- Source details (title, authors, venue/year, access links).
- Research question or goal for the reading block.
- Time/length constraints and output format for notes.

### Workflow
1. **Intent & Constraint Scan**: Capture the research question, success criteria, and the three constraint classes; confirm INFERRED items before proceeding.
2. **Plan the Passes**: Outline skim → detailed read → consolidation; define note schema (summary, claim, evidence, page, keyword tags).
3. **Pass 1 – Structural Read**: Map structure, thesis, methods, key figures/tables. Log HARD coverage gaps.
4. **Pass 2 – Evidence Pass**: Extract claims with page anchors, record confidence per claim, and tag uncertainties for follow-up.
5. **Synthesize & Validate**: Cluster notes by theme, mark contradictions, and run a self-check against constraints and quality gates (searchability, completeness, bias).
6. **Package Deliverables**: Produce annotated notes (Markdown), a findings digest, and open questions; store with project-level tags for recall.

### Validation & Quality Gates
- Notes include source/page anchors and keyword tags; duplicates merged.
- Minimum two passes completed with documented deltas between passes.
- INFERRED constraints resolved or explicitly flagged.
- Deliverables saved alongside README, examples, and references when available.

### Response Template
```
**Intent & Constraints**
- HARD: ...
- SOFT: ...
- INFERRED (confirm): ...

**Plan**
- Pass design and note schema.

**Findings & Evidence**
- Claim → evidence (page/link) → confidence ceiling.
- Gaps / follow-ups.

**Deliverables**
- Notes: <location>
- Digest: <summary bullets>

Confidence: 0.78 (ceiling: inference 0.70) - based on structured review of provided sources.
```

Confidence: 0.78 (ceiling: inference 0.70) - Template assumes structured reading completed with evidential anchors.
