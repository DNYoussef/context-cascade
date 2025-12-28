---
name: hive-mind-advanced
description: Advanced Hive Mind collective intelligence system for queen-led multi-agent coordination with consensus mechanisms and persistent memory
---

## Orchestration Skill Guidelines

### When to Use This Skill
- **Queen-led coordination** requiring hierarchical multi-agent control
- **Consensus-driven decisions** needing Byzantine fault tolerance
- **Collective intelligence** tasks benefiting from shared memory
- **Strategic planning** with tactical execution delegation
- **Large-scale swarms** with 10+ specialized worker agents

### When NOT to Use This Skill
- **Single-agent tasks** with no coordination requirements
- **Simple workflows** without consensus needs
- **Flat topologies** where hierarchy adds no value
- **Ephemeral tasks** not needing collective memory

### Success Criteria
- **Queen successfully coordinates** all worker agents
- **Consensus achieved** using configured algorithm (majority/weighted/Byzantine)
- **Collective memory shared** across all agents with <10ms access time
- **All workers complete tasks** with 100% assignment success
- **Session state persisted** with checkpoint recovery capability

### Edge Cases to Handle
- **Queen failure** - Implement queen failover and re-election
- **Worker unresponsiveness** - Timeout detection and task reassignment
- **Consensus deadlock** - Fallback to weighted or majority consensus
- **Memory corruption** - Validate memory integrity with checksums
- **Session crash** - Resume from last checkpoint with full state recovery

### Guardrails (NEVER Violate)
- **NEVER lose collective memory** - Persist to SQLite with WAL mode
- **ALWAYS validate queen health** - Monitor queen heartbeat continuously
- **ALWAYS track worker states** - Real-time worker status in shared memory
- **NEVER skip consensus** - Critical decisions require configured consensus
- **ALWAYS checkpoint sessions** - Save state at key milestones

### Evidence-Based Validation
- **Verify queen coordination** - Check queen issued commands to all workers
- **Validate consensus results** - Confirm vote counts meet algorithm threshold
- **Check memory consistency** - Query collective memory, verify no conflicts
- **Measure worker efficiency** - Calculate task completion rate per worker
- **Audit session recovery** - Test checkpoint restore, verify full state


# Hive Mind Advanced Skill

Master the advanced Hive Mind collective intelligence system for sophisticated multi-agent coordination using queen-led architecture, Byzantine consensus, and collective memory.

## Overview

The Hive Mind system represents the pinnacle of multi-agent coordination in Claude Flow, implementing a queen-led hierarchical architecture where a strategic queen coordinator directs specialized worker agents through collective decision-making and shared memory.

## Core Concepts

### Architecture Patterns

**Queen-Led Coordination**
- Strategic queen agents orchestrate high-level objectives
- Tactical queens manage mid-level execution
- Adaptive queens dynamically adjust strategies based on performance

**Worker Specialization**
- Researcher agents: Analysis and investigation
- Coder agents: Implementation and development
- Analyst agents: Data processing and metrics
- Tester agents: Quality assurance and validation
- Architect agents: System design and planning
- Reviewer agents: Code review and improvement
- Optimizer agents: Performance enhancement
- Documenter agents: Documentation generation

**Collective Memory System**
- Shared knowledge base across all agents
- LRU cache with memory pressure handling
- SQLite persistence with WAL mode
- Memory consolidation and association
- Access pattern tracking and optimization

### Consensus Mechanisms

**Majority Consensus**
Simple voting where the option with most votes wins.

**Weighted Consensus**
Queen vote counts as 3x weight, providing strategic guidance.

**Byzantine Fault Tolerance**
Requires 2/3 majority for decision approval, ensuring robust consensus even with faulty agents.

## Getting Started

### 1. Initialize Hive Mind

```bash
# Basic initialization
npx claude-flow hive-mind init

# Force reinitialize
npx claude-flow hive-mind init --force

# Custom configuration
npx claude-flow hive-mind init --config hive-config.json
```

### 2. Spawn a Swarm

```bash
# Basic spawn with objective
npx claude-flow hive-mind spawn "Build microservices architecture"

# Strategic queen type
npx claude-flow hive-mind spawn "Research AI patterns" --queen-type strategic

# Tactical queen with max workers
npx claude-flow hive-mind spawn "Implement API" --queen-type tactical --max-workers 12

# Adaptive queen with consensus
npx claude-flow hive-mind spawn "Optimize system" --queen-type adaptive --consensus byzantine

# Generate Claude Code commands
npx claude-flow hive-mind spawn "Build full-stack app" --claude
```

### 3. Monitor Status

```bash
# Check hive mind status
npx claude-flow hive-mind status

# Get detailed metrics
npx claude-flow hive-mind metrics

# Monitor collective memory
npx claude-flow hive-mind memory
```

## Advanced Workflows

### Session Management

**Create and Manage Sessions**

```bash
# List active sessions
npx claude-flow hive-mind sessions

# Pause a session
npx claude-flow hive-mind pause <session-id>

# Resume a paused session
npx claude-flow hive-mind resume <session-id>

# Stop a running session
npx claude-flow hive-mind stop <session-id>
```

**Session Features**
- Automatic checkpoint creation
- Progress tracking with completion percentages
- Parent-child process management
- Session logs with event tracking
- Export/import capabilities

### Consensus Building

The Hive Mind builds consensus through structured voting:

```javascript
// Programmatic consensus building
const decision = await hiveMind.buildConsensus(
  'Architecture pattern selection',
  ['microservices', 'monolith', 'serverless']
);

// Result includes:
// - decision: Winning option
// - confidence: Vote percentage
// - votes: Individual agent votes
```

**Consensus Algorithms**

1. **Majority** - Simple democratic voting
2. **Weighted** - Queen has 3x voting power
3. **Byzantine** - 2/3 supermajority required

### Collective Memory

**Storing Knowledge**

```javascript
// Store in collective memory
await memory.store('api-patterns', {
  rest: { pros: [...], cons: [...] },
  graphql: { pros: [...], cons: [...] }
}, 'knowledge', { confidence: 0.95 });
```

**Memory Types**
- `knowledge`: Permanent insights (no TTL)
- `context`: Session context (1 hour TTL)
- `task`: Task-specific data (30 min TTL)
- `result`: Execution results (permanent, compressed)
- `error`: Error logs (24 hour TTL)
- `metric`: Performance metrics (1 hour TTL)
- `consensus`: Decision records (permanent)
- `system`: System configuration (permanent)

**Searching and Retrieval**

```javascript
// Search memory by pattern
const results = await memory.search('api*', {
  type: 'knowledge',
  minConfidence: 0.8,
  limit: 50
});

// Get related memories
const related = await memory.getRelated('api-patterns', 10);

// Build associations
await memory.associate('rest-api', 'authentication', 0.9);
```

### Task Distribution

**Automatic Worker Assignment**

The system intelligently assigns tasks based on:
- Keyword matching with agent specialization
- Historical performance metrics
- Worker availability and load
- Task complexity analysis

```javascript
// Create task (auto-assigned)
const task = await hiveMind.createTask(
  'Implement user authentication',
  priority: 8,
  { estimatedDuration: 30000 }
);
```

**Auto-Scaling**

```javascript
// Configure auto-scaling
const config = {
  autoScale: true,
  maxWorkers: 12,
  scaleUpThreshold: 2, // Pending tasks per idle worker
  scaleDownThreshold: 2 // Idle workers above pending tasks
};
```

## Integration Patterns

### With Claude Code

Generate Claude Code spawn commands directly:

```bash
npx claude-flow hive-mind spawn "Build REST API" --claude
```

Output:
```javascript
Task("Queen Coordinator", "Orchestrate REST API development...", "coordinator")
Task("Backend Developer", "Implement Express routes...", "backend-dev")
Task("Database Architect", "Design PostgreSQL schema...", "code-analyzer")
Task("Test Engineer", "Create Jest test suite...", "tester")
```

### With SPARC Methodology

```bash
# Use hive mind for SPARC workflow
npx claude-flow sparc tdd "User authentication" --hive-mind

# Spawns:
# - Specification agent
# - Architecture agent
# - Coder agents
# - Tester agents
# - Reviewer agents
```

### With GitHub Integration

```bash
# Repository analysis with hive mind
npx claude-flow hive-mind spawn "Analyze repo quality" --objective "owner/repo"

# PR review coordination
npx claude-flow hive-mind spawn "Review PR #123" --queen-type tactical
```

## Performance Optimization

### Memory Optimization

The collective memory system includes advanced optimizations:

**LRU Cache**
- Configurable cache size (default: 1000 entries)
- Memory pressure handling (default: 50MB)
- Automatic eviction of least-used entries

**Database Optimization**
- WAL (Write-Ahead Logging) mode
- 64MB cache size
- 256MB memory mapping
- Prepared statements for common queries
- Automatic ANALYZE and OPTIMIZE

**Object Pooling**
- Query result pooling
- Memory entry pooling
- Reduced garbage collection pressure

### Performance Metrics

```javascript
// Get performance insights
const insights = hiveMind.getPerformanceInsights();

// Includes:
// - asyncQueue utilization
// - Batch processing stats
// - Success rates
// - Average processing times
// - Memory efficiency
```

### Task Execution

**Parallel Processing**
- Batch agent spawning (5 agents per batch)
- Concurrent task orchestration
- Async operation optimization
- Non-blocking task assignment

**Benchmarks**
- 10-20x faster batch spawning
- 2.8-4.4x speed improvement overall
- 32.3% token reduction
- 84.8% SWE-Bench solve rate

## Configuration

### Hive Mind Config

```javascript
{
  "objective": "Build microservices",
  "name": "my-hive",
  "queenType": "strategic", // strategic | tactical | adaptive
  "maxWorkers": 8,
  "consensusAlgorithm": "byzantine", // majority | weighted | byzantine
  "autoScale": true,
  "memorySize": 100, // MB
  "taskTimeout": 60, // minutes
  "encryption": false
}
```

### Memory Config

```javascript
{
  "maxSize": 100, // MB
  "compressionThreshold": 1024, // bytes
  "gcInterval": 300000, // 5 minutes
  "cacheSize": 1000,
  "cacheMemoryMB": 50,
  "enablePooling": true,
  "enableAsyncOperations": true
}
```

## Hooks Integration

Hive Mind integrates with Claude Flow hooks for automation:

**Pre-Task Hooks**
- Auto-assign agents by file type
- Validate objective complexity
- Optimize topology selection
- Cache search patterns

**Post-Task Hooks**
- Auto-format deliverables
- Train neural patterns
- Update collective memory
- Analyze performance bottlenecks

**Session Hooks**
- Generate session summaries
- Persist checkpoint data
- Track comprehensive metrics
- Restore execution context

## Best Practices

### 1. Choose the Right Queen Type

**Strategic Queens** - For research, planning, and analysis
```bash
npx claude-flow hive-mind spawn "Research ML frameworks" --queen-type strategic
```

**Tactical Queens** - For implementation and execution
```bash
npx claude-flow hive-mind spawn "Build authentication" --queen-type tactical
```

**Adaptive Queens** - For optimization and dynamic tasks
```bash
npx claude-flow hive-mind spawn "Optimize performance" --queen-type adaptive
```

### 2. Leverage Consensus

Use consensus for critical decisions:
- Architecture pattern selection
- Technology stack choices
- Implementation approach
- Code review approval
- Release readiness

### 3. Utilize Collective Memory

**Store Learnings**
```javascript
// After successful pattern implementation
await memory.store('auth-pattern', {
  approach: 'JWT with refresh tokens',
  pros: ['Stateless', 'Scalable'],
  cons: ['Token size', 'Revocation complexity'],
  implementation: {...}
}, 'knowledge', { confidence: 0.95 });
```

**Build Associations**
```javascript
// Link related concepts
await memory.associate('jwt-auth', 'refresh-tokens', 0.9);
await memory.associate('jwt-auth', 'oauth2', 0.7);
```

### 4. Monitor Performance

```bash
# Regular status checks
npx claude-flow hive-mind status

# Track metrics
npx claude-flow hive-mind metrics

# Analyze memory usage
npx claude-flow hive-mind memory
```

### 5. Session Management

**Checkpoint Frequently**
```javascript
// Create checkpoints at key milestones
await sessionManager.saveCheckpoint(
  sessionId,
  'api-routes-complete',
  { completedRoutes: [...], remaining: [...] }
);
```

**Resume Sessions**
```bash
# Resume from any previous state
npx claude-flow hive-mind resume <session-id>
```

## Troubleshooting

### Memory Issues

**High Memory Usage**
```bash
# Run garbage collection
npx claude-flow hive-mind memory --gc

# Optimize database
npx claude-flow hive-mind memory --optimize

# Export and clear
npx claude-flow hive-mind memory --export --clear
```

**Low Cache Hit Rate**
```javascript
// Increase cache size in config
{
  "cacheSize": 2000,
  "cacheMemoryMB": 100
}
```

### Performance Issues

**Slow Task Assignment**
```javascript
// Enable worker type caching
// The system caches best worker matches for 5 minutes
// Automatic - no configuration needed
```

**High Queue Utilization**
```javascript
// Increase async queue concurrency
{
  "asyncQueueConcurrency": 20 // Default: min(maxWorkers * 2, 20)
}
```

### Consensus Failures

**No Consensus Reached (Byzantine)**
```bash
# Switch to weighted consensus for more decisive results
npx claude-flow hive-mind spawn "..." --consensus weighted

# Or use simple majority
npx claude-flow hive-mind spawn "..." --consensus majority
```

## Advanced Topics

### Custom Worker Types

Define specialized workers in `agents/`:

```yaml
type: specialist
capabilities:
  - vulnerability-scanning
  - security-review
  - penetration-testing
  - compliance-checking
priority: high
```

### Neural Pattern Training

The system trains on successful patterns:

```javascript
// Automatic pattern learning
// Happens after successful task completion
// Stores in collective memory
// Improves future task matching
```

### Multi-Hive Coordination

Run multiple hive minds simultaneously:

```bash
# Frontend hive
npx claude-flow hive-mind spawn "Build UI" --name frontend-hive

# Backend hive
npx claude-flow hive-mind spawn "Build API" --name backend-hive

# They share collective memory for coordination
```

### Export/Import Sessions

```bash
# Export session for backup
npx claude-flow hive-mind export <session-id> --output backup.json

# Import session
npx claude-flow hive-mind import backup.json
```

## API Reference

### HiveMindCore

```javascript
const hiveMind = new HiveMindCore({
  objective: 'Build system',
  queenType: 'strategic',
  maxWorkers: 8,
  consensusAlgorithm: 'byzantine'
});

await hiveMind.initialize();
await hiveMind.spawnQueen(queenData);
await hiveMind.spawnWorkers(['coder', 'tester']);
await hiveMind.createTask('Implement feature', 7);
const decision = await hiveMind.buildConsensus('topic', options);
const status = hiveMind.getStatus();
await hiveMind.shutdown();
```

### CollectiveMemory

```javascript
const memory = new CollectiveMemory({
  swarmId: 'hive-123',
  maxSize: 100,
  cacheSize: 1000
});

await memory.store(key, value, type, metadata);
const data = await memory.retrieve(key);
const results = await memory.search(pattern, options);
const related = await memory.getRelated(key, limit);
await memory.associate(key1, key2, strength);
const stats = memory.getStatistics();
const analytics = memory.getAnalytics();
const health = await memory.healthCheck();
```

### HiveMindSessionManager

```javascript
const sessionManager = new HiveMindSessionManager();

const sessionId = await sessionManager.createSession(
  swarmId, swarmName, objective, metadata
);

await sessionManager.saveCheckpoint(sessionId, name, data);
const sessions = await sessionManager.getActiveSessions();
const session = await sessionManager.getSession(sessionId);
await sessionManager.pauseSession(sessionId);
await sessionManager.resumeSession(sessionId);
await sessionManager.stopSession(sessionId);
await sessionManager.completeSession(sessionId);
```

## Examples

### Full-Stack Development

```bash
# Initialize hive mind
npx claude-flow hive-mind init

# Spawn full-stack hive
npx claude-flow hive-mind spawn "Build e-commerce platform" \
  --queen-type strategic \
  --max-workers 10 \
  --consensus weighted \
  --claude

# Output generates Claude Code commands:
# - Queen coordinator
# - Frontend developers (React)
# - Backend developers (Node.js)
# - Database architects
# - DevOps engineers
# - Security auditors
# - Test engineers
# - Documentation specialists
```

### Research and Analysis

```bash
# Spawn research hive
npx claude-flow hive-mind spawn "Research GraphQL vs REST" \
  --queen-type adaptive \
  --consensus byzantine

# Researchers gather data
# Analysts process findings
# Queen builds consensus on recommendation
# Results stored in collective memory
```

### Code Review

```bash
# Review coordination
npx claude-flow hive-mind spawn "Review PR #456" \
  --queen-type tactical \
  --max-workers 6

# Spawns:
# - Code analyzers
# - Security reviewers
# - Performance reviewers
# - Test coverage analyzers
# - Documentation reviewers
# - Consensus on approval/changes
```

## Skill Progression

### Beginner
1. Initialize hive mind
2. Spawn basic swarms
3. Monitor status
4. Use majority consensus

### Intermediate
1. Configure queen types
2. Implement session management
3. Use weighted consensus
4. Access collective memory
5. Enable auto-scaling

### Advanced
1. Byzantine fault tolerance
2. Memory optimization
3. Custom worker types
4. Multi-hive coordination
5. Neural pattern training
6. Session export/import
7. Performance tuning

## Related Skills

- `swarm-orchestration`: Basic swarm coordination
- `consensus-mechanisms`: Distributed decision making
- `memory-systems`: Advanced memory management
- `sparc-methodology`: Structured development workflow
- `github-integration`: Repository coordination

## References

- [Hive Mind Documentation](https://github.com/ruvnet/claude-flow/docs/hive-mind)
- [Collective Intelligence Patterns](https://github.com/ruvnet/claude-flow/docs/patterns)
- [Byzantine Consensus](https://github.com/ruvnet/claude-flow/docs/consensus)
- [Memory Optimization](https://github.com/ruvnet/claude-flow/docs/memory)

-----------|---------|----------|
| **No queen failover strategy** | Queen agent crashes, entire swarm halts because workers have no coordinator to assign tasks or aggregate results. | Implement queen health monitoring with automatic re-election. Use highest-performing worker as interim queen until new queen spawned. |
| **Memory without garbage collection** | Collective memory grows unbounded, consuming gigabytes, slowing queries, eventually causing out-of-memory crashes. | Configure gcInterval: 300000ms (5 min) with memory pressure handling. LRU eviction at 50MB cache threshold. VACUUM database monthly. |
| **Consensus deadlock on 50/50 split** | Byzantine consensus requires 2/3 majority but agents vote 5 Yes, 5 No on architecture decision. System hangs indefinitely. | Fallback to weighted consensus (queen breaks tie). If still deadlocked, escalate to user with options and rationale. |
| **Worker specialization mismatch** | Task "Implement ML model" assigned to frontend-specialist because keyword matching failed. Wrong agent, poor results, wasted time. | Improve keyword dictionaries per worker type. Add capability-based assignment (agents declare capabilities in YAML). Manual override if confidence <0.7. |
| **Session state not persisted** | System crash mid-execution loses 3 hours of work because session checkpoints not saved. Swarm restarts from zero. | Auto-checkpoint at key milestones (every 5 tasks completed). Enable session export/import. Use WAL mode for crash recovery. |

## Conclusion

Hive Mind Advanced represents the apex of multi-agent coordination in distributed AI systems, combining queen-led hierarchical control, Byzantine fault-tolerant consensus, and persistent collective memory to achieve emergent intelligence beyond individual agents. The system excels at large-scale workflows requiring strategic planning (queen), specialized execution (workers), and robust decision-making (consensus).

The skill's unique contributions are: (1) queen-worker topology enables strategic oversight without micromanagement (queen delegates to worker expertise), (2) Byzantine consensus provides fault tolerance for mission-critical decisions while weighted consensus enables fast iteration, and (3) collective memory transforms ephemeral agent interactions into long-term organizational knowledge that improves with each execution.

Use Hive Mind Advanced when coordinating 10+ specialized agents, implementing systems requiring fault-tolerant consensus (Byzantine or weighted), or building AI organizations that must learn and improve across sessions. The architecture scales from tactical execution (single queen, 6 workers) to multi-queen hierarchies (strategic queen -> tactical queens -> workers) for enterprise-scale automation. The key insight: collective intelligence emerges not from individual agent capability, but from coordination protocols, consensus mechanisms, and shared memory that enable agents to think and decide as a unified entity.