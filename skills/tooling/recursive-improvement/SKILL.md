/*============================================================================*/
/* SKILL SKILL :: VERILINGUA x VERIX EDITION                      */
/*============================================================================*/

---
name: SKILL
version: 1.0.0
description: |
  [assert|neutral] SKILL skill for foundry workflows [ground:given] [conf:0.95] [state:confirmed]
category: foundry
tags:
- general
author: system
cognitive_frame:
  primary: compositional
  goal_analysis:
    first_order: "Execute SKILL workflow"
    second_order: "Ensure quality and consistency"
    third_order: "Enable systematic foundry processes"
---

/*----------------------------------------------------------------------------*/
/* S0 META-IDENTITY                                                            */
/*----------------------------------------------------------------------------*/

[define|neutral] SKILL := {
  name: "SKILL",
  category: "foundry",
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
  keywords: ["SKILL", "foundry", "workflow"],
  context: "user needs SKILL capability"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S3 CORE CONTENT                                                             */
/*----------------------------------------------------------------------------*/

# Recursive Improvement - Meta-Loop Skill

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



---
name: recursive-improvement
description: Self-improving meta-loop that audits and enhances skills, prompts, and expertise files
category: foundry
version: 2.0.0
triggers:
  - "improve skill"
  - "audit skill"
  - "run improvement cycle"
  - "meta-loop"
  - "self-improve"
mcp_servers:
  required: [memory-mcp]
  optional: [connascence-analyzer]
---

## Trigger Keywords

**USE WHEN user mentions:**
- "improve skill", "audit skill", "enhance skill", "optimize skill"
- "run improvement cycle", "meta-loop", "self-improve"
- "skill quality check", "documentation audit"
- "recursive improvement", "systematic improvement"
- "batch improve skills", "improve all skills"
- "skill missing [section]", "incomplete documentation"

**DO NOT USE when:**
- User wants to CREATE a new skill - use skill-creator-agent or micro-skill-creator
- User wants to CREATE an agent - use agent-creator
- User wants to improve a PROMPT (not skill) - use prompt-architect
- User wants one-off manual fix - direct editing faster
- Eval-harness benchmarks failing - fix root cause first, not improve on broken baseline
- During active feature development - finish feature, then improve

**Instead use:**
- skill-creator-agent when creating new skills from scratch
- agent-creator when creating new agents
- prompt-architect when optimizing prompts
- skill-forge when applying specific improvements (recursive-improvement coordinates it)


## Overview

The Recursive Improvement skill orchestrates the meta-loop that enables the system to improve itself. It coordinates four specialized auditors (skill-auditor, prompt-auditor, expertise-auditor, output-auditor) to detect issues, generate improvement proposals, apply changes via skill-forge, and validate results through the frozen eval-harness.

**Key Constraint**: The eval-harness is FROZEN - it never self-improves. This prevents Goodhart's Law (optimizing the metric instead of the goal).

## When to Use

**Use When**:
- Skill documentation is incomplete (missing Core Principles, Anti-Patterns, Conclusion)
- Prompt quality has degraded (inconsistent outputs, missing constraints)
- Expertise files are outdated (file locations changed, patterns stale)
- Output quality has dropped (theater code, unvalidated claims)

**Do Not Use**:
- For one-off fixes (use direct editing)
- When eval-harness benchmarks are failing (fix root cause first)
- During active feature development (finish feature first)

## Core Principles

Recursive Improvement operates on 3 fundamental principles:

### Principle 1: Frozen Eval Harness Prevents Goodhart's Law
The evaluation harness that gates all improvements is NEVER self-improved. This ensures the system optimizes for genuine quality, not for passing corrupted benchmarks.

In practice:
- Eval-harness benchmarks are defined externally and versioned separately
- Changes to eval-harness require human approval and audit trail
- All improvement proposals are tested against frozen benchmarks before commit

### Principle 2: Propose-Test-Compare-Commit Pipeline
Every improvement follows a rigorous pipeline: propose changes, test against benchmarks, compare to baseline, commit only if better. No direct edits bypass this pipeline.

In practice:
- Auditors generate structured proposals with predicted improvement deltas
- skill-forge applies proposals in sandbox before production
- A/B comparison ensures new version outperforms baseline
- Rollback available for 30 days if regressions discovered later

### Principle 3: Documentation Completeness Is Non-Negotiable
Skills are not production-ready until they pass documentation audit (100% Tier 1, 100% Tier 2). Missing sections are auto-generated using templates from SKILL-AUDIT-PROTOCOL.md.

In practice:
- Every skill audit checks for Core Principles, Anti-Patterns, Conclusion
- Missing sections trigger auto-generation using domain-specific t

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
  pattern: "skills/foundry/SKILL/{project}/{timestamp}",
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
