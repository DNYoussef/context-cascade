# Quick Reference: Research Observability

- **Triggers:** need telemetry/monitoring for experiments, data pipelines, or research services; drift or regression detection; reproducibility evidence.
- **Constraints:** bucket HARD (privacy, compliance, budgets), SOFT (preferred tools, dashboards), INFERRED (ownership, retention) and confirm them.
- **Workflow:**
  1. Scope goals and SLIs/SLOs.
  2. Design signals, sampling, and tagging.
  3. Implement exporters/collectors and run smoke/data-quality tests.
  4. Build dashboards + alerts with runbooks.
  5. Review coverage, noise, and ownership; iterate.
- **Quality Gates:** mapped signals-to-questions, privacy respected, alert noise acceptable, evidence stored with confidence ceilings.
- **Output Template:** scope/constraints → signals/plan → validation → gaps with **Confidence: X.XX (ceiling: TYPE Y.YY)**.
