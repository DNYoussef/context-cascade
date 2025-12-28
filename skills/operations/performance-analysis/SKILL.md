---

## CRITICAL: PERFORMANCE OPTIMIZATION GUARDRAILS

**BEFORE any optimization, validate**:
- [ ] Baseline metrics captured (latency p50/p99, throughput, error rate)
- [ ] Profiling data analyzed (CPU, memory, I/O bottlenecks)
- [ ] Load testing with production-like traffic patterns
- [ ] A/B testing plan for performance changes
- [ ] Rollback plan if optimization degrades performance

**NEVER**:
- Optimize without profiling (avoid premature optimization)
- Deploy performance changes without load testing
- Sacrifice code clarity for micro-optimizations
- Ignore memory leaks and resource exhaustion
- Skip monitoring after optimization deployment

**ALWAYS**:
- Measure before and after (quantify improvement)
- Document trade-offs (performance vs maintainability)
- Use caching strategically (cache invalidation is hard)
- Optimize critical path first (Pareto principle)
- Retain performance metrics over time (track regressions)

**Evidence-Based Techniques for Performance**:
- **Program-of-Thought**: Model system as data flow (identify bottlenecks)
- **Chain-of-Thought**: Trace request lifecycle (find latency sources)
- **Least-to-Most**: Optimize highest-impact bottleneck first
- **Self-Consistency**: Apply same optimization patterns across similar code

name: performance-analysis
version: 1.0.0
description: Comprehensive performance analysis, bottleneck detection, and optimization recommendations for Claude Flow swarms
category: monitoring
tags: [performance, bottleneck, optimization, profiling, metrics, analysis]
author: Claude Flow Team
---

# Performance Analysis Skill

Comprehensive performance analysis suite for identifying bottlenecks, profiling swarm operations, generating detailed reports, and providing actionable optimization recommendations.

## Overview

This skill consolidates all performance analysis capabilities:
- **Bottleneck Detection**: Identify performance bottlenecks across communication, processing, memory, and network
- **Performance Profiling**: Real-time monitoring and historical analysis of swarm operations
- **Report Generation**: Create comprehensive performance reports in multiple formats
- **Optimization Recommendations**: AI-powered suggestions for improving performance

## Quick Start

### Basic Bottleneck Detection
```bash
npx claude-flow bottleneck detect
```

### Generate Performance Report
```bash
npx claude-flow analysis performance-report --format html --include-metrics
```

### Analyze and Auto-Fix
```bash
npx claude-flow bottleneck detect --fix --threshold 15
```

## Core Capabilities

### 1. Bottleneck Detection

#### Command Syntax
```bash
npx claude-flow bottleneck detect [options]
```

#### Options
- `--swarm-id, -s <id>` - Analyze specific swarm (default: current)
- `--time-range, -t <range>` - Analysis period: 1h, 24h, 7d, all (default: 1h)
- `--threshold <percent>` - Bottleneck threshold percentage (default: 20)
- `--export, -e <file>` - Export analysis to file
- `--fix` - Apply automatic optimizations

#### Usage Examples
```bash
# Basic detection for current swarm
npx claude-flow bottleneck detect

# Analyze specific swarm over 24 hours
npx claude-flow bottleneck detect --swarm-id swarm-123 -t 24h

# Export detailed analysis
npx claude-flow bottleneck detect -t 24h -e bottlenecks.json

# Auto-fix detected issues
npx claude-flow bottleneck detect --fix --threshold 15

# Low threshold for sensitive detection
npx claude-flow bottleneck detect --threshold 10 --export critical-issues.json
```

#### Metrics Analyzed

**Communication Bottlenecks:**
- Message queue delays
- Agent response times
- Coordination overhead
- Memory access patterns
- Inter-agent communication latency

**Processing Bottlenecks:**
- Task completion times
- Agent utilization rates
- Parallel execution efficiency
- Resource contention
- CPU/memory usage patterns

**Memory Bottlenecks:**
- Cache hit rates
- Memory access patterns
- Storage I/O performance
- Neural pattern loading times
- Memory allocation efficiency

**Network Bottlenecks:**
- API call latency
- MCP communication delays
- External service timeouts
- Concurrent request limits
- Network throughput issues

#### Output Format
```
🔍 Bottleneck Analysis Report
━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 Summary
├── Time Range: Last 1 hour
├── Agents Analyzed: 6
├── Tasks Processed: 42
└── Critical Issues: 2

🚨 Critical Bottlenecks
1. Agent Communication (35% impact)
   └── coordinator → coder-1 messages delayed by 2.3s avg

2. Memory Access (28% impact)
   └── Neural pattern loading taking 1.8s per access

⚠️ Warning Bottlenecks
1. Task Queue (18% impact)
   └── 5 tasks waiting > 10s for assignment

💡 Recommendations
1. Switch to hierarchical topology (est. 40% improvement)
2. Enable memory caching (est. 25% improvement)
3. Increase agent concurrency to 8 (est. 20% improvement)

✅ Quick Fixes Available
Run with --fix to apply:
- Enable smart caching
- Optimize message routing
- Adjust agent priorities
```

### 2. Performance Profiling

#### Real-time Detection
Automatic analysis during task execution:
- Execution time vs. complexity
- Agent utilization rates
- Resource constraints
- Operation patterns

#### Common Bottleneck Patterns

**Time Bottlenecks:**
- Tasks taking > 5 minutes
- Sequential operations that could parallelize
- Redundant file operations
- Inefficient algorithm implementations

**Coordination Bottlenecks:**
- Single agent for complex tasks
- Unbalanced agent workloads
- Poor topology selection
- Excessive synchronization points

**Resource Bottlenecks:**
- High operation count (> 100)
- Memory constraints
- I/O limitations
- Thread pool saturation

#### MCP Integration
```javascript
// Check for bottlenecks in Claude Code
mcp__claude-flow__bottleneck_detect({
  timeRange: "1h",
  threshold: 20,
  autoFix: false
})

// Get detailed task results with bottleneck analysis
mcp__claude-flow__task_results({
  taskId: "task-123",
  format: "detailed"
})
```

**Result Format:**
```json
{
  "bottlenecks": [
    {
      "type": "coordination",
      "severity": "high",
      "description": "Single agent used for complex task",
      "recommendation": "Spawn specialized agents for parallel work",
      "impact": "35%",
      "affectedComponents": ["coordinator", "coder-1"]
    }
  ],
  "improvements": [
    {
      "area": "execution_time",
      "suggestion": "Use parallel task execution",
      "expectedImprovement": "30-50% time reduction",
      "implementationSteps": [
        "Split task into smaller units",
        "Spawn 3-4 specialized agents",
        "Use mesh topology for coordination"
      ]
    }
  ],
  "metrics": {
    "avgExecutionTime": "142s",
    "agentUtilization": "67%",
    "cacheHitRate": "82%",
    "parallelizationFactor": 1.2
  }
}
```

### 3. Report Generation

#### Command Syntax
```bash
npx claude-flow analysis performance-report [options]
```

#### Options
- `--format <type>` - Report format: json, html, markdown (default: markdown)
- `--include-metrics` - Include detailed metrics and charts
- `--compare <id>` - Compare with previous swarm
- `--time-range <range>` - Analysis period: 1h, 24h, 7d, 30d, all
- `--output <file>` - Output file path
- `--sections <list>` - Comma-separated sections to include

#### Report Sections
1. **Executive Summary**
   - Overall performance score
   - Key metrics overview
   - Critical findings

2. **Swarm Overview**
   - Topology configuration
   - Agent distribution
   - Task statistics

3. **Performance Metrics**
   - Execution times
   - Throughput analysis
   - Resource utilization
   - Latency breakdown

4. **Bottleneck Analysis**
   - Identified bottlenecks
   - Impact assessment
   - Optimization priorities

5. **Comparative Analysis** (when --compare used)
   - Performance trends
   - Improvement metrics
   - Regression detection

6. **Recommendations**
   - Prioritized action items
   - Expected improvements
   - Implementation guidance

#### Usage Examples
```bash
# Generate HTML report with all metrics
npx claude-flow analysis performance-report --format html --include-metrics

# Compare current swarm with previous
npx claude-flow analysis performance-report --compare swarm-123 --format markdown

# Custom output with specific sections
npx claude-flow analysis performance-report \
  --sections summary,metrics,recommendations \
  --output reports/perf-analysis.html \
  --format html

# Weekly performance report
npx claude-flow analysis performance-report \
  --time-range 7d \
  --include-metrics \
  --format markdown \
  --output docs/weekly-performance.md

# JSON format for CI/CD integration
npx claude-flow analysis performance-report \
  --format json \
  --output build/performance.json
```

#### Sample Markdown Report
```markdown
# Performance Analysis Report

## Executive Summary
- **Overall Score**: 87/100
- **Analysis Period**: Last 24 hours
- **Swarms Analyzed**: 3
- **Critical Issues**: 1

## Key Metrics
| Metric | Value | Trend | Target |
|--------|-------|-------|--------|
| Avg Task Time | 42s | ↓ 12% | 35s |
| Agent Utilization | 78% | ↑ 5% | 85% |
| Cache Hit Rate | 91% | → | 90% |
| Parallel Efficiency | 2.3x | ↑ 0.4x | 2.5x |

## Bottleneck Analysis
### Critical
1. **Agent Communication Delay** (Impact: 35%)
   - Coordinator → Coder messages delayed by 2.3s avg
   - **Fix**: Switch to hierarchical topology

### Warnings
1. **Memory Access Pattern** (Impact: 18%)
   - Neural pattern loading: 1.8s per access
   - **Fix**: Enable memory caching

## Recommendations
1. **High Priority**: Switch to hierarchical topology (40% improvement)
2. **Medium Priority**: Enable memory caching (25% improvement)
3. **Low Priority**: Increase agent concurrency to 8 (20% improvement)
```

### 4. Optimization Recommendations

#### Automatic Fixes
When using `--fix`, the following optimizations may be applied:

**1. Topology Optimization**
- Switch to more efficient topology (mesh → hierarchical)
- Adjust communication patterns
- Reduce coordination overhead
- Optimize message routing

**2. Caching Enhancement**
- Enable memory caching
- Optimize cache strategies
- Preload common patterns
- Implement cache warming

**3. Concurrency Tuning**
- Adjust agent counts
- Optimize parallel execution
- Balance workload distribution
- Implement load balancing

**4. Priority Adjustment**
- Reorder task queues
- Prioritize critical paths
- Reduce wait times
- Implement fair scheduling

**5. Resource Optimization**
- Optimize memory usage
- Reduce I/O operations
- Batch API calls
- Implement connection pooling

#### Performance Impact
Typical improvements after bottleneck resolution:

- **Communication**: 30-50% faster message delivery
- **Processing**: 20-40% reduced task completion time
- **Memory**: 40-60% fewer cache misses
- **Network**: 25-45% reduced API latency
- **Overall**: 25-45% total performance improvement

## Advanced Usage

### Continuous Monitoring
```bash
# Monitor performance in real-time
npx claude-flow swarm monitor --interval 5

# Generate hourly reports
while true; do
  npx claude-flow analysis performance-report \
    --format json \
    --output logs/perf-$(date +%Y%m%d-%H%M).json
  sleep 3600
done
```

### CI/CD Integration
```yaml
# .github/workflows/performance.yml
name: Performance Analysis
on: [push, pull_request]

jobs:
  analyze:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Run Performance Analysis
        run: |
          npx claude-flow analysis performance-report \
            --format json \
            --output performance.json
      - name: Check Performance Thresholds
        run: |
          npx claude-flow bottleneck detect \
            --threshold 15 \
            --export bottlenecks.json
      - name: Upload Reports
        uses: actions/upload-artifact@v2
        with:
          name: performance-reports
          path: |
            performance.json
            bottlenecks.json
```

### Custom Analysis Scripts
```javascript
// scripts/analyze-performance.js
const { exec } = require('child_process');
const fs = require('fs');

async function analyzePerformance() {
  // Run bottleneck detection
  const bottlenecks = await runCommand(
    'npx claude-flow bottleneck detect --format json'
  );

  // Generate performance report
  const report = await runCommand(
    'npx claude-flow analysis performance-report --format json'
  );

  // Analyze results
  const analysis = {
    bottlenecks: JSON.parse(bottlenecks),
    performance: JSON.parse(report),
    timestamp: new Date().toISOString()
  };

  // Save combined analysis
  fs.writeFileSync(
    'analysis/combined-report.json',
    JSON.stringify(analysis, null, 2)
  );

  // Generate alerts if needed
  if (analysis.bottlenecks.critical.length > 0) {
    console.error('CRITICAL: Performance bottlenecks detected!');
    process.exit(1);
  }
}

function runCommand(cmd) {
  return new Promise((resolve, reject) => {
    exec(cmd, (error, stdout, stderr) => {
      if (error) reject(error);
      else resolve(stdout);
    });
  });
}

analyzePerformance().catch(console.error);
```

## Best Practices

### 1. Regular Analysis
- Run bottleneck detection after major changes
- Generate weekly performance reports
- Monitor trends over time
- Set up automated alerts

### 2. Threshold Tuning
- Start with default threshold (20%)
- Lower for production systems (10-15%)
- Higher for development (25-30%)
- Adjust based on requirements

### 3. Fix Strategy
- Always review before applying --fix
- Test fixes in development first
- Apply fixes incrementally
- Monitor impact after changes

### 4. Report Integration
- Include in documentation
- Share with team regularly
- Track improvements over time
- Use for capacity planning

### 5. Continuous Optimization
- Learn from each analysis
- Build performance budgets
- Establish baselines
- Set improvement goals

## Troubleshooting

### Common Issues

**High Memory Usage**
```bash
# Analyze memory bottlenecks
npx claude-flow bottleneck detect --threshold 10

# Check cache performance
npx claude-flow cache manage --action stats

# Review memory metrics
npx claude-flow memory usage
```

**Slow Task Execution**
```bash
# Identify slow tasks
npx claude-flow task status --detailed

# Analyze coordination overhead
npx claude-flow bottleneck detect --time-range 1h

# Check agent utilization
npx claude-flow agent metrics
```

**Poor Cache Performance**
```bash
# Analyze cache hit rates
npx claude-flow analysis performance-report --sections metrics

# Review cache strategy
npx claude-flow cache manage --action analyze

# Enable cache warming
npx claude-flow bottleneck detect --fix
```

## Integration with Other Skills

- **swarm-orchestration**: Use performance data to optimize topology
- **memory-management**: Improve cache strategies based on analysis
- **task-coordination**: Adjust scheduling based on bottlenecks
- **neural-training**: Train patterns from performance data

## Related Commands

- `npx claude-flow swarm monitor` - Real-time monitoring
- `npx claude-flow token usage` - Token optimization analysis
- `npx claude-flow cache manage` - Cache optimization
- `npx claude-flow agent metrics` - Agent performance metrics
- `npx claude-flow task status` - Task execution analysis

## See Also

- [Bottleneck Detection Guide](/workspaces/claude-code-flow/.claude/commands/analysis/bottleneck-detect.md)
- [Performance Report Guide](/workspaces/claude-code-flow/.claude/commands/analysis/performance-report.md)
- [Performance Bottlenecks Overview](/workspaces/claude-code-flow/.claude/commands/analysis/performance-bottlenecks.md)
- [Swarm Monitoring Documentation](../swarm-orchestration/SKILL.md)
- [Memory Management Documentation](../memory-management/SKILL.md)

---

**Version**: 1.0.0
**Last Updated**: 2025-10-19
**Maintainer**: Claude Flow Team

---

## Core Principles

### 1. Measure Before Optimizing
Premature optimization based on intuition rather than profiling data is the root of wasted effort. Performance bottlenecks are rarely where developers expect - profiling reveals the actual critical path. Optimizing non-bottlenecks improves nothing while adding complexity.

In practice:
- Establish baseline metrics (p50/p99 latency, throughput, error rate) before changes
- Profile production-like workloads to identify actual bottlenecks (CPU, memory, I/O, network)
- Focus optimization on the top 3 bottlenecks by impact - Pareto principle applies (20% of code causes 80% of performance issues)
- Quantify improvement with A/B testing - "feels faster" is not a metric

### 2. Optimization Has Trade-Offs
Every performance optimization sacrifices something - code clarity, maintainability, memory usage, or development time. Micro-optimizations that save 2ms while making code unreadable are net negative for long-term velocity.

In practice:
- Document trade-offs explicitly (e.g., "caching reduces latency 40% but increases memory 20%")
- Optimize critical path first, tolerate inefficiency in rarely-executed code
- Preserve code clarity unless optimization is on critical path with proven impact
- Set performance budgets that balance speed with maintainability

### 3. Monitor Performance Over Time
One-time optimization without continuous monitoring guarantees performance regressions. New features, dependency updates, and data volume growth slowly degrade performance until customer complaints force reactive firefighting.

In practice:
- Track key metrics continuously (response time p99, throughput, resource utilization)
- Set up automated alerts for performance degradation (latency > baseline + 20%)
- Run load tests in CI/CD to catch regressions before production
- Maintain performance budgets as part of code review (max bundle size, max query time)

---

## Anti-Patterns

| Anti-Pattern | Why It Fails | Correct Approach |
|-------------|--------------|------------------|
| **Optimizing Without Profiling** | Developer intuition about bottlenecks is wrong 70%+ of the time. Optimizing based on guesses wastes effort on non-critical code while ignoring actual performance issues. Results in complex, hard-to-maintain code with no measurable improvement. | Profile first with production-like data and traffic patterns. Use tools (flamegraphs, performance monitors) to identify actual bottlenecks. Focus optimization on top 3 bottlenecks by measured impact. Quantify improvement with before/after benchmarks. |
| **Micro-Optimizations Everywhere** | Optimizing rarely-executed code (startup routines, config loading, error paths) provides negligible user-facing benefit while sacrificing code clarity. Developers spend days optimizing code that executes once per server restart. | Optimize critical path only - code executed thousands/millions of times per day (request handlers, data transforms, rendering loops). Use performance profiling to identify hot paths. Preserve code clarity in non-critical paths - maintainability matters more than 2ms saved in startup. |
| **No Continuous Monitoring** | One-time optimization without ongoing measurement allows performance regressions to accumulate unnoticed. New features, dependency updates, and data growth slowly degrade performance until customer complaints force reactive investigation. | Implement continuous performance monitoring with automated alerts. Track key metrics (p99 latency, throughput, error rate) over time. Run load tests in CI/CD to catch regressions before production deployment. Set performance budgets for bundle size, query time, API latency. |

---

## Common Anti-Patterns

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| **Optimizing Without Profiling** | Developer intuition about bottlenecks is wrong 70%+ of time. Optimizing based on guesses wastes effort on non-critical code while ignoring actual issues. Results in complex code with no measurable improvement. | Profile first with production-like data and traffic. Use flamegraphs and performance monitors to identify actual bottlenecks. Focus on top 3 bottlenecks by measured impact. Quantify improvement with before/after benchmarks. |
| **Micro-Optimizations Everywhere** | Optimizing rarely-executed code (startup, config loading, error paths) provides negligible user benefit while sacrificing code clarity. Days spent optimizing code that executes once per server restart. | Optimize critical path only - code executed thousands/millions times per day (request handlers, data transforms, rendering). Use profiling to identify hot paths. Preserve clarity in non-critical paths - maintainability matters more than 2ms saved in startup. |
| **Ignoring p95/p99 Latency** | Reporting average response time while ignoring tail latency. API averages 100ms but p95=2000ms, p99=8000ms means 5% requests take 20x longer. Terrible experience for 1 in 20 users hidden by averages. | ALWAYS measure and optimize for p95/p99 latency, not averages. Run load tests with percentile reporting. Set performance budgets on tail latency (p95 <500ms, p99 <1000ms). Profile slow requests specifically to find root causes (cache misses, lock contention, GC pauses). |

---

## Conclusion

Performance analysis transforms subjective "feels slow" complaints into data-driven optimization through systematic bottleneck detection, profiling, and impact quantification. This skill provides comprehensive tooling for identifying performance issues across communication, processing, memory, and network dimensions, then prioritizing optimizations by measurable impact.

Use this skill to establish baseline performance metrics, profile production-like workloads, identify actual bottlenecks (not assumed ones), and quantify improvement through A/B testing. The automated bottleneck detection (`bottleneck detect --fix`) applies proven optimizations (caching, topology changes, concurrency tuning) with estimated impact percentages, enabling informed trade-off decisions between performance gains and code complexity.

The key insight is that performance optimization without profiling data is guesswork - developer intuition about bottlenecks is wrong 70%+ of the time. Profiling reveals the actual critical path, allowing focused effort on the 20% of code causing 80% of performance issues (Pareto principle). Micro-optimizations that save 2ms while making code unreadable are net negative for long-term velocity - optimize critical paths only, preserve clarity elsewhere.

Continuous monitoring prevents performance regressions by tracking key metrics (p99 latency, throughput, resource utilization) over time and alerting on degradation. Without ongoing measurement, new features and dependency updates slowly degrade performance until customer complaints force reactive firefighting. The performance report generation (`performance-report --compare`) enables trend analysis, regression detection, and proactive optimization before user impact.

Success requires treating performance as a continuous discipline, not a one-time fix. Establish performance budgets (max latency, max bundle size, max query time) during architecture phase, enforce budgets in code review and CI/CD, and prioritize optimization by measured impact rather than developer assumptions. The difference between fast systems and slow systems is systematic profiling, data-driven optimization, and continuous monitoring - not individual developer skill.

---

## System Design Integration (Dr. Synthara Methodology)

### Cache Placement Decision Tree

```
What are you caching?
|
+-- Static assets (images/js/css)?
|   +-- CDN + long TTL + versioned filenames
|   +-- CloudFront, Cloudflare, Akamai
|   +-- Invalidation: version in filename (app.v1.2.3.js)
|
+-- Hot reads that tolerate slight staleness?
|   +-- App cache (Redis/Memcached) + TTL
|   +-- Write-through or write-behind pattern
|   +-- Invalidation: TTL-based or explicit
|
+-- Expensive computed results (reports, aggregations)?
    +-- Cache with invalidation strategy + stampede protection
    +-- Request coalescing / single-flight
    +-- Stale-while-revalidate patterns
```

**What I'm Thinking**: Stampedes (thundering herd) and invalidation are the HARDEST parts:
- TTL + soft TTL (serve stale, refresh async)
- Request coalescing (one compute, many waiters)
- Cache warming (preload before traffic)
- Write-through (update cache on write)

### Performance SPOF Identification

| SPOF Risk | Performance Defense |
|-----------|---------------------|
| **Single database** | Read replicas, connection pooling |
| **No caching** | Cache hot paths, set TTLs |
| **Sync blocking calls** | Async where possible, timeouts |
| **No pagination** | Cursor-based pagination, limit results |
| **N+1 queries** | Batch loading, JOINs, DataLoader |
| **Missing indexes** | EXPLAIN ANALYZE, add indexes |

**What I'm Thinking**: "Where does latency accumulate?"
- Network calls compound (100ms * 10 calls = 1s)
- Database is usually the bottleneck
- Profile BEFORE optimizing

### Master Performance Design Flow

```
PERFORMANCE DESIGN FLOW
1) Define SLOs
   +-- p50 latency target (user-perceived)
   +-- p99 latency target (tail latency)
   +-- Throughput target (requests/second)
2) Measure baseline
   +-- Profile production-like traffic
   +-- Identify top 3 bottlenecks
   +-- Quantify impact of each
3) Optimize critical path
   +-- Cache hot reads (Redis)
   +-- CDN for static assets
   +-- Database indexes + query optimization
   +-- Connection pooling
4) Implement async patterns
   +-- Queue non-critical work
   +-- Background jobs for slow operations
   +-- Webhooks instead of polling
5) Add circuit breakers
   +-- Timeout slow dependencies
   +-- Fallback to cached data
   +-- Graceful degradation
6) Monitor continuously
   +-- p50/p95/p99 latency dashboards
   +-- Throughput and error rate
   +-- Cache hit rate
```

### Phase 0 Performance Constraint Extraction

| Constraint | Questions |
|------------|-----------|
| **Latency Target** | p50? p95? p99? (milliseconds) |
| **Throughput** | Peak QPS? Sustained QPS? |
| **Budget** | Acceptable infrastructure cost? |
| **Hot Paths** | Which endpoints are high-traffic? |
| **Data Freshness** | How stale can cached data be? |

### The 90-Second Interview Narrative for Performance

1. **Clarify** SLOs (p50/p99 latency, throughput)
2. **Measure** profile production traffic, find bottlenecks
3. **Database** indexes, query optimization, read replicas
4. **Caching** Redis for hot paths, CDN for static
5. **Async** queue slow work, background jobs
6. **Resilience** timeouts, circuit breakers, fallbacks
7. **Monitor** continuous metrics, alert on degradation
8. **Trade-offs** cost vs latency, freshness vs speed

### Performance Anti-Patterns from System Design

| Anti-Pattern | Why It Fails | Correct Approach |
|--------------|--------------|------------------|
| Optimizing without profiling | Developer intuition wrong 70%+ of time | Profile first, then optimize top 3 bottlenecks |
| Caching everything | Memory costs, stale data, invalidation complexity | Cache hot paths only, set appropriate TTLs |
| Reporting averages only | Hides tail latency (p99 users suffer) | Always measure p95/p99, not just average |
| Premature optimization | Wastes time on non-critical code | Optimize critical path after profiling |
| No timeout on external calls | One slow dependency blocks everything | Timeout + circuit breaker + fallback |

### Cache Invalidation Strategies

```
Which invalidation pattern fits?
|
+-- Data changes rarely + staleness OK for minutes?
|   +-- TTL-based (set expiry, auto-refresh)
|
+-- Data changes frequently + must be fresh?
|   +-- Write-through (update cache on every write)
|
+-- Expensive to compute + high read volume?
|   +-- Stale-while-revalidate (serve stale, refresh async)
|
+-- Complex dependencies between cached items?
    +-- Explicit invalidation with cache tags
    +-- Publish/subscribe for cache updates
```

**What I'm Thinking**: "There are only two hard things in computer science: cache invalidation and naming things."
- Start with TTL (simple, predictable)
- Add explicit invalidation only when freshness critical
- Monitor cache hit rate (should be >90% for hot paths)
