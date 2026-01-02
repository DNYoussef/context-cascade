---
name: rapid-manuscript-drafter
description: Draft research manuscripts quickly with structured sections, evidence links, and confidence ceilings.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
x-version: 3.2.0
x-category: research
x-vcl-compliance: v3.1.1
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

## STANDARD OPERATING PROCEDURE

### Purpose
- Produce rapid, coherent research manuscript drafts while preserving evidential integrity.
- Enforce constraint clarity (venue, length, style) and explicit ceilings on claims.
- Keep structure-first artifacts ready for iteration and review.

### Trigger Conditions
- **Positive:** first-pass manuscripts, section rewrites, or structured outlines.
- **Negative:** final camera-ready polishing (use publication skills) or prompt-only edits (`prompt-architect`).

### Guardrails
- Bucket constraints: HARD (venue format, length, deadlines), SOFT (tone, emphasis), INFERRED (reviewer expectations) with sources.
- Two-pass drafting: outline/structure → evidence and epistemic validation.
- All claims tie to evidence; ceilings reflect evidence type.

### Inputs
- Target venue/template, key findings, figures/tables, references.
- Audience and novelty/impact story.

### Workflow
1. **Frame & Constraints**: Capture venue rules, deadlines, and required sections; confirm INFERRED reviewer needs.
2. **Outline Pass**: Build section-by-section outline with thesis and contributions.
3. **Draft Pass**: Fill sections with claims linked to evidence, figures, and references; enforce clarity.
4. **Validation Pass**: Check constraints (length/style), evidence coverage, and confidence ceilings; remove overclaims.
5. **Package**: Provide draft, change log, and next edits; store alongside README/examples.

### Validation & Quality Gates
- Outline and draft both completed; deltas captured between passes.
- Claims cite evidence and include ceilings.
- Formatting and length conform to venue constraints.

### Response Template
```
**Constraints**
- HARD / SOFT / INFERRED.

**Outline Snapshot**
- ...

**Draft Status**
- Sections completed, evidence links, gaps.

**Risks / Next Edits**
- ...

Confidence: 0.79 (ceiling: inference 0.70) - based on drafted sections and evidence links.
```

Confidence: 0.79 (ceiling: inference 0.70) - reflects completed passes with cited evidence.
