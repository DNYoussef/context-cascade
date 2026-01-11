/*============================================================================*/
/* PAIR-PROGRAMMING SKILL :: VERILINGUA x VERIX EDITION                      */
/*============================================================================*/

---
name: pair-programming
version: 1.0.0
description: |
  [assert|neutral] AI-assisted pair programming with multiple modes (driver/navigator/switch), real-time verification, quality monitoring, and comprehensive testing. Supports TDD, debugging, refactoring, and learning se [ground:given] [conf:0.95] [state:confirmed]
category: delivery
tags:
- delivery
- development
- workflow
author: ruv
cognitive_frame:
  primary: evidential
  goal_analysis:
    first_order: "Execute pair-programming workflow"
    second_order: "Ensure quality and consistency"
    third_order: "Enable systematic delivery processes"
---

/*----------------------------------------------------------------------------*/
/* S0 META-IDENTITY                                                            */
/*----------------------------------------------------------------------------*/

[define|neutral] SKILL := {
  name: "pair-programming",
  category: "delivery",
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
  keywords: ["pair-programming", "delivery", "workflow"],
  context: "user needs pair-programming capability"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S3 CORE CONTENT                                                             */
/*----------------------------------------------------------------------------*/

# Pair Programming

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.




## When to Use This Skill

- **Learning Sessions**: Teaching or learning new technologies, patterns, or codebases
- **Complex Features**: Tackling features requiring deep collaboration
- **Debugging Sessions**: Pair debugging to solve difficult bugs faster
- **Code Reviews**: Real-time collaborative code review and refactoring
- **Knowledge Transfer**: Onboarding new team members or sharing expertise
- **TDD Sessions**: Test-driven development with navigator/driver roles

## When NOT to Use This Skill

- **Simple Tasks**: Trivial changes or routine maintenance
- **Independent Work**: Tasks requiring deep focus without interruption
- **Different Timezones**: Async code review more appropriate
- **Solo Learning**: Self-paced tutorials or experimentation

## Success Criteria

- [ ] Both participants understand the implementation
- [ ] Code meets team quality standards
- [ ] Tests written and passing
- [ ] Knowledge successfully shared
- [ ] Documentation updated if needed
- [ ] Both participants satisfied with collaboration
- [ ] No blockers remaining

## Edge Cases to Handle

- **Skill Imbalance**: Significant experience gap between pair members
- **Disagreement**: Conflicting approaches or opinions
- **Fatigue**: Long sessions reducing effectiveness
- **Tool Differences**: Different IDE preferences or setups
- **Communication Styles**: Different working or communication preferences
- **Remote Pairing**: Latency, screen sharing issues, or connectivity problems

## Guardrails

- **NEVER** dominate the keyboard without switching roles
- **ALWAYS** switch driver/navigator roles every 25-30 minutes
- **NEVER** criticize or dismiss partner ideas
- **ALWAYS** explain reasoning for technical decisions
- **NEVER** skip breaks - take 5-10 minute breaks hourly
- **ALWAYS** commit working code at session end
- **NEVER** pair for more than 4-5 hours continuously

## Evidence-Based Validation

- [ ] Code compiles and runs successfully
- [ ] All tests passing (unit, integration)
- [ ] Both participants can explain implementation
- [ ] Code reviewed against team style guide
- [ ] Git commits follow team conventions
- [ ] Documentation reflects changes
- [ ] Security considerations addressed

Collaborative AI pair programming with intelligent role management, real-time quality monitoring, and comprehensive development workflows.

## What This Skill Does

This skill provides professional pair programming capabilities with AI assistance, supporting multiple collaboration modes, continuous verification, and integrated testing. It manages driver/navigator roles, performs real-time code review, tracks quality metrics, and ensures high standards through truth-score verification.

**Key Capabilities:**
- **Multiple Modes**: Driver, Navigator, Switch, TDD, Review, Mentor, Debug
- **Real-Time Verification**: Automatic quality scoring with rollback on failures
- **Role Management**: Seamless switching between driver/navigator roles
- **Testing Integration**: Auto-generate tests, track coverage, continuous testing
- **Code Review**: Security scanning, performance analysis, best practice enforcement
- **Session Persistence**: Auto-save, recovery, export, and sharing

## Prerequisites

**Required:**
- Claude Flow CLI installed (`npm install -g claude-flow@alpha`)
- Git repository (optional but recommended)

**Recommended:**
- Testing framework (Jest, pytest, etc.)
- Linter configured (ESLint, pylint, etc.)
- Code formatter (Prettier, Black, etc.)

## Quick Start

### Basic Session
```bash
# Start simple pair programming
claude-flow pair --start
```

### TDD Session
```bash
# Test-driven development
claude-flow pair --start \
  --mode tdd \
  --test-first \
  --coverage 90
```

---

## Complete Guide

### Session Control Commands

#### Starting Sessions
```bash
# Basic start
claude-flow pair --start

# Expert refactoring session
claude-flow pair --start \
 

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
  pattern: "skills/delivery/pair-programming/{project}/{timestamp}",
  store: ["executions", "decisions", "patterns"],
  retrieve: ["similar_tasks", "proven_patterns"]
} [ground:system-policy] [conf:1.0] [state:confirmed]

[define|neutral] MEMORY_TAGGING := {
  WHO: "pair-programming-{session_id}",
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

[commit|confident] <promise>PAIR_PROGRAMMING_VERILINGUA_VERIX_COMPLIANT</promise> [ground:self-validation] [conf:0.99] [state:confirmed]
