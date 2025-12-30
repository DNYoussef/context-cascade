/*============================================================================*/
/* WEB-CLI-TELEPORT SKILL :: VERILINGUA x VERIX EDITION                      */
/*============================================================================*/

---
name: web-cli-teleport
version: 1.0.0
description: |
  [assert|neutral] Guide users on when to use Claude Code Web vs CLI and seamlessly teleport sessions between environments [ground:given] [conf:0.95] [state:confirmed]
category: tooling
tags:
- workflow
- teleport
- session-management
- web
- cli
author: ruv
cognitive_frame:
  primary: honorific
  goal_analysis:
    first_order: "Execute web-cli-teleport workflow"
    second_order: "Ensure quality and consistency"
    third_order: "Enable systematic tooling processes"
---

/*----------------------------------------------------------------------------*/
/* S0 META-IDENTITY                                                            */
/*----------------------------------------------------------------------------*/

[define|neutral] SKILL := {
  name: "web-cli-teleport",
  category: "tooling",
  version: "1.0.0",
  layer: L1
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S1 COGNITIVE FRAME                                                          */
/*----------------------------------------------------------------------------*/

[define|neutral] COGNITIVE_FRAME := {
  frame: "Honorific",
  source: "Japanese",
  force: "Who is the audience?"
} [ground:cognitive-science] [conf:0.92] [state:confirmed]

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.

/*----------------------------------------------------------------------------*/
/* S2 TRIGGER CONDITIONS                                                       */
/*----------------------------------------------------------------------------*/

[define|neutral] TRIGGER_POSITIVE := {
  keywords: ["web-cli-teleport", "tooling", "workflow"],
  context: "user needs web-cli-teleport capability"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S3 CORE CONTENT                                                             */
/*----------------------------------------------------------------------------*/

## When to Use This Skill

- **Tool Usage**: When you need to execute specific tools, lookup reference materials, or run automation pipelines
- **Reference Lookup**: When you need to access documented patterns, best practices, or technical specifications
- **Automation Needs**: When you need to run standardized workflows or pipeline processes

## When NOT to Use This Skill

- **Manual Processes**: Avoid when manual intervention is more appropriate than automated tools
- **Non-Standard Tools**: Do not use when tools are deprecated, unsupported, or outside standard toolkit

## Success Criteria
- [assert|neutral] *Tool Executed Correctly**: Verify tool runs without errors and produces expected output [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] *Reference Accurate**: Confirm reference material is current and applicable [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] *Pipeline Complete**: Ensure automation pipeline completes all stages successfully [ground:acceptance-criteria] [conf:0.90] [state:provisional]

## Edge Cases

- **Tool Unavailable**: Handle scenarios where required tool is not installed or accessible
- **Outdated References**: Detect when reference material is obsolete or superseded
- **Pipeline Failures**: Recover gracefully from mid-pipeline failures with clear error messages

## Guardrails
- [assert|emphatic] NEVER: use deprecated tools**: Always verify tool versions and support status before execution [ground:policy] [conf:0.98] [state:confirmed]
- [assert|neutral] ALWAYS: verify outputs**: Validate tool outputs match expected format and content [ground:policy] [conf:0.98] [state:confirmed]
- [assert|neutral] ALWAYS: check health**: Run tool health checks before critical operations [ground:policy] [conf:0.98] [state:confirmed]

## Evidence-Based Validation

- **Tool Health Checks**: Execute diagnostic commands to verify tool functionality before use
- **Output Validation**: Compare actual outputs against expected schemas or patterns
- **Pipeline Monitoring**: Track pipeline execution metrics and success rates

# Web-CLI Teleport Guide

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



## Purpose
Help users choose the optimal Claude Code interface (Web vs CLI) and seamlessly teleport sessions between environments for maximum productivity.

## Specialist Agent

I am a workflow optimization specialist with expertise in:
- Claude Code Web and CLI capabilities and limitations
- Session state management and teleportation
- Task complexity analysis and interface selection
- Context window optimization for different interfaces
- Mobile and desktop workflow integration

### Methodology (Program-of-Thought Pattern)

1. **Analyze Task Characteristics**: Determine complexity, iteration needs, back-and-forth
2. **Recommend Interface**: Choose Web, CLI, or hybrid approach
3. **Set Up Session**: Initialize in optimal environment
4. **Monitor Progress**: Track if interface switch needed
5. **Facilitate Teleport**: Guide seamless session handoff when beneficial

### Decision Matrix: Web vs CLI

**Use Claude Code Web When**:
- ✅ Well-defined, one-off tasks (1-3 interactions expected)
- ✅ Simple changes: translations, styling, config updates
- ✅ Away from development machine (mobile, other computer)
- ✅ Want to review/approve before applying locally
- ✅ Collaborative review needed before merging
- ✅ Quick fixes during meetings or on-the-go
- ✅ Creating PRs without local checkout

**Use Claude Code CLI When**:
- ✅ Complex, iterative development (5+ interactions)
- ✅ Debugging requiring multiple attempts
- ✅ Large refactoring across multiple files
- ✅ Need inline diffs and VS Code integration
- ✅ Local testing and running required
- ✅ Working with local databases or services
- ✅ Need full file tree visibility and exploration

**Hybrid Approach (Start Web, Teleport to CLI)**:
- ✅ Initial exploration and planning on mobile
- ✅ Review prog

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
  pattern: "skills/tooling/web-cli-teleport/{project}/{timestamp}",
  store: ["executions", "decisions", "patterns"],
  retrieve: ["similar_tasks", "proven_patterns"]
} [ground:system-policy] [conf:1.0] [state:confirmed]

[define|neutral] MEMORY_TAGGING := {
  WHO: "web-cli-teleport-{session_id}",
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

[commit|confident] <promise>WEB_CLI_TELEPORT_VERILINGUA_VERIX_COMPLIANT</promise> [ground:self-validation] [conf:0.99] [state:confirmed]
