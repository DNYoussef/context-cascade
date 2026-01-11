# Hive Mind Collective Intelligence - Quick Start

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



Queen-led multi-agent coordination with consensus and shared memory.

## Quick Start

```bash
# 1. Initialize Hive Mind
npx claude-flow@alpha hive init --queen-enabled --max-agents 20

# 2. Spawn coordinators
npx claude-flow@alpha agent spawn --role "queen-coordinator"
npx claude-flow@alpha agent spawn --role "collective-intelligence-coordinator"
npx claude-flow@alpha agent spawn --role "swarm-memory-manager"

# 3. Spawn workers and coordinate
npx claude-flow@alpha agent spawn --type researcher --hive-member --count 5
npx claude-flow@alpha hive assign --task "Analyze project" --agents "researcher-*"

# 4. Reach consensus and execute
npx claude-flow@alpha hive consensus init --proposal "Refactor module X"
npx claude-flow@alpha hive execute-plan --plan execution-plan.json
```

## Agents
- **collective-intelligence-coordinator:** Aggregate insights
- **queen-coordinator:** Strategic direction
- **swarm-memory-manager:** Shared memory

## Success Metrics
- [assert|neutral] Consensus time: <2 min [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] Memory sync: <100ms [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] Collective accuracy: >90% [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] Promise: `<promise>README_VERIX_COMPLIANT</promise>`* [ground:acceptance-criteria] [conf:0.90] [state:provisional]
