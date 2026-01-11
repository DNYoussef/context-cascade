/*============================================================================*/
/* PPTX-GENERATION SKILL :: VERILINGUA x VERIX EDITION                      */
/*============================================================================*/

---
name: pptx-generation
version: 1.0.0
description: |
  [assert|neutral] Enterprise-grade PowerPoint deck generation system using evidence-based prompting techniques, workflow enforcement, and constraint-based design. Use when creating professional presentations (board dec [ground:given] [conf:0.95] [state:confirmed]
category: tooling
tags:
- general
author: ruv
cognitive_frame:
  primary: aspectual
  goal_analysis:
    first_order: "Execute pptx-generation workflow"
    second_order: "Ensure quality and consistency"
    third_order: "Enable systematic tooling processes"
---

/*----------------------------------------------------------------------------*/
/* S0 META-IDENTITY                                                            */
/*----------------------------------------------------------------------------*/

[define|neutral] SKILL := {
  name: "pptx-generation",
  category: "tooling",
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
  keywords: ["pptx-generation", "tooling", "workflow"],
  context: "user needs pptx-generation capability"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S3 CORE CONTENT                                                             */
/*----------------------------------------------------------------------------*/

# PowerPoint Generation Skill

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



## Overview

This skill implements a systematic framework for generating professional-quality PowerPoint presentations using AI. It addresses the unique challenges of PowerPoint as a medium that combines data analysis, narrative structure, visual design, and spatial layout—making it one of the most complex AI generation tasks in corporate knowledge work.

The skill applies evidence-based prompting techniques (plan-and-solve, program-of-thought, self-consistency), structural optimization principles (workflow enforcement, constraint-based design, validation gates), and proven spatial layout patterns to ensure consistent, high-quality outputs.

## Core Principles

### 1. Workflow Enforcement

AI systems exhibit tool degradation—silently switching to suboptimal alternatives when primary tools encounter difficulties. For spatial/visual tasks, this creates unreliable outputs.

**Implementation**: Explicitly specify the html2pptx technical workflow and prohibit alternative approaches. Require documentation review before execution.

**Rationale**: PowerPoint generation requires precise spatial calculations. The html2pptx skill provides reliable pixel-level control. Preventing tool switching eliminates the primary source of layout inconsistencies.

### 2. Constraint-Based Design Over Decorative Specification

Simple visual rules scale reliably; complex decorative elements create brittleness in AI generation.

**Implementation**: Define what NOT to do (negative constraints) before specifying positive behaviors. Prohibit border boxes, outline shapes, and rounded rectangles. Emphasize spacing, typography, and subtle color blocks.

**Rationale**: Visual design has exponentially more failure modes than success modes. Eliminating known problematic patterns focuses generative capacity within reliable boundaries. Clean design enables AI to prioritize content synthesis over visual parsing.

### 3. Pre-Execution Design Planning

Separating planning from execution prevents premature commitment to suboptimal visual approaches.

**Implementation**: Require written design plan specifying layout approach, color palette, typography hierarchy, and visual emphasis strategy before code generation.

**Rationale**: Mimics human design process. Creates audit trail for review. Establishes coherent visual system before implementation begins. Dramatically improves consistency across multi-slide decks.

### 4. Quantified Visual Specifications

Vague instructions ("clean margins") force the AI to guess intent. Precise specifications eliminate ambiguity.

**Implementation**: Convert qualitative requirements to measurable parameters (contrast ratios, font sizes, margin measurements, element counts).

**Rationale**: Spatial relationships are inherently quantitative. Explicit measurements create reproducible results and enable automated validation.

### 5. Multi-Chat Architecture for Complex Decks

Visual elements consume tokens faster than text or data. Single-context generation becomes unreliable beyond ~15 slides.

**Implementation**: Separate architect (narrative structure), generator (slide production), and assembly (consistency validation) into distinct conversations for 30+ slide decks.

**Rationale**: Manages context window limitations. Allows focused expertise in each phase. Enables section-level iteration without full deck regeneration.

## When to Use This Skill

**Primary Use Cases**:
- Board decks and executive presentations requiring professional polish
- Financial reports integrating data from multiple sources
- Strategic analyses combining quantitative and qualitative content
- Project updates demanding consistent visual language
- Any presentation where visual quality impacts stakeholder perception

**Skill Triggers**:
- User requests "create a presentation," "make slides," "build a deck"
- User asks to "analyze [data] and present finding

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
  pattern: "skills/tooling/pptx-generation/{project}/{timestamp}",
  store: ["executions", "decisions", "patterns"],
  retrieve: ["similar_tasks", "proven_patterns"]
} [ground:system-policy] [conf:1.0] [state:confirmed]

[define|neutral] MEMORY_TAGGING := {
  WHO: "pptx-generation-{session_id}",
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

[commit|confident] <promise>PPTX_GENERATION_VERILINGUA_VERIX_COMPLIANT</promise> [ground:self-validation] [conf:0.99] [state:confirmed]
