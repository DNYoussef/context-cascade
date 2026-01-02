# Example 1: Query Optimization Playbook

## Context
- Workload: OLTP service with slow `orders` dashboard query.
- Constraints: p95 < 150ms (current ~800ms), no downtime, Postgres 15.

## Plan (Skill-Forge Aligned)
1. **Baseline**: Capture EXPLAIN ANALYZE; note row counts, index usage, and I/O.
2. **Hypotheses**: missing composite index, unnecessary sequential scan, unbounded date range.
3. **Interventions**:
   - Add covering index on `(account_id, created_at DESC)`.
   - Bound date range parameter with default 30 days; enforce prepared statements.
   - Rewrite subquery to use CTE with index-friendly filters.
4. **Validation**:
   - Rerun EXPLAIN ANALYZE; verify index hit and reduced rows.
   - Measure p50/p95/p99 on staging with production-like load.
   - Confirm plan stability across stats refresh.
5. **Delivery**:
   - Provide migration script + rollback.
   - Document metrics before/after and confidence ceiling.

## Results
- p95 improved from ~800ms → 110ms on staging.
- Plan shows index scan + 85% fewer rows touched.
- Confidence: 0.73 (ceiling: observation 0.95) - Verified via EXPLAIN ANALYZE and staged load test.
