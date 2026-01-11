/*============================================================================*/
/* LANDING-PAGE-GENERATOR SKILL :: VERILINGUA x VERIX EDITION                      */
/*============================================================================*/

---
name: landing-page-generator
version: 2.0.0
description: |
  [assert|neutral] Comprehensive 6-phase SOP for AI-driven landing page creation (Research -> Copy -> Inspiration -> Build -> Iterate -> Deploy). Use when building marketing pages, sales pages, or product landing pages. [ground:given] [conf:0.95] [state:confirmed]
category: delivery
tags:
- general
author: system
cognitive_frame:
  primary: evidential
  goal_analysis:
    first_order: "Execute landing-page-generator workflow"
    second_order: "Ensure quality and consistency"
    third_order: "Enable systematic delivery processes"
---

/*----------------------------------------------------------------------------*/
/* S0 META-IDENTITY                                                            */
/*----------------------------------------------------------------------------*/

[define|neutral] SKILL := {
  name: "landing-page-generator",
  category: "delivery",
  version: "2.0.0",
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
  keywords: ["landing-page-generator", "delivery", "workflow"],
  context: "user needs landing-page-generator capability"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S3 CORE CONTENT                                                             */
/*----------------------------------------------------------------------------*/

# Landing Page Generator

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



A comprehensive 6-phase SOP for AI-driven landing page creation, from research to deployment. Converts product/service briefs into high-converting, deployable landing pages using evidence-based design patterns and conversion psychology.

## Overview

Landing Page Generator represents a systematic approach to creating landing pages that actually convert. Rather than generating generic templates, it employs a research-driven methodology that ensures every page is optimized for its specific audience, product, and conversion goal.

This skill draws inspiration from direct response marketing principles--understanding that a landing page is not just a website, but a carefully crafted argument that guides visitors toward a single action. The 6-phase workflow mirrors how professional conversion rate optimization (CRO) teams work: research the market, craft compelling copy, gather design inspiration, build with purpose, iterate based on feedback, and deploy with confidence.

**Key Innovation**: This skill combines:
- **Web research** for current best practices and conversion tactics
- **Structured copywriting** using proven frameworks (AIDA, PAS, FAB)
- **Design system extraction** via Firecrawl for brand consistency
- **Multi-model code generation** using highest-capability models
- **Context-aware iteration** to prevent quality degradation
- **Automated deployment** via Netlify CLI

The result is landing pages that don't just look good--they convert visitors into customers.

## Core Principles

Landing Page Generator operates on five fundamental principles that ensure every page achieves its conversion goal:

### Principle 1: Copy Before Design

The words on the page matter more than how it looks. A well-written page with mediocre design will outperform a beautiful page with weak copy. This is why Phase 2 (Copy) comes before Phase 3 (Inspiration) and Phase 4 (Build).

In practice:
- Always complete copy review before moving to design
- Never let design decisions compromise copy clarity
- Test copy with the "squint test"--if you squint, can you still understand the hierarchy?
- Headlines should stand alone as complete value propositions

### Principle 2: One Page, One Goal

Every landing page should have exactly one conversion goal. Multiple CTAs, competing messages, or confusing navigation kill conversions. The page exists to drive one specific action.

In practice:
- Define the single desired action before starting
- Remove anything that doesn't support that action
- Use the "newspaper test"--could someone scanning for 5 seconds understand what to do?
- Secondary CTAs (like "Learn More") should be visually subordinate

### Principle 3: Research-Driven, Not Assumption-Driven

What worked last year may not work today. Landing page best practices evolve constantly. Phase 1 (Research) ensures every page is built on current, evidence-based tactics rather than outdated assumptions.

In practice:
- Always emphasize "as of today's date" in research prompts
- Look for specific conversion rate data, not just design trends
- Research competitor landing pages for inspiration and differentiation
- Update the playbook regularly as tactics evolve

### Principle 4: Inspiration, Not Imitation

Extracting branding from inspiration sites creates consistency, not copycats. The goal is to capture design systems (colors, fonts, spacing) while maintaining unique value propositions and messaging.

In practice:
- Use Firecrawl for objective branding data, not subjective "feel"
- Screenshots capture layout patterns, not copy to replicate
- Adapt inspiration to your brand, don't adopt it wholesale
- Multiple inspiration sources prevent single-source bias

### Principle 5: Iterate in the Right Environment

AI context windows have limits. After 2-3 iterations, quality degrades as the context fills. Moving to dedicated coding environments (like Cursor) pre

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
  pattern: "skills/delivery/landing-page-generator/{project}/{timestamp}",
  store: ["executions", "decisions", "patterns"],
  retrieve: ["similar_tasks", "proven_patterns"]
} [ground:system-policy] [conf:1.0] [state:confirmed]

[define|neutral] MEMORY_TAGGING := {
  WHO: "landing-page-generator-{session_id}",
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

[commit|confident] <promise>LANDING_PAGE_GENERATOR_VERILINGUA_VERIX_COMPLIANT</promise> [ground:self-validation] [conf:0.99] [state:confirmed]
