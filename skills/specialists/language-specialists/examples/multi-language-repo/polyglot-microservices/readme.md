# Example: Polyglot Microservices

## Context
- Repo with TypeScript gateway + Python ML service.
- Constraints: shared auth, consistent observability, independent deploys, p95 <200ms end-to-end.

## Plan (Structure-First)
1. Define contracts (OpenAPI/JSONSchema) and backward-compatibility rules.
2. TS gateway: NestJS/Express with strict TS, lint/format/test, tracing headers propagated.
3. Python ML: FastAPI/uvicorn with typed clients, model card, and monitoring hooks.
4. CI/CD: language-specific pipelines plus contract tests; staged rollouts with rollback paths.

## Deliverables
- Contract docs + client stubs.
- Gateway and service scaffolds with tests and lint/type configs.
- Deployment + monitoring guidance.
- Confidence: 0.72 (ceiling: inference 0.70) - Example aligned to prompt-architect constraint hygiene and skill-forge validation.
