# Expertise Manager Quick Reference

## Purpose
Route requests to the right specialist, keep coverage maps healthy, and surface gaps before execution begins.

## Rapid Intake
1. Classify the request domain (e.g., ML build, ML debugging, system design, frontend, language).
2. Extract constraints: HARD / SOFT / INFERRED; confirm inferred constraints with the requester.
3. Check registry for matching skills and note missing docs or tests.

## Routing Matrix (Examples)
- **Implementation-heavy ML:** `ml-expert` (fallback: `ml`).
- **Training incidents/debug:** `ml-training-debugger` → `ml-expert` if code changes follow.
- **System design & capacity:** `system-design-architect`.
- **Frontend delivery:** `frontend-specialists` → `react-specialist` for React stacks.
- **Language-specific:** `language-specialists` → `python-specialist` or `typescript-specialist`.
- **Data layer:** `sql-database-specialist`.
- **Hook work:** `hook-creator`.

## Guardrails (Skill-Forge + Prompt-Architect)
- Structure-first: ensure each skill has `SKILL.md`, examples, tests, and resource docs.
- Adversarial validation: test ambiguous routing and overlapping ownership.
- Explicit confidence ceiling in every decision note.
- MCP tagging: `WHO=expertise-manager-{session}`, `WHY=skill-execution`.

## Decision Output Template
- Request summary and constraints.
- Assigned specialist(s) + backup + SLA.
- Validation notes (edge cases probed, missing docs flagged).
- Confidence: `X.XX (ceiling: TYPE Y.YY) - rationale`.

Confidence: 0.71 (ceiling: inference 0.70) - Quick reference rebuilt with the skill-forge routing and prompt-architect constraint format.
