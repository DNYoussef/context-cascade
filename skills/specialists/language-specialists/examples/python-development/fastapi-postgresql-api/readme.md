# Example: FastAPI + PostgreSQL Service

## Context
- Build a FastAPI service with PostgreSQL backing store and JWT auth.
- Constraints: Python 3.11, p95 latency <150ms, migrations with rollback, lint/format/type/test required.

## Plan (Prompt-Architect + Skill-Forge)
1. Capture HARD/SOFT/INFERRED constraints (SLOs, auth, ORM choice, deployment target).
2. Scaffold FastAPI with async SQLAlchemy + Alembic migrations; enforce `ruff + black + mypy + pytest`.
3. Implement routes, schema validation (pydantic), and DB layer with prepared statements.
4. Add tests (unit + integration), CI job matrix, and rollout/rollback notes.

## Deliverables
- Service skeleton + Alembic migrations.
- Test suite and CI config snippets.
- Operations notes (env vars, health checks, monitoring hooks).
- Confidence: 0.73 (ceiling: inference 0.70) - Validated on local/staging with lint/type/test green.
