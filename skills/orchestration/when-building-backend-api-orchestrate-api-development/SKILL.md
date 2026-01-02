---
name: when-building-backend-api-orchestrate-api-development
description: Orchestrate backend API development with staged planning, implementation, testing, and rollout guardrails.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
x-version: 3.2.0
x-category: orchestration
x-vcl-compliance: v3.2.0
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

## STANDARD OPERATING PROCEDURE

### Purpose
Coordinate backend API delivery—from design through deployment—with explicit constraints, validations, and confidence-aware approvals.

### Trigger Conditions
- **Positive:** new API design, contract changes, breaking-change reviews, rollout planning, dependency migrations, performance hardening.
- **Negative:** trivial doc edits, prompt-only tweaks (route to prompt-architect), or meta-skill creation (route to skill-forge).

### Guardrails
- **Skill-Forge structure-first:** keep `SKILL.md`, `examples/`, `tests/` maintained; add `resources/`/`references/` or log remediation tasks.
- **Prompt-Architect hygiene:** extract HARD/SOFT/INFERRED requirements (SLA, auth, compatibility), keep outputs in English, and publish ceilings for confidence.
- **API safety:** enforce contract tests, backward compatibility plans, schema validation, authz/authn, and rollback/canary strategies; registry-only agents and hook budgets apply.
- **Adversarial validation:** fuzz endpoints, run load and failure drills, and verify migration/rollback; capture evidence.
- **MCP tagging:** store API orchestration notes under WHO=`api-development-{session}` and WHY=`skill-execution`.

### Execution Playbook
1. **Intent & constraints:** define API purpose, SLAs, dependencies, and compliance; confirm inferred requirements.
2. **Design:** draft contracts, error models, and versioning; set compatibility and deprecation policy.
3. **Build & delegate:** assign roles for implementation, testing, and review; wire CI and linters.
4. **Safety nets:** plan migrations, feature flags, canaries, and rollback; guard secrets and quotas.
5. **Validation loop:** run contract, load, and security tests; simulate rollback; log evidence.
6. **Delivery:** summarize changes, validation, risks, and confidence ceiling.

### Output Format
- API intent, constraints, and contract summary.
- Deployment/rollback strategy, SLAs, and dependency impacts.
- Validation evidence (contract, load, security) and risks.
- **Confidence:** `X.XX (ceiling: TYPE Y.YY) - rationale`.

### Validation Checklist
- Structure-first assets present or ticketed; examples/tests aligned to current API.
- Contracts versioned; auth/perf/compatibility verified; registry and hook budgets confirmed.
- Adversarial/COV runs stored with MCP tags; confidence ceiling declared; English-only output.

### Completion Definition
API work is ready when contracts and tests pass, rollout/rollback are validated, risks are owned, and orchestration notes persist with MCP tags.

Confidence: 0.70 (ceiling: inference 0.70) - Backend API orchestration rewritten with skill-forge scaffolding and prompt-architect constraint/confidence rules.
