# Observability - Quick Reference v2.1.0

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



## Purpose
Monitoring, logging, tracing, and alerting.

## Three Pillars

| Pillar | Tools |
|--------|-------|
| Metrics | Prometheus, Grafana |
| Logs | ELK, Loki |
| Traces | Jaeger, OpenTelemetry |

## Quick Commands

```bash
# Setup monitoring
Use observability metrics for: [service]

# Setup logging
Use observability logs for: [service]

# Setup tracing
Use observability traces for: [service]

# Create dashboard
Use observability dashboard for: [metrics]
```

## SLO Pattern

```yaml
SLI: Request latency p99
SLO: 99% < 200ms
Error Budget: 1% downtime/month
```

## Key Metrics

- Request rate (QPS)
- Error rate (%)
- Latency (p50, p95, p99)
- Saturation (CPU, memory)

## Best Practices

- Structured JSON logging
- Correlation IDs
- Alert on symptoms
- Define SLOs first

## Related Skills

- **infrastructure**
- **deployment-readiness**
- **performance-analysis**


---
*Promise: `<promise>QUICK_REFERENCE_VERIX_COMPLIANT</promise>`*
