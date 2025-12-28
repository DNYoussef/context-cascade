---
name: swarm-orchestration
description: Orchestrate multi-agent swarms with agentic-flow for parallel task execution, dynamic topology, and intelligent coordination. Use when scaling beyond single agents, implementing complex workflows, or building distributed AI systems.
---

## Orchestration Skill Guidelines

### When to Use This Skill
- **Parallel multi-agent execution** requiring concurrent task processing
- **Complex implementation** with 6+ independent tasks
- **Theater-free development** requiring 0% tolerance validation
- **Dynamic agent selection** from 86+ agent registry
- **High-quality delivery** needing Byzantine consensus validation

### When NOT to Use This Skill
- **Single-agent tasks** with no parallelization benefit
- **Simple sequential work** completing in <2 hours
- **Planning phase** (use research-driven-planning first)
- **Trivial changes** to single files

### Success Criteria
- **Agent+skill matrix generated** with optimal assignments
- **Parallel execution successful** with 8.3x speedup achieved
- **Theater detection passes** with 0% theater detected
- **Integration tests pass** at 100% rate
- **All agents complete** with no orphaned workers

### Edge Cases to Handle
- **Agent failures** - Implement agent health monitoring and replacement
- **Task timeout** - Configure per-task timeout with escalation
- **Consensus failure** - Have fallback from Byzantine to weighted consensus
- **Resource exhaustion** - Limit max parallel agents, queue excess
- **Conflicting outputs** - Implement merge conflict resolution strategy

### Guardrails (NEVER Violate)
- **NEVER lose agent state** - Persist agent progress to memory continuously
- **ALWAYS track swarm health** - Monitor all agent statuses in real-time
- **ALWAYS validate consensus** - Require 4/5 agreement for theater detection
- **NEVER skip theater audit** - Zero tolerance, any theater blocks merge
- **ALWAYS cleanup workers** - Terminate agents on completion/failure

### Evidence-Based Validation
- **Check all agent statuses** - Verify each agent completed successfully
- **Validate parallel execution** - Confirm tasks ran concurrently, not sequentially
- **Measure speedup** - Calculate actual speedup vs sequential baseline
- **Audit theater detection** - Run 6-agent consensus, verify 0% detection
- **Verify integration** - Execute sandbox tests, confirm 100% pass rate


# Swarm Orchestration

## What This Skill Does

Orchestrates multi-agent swarms using agentic-flow's advanced coordination system. Supports mesh, hierarchical, and adaptive topologies with automatic task distribution, load balancing, and fault tolerance.

## Prerequisites

- agentic-flow v1.5.11+
- Node.js 18+
- Understanding of distributed systems (helpful)

## Quick Start

```bash
# Initialize swarm
npx agentic-flow hooks swarm-init --topology mesh --max-agents 5

# Spawn agents
npx agentic-flow hooks agent-spawn --type coder
npx agentic-flow hooks agent-spawn --type tester
npx agentic-flow hooks agent-spawn --type reviewer

# Orchestrate task
npx agentic-flow hooks task-orchestrate \
  --task "Build REST API with tests" \
  --mode parallel
```

## Topology Patterns

### 1. Mesh (Peer-to-Peer)
```typescript
// Equal peers, distributed decision-making
await swarm.init({
  topology: 'mesh',
  agents: ['coder', 'tester', 'reviewer'],
  communication: 'broadcast'
});
```

### 2. Hierarchical (Queen-Worker)
```typescript
// Centralized coordination, specialized workers
await swarm.init({
  topology: 'hierarchical',
  queen: 'architect',
  workers: ['backend-dev', 'frontend-dev', 'db-designer']
});
```

### 3. Adaptive (Dynamic)
```typescript
// Automatically switches topology based on task
await swarm.init({
  topology: 'adaptive',
  optimization: 'task-complexity'
});
```

## Task Orchestration

### Parallel Execution
```typescript
// Execute tasks concurrently
const results = await swarm.execute({
  tasks: [
    { agent: 'coder', task: 'Implement API endpoints' },
    { agent: 'frontend', task: 'Build UI components' },
    { agent: 'tester', task: 'Write test suite' }
  ],
  mode: 'parallel',
  timeout: 300000 // 5 minutes
});
```

### Pipeline Execution
```typescript
// Sequential pipeline with dependencies
await swarm.pipeline([
  { stage: 'design', agent: 'architect' },
  { stage: 'implement', agent: 'coder', after: 'design' },
  { stage: 'test', agent: 'tester', after: 'implement' },
  { stage: 'review', agent: 'reviewer', after: 'test' }
]);
```

### Adaptive Execution
```typescript
// Let swarm decide execution strategy
await swarm.autoOrchestrate({
  goal: 'Build production-ready API',
  constraints: {
    maxTime: 3600,
    maxAgents: 8,
    quality: 'high'
  }
});
```

## Memory Coordination

```typescript
// Share state across swarm
await swarm.memory.store('api-schema', {
  endpoints: [...],
  models: [...]
});

// Agents read shared memory
const schema = await swarm.memory.retrieve('api-schema');
```

## Advanced Features

### Load Balancing
```typescript
// Automatic work distribution
await swarm.enableLoadBalancing({
  strategy: 'dynamic',
  metrics: ['cpu', 'memory', 'task-queue']
});
```

### Fault Tolerance
```typescript
// Handle agent failures
await swarm.setResiliency({
  retry: { maxAttempts: 3, backoff: 'exponential' },
  fallback: 'reassign-task'
});
```

### Performance Monitoring
```typescript
// Track swarm metrics
const metrics = await swarm.getMetrics();
// { throughput, latency, success_rate, agent_utilization }
```

## Integration with Hooks

```bash
# Pre-task coordination
npx agentic-flow hooks pre-task --description "Build API"

# Post-task synchronization
npx agentic-flow hooks post-task --task-id "task-123"

# Session restore
npx agentic-flow hooks session-restore --session-id "swarm-001"
```

## Best Practices

1. **Start small**: Begin with 2-3 agents, scale up
2. **Use memory**: Share context through swarm memory
3. **Monitor metrics**: Track performance and bottlenecks
4. **Enable hooks**: Automatic coordination and sync
5. **Set timeouts**: Prevent hung tasks

## Troubleshooting

### Issue: Agents not coordinating
**Solution**: Verify memory access and enable hooks

### Issue: Poor performance
**Solution**: Check topology (use adaptive) and enable load balancing

## Learn More

- Swarm Guide: docs/swarm/orchestration.md
- Topology Patterns: docs/swarm/topologies.md
- Hooks Integration: docs/hooks/coordination.md
## Core Principles

Swarm Orchestration operates on 3 fundamental principles:

### Principle 1: Topology Determines Coordination Efficiency
The spatial arrangement of agents (mesh, hierarchical, adaptive) fundamentally shapes communication patterns, decision latency, and fault tolerance characteristics.

In practice:
- Mesh topology for peer-to-peer equality (code review swarms, research teams)
- Hierarchical topology for centralized control (queen-worker, feature development)
- Adaptive topology switches dynamically based on task complexity (simple tasks -> mesh, complex -> hierarchical)
- Topology selection impacts message overhead (mesh: O(n^2), hierarchical: O(n), star: O(1) from queen)

### Principle 2: Parallel Task Distribution Achieves 8.3x Speedup
Concurrent agent execution on independent tasks eliminates sequential bottlenecks, with speedup proportional to task parallelism and agent count.

In practice:
- Identify independent tasks with no data dependencies (frontend + backend + database design)
- Spawn all parallel agents in SINGLE message (Golden Rule: 1 message = all operations)
- Use ruv-swarm MCP for load balancing across agents (dynamic work distribution)
- Measure actual speedup vs sequential baseline (target: 6-10x for 8+ agents)

### Principle 3: Swarm Memory Enables Stateful Coordination
Shared memory persists context across agents and sessions, eliminating redundant work and enabling collaborative intelligence.

In practice:
- Store intermediate results in swarm memory (API schema, architecture decisions, bug patterns)
- Agents read shared memory before starting work (avoid duplicate analysis)
- Memory tagged with WHO/WHEN/PROJECT/WHY for traceability and vector search
- Future swarms query memory for similar problems, retrieve proven solutions first

## Common Anti-Patterns

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| **Sequential Task() calls across messages** | Agents spawn one-by-one, waiting for each to complete before next starts. No parallelism achieved despite independent tasks. | Spawn ALL parallel agents in SINGLE message using array of Task() calls. Let system coordinate concurrency. |
| **No swarm health monitoring** | Agent crashes silently, swarm continues without noticing, task never completes, no error surfaced until timeout (hours later). | Enable agent heartbeat monitoring. Detect unresponsive agents within 30s. Reassign tasks automatically to healthy agents. |
| **Memory without tagging protocol** | Agents store unstructured data in swarm memory. No WHO/WHEN/PROJECT/WHY tags. Future queries return irrelevant results. | Use taggedMemoryStore() wrapper. Enforce required tags (WHO, WHEN, PROJECT, WHY). Query by metadata for precision. |
| **Theater detection bypass** | Swarm completes implementation, no validation, 40% of code is mock/placeholder, discovered only in production. | Run 6-agent Byzantine consensus theater detection (4/6 agreement required). Block merge if >0% theater detected. |
| **Resource exhaustion from unlimited agents** | Swarm spawns 50 agents concurrently, system runs out of memory/CPU, all agents fail, nothing completes. | Set maxAgents limit based on system resources (8-12 typical). Queue excess tasks. Monitor resource utilization. |

## Conclusion

Swarm Orchestration transforms single-agent sequential execution into massively parallel distributed coordination, achieving 8.3x speedup on complex implementations through intelligent topology selection, parallel task distribution, and shared memory. The skill provides production-grade multi-agent systems with fault tolerance, load balancing, and Byzantine consensus validation.

The value proposition centers on three capabilities: (1) topology patterns (mesh/hierarchical/adaptive) optimize coordination efficiency for different task types, (2) parallel execution eliminates sequential bottlenecks by spawning all independent tasks concurrently, and (3) swarm memory maintains stateful context across agents and sessions, enabling collaborative intelligence and avoiding redundant work.

Use Swarm Orchestration when implementing complex features with 6+ independent tasks (backend + frontend + tests + docs running concurrently), building systems requiring Byzantine consensus validation (0% theater tolerance), or coordinating distributed agents across multiple execution environments. The architecture scales from small swarms (3-5 agents) to enterprise-scale coordination (50+ agents with hierarchical topology). The key insight: coordination overhead is the bottleneck - optimize agent communication patterns (topology) and eliminate sequential dependencies (parallelism) to unlock true multi-agent leverage.