---
name: research-driven-planning
description: Build plans anchored in research evidence, constraints, and validation gates.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
x-version: 3.2.0
x-category: research
x-vcl-compliance: v3.1.1
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

## STANDARD OPERATING PROCEDURE

### Purpose
- Create actionable plans whose milestones and decisions are backed by research evidence.
- Surface constraints explicitly and enforce confidence ceilings on recommendations.
- Maintain structure-first documentation for traceability.

### Trigger Conditions
- **Positive:** planning product/research work that must be evidence-based; prioritization aligned to findings.
- **Negative:** purely operational project planning (route to delivery skills) or ad-hoc brainstorming (`rapid-idea-generator`).

### Guardrails
- HARD / SOFT / INFERRED constraints captured with sources and ownership.
- Two-pass plan refinement: structure/milestones → epistemic validation against evidence and risks.
- Recommendations carry confidence ceilings; assumptions documented.

### Inputs
- Goal and desired outcomes; available evidence and gaps.
- Constraints (budget, time, compliance) and stakeholders.

### Workflow
1. **Frame & Evidence Audit**: Capture objectives, constraint buckets, and existing evidence; flag gaps.
2. **Plan Draft**: Define milestones, owners, dependencies, and validation checkpoints linked to evidence.
3. **Validation Pass**: Stress-test against constraints, risks, and evidence strength; adjust sequencing.
4. **Finalize & Communicate**: Produce plan summary, risks, and next steps; store in references/examples.

### Validation & Quality Gates
- Evidence mapped to milestones; gaps highlighted with follow-ups.
- Constraints addressed; INFERRED items assigned for confirmation.
- Confidence ceilings attached to recommendations.

### Response Template
```
**Goal & Constraints**
- HARD / SOFT / INFERRED.

**Plan**
- Milestones → evidence link → owner/checkpoint.

**Risks & Gaps**
- ...

**Next Steps**
- ...

Confidence: 0.80 (ceiling: inference 0.70) - based on evidence-backed planning.
```

Confidence: 0.80 (ceiling: inference 0.70) - reflects validated plan tied to evidence and constraints.
