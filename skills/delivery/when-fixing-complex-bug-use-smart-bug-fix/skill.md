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

# When Fixing Complex Bug Use Smart Bug Fix

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



---
name: when-fixing-complex-bug-use-smart-bug-fix
trigger: "when user reports complex bug, production issue, or requests systematic debugging"
description: "Intelligent bug fixing workflow combining root cause analysis, multi-model reasoning, automated testing, and validation to systematically fix bugs"
version: 2.0.0
author: Base Template Generator
category: debugging
tags:
  - bug-fix
  - debugging
  - root-cause-analysis
  - testing
  - validation
agents:
  - researcher (RCA specialist)
  - coder (fix implementer)
  - tester (validation specialist)
  - reviewer (quality assurance)
  - performance-analyzer
coordinator: hierarchical-coordinator
memory_patterns:
  - swarm/bug-fix/issue-report
  - swarm/bug-fix/rca-findings
  - swarm/bug-fix/fix-implementation
  - swarm/bug-fix/test-validation
  - swarm/bug-fix/verification
success_criteria:
  - Root cause identified and documented
  - Fix implemented without introducing regressions
  - All tests passing including new regression tests
  - Bug verified resolved in production-like environment
  - Documentation updated with fix details
---

## Assigned Agents

### Primary Agent
- **researcher (RCA specialist)** - Best match for root cause analysis (RCA). Expert in systematic bug investigation using 5 Whys technique, git blame analysis, debugging tools, and hypothesis formation. Leads initial issue analysis, reproduction, deep RCA (Phase 1-2), and final verification (Phase 7).

### Secondary Agents
- **coder (fix implementer)** - Phase 4: Implements bug fix addressing validated root cause with minimal code changes
- **tester (validation specialist)** - Phase 3 & 5: Hypothesis validation and comprehensive test suite execution
- **reviewer (quality assurance)** - Phase 6: Code review, security scan, performance impact analysis
- **performance-analyzer** - Phase 6: Performance monitoring and regression detection

### Fallback Agents
- **code-analyzer** - Alternative for code analysis if researcher needs support
- **production-validator** - Alternative for production verification if reviewer unavailable
- **backend-dev** - Alternative implementation if coder unavailable

### Coordination Pattern
**Pattern**: Hierarchical RCA Workflow (7 phases with validation loops)
**Topology**: Hierarchical coordination with hypothesis-driven development
**Memory Namespace**: `swarm/bug-fix/*` (issue-report, rca-findings, fix-implementation, test-validation, verification)

**Agent Collaboration**:
1. **RCA Investigation**: Researcher performs deep root cause analysis before any fix
2. **Hypothesis Validation**: Tester validates hypothesis before coder implements fix
3. **Feedback Loops**: If hypothesis fails → return to researcher; if tests fail → return to coder
4. **Byzantine Pattern**: Optional 6-validator consensus for critical bugs
5. **Production Verification**: Final researcher verification in production-like environment
6. **Post-Mortem**: Documentation and knowledge base updates

**Utilization**: Critical debugging skill using 5 specialized agents with validation gates. Ensures systematic bug resolution without regressions.

---

## Trigger Conditions

Use this skill when:
- User reports a complex bug requiring investigation
- Production issue needs systematic root cause analysis
- Intermittent bug that's hard to reproduce
- Bug affecting multiple components or services
- Critical issue requiring validated fix
- Bug with unclear root cause
- Need comprehensive testing before deployment

## Skill Overview

This skill provides systematic bug fixing through a 7-phase workflow: issue analysis, root cause analysis (RCA), hypothesis testing, fix implementation, comprehensive validation, regression testing, and verification. Multi-agent coordination ensures thorough investigation and safe resolution.

## 7-Phase Skill-Forge Methodology

### Phase 1: Issue Analysis & Repro

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
