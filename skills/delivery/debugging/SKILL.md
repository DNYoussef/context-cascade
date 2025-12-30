/*============================================================================*/
/* DEBUGGING SKILL :: VERILINGUA x VERIX EDITION                      */
/*============================================================================*/

---
name: debugging
version: 1.0.0
description: |
  [assert|neutral] Systematic debugging methodology using a 5-phase protocol. Use when troubleshooting code failures, investigating bugs, or analyzing unexpected behavior. Applies 10 proven debugging techniques includin [ground:given] [conf:0.95] [state:confirmed]
category: delivery
tags:
- delivery
- development
- workflow
author: ruv
cognitive_frame:
  primary: aspectual
  goal_analysis:
    first_order: "Execute debugging workflow"
    second_order: "Ensure quality and consistency"
    third_order: "Enable systematic delivery processes"
---

/*----------------------------------------------------------------------------*/
/* S0 META-IDENTITY                                                            */
/*----------------------------------------------------------------------------*/

[define|neutral] SKILL := {
  name: "debugging",
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
  keywords: ["debugging", "delivery", "workflow"],
  context: "user needs debugging capability"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S3 CORE CONTENT                                                             */
/*----------------------------------------------------------------------------*/

# Debugging - Systematic Code Investigation

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.




## When to Use This Skill

- **Production Incidents**: Critical bugs affecting live users requiring rapid diagnosis
- **Intermittent Failures**: Flaky tests, race conditions, or timing-dependent bugs
- **Performance Issues**: Slow endpoints, memory leaks, or CPU spikes
- **Integration Failures**: Third-party API errors, database connectivity issues
- **Regression Analysis**: New bugs introduced by recent changes
- **Complex Stack Traces**: Multi-layered errors spanning multiple services

## When NOT to Use This Skill

- **Feature Development**: Building new functionality (use feature-dev-complete instead)
- **Code Reviews**: Reviewing code quality or architecture (use code-review-assistant)
- **Refactoring**: Restructuring code without fixing bugs (use refactoring skills)
- **Known Issues**: Bugs with clear root cause already identified

## Success Criteria

- [ ] Root cause identified with supporting evidence
- [ ] Fix implemented and tested
- [ ] Regression test added to prevent recurrence
- [ ] All related test suites passing
- [ ] Fix validated in production-like environment
- [ ] Documentation updated with troubleshooting notes
- [ ] Monitoring/alerting adjusted if needed

## Edge Cases to Handle

- **Heisenbugs**: Bugs that disappear when debugger attached
- **Multi-Service Failures**: Cascading errors across microservices
- **Data Corruption**: State inconsistencies requiring rollback
- **Timezone Issues**: Date/time bugs across regions
- **Concurrency Bugs**: Race conditions, deadlocks, or thread safety
- **Memory Corruption**: Pointer errors, buffer overflows in native code

## Guardrails

- **NEVER** deploy debug code or verbose logging to production
- **ALWAYS** reproduce bugs locally before proposing fixes
- **NEVER** fix symptoms without understanding root cause
- **ALWAYS** add regression tests for fixed bugs
- **NEVER** disable tests to make CI pass
- **ALWAYS** verify fixes do not introduce new bugs
- **NEVER** modify production data without backup

## Evidence-Based Validation

- [ ] Bug reproduced consistently with minimal test case
- [ ] Stack traces analyzed with error tracking tools (Sentry, Rollbar)
- [ ] Performance profiled with appropriate tools (Chrome DevTools, py-spy)
- [ ] Fix verified with automated tests
- [ ] Integration tests passing
- [ ] No new errors in application logs
- [ ] Memory/CPU usage within normal bounds

Systematic debugging through proven methodologies and comprehensive error analysis.

## When to Use This Skill

Use when code fails or produces unexpected results, investigating intermittent bugs, analyzing production errors, or debugging complex race conditions and edge cases.

## 5-Phase Debugging Protocol

### Phase 1: Reproduce Reliably
- Create minimal test case that triggers the bug
- Document exact sequence of inputs/conditions
- Verify bug occurs consistently
- Strip away unnecessary complexity

### Phase 2: Understand Root Cause
- Trace execution path leading to failure
- Examine variable values and state
- Identify incorrect assumptions
- Understand what code should do vs. what it does

### Phase 3: Design the Fix
- Determine changes needed to eliminate bug
- Consider impact on other functionality
- Check for similar bugs elsewhere
- Plan testing strategy

### Phase 4: Implement Using Best Practices
- Write clear, readable code
- Add comprehensive comments
- Handle edge cases properly
- Validate assumptions

### Phase 5: Verify the Fix
- Confirm bug no longer occurs
- Run regression tests
- Test edge cases
- Validate under original conditions

## 10 Debugging Methodologies

1. **Binary Search Debugging** - Divide and conquer to isolate bug location
2. **Rubber Duck Debugging** - Explain code to surface blind spots
3. **Hypothesis-Driven** - Form and test explicit hypotheses
4. **Differential Debugging** - Compare working vs. broken code
5. **Logg

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
  pattern: "skills/delivery/debugging/{project}/{timestamp}",
  store: ["executions", "decisions", "patterns"],
  retrieve: ["similar_tasks", "proven_patterns"]
} [ground:system-policy] [conf:1.0] [state:confirmed]

[define|neutral] MEMORY_TAGGING := {
  WHO: "debugging-{session_id}",
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

[commit|confident] <promise>DEBUGGING_VERILINGUA_VERIX_COMPLIANT</promise> [ground:self-validation] [conf:0.99] [state:confirmed]
