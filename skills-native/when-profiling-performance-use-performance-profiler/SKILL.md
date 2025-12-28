---
name: when-profiling-performance-use-performance-profiler
description: Comprehensive performance profiling, bottleneck detection, and optimization system
---

# Performance Profiler Skill

## Overview

**When profiling performance, use performance-profiler** to measure, analyze, and optimize application performance across CPU, memory, I/O, and network dimensions.

## MECE Breakdown

### Mutually Exclusive Components:
1. **Baseline Phase**: Establish current performance metrics
2. **Detection Phase**: Identify bottlenecks and hot paths
3. **Analysis Phase**: Root cause analysis and impact assessment
4. **Optimization Phase**: Generate and prioritize recommendations
5. **Implementation Phase**: Apply optimizations with agent assistance
6. **Validation Phase**: Benchmark improvements and verify gains

### Collectively Exhaustive Coverage:
- **CPU Profiling**: Function execution time, hot paths, call graphs
- **Memory Profiling**: Heap usage, allocations, leaks, garbage collection
- **I/O Profiling**: File system, database, network latency
- **Network Profiling**: Request timing, bandwidth, connection pooling
- **Concurrency**: Thread utilization, lock contention, async operations
- **Algorithm Analysis**: Time complexity, space complexity
- **Cache Analysis**: Hit rates, cache misses, invalidation patterns
- **Database**: Query performance, N+1 problems, index usage

## Features

### Core Capabilities:
- Multi-dimensional performance profiling (CPU, memory, I/O, network)
- Automated bottleneck detection with prioritization
- Real-time profiling and historical analysis
- Flame graph generation for visual analysis
- Memory leak detection and heap snapshots
- Database query optimization
- Algorithmic complexity analysis
- A/B comparison of before/after optimizations
- Production-safe profiling with minimal overhead
- Integration with APM tools (New Relic, DataDog, etc.)

### Profiling Modes:
- **Quick Scan**: 30-second lightweight profiling
- **Standard**: 5-minute comprehensive analysis
- **Deep**: 30-minute detailed investigation
- **Continuous**: Long-running production monitoring
- **Stress Test**: Load-based profiling under high traffic

## Usage

### Slash Command:
```bash
/profile [path] [--mode quick|standard|deep] [--target cpu|memory|io|network|all]
```

### Subagent Invocation:
```javascript
Task("Performance Profiler", "Profile ./app with deep CPU and memory analysis", "performance-analyzer")
```

### MCP Tool:
```javascript
mcp__performance-profiler__analyze({
  project_path: "./app",
  profiling_mode: "standard",
  targets: ["cpu", "memory", "io"],
  generate_optimizations: true
})
```

## Architecture

### Phase 1: Baseline Measurement
1. Establish current performance metrics
2. Define performance budgets
3. Set up monitoring infrastructure
4. Capture baseline snapshots

### Phase 2: Bottleneck Detection
1. CPU profiling (sampling or instrumentation)
2. Memory profiling (heap analysis)
3. I/O profiling (syscall tracing)
4. Network profiling (packet analysis)
5. Database profiling (query logs)

### Phase 3: Root Cause Analysis
1. Correlate metrics across dimensions
2. Identify causal relationships
3. Calculate performance impact
4. Prioritize issues by severity

### Phase 4: Optimization Generation
1. Algorithmic improvements
2. Caching strategies
3. Parallelization opportunities
4. Database query optimization
5. Memory optimization
6. Network optimization

### Phase 5: Implementation
1. Generate optimized code with coder agent
2. Apply database optimizations
3. Configure caching layers
4. Implement parallelization

### Phase 6: Validation
1. Run benchmark suite
2. Compare before/after metrics
3. Verify no regressions
4. Generate performance report

## Output Formats

### Performance Report:
```json
{
  "project": "my-app",
  "profiling_mode": "standard",
  "duration_seconds": 300,
  "baseline": {
    "requests_per_second": 1247,
    "avg_response_time_ms": 123,
    "p95_response_time_ms": 456,
    "p99_response_time_ms": 789,
    "cpu_usage_percent": 67,
    "memory_usage_mb": 512,
    "error_rate_percent": 0.1
  },
  "bottlenecks": [
    {
      "type": "cpu",
      "severity": "high",
      "function": "processData",
      "time_percent": 34.5,
      "calls": 123456,
      "avg_time_ms": 2.3,
      "recommendation": "Optimize algorithm complexity from O(n²) to O(n log n)"
    }
  ],
  "optimizations": [...],
  "estimated_improvement": {
    "throughput_increase": "3.2x",
    "latency_reduction": "68%",
    "memory_reduction": "45%"
  }
}
```

### Flame Graph:
Interactive SVG flame graph showing call stack with time proportions

### Heap Snapshot:
Memory allocation breakdown with retention paths

### Optimization Report:
Prioritized list of actionable improvements with code examples

## Examples

### Example 1: Quick CPU Profiling
```bash
/profile ./my-app --mode quick --target cpu
```

### Example 2: Deep Memory Analysis
```bash
/profile ./my-app --mode deep --target memory --detect-leaks
```

### Example 3: Full Stack Optimization
```bash
/profile ./my-app --mode standard --target all --optimize --benchmark
```

### Example 4: Database Query Optimization
```bash
/profile ./my-app --mode standard --target io --database --explain-queries
```

## Integration with Claude-Flow

### Coordination Pattern:
```javascript
// Step 1: Initialize profiling swarm
mcp__claude-flow__swarm_init({ topology: "star", maxAgents: 5 })

// Step 2: Spawn specialized agents
[Parallel Execution]:
  Task("CPU Profiler", "Profile CPU usage and identify hot paths in ./app", "performance-analyzer")
  Task("Memory Profiler", "Analyze heap usage and detect memory leaks", "performance-analyzer")
  Task("I/O Profiler", "Profile file system and database operations", "performance-analyzer")
  Task("Network Profiler", "Analyze network requests and identify slow endpoints", "performance-analyzer")
  Task("Optimizer", "Generate optimization recommendations based on profiling data", "optimizer")

// Step 3: Implementation agent applies optimizations
[Sequential Execution]:
  Task("Coder", "Implement recommended optimizations from profiling analysis", "coder")
  Task("Benchmarker", "Run benchmark suite and validate improvements", "performance-benchmarker")
```

## Configuration

### Default Settings:
```json
{
  "profiling": {
    "sampling_rate_hz": 99,
    "stack_depth": 128,
    "include_native_code": false,
    "track_allocations": true
  },
  "thresholds": {
    "cpu_hot_path_percent": 10,
    "memory_leak_growth_mb": 10,
    "slow_query_ms": 100,
    "slow_request_ms": 1000
  },
  "optimization": {
    "auto_apply": false,
    "require_approval": true,
    "run_tests_before": true,
    "run_benchmarks_after": true
  },
  "output": {
    "flame_graph": true,
    "heap_snapshot": true,
    "call_tree": true,
    "recommendations": true
  }
}
```

## Profiling Techniques

### CPU Profiling:
- **Sampling**: Periodic stack sampling (low overhead)
- **Instrumentation**: Function entry/exit hooks (accurate but higher overhead)
- **Tracing**: Event-based profiling

### Memory Profiling:
- **Heap Snapshots**: Point-in-time memory state
- **Allocation Tracking**: Record all allocations
- **Leak Detection**: Compare snapshots over time
- **GC Analysis**: Garbage collection patterns

### I/O Profiling:
- **Syscall Tracing**: Track system calls (strace, dtrace)
- **File System**: Monitor read/write operations
- **Database**: Query logging and EXPLAIN ANALYZE
- **Network**: Packet capture and request timing

### Concurrency Profiling:
- **Thread Analysis**: CPU utilization per thread
- **Lock Contention**: Identify blocking operations
- **Async Operations**: Promise/callback timing

## Performance Optimization Strategies

### Algorithmic:
- Reduce time complexity (O(n²) → O(n log n))
- Use appropriate data structures
- Eliminate unnecessary work
- Memoization and dynamic programming

### Caching:
- In-memory caching (Redis, Memcached)
- CDN for static assets
- HTTP caching headers
- Query result caching

### Parallelization:
- Multi-threading
- Worker pools
- Async I/O
- Batching operations

### Database:
- Add missing indexes
- Optimize queries
- Reduce N+1 queries
- Connection pooling
- Read replicas

### Memory:
- Object pooling
- Reduce allocations
- Stream processing
- Compression

### Network:
- Connection keep-alive
- HTTP/2 or HTTP/3
- Compression
- Request batching
- Rate limiting

## Performance Budgets

### Frontend:
- Time to First Byte (TTFB): < 200ms
- First Contentful Paint (FCP): < 1.8s
- Largest Contentful Paint (LCP): < 2.5s
- Time to Interactive (TTI): < 3.8s
- Total Blocking Time (TBT): < 200ms
- Cumulative Layout Shift (CLS): < 0.1

### Backend:
- API Response Time (p50): < 100ms
- API Response Time (p95): < 500ms
- API Response Time (p99): < 1000ms
- Throughput: > 1000 req/s
- Error Rate: < 0.1%
- CPU Usage: < 70%
- Memory Usage: < 80%

### Database:
- Query Time (p50): < 10ms
- Query Time (p95): < 50ms
- Query Time (p99): < 100ms
- Connection Pool Utilization: < 80%

## Best Practices

1. Profile production workloads when possible
2. Use production-like data volumes
3. Profile under realistic load
4. Measure multiple times for consistency
5. Focus on p95/p99, not just averages
6. Optimize bottlenecks in order of impact
7. Always benchmark before and after
8. Monitor for regressions in CI/CD
9. Set up continuous profiling
10. Track performance over time

## Troubleshooting

### Issue: High CPU usage but no obvious hot path
**Solution**: Check for excessive small function calls, increase sampling rate, or use instrumentation

### Issue: Memory grows continuously
**Solution**: Run heap snapshot comparison to identify leak sources

### Issue: Slow database queries
**Solution**: Use EXPLAIN ANALYZE, check for missing indexes, analyze query plans

### Issue: High latency but low CPU
**Solution**: Profile I/O operations, check for blocking synchronous calls

## See Also

- PROCESS.md - Detailed step-by-step profiling workflow
- README.md - Quick start guide
- subagent-performance-profiler.md - Agent implementation details
- slash-command-profile.sh - Command-line interface
- mcp-performance-profiler.json - MCP tool schema

## Core Principles

### 1. Profiling Under Realistic Load is Non-Negotiable
Profiling on empty databases with synthetic test data produces performance profiles unrelated to production behavior. A function that takes 50ms with 100 database rows takes 5000ms with 100,000 production rows when it triggers O(n^2) query patterns. Optimizing based on unrealistic profiling wastes engineering effort on bottlenecks that don't exist in production while ignoring actual performance cliffs.

**In practice**: Before profiling, restore production database snapshot to staging environment (anonymize PII but preserve data volume and distribution). Generate realistic load using production traffic patterns: if production serves 1000 req/s with 70% reads and 30% writes, profiling load generator should match those ratios. Use `scripts/load-generator.sh` with production request logs as input (replays actual user behavior patterns, not synthetic uniform load). Profile under production-like concurrency: if production runs 50 concurrent workers, profile with 50 workers. This reveals real bottlenecks: database connection pool exhaustion under load, cache stampede during traffic spikes, memory leaks that only manifest after hours of sustained traffic.

### 2. Optimize Bottlenecks in Impact Order, Not Discovery Order
The first bottleneck discovered during profiling is rarely the most impactful. A function consuming 5% of CPU that's called once per request is less critical than a function consuming 1% of CPU called 100 times per request (total 100% CPU impact). Optimizing in discovery order results in marginal improvements (5% faster) while ignoring multiplicative improvements (50% faster from eliminating N+1 queries).

**In practice**: Use flame graph visualization to identify hot paths by total CPU percentage. Sort bottlenecks by impact score: CPU percentage x call frequency x user-facing latency contribution. For a web API: Database query consuming 40% of request time with 200ms avg latency = 80ms user impact per request. In-memory JSON serialization consuming 10% of request time with 50ms avg latency = 5ms user impact. Optimize database query first (16x higher impact). The performance-analyzer agent ranks bottlenecks automatically using this scoring, preventing wasted effort on low-impact optimizations.

### 3. Performance Budgets Prevent Regression, Not Initial Optimization
Setting performance budgets after optimization is performative documentation - the budgets encode current performance, not acceptable performance. Budgets prevent regression by failing CI builds when new code degrades performance below thresholds, but only if thresholds are set proactively based on user experience requirements, not reactively based on current implementation.

**In practice**: Define performance budgets from user experience requirements BEFORE profiling: If UX research shows users abandon checkout flows at >3s page load, set budget: Time to Interactive <2.5s (safety margin). API serving real-time dashboards requires <500ms p95 latency (perceived as instant). Batch processing pipelines tolerate 10min runtime for hourly jobs. Codify budgets in `config/performance-budgets.json` and enforce in CI: `scripts/performance-ci.sh` runs benchmark suite on every PR, fails build if any metric exceeds budget. This prevents death-by-thousand-cuts performance degradation where each PR adds 50ms latency until application becomes unusable.

## Anti-Patterns

| Anti-Pattern | Problem | Solution |
|-------------|---------|----------|
| **Premature Optimization Based on Intuition** | Developer "knows" JSON parsing is slow, spends 2 days implementing custom binary protocol. Profiling reveals JSON parsing consumed 0.5% of request time, actual bottleneck was N+1 database queries consuming 60% of time. Binary protocol improved performance 0.5%, fixing N+1 queries would improve 60% (120x more impact). Engineering effort wasted. | ALWAYS profile BEFORE optimizing. Run `scripts/profiler.sh --mode standard --target all` to measure actual performance characteristics. Flame graph reveals CPU hotspots, memory profiler shows allocation bottlenecks, I/O profiler identifies slow database queries. Optimize top 3 bottlenecks by measured impact (CPU%, memory%, latency contribution), not assumed bottlenecks. Re-profile after each optimization to validate impact and identify next bottleneck. |
| **Profiling with Unrealistic Data Volumes** | Profile application with 1000-row test database. Queries complete in <10ms, no performance issues detected. Deploy to production with 10M-row database. Same queries take 5000ms, application unusable. Root cause: missing database index, not detected because test data too small to trigger performance cliff. | Generate production-scale test data using `scripts/data-generator.sh --scale production --rows 10000000`. Profile against realistic data volumes: if production has 10M users, 100M events, profile with similar scale. This exposes algorithmic complexity issues (O(n) becomes O(n^2) at scale), missing database indexes (full table scans acceptable at 1000 rows, catastrophic at 10M rows), and memory issues (in-memory caching works for 1000 rows, causes OOM for 10M rows). |
| **Ignoring p95/p99 Latency in Favor of Averages** | API reports average response time 100ms, declares success. Users complain of slow performance. Investigation reveals: p50=50ms (fast), p95=2000ms (slow), p99=8000ms (extremely slow). 5% of requests take 20x longer than average, creating terrible user experience for 1 in 20 requests. Average latency hides performance problems affecting significant user population. | ALWAYS measure and optimize for p95/p99 latency, not averages. Run `scripts/load-test.sh --duration 300 --report-percentiles` to collect latency distribution. Set performance budgets on tail latency: p95 <500ms, p99 <1000ms. Profile slow requests specifically: `scripts/profiler.sh --filter "latency>1000ms"` captures profile of slowest 1% of requests. Common root causes: cache misses (cold cache requests 10x slower), lock contention (requests waiting for shared resource), garbage collection pauses (GC stalls slow minority of requests). |

## Common Anti-Patterns

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| **Premature Optimization Without Profiling** | Developer "knows" JSON parsing is slow, spends 2 days implementing binary protocol. Profiling reveals JSON parsing consumed 0.5% request time, actual bottleneck was N+1 queries at 60%. Binary protocol improved 0.5%, fixing N+1 would improve 60% (120x more impact). | ALWAYS profile BEFORE optimizing. Run profiler --mode standard --target all to measure actual characteristics. Flamegraph reveals CPU hotspots, memory profiler shows allocations, I/O profiler identifies slow queries. Optimize top 3 bottlenecks by measured impact, not assumptions. |
| **Profiling with Unrealistic Data** | Profile with 1000-row test database. Queries complete <10ms, no issues. Deploy to production with 10M-row database. Same queries take 5000ms, app unusable. Root cause: missing database index not detected because test data too small to trigger performance cliff. | Generate production-scale test data with data-generator.sh --scale production --rows 10000000. Profile against realistic volumes. Exposes algorithmic complexity (O(n) becomes O(n²) at scale), missing indexes (full scans acceptable at 1000 rows, catastrophic at 10M), memory issues (caching works for 1000 rows, causes OOM for 10M). |
| **Ignoring Tail Latency for Averages** | API reports avg 100ms, declares success. Users complain of slowness. Investigation: p50=50ms, p95=2000ms, p99=8000ms. 5% requests take 20x longer than average, terrible UX for 1 in 20 requests. Averages hide problems affecting significant population. | ALWAYS measure p95/p99 latency, not averages. Run load-test.sh --duration 300 --report-percentiles. Set budgets on tail latency: p95 <500ms, p99 <1000ms. Profile slow requests: profiler.sh --filter "latency>1000ms" captures slowest 1%. Common causes: cache misses, lock contention, GC pauses. |

---

## Conclusion

Performance profiling transforms intuition-based optimization into data-driven engineering. The workflows documented here (realistic load profiling, impact-based bottleneck prioritization, flame graph analysis, algorithmic optimization) eliminate guesswork from performance engineering by measuring actual system behavior under production-like conditions. The fundamental insight: performance characteristics are emergent properties of system architecture, data volume, and load patterns - they cannot be predicted from code inspection alone.

Effective profiling requires three disciplines: production-realistic conditions (data volumes matching production scale, load patterns matching production traffic distribution, concurrency matching production deployment), impact-based prioritization (optimize bottlenecks by CPU percentage x call frequency x user impact, not discovery order), and comprehensive measurement (CPU, memory, I/O, network profiling reveals different bottleneck categories, single-dimension profiling misses cross-cutting issues). Without these disciplines, profiling produces misleading results that waste engineering effort on low-impact optimizations while ignoring critical performance cliffs.

The multi-agent profiling architecture (parallel CPU/memory/I/O/network profilers coordinated by performance-analyzer) enables comprehensive performance characterization in a single profiling run. This is critical for production systems where profiling overhead must be minimized - running four separate profiling sessions quadruples measurement overhead and risks perturbing system behavior. The analyzer agent synthesizes results across profiling dimensions, identifying cross-cutting bottlenecks (database query causing both CPU hotspot from result processing AND I/O bottleneck from slow disk reads).

Implementation sequencing: Start with flame graph profiling under realistic load (identifies CPU bottlenecks, highest ROI optimization category), then add memory profiling for allocation-heavy code paths (prevents memory leaks and excessive GC), then add I/O profiling for data-intensive operations (optimizes database queries, file system access). Attempting comprehensive profiling without production-realistic test data wastes time characterizing performance properties that don't exist in production. The upfront investment in production-scale test environments (typically 1-2 days) prevents weeks of optimizing wrong bottlenecks.