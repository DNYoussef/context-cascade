# Observability (Research)

Instrument research experiments and data pipelines with clear SLIs, telemetry, and validation gates. Uses skill-forge’s structure-first approach and prompt-architect’s constraint/confidence hygiene.

## Steps
1. Define observability goals and HARD / SOFT / INFERRED constraints (privacy, cost, performance).
2. Choose signals (logs, metrics, traces), tagging, sampling, and budgets.
3. Implement exporters/collectors; run smoke tests and data-quality checks.
4. Build dashboards and alerts with runbooks.
5. Review coverage, tune noise, and store artifacts.

## Deliverables
- Instrumentation plan and implemented config
- Dashboards/alerts with owners and runbooks
- Coverage notes with confidence ceilings

Confidence: 0.84 (ceiling: observation 0.95) - based on validated telemetry and dashboards.
