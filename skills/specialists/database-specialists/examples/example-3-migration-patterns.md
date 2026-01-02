# Example 3: Safe Migration Pattern

## Scenario
Zero-downtime column type change (VARCHAR → TEXT) on a high-traffic table.

## Pattern (Structure-First)
1. **Preparation**
   - Back up table; capture baseline metrics (lock wait, latency, error rate).
   - Add nullable shadow column `new_text TEXT`.
2. **Backfill**
   - Batch copy data with chunking and sleep; monitor locks.
   - Verify row counts and checksums between columns.
3. **Dual-Write Window**
   - Update application to write both columns; add constraint validation job.
4. **Cutover**
   - Swap reads to `new_text`; drop old constraint-dependent objects.
   - Rename columns (`old`→`backup`, `new_text`→original name) with transactional script.
5. **Cleanup**
   - Remove backup column after stable period; update indexes.
6. **Validation**
   - Regression tests, plan checks, and rollback script ready.

## Outputs
- Migration + rollback scripts with timing guidance.
- Monitoring checklist (locks, replication lag, errors).
- Confidence: 0.73 (ceiling: inference 0.70) - Based on staged rehearsal using skill-forge validation steps.
