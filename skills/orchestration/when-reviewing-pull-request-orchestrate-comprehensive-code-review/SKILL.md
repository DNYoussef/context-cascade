---
name: when-reviewing-pull-request-orchestrate-comprehensive-code-review
description: Orchestrate multi-agent code reviews with structured prompts, safety checks, and evidence-backed approvals.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
x-version: 3.2.0
x-category: orchestration
x-vcl-compliance: v3.2.0
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

## STANDARD OPERATING PROCEDURE

### Purpose
Coordinate comprehensive PR reviews using specialized reviewers (security, performance, correctness) with explicit constraints and confidence ceilings.

### Trigger Conditions
- **Positive:** PR triage, deep reviews, risky changes, release blockers, compliance-sensitive diffs, regression prevention.
- **Negative:** trivial cosmetic changes, prompt-only edits (route to prompt-architect), or new skill weaving (route to skill-forge).

### Guardrails
- **Skill-Forge structure-first:** keep `SKILL.md`, `examples/`, `tests/` updated; add `resources/`/`references/` or log remediation tasks.
- **Prompt-Architect hygiene:** capture HARD/SOFT/INFERRED constraints (test expectations, risk areas), maintain English-only outputs, and state ceilings.
- **Review safety:** enforce registry agents, require test evidence, check security/performance impacts, and set rollback/mitigation paths; honor hook latency budgets.
- **Adversarial validation:** request failing test reproduction, fuzz risky areas, and cross-check with baselines; capture evidence.
- **MCP tagging:** store review records with WHO=`code-review-orchestration-{session}` and WHY=`skill-execution`.

### Execution Playbook
1. **Intent & scope:** read PR context, risks, and constraints; confirm inferred requirements.
2. **Reviewer roster:** assign specialized reviewers, timeboxes, and acceptance criteria.
3. **Review rounds:** gather findings, adversarial checks, and evidence; track TodoWrite actions.
4. **Resolution:** consolidate feedback, request fixes, retest, and decide approve/block.
5. **Validation loop:** ensure tests and mitigations pass; record telemetry and deltas.
6. **Delivery:** present decision, evidence, residual risks, and confidence ceiling.

### Output Format
- PR summary, risk areas, and constraints.
- Reviewer roles, findings, and evidence.
- Required fixes/tests, mitigations, and decision.
- **Confidence:** `X.XX (ceiling: TYPE Y.YY) - rationale`.

### Validation Checklist
- Structure-first assets present or ticketed; examples/tests aligned to review outcomes.
- Tests/security/performance checks executed; registry and hooks validated.
- Adversarial/COV runs stored with MCP tags; confidence ceiling declared; English-only output.

### Completion Definition
Review is complete when findings are resolved or accepted, evidence is stored, risks are owned, and decision plus confidence ceiling are documented with MCP tags.

Confidence: 0.70 (ceiling: inference 0.70) - Code-review orchestration rewritten with skill-forge scaffolding and prompt-architect constraint/confidence rules.
