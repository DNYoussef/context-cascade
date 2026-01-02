---
name: README
description: Legacy description preserved in appendix.
allowed-tools: []
model: auto
x-version: 1.0.0
x-category: orchestration
x-vcl-compliance: v3.1.1
x-origin-path: orchestration/consensus/README.md
---

## STANDARD OPERATING PROCEDURE

### Purpose
- Mission: Legacy description preserved in appendix.
- Category: orchestration; source file: orchestration/consensus/README.md
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
<pre># Distributed Consensus Builder Agents

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



## Overview

This directory contains specialized agents for implementing advanced distributed consensus mechanisms and fault-tolerant coordination protocols. These agents work together to provide robust, scalable consensus capabilities for distributed swarm systems.

## Agent Collection

### Core Consensus Protocols

#### 1. **Byzantine Consensus Coordinator** (`byzantine-coordinator.md`)
- **Mission**: Implement Byzantine fault-tolerant consensus algorithms for secure decision-making
- **Key Features**:
  - PBFT (Practical Byzantine Fault Tolerance) implementation
  - Malicious agent detection and isolation
  - Threshold signature schemes
  - Network partition recovery protocols
  - DoS protection and rate limiting

#### 2. **Raft Consensus Manager** (`raft-manager.md`)
- **Mission**: Implement Raft consensus algorithm with leader election and log replication
- **Key Features**:
  - Leader election with randomized timeouts
  - Log replication and consistency guarantees
  - Follower synchronization and catch-up mechanisms
  - Snapshot creation and log compaction
  - Leadership transfer protocols

#### 3. **Gossip Protocol Coordinator** (`gossip-coordinator.md`)
- **Mission**: Implement epidemic information dissemination for scalable communication
- **Key Features**:
  - Push/Pull/Hybrid gossip protocols
  - Anti-entropy state synchronization
  - Membership management and failure detection
  - Network topology discovery
  - Adaptive gossip parameter tuning

### Security and Cryptography

#### 4. **Security Manager** (`security-manager.md`)
- **Mission**: Provide comprehensive security mechanisms for consensus protocols
- **Key Features**:
  - Threshold cryptography and signature schemes
  - Zero-knowledge proof systems
  - Attack detection and mitigation (Byzantine, Sybil, Eclipse, DoS)
  - Secure key management and distribution
  - End-to-end encryption for consensus traffic

### State Synchronization

#### 5. **CRDT Synchronizer** (`crdt-synchronizer.md`)
- **Mission**: Implement Conflict-free Replicated Data Types for eventual consistency
- **Key Features**:
  - State-based and operation-based CRDTs
  - G-Counter, PN-Counter, OR-Set, LWW-Register implementations
  - RGA (Replicated Growable Array) for sequences
  - Delta-state CRDT optimization
  - Causal consistency tracking

### Performance and Optimization

#### 6. **Performance Benchmarker** (`performance-benchmarker.md`)
- **Mission**: Comprehensive performance analysis and optimization for consensus protocols
- **Key Features**:
  - Throughput and latency measurement
  - Resource utilization monitoring
  - Comparative protocol analysis
  - Adaptive performance tuning
  - Real-time optimization recommendations

#### 7. **Quorum Manager** (`quorum-manager.md`)
- **Mission**: Dynamic quorum adjustment based on network conditions and fault tolerance
- **Key Features**:
  - Network-based quorum strategies
  - Performance-optimized quorum sizing
  - Fault tolerance analysis and optimization
  - Intelligent membership management
  - Predictive quorum adjustments

## Architecture Integration

### MCP Integration Points

All consensus agents integrate with the MCP (Model Context Protocol) coordination system:

```javascript
// Memory coordination for persistent state
await this.mcpTools.memory_usage({
  action: &#x27;store&#x27;,
  key: &#x27;consensus_state&#x27;,
  value: JSON.stringify(consensusData),
  namespace: &#x27;distributed_consensus&#x27;
});

// Performance monitoring
await this.mcpTools.metrics_collect({
  components: [&#x27;consensus_latency&#x27;, &#x27;throughput&#x27;, &#x27;fault_tolerance&#x27;]
});

// Task orchestration
await this.mcpTools.task_orchestrate({
  task: &#x27;consensus_round&#x27;,
  strategy: &#x27;parallel&#x27;,
  priority: &#x27;high&#x27;
});
```

### Swarm Coordination

Agents coordinate with the broader swarm infrastructure:

- **Node Discovery**: Integration with swarm node discovery mechanisms
- **Health Monitoring**: Consensus participation in distributed health checks  
- **Load Balancing**: Dynamic load distribution across consensus participants
- **Fault Recovery**: Coordinated recovery from node and network failures

## Usage Patterns

### Basic Consensus Setup

```javascript
// Initialize Byzantine consensus for high-security scenarios
const byzantineConsensus = new ByzantineConsensusCoordinator(&#x27;node-1&#x27;, 7, 2);
await byzantineConsensus.initializeNode();

// Initialize Raft for leader-based coordination
const raftConsensus = new RaftConsensusManager(&#x27;node-1&#x27;, [&#x27;node-1&#x27;, &#x27;node-2&#x27;, &#x27;node-3&#x27;]);
await raftConsensus.initialize();

// Initialize Gossip for scalable information dissemination
const gossipCoordinator = new GossipProtocolCoordinator(&#x27;node-1&#x27;, [&#x27;seed-1&#x27;, &#x27;seed-2&#x27;]);
await gossipCoordinator.initialize();
```

### Security-Enhanced Consensus

```javascript
// Add security layer to consensus protocols
const securityManager = new SecurityManager();
await securityManager.generateDistributedKeys(participants, threshold);

const secureConsensus = new SecureConsensusWrapper(
  byzantineConsensus, 
  securityManager
);
```

### Performance Optimization

```javascript
// Benchmark and optimize consensus performance
const benchmarker = new ConsensusPerformanceBenchmarker();
const results = await benchmarker.runComprehensiveBenchmarks(
  [&#x27;byzantine&#x27;, &#x27;raft&#x27;, &#x27;gossip&#x27;],
  scenarios
);

// Apply adaptive optimizations
const optimizer = new AdaptiveOptimizer();
await optimizer.optimizeBasedOnResults(results);
```

### State Synchronization

```javascript
// Set up CRDT-based state synchronization
const crdtSynchronizer = new CRDTSynchronizer(&#x27;node-1&#x27;, replicationGroup);
const counter = crdtSynchronizer.registerCRDT(&#x27;request_counter&#x27;, &#x27;G_COUNTER&#x27;);
const userSet = crdtSynchronizer.registerCRDT(&#x27;active_users&#x27;, &#x27;OR_SET&#x27;);

await crdtSynchronizer.synchronize();
```

## Advanced Features

### Fault Tolerance

- **Byzantine Fault Tolerance**: Handles up to f &lt; n/3 malicious nodes
- **Crash Fault Tolerance**: Recovers from node failures and network partitions
- **Network Partition Tolerance**: Maintains consistency during network splits
- **Graceful Degradation**: Continues operation with reduced functionality

### Scalability

- **Horizontal Scaling**: Add/remove nodes dynamically
- **Load Distribution**: Distribute consensus load across available resources
- **Gossip-based Dissemination**: Logarithmic message complexity
- **Delta Synchronization**: Efficient incremental state updates

### Security

- **Cryptographic Primitives**: Ed25519 signatures, threshold cryptography
- **Attack Mitigation**: Protection against Byzantine, Sybil, Eclipse, and DoS attacks
- **Zero-Knowledge Proofs**: Privacy-preserving consensus verification
- **Secure Communication**: TLS 1.3 with forward secrecy

### Performance

- **Adaptive Optimization**: Real-time parameter tuning based on performance
- **Resource Monitoring**: CPU, memory, network, and storage utilization
- **Bottleneck Detection**: Automatic identification of performance constraints
- **Predictive Scaling**: Anticipate resource needs before bottlenecks occur

## Testing and Validation

### Consensus Correctness
- **Safety Properties**: Verify agreement and validity properties
- **Liveness Properties**: Ensure progress under normal conditions
- **Fault Injection**: Test behavior under various failure scenarios
- **Formal Verification**: Mathematical proofs of correctness

### Performance Testing
- **Load Testing**: High-throughput consensus scenarios
- **Latency Analysis**: End-to-end latency measurement and optimization
- **Scalability Testing**: Performance with varying cluster sizes
- **Resource Efficiency**: Optimize resource utilization

### Security Validation
- **Penetration Testing**: Simulated attacks on consensus protocols
- **Cryptographic Verification**: Validate security of cryptographic schemes
- **Threat Modeling**: Analyze potential attack vectors
- **Compliance Testing**: Ensure adherence to security standards

## Deployment Considerations

### Network Requirements
- **Bandwidth**: Sufficient bandwidth for consensus message traffic
- **Latency**: Low-latency network connections between nodes
- **Reliability**: Stable network connectivity for consensus participants
- **Security**: Encrypted communication channels

### Resource Requirements
- **CPU**: Adequate processing power for cryptographic operations
- **Memory**: Sufficient RAM for consensus state and message buffers
- **Storage**: Persistent storage for consensus logs and state
- **Redundancy**: Multiple nodes for fault tolerance

### Monitoring and Observability
- **Metrics Collection**: Real-time performance and health metrics
- **Alerting**: Notifications for consensus failures or degraded performance
- **Logging**: Comprehensive audit trails for consensus operations
- **Dashboards**: Visual monitoring of consensus health and performance

## Integration Examples

See individual agent files for detailed implementation examples and integration patterns with specific consensus protocols and use cases.

---
*Promise: `&lt;promise&gt;README_VERIX_COMPLIANT&lt;/promise&gt;`*
</pre>
</details>

