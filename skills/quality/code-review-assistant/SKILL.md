/*============================================================================*/
/* CODE-REVIEW-ASSISTANT SKILL :: VERILINGUA x VERIX EDITION                      */
/*============================================================================*/

---
name: code-review-assistant
version: 1.1.0
description: |
  [assert|neutral] Comprehensive PR review using multi-agent swarm with specialized reviewers for security, performance, style, tests, and documentation. Provides detailed feedback with auto-fix suggestions and merge re [ground:given] [conf:0.95] [state:confirmed]
category: quality
tags:
- review
- pr
- github
- swarm
- essential
author: ruv
cognitive_frame:
  primary: evidential
  goal_analysis:
    first_order: "Execute code-review-assistant workflow"
    second_order: "Ensure quality and consistency"
    third_order: "Enable systematic quality processes"
---

/*----------------------------------------------------------------------------*/
/* S0 META-IDENTITY                                                            */
/*----------------------------------------------------------------------------*/

[define|neutral] SKILL := {
  name: "code-review-assistant",
  category: "quality",
  version: "1.1.0",
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
  keywords: ["code-review-assistant", "quality", "workflow"],
  context: "user needs code-review-assistant capability"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S3 CORE CONTENT                                                             */
/*----------------------------------------------------------------------------*/

## Kanitsal Kod Incelemesi (Evidential Code Review)

Her bulgu icin kaynak belirtilmeli:
- **DOGRUDAN**: Kod satirinda goruldu [file:line]
- **STIL_KURALI**: Style guide referansi [rule_id]
- **EN_IYI_PRATIK**: Best practice citation [reference]

Every review comment MUST cite:
1. **Code location**: [file:line] with surrounding context
2. **Evidence type**: DIRECT (seen in code), STYLE_RULE (documented standard), BEST_PRACTICE (industry reference)
3. **Reference source**: Style guide section, security advisory, performance benchmark

## Keigo Wakugumi (Hierarchical Organization)

Rejisutaa Shurui (Severity Levels):
- **SONKEIGO (CRITICAL)**: Architecture-level issues (security vulnerabilities, data loss risks)
- **TEINEIGO (MAJOR)**: Module-level issues (performance bottlenecks, maintainability problems)
- **CASUAL (MINOR)**: Function-level improvements (code style, readability)
- **NIT**: Line-level suggestions (formatting, naming)

Review findings are organized hierarchically:
1. System-level concerns (architecture, security, data integrity)
2. Component-level issues (modules, services, APIs)
3. Implementation details (functions, algorithms)
4. Surface-level polish (style, naming, comments)

## When to Use This Skill

Use this skill when:
- Code quality issues are detected (violations, smells, anti-patterns)
- Audit requirements mandate systematic review (compliance, release gates)
- Review needs arise (pre-merge, production hardening, refactoring preparation)
- Quality metrics indicate degradation (test coverage drop, complexity increase)
- Theater detection is needed (mock data, stubs, incomplete implementations)

## When NOT to Use This Skill

Do NOT use this skill for:
- Simple formatting fixes (use linter/prettier directly)
- Non-code files (documentation, configuration without logic)
- Trivial changes (typo fixes, comment updates)
- Generated code (build artifacts, vendor dependencies)
- Third-party libraries (focus on application code)

## Success Criteria
- [assert|neutral] This skill succeeds when: [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] *Violations Detected**: All quality issues found with ZERO false negatives [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] *False Positive Rate**: <5% (95%+ findings are genuine issues) [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] *Actionable Feedback**: Every finding includes file path, line number, and fix guidance [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] *Root Cause Identified**: Issues traced to underlying causes, not just symptoms [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] *Fix Verification**: Proposed fixes validated against codebase constraints [ground:acceptance-criteria] [conf:0.90] [state:provisional]

## Edge Cases and Limitations

Handle these edge cases carefully:
- **Empty Files**: May trigger false positives - verify intent (stub vs intentional)
- **Generated Code**: Skip or flag as low priority (auto-generated files)
- **Third-Party Libraries**: Exclude from analysis (vendor/, node_modules/)
- **Domain-Specific Patterns**: What looks like violation may be intentional (DSLs)
- **Legacy Code**: Balance ideal standards with pragmatic technical debt management

## Quality Analysis Guardrails

CRITICAL RULES - ALWAYS FOLLOW:
- **NEVER approve code without evidence**: Require actual execution, not assumptions
- **ALWAYS provide line numbers**: Every finding MUST include file:line reference
- **VALIDATE findings against multiple perspectives**: Cross-check with complementary tools
- **DISTINGUISH symptoms from root causes**: Report underlying issues, not just manifestations
- **AVOID false confidence**: Flag uncertain findings as "needs manual review"
- **PRESERVE context**: Show surrounding code (5 lines before/after minimum)
- **TRACK false positives**: Learn from mistakes to improve detectio

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
  pattern: "skills/quality/code-review-assistant/{project}/{timestamp}",
  store: ["executions", "decisions", "patterns"],
  retrieve: ["similar_tasks", "proven_patterns"]
} [ground:system-policy] [conf:1.0] [state:confirmed]

[define|neutral] MEMORY_TAGGING := {
  WHO: "code-review-assistant-{session_id}",
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

[commit|confident] <promise>CODE_REVIEW_ASSISTANT_VERILINGUA_VERIX_COMPLIANT</promise> [ground:self-validation] [conf:0.99] [state:confirmed]
