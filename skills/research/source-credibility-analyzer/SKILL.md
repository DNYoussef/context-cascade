---
name: source-credibility-analyzer
description: Assess credibility, bias, and reliability of sources with explicit criteria and confidence ceilings.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
x-version: 3.2.0
x-category: research
x-vcl-compliance: v3.1.1
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

## STANDARD OPERATING PROCEDURE

### Purpose
- Evaluate sources before using them in research outputs.
- Make constraints and evidence explicit to avoid unvetted citations.
- Keep structure-first documentation aligned with skill-forge standards.

### Trigger Conditions
- **Positive:** screening papers/articles/web data for reliability; comparing conflicting sources.
- **Negative:** general synthesis (use `general-research-workflow`) or idea generation without sourcing.

### Guardrails
- Constraint buckets: HARD (recency, peer-review, provenance), SOFT (domain experts, diversity), INFERRED (author incentives) with sources.
- Two-pass evaluation: factual/provenance checks → epistemic/impact assessment.
- Confidence ceilings: observation 0.95 for verifiable facts; inference 0.70 for bias assessments.

### Inputs
- Source metadata (authors, venue, date, links).
- Research context and required quality thresholds.

### Workflow
1. **Scope & Constraints**: Record quality criteria and constraint buckets; confirm INFERRED motivations/risks.
2. **Provenance Check**: Validate authorship, venue, recency, and originality.
3. **Content Check**: Inspect methodology, data quality, reproducibility, and alignment to question.
4. **Bias & Risk Assessment**: Identify conflicts of interest, cherry-picking, or missing context.
5. **Score & Recommend**: Rate credibility with rationale and ceiling; recommend use/avoid/follow-up; store notes in references/examples.

### Validation & Quality Gates
- Evidence recorded for scores; conflicting indicators highlighted.
- Constraints respected; red flags noted.
- Confidence ceilings attached to each rating.

### Response Template
```
**Source & Context**
- ...

**Assessment**
- Provenance: ...
- Methodology: ...
- Bias/Risks: ...

**Rating**
- Credibility score + rationale + confidence ceiling.
- Recommendation: use / cautious / avoid.

Confidence: 0.82 (ceiling: inference 0.70) - based on evaluated criteria and evidence.
```

Confidence: 0.82 (ceiling: inference 0.70) - reflects completed checks with documented evidence.
