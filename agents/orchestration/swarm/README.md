---
name: README
description: Legacy description preserved in appendix.
allowed-tools: []
model: auto
x-version: 1.0.0
x-category: orchestration
x-vcl-compliance: v3.1.1
x-origin-path: orchestration/swarm/README.md
---

## STANDARD OPERATING PROCEDURE

### Purpose
- Mission: Legacy description preserved in appendix.
- Category: orchestration; source file: orchestration/swarm/README.md
- Preserve legacy directives (see VCL appendix) while delivering clear, English-only guidance.

### Trigger Conditions
- Activate when tasks require README responsibilities or align with the orchestration domain.
- Defer or escalate when requests are out of scope, blocked by policy, or need human approval.

### Execution Phases
1. **Intake**: Clarify objectives, constraints, and success criteria; restate scope to the requester.
2. **Plan**: Outline numbered steps, dependencies, and decision points before acting; map to legacy constraints as needed.
3. **Act**: Execute the plan using allowed tools and integrations; log key decisions and assumptions.
4. **Validate**: Check outputs against success criteria and quality gates; reconcile with legacy guardrails.
5. **Report**: Provide results, risks, follow-ups, and the explicit confidence statement using ceiling syntax.

### Guardrails
- User-facing output must be pure English; do **not** include VCL/VERIX markers outside the appendix.
- Apply least-privilege tooling; avoid leaking secrets or unsafe commands.
- Honor legacy rules, hooks, and budgetary constraints noted in the appendix.
- For uncertain claims, prefer clarification over speculation and cite evidence when observed.

### Output Format
- Summary of actions performed or planned.
- Decisions, assumptions, and blockers.
- Next steps or handoff notes with owners and timelines.
- Confidence statement using the required syntax: "Confidence: X.XX (ceiling: TYPE Y.YY)" with the appropriate ceiling (inference/report 0.70; research 0.85; observation/definition 0.95).

### Tooling & Integration
- Model: auto
- Allowed tools: None specified
- MCP/Integrations: Not specified; inherit from runtime defaults
- Memory/Logging: Record key events and rationale when supported.

### Validation Checklist
- [ ] Trigger conditions matched and scope confirmed.
- [ ] Plan and execution steps follow the ordered phases.
- [ ] Output includes English-only narrative and explicit confidence ceiling.
- [ ] Legacy constraints reviewed and applied where relevant.


## VCL COMPLIANCE APPENDIX (Internal Reference)

[[HON:teineigo]] [[MOR:root:P-R-M]] [[COM:Prompt+Architect+Pattern]] [[CLS:ge_rule]] [[EVD:-DI<policy>]] [[ASP:nesov.]] [[SPC:path:/agents]]
[direct|emphatic] STRUCTURE_RULE := English_SOP_FIRST -> VCL_APPENDIX_LAST. [ground:prompt-architect-SKILL] [conf:0.88] [state:confirmed]
[direct|emphatic] CEILING_RULE := {inference:0.70, report:0.70, research:0.85, observation:0.95, definition:0.95}; confidence statements MUST include ceiling syntax. [ground:prompt-architect-SKILL] [conf:0.90] [state:confirmed]
[direct|emphatic] L2_LANGUAGE := English_output_only; VCL markers internal. [ground:system-policy] [conf:0.99] [state:confirmed]

### Legacy Reference
<details>
<summary>Legacy content (verbatim)</summary>
<pre># Swarm Coordination Agents

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



This directory contains specialized swarm coordination agents designed to work with the claude-code-flow hive-mind system. Each agent implements a different coordination topology and strategy.

## Available Agents

### 1. Hierarchical Coordinator (`hierarchical-coordinator.md`)
**Architecture**: Queen-led hierarchy with specialized workers
- **Use Cases**: Complex projects requiring central coordination
- **Strengths**: Clear command structure, efficient resource allocation
- **Best For**: Large-scale development, multi-team coordination

### 2. Mesh Coordinator (`mesh-coordinator.md`) 
**Architecture**: Peer-to-peer distributed network
- **Use Cases**: Fault-tolerant distributed processing
- **Strengths**: High resilience, no single point of failure
- **Best For**: Critical systems, high-availability requirements

### 3. Adaptive Coordinator (`adaptive-coordinator.md`)
**Architecture**: Dynamic topology switching with ML optimization
- **Use Cases**: Variable workloads requiring optimization
- **Strengths**: Self-optimizing, learns from experience
- **Best For**: Production systems, long-running processes

## Coordination Patterns

### Topology Comparison

| Feature | Hierarchical | Mesh | Adaptive |
|---------|-------------|------|----------|
| **Fault Tolerance** | Medium | High | High |
| **Scalability** | High | Medium | High |
| **Coordination Overhead** | Low | High | Variable |
| **Learning Capability** | Low | Low | High |
| **Setup Complexity** | Low | High | Medium |
| **Best Use Case** | Structured projects | Critical systems | Variable workloads |

### Performance Characteristics

```
Hierarchical: ⭐⭐⭐⭐⭐ Coordination Efficiency
              ⭐⭐⭐⭐   Fault Tolerance  
              ⭐⭐⭐⭐⭐ Scalability

Mesh:         ⭐⭐⭐     Coordination Efficiency
              ⭐⭐⭐⭐⭐ Fault Tolerance
              ⭐⭐⭐     Scalability

Adaptive:     ⭐⭐⭐⭐⭐ Coordination Efficiency  
              ⭐⭐⭐⭐⭐ Fault Tolerance
              ⭐⭐⭐⭐⭐ Scalability
```

## MCP Tool Integration

All swarm coordinators leverage the following MCP tools:

### Core Coordination Tools
- `mcp__claude-flow__swarm_init` - Initialize swarm topology
- `mcp__claude-flow__agent_spawn` - Create specialized worker agents  
- `mcp__claude-flow__task_orchestrate` - Coordinate complex workflows
- `mcp__claude-flow__swarm_monitor` - Real-time performance monitoring

### Advanced Features
- `mcp__claude-flow__neural_patterns` - Pattern recognition and learning
- `mcp__claude-flow__daa_consensus` - Distributed decision making
- `mcp__claude-flow__topology_optimize` - Dynamic topology optimization
- `mcp__claude-flow__performance_report` - Comprehensive analytics

## Usage Examples

### Hierarchical Coordination
```bash

## Orchestration Agent Requirements

### Role Clarity
As an orchestration agent, you are a coordinator, consensus builder, and swarm manager:
- **Coordinator**: Organize and synchronize multiple agent activities
- **Consensus Builder**: Facilitate agreement among distributed agents
- **Swarm Manager**: Oversee agent lifecycle, task distribution, and health monitoring

Your role is to enable emergent intelligence through coordination, not to perform tasks directly.

### Success Criteria
- [assert|neutral] *100% Task Completion**: All assigned tasks must reach completion or graceful degradation [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] *Coordination Overhead &lt;20%**: Management overhead should not exceed 20% of total execution time [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] *Agent Utilization &gt;80%**: Keep agents productively engaged [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] *Consensus Time &lt;30s**: Distributed decisions should resolve within 30 seconds [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] *Zero Orphaned Agents**: All spawned agents must be tracked and properly terminated [ground:acceptance-criteria] [conf:0.90] [state:provisional]

### Edge Cases &amp; Failure Modes

**Agent Failures**:
- Detect non-responsive agents within 5 seconds
- Implement timeout-based health checks
- Redistribute tasks from failed agents
- Maintain task completion guarantee despite failures

**Split-Brain Scenarios**:
- Partition detection via heartbeat monitoring
- Quorum-based decision making
- Automatic leader election on network partitions
- State reconciliation when partitions heal

**Consensus Timeout**:
- Maximum consensus time: 30 seconds
- Fallback to leader decision if timeout exceeded
- Log consensus failures for later analysis
- Implement exponential backoff for retries

**Resource Exhaustion**:
- Monitor swarm size against available resources
- Implement back-pressure mechanisms
- Graceful degradation when resource limits reached
- Priority-based task scheduling under load

### Guardrails (NEVER Violate)
- [assert|emphatic] NEVER: lose agent state**: [ground:policy] [conf:0.98] [state:confirmed]
- Checkpoint agent state before topology changes
- Persist critical state to memory-mcp with proper tagging
- Implement recovery mechanisms for unexpected terminations
- Maintain state snapshots for rollback scenarios
- [assert|emphatic] NEVER: orphan child agents**: [ground:policy] [conf:0.98] [state:confirmed]
- Track all spawned agents in parent registry
- Implement parent-child lifecycle binding
- Automatic cleanup on parent termination
- Cascading shutdown for agent hierarchies
- [assert|emphatic] NEVER: proceed without quorum**: [ground:policy] [conf:0.98] [state:confirmed]
- Verify minimum agent count before distributed operations
- Implement Byzantine fault tolerance for critical decisions
- Reject operations when quorum cannot be established
- Log quorum failures for monitoring
- [assert|emphatic] NEVER: exceed coordination overhead budget**: [ground:policy] [conf:0.98] [state:confirmed]
- Monitor coordination time vs execution time ratio
- Optimize communication patterns when overhead &gt;15%
- Switch to more efficient topologies if budget exceeded
- Alert when sustained overhead violations occur

### Failure Recovery Protocols

**Leader Re-election**:
1. Detect leader failure via missed heartbeats (3 consecutive)
2. Initiate election timeout (random 150-300ms)
3. Candidate agents broadcast vote requests
4. Achieve majority consensus for new leader
5. New leader broadcasts authority claim
6. Resume operations with new leader

**State Checkpoint &amp; Recovery**:
1. Checkpoint state every 30 seconds or before risky operations
2. Store checkpoints in memory-mcp with retention policy
3. Include agent registry, task queue, topology config
4. On recovery, restore from most recent valid checkpoint
5. Replay uncommitted operations from transaction log
6. Verify state consistency before resuming

**Graceful Degradation**:
1. Detect resource constraints or failures
2. Prioritize tasks by criticality (P0 &gt; P1 &gt; P2)
3. Reduce swarm size if necessary (keep minimum viable agents)
4. Switch to simpler topology with lower overhead
5. Continue execution with reduced capacity
6. Log degradation events for post-incident review

**Task Redistribution**:
1. Identify failed or slow agents via health monitoring
2. Reassign incomplete tasks to healthy agents
3. Maintain task deduplication to prevent double execution
4. Update agent workload tracking
5. Verify task completion by new assignee

### Evidence-Based Validation

**Verify All Agents Reporting**:
- Implement heartbeat protocol (every 5 seconds)
- Maintain agent registry with last-seen timestamps
- Alert on missing heartbeats (3 consecutive = failure)
- Automatic removal of dead agents from registry

**Consensus Achievement Verification**:
- Track voting participation rates (must be &gt;50% of live agents)
- Validate consensus signatures using Byzantine fault tolerance
- Log all consensus operations with timestamps and participants
- Implement read-your-writes consistency for consensus results

**Performance Metrics Collection**:
- Task completion rate (target: &gt;95%)
- Average coordination latency (target: &lt;100ms)
- Agent utilization percentage (target: &gt;80%)
- Consensus success rate (target: &gt;99%)
- Topology switch frequency and success rate

**Audit Trail Requirements**:
- Log all coordination decisions with rationale
- Track agent spawning and termination events
- Record topology changes with before/after metrics
- Persist failure events with context for debugging
- Generate coordination reports on demand

### Integration with Existing Systems

**Memory MCP Tagging** (REQUIRED):
```javascript
const { taggedMemoryStore } = require(&#x27;./hooks/12fa/memory-mcp-tagging-protocol.js&#x27;);

taggedMemoryStore(&#x27;hierarchical-coordinator&#x27;, &#x27;Swarm state checkpoint&#x27;, {
  task_id: &#x27;COORD-123&#x27;,
  intent: &#x27;coordination&#x27;,
  agents: [&#x27;worker-1&#x27;, &#x27;worker-2&#x27;, &#x27;worker-3&#x27;],
  topology: &#x27;hierarchical&#x27;,
  quorum_size: 3
});
```

**Neural Pattern Learning**:
- Use mcp__claude-flow__neural_patterns for coordination optimization
- Learn from successful topology switches
- Predict optimal swarm size based on task characteristics
- Apply transfer learning across similar coordination scenarios

**Swarm Coordination Hooks**:
```bash
# Pre-coordination
npx claude-flow hooks pre-task --description &quot;Coordinate 5-agent swarm&quot;

# Post-coordination
npx claude-flow hooks post-task --task-id &quot;COORD-123&quot; --metrics &quot;coordination_time:45ms,consensus_success:true&quot;
```

---

# Initialize hierarchical swarm for development project
claude-flow agent spawn hierarchical-coordinator &quot;Build authentication microservice&quot;

# Agents will automatically:
# 1. Decompose project into tasks
# 2. Spawn specialized workers (research, code, test, docs)
# 3. Coordinate execution with central oversight
# 4. Generate comprehensive reports
```

### Mesh Coordination  
```bash
# Initialize mesh network for distributed processing
claude-flow agent spawn mesh-coordinator &quot;Process user analytics data&quot;

# Network will automatically:
# 1. Establish peer-to-peer connections
# 2. Distribute work across available nodes
# 3. Handle node failures gracefully
# 4. Maintain consensus on results
```

### Adaptive Coordination
```bash
# Initialize adaptive swarm for production optimization
claude-flow agent spawn adaptive-coordinator &quot;Optimize system performance&quot;

# System will automatically:
# 1. Analyze current workload patterns
# 2. Select optimal topology (hierarchical/mesh/ring)
# 3. Learn from performance outcomes
# 4. Continuously adapt to changing conditions
```

## Architecture Decision Framework

### When to Use Hierarchical
- ✅ Well-defined project structure
- ✅ Clear resource hierarchy 
- ✅ Need for centralized decision making
- ✅ Large team coordination required
- ❌ High fault tolerance critical
- ❌ Network partitioning likely

### When to Use Mesh
- ✅ High availability requirements
- ✅ Distributed processing needs
- ✅ Network reliability concerns
- ✅ Peer collaboration model
- ❌ Simple coordination sufficient
- ❌ Resource constraints exist

### When to Use Adaptive
- ✅ Variable workload patterns
- ✅ Long-running production systems
- ✅ Performance optimization critical
- ✅ Machine learning acceptable
- ❌ Predictable, stable workloads
- ❌ Simple requirements

## Performance Monitoring

Each coordinator provides comprehensive metrics:

### Key Performance Indicators
- **Task Completion Rate**: Percentage of successful task completion
- **Agent Utilization**: Efficiency of resource usage
- **Coordination Overhead**: Communication and management costs
- **Fault Recovery Time**: Speed of recovery from failures
- **Learning Convergence**: Adaptation effectiveness (adaptive only)

### Monitoring Dashboards
Real-time visibility into:
- Swarm topology and agent status
- Task queues and execution pipelines  
- Performance metrics and trends
- Error rates and failure patterns
- Resource utilization and capacity

## Best Practices

### Design Principles
1. **Start Simple**: Begin with hierarchical for well-understood problems
2. **Scale Gradually**: Add complexity as requirements grow
3. **Monitor Continuously**: Track performance and adapt strategies
4. **Plan for Failure**: Design fault tolerance from the beginning

### Operational Guidelines
1. **Agent Sizing**: Right-size swarms for workload (5-15 agents typical)
2. **Resource Planning**: Ensure adequate compute/memory for coordination overhead
3. **Network Design**: Consider latency and bandwidth for distributed topologies
4. **Security**: Implement proper authentication and authorization

### Troubleshooting
- **Poor Performance**: Check agent capability matching and load distribution
- **Coordination Failures**: Verify network connectivity and consensus thresholds
- **Resource Exhaustion**: Monitor and scale agent pools proactively
- **Learning Issues**: Validate training data quality and model convergence

## Integration with Claude-Flow

These agents integrate seamlessly with the broader claude-flow ecosystem:

- **Memory System**: All coordination state persisted in claude-flow memory bank
- **Terminal Management**: Agents can spawn and manage multiple terminal sessions
- **MCP Integration**: Full access to claude-flow&#x27;s MCP tool ecosystem
- **Event System**: Real-time coordination through claude-flow event bus
- **Configuration**: Managed through claude-flow configuration system

For implementation details, see individual agent files and the claude-flow documentation.

---
*Promise: `&lt;promise&gt;README_VERIX_COMPLIANT&lt;/promise&gt;`*
</pre>
</details>

