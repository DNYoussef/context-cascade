# Performance Analysis - Quick Start

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



Comprehensive performance analysis and optimization for Claude Flow swarms.

## Quick Start

```bash
# 1. Establish baseline
npx claude-flow@alpha performance baseline --duration 300 --output baseline.json

# 2. Profile system
npx claude-flow@alpha performance profile-swarm --duration 300 --output profile.json

# 3. Analyze issues
npx claude-flow@alpha performance analyze --detect-bottlenecks --output analysis.json

# 4. Optimize
npx claude-flow@alpha performance optimize --recommendations recommendations.json

# 5. Validate
npx claude-flow@alpha performance compare --baseline baseline.json --current optimized.json
```

## Agents
- **performance-analyzer:** Performance analysis
- **performance-benchmarker:** Benchmarking
- **perf-analyzer:** Deep profiling

## Success Metrics
- [assert|neutral] Throughput improvement: ≥15% [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] Latency reduction: ≥20% [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] Error rate: <1% [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] Promise: `<promise>README_VERIX_COMPLIANT</promise>`* [ground:acceptance-criteria] [conf:0.90] [state:provisional]
