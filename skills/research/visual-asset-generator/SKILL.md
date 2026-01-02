---
name: visual-asset-generator
description: Generate research visuals (figures, diagrams) with constraints, evidence alignment, and confidence ceilings.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
x-version: 3.2.0
x-category: research
x-vcl-compliance: v3.1.1
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

## STANDARD OPERATING PROCEDURE

### Purpose
- Produce visual assets that accurately reflect research findings and constraints.
- Apply constraint hygiene and explicit ceilings to avoid misrepresentation.
- Maintain structure-first documentation for reproducibility.

### Trigger Conditions
- **Positive:** requests for figures, diagrams, charts, or schematics tied to research outputs.
- **Negative:** purely aesthetic design work unrelated to research; or text-only summaries.

### Guardrails
- Constraints bucketed: HARD (data accuracy, confidentiality, formats), SOFT (style preferences), INFERRED (audience literacy).
- Two-pass loop: draft visual plan → validate against evidence and constraints.
- Explicitly cite data sources and uncertainty; include confidence ceilings where interpretation is inferred.

### Inputs
- Goal of the visual, target audience, and format requirements.
- Data/metrics to visualize and source locations.
- Style guidance and accessibility needs.

### Workflow
1. **Scope & Constraints**: Capture objectives and constraint buckets; confirm INFERRED assumptions.
2. **Design Plan**: Choose visual types, annotations, and data mappings; check feasibility.
3. **Create Draft**: Build the asset with labeled data sources and units.
4. **Validate**: Verify data accuracy, legends, accessibility, and confidentiality; apply ceilings to interpretive statements.
5. **Deliver & Store**: Provide assets, source files, and usage notes; update references/examples.

### Validation & Quality Gates
- Data sources cited; transformations documented.
- Visual readable and accessible; constraints respected.
- Interpretations include confidence ceilings.

### Response Template
```
**Goal & Constraints**
- HARD / SOFT / INFERRED.

**Design**
- Visual type, data sources, annotations.

**Validation**
- Accuracy checks, accessibility, risks.

**Deliverables**
- Asset paths, source files, usage notes.

Confidence: 0.80 (ceiling: research 0.85) - based on validated visuals and data checks.
```

Confidence: 0.80 (ceiling: research 0.85) - reflects validated visual assets tied to evidence.
