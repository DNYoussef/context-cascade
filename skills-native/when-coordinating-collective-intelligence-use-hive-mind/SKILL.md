---
name: when-coordinating-collective-intelligence-use-hive-mind
description: Advanced Hive Mind collective intelligence for queen-led multi-agent coordination with consensus and memory
---

# Hive Mind Collective Intelligence SOP

## Overview

Implement advanced Hive Mind collective intelligence system with queen-led coordination, consensus mechanisms, persistent memory, and distributed decision-making.

## Agents & Responsibilities

### collective-intelligence-coordinator
**Role:** Coordinate collective intelligence processing
**Responsibilities:**
- Aggregate agent insights
- Synthesize collective knowledge
- Identify patterns across agents
- Facilitate group learning

### queen-coordinator
**Role:** Lead and direct hive activities
**Responsibilities:**
- Set strategic direction
- Prioritize tasks
- Resolve conflicts
- Make final decisions

### swarm-memory-manager
**Role:** Manage shared memory and knowledge base
**Responsibilities:**
- Store collective memory
- Synchronize agent states
- Maintain knowledge graph
- Ensure data consistency

## Phase 1: Initialize Hive Mind

### Objective
Establish Hive Mind infrastructure with queen and collective intelligence systems.

### Scripts

```bash
# Initialize Hive Mind
npx claude-flow@alpha hive init \
  --queen-enabled \
  --collective-intelligence \
  --consensus-mechanism "proof-of-intelligence" \
  --max-agents 20

# Spawn queen coordinator
npx claude-flow@alpha agent spawn \
  --type coordinator \
  --role "queen-coordinator" \
  --capabilities "strategic-direction,conflict-resolution,final-decisions"

# Spawn collective intelligence coordinator
npx claude-flow@alpha agent spawn \
  --type coordinator \
  --role "collective-intelligence-coordinator" \
  --capabilities "insight-aggregation,pattern-recognition,group-learning"

# Spawn memory manager
npx claude-flow@alpha agent spawn \
  --type coordinator \
  --role "swarm-memory-manager" \
  --capabilities "memory-storage,state-sync,knowledge-graph"

# Initialize shared memory
npx claude-flow@alpha memory init \
  --type "distributed" \
  --replication 3 \
  --consistency "strong"

# Verify Hive Mind status
npx claude-flow@alpha hive status --show-queen --show-collective
```

### Hive Mind Architecture

**Queen Layer:**
```
Queen Coordinator
    ↓
Strategic Direction
    ↓
Task Prioritization
    ↓
Final Decisions
```

**Collective Intelligence Layer:**
```
Agent 1 → Insights →┐
Agent 2 → Insights →├─ Collective Intelligence → Synthesis
Agent 3 → Insights →│
Agent N → Insights →┘
```

**Memory Layer:**
```
Local Memory ←→ Swarm Memory Manager ←→ Distributed Memory Store
```

### Memory Patterns

```bash
# Store hive configuration
npx claude-flow@alpha memory store \
  --key "hive/config" \
  --value '{
    "queenEnabled": true,
    "consensusMechanism": "proof-of-intelligence",
    "maxAgents": 20,
    "initialized": "'$(date -Iseconds)'"
  }'

# Initialize collective memory
npx claude-flow@alpha memory store \
  --key "hive/collective/insights" \
  --value '[]'

npx claude-flow@alpha memory store \
  --key "hive/collective/patterns" \
  --value '{}'
```

## Phase 2: Coordinate Agents

### Objective
Queen-led coordination of agent activities and task assignments.

### Scripts

```bash
# Spawn worker agents
for i in {1..5}; do
  npx claude-flow@alpha agent spawn \
    --type researcher \
    --hive-member \
    --report-to queen
done

for i in {1..5}; do
  npx claude-flow@alpha agent spawn \
    --type coder \
    --hive-member \
    --report-to queen
done

# Queen assigns tasks
npx claude-flow@alpha hive assign \
  --task "Analyze codebase" \
  --agents "researcher-*" \
  --priority high

npx claude-flow@alpha hive assign \
  --task "Implement features" \
  --agents "coder-*" \
  --priority high \
  --depends-on "Analyze codebase"

# Monitor coordination
npx claude-flow@alpha hive monitor \
  --show-assignments \
  --show-progress \
  --interval 10

# Queen reviews progress
npx claude-flow@alpha hive review \
  --by queen \
  --output review-report.json
```

### Queen Decision Process

```bash
#!/bin/bash
# queen-decision-process.sh

# Collect agent insights
INSIGHTS=$(npx claude-flow@alpha agent collect-insights --all --format json)

# Queen analyzes
ANALYSIS=$(npx claude-flow@alpha queen analyze \
  --insights "$INSIGHTS" \
  --format json)

# Queen makes decision
DECISION=$(npx claude-flow@alpha queen decide \
  --analysis "$ANALYSIS" \
  --strategy "consensus-weighted")

# Broadcast decision to hive
npx claude-flow@alpha hive broadcast \
  --from queen \
  --message "$DECISION"

# Store decision in memory
npx claude-flow@alpha memory store \
  --key "hive/decisions/$(date +%s)" \
  --value "$DECISION"
```

## Phase 3: Synchronize Memory

### Objective
Maintain synchronized shared memory across all hive members.

### Scripts

```bash
# Setup memory synchronization
npx claude-flow@alpha memory sync init \
  --interval 5s \
  --consistency strong \
  --conflict-resolution "queen-decides"

# Monitor memory sync
npx claude-flow@alpha memory sync status \
  --show-lag \
  --show-conflicts

# Store collective insights
npx claude-flow@alpha memory store \
  --key "hive/collective/insights/$(date +%s)" \
  --value '{
    "agent": "researcher-1",
    "insight": "Pattern X detected in codebase",
    "confidence": 0.85,
    "timestamp": "'$(date -Iseconds)'"
  }'

# Retrieve collective knowledge
KNOWLEDGE=$(npx claude-flow@alpha memory retrieve \
  --key "hive/collective/*" \
  --format json)

# Build knowledge graph
npx claude-flow@alpha hive knowledge-graph \
  --build-from "$KNOWLEDGE" \
  --output knowledge-graph.json

# Visualize knowledge graph
npx claude-flow@alpha hive visualize \
  --type knowledge-graph \
  --input knowledge-graph.json \
  --output knowledge-graph.png
```

### Memory Synchronization Patterns

**Immediate Sync:**
```bash
# Critical data - sync immediately
npx claude-flow@alpha memory store \
  --key "critical/data" \
  --value "..." \
  --sync immediate
```

**Eventual Consistency:**
```bash
# Non-critical data - eventual sync
npx claude-flow@alpha memory store \
  --key "insights/data" \
  --value "..." \
  --sync eventual
```

**Conflict Resolution:**
```bash
# Queen resolves conflicts
npx claude-flow@alpha memory resolve-conflicts \
  --strategy "queen-decides" \
  --auto-apply
```

## Phase 4: Reach Consensus

### Objective
Collective decision-making through consensus mechanisms.

### Scripts

```bash
# Initiate consensus process
npx claude-flow@alpha hive consensus init \
  --proposal "Should we refactor module X?" \
  --mechanism "proof-of-intelligence" \
  --threshold 0.67

# Agents vote
npx claude-flow@alpha agent vote \
  --agent-id "researcher-1" \
  --proposal-id "proposal-001" \
  --vote yes \
  --reasoning "Complexity metrics indicate need"

# Collect votes
VOTES=$(npx claude-flow@alpha hive consensus votes \
  --proposal-id "proposal-001" \
  --format json)

# Calculate consensus
RESULT=$(npx claude-flow@alpha hive consensus calculate \
  --votes "$VOTES" \
  --mechanism "proof-of-intelligence")

# Queen validates consensus
npx claude-flow@alpha queen validate-consensus \
  --result "$RESULT" \
  --apply-decision

# Store consensus result
npx claude-flow@alpha memory store \
  --key "hive/consensus/proposal-001" \
  --value "$RESULT"
```

### Consensus Mechanisms

**Proof of Intelligence:**
- Agents with higher intelligence scores have more weight
- Based on past performance and accuracy

**Byzantine Fault Tolerant:**
- Tolerates up to 33% malicious agents
- Requires 67% agreement

**Weighted Voting:**
- Votes weighted by agent specialization
- Domain experts have more influence

**Queen Override:**
- Queen can override consensus in critical situations
- Logged and justified

## Phase 5: Execute Collectively

### Objective
Coordinated execution of collective decisions with synchronized actions.

### Scripts

```bash
# Plan collective execution
npx claude-flow@alpha hive plan-execution \
  --decision "$RESULT" \
  --output execution-plan.json

# Assign execution tasks
npx claude-flow@alpha hive execute-plan \
  --plan execution-plan.json \
  --strategy "parallel"

# Monitor collective execution
npx claude-flow@alpha hive monitor-execution \
  --plan-id "plan-001" \
  --interval 5 \
  --output execution-log.json

# Collect execution results
RESULTS=$(npx claude-flow@alpha hive collect-results \
  --plan-id "plan-001" \
  --format json)

# Queen evaluates results
EVALUATION=$(npx claude-flow@alpha queen evaluate \
  --results "$RESULTS")

# Update collective memory
npx claude-flow@alpha memory store \
  --key "hive/executions/plan-001" \
  --value '{
    "plan": "'$PLAN_ID'",
    "results": '$RESULTS',
    "evaluation": '$EVALUATION',
    "timestamp": "'$(date -Iseconds)'"
  }'

# Generate hive report
npx claude-flow@alpha hive report \
  --include-consensus \
  --include-execution \
  --include-learnings \
  --output hive-report.md
```

### Collective Learning

```bash
# Extract learnings from execution
LEARNINGS=$(npx claude-flow@alpha hive extract-learnings \
  --execution-id "plan-001" \
  --format json)

# Update collective intelligence
npx claude-flow@alpha hive update-intelligence \
  --learnings "$LEARNINGS"

# Train collective patterns
npx claude-flow@alpha neural train \
  --agent-id "collective-intelligence-coordinator" \
  --pattern convergent \
  --data "$LEARNINGS"

# Verify learning
npx claude-flow@alpha hive verify-learning \
  --test-cases test-cases.json
```

## Success Criteria

- [ ] Hive Mind initialized
- [ ] Queen coordinating effectively
- [ ] Memory synchronized
- [ ] Consensus reached on decisions
- [ ] Collective execution successful

### Performance Targets
- Consensus time: <2 minutes
- Memory sync latency: <100ms
- Queen decision time: <30 seconds
- Collective accuracy: >90%
- Coordination overhead: <15%

## Best Practices

1. **Clear Hierarchy:** Queen has final authority
2. **Shared Memory:** All agents access common knowledge
3. **Consensus Building:** Seek agreement before major decisions
4. **Continuous Learning:** Update collective intelligence
5. **Conflict Resolution:** Queen resolves conflicts quickly
6. **Pattern Recognition:** Identify and share patterns
7. **Knowledge Sharing:** Propagate insights rapidly
8. **Performance Tracking:** Monitor collective performance

## Common Issues & Solutions

### Issue: Consensus Deadlock
**Symptoms:** Agents can't reach agreement
**Solution:** Queen intervenes and makes final decision

### Issue: Memory Sync Lag
**Symptoms:** Agents have inconsistent state
**Solution:** Increase sync frequency, reduce data volume

### Issue: Queen Bottleneck
**Symptoms:** Queen overwhelmed with decisions
**Solution:** Delegate routine decisions to collective intelligence

## MCP Requirements

This skill requires the following MCP servers for optimal functionality:

### ruv-swarm (25k tokens)

**Purpose**: Multi-agent swarm coordination with collective intelligence

**Tools Used**:
- `mcp__ruv-swarm__swarm_init`: Initialize hive mind topology (mesh or star)
- `mcp__ruv-swarm__agent_spawn`: Spawn worker agents in the hive
- `mcp__ruv-swarm__agent_metrics`: Monitor individual agent performance

**Activation** (PowerShell):
```powershell
# Check if already active
claude mcp list

# Add if not present
claude mcp add ruv-swarm npx ruv-swarm mcp start
```

**Usage Example**:
```javascript
// Initialize hive mind with queen coordinator
mcp__ruv-swarm__swarm_init({
  topology: "star",
  maxAgents: 20,
  strategy: "specialized"
})

// Spawn worker agents
mcp__ruv-swarm__agent_spawn({
  type: "researcher",
  capabilities: ["analysis", "pattern-recognition"]
})

// Monitor collective performance
mcp__ruv-swarm__agent_metrics({ metric: "performance" })
```

**Token Cost**: 25k tokens (12.5% of 200k context)
**When to Load**: Always (core coordination mechanism)

### Memory MCP (8.5k tokens)

**Purpose**: Shared memory for collective intelligence and consensus

**Tools Used**:
- `mcp__memory-mcp__memory_store`: Store collective insights and decisions
- `mcp__memory-mcp__vector_search`: Find similar collective patterns

**Activation** (PowerShell):
```powershell
# Already configured
claude mcp list
```

**Usage Example**:
```javascript
// Store collective insight
const { taggedMemoryStore } = require('./hooks/12fa/memory-mcp-tagging-protocol.js');
taggedMemoryStore('collective-intelligence-coordinator', 'Pattern X detected by 5 agents', {
  consensus_score: 0.85,
  agents_agreeing: 5
});

// Retrieve collective knowledge
mcp__memory-mcp__vector_search({ query: "collective decision patterns", limit: 10 })
```

**Token Cost**: 8.5k tokens (4.25% of 200k context)
**When to Load**: Always (required for shared memory)

## Integration Points

- **advanced-swarm:** For topology optimization
- **swarm-orchestration:** For task coordination
- **performance-analysis:** For collective performance metrics

## References

- Collective Intelligence Theory
- Consensus Algorithms
- Distributed Memory Systems
- Queen-Worker Patterns

## Anti-Patterns

| Anti-Pattern | Problem | Solution |
|-------------|---------|----------|
| **Queen Bottleneck** | Queen becomes single point of failure when making all decisions, overwhelming coordination capacity and slowing collective progress. | Delegate routine decisions to collective consensus. Queen focuses only on strategic direction, conflict resolution, and exceptional cases. Implement decision delegation rules based on impact and urgency. |
| **Memory Sync Lag** | Agents operate with stale state due to infrequent or slow memory synchronization, causing inconsistent behavior and duplicate work. | Increase sync frequency for critical data paths. Use event-driven sync triggers for high-priority updates. Implement version vectors to detect and resolve conflicts. Monitor sync latency metrics. |
| **Consensus Deadlock** | Agents cannot reach agreement due to equally weighted conflicting opinions, blocking progress indefinitely without resolution mechanism. | Set consensus timeout (e.g., 2 minutes) after which queen intervenes. Implement tie-breaking rules based on agent seniority or domain expertise. Allow queen override for time-sensitive decisions. |

-----------|---------|----------|
| **Queen Bottleneck** | Queen becomes single point of failure when making all decisions, overwhelming coordination capacity and slowing collective progress. | Delegate routine decisions to collective consensus. Queen focuses only on strategic direction, conflict resolution, and exceptional cases. Implement decision delegation rules based on impact and urgency. |
| **Memory Sync Lag** | Agents operate with stale state due to infrequent or slow memory synchronization, causing inconsistent behavior and duplicate work. | Increase sync frequency for critical data paths. Use event-driven sync triggers for high-priority updates. Implement version vectors to detect and resolve conflicts. Monitor sync latency metrics. |
| **Consensus Deadlock** | Agents cannot reach agreement due to equally weighted conflicting opinions, blocking progress indefinitely without resolution mechanism. | Set consensus timeout (e.g., 2 minutes) after which queen intervenes. Implement tie-breaking rules based on agent seniority or domain expertise. Allow queen override for time-sensitive decisions. |

## Conclusion

The Hive Mind collective intelligence system transforms isolated agents into a coordinated organism capable of solving complex problems through distributed cognition and emergent consensus. By combining queen-led strategic direction with worker autonomy and collective decision-making, the system achieves both decisive leadership and diverse perspectives. The shared memory layer serves as the hive's nervous system, propagating learnings across all members and enabling pattern recognition that no single agent could achieve alone.

Success with Hive Mind depends on balancing centralized authority with distributed intelligence. The queen must resist the temptation to micromanage and instead focus on high-level strategy, allowing specialists to execute with autonomy within their domains. Consensus mechanisms aggregate these diverse perspectives into collective decisions that are more robust than any individual agent's judgment. When conflicts arise, the queen's authority provides decisive resolution without undermining the value of collective input.

The memory synchronization architecture is critical infrastructure - without rapid, consistent state sharing, the hive devolves into disconnected individuals working at cross purposes. Strong consistency for critical data ensures coordination safety, while eventual consistency for learnings optimizes for performance. The knowledge graph elevates raw memory storage into structured collective intelligence, enabling pattern recognition and insight reuse that compounds over time. Teams implementing Hive Mind should treat memory architecture as first-class infrastructure, not an afterthought, and invest in monitoring sync latency, conflict rates, and knowledge graph connectivity to maintain collective intelligence quality.