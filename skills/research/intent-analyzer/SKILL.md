/*============================================================================*/
/* SKILL SKILL :: VERILINGUA x VERIX EDITION                      */
/*============================================================================*/

---
name: SKILL
version: 1.0.0
description: |
  [assert|neutral] SKILL skill for research workflows [ground:given] [conf:0.95] [state:confirmed]
category: research
tags:
- general
author: system
cognitive_frame:
  primary: evidential
  goal_analysis:
    first_order: "Execute SKILL workflow"
    second_order: "Ensure quality and consistency"
    third_order: "Enable systematic research processes"
---

/*----------------------------------------------------------------------------*/
/* S0 META-IDENTITY                                                            */
/*----------------------------------------------------------------------------*/

[define|neutral] SKILL := {
  name: "SKILL",
  category: "research",
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
  keywords: ["SKILL", "research", "workflow"],
  context: "user needs SKILL capability"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S3 CORE CONTENT                                                             */
/*----------------------------------------------------------------------------*/

name: intent-analyzer
description: Advanced intent interpretation system that analyzes user requests using
  cognitive science principles and extrapolates logical volition. Use when user requests
  are ambiguous, when deeper understanding would improve response quality, or when
  helping users clarify what they truly need. Applies probabilistic intent mapping,
  first principles decomposition, and Socratic clarification to transform vague requests
  into well-understood goals.
version: 1.0.0
category: research
tags:
- research
- analysis
- planning
author: ruv
---

# Intent Analyzer

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



An advanced system for deeply understanding user intent by going beyond surface-level requests to discover underlying goals, unstated constraints, and true needs.

## Overview

Intent Analyzer represents a sophisticated approach to understanding what users really want. Rather than taking requests at face value, it employs cognitive science principles to examine underlying intent, identify implicit assumptions, recognize unstated constraints, and help users articulate their true goals clearly.

This skill draws inspiration from coherent extrapolated volition in AI alignment theory—determining what someone would want if they "knew more, thought faster, and were more the person they wished they were." Applied practically, this means understanding not just what the user explicitly requested, but what they would have requested with complete knowledge of possibilities, perfect clarity about their goals, and full awareness of relevant constraints.

## When to Use This Skill

Apply Intent Analyzer when:
- User requests are ambiguous or could be interpreted multiple ways
- Deeper understanding of goals would significantly improve response quality
- The stated request might be a proxy for an unstated underlying need
- Critical information appears to be missing or assumed
- Multiple reasonable interpretations exist and choosing wrong would waste effort
- Helping users clarify complex or poorly-defined problems
- Teaching or mentoring where understanding motivation improves guidance

This skill is particularly valuable for complex, open-ended, or high-stakes requests where misunderstanding intent could lead to significant wasted effort or poor outcomes.

## Core Principles

Intent Analyzer operates on five fundamental principles:

### First Principles Decomposition

Break down every request to its most fundamental goals. Question surface-level assumptions about what is being asked. Often, the stated request is a proxy for a deeper underlying need.

For example:
- "Summarize this document" might actually mean: seeking specific information within it, preparing for a meeting, evaluating whether to read it fully, or extracting key decisions
- "Help me write code" might actually mean: learning programming concepts, completing a specific project, debugging existing code, or understanding best practices

Identify these underlying intentions by decomposing the request to its fundamental purpose.

### Probabilistic Intent Mapping

Every user message carries multiple possible interpretations with varying probabilities. Construct a probability distribution over potential intents considering:
- Context clues in the phrasing
- Domain patterns and common use cases
- Explicit and implicit information provided
- What's left unsaid or assumed

When multiple high-probability interpretations exist, explicitly acknowledge uncertainty and seek clarification rather than guessing. When one interpretation is clearly dominant (>80% confidence), proceed while remaining open to correction.

### Evidence-Based Pattern Recognition

Recognize which category of request this represents based on established taxonomies:
- Creative task (writing, design, ideation)
- Analytical task (evaluation, comparison, assessment)
- Technical task (coding, configuration, troubleshooting)
- Learning query (explanation, teachin

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
  pattern: "skills/research/SKILL/{project}/{timestamp}",
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
