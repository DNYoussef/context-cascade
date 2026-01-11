/*============================================================================*/
/* SKILL SKILL :: VERILINGUA x VERIX EDITION                      */
/*============================================================================*/

---
name: skill
version: 1.0.0
description: |
  [assert|neutral] skill skill for delivery workflows [ground:given] [conf:0.95] [state:confirmed]
category: delivery
tags:
- general
author: system
cognitive_frame:
  primary: aspectual
  goal_analysis:
    first_order: "Execute skill workflow"
    second_order: "Ensure quality and consistency"
    third_order: "Enable systematic delivery processes"
---

/*----------------------------------------------------------------------------*/
/* S0 META-IDENTITY                                                            */
/*----------------------------------------------------------------------------*/

[define|neutral] SKILL := {
  name: "skill",
  category: "delivery",
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
  keywords: ["skill", "delivery", "workflow"],
  context: "user needs skill capability"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S3 CORE CONTENT                                                             */
/*----------------------------------------------------------------------------*/

# When Collaborative Coding Use Pair Programming

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



---
name: when-collaborative-coding-use-pair-programming
trigger: "when user requests collaborative coding, real-time code review, or paired development session"
description: "AI-assisted pair programming with multiple modes (driver/navigator/switch), real-time verification, quality monitoring, and comprehensive testing support"
version: 2.0.0
author: Base Template Generator
category: development
tags:
  - pair-programming
  - collaborative
  - tdd
  - code-review
  - quality-assurance
agents:
  - coder (driver)
  - reviewer (navigator)
  - tester
  - performance-analyzer
coordinator: adaptive-coordinator
memory_patterns:
  - swarm/pair-programming/session-state
  - swarm/pair-programming/code-changes
  - swarm/pair-programming/review-feedback
  - swarm/pair-programming/test-results
  - swarm/pair-programming/metrics
success_criteria:
  - Code changes reviewed in real-time
  - All tests passing after each change
  - Code quality maintained above threshold
  - Performance metrics within acceptable range
  - No security vulnerabilities introduced
---

## Trigger Conditions

Use this skill when:
- User requests pair programming session
- Real-time collaborative coding needed
- Code review required during development
- TDD workflow with immediate feedback desired
- Learning/mentoring session for coding practices
- Debugging complex issues with second perspective
- Refactoring with continuous quality checks

## Skill Overview

This skill provides AI-assisted pair programming with three distinct modes: Driver/Navigator (traditional pairing), Switch Mode (role reversal), and TDD Mode (test-first development). Real-time quality monitoring, security scanning, and performance optimization ensure high-quality code output.

## 7-Phase Skill-Forge Methodology

### Phase 1: Session Initialization

**Objective**: Set up pair programming environment and establish session parameters

**Agent**: `coder` (session lead)

**Activities**:
- Initialize pair programming session
- Determine programming mode (driver/navigator/switch/tdd)
- Set up shared workspace and memory
- Configure quality thresholds and monitoring
- Establish coding standards and conventions
- Define session goals and success criteria

**Memory Keys**:
- `swarm/pair-programming/session-state/mode`
- `swarm/pair-programming/session-state/goals`
- `swarm/pair-programming/session-state/standards`
- `swarm/pair-programming/session-state/thresholds`

**Script**:
```bash
npx claude-flow@alpha hooks pre-task --description "Pair programming session init"
npx claude-flow@alpha hooks session-restore --session-id "pair-prog-${SESSION_ID}"
# Initialize session
npx claude-flow@alpha memory store "swarm/pair-programming/session-state/mode" "$SELECTED_MODE"
npx claude-flow@alpha memory store "swarm/pair-programming/session-state/goals" "$SESSION_GOALS"
npx claude-flow@alpha hooks notify --message "Pair programming session started: $SELECTED_MODE mode"
```

### Phase 2: Driver Mode (Code Implementation)

**Objective**: Write code with real-time navigator feedback

**Agent**: `coder` (driver)

**Activities**:
- Implement code changes based on task requirements
- Explain approach and reasoning to navigator
- Write code incrementally with frequent commits
- Respond to navigator feedback and suggestions
- Store code changes in memory for review

**Memory Keys**:
- `swarm/pair-programming/code-changes/current-file`
- `swarm/pair-programming/code-changes/diff`
- `swarm/pair-programming/code-changes/explanation`
- `swarm/pair-programming/code-changes/timestamp`

**Script**:
```bash
npx claude-flow@alpha hooks pre-task --description "Driver: implementing ${FEATURE}"
STANDARDS=$(npx claude-flow@alpha memory retrieve "swarm/pair-programming/session-state/standards")
# Write code
npx claude-flow@alpha hooks post-edit --file "$FILE_PATH" --memory-key "swarm/pair-programming/code

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
  pattern: "skills/delivery/skill/{project}/{timestamp}",
  store: ["executions", "decisions", "patterns"],
  retrieve: ["similar_tasks", "proven_patterns"]
} [ground:system-policy] [conf:1.0] [state:confirmed]

[define|neutral] MEMORY_TAGGING := {
  WHO: "skill-{session_id}",
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
