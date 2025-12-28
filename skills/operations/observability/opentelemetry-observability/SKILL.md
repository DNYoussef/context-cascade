---
name: opentelemetry-observability
description: OpenTelemetry specialist for distributed tracing, metrics collection, log correlation, auto-instrumentation, custom spans, trace context propagation, and sampling strategies. Use when implementing observability in microservices, debugging production issues, monitoring performance, or requiring OpenTelemetry best practices. Handles integration with Jaeger/Zipkin/Tempo, Prometheus/Grafana, and cloud-native observability platforms.
category: Observability
complexity: High
triggers: ["opentelemetry", "otel", "distributed tracing", "observability", "metrics", "spans", "tracing", "jaeger", "zipkin", "tempo", "instrumentation"]
---

# OpenTelemetry Observability Specialist

Expert distributed tracing, metrics, and logging with OpenTelemetry for production observability.

## Purpose

Comprehensive OpenTelemetry expertise including auto-instrumentation, custom spans, metrics collection, log correlation, trace context propagation, and sampling. Ensures applications are fully observable with actionable telemetry data.

## When to Use

- Implementing distributed tracing in microservices
- Monitoring application performance (APM)
- Debugging production issues across services
- Setting up metrics collection and dashboards
- Correlating logs with traces
- Optimizing sampling strategies for cost/performance
- Migrating from proprietary APM to OpenTelemetry

## Prerequisites

**Required**: Understanding of distributed systems, HTTP, basic observability concepts

**Agents**: `cicd-engineer`, `perf-analyzer`, `backend-dev`, `system-architect`

## Core Workflows

### Workflow 1: Node.js Auto-Instrumentation

**Step 1: Install OpenTelemetry Packages**

```bash
npm install @opentelemetry/sdk-node \
  @opentelemetry/auto-instrumentations-node \
  @opentelemetry/exporter-trace-otlp-http \
  @opentelemetry/exporter-metrics-otlp-http
```

**Step 2: Initialize OpenTelemetry**

```javascript
// instrumentation.js
const { NodeSDK } = require('@opentelemetry/sdk-node');
const { getNodeAutoInstrumentations } = require('@opentelemetry/auto-instrumentations-node');
const { OTLPTraceExporter } = require('@opentelemetry/exporter-trace-otlp-http');
const { OTLPMetricExporter } = require('@opentelemetry/exporter-metrics-otlp-http');
const { Resource } = require('@opentelemetry/resources');
const { SemanticResourceAttributes } = require('@opentelemetry/semantic-conventions');

const sdk = new NodeSDK({
  resource: new Resource({
    [SemanticResourceAttributes.SERVICE_NAME]: 'my-service',
    [SemanticResourceAttributes.SERVICE_VERSION]: '1.0.0',
    [SemanticResourceAttributes.DEPLOYMENT_ENVIRONMENT]: 'production',
  }),
  traceExporter: new OTLPTraceExporter({
    url: 'http://localhost:4318/v1/traces',
  }),
  metricReader: new PeriodicExportingMetricReader({
    exporter: new OTLPMetricExporter({
      url: 'http://localhost:4318/v1/metrics',
    }),
    exportIntervalMillis: 60000,
  }),
  instrumentations: [
    getNodeAutoInstrumentations({
      '@opentelemetry/instrumentation-http': { enabled: true },
      '@opentelemetry/instrumentation-express': { enabled: true },
      '@opentelemetry/instrumentation-pg': { enabled: true },
      '@opentelemetry/instrumentation-redis': { enabled: true },
    }),
  ],
});

sdk.start();

process.on('SIGTERM', () => {
  sdk.shutdown().then(
    () => console.log('Tracing terminated'),
    (err) => console.log('Error terminating tracing', err)
  );
});
```

**Step 3: Start Application with Instrumentation**

```bash
node --require ./instrumentation.js app.js
```

### Workflow 2: Custom Spans and Attributes

```javascript
const { trace } = require('@opentelemetry/api');

const tracer = trace.getTracer('my-service', '1.0.0');

async function processOrder(orderId) {
  const span = tracer.startSpan('processOrder', {
    attributes: {
      'order.id': orderId,
      'order.priority': 'high',
    },
  });

  try {
    // Set span status
    span.setStatus({ code: SpanStatusCode.OK });

    // Add event to span
    span.addEvent('order_validated', {
      'validation.result': 'success',
    });

    // Child span
    const childSpan = tracer.startSpan('calculateTotal', {
      parent: span,
    });
    const total = await calculateTotal(orderId);
    childSpan.setAttribute('order.total', total);
    childSpan.end();

    return total;
  } catch (error) {
    // Record exception
    span.recordException(error);
    span.setStatus({
      code: SpanStatusCode.ERROR,
      message: error.message,
    });
    throw error;
  } finally {
    span.end();
  }
}
```

### Workflow 3: Custom Metrics

```javascript
const { metrics } = require('@opentelemetry/api');

const meter = metrics.getMeter('my-service', '1.0.0');

// Counter: Monotonically increasing value
const orderCounter = meter.createCounter('orders.processed', {
  description: 'Total number of orders processed',
});

orderCounter.add(1, {
  'order.type': 'online',
  'order.status': 'completed',
});

// Histogram: Statistical distribution
const requestDuration = meter.createHistogram('http.server.duration', {
  description: 'HTTP request duration in milliseconds',
  unit: 'ms',
});

requestDuration.record(150, {
  'http.method': 'POST',
  'http.route': '/api/orders',
  'http.status_code': 200,
});

// UpDownCounter: Value can go up or down
const activeConnections = meter.createUpDownCounter('db.connections.active', {
  description: 'Number of active database connections',
});

activeConnections.add(1); // Connection opened
activeConnections.add(-1); // Connection closed

// ObservableGauge: Current value snapshot
const memoryUsage = meter.createObservableGauge('process.memory.usage', {
  description: 'Process memory usage in bytes',
  unit: 'bytes',
});

memoryUsage.addCallback((result) => {
  result.observe(process.memoryUsage().heapUsed, {
    'memory.type': 'heap',
  });
});
```

### Workflow 4: Context Propagation (W3C Trace Context)

```javascript
// Propagate context between services
const { propagation, context } = require('@opentelemetry/api');

// Client-side: Inject trace context into HTTP headers
async function callExternalService(url, data) {
  const span = tracer.startSpan('external_api_call');
  const headers = {};

  // Inject trace context into headers (W3C Trace Context)
  propagation.inject(context.active(), headers);

  try {
    const response = await fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        ...headers, // traceparent, tracestate headers
      },
      body: JSON.stringify(data),
    });
    return response.json();
  } finally {
    span.end();
  }
}

// Server-side: Extract trace context from HTTP headers
app.post('/api/process', (req, res) => {
  // Extract context from incoming headers
  const extractedContext = propagation.extract(context.active(), req.headers);

  context.with(extractedContext, () => {
    const span = tracer.startSpan('process_request');
    // This span will be a child of the parent trace from the caller
    // ...
    span.end();
  });

  res.json({ status: 'ok' });
});
```

### Workflow 5: Sampling Strategies

```javascript
const { ParentBasedSampler, AlwaysOnSampler, AlwaysOffSampler, TraceIdRatioBasedSampler } = require('@opentelemetry/sdk-trace-base');

// Probability-based sampling (10% of traces)
const sampler = new TraceIdRatioBasedSampler(0.1);

// Parent-based sampling with rate limiting
const parentBasedSampler = new ParentBasedSampler({
  root: new TraceIdRatioBasedSampler(0.1), // 10% for root spans
  remoteParentSampled: new AlwaysOnSampler(), // Always sample if parent sampled
  remoteParentNotSampled: new AlwaysOffSampler(), // Never sample if parent not sampled
  localParentSampled: new AlwaysOnSampler(),
  localParentNotSampled: new AlwaysOffSampler(),
});

const sdk = new NodeSDK({
  sampler: parentBasedSampler,
  // ... other config
});
```

## Best Practices

**1. Use Semantic Conventions**
```javascript
// ✅ GOOD: Standard semantic conventions
const { SemanticAttributes } = require('@opentelemetry/semantic-conventions');

span.setAttributes({
  [SemanticAttributes.HTTP_METHOD]: 'POST',
  [SemanticAttributes.HTTP_URL]: '/api/users',
  [SemanticAttributes.HTTP_STATUS_CODE]: 200,
  [SemanticAttributes.DB_SYSTEM]: 'postgresql',
  [SemanticAttributes.DB_NAME]: 'mydb',
});

// ❌ BAD: Custom attributes without namespace
span.setAttributes({
  method: 'POST',
  url: '/api/users',
});
```

**2. Keep Span Names Concise**
```javascript
// ✅ GOOD: Generic operation name (use attributes for details)
const span = tracer.startSpan('GET /api/users/:id', {
  attributes: { 'user.id': userId },
});

// ❌ BAD: High cardinality span names
const span = tracer.startSpan(`GET /api/users/${userId}`);
```

**3. Always End Spans**
```javascript
// ✅ GOOD: Use try/finally to ensure span ends
const span = tracer.startSpan('operation');
try {
  await doWork();
} finally {
  span.end();
}

// ❌ BAD: Span might never end
const span = tracer.startSpan('operation');
await doWork();
span.end();
```

**4. Use Baggage for Cross-Cutting Concerns**
```javascript
const { propagation, baggageUtils } = require('@opentelemetry/api');

// Set baggage (propagates across service boundaries)
const baggage = propagation.createBaggage({
  'user.id': { value: '12345' },
  'request.id': { value: 'req-abc-123' },
});

context.with(propagation.setBaggage(context.active(), baggage), () => {
  // Baggage available in all child spans
  const userId = propagation.getBaggage(context.active())?.getEntry('user.id')?.value;
});
```

**5. Log Correlation**
```javascript
const { trace } = require('@opentelemetry/api');
const winston = require('winston');

const logger = winston.createLogger({
  format: winston.format.combine(
    winston.format((info) => {
      const span = trace.getActiveSpan();
      if (span) {
        const spanContext = span.spanContext();
        info.trace_id = spanContext.traceId;
        info.span_id = spanContext.spanId;
      }
      return info;
    })(),
    winston.format.json()
  ),
  transports: [new winston.transports.Console()],
});

logger.info('Order processed', { order_id: '123' });
// Output: { "message": "Order processed", "order_id": "123", "trace_id": "...", "span_id": "..." }
```

## Quality Criteria

- ✅ All HTTP requests automatically traced
- ✅ Database queries instrumented
- ✅ Custom business logic spans added
- ✅ Metrics exported every 60 seconds
- ✅ Sampling rate configured (not 100% in production)
- ✅ Trace context propagated across services
- ✅ Logs correlated with traces

## Backend Setup (Jaeger)

```bash
# Run Jaeger all-in-one (for development)
docker run -d --name jaeger \
  -e COLLECTOR_OTLP_ENABLED=true \
  -p 16686:16686 \
  -p 4318:4318 \
  jaegertracing/all-in-one:latest

# Access Jaeger UI: http://localhost:16686
```

## Troubleshooting

**Issue**: No traces appearing in Jaeger
**Solution**: Check exporter URL, ensure OTLP collector is running, verify network connectivity

**Issue**: High memory usage
**Solution**: Reduce sampling rate, use batch span processor with smaller queue size

**Issue**: Missing trace context between services
**Solution**: Ensure W3C Trace Context headers (traceparent, tracestate) are propagated

## Related Skills

- `kubernetes-specialist`: Deploying OTel Collector in K8s
- `aws-specialist`: AWS X-Ray integration
- `backend-dev`: Application instrumentation

## Tools

- Jaeger: Open-source tracing backend
- Zipkin: Distributed tracing system
- Grafana Tempo: High-scale tracing backend
- Prometheus: Metrics collection
- Grafana: Visualization

## MCP Tools

- `mcp__flow-nexus__execution_stream_subscribe` for real-time trace monitoring
- `mcp__flow-nexus__realtime_subscribe` for live metrics
- `mcp__memory-mcp__memory_store` for OTel patterns

## Success Metrics

- Trace coverage: ≥95% of requests
- Sampling rate: 5-10% (production)
- Metrics export interval: 60 seconds
- Span drop rate: <1%
- Log-trace correlation: 100%

---

**Skill Version**: 1.0.0
**Last Updated**: 2025-11-02

## Core Principles

OpenTelemetry Observability operates on 3 fundamental principles:

### Principle 1: Context Propagation is Non-Negotiable
Distributed tracing only works if trace context flows across service boundaries. W3C Trace Context headers (traceparent, tracestate) must be propagated through HTTP calls, message queues, and async operations. This principle enables end-to-end visibility.

In practice:
- Use OpenTelemetry auto-instrumentation to inject/extract trace context automatically
- Explicitly propagate context in custom HTTP clients and message queue consumers
- Validate context propagation in integration tests by checking trace continuity
- Use baggage for cross-cutting concerns like user ID or request ID that need to flow everywhere

### Principle 2: Cardinality Control Prevents Metric Explosions
High-cardinality attributes (user IDs, request IDs) in metric labels cause exponential growth in time series, leading to OOM errors, high storage costs, and query timeouts. This principle ensures sustainable observability costs.

In practice:
- Use low-cardinality labels for metrics (environment, service, endpoint, status code)
- Put high-cardinality data in span attributes, not metric labels
- Use histograms for latency distribution instead of individual timers per request
- Implement sampling to reduce trace volume while maintaining statistical significance

### Principle 3: Semantic Conventions Enable Tool Interoperability
OpenTelemetry defines semantic conventions for common attributes (http.method, db.system, messaging.destination). Following conventions ensures your telemetry works with all backends (Jaeger, Zipkin, Grafana, Prometheus) without custom transforms.

In practice:
- Use SemanticAttributes constants from OpenTelemetry SDK, not custom strings
- Follow naming patterns (http.*, db.*, messaging.*, rpc.*) for standard operations
- Document custom attributes with namespace prefixes (myapp.order.priority)
- Validate semantic convention compliance in code reviews

## Common Anti-Patterns

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| **100% Sampling in Production** | Capturing every trace creates massive backend load, storage costs exploding to hundreds of GB/day, and query performance degradation from index bloat. | Use TraceIdRatioBasedSampler (5-10% for production). Implement parent-based sampling to preserve complete traces. Use tail sampling for error-biased retention. |
| **High-Cardinality Span Names** | Using unique IDs in span names (GET /users/12345 instead of GET /users/:id) creates millions of unique operations, breaking trace aggregation and dashboards. | Use generic operation names with placeholders. Put dynamic values in span attributes. Follow semantic conventions for HTTP routes (http.route: /users/:id). |
| **Forgetting to End Spans** | Unclosed spans accumulate in memory, causing memory leaks, inaccurate latency measurements, and spans never exported to backend. | Always use try/finally blocks to ensure span.end() is called. Use context managers (Python with) or defer (Go) for automatic cleanup. |
| **Logging Without Trace Correlation** | Logs and traces live in separate systems with no correlation, forcing manual detective work to connect error logs to slow traces. | Inject trace_id and span_id into structured log fields. Use OpenTelemetry LogRecordProcessor to auto-correlate. Configure backend (Grafana) to link logs to traces. |
| **No Metric Export Validation** | Metrics are collected but never exported due to misconfigured endpoint, network issues, or authentication failures. Silent failures leave blind spots. | Implement health checks that verify metric export success. Monitor OTLP exporter metrics (exported count, failed count). Test export in staging environments. |

## Conclusion

The OpenTelemetry Observability skill provides a comprehensive framework for implementing production-grade distributed tracing, metrics, and log correlation across microservices architectures. By mastering the three core principles of context propagation, cardinality control, and semantic conventions, you ensure that your observability infrastructure is both powerful and sustainable at scale.

The workflows demonstrate the complete lifecycle from auto-instrumentation setup to custom span creation, metrics collection, and advanced sampling strategies. The emphasis on W3C Trace Context propagation ensures trace continuity across polyglot services, while the semantic conventions guarantee interoperability with all major observability backends. The anti-patterns table serves as a critical reference to avoid common pitfalls that lead to metric explosions, memory leaks, and unactionable telemetry.

This skill is particularly valuable when debugging production issues across distributed systems, implementing SLO-based alerting, or migrating from proprietary APM solutions to vendor-neutral OpenTelemetry. Whether you're instrumenting a Node.js microservice, a Python Flask API, or a complex event-driven architecture with message queues, the patterns and best practices documented here provide a solid foundation. Combined with backend setup guides (Jaeger, Prometheus, Grafana Tempo) and troubleshooting references, you have everything needed to build observable systems that provide actionable insights when incidents occur.

---

## System Design Integration (Dr. Synthara Methodology)

### Observability as the Immune System

In Dr. Synthara's organism model, observability is the **immune system** - it detects problems, triggers responses, and enables recovery. Without observability, your system is blind to its own health.

**The Three Pillars Mapped to Body Systems**:
- **Metrics** = Vital signs (CPU, memory, request rate) - continuous health monitoring
- **Logs** = Medical records - detailed event history for diagnosis
- **Traces** = MRI scans - see inside distributed requests

### Observability Decision Tree

```
What problem are you solving?
|
+-- "Is the system healthy right now?"
|   +-- Metrics (Prometheus, CloudWatch)
|   +-- Dashboards showing current state
|   +-- Alerting on threshold violations
|
+-- "What happened during this incident?"
|   +-- Logs (ELK, Loki, CloudWatch Logs)
|   +-- Structured JSON with trace_id correlation
|   +-- Search by time range and attributes
|
+-- "Why is this request slow?"
    +-- Traces (Jaeger, Tempo, X-Ray)
    +-- Follow request across services
    +-- Identify bottleneck spans
```

### SPOF Mitigation Through Observability

| SPOF Risk | Observability Defense |
|-----------|----------------------|
| **Database failure** | Metrics: connection pool usage, query latency p99 |
| **Memory leak** | Metrics: heap usage trend, GC frequency |
| **Cascading failure** | Traces: identify failing upstream service |
| **Network partition** | Metrics: inter-service error rates by destination |
| **Silent failures** | Alerts: on zero-traffic (dead service detection) |

**What I'm Thinking**: "How do I know this is failing at 2am?"
- Every SPOF needs a metric
- Every failure mode needs an alert
- Every alert needs a runbook

### Master Design Flow for Observability

```
OBSERVABILITY DESIGN FLOW
1) Define SLIs (Service Level Indicators)
   +-- Availability: successful requests / total requests
   +-- Latency: p50, p95, p99 response time
   +-- Error rate: errors / total requests
2) Set SLOs (Service Level Objectives)
   +-- "99.9% of requests succeed"
   +-- "p99 latency < 500ms"
3) Instrument the code
   +-- Auto-instrumentation for frameworks
   +-- Custom spans for business logic
   +-- Metrics for cardinality-safe dimensions
4) Configure sampling
   +-- 5-10% for production traces
   +-- 100% for errors (tail sampling)
5) Set up alerting
   +-- Alert on SLO burn rate, not raw metrics
   +-- PagerDuty/Slack integration
   +-- Runbook links in alerts
6) Build dashboards
   +-- RED metrics (Rate, Errors, Duration)
   +-- USE metrics (Utilization, Saturation, Errors)
```

### Phase 0 Observability Constraint Extraction

| Constraint | Questions |
|------------|-----------|
| **SLOs** | What availability/latency targets? |
| **Scale** | How many services? QPS? |
| **Budget** | Trace storage costs? Metric cardinality limits? |
| **Retention** | How long to keep traces/logs? |
| **Compliance** | PII in logs? Audit requirements? |

### The 90-Second Interview Narrative for Observability

1. **Clarify** SLOs, scale, compliance requirements
2. **Three pillars** metrics (Prometheus), logs (Loki), traces (Tempo)
3. **Instrumentation** auto + custom spans for business logic
4. **Sampling** 5-10% traces, 100% for errors
5. **Alerting** SLO-based (burn rate), not threshold-based
6. **Correlation** trace_id in logs, exemplars in metrics
7. **Dashboards** RED/USE patterns, service maps
8. **Trade-offs** cost vs resolution, sampling vs completeness

### Anti-Pattern: Observability as Afterthought

> "You cannot debug what you cannot see."

| Anti-Pattern | Why It Fails | Correct Approach |
|--------------|--------------|------------------|
| Add monitoring after launch | First incident = blind debugging | Instrument BEFORE deploy |
| Alert on every metric | Alert fatigue, ignored pages | Alert on SLO burn rate |
| 100% sampling in prod | Cost explosion, storage overflow | 5-10% with tail sampling |
| Logs without trace_id | Manual correlation during incident | Auto-inject trace context |
