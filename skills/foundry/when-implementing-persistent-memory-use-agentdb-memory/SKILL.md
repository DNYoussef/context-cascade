/*============================================================================*/
/* AGENTDB PERSISTENT MEMORY PATTERNS SKILL :: VERILINGUA x VERIX EDITION                      */
/*============================================================================*/

---
name: AgentDB Persistent Memory Patterns
version: 1.0.0
description: |
  [assert|neutral] AgentDB Persistent Memory Patterns skill for agentdb workflows [ground:given] [conf:0.95] [state:confirmed]
category: agentdb
tags:
- general
author: system
cognitive_frame:
  primary: evidential
  goal_analysis:
    first_order: "Execute AgentDB Persistent Memory Patterns workflow"
    second_order: "Ensure quality and consistency"
    third_order: "Enable systematic agentdb processes"
---

/*----------------------------------------------------------------------------*/
/* S0 META-IDENTITY                                                            */
/*----------------------------------------------------------------------------*/

[define|neutral] SKILL := {
  name: "AgentDB Persistent Memory Patterns",
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
  keywords: ["AgentDB Persistent Memory Patterns", "agentdb", "workflow"],
  context: "user needs AgentDB Persistent Memory Patterns capability"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S3 CORE CONTENT                                                             */
/*----------------------------------------------------------------------------*/

# AgentDB Persistent Memory Patterns

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



## Overview

Implement persistent memory patterns for AI agents using AgentDB - session memory, long-term storage, pattern learning, and context management for stateful agents, chat systems, and intelligent assistants.

## SOP Framework: 5-Phase Memory Implementation

### Phase 1: Design Memory Architecture (1-2 hours)
- Define memory schemas (episodic, semantic, procedural)
- Plan storage layers (short-term, working, long-term)
- Design retrieval mechanisms
- Configure persistence strategies

### Phase 2: Implement Storage Layer (2-3 hours)
- Create memory stores in AgentDB
- Implement session management
- Build long-term memory persistence
- Setup memory indexing

### Phase 3: Test Memory Operations (1-2 hours)
- Validate store/retrieve operations
- Test memory consolidation
- Verify pattern recognition
- Benchmark performance

### Phase 4: Optimize Performance (1-2 hours)
- Implement caching layers
- Optimize retrieval queries
- Add memory compression
- Performance tuning

### Phase 5: Document Patterns (1 hour)
- Create usage documentation
- Document memory patterns
- Write integration examples
- Generate API documentation

## Quick Start

```typescript
import { AgentDB, MemoryManager } from 'agentdb-memory';

// Initialize memory system
const memoryDB = new AgentDB({
  name: 'agent-memory',
  dimensions: 768,
  memory: {
    sessionTTL: 3600,
    consolidationInterval: 300,
    maxSessionSize: 1000
  }
});

const memoryManager = new MemoryManager({
  database: memoryDB,
  layers: ['episodic', 'semantic', 'procedural']
});

// Store memory
await memoryManager.store({
  type: 'episodic',
  content: 'User preferred dark theme',
  context: { userId: '123', timestamp: Date.now() }
});

// Retrieve memory
const memories = await memoryManager.retrieve({
  query: 'user preferences',
  type: 'episodic',
  limit: 10
});
```

## Memory Patterns

### Session Memory
```typescript
const session = await memoryManager.createSession('user-123');
await session.store('conversation', messageHistory);
await session.store('preferences', userPrefs);
const context = await session.getContext();
```

### Long-Term Storage
```typescript
await memoryManager.consolidate({
  from: 'working-memory',
  to: 'long-term-memory',
  strategy: 'importance-based'
});
```

### Pattern Learning
```typescript
const patterns = await memoryManager.learnPatterns({
  memory: 'episodic',
  algorithm: 'clustering',
  minSupport: 0.1
});
```

## Success Metrics
- [assert|neutral] Memory persists across agent restarts [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] Retrieval latency < 50ms (p95) [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] Pattern recognition accuracy > 85% [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] Context maintained with 95% accuracy [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] Memory consolidation working [ground:acceptance-criteria] [conf:0.90] [state:provisional]

## MCP Requirements

This skill operates using AgentDB's npm package and API only. No additional MCP servers required.

All AgentDB memory operations are performed through:
- npm CLI: `npx agentdb@latest`
- TypeScript/JavaScript API: `import { AgentDB, MemoryManager } from 'agentdb-memory'`

## Additional Resources

- Full documentation: SKILL.md
- Process guide: PROCESS.md
- AgentDB Memory Docs: https://agentdb.dev/docs/memory

## Core Principles

AgentDB Persistent Memory Patterns operates on 3 fundamental principles:

### Principle 1: Memory Layering - Separate Short-Term, Working, and Long-Term Storage

Memory systems mirror human cognition by organizing information across distinct temporal layers. Short-term memory handles immediate context (current conversation), working memory maintains active task state, and long-term memory co

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
  pattern: "skills/agentdb/AgentDB Persistent Memory Patterns/{project}/{timestamp}",
  store: ["executions", "decisions", "patterns"],
  retrieve: ["similar_tasks", "proven_patterns"]
} [ground:system-policy] [conf:1.0] [state:confirmed]

[define|neutral] MEMORY_TAGGING := {
  WHO: "AgentDB Persistent Memory Patterns-{session_id}",
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

[commit|confident] <promise>AGENTDB PERSISTENT MEMORY PATTERNS_VERILINGUA_VERIX_COMPLIANT</promise> [ground:self-validation] [conf:0.99] [state:confirmed]
