/*============================================================================*/
/* SKILL SKILL :: VERILINGUA x VERIX EDITION                      */
/*============================================================================*/

---
name: SKILL
version: 1.0.0
description: |
  [assert|neutral] Intelligent multi-model orchestrator that routes tasks to Gemini or Codex based on their strengths [ground:given] [conf:0.95] [state:confirmed]
category: platforms
tags:
- orchestration
- multi-model
- routing
- automation
- gemini
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

# Multi-Model Orchestrator Skill

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



## Purpose
Automatically route tasks to the optimal AI model (Gemini or Codex) based on task requirements and each model's unique strengths. You don't need to decide - the orchestrator does it for you.

## How It Works

The orchestrator analyzes your request and routes to:

### Gemini CLI → For:
- **Mega-Context**: Large codebase analysis (30K+ lines)
- **Web Search**: Real-time information needs
- **Media Gen**: Image/video creation
- **Extensions**: Figma, Stripe, Postman integrations

### Codex CLI → For:
- **Full Auto**: Unattended prototyping/scaffolding
- **Alternative Reasoning**: Second opinions, different approaches

### Claude Code → For:
- **Everything Else**: Implementation, refinement, complex reasoning

## Usage

### Let Orchestrator Decide
```
/multi-model "I need to understand this 50K line codebase and create architecture diagrams"

Orchestrator routes to:
1. gemini-megacontext (analyze codebase)
2. gemini-media (create diagrams)
```

### Complex Multi-Step Tasks
```
/multi-model "Research React 19 best practices, prototype a dashboard, and generate UI mockups"

Orchestrator routes to:
1. gemini-search (React 19 info)
2. codex-auto (prototype dashboard)
3. gemini-media (UI mockups)
4. Claude Code (integrate and refine)
```

## Decision Matrix

| Task Type | Routed To | Why |
|-----------|-----------|-----|
| Analyze entire codebase | gemini-megacontext | 1M token context |
| Need current API docs | gemini-search | Web search grounding |
| Create diagrams/videos | gemini-media | Imagen/Veo |
| Figma/Stripe integration | gemini-extensions | Extension ecosystem |
| Rapid prototyping | codex-auto | Full Auto mode |
| Alternative solution | codex-reasoning | Different AI perspective |
| Implementation/refinement | Claude Code | Best overall reasoning |

## Real Examples

### Example 1: New Project Setup
```
User: "Set up a new Next.js 15 project with best practices"

Orchestrator:
1. gemini-search → Get Next.js 15 current best practices
2. codex-auto → Scaffold project structure
3. Claude Code → Customize and refine
```

### Example 2: Codebase Migration
```
User: "Migrate this legacy codebase to TypeScript"

Orchestrator:
1. gemini-megacontext → Analyze entire codebase structure
2. codex-auto → Auto-convert files to TypeScript
3. Claude Code → Fix type errors and refine
```

### Example 3: Documentation Creation
```
User: "Create comprehensive documentation with visuals"

Orchestrator:
1. gemini-megacontext → Understand architecture
2. gemini-media → Generate architecture diagrams
3. Claude Code → Write documentation content
```

## Benefits

### Automatic Optimization
- ✅ Uses each model's unique strengths
- ✅ No need to remember which CLI does what
- ✅ Optimal tool selection for each subtask
- ✅ Coordinates multiple models seamlessly

### Cost Efficiency
- ✅ Uses Gemini's free tier when appropriate (60/min, 1000/day)
- ✅ Leverages your ChatGPT Plus subscription optimally
- ✅ Uses Claude Code for what it does best

### Time Savings
- ✅ Parallel execution when possible
- ✅ No manual routing decisions
- ✅ Automatic task decomposition

## Response Format

The orchestrator provides:
```markdown
# Multi-Model Task Orchestration

## Task Analysis
[How the task was broken down]

## Routing Decisions
1. **gemini-megacontext**: [Why and what]
2. **codex-auto**: [Why and what]
3. **Claude Code**: [Why and what]

## Execution Plan
[Step-by-step execution order]

## Results from Each Model
### Gemini Results
[Output summary]

### Codex Results
[Output summary]

### Claude Integration
[How Claude combined/refined results]

## Final Deliverable
[Combined, polished output]
```

## When to Use

### Perfect For:
✅ Don't know which model to use
✅ Task spans multiple capabilities
✅ Want automatic optimization
✅ Complex multi-step workflows
✅ Learning which model does what

### Direct Skill Use Instead:
Use specific sk

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
