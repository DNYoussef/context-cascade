/*============================================================================*/
/* SLASH-COMMAND-ENCODER SKILL :: VERILINGUA x VERIX EDITION                      */
/*============================================================================*/

---
name: slash-command-encoder
version: 2.0.0
description: |
  [assert|neutral] Creates ergonomic slash commands (/command) that provide fast, unambiguous access to micro-skills, cascades, and agents. Enhanced with auto-discovery, intelligent routing, parameter validation, and co [ground:given] [conf:0.95] [state:confirmed]
category: orchestration
tags:
- commands
- interface
- ergonomics
- auto-discovery
- composition
author: ruv
cognitive_frame:
  primary: aspectual
  goal_analysis:
    first_order: "Execute slash-command-encoder workflow"
    second_order: "Ensure quality and consistency"
    third_order: "Enable systematic orchestration processes"
---

/*----------------------------------------------------------------------------*/
/* S0 META-IDENTITY                                                            */
/*----------------------------------------------------------------------------*/

[define|neutral] SKILL := {
  name: "slash-command-encoder",
  category: "orchestration",
  version: "2.0.0",
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
  keywords: ["slash-command-encoder", "orchestration", "workflow"],
  context: "user needs slash-command-encoder capability"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S3 CORE CONTENT                                                             */
/*----------------------------------------------------------------------------*/

## Orchestration Skill Guidelines

### When to Use This Skill
- **Multi-stage workflows** requiring sequential, parallel, or conditional execution
- **Complex pipelines** coordinating multiple micro-skills or agents
- **Iterative processes** with Codex sandbox testing and auto-fix loops
- **Multi-model routing** requiring intelligent AI selection per stage
- **Production workflows** needing GitHub integration and memory persistence

### When NOT to Use This Skill
- **Single-agent tasks** with no coordination requirements
- **Simple sequential work** that doesn't need stage management
- **Trivial operations** completing in <5 minutes
- **Pure research** without implementation stages

### Success Criteria
- [assert|neutral] *All stages complete** with 100% success rate [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] *Dependency resolution** with no circular dependencies [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] *Model routing optimal** for each stage (Gemini/Codex/Claude) [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] *Memory persistence** maintained across all stages [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] *No orphaned stages** - all stages tracked and completed [ground:acceptance-criteria] [conf:0.90] [state:provisional]

### Edge Cases to Handle
- **Stage failure mid-cascade** - Implement retry with exponential backoff
- **Circular dependencies** - Validate DAG structure before execution
- **Model unavailability** - Have fallback model selection per stage
- **Memory overflow** - Implement stage result compression
- **Timeout on long stages** - Configure per-stage timeout limits

### Guardrails (NEVER Violate)
- [assert|emphatic] NEVER: lose stage state** - Persist after each stage completion [ground:policy] [conf:0.98] [state:confirmed]
- [assert|neutral] ALWAYS: validate dependencies** - Check DAG acyclic before execution [ground:policy] [conf:0.98] [state:confirmed]
- [assert|neutral] ALWAYS: track cascade progress** - Update memory with real-time status [ground:policy] [conf:0.98] [state:confirmed]
- [assert|emphatic] NEVER: skip error handling** - Every stage needs try/catch with fallback [ground:policy] [conf:0.98] [state:confirmed]
- [assert|neutral] ALWAYS: cleanup on failure** - Release resources, clear temp state [ground:policy] [conf:0.98] [state:confirmed]

### Evidence-Based Validation
- **Verify stage outputs** - Check actual results vs expected schema
- **Validate data flow** - Confirm outputs passed correctly to next stage
- **Check model routing** - Verify correct AI used per stage requirements
- **Measure cascade performance** - Track execution time vs estimates
- **Audit memory usage** - Ensure no memory leaks across stages


# Slash Command Encoder (Enhanced)

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



## Overview
Creates fast, scriptable `/command` interfaces for micro-skills, cascades, and agents. This enhanced version includes automatic skill discovery, intelligent command generation, parameter validation, multi-model routing, and command chaining patterns.

## Philosophy: Expert Efficiency

**Command Line UX for AI**: Expert users benefit from fast, precise, scriptable interfaces over natural language when performing repeated operations.

**Enhanced Capabilities**:
- **Auto-Discovery**: Scans and catalogs all installed skills automatically
- **Intelligent Routing**: Commands invoke optimal AI/agent for task
- **Parameter Validation**: Type-checked, auto-completed parameters
- **Command Chaining**: Compose commands into pipelines
- **Multi-Model Integration**: Direct access to Gemini/Codex via commands

**Key Principles**:
1. Fast and unambiguous invocation
2. Self-documenting through naming
3. Composable and scriptable
4. Type-safe parameter handling
5. Muscle memory for power users

## When to Create Slash Commands

✅ **Per

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
  pattern: "skills/orchestration/slash-command-encoder/{project}/{timestamp}",
  store: ["executions", "decisions", "patterns"],
  retrieve: ["similar_tasks", "proven_patterns"]
} [ground:system-policy] [conf:1.0] [state:confirmed]

[define|neutral] MEMORY_TAGGING := {
  WHO: "slash-command-encoder-{session_id}",
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

[commit|confident] <promise>SLASH_COMMAND_ENCODER_VERILINGUA_VERIX_COMPLIANT</promise> [ground:self-validation] [conf:0.99] [state:confirmed]
