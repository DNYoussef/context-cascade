---
name: when-verifying-quality-use-verification-quality
description: Route verification and validation tasks to the verification-quality skill with clear constraints and evidence.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
x-version: 3.2.0
x-category: research
x-vcl-compliance: v3.1.1
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

## STANDARD OPERATING PROCEDURE

### Purpose
- Ensure quality verification (tests, metrics, acceptance gates) runs via `verification-quality` with constraint and confidence rigor.

### Trigger Conditions
- **Positive:** validating overall quality bars, regression checks, or release readiness for research artifacts.
- **Negative:** single bug reproduction (use functionality audit) or style-only feedback.

### Guardrails
- Constraints bucketed as HARD (quality bars, compliance), SOFT (target metrics), INFERRED (risk tolerance, rollback needs).
- Two-pass loop: scope/routing → epistemic validation of results.
- Findings require evidence and explicit ceilings.

### Inputs
- Artifact context, quality criteria, metrics, and test scope.

### Workflow
1. **Scope & Route**: Confirm verification need; record constraints and success criteria.
2. **Invoke Verification-Quality**: Provide metrics, thresholds, and environments.
3. **Validate Evidence**: Ensure results map to criteria with ceilings; note gaps.
4. **Summarize & Recommend**: Provide release/readiness decision, risks, and actions; store outputs.

### Validation & Quality Gates
- Constraints mapped to checks; INFERRED items flagged.
- Evidence tied to metrics/tests; ceilings aligned to evidence type.
- Clear pass/blockers and remediation plan.

### Response Template
```
**Routing**: Using verification-quality because ...
**Constraints**: HARD / SOFT / INFERRED.
**Results**: metric/test → outcome → confidence ceiling.
**Decision**: pass / conditional / block + risks + actions.

Confidence: 0.82 (ceiling: inference 0.70) - based on verification evidence.
```

Confidence: 0.82 (ceiling: inference 0.70) - reflects validated verification outcomes with evidence.
