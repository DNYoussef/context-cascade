/*============================================================================*/
/* AGENTDB REINFORCEMENT LEARNING TRAINING SKILL :: VERILINGUA x VERIX EDITION                      */
/*============================================================================*/

---
name: AgentDB Reinforcement Learning Training
version: 1.0.0
description: |
  [assert|neutral] AgentDB Reinforcement Learning Training skill for agentdb workflows [ground:given] [conf:0.95] [state:confirmed]
category: agentdb
tags:
- general
author: system
cognitive_frame:
  primary: evidential
  goal_analysis:
    first_order: "Execute AgentDB Reinforcement Learning Training workflow"
    second_order: "Ensure quality and consistency"
    third_order: "Enable systematic agentdb processes"
---

/*----------------------------------------------------------------------------*/
/* S0 META-IDENTITY                                                            */
/*----------------------------------------------------------------------------*/

[define|neutral] SKILL := {
  name: "AgentDB Reinforcement Learning Training",
  category: "agentdb",
  version: "1.0.0",
  layer: L1
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S1 COGNITIVE FRAME                                                          */
/*----------------------------------------------------------------------------*/

[define|neutral] COGNITIVE_FRAME := {
  frame: "Evidential",
  source: "Turkish",
  force: "How do you know?"
} [ground:cognitive-science] [conf:0.92] [state:confirmed]

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.

/*----------------------------------------------------------------------------*/
/* S2 TRIGGER CONDITIONS                                                       */
/*----------------------------------------------------------------------------*/

[define|neutral] TRIGGER_POSITIVE := {
  keywords: ["AgentDB Reinforcement Learning Training", "agentdb", "workflow"],
  context: "user needs AgentDB Reinforcement Learning Training capability"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S3 CORE CONTENT                                                             */
/*----------------------------------------------------------------------------*/

# AgentDB Reinforcement Learning Training

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



## Overview

Train AI learning plugins with AgentDB's 9 reinforcement learning algorithms including Decision Transformer, Q-Learning, SARSA, Actor-Critic, PPO, and more. Build self-learning agents, implement RL, and optimize agent behavior through experience.

## When to Use This Skill

Use this skill when you need to:
- Train autonomous agents that learn from experience
- Implement reinforcement learning systems
- Optimize agent behavior through trial and error
- Build self-improving AI systems
- Deploy RL agents in production environments
- Benchmark and compare RL algorithms

## Available RL Algorithms

1. **Q-Learning** - Value-based, off-policy
2. **SARSA** - Value-based, on-policy
3. **Deep Q-Network (DQN)** - Deep RL with experience replay
4. **Actor-Critic** - Policy gradient with value baseline
5. **Proximal Policy Optimization (PPO)** - Trust region policy optimization
6. **Decision Transformer** - Offline RL with transformers
7. **Advantage Actor-Critic (A2C)** - Synchronous advantage estimation
8. **Twin Delayed DDPG (TD3)** - Continuous control
9. **Soft Actor-Critic (SAC)** - Maximum entropy RL

## SOP Framework: 5-Phase RL Training Deployment

### Phase 1: Initialize Learning Environment (1-2 hours)

**Objective:** Setup AgentDB learning infrastructure with environment configuration

**Agent:** ml-developer

**Steps:**

1. **Install AgentDB Learning Module**
```bash
npm install agentdb-learning@latest
npm install @agentdb/rl-algorithms @agentdb/environments
```

2. **Initialize learning database**
```typescript
import { AgentDB, LearningPlugin } from 'agentdb-learning';

const learningDB = new AgentDB({
  name: 'rl-training-db',
  dimensions: 512, // State embedding dimension
  learning: {
    enabled: true,
    persistExperience: true,
    replayBufferSize: 100000
  }
});

await learningDB.initialize();

// Create learning plugin
const learningPlugin = new LearningPlugin({
  database: learningDB,
  algorithms: ['q-learning', 'dqn', 'ppo', 'actor-critic'],
  config: {
    batchSize: 64,
    learningRate: 0.001,
    discountFactor: 0.99,
    explorationRate: 1.0,
    explorationDecay: 0.995
  }
});

await learningPlugin.initialize();
```

3. **Define environment**
```typescript
import { Environment } from '@agentdb/environments';

const environment = new Environment({
  name: 'grid-world',
  stateSpace: {
    type: 'continuous',
    shape: [10, 10],
    bounds: [[0, 10], [0, 10]]
  },
  actionSpace: {
    type: 'discrete',
    actions: ['up', 'down', 'left', 'right']
  },
  rewardFunction: (state, action, nextState) => {
    // Distance to goal reward
    const goalDistance = Math.sqrt(
      Math.pow(nextState[0] - 9, 2) +
      Math.pow(nextState[1] - 9, 2)
    );
    return -goalDistance + (goalDistance === 0 ? 100 : 0);
  },
  terminalCondition: (state) => {
    return state[0] === 9 && state[1] === 9; // Reached goal
  }
});

await environment.initialize();
```

4. **Setup monitoring**
```typescript
const monitor = learningPlugin.createMonitor({
  metrics: ['reward', 'loss', 'exploration-rate', 'episode-length'],
  logInterval: 100, // Log every 100 episodes
  saveCheckpoints: true,
  checkpointInterval: 1000
});

monitor.on('episode-complete', (episode) => {
  console.log('Episode:', episode.number, 'Reward:', episode.totalReward);
});
```

**Memory Pattern:**
```typescript
await agentDB.memory.store('agentdb/learning/environment', {
  name: environment.name,
  stateSpace: environment.stateSpace,
  actionSpace: environment.actionSpace,
  initialized: Date.now()
});
```

**Validation:**
- Learning database initialized
- Environment configured and tested
- Monitor capturing metrics
- Configuration stored in memory

### Phase 2: Configure RL Algorithm (1-2 hours)

**Objective:** Select and configure RL algorithm for the learning task

**Agent:** ml-developer

**Steps:**

1. **Select algo

/*----------------------------------------------------------------------------*/
/* S4 SUCCESS CRITERIA                                                         */
/*----------------------------------------------------------------------------*/

[define|neutral] SUCCESS_CRITERIA := {
  primary: "Skill execution completes successfully",
  quality: "Output meets quality thresholds",
  verification: "Results validated against requirements"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S5 MCP INTEGRATION                                                          */
/*----------------------------------------------------------------------------*/

[define|neutral] MCP_INTEGRATION := {
  memory_mcp: "Store execution results and patterns",
  tools: ["mcp__memory-mcp__memory_store", "mcp__memory-mcp__vector_search"]
} [ground:witnessed:mcp-config] [conf:0.95] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S6 MEMORY NAMESPACE                                                         */
/*----------------------------------------------------------------------------*/

[define|neutral] MEMORY_NAMESPACE := {
  pattern: "skills/agentdb/AgentDB Reinforcement Learning Training/{project}/{timestamp}",
  store: ["executions", "decisions", "patterns"],
  retrieve: ["similar_tasks", "proven_patterns"]
} [ground:system-policy] [conf:1.0] [state:confirmed]

[define|neutral] MEMORY_TAGGING := {
  WHO: "AgentDB Reinforcement Learning Training-{session_id}",
  WHEN: "ISO8601_timestamp",
  PROJECT: "{project_name}",
  WHY: "skill-execution"
} [ground:system-policy] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S7 SKILL COMPLETION VERIFICATION                                            */
/*----------------------------------------------------------------------------*/

[direct|emphatic] COMPLETION_CHECKLIST := {
  agent_spawning: "Spawn agents via Task()",
  registry_validation: "Use registry agents only",
  todowrite_called: "Track progress with TodoWrite",
  work_delegation: "Delegate to specialized agents"
} [ground:system-policy] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S8 ABSOLUTE RULES                                                           */
/*----------------------------------------------------------------------------*/

[direct|emphatic] RULE_NO_UNICODE := forall(output): NOT(unicode_outside_ascii) [ground:windows-compatibility] [conf:1.0] [state:confirmed]

[direct|emphatic] RULE_EVIDENCE := forall(claim): has(ground) AND has(confidence) [ground:verix-spec] [conf:1.0] [state:confirmed]

[direct|emphatic] RULE_REGISTRY := forall(agent): agent IN AGENT_REGISTRY [ground:system-policy] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* PROMISE                                                                     */
/*----------------------------------------------------------------------------*/

[commit|confident] <promise>AGENTDB REINFORCEMENT LEARNING TRAINING_VERILINGUA_VERIX_COMPLIANT</promise> [ground:self-validation] [conf:0.99] [state:confirmed]
