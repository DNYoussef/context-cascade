---
name: deployment-readiness
description: Production deployment validation for Deep Research SOP Pipeline H ensuring models ready for real-world deployment. Use before deploying to production, creating deployment plans, or validating infrastructure requirements. Validates performance benchmarks, monitoring setup, incident response plans, rollback strategies, and infrastructure scalability for Quality Gate 3.
---

# Deployment Readiness

Validate ML models and systems for production deployment, ensuring operational readiness across performance, monitoring, security, and incident management dimensions.

## Liangci Kuangjia (Deployment Classification Framework)

### Deployment Type Classifiers

**FEATURE (xin gong-neng)** - New Functionality
- Risk: MEDIUM-HIGH
- Testing: Comprehensive E2E required
- Rollback: Feature flag toggle
- Monitoring: New metrics for feature usage
- Example: "New payment gateway integration"

**HOTFIX (jin-ji xiu-fu)** - Critical Bug Fix
- Risk: HIGH (expedited process)
- Testing: Focused regression on affected area
- Rollback: Immediate revert capability required
- Monitoring: Error rate alerts with 1-min interval
- Example: "Fix authentication bypass vulnerability"

**ROLLBACK (hui-gun)** - Revert to Previous Version
- Risk: LOW-MEDIUM (known good state)
- Testing: Smoke tests only
- Rollback: N/A (is rollback)
- Monitoring: Verify previous metrics restored
- Example: "Revert failed v2.3.0 deployment"

**CONFIG (pei-zhi)** - Configuration-Only Change
- Risk: LOW
- Testing: Config validation, no code changes
- Rollback: Config file revert
- Monitoring: Service health checks
- Example: "Update feature flag percentages"

**MIGRATION (qian-yi)** - Database/Infrastructure Migration
- Risk: CRITICAL
- Testing: Full backup, dry-run in staging
- Rollback: Migration rollback script required
- Monitoring: Database metrics, query performance
- Example: "Migrate PostgreSQL 15 to 16"

### Risk Level Classifiers

**HIGH (gao feng-xian)** - Breaking Changes
- Database migrations with data transformation
- Authentication/authorization changes
- Payment processing modifications
- Third-party API version upgrades
- Multi-service coordination required
- **Gate Requirement**: Manual approval + 24hr monitoring

**MEDIUM (zhong feng-xian)** - Standard Features
- New API endpoints (backward compatible)
- UI component updates
- Non-critical service additions
- Dependency minor version updates
- **Gate Requirement**: Automated tests + smoke tests

**LOW (di feng-xian)** - Minor Updates
- Documentation changes
- Logging improvements
- Configuration tweaks (non-breaking)
- UI copy changes
- **Gate Requirement**: Basic validation only

### Environment Progression Classifier

**DEV (kai-fa huan-jing)** - Development Environment
- Purpose: Rapid iteration, breaking changes allowed
- Deployment: Continuous (on every commit)
- Monitoring: Basic logs, no SLA
- Rollback: Not required

**STAGING (yan-zheng huan-jing)** - Staging Environment
- Purpose: Production-like validation
- Deployment: Daily or on-demand
- Monitoring: Full observability stack
- Rollback: Required, tested before prod
- **Gate**: Must pass ALL tests before prod promotion

**PRODUCTION (sheng-chan huan-jing)** - Production Environment
- Purpose: Live customer traffic
- Deployment: Scheduled windows only
- Monitoring: 24/7 alerting, SLA tracking
- Rollback: <5 min SLA, tested in staging
- **Gate**: Requires staging validation + approvals

### Deployment Strategy Classifier

**BLUE-GREEN (lan-lv bu-shu)** - Zero-Downtime Switch
- Two identical environments (blue=current, green=new)
- Traffic switch is instantaneous
- Rollback: Switch traffic back to blue
- Best for: HOTFIX, FEATURE with high confidence

**CANARY (jin-si-que bu-shu)** - Gradual Rollout
- Progressive traffic shift: 5% → 25% → 50% → 100%
- Monitor metrics at each stage
- Rollback: Reduce traffic to 0%
- Best for: FEATURE, MIGRATION with uncertainty

**ROLLING (gun-dong bu-shu)** - Instance-by-Instance Update
- Update instances sequentially
- Maintain minimum capacity during update
- Rollback: Reverse instance updates
- Best for: CONFIG, low-risk FEATURE

**BIG-BANG (yi-ci-xing bu-shu)** - All-at-Once Deployment
- Replace all instances simultaneously
- Downtime window required
- Rollback: Full redeployment of previous version
- Best for: MIGRATION (database), scheduled maintenance

### Classification Decision Matrix

```yaml
deployment_classification:
  type: FEATURE
  risk: HIGH
  environments:
    - DEV [SV:RAZVERNUTO]
    - STAGING [NSV:TESTIRUYETSYA]
    - PRODUCTION [OZHIDAET]
  strategy: CANARY
  rollback_plan: blue-green-fallback
  monitoring:
    - error_rate: <5% threshold
    - latency_p95: <200ms threshold
    - saturation: <80% threshold
  gates_passed:
    - tests: [SV:PROVERENO] 100% pass
    - security: [SV:ODOBRENO] zero critical issues
    - performance: [NSV:VYPOLNYAETSYA] benchmarking in progress
```

### Output Template: Deployment Classification Report

```markdown
# Deployment Classification Report

**Deployment ID**: DEPLOY-2025-12-19-001
**Timestamp**: 2025-12-19T14:32:00Z
**Requested By**: platform-team

## Classification

- **Type**: FEATURE (xin gong-neng) - Payment gateway v2
- **Risk Level**: HIGH (gao feng-xian) - Third-party API integration
- **Strategy**: CANARY (jin-si-que bu-shu) - 5% → 25% → 50% → 100%
- **Environment**: STAGING (yan-zheng huan-jing) → PRODUCTION (sheng-chan huan-jing)

## State Tracking

### Infrastructure [SV:ZAVERSHENO]
- Capacity Planning: [SV:ZAVERSHENO] ✓
- Environment Setup: [SV:ZAVERSHENO] ✓
- Load Balancer Config: [SV:PROVERENO] ✓

### Testing [NSV:VYPOLNYAETSYA]
- Unit Tests: [SV:PROVERENO] 100% pass ✓
- Integration Tests: [NSV:VYPOLNYAETSYA] 87/100 pass (in progress)
- Load Tests: [OZHIDAET] (blocked by integration tests)

### Deployment Gates
- Gate 1 (Security): [SV:ODOBRENO] ✓
- Gate 2 (Performance): [NSV:TESTIRUYETSYA] (pending load tests)
- Gate 3 (Approval): [OZHIDAET] (requires Gate 2)

## Rollback Plan

- **Strategy**: Blue-Green fallback
- **RTO**: <5 minutes
- **Procedure**: `kubectl patch service payment-gateway -p '{"spec":{"selector":{"version":"blue"}}}'`
- **Validation**: [SV:PROVERENO] tested in staging

## Risk Mitigation

- **HIGH Risk Items**:
  - Payment processing: Feature flag at 5% initial rollout
  - Database migration: Separate deployment, tested with prod-like data
  - Third-party API: Circuit breaker configured (timeout: 3s, failure threshold: 5)

- **Monitoring Alerts**:
  - Payment failure rate >2%: Auto-rollback
  - API latency p95 >500ms: Alert + manual review
  - Error spike >10x baseline: Auto-rollback

## Recommendation

**Status**: [ZABLOKIROVANO] - DO NOT DEPLOY
**Reason**: Integration tests incomplete (87/100), load tests not started
**Next Steps**:
1. Complete integration tests → [SV:PROVERENO]
2. Run load tests → [SV:PROVERENO]
3. Gate 2 approval → [SV:ODOBRENO]
4. Schedule deployment window (Tuesday 10am-12pm)
```

## Quick Start

### 1. Infrastructure Requirements
```yaml
# deployment/infrastructure_requirements.yaml

compute:
  gpu:
    type: "NVIDIA A100"
    count: 2
    memory: "80GB each"
  cpu:
    cores: 32
    memory: "256GB"

storage:
  model_weights: "50GB"
  datasets: "500GB"
  logs: "100GB"

network:
  ingress_bandwidth: "10Gbps"
  egress_bandwidth: "10Gbps"
  latency_target: "<100ms p95"

scalability:
  min_instances: 2
  max_instances: 10
  autoscaling_metric: "requests_per_second"
  target_utilization: 70%
```

### 2. Performance Benchmarking
```bash
# Benchmark in production environment
python scripts/production_benchmarks.py \
  --model deployment/model.pth \
  --environment production \
  --metrics "latency,throughput,memory,cpu" \
  --duration 3600 \
  --output deployment/benchmarks.json
```

### 3. Monitoring Setup
```bash
# Deploy monitoring stack (Prometheus + Grafana)
docker-compose -f deployment/monitoring/docker-compose.yml up -d

# Configure alerts
kubectl apply -f deployment/monitoring/alerts.yaml

# Test alert pipeline
python scripts/test_alerts.py --alert-manager http://localhost:9093
```

### 4. Deployment Plan
```bash
# Generate deployment plan
python scripts/generate_deployment_plan.py \
  --model deployment/model.pth \
  --infrastructure deployment/infrastructure_requirements.yaml \
  --output deployment/deployment_plan.md
```

### 5. Validate Deployment Readiness
```bash
# Run comprehensive readiness checks
python scripts/validate_deployment_readiness.py \
  --deployment-plan deployment/deployment_plan.md \
  --benchmarks deployment/benchmarks.json \
  --monitoring-config deployment/monitoring/ \
  --output deployment/readiness_report.md
```

#### 1.2 Environment Setup
```bash
# Setup production environment
# Using Kubernetes for orchestration

# 1. Create namespace
kubectl create namespace ml-production

# 2. Deploy model serving (TorchServe, TensorFlow Serving, or custom)
kubectl apply -f deployment/kubernetes/model-serving.yaml

# 3. Deploy load balancer
kubectl apply -f deployment/kubernetes/load-balancer.yaml

# 4. Verify deployment
kubectl get pods -n ml-production
kubectl get services -n ml-production
```

**Deliverable**: Production environment deployed

#### 2.2 Throughput Benchmarking
```python
# scripts/benchmark_throughput.py

def benchmark_throughput(model, duration_seconds=3600):
    """Benchmark queries per second (QPS)."""
    start_time = time.time()
    requests_processed = 0

    while time.time() - start_time < duration_seconds:
        # Simulate request
        output = model(test_input)
        requests_processed += 1

    elapsed = time.time() - start_time
    qps = requests_processed / elapsed

    print(f"Throughput: {qps:.2f} QPS")

    # Check against target (e.g., 100 QPS)
    target_qps = 100.0
    if qps < target_qps:
        print(f"⚠️  WARNING: Throughput {qps:.2f} QPS below target {target_qps}")
        return False
    else:
        print(f"✅ PASS: Throughput {qps:.2f} QPS meets target")
        return True

# Run benchmark
benchmark_throughput(model)
```

**Deliverable**: Throughput benchmarks

### Phase 3: Monitoring & Observability (2-3 days)

**Objective**: Set up comprehensive monitoring

**Steps**:

#### 3.1 Metrics Collection
```yaml
# deployment/monitoring/prometheus.yml

global:
  scrape_interval: 15s
  evaluation_interval: 15s

scrape_configs:
  - job_name: 'model-serving'
    static_configs:
      - targets: ['model-serving:8080']

  - job_name: 'node-exporter'
    static_configs:
      - targets: ['node-exporter:9100']

  - job_name: 'gpu-exporter'
    static_configs:
      - targets: ['dcgm-exporter:9400']
```

**Key Metrics**:
- **Inference Metrics**: Latency (P50, P95, P99), throughput (QPS), error rate
- **Resource Metrics**: GPU utilization, CPU utilization, memory usage
- **Business Metrics**: Requests per user, predictions per day, model drift

#### 3.3 Dashboards
```json
// deployment/monitoring/grafana_dashboard.json

{
  "dashboard": {
    "title": "ML Model Production Monitoring",
    "panels": [
      {
        "title": "Inference Latency (P95)",
        "targets": [
          {
            "expr": "histogram_quantile(0.95, rate(inference_duration_seconds_bucket[5m]))"
          }
        ]
      },
      {
        "title": "Requests Per Second",
        "targets": [
          {
            "expr": "rate(inference_requests_total[1m])"
          }
        ]
      },
      {
        "title": "Error Rate",
        "targets": [
          {
            "expr": "rate(inference_errors_total[5m]) / rate(inference_requests_total[5m])"
          }
        ]
      },
      {
        "title": "GPU Utilization",
        "targets": [
          {
            "expr": "DCGM_FI_DEV_GPU_UTIL"
          }
        ]
      }
    ]
  }
}
```

**Deliverable**: Monitoring dashboards

#### 4.2 Rollback Strategy
```bash
# deployment/rollback.sh

#!/bin/bash
set -e

# Rollback strategy: Blue-Green Deployment

echo "Starting rollback to previous version..."

# 1. Verify previous version exists
if [ ! -f "deployment/previous_version.yaml" ]; then
    echo "ERROR: Previous version not found"
    exit 1
fi

# 2. Deploy previous version (green)
kubectl apply -f deployment/previous_version.yaml

# 3. Wait for deployment to be ready
kubectl wait --for=condition=available --timeout=300s deployment/model-serving-green

# 4. Switch traffic to green (previous version)
kubectl patch service model-serving -p '{"spec":{"selector":{"version":"green"}}}'

# 5. Verify rollback successful
python scripts/verify_deployment.py --expected-version green

# 6. Terminate blue (failed version)
kubectl delete deployment model-serving-blue

echo "✅ Rollback completed successfully"
```

**Deliverable**: Rollback strategy

### Phase 6: Documentation (1-2 days)

**Objective**: Document deployment procedures

**Deliverables**:

#### 6.1 Deployment Checklist
```markdown
# Deployment Checklist

## Pre-Deployment
- [ ] Model trained and Gate 2 APPROVED
- [ ] Reproducibility audit passed
- [ ] Performance benchmarks meet SLA
- [ ] Monitoring configured and tested
- [ ] Alerts configured and tested
- [ ] Incident response plan documented
- [ ] Rollback strategy tested
- [ ] Security validation passed

## Deployment
- [ ] Deploy to staging environment
- [ ] Run smoke tests in staging
- [ ] Deploy to production (canary or blue-green)
- [ ] Monitor metrics for 24 hours
- [ ] Gradually ramp traffic (10% → 50% → 100%)

## Post-Deployment
- [ ] Verify all metrics within SLA
- [ ] Check error logs
- [ ] Confirm alerts working
- [ ] Update documentation
- [ ] Notify stakeholders
```

#### 6.2 Operations Manual
- Deployment procedures
- Scaling procedures
- Monitoring procedures
- Troubleshooting guide
- Runbooks for common issues

**Deliverable**: Complete deployment documentation

## Troubleshooting

### Issue: High latency (>100ms P95)
**Solution**: Scale up instances, optimize model (quantization, pruning), use faster hardware

### Issue: Low throughput (<100 QPS)
**Solution**: Increase batch size, use model parallelism, optimize data loading

### Issue: Gate 3 validation fails
**Solution**: Ensure all deployment readiness criteria met (performance, monitoring, incident response)

## References

### Deployment Best Practices
- Google SRE Handbook
- AWS Well-Architected Framework
- Kubernetes Best Practices

### Monitoring Standards
- Prometheus Best Practices
- OpenTelemetry
- The Four Golden Signals (Latency, Traffic, Errors, Saturation)

## Core Principles

Deployment Readiness operates on 3 fundamental principles:

### Principle 1: Production Performance Differs From Development
Models that run fast on development machines (1 GPU, synthetic data, no network latency) often fail performance SLAs in production (shared GPUs, real data volumes, network overhead). Benchmarking in production-like environments is non-negotiable.

In practice:
- Benchmark on production hardware (same GPU type, same instance size)
- Use production data volumes (1M records, not 1000)
- Simulate production network latency and concurrent requests

### Principle 2: Monitoring Precedes Deployment
Deploying without monitoring is deploying blind - you won't know when failures occur or what caused them. Monitoring infrastructure (metrics, logs, alerts) must be operational BEFORE first production request.

In practice:
- Prometheus + Grafana deployed and configured before model deployment
- Alerts tested by triggering synthetic failures (kill pod, inject latency)
- Dashboards validated with realistic load (not just healthy system metrics)

### Principle 3: Rollback Speed Determines Incident Impact
The difference between a 5-minute incident and a 4-hour incident is rollback readiness. Blue-green deployments enable instant traffic switching to previous version without debugging failed deployment.

In practice:
- Blue-green deployment: Both versions running, instant traffic switch
- Rollback tested in staging (verify <5 minute rollback time)
- Rollback decision criteria defined before deployment (error rate >5%, latency >200ms P95)

## Common Anti-Patterns

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| **"Works On My Machine"** | Model runs fast on developer laptop (local GPU, no network calls, synthetic data). Production deployment has 10x higher latency due to shared GPUs and real data volumes. | Benchmark in production environment with production hardware, data volumes, and network conditions. Validate P95 latency <100ms with 100 QPS load. |
| **"We'll Add Monitoring Later"** | Deploy model without metrics/alerts. Production issue discovered by user complaints after 2 hours of degraded performance. | Deploy monitoring stack BEFORE model deployment. Test alerts by killing pods or injecting latency. Verify alerts fire within 2 minutes of synthetic failures. |
| **"Hotfix In Production"** | Deployment fails, team debugs in production. 4 hours later, issue identified but requires code changes. No way to revert to previous working version. | Document and TEST rollback procedure in staging. Blue-green deployment enables instant traffic switch to previous version. Rollback first, debug later. |

## Conclusion

Deployment Readiness provides systematic validation that ML models and systems are operationally ready for production deployment. The skill coordinates performance benchmarking, monitoring setup, incident response planning, and rollback testing across production-like environments.

Use this skill as Quality Gate 3 in the Deep Research SOP pipeline, or as the final validation before any production ML deployment. The 1-2 week investment in deployment readiness prevents weeks of incident response and emergency fixes - 90% of production ML failures stem from inadequate operational readiness, not model accuracy.

The framework enforces three critical validations: production performance benchmarks (not development machine performance), monitoring infrastructure operational before deployment (not added reactively after incidents), and tested rollback procedures (not improvised during outages). These validations are often skipped under deadline pressure, creating technical debt that manifests as extended production incidents.

Success requires treating deployment readiness as non-negotiable - partial passes are failures. The difference between reliable ML systems and incident-prone systems is operational discipline, not model sophistication. This skill ensures operational readiness meets the same rigorous standards as model accuracy.