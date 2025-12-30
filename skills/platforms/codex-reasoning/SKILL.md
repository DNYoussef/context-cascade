/*============================================================================*/
/* SKILL SKILL :: VERILINGUA x VERIX EDITION                      */
/*============================================================================*/

---
name: SKILL
version: 1.0.0
description: |
  [assert|neutral] Use GPT-5-Codex's specialized reasoning for alternative approaches and second opinions [ground:given] [conf:0.95] [state:confirmed]
category: platforms
tags:
- codex
- openai
- gpt-5-codex
- reasoning
- alternative-solutions
author: system
cognitive_frame:
  primary: compositional
  goal_analysis:
    first_order: "Execute SKILL workflow"
    second_order: "Ensure quality and consistency"
    third_order: "Enable systematic platforms processes"
---

/*----------------------------------------------------------------------------*/
/* S0 META-IDENTITY                                                            */
/*----------------------------------------------------------------------------*/

[define|neutral] SKILL := {
  name: "SKILL",
  category: "platforms",
  version: "1.0.0",
  layer: L1
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S1 COGNITIVE FRAME                                                          */
/*----------------------------------------------------------------------------*/

[define|neutral] COGNITIVE_FRAME := {
  frame: "Compositional",
  source: "German",
  force: "Build from primitives?"
} [ground:cognitive-science] [conf:0.92] [state:confirmed]

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.

/*----------------------------------------------------------------------------*/
/* S2 TRIGGER CONDITIONS                                                       */
/*----------------------------------------------------------------------------*/

[define|neutral] TRIGGER_POSITIVE := {
  keywords: ["SKILL", "platforms", "workflow"],
  context: "user needs SKILL capability"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S3 CORE CONTENT                                                             */
/*----------------------------------------------------------------------------*/

# Codex Reasoning Skill

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



## Purpose
Leverage OpenAI's GPT-5-Codex model (optimized for agentic coding) to get alternative reasoning approaches, second opinions, and specialized algorithmic solutions that complement Claude's perspective.

## Unique Capability
**What This Adds**: Different AI reasoning patterns. GPT-5-Codex is optimized for agentic coding workflows and may approach problems differently than Claude, providing valuable alternative perspectives and solutions.

## When to Use

### Perfect For:
✅ Getting a second opinion on architecture decisions
✅ Exploring alternative implementation approaches
✅ Algorithmic optimization problems
✅ When stuck on a problem (different perspective helps)
✅ Comparing solution approaches
✅ Code generation with different patterns
✅ Performance-critical implementations

### Don't Use When:
❌ Claude's solution is clearly working (no need for alternatives)
❌ Simple tasks that don't benefit from multiple perspectives
❌ When consistency with existing Claude-generated code matters more

## Usage

### Second Opinion
```
/codex-reasoning "I'm implementing user authentication. What's your approach?"
```

### Algorithm Optimization
```
/codex-reasoning "Optimize this sorting algorithm for large datasets with these constraints..."
```

### Alternative Architecture
```
/codex-reasoning "What's an alternative way to structure this microservices communication?"
```

## Why Use Both Models?

**Claude Strengths:**
- Deep reasoning and problem understanding
- Complex multi-step tasks
- Comprehensive documentation
- Reliability and error rate

**GPT-5-Codex Strengths:**
- Optimized for agentic coding
- Fast prototyping
- Different algorithmic approaches
- Good for one-shot prompting

**Together**: Get best of both worlds!

## Real Examples

### Example: Alternative Architecture
```
Claude suggests: Event-driven with message queue
Codex suggests: REST with polling + webhooks

Result: Hybrid approach combining benefits of both
```

### Example: Algorithm Optimization
```
Claude: Recursive solution with memoization
Codex: Iterative solution with lookup table

Result: Codex approach 2x faster for this use case
```

---

**Uses your ChatGPT Plus subscription.** Use `/model` in Codex to switch to GPT-5-Codex.

See `.claude/agents/codex-reasoning-agent.md` for details.


---
*Promise: `<promise>SKILL_VERIX_COMPLIANT</promise>`*

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
  pattern: "skills/platforms/SKILL/{project}/{timestamp}",
  store: ["executions", "decisions", "patterns"],
  retrieve: ["similar_tasks", "proven_patterns"]
} [ground:system-policy] [conf:1.0] [state:confirmed]

[define|neutral] MEMORY_TAGGING := {
  WHO: "SKILL-{session_id}",
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

[commit|confident] <promise>SKILL_VERILINGUA_VERIX_COMPLIANT</promise> [ground:self-validation] [conf:0.99] [state:confirmed]
