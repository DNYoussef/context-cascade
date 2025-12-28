---
name: advanced-coordination
description: Advanced multi-agent coordination patterns for complex distributed systems. Use when coordinating 5+ agents with dynamic task dependencies, implementing Byzantine fault tolerance, or managing distributed consensus protocols. Provides RAFT, Gossip, and Byzantine coordination strategies.
---

## Orchestration Skill Guidelines

### When to Use This Skill
- **Multi-agent coordination** requiring topology-aware task distribution
- **Cloud-based orchestration** with Flow Nexus platform integration
- **Event-driven workflows** needing message-based coordination
- **Distributed systems** spanning multiple execution environments
- **Scalable swarms** with adaptive topology management

### When NOT to Use This Skill
- **Single-agent tasks** with no coordination overhead
- **Local-only execution** not using cloud features
- **Simple sequential work** without event-driven needs
- **Static topologies** not requiring adaptive scaling

### Success Criteria
- **Coordination topology established** (mesh/hierarchical/star)
- **All agents registered** in coordination namespace
- **Event routing functional** with <50ms message latency
- **No coordination deadlocks** - All agents progressing
- **Scalability validated** - Handles target agent count

### Edge Cases to Handle
- **Network partitions** - Implement partition tolerance with eventual consistency
- **Message loss** - Add message acknowledgment and retry logic
- **Agent disconnection** - Detect disconnects, redistribute work
- **Topology reconfiguration** - Support live topology changes without restart
- **Rate limiting** - Handle cloud API rate limits with backoff

### Guardrails (NEVER Violate)
- **NEVER lose coordination state** - Persist topology and agent registry
- **ALWAYS validate topology** - Check for cycles, orphaned nodes
- **ALWAYS monitor message queues** - Prevent queue overflow
- **NEVER skip health checks** - Continuous agent liveness monitoring
- **ALWAYS handle failures gracefully** - No cascading failures

### Evidence-Based Validation
- **Verify topology structure** - Validate graph properties (connected, acyclic if needed)
- **Check message delivery** - Confirm all messages reached targets
- **Measure coordination overhead** - Calculate % time spent on coordination vs work
- **Validate agent reachability** - Ping all agents, verify responses
- **Audit scalability** - Test with max agent count, measure performance


# Advanced Coordination - Distributed Agent Management

Sophisticated coordination protocols for large-scale multi-agent systems with fault tolerance and consensus requirements.

## When to Use This Skill

Use when coordinating complex multi-agent workflows with 5+ concurrent agents, implementing fault-tolerant distributed systems, managing dynamic task dependencies across agents, or requiring consensus protocols (RAFT, Byzantine, Gossip).

## Coordination Strategies

### RAFT Consensus
- Leader election among agents
- Replicated log consistency
- Fault tolerance for N/2+1 failures
- Strong consistency guarantees

### Gossip Protocol
- Peer-to-peer agent communication
- Eventually consistent state sharing
- Highly scalable (100+ agents)
- Network partition resilient

### Byzantine Fault Tolerance
- Malicious or faulty agent detection
- 3F+1 redundancy for F failures
- Cryptographic verification
- Critical system integrity

## Process

1. **Analyze coordination requirements**
   - Determine number of agents needed
   - Identify fault tolerance needs
   - Assess consistency requirements
   - Define communication patterns

2. **Select coordination strategy**
   - RAFT for strong consistency
   - Gossip for high scalability
   - Byzantine for security-critical systems
   - Hybrid for complex requirements

3. **Initialize coordination topology**
   - Set up agent communication channels
   - Establish leader election if needed
   - Configure heartbeat and timeouts
   - Define state replication rules

4. **Monitor coordination health**
   - Track agent liveness
   - Detect network partitions
   - Monitor consensus progress
   - Log coordination events

5. **Handle failures gracefully**
   - Automatic failover
   - State recovery mechanisms
   - Network partition healing
   - Agent replacement strategies

## Integration

- **Claude-Flow**: `npx claude-flow@alpha swarm init --topology mesh`
- **Monitoring**: Real-time coordination metrics
- **Memory-MCP**: Cross-agent state persistence
## Core Principles

Advanced Coordination operates on 3 fundamental principles:

### Principle 1: Consensus Protocols Provide Fault-Tolerant Distributed Agreement
Different coordination strategies (RAFT, Gossip, Byzantine) trade off consistency, availability, and partition tolerance based on system requirements.

In practice:
- RAFT for strong consistency with leader election (financial transactions, critical state machines)
- Gossip protocol for eventual consistency with high scalability (service discovery, distributed caching)
- Byzantine Fault Tolerance for malicious agent detection (security-critical systems, 3F+1 redundancy)
- Hybrid approaches combine protocols (RAFT for critical operations, Gossip for metrics aggregation)

### Principle 2: Network Partition Tolerance Requires Graceful Degradation
Distributed systems must detect partitions, operate with reduced functionality, and heal automatically when network connectivity restores.

In practice:
- Heartbeat monitoring detects agent disconnections within 5-10 seconds
- Partition-tolerant state replication continues local writes, syncs on reconnection
- Quorum-based decisions adapt thresholds during partitions (5/7 agents -> 3/4 remaining agents)
- Eventual consistency healing reconciles divergent state when partition resolves

### Principle 3: Dynamic Task Dependencies Require Real-Time Coordination
Agent work must adapt to runtime conditions, with task graphs updated dynamically based on intermediate results and changing requirements.

In practice:
- Task scheduler maintains DAG (directed acyclic graph) of dependencies
- Completed tasks unblock dependent tasks automatically (cascading execution)
- Failed tasks trigger fallback chains or alternative execution paths
- Conditional branching based on agent results (if quality_score > 0.8 -> fast_path else -> comprehensive_audit)

## Common Anti-Patterns

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| **No partition detection** | Network partition occurs, system continues assuming all agents healthy, writes diverge, data corruption after partition heals. | Implement heartbeat monitoring (5s interval). Detect missing heartbeats within 15s. Trigger partition protocol (quorum adjustment, read-only mode). |
| **RAFT for >211 agents** | Leader election overhead dominates, message complexity O(n^2), system spends 80% time coordinating instead of working. | Use Gossip protocol for large swarms (scales to 1000+ agents). Reserve RAFT for critical subsystems with <10 agents. |
| **Circular task dependencies** | Task A depends on B, B depends on C, C depends on A. Scheduler deadlocks, no task can start, system hangs indefinitely. | Validate task graph as DAG before execution. Reject circular dependencies at design time. Use topological sort for execution order. |
| **No Byzantine agent detection** | Malicious agent submits false results, corrupts shared state, other agents trust blindly, system produces incorrect output. | Implement Byzantine consensus with cryptographic verification. Require 2/3 agreement for critical operations. Blacklist agents with <60% agreement rate. |
| **Message queue overflow** | Agents generate messages faster than consumers process them, queue grows unbounded, memory exhausted, system crashes. | Set max queue size with backpressure. Block producers when queue full. Implement message priority (critical > normal > low). |

## Conclusion

Advanced Coordination provides the distributed systems foundation for large-scale multi-agent orchestration, implementing battle-tested consensus protocols (RAFT, Gossip, Byzantine) with fault tolerance, partition handling, and dynamic task dependency management. The skill enables production-grade distributed AI systems that maintain correctness and availability despite agent failures, network partitions, and malicious behavior.

The core contributions are: (1) consensus protocol selection (RAFT/Gossip/Byzantine) optimizes the consistency-availability-partition tolerance tradeoff for specific system requirements, (2) partition tolerance with graceful degradation enables continued operation during network failures and automatic healing on reconnection, and (3) dynamic task dependency graphs adapt execution plans in real-time based on intermediate results and runtime conditions.

Use Advanced Coordination when building distributed systems with 20+ agents spanning multiple execution environments, implementing security-critical workflows requiring Byzantine fault tolerance, or managing complex task graphs with dynamic dependencies determined at runtime. The architecture scales from small clusters (5-10 agents with RAFT) to massive swarms (1000+ agents with Gossip). The key insight: coordination is the hard problem in distributed systems - consensus protocols, partition tolerance, and dynamic scheduling are not optional features but fundamental requirements for correctness at scale.