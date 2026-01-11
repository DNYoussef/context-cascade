/*============================================================================*/
/* AGENT-SELECTOR SKILL :: VERILINGUA x VERIX EDITION                      */
/*============================================================================*/

---
name: agent-selector
version: 2.1.0
description: |
  [assert|neutral] Intelligent agent selection from 203-agent registry using semantic matching and capability analysis [ground:given] [conf:0.95] [state:confirmed]
category: orchestration
tags:
- general
author: System
cognitive_frame:
  primary: evidential
  goal_analysis:
    first_order: "Execute agent-selector workflow"
    second_order: "Ensure quality and consistency"
    third_order: "Enable systematic orchestration processes"
---

/*----------------------------------------------------------------------------*/
/* S0 META-IDENTITY                                                            */
/*----------------------------------------------------------------------------*/

[define|neutral] SKILL := {
  name: "agent-selector",
  category: "orchestration",
  version: "2.1.0",
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
  keywords: ["agent-selector", "orchestration", "workflow"],
  context: "user needs agent-selector capability"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S3 CORE CONTENT                                                             */
/*----------------------------------------------------------------------------*/

# Agent Selector Micro-Skill

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



## Phase 0: Expertise Loading

Before selecting agents:

1. **Detect Domain**: Identify task domain from request
2. **Check Expertise**: Look for `.claude/expertise/agent-selection.yaml`
3. **Load Context**: If exists, load agent performance history and preferences
4. **Apply Configuration**: Use expertise for optimal agent matching

## Purpose

Intelligently selects the most appropriate specialized agent from the 203-agent registry based on:
- Task requirements and complexity
- Agent capabilities and specializations
- Domain expertise (category/subcategory)
- Tool and MCP requirements
- Phase alignment (planning, development, testing, etc.)

**Critical for Phase 4 routing** to ensure Claude Code uses specialized agents instead of generic ones.

## When to Use

- **Before any Task() invocation** in Phase 5 execution
- When planning multi-agent workflows and need optimal agent assignment
- When you're unsure which specialized agent to use for a task
- To validate that a generic agent name has a specialized alternative

## How It Works

**4-Step Process:**

1. **Parse Task Requirements**
   - Extract domain (backend, frontend, database, testing, etc.)
   - Identify key capabilities needed (Express.js, PostgreSQL, TDD, etc.)
   - Determine phase (planning, development, testing, deployment)
   - Note tool/MCP requirements

2. **Semantic Search (Memory MCP)**
   - Query Memory MCP with task description
   - Get top 5-10 candidate agents ranked by similarity
   - Filter by category/phase if known

3. **Capability Matching**
   - Score each candidate agent based on:
     - Exact capability matches (highest priority)
     - Domain specialization (category/subcategory)
     - Tool/MCP alignment
     - Phase alignment
   - Apply fallback rules if no perfect match

4. **Return Selection + Reasoning**
   - Selected agent name
   - Agent source (file path in registry)
   - Capabilities that matched
   - Alternatives considered
   - Selection reasoning

## Usage

```javascript
// Skill invocation
Skill("agent-selector")

// Agent will prompt you for:
// 1. Task description (what needs to be done)
// 2. Domain hint (optional: backend, frontend, testing, etc.)
// 3. Phase hint (optional: development, testing, deployment)

// Output:
{
  "selected_agent": "dev-backend-api",
  "agent_source": "delivery/development/backend/dev-backend-api.md",
  "agent_category": "delivery/development/backend",
  "capabilities": ["Express.js", "REST APIs", "JWT", "OpenAPI"],
  "selection_reasoning": "Specialized backend API agent with exact match for Express.js + REST requirements",
  "alternatives_considered": [
    {
      "name": "backend-specialist",
      "score": 0.82,
      "reason": "Less API-specific, more general backend work"
    }
  ],
  "confidence": 0.95
}
```

## Integration with Phase 4 Routing

**Automatic Integration:**

When Phase 4 routing runs, it MUST use this skill (or inline equivalent) to select agents:

```javascript
// Phase 4 Routing
for (const task of plan.tasks) {
  // Invoke agent-selector
  const agentSelection = Skill("agent-selector", {
    task: task.description,
    domain: task.domain,
    phase: task.phase
  });

  // Use selected agent in Phase 5
  task.agent = agentSelection.selected_agent;
  task.agent_source = agentSelection.agent_source;
  task.agent_capabilities = agentSelection.capabilities;
  task.agent_reasoning = agentSelection.selection_reasoning;
}
```

## Agent Selection Criteria (Priority Order)

1. **Exact Capability Match** (score: 1.0)
   - Agent metadata lists exact task requirement
   - Example: "Express.js API development" → dev-backend-api

2. **Domain Specialization** (score: 0.9)
   - Agent is in correct category/subcategory
   - Example: Backend task → delivery/development/backend agents

3. **Tool Requirements** (score: 0.8)
   - Agent has required tools/MCP servers
   - Example: Needs Post

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
  pattern: "skills/orchestration/agent-selector/{project}/{timestamp}",
  store: ["executions", "decisions", "patterns"],
  retrieve: ["similar_tasks", "proven_patterns"]
} [ground:system-policy] [conf:1.0] [state:confirmed]

[define|neutral] MEMORY_TAGGING := {
  WHO: "agent-selector-{session_id}",
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

[commit|confident] <promise>AGENT_SELECTOR_VERILINGUA_VERIX_COMPLIANT</promise> [ground:self-validation] [conf:0.99] [state:confirmed]
