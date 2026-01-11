/*============================================================================*/
/* REASONINGBANK-INTELLIGENCE SKILL :: VERILINGUA x VERIX EDITION                      */
/*============================================================================*/

---
name: reasoningbank-intelligence
version: 1.0.0
description: |
  [assert|neutral] Implement adaptive learning with ReasoningBank for pattern recognition, strategy optimization, and continuous improvement. Use when building self-learning agents, optimizing workflows, or implementing [ground:given] [conf:0.95] [state:confirmed]
category: platforms
tags:
- platforms
- integration
- tools
author: ruv
cognitive_frame:
  primary: aspectual
  goal_analysis:
    first_order: "Execute reasoningbank-intelligence workflow"
    second_order: "Ensure quality and consistency"
    third_order: "Enable systematic platforms processes"
---

/*----------------------------------------------------------------------------*/
/* S0 META-IDENTITY                                                            */
/*----------------------------------------------------------------------------*/

[define|neutral] SKILL := {
  name: "reasoningbank-intelligence",
  category: "platforms",
  version: "1.0.0",
  layer: L1
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S1 COGNITIVE FRAME                                                          */
/*----------------------------------------------------------------------------*/

[define|neutral] COGNITIVE_FRAME := {
  frame: "Aspectual",
  source: "Russian",
  force: "Complete or ongoing?"
} [ground:cognitive-science] [conf:0.92] [state:confirmed]

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.

/*----------------------------------------------------------------------------*/
/* S2 TRIGGER CONDITIONS                                                       */
/*----------------------------------------------------------------------------*/

[define|neutral] TRIGGER_POSITIVE := {
  keywords: ["reasoningbank-intelligence", "platforms", "workflow"],
  context: "user needs reasoningbank-intelligence capability"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S3 CORE CONTENT                                                             */
/*----------------------------------------------------------------------------*/

## When NOT to Use This Skill

- Simple fact retrieval without reasoning chains
- Operations that do not require logical inference
- Tasks without complex multi-step reasoning needs
- Applications that do not benefit from reasoning trace storage

## Success Criteria
- [assert|neutral] Reasoning chain accuracy: >90% logically valid steps [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] Retrieval relevance: Top-5 recall >0.85 for similar reasoning [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] Storage efficiency: <1MB per 100 reasoning chains [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] Query latency: <50ms for reasoning retrieval [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] Integration success: Seamless connection with AgentDB backend [ground:acceptance-criteria] [conf:0.90] [state:provisional]

## Edge Cases & Error Handling

- **Invalid Reasoning Chains**: Validate logical consistency before storage
- **Retrieval Failures**: Fallback to alternative search strategies
- **Storage Limits**: Implement pruning strategies for old/low-quality chains
- **Embedding Mismatches**: Ensure consistent embedding models across storage/retrieval
- **Circular Reasoning**: Detect and prevent circular reference chains

## Guardrails & Safety
- [assert|emphatic] NEVER: store reasoning chains with sensitive or PII data [ground:policy] [conf:0.98] [state:confirmed]
- [assert|neutral] ALWAYS: validate reasoning quality before storage [ground:policy] [conf:0.98] [state:confirmed]
- [assert|neutral] ALWAYS: sanitize inputs to prevent prompt injection [ground:policy] [conf:0.98] [state:confirmed]
- [assert|emphatic] NEVER: expose internal reasoning structures in public APIs [ground:policy] [conf:0.98] [state:confirmed]
- [assert|neutral] ALWAYS: implement access control for reasoning retrieval [ground:policy] [conf:0.98] [state:confirmed]
- [assert|neutral] ALWAYS: audit reasoning chains for bias and harmful content [ground:policy] [conf:0.98] [state:confirmed]

## Evidence-Based Validation

- Verify reasoning quality: Check logical consistency and validity
- Validate retrieval: Test that similar reasoning is correctly retrieved
- Monitor storage: Track database size and query performance
- Test edge cases: Validate handling of complex/invalid reasoning chains
- Benchmark improvements: Measure reasoning quality vs baseline methods


# ReasoningBank Intelligence

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



## What This Skill Does

Implements ReasoningBank's adaptive learning system for AI agents to learn from experience, recognize patterns, and optimize strategies over time. Enables meta-cognitive capabilities and continuous improvement.

## Prerequisites

- agentic-flow v1.5.11+
- AgentDB v1.0.4+ (for persistence)
- Node.js 18+

## Quick Start

```typescript
import { ReasoningBank } from 'agentic-flow/reasoningbank';

// Initialize ReasoningBank
const rb = new ReasoningBank({
  persist: true,
  learningRate: 0.1,
  adapter: 'agentdb' // Use AgentDB for storage
});

// Record task outcome
await rb.recordExperience({
  task: 'code_review',
  approach: 'static_analysis_first',
  outcome: {
    success: true,
    metrics: {
      bugs_found: 5,
      time_taken: 120,
      false_positives: 1
    }
  },
  context: {
    language: 'typescript',
    complexity: 'medium'
  }
});

// Get optimal strategy
const strategy = await rb.recommendStrategy('code_review', {
  language: 'typescript',
  complexity: 'high'
});
```

## Core Features

### 1. Pattern Recognition
```typescript
// Learn patterns from data
await rb.learnPattern({
  pattern: 'api_errors_increase_after_deploy',
  triggers: ['deployment', 'traffic_spike'],
  actions: ['rollback', 'scale_up'],
  confidence: 0.85
});

// Match patterns
const matches = await rb.matchPatterns(currentSituation);
```

### 2. Strategy Optimization
```typ

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
  pattern: "skills/platforms/reasoningbank-intelligence/{project}/{timestamp}",
  store: ["executions", "decisions", "patterns"],
  retrieve: ["similar_tasks", "proven_patterns"]
} [ground:system-policy] [conf:1.0] [state:confirmed]

[define|neutral] MEMORY_TAGGING := {
  WHO: "reasoningbank-intelligence-{session_id}",
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

[commit|confident] <promise>REASONINGBANK_INTELLIGENCE_VERILINGUA_VERIX_COMPLIANT</promise> [ground:self-validation] [conf:0.99] [state:confirmed]
