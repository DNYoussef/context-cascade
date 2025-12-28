---
name: when-analyzing-performance-use-performance-analysis
description: Comprehensive performance analysis, bottleneck detection, and optimization recommendations for Claude Flow swarms
---

# Performance Analysis SOP

## Overview

Comprehensive performance analysis for Claude Flow swarms including bottleneck detection, profiling, benchmarking, and actionable optimization recommendations.

## Agents & Responsibilities

### performance-analyzer
**Role:** Analyze system performance and identify issues
**Responsibilities:**
- Collect performance metrics
- Analyze resource utilization
- Identify bottlenecks
- Generate analysis reports

### performance-benchmarker
**Role:** Run performance benchmarks and comparisons
**Responsibilities:**
- Execute benchmark suites
- Compare performance across configurations
- Establish performance baselines
- Validate improvements

### perf-analyzer
**Role:** Deep performance profiling and optimization
**Responsibilities:**
- Profile code execution
- Analyze memory usage
- Optimize critical paths
- Recommend improvements

## Phase 1: Establish Baseline

### Objective
Measure current performance and establish baseline metrics.

### Scripts

```bash
# Collect baseline metrics
npx claude-flow@alpha performance baseline \
  --duration 300 \
  --interval 5 \
  --output baseline-metrics.json

# Run benchmark suite
npx claude-flow@alpha benchmark run \
  --type swarm \
  --iterations 10 \
  --output benchmark-results.json

# Profile system resources
npx claude-flow@alpha performance profile \
  --include-cpu \
  --include-memory \
  --include-network \
  --output resource-profile.json

# Collect agent metrics
npx claude-flow@alpha agent metrics --all --format json > agent-metrics.json

# Store baseline
npx claude-flow@alpha memory store \
  --key "performance/baseline" \
  --file baseline-metrics.json

# Generate baseline report
npx claude-flow@alpha performance report \
  --type baseline \
  --metrics baseline-metrics.json \
  --output baseline-report.md
```

### Key Baseline Metrics

**Swarm-Level:**
- Total throughput (tasks/min)
- Average latency (ms)
- Resource utilization (%)
- Error rate (%)
- Coordination overhead (ms)

**Agent-Level:**
- Task completion rate
- Response time (ms)
- CPU usage (%)
- Memory usage (MB)
- Idle time (%)

**System-Level:**
- Total CPU usage (%)
- Total memory usage (MB)
- Network bandwidth (MB/s)
- Disk I/O (MB/s)

### Memory Patterns

```bash
# Store performance baseline
npx claude-flow@alpha memory store \
  --key "performance/baseline/timestamp" \
  --value "$(date -Iseconds)"

npx claude-flow@alpha memory store \
  --key "performance/baseline/metrics" \
  --value '{
    "throughput": 145.2,
    "latency": 38.5,
    "utilization": 0.78,
    "errorRate": 0.012,
    "timestamp": "'$(date -Iseconds)'"
  }'
```

## Phase 2: Profile System

### Objective
Deep profiling of system components to identify performance characteristics.

### Scripts

```bash
# Profile swarm execution
npx claude-flow@alpha performance profile-swarm \
  --duration 300 \
  --sample-rate 100 \
  --output swarm-profile.json

# Profile individual agents
for AGENT in $(npx claude-flow@alpha agent list --format json | jq -r '.[].id'); do
  npx claude-flow@alpha performance profile-agent \
    --agent-id "$AGENT" \
    --duration 60 \
    --output "profiles/agent-$AGENT.json"
done

# Profile memory usage
npx claude-flow@alpha memory profile \
  --show-hotspots \
  --show-leaks \
  --output memory-profile.json

# Profile network communication
npx claude-flow@alpha performance profile-network \
  --show-latency \
  --show-bandwidth \
  --output network-profile.json

# Generate flamegraph
npx claude-flow@alpha performance flamegraph \
  --input swarm-profile.json \
  --output flamegraph.svg

# Analyze CPU hotspots
npx claude-flow@alpha performance hotspots \
  --type cpu \
  --threshold 5 \
  --output cpu-hotspots.json
```

### Profiling Analysis

```bash
# Identify slow functions
SLOW_FUNCTIONS=$(jq '[.profile[] | select(.time > 100)]' swarm-profile.json)

# Identify memory hogs
MEMORY_HOGS=$(jq '[.memory[] | select(.usage > 100)]' memory-profile.json)

# Identify network bottlenecks
NETWORK_ISSUES=$(jq '[.network[] | select(.latency > 50)]' network-profile.json)

echo "Slow Functions: $(echo $SLOW_FUNCTIONS | jq length)"
echo "Memory Hogs: $(echo $MEMORY_HOGS | jq length)"
echo "Network Issues: $(echo $NETWORK_ISSUES | jq length)"
```

## Phase 3: Analyze Issues

### Objective
Identify and categorize performance issues and bottlenecks.

### Scripts

```bash
# Run comprehensive analysis
npx claude-flow@alpha performance analyze \
  --input swarm-profile.json \
  --detect-bottlenecks \
  --detect-memory-leaks \
  --detect-deadlocks \
  --output analysis-results.json

# Identify bottlenecks by type
npx claude-flow@alpha performance bottlenecks \
  --categorize \
  --priority-order \
  --output bottleneck-report.json

# Analyze agent performance
npx claude-flow@alpha agent analyze-performance \
  --all \
  --identify-underperformers \
  --output agent-analysis.json

# Analyze coordination overhead
npx claude-flow@alpha performance coordination-overhead \
  --calculate \
  --breakdown \
  --output coordination-analysis.json

# Root cause analysis
npx claude-flow@alpha performance root-cause \
  --issue "high-latency" \
  --trace-back \
  --output root-cause-analysis.json
```

### Issue Classification

**Critical Issues:**
- Deadlocks
- Memory leaks
- Complete performance degradation
- System instability

**High Priority:**
- Bottlenecks causing >30% slowdown
- High error rates (>5%)
- Resource exhaustion
- Coordination failures

**Medium Priority:**
- Moderate slowdowns (10-30%)
- Suboptimal resource utilization
- Inefficient algorithms
- Poor load balancing

**Low Priority:**
- Minor optimizations (<10% impact)
- Code style issues
- Documentation gaps

### Memory Patterns

```bash
# Store analysis results
npx claude-flow@alpha memory store \
  --key "performance/analysis/issues" \
  --value '{
    "critical": 0,
    "high": 3,
    "medium": 8,
    "low": 12,
    "timestamp": "'$(date -Iseconds)'"
  }'

# Store bottleneck information
npx claude-flow@alpha memory store \
  --key "performance/analysis/bottlenecks" \
  --file bottleneck-report.json
```

## Phase 4: Optimize Performance

### Objective
Apply optimizations based on analysis and measure improvements.

### Scripts

```bash
# Get optimization recommendations
npx claude-flow@alpha performance recommend \
  --based-on analysis-results.json \
  --prioritize \
  --output recommendations.json

# Apply automatic optimizations
npx claude-flow@alpha performance optimize \
  --recommendations recommendations.json \
  --auto-apply safe-optimizations

# Manual optimizations
# 1. Fix identified bottlenecks
# 2. Optimize hot paths
# 3. Reduce coordination overhead
# 4. Improve resource utilization

# Optimize swarm topology
npx claude-flow@alpha swarm optimize-topology \
  --based-on analysis-results.json

# Optimize agent allocation
npx claude-flow@alpha agent rebalance \
  --strategy performance-optimized

# Optimize memory usage
npx claude-flow@alpha memory optimize \
  --reduce-footprint \
  --clear-unused

# Apply neural optimizations
npx claude-flow@alpha neural train \
  --pattern convergent \
  --iterations 10
```

### Optimization Techniques

**Parallelization:**
```bash
# Increase parallelism for independent tasks
npx claude-flow@alpha swarm configure \
  --max-parallel-tasks 8
```

**Caching:**
```bash
# Enable result caching
npx claude-flow@alpha performance cache \
  --enable \
  --strategy lru \
  --max-size 1000
```

**Load Balancing:**
```bash
# Rebalance agent workloads
npx claude-flow@alpha swarm rebalance \
  --strategy adaptive \
  --target-variance 0.1
```

**Resource Allocation:**
```bash
# Optimize resource allocation
npx claude-flow@alpha agent configure --all \
  --memory-limit auto \
  --cpu-limit auto
```

## Phase 5: Validate Results

### Objective
Measure improvements and validate optimization effectiveness.

### Scripts

```bash
# Collect post-optimization metrics
npx claude-flow@alpha performance baseline \
  --duration 300 \
  --output optimized-metrics.json

# Run comparison benchmark
npx claude-flow@alpha benchmark run \
  --type swarm \
  --iterations 10 \
  --output optimized-benchmark.json

# Compare before/after
npx claude-flow@alpha performance compare \
  --baseline baseline-metrics.json \
  --current optimized-metrics.json \
  --output improvement-report.json

# Calculate improvements
THROUGHPUT_IMPROVEMENT=$(jq '.improvements.throughput.percentage' improvement-report.json)
LATENCY_IMPROVEMENT=$(jq '.improvements.latency.percentage' improvement-report.json)

echo "Throughput improved by: $THROUGHPUT_IMPROVEMENT%"
echo "Latency improved by: $LATENCY_IMPROVEMENT%"

# Validate improvements meet targets
npx claude-flow@alpha performance validate \
  --improvements improvement-report.json \
  --targets performance-targets.json

# Generate final report
npx claude-flow@alpha performance report \
  --type comprehensive \
  --include-baseline \
  --include-analysis \
  --include-optimizations \
  --include-results \
  --output final-performance-report.md

# Archive performance data
npx claude-flow@alpha performance archive \
  --output performance-archive-$(date +%Y%m%d).tar.gz
```

### Validation Criteria

**Minimum Improvements:**
- Throughput: +15%
- Latency: -20%
- Resource utilization: More balanced (variance <10%)
- Error rate: -50% or <1%

**Validation Checks:**
```bash
# Check if improvements meet targets
if (( $(echo "$THROUGHPUT_IMPROVEMENT >= 15" | bc -l) )); then
  echo "✓ Throughput target met"
else
  echo "✗ Throughput target not met"
fi

if (( $(echo "$LATENCY_IMPROVEMENT >= 20" | bc -l) )); then
  echo "✓ Latency target met"
else
  echo "✗ Latency target not met"
fi
```

## Success Criteria

- [ ] Baseline established
- [ ] System profiled
- [ ] Issues identified and categorized
- [ ] Optimizations applied
- [ ] Improvements validated

### Performance Targets
- Throughput improvement: ≥15%
- Latency reduction: ≥20%
- Resource utilization variance: <10%
- Error rate: <1%
- Optimization overhead: <5%

## Best Practices

1. **Baseline First:** Always establish baseline before optimizing
2. **Measure Everything:** Comprehensive metrics collection
3. **Identify Bottlenecks:** Focus on critical path
4. **Incremental Optimization:** Apply optimizations incrementally
5. **Validate Improvements:** Always measure after optimizing
6. **Document Changes:** Record all optimization actions
7. **Regression Testing:** Ensure optimizations don't break functionality
8. **Continuous Monitoring:** Track performance over time

## Common Issues & Solutions

### Issue: No Performance Improvement
**Symptoms:** Metrics unchanged after optimization
**Solution:** Re-analyze bottlenecks, verify optimizations applied correctly

### Issue: Performance Regression
**Symptoms:** Performance worse after optimization
**Solution:** Rollback changes, re-evaluate optimization strategy

### Issue: Inconsistent Results
**Symptoms:** Performance varies significantly between runs
**Solution:** Increase measurement duration, check for external factors

## Integration Points

- **advanced-swarm:** For topology optimization
- **swarm-orchestration:** For coordination optimization
- **cascade-orchestrator:** For workflow optimization

## References

- Performance Analysis Methodologies
- Profiling Techniques
- Optimization Patterns
- Benchmarking Best Practices

## Core Principles

Performance Analysis operates on 3 fundamental principles:

### Principle 1: Baseline Before Optimize - Measure Twice, Cut Once
Optimization without baseline metrics is guesswork. Premature optimization wastes time fixing non-bottlenecks while real issues remain hidden. This principle ensures data-driven decision making.

In practice:
- Establish baseline metrics (throughput, latency, resource utilization) before any optimization work
- Run benchmarks for 300+ seconds to smooth out variance and warm up caches
- Store baseline in Memory MCP with ISO timestamps for historical comparison
- Define success criteria upfront (15% throughput gain, 20% latency reduction) before optimization begins

### Principle 2: Profile to Identify, Don't Assume Bottlenecks
Developer intuition about performance bottlenecks is notoriously unreliable. Profiling tools reveal actual hotspots, which are often surprising (e.g., JSON serialization, not database queries). This principle eliminates wasted effort.

In practice:
- Use flamegraphs to visualize CPU hotspots and identify functions consuming >5% execution time
- Profile memory allocation to detect leaks, excessive GC pressure, and large object allocations
- Trace network calls to identify high-latency dependencies and coordination overhead
- Analyze coordination overhead separately (swarm-level metrics vs agent-level metrics)

### Principle 3: Incremental Optimization with Regression Testing
Applying all optimizations at once makes it impossible to attribute improvements or identify regressions. Small, validated changes compound into major gains. This principle ensures safe, measurable progress.

In practice:
- Apply one optimization at a time (fix hottest path first, then retest)
- Validate improvement meets targets (15% gain) before proceeding to next optimization
- Run regression tests after each change to ensure functionality is preserved
- Rollback changes that degrade performance or introduce bugs

## Common Anti-Patterns

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| **Optimizing Without Profiling** | Developers guess at bottlenecks based on intuition, wasting hours optimizing code that consumes <1% of execution time while real bottlenecks remain unfixed. | Always profile first. Use flamegraphs to identify CPU hotspots. Focus optimization effort on functions consuming >5% execution time. Measure before/after. |
| **No Baseline Metrics** | Starting optimization without baseline makes it impossible to measure improvement. You cannot know if changes helped, hurt, or had no effect. | Run comprehensive baseline before any optimization (Phase 1). Store metrics in Memory MCP with timestamps. Define success criteria (15% throughput gain). Compare post-optimization metrics to baseline. |
| **Ignoring Coordination Overhead** | Focusing only on agent-level performance while swarm coordination consumes 30-50% of latency. Parallel agents with high coordination overhead perform worse than sequential execution. | Profile swarm-level coordination overhead separately. Measure inter-agent communication latency. Optimize task distribution and reduce message passing. Consider agent topology changes. |
| **Short Benchmark Durations** | Running benchmarks for <60 seconds leads to noisy results dominated by JIT warmup, cache misses, and outliers. Cannot distinguish signal from noise. | Run benchmarks for 300+ seconds to smooth variance. Discard first 30 seconds to allow JIT compilation and cache warmup. Use percentiles (p95, p99) instead of averages. |
| **Batch Optimizations Without Isolation** | Applying multiple optimizations simultaneously makes it impossible to attribute gains to specific changes. If performance degrades, cannot identify root cause. | Apply one optimization at a time. Measure improvement after each change. Rollback if target not met or regression detected. Document what worked for future reference. |

## Conclusion

The Performance Analysis skill provides a systematic, data-driven approach to identifying and eliminating performance bottlenecks in distributed swarm systems. By following the three core principles of baseline establishment, profiling-driven optimization, and incremental validation, you ensure that performance work delivers measurable, sustainable improvements rather than guesswork and regressions.

The 5-phase workflow (Baseline, Profile, Analyze, Optimize, Validate) is designed to minimize wasted effort and maximize impact. The emphasis on comprehensive profiling (CPU, memory, network) ensures that you optimize the right bottlenecks, while the incremental optimization approach with regression testing prevents performance gains from being offset by hidden regressions. The anti-patterns table serves as a critical checklist to avoid common mistakes that plague performance work.

This skill is particularly valuable when optimizing Claude Flow swarms, debugging high-latency distributed systems, or preparing applications for production scale. Whether you are troubleshooting a 2x slowdown in swarm execution, reducing coordination overhead in multi-agent workflows, or improving resource utilization to reduce infrastructure costs, the methodologies documented here provide a proven framework. Combined with the neural optimization techniques, memory profiling, and benchmark validation, you have everything needed to systematically improve performance while maintaining system stability.