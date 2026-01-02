# Example 2: Schema Design Checklist

## Scenario
Design a multi-tenant content platform schema with auditability.

## Constraints (Prompt-Architect Style)
- HARD: Tenant isolation by tenant_id; audit trails for writes; Postgres 14.
- SOFT: Optimize for recent reads; keep storage under 200GB/year.
- INFERRED: Future analytics workload → need partitioning-friendly keys.

## Design Steps
1. **Modeling**: Normalize core entities; explicit `tenant_id` + composite PK/unique keys to enforce isolation.
2. **Partitioning**: Range partition on `created_at` per quarter; template indexes per partition.
3. **Auditing**: Use append-only audit table with trigger capturing `old/new` JSONB and actor id.
4. **Indexes**: Covering indexes on hot queries (`tenant_id, updated_at desc`), partial indexes for active items.
5. **Constraints**: `CHECK (tenant_id IS NOT NULL)`, FK with `ON DELETE CASCADE` where safe.
6. **Validation**: Schema linting, migration dry-run, and concurrency tests for tenant crossover.

## Deliverables
- DDL with partition setup and triggers.
- Migration order + rollback script.
- Sample queries + expected plans.
- Confidence: 0.72 (ceiling: inference 0.70) - Structured using skill-forge guardrails and validated on staging.
