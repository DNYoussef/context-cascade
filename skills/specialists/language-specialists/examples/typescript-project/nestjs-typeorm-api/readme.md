# Example: NestJS + TypeORM API

## Context
- Build a NestJS service using TypeORM with PostgreSQL.
- Constraints: Node 20, strict TS, migrations with rollback, p95 <120ms on key endpoints.

## Plan (Skill-Forge Aligned)
1. Capture HARD/SOFT/INFERRED constraints (modules, auth, caching, deployment target).
2. Configure strict tsconfig, eslint/prettier, and testing (jest + supertest); enable TypeORM migrations.
3. Implement modules/entities/DTOs with validation and error handling.
4. Add tests, health checks, metrics, and rollout/rollback docs.

## Deliverables
- NestJS project skeleton with TypeORM config and migrations.
- Tests and CI snippets.
- Operational notes (env vars, migration order, monitoring hooks).
- Confidence: 0.72 (ceiling: inference 0.70) - Built following prompt-architect constraint extraction and skill-forge validation steps.
