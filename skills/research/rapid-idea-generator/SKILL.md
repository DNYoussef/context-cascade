---
name: rapid-idea-generator
description: Quickly generate and triage research ideas with constraint clarity and confidence ceilings.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
x-version: 3.2.0
x-category: research
x-vcl-compliance: v3.1.1
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

## STANDARD OPERATING PROCEDURE

### Purpose
- Produce a set of research ideas aligned to constraints and evaluation criteria.
- Apply prompt-architect constraint extraction and explicit ceilings to each idea.
- Keep structure-first artifacts for reuse and follow-up.

### Trigger Conditions
- **Positive:** brainstorming research directions, generating project briefs, seeding backlogs.
- **Negative:** detailed execution planning (use `interactive-planner`) or prompt-only refinement.

### Guardrails
- HARD / SOFT / INFERRED constraints (domains, data access, compute, timelines) captured upfront.
- Two-pass loop: initial ideation breadth → filter/refine with feasibility and evidence.
- Confidence ceilings for feasibility/impact claims; do not oversell speculation.

### Inputs
- Goal statement and evaluation criteria (impact, novelty, feasibility).
- Constraints and exclusions.
- Timebox and output format.

### Workflow
1. **Frame & Constraints**: Record goals and constraint buckets; confirm INFERRED items.
2. **Generate Broad Set**: Produce diverse ideas respecting HARD constraints.
3. **Refine & Score**: Apply feasibility/impact/novelty scores with rationale and ceilings.
4. **Select & Next Steps**: Recommend top options with immediate actions and risks.
5. **Store Artifacts**: Save idea list and scoring for reuse; update examples/references if patterns emerge.

### Validation & Quality Gates
- Ideas respect HARD constraints; SOFT preferences reflected.
- Rationale and confidence ceilings provided for scores.
- Top picks include next steps and risks.

### Response Template
```
**Constraints**
- HARD / SOFT / INFERRED.

**Ideas (scorecards)**
- Idea → impact/feasibility/novelty + rationale + confidence ceiling.

**Top Picks & Next Steps**
- ...

Confidence: 0.77 (ceiling: inference 0.70) - based on structured generation and scoring.
```

Confidence: 0.77 (ceiling: inference 0.70) - reflects ideation validated against constraints.
