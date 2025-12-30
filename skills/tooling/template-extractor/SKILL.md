/*============================================================================*/
/* TEMPLATE-EXTRACTOR SKILL :: VERILINGUA x VERIX EDITION                      */
/*============================================================================*/

---
name: template-extractor
version: 1.0.0
description: |
  [assert|neutral] Reverse-engineer document templates to extract exact design specifications and generate reusable AI prompts for pixel-perfect document recreation [ground:given] [conf:0.95] [state:confirmed]
category: tooling
tags:
- general
author: system
cognitive_frame:
  primary: honorific
  goal_analysis:
    first_order: "Execute template-extractor workflow"
    second_order: "Ensure quality and consistency"
    third_order: "Enable systematic tooling processes"
---

/*----------------------------------------------------------------------------*/
/* S0 META-IDENTITY                                                            */
/*----------------------------------------------------------------------------*/

[define|neutral] SKILL := {
  name: "template-extractor",
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
  keywords: ["template-extractor", "tooling", "workflow"],
  context: "user needs template-extractor capability"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S3 CORE CONTENT                                                             */
/*----------------------------------------------------------------------------*/

# Template Extractor

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



## Overview

Template Extractor is a systematic reverse-engineering tool that extracts precise design specifications from existing documents (DOCX, PPTX, XLSX, PDF) to enable pixel-perfect recreation. Unlike visual inspection which leads to "close enough" approximations, this skill unpacks document file structures and parses their underlying XML to extract exact font sizes, color hex codes, spacing values, and layout configurations.

The skill generates two critical outputs: (1) a code-level technical specification with exact measurements and values, and (2) an AI-ready prompt that enables any language model to recreate documents in that exact style. This dual-output approach ensures both machine precision and human comprehension.

By validating extracted templates through test recreation and visual comparison, Template Extractor guarantees that generated specifications are accurate and actionable, eliminating the guesswork and iteration cycles typical of manual document formatting.

## When to Use

**Use When**:
- User provides a sample document (DOCX, PPTX, XLSX, or PDF) and wants to replicate its formatting exactly
- User needs to create a reusable document style guide from an existing file without manual measurement
- User wants to generate an AI prompt that enables consistent document generation across multiple files
- User needs to standardize document formatting across a team by extracting a reference template
- User is migrating from one document system to another and needs precise format specifications
- User wants to create a branded document generator that matches corporate style guides
- User needs to audit existing documents to document their design specifications
- User wants to ensure document formatting consistency without manually measuring fonts and spacing

**Do Not Use**:
- User wants to create a document from scratch without a reference template (use doc-generator or pptx-generation instead)
- User only needs to convert document formats without preserving exact styling (use standard conversion tools)
- User wants to improve or modify existing formatting rather than replicate it exactly
- User is working with handwritten documents or non-digital formats (no structured data to extract)
- User needs real-time document editing rather than specification extraction
- User's priority is content extraction rather than format specification

## Core Principles

### Principle 1: Systematic Extraction Over Visual Guessing

Human visual inspection of documents leads to approximations: "that looks like 14pt" or "probably Arial". Template Extractor treats documents as ZIP archives containing structured XML, unpacking them to access authoritative sources like `styles.xml`, `theme1.xml`, and `document.xml`. This approach extracts definitive values rather than best guesses.

**Why This Matters**: A "close enough" color (#333333 vs #1F1F1F) creates subtle inconsistency that compounds across documents. A 1pt font size difference (11pt vs 12pt) changes readability and layout flow. Manual inspection cannot reliably detect these differences, but XML parsing provides ground truth.

**In Practice**:
- Unpack DOCX/PPTX/XLSX files as ZIP archives to access internal XML structure
- Parse `word/styles.xml` for exact heading and body text specifications
- Extract `word/theme/theme1.xml` for color scheme definitions (hex values, not visual approximations)
- Read `word/document.xml` for page layout settings (margins, orientation, dimensions)
- Convert OOXML units (half-points, twips, EMUs) to standard measurements using precise formulas
- Extract embedded media files (logos, images) from `word/media/` directories
- For PDFs, use metadata extraction and text analysis to identify fonts and spacing patterns

### Principle 2: Dual Output (Specification + Prompt)

Template Extractor generates two complementary artifacts: a technical specifi

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
  pattern: "skills/tooling/template-extractor/{project}/{timestamp}",
  store: ["executions", "decisions", "patterns"],
  retrieve: ["similar_tasks", "proven_patterns"]
} [ground:system-policy] [conf:1.0] [state:confirmed]

[define|neutral] MEMORY_TAGGING := {
  WHO: "template-extractor-{session_id}",
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

[commit|confident] <promise>TEMPLATE_EXTRACTOR_VERILINGUA_VERIX_COMPLIANT</promise> [ground:self-validation] [conf:0.99] [state:confirmed]
