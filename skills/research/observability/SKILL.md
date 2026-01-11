/*============================================================================*/
/* OBSERVABILITY SKILL :: VERILINGUA x VERIX EDITION                      */
/*============================================================================*/

---
name: observability
version: 2.1.0
description: |
  [assert|neutral] Observability specialists hub for monitoring, logging, tracing, and alerting. Routes to specialists for metrics collection, log aggregation, distributed tracing, and incident response. Use for system  [ground:given] [conf:0.95] [state:confirmed]
category: research
tags:
- general
author: system
cognitive_frame:
  primary: evidential
  goal_analysis:
    first_order: "Execute observability workflow"
    second_order: "Ensure quality and consistency"
    third_order: "Enable systematic research processes"
---

/*----------------------------------------------------------------------------*/
/* S0 META-IDENTITY                                                            */
/*----------------------------------------------------------------------------*/

[define|neutral] SKILL := {
  name: "observability",
  category: "research",
  version: "2.1.0",
  layer: L1
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S1 COGNITIVE FRAME                                                          */
/*----------------------------------------------------------------------------*/

[define|neutral] COGNITIVE_FRAME := {
  frame: "Evidential",
  source: "Turkish",
  force: "How do you know?"
} [ground:cognitive-science] [conf:0.92] [state:confirmed]

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.

/*----------------------------------------------------------------------------*/
/* S2 TRIGGER CONDITIONS                                                       */
/*----------------------------------------------------------------------------*/

[define|neutral] TRIGGER_POSITIVE := {
  keywords: ["observability", "research", "workflow"],
  context: "user needs observability capability"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S3 CORE CONTENT                                                             */
/*----------------------------------------------------------------------------*/

# Observability

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



Central hub for monitoring, logging, tracing, and system observability.

## Phase 0: Expertise Loading

```yaml
expertise_check:
  domain: observability
  file: .claude/expertise/observability.yaml

  if_exists:
    - Load monitoring patterns
    - Load alerting rules
    - Apply SLO definitions

  if_not_exists:
    - Flag discovery mode
    - Document patterns learned
```

## When to Use This Skill

Use observability when:
- Setting up monitoring infrastructure
- Implementing logging strategies
- Configuring distributed tracing
- Creating dashboards and alerts
- Debugging production issues

## Observability Pillars

| Pillar | Purpose |
|--------|---------|
| Metrics | Quantitative measurements |
| Logs | Event records |
| Traces | Request flow tracking |
| Alerts | Incident notification |

## Tool Ecosystem

### Metrics
```yaml
tools:
  - Prometheus
  - Grafana
  - Datadog
  - CloudWatch
metrics_types:
  - Counters
  - Gauges
  - Histograms
  - Summaries
```

### Logging
```yaml
tools:
  - ELK Stack (Elasticsearch, Logstash, Kibana)
  - Loki
  - Splunk
  - CloudWatch Logs
patterns:
  - Structured logging (JSON)
  - Log levels
  - Correlation IDs
```

### Tracing
```yaml
tools:
  - Jaeger
  - Zipkin
  - OpenTelemetry
  - X-Ray
patterns:
  - Span context propagation
  - Baggage items
  - Sampling strategies
```

## SLO/SLI/SLA

```yaml
definitions:
  SLI: "Service Level Indicator - measurable metric"
  SLO: "Service Level Objective - target value"
  SLA: "Service Level Agreement - contractual commitment"

example:
  SLI: "Request latency p99"
  SLO: "99% of requests < 200ms"
  SLA: "99.9% availability per month"
```

## MCP Requirements

- **claude-flow**: For orchestration
- **Bash**: For tool CLI commands

## Recursive Improvement Integration (v2.1)

### Eval Harness Integration

```yaml
benchmark: observability-benchmark-v1
  tests:
    - obs-001: Monitoring coverage
    - obs-002: Alert quality
  minimum_scores:
    monitoring_coverage: 0.85
    alert_quality: 0.80
```

### Memory Namespace

```yaml
namespaces:
  - observability/configs/{id}: Monitoring configs
  - observability/dashboards: Dashboard templates
  - improvement/audits/observability: Skill audits
```

### Uncertainty Handling

```yaml
confidence_check:
  if confidence >= 0.8:
    - Proceed with implementation
  if confidence 0.5-0.8:
    - Confirm tool stack
  if confidence < 0.5:
    - Ask for infrastructure details
```

### Cross-Skill Coordination

Works with: **infrastructure**, **deployment-readiness**, **performance-analysis**

---

## !! SKILL COMPLETION VERIFICATION (MANDATORY) !!

- [ ] **Agent Spawning**: Spawned agent via Task()
- [ ] **Agent Registry Validation**: Agent from registry
- [ ] **TodoWrite Called**: Called with 5+ todos
- [ ] **Work Delegation**: Delegated to agents

**Remember: Skill() -> Task() -> TodoWrite() - ALWAYS**

## Core Principles

### 1. Three Pillars Integration
Comprehensive observability requires unified collection and correlation of metrics, logs, and traces - no single pillar provides complete system visibility.

**In practice:**
- Implement metrics collection for quantitative measurements (counters, gauges, histograms)
- Deploy structured logging with correlation IDs for event tracking across services
- Configure distributed tracing with span context propagation for request flow visualization
- Correlate all three pillars using common identifiers (trace IDs, request IDs, user IDs)

### 2. Proactive Alerting with SLO-Based Thresholds
Alerting must be driven by Service Level Objectives that reflect actual user impact, not arbitrary metric thresholds that generate noise.

**In practice:**
- Define SLIs (Service Level Indicators) that measure user-facing behavior (p99 latency, error rate)
- Set SLOs (Service Level Objectives) based on business requirements (99% requests < 200ms)
- Configure alerts to fire when SLO burn rate

/*----------------------------------------------------------------------------*/
/* S4 SUCCESS CRITERIA                                                         */
/*----------------------------------------------------------------------------*/

[define|neutral] SUCCESS_CRITERIA := {
  primary: "Skill execution completes successfully",
  quality: "Output meets quality thresholds",
  verification: "Results validated against requirements"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S5 MCP INTEGRATION                                                          */
/*----------------------------------------------------------------------------*/

[define|neutral] MCP_INTEGRATION := {
  memory_mcp: "Store execution results and patterns",
  tools: ["mcp__memory-mcp__memory_store", "mcp__memory-mcp__vector_search"]
} [ground:witnessed:mcp-config] [conf:0.95] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S6 MEMORY NAMESPACE                                                         */
/*----------------------------------------------------------------------------*/

[define|neutral] MEMORY_NAMESPACE := {
  pattern: "skills/research/observability/{project}/{timestamp}",
  store: ["executions", "decisions", "patterns"],
  retrieve: ["similar_tasks", "proven_patterns"]
} [ground:system-policy] [conf:1.0] [state:confirmed]

[define|neutral] MEMORY_TAGGING := {
  WHO: "observability-{session_id}",
  WHEN: "ISO8601_timestamp",
  PROJECT: "{project_name}",
  WHY: "skill-execution"
} [ground:system-policy] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S7 SKILL COMPLETION VERIFICATION                                            */
/*----------------------------------------------------------------------------*/

[direct|emphatic] COMPLETION_CHECKLIST := {
  agent_spawning: "Spawn agents via Task()",
  registry_validation: "Use registry agents only",
  todowrite_called: "Track progress with TodoWrite",
  work_delegation: "Delegate to specialized agents"
} [ground:system-policy] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S8 ABSOLUTE RULES                                                           */
/*----------------------------------------------------------------------------*/

[direct|emphatic] RULE_NO_UNICODE := forall(output): NOT(unicode_outside_ascii) [ground:windows-compatibility] [conf:1.0] [state:confirmed]

[direct|emphatic] RULE_EVIDENCE := forall(claim): has(ground) AND has(confidence) [ground:verix-spec] [conf:1.0] [state:confirmed]

[direct|emphatic] RULE_REGISTRY := forall(agent): agent IN AGENT_REGISTRY [ground:system-policy] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* PROMISE                                                                     */
/*----------------------------------------------------------------------------*/

[commit|confident] <promise>OBSERVABILITY_VERILINGUA_VERIX_COMPLIANT</promise> [ground:self-validation] [conf:0.99] [state:confirmed]
