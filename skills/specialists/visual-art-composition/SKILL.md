/*============================================================================*/
/* VISUAL-ART-COMPOSITION SKILL :: VERILINGUA x VERIX EDITION                      */
/*============================================================================*/

---
name: visual-art-composition
version: 1.0.0
description: |
  [assert|neutral] Orthogonal framework for generating image prompts using 13 independently combinable aesthetic dimensions from 29+ cultural and theoretical art traditions [ground:given] [conf:0.95] [state:confirmed]
category: specialists
tags:
- general
author: system
cognitive_frame:
  primary: honorific
  goal_analysis:
    first_order: "Execute visual-art-composition workflow"
    second_order: "Ensure quality and consistency"
    third_order: "Enable systematic specialists processes"
---

/*----------------------------------------------------------------------------*/
/* S0 META-IDENTITY                                                            */
/*----------------------------------------------------------------------------*/

[define|neutral] SKILL := {
  name: "visual-art-composition",
  category: "specialists",
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
  keywords: ["visual-art-composition", "specialists", "workflow"],
  context: "user needs visual-art-composition capability"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S3 CORE CONTENT                                                             */
/*----------------------------------------------------------------------------*/

# Visual Art Composition System

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



## Overview

The Visual Art Composition System transforms "describe what you want to see" into structured, orthogonal aesthetic frameworks that combine multiple cultural art traditions in novel ways. Rather than treating art styles as monolithic presets ("make it look Japanese"), this system decomposes 29+ art traditions into 13 independently variable dimensions - each representing a distinct cognitive question that artists ask when creating work.

This approach enables unprecedented creative combinations: Byzantine spatial logic with Futurist motion, Yoruba emotional composure with Expressionist color, Japanese negative space with Islamic geometric patterns. The framework is built on the insight that art traditions are decision-making systems, not just visual styles. When you understand the questions each tradition asks (Where does form sit in space? How does color express emotion? What is deliberately absent?), you can recombine these cognitive frameworks to generate genuinely novel aesthetic experiences.

The system works by providing 13 orthogonal dimensions (spatial representation, color philosophy, emotional register, value structure, completion philosophy, etc.) with 4-8 values per dimension drawn from specific art traditions. Because dimensions are independent, any value from one dimension can combine with any value from another - creating thousands of possible aesthetic combinations. The system includes validation rules to prevent mutually exclusive combinations and resolution strategies for productive tensions that generate creative innovation.

## When to Use

**Use When**:
- Generating image prompts for AI image/video generation (Midjourney, DALL-E, Sora, Runway, Veo)
- Creating art direction briefs that specify precise aesthetic intent beyond "style references"
- Exploring cross-cultural aesthetic synthesis (e.g., Byzantine structure meets modern content)
- Designing visual systems with intentional productive tensions (motion within stillness, perfect forms with noble imperfection)
- Articulating why certain visual approaches feel derivative and seeking genuine novelty

**Do Not Use**:
- When simple style references suffice ("make it look like Monet")
- For technical specifications without aesthetic intent (color values, aspect ratios, file formats)
- When client/stakeholder cannot engage with conceptual frameworks (needs concrete mockups instead)

## Core Principles

### Principle 1: Orthogonal Dimensions Enable Novel Combinations

Each of the 13 dimensions represents an independent cognitive question. Changing one dimension does not require changing others. This independence means you can combine Byzantine reverse perspective with Futurist motion fragmentation, or Japanese ma emptiness with Victorian horror vacui (if you resolve the productive tension).

Orthogonality eliminates the constraint of historical coherence - you are not bound to "styles" as packages. Instead, you select decision-making frameworks from different traditions and layer them. A composition can ask the spatial question like a Renaissance artist, the color question like a Chinese painter, and the emotional question like a Yoruba sculptor.

In practice:
- Select values across dimensions without worrying about historical compatibility
- Combine opposing values deliberately to create productive tensions
- Validate only for logical contradictions (mutually exclusive pairs), not historical accuracy
- Use cross-cultural synthesis as the default, not the exception

### Principle 2: Cognitive Questions Over Visual Styles

Each art tradition embodies a set of cognitive questions artists ask while creating. Byzantine iconography asks "How does sacred space reach toward the viewer?" (reverse perspective). Chinese painting asks "Does this have spirit resonance?" (qi yun). Yoruba sculpture asks "Does this embody cool composure?" (itutu).

Wh

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
  pattern: "skills/specialists/visual-art-composition/{project}/{timestamp}",
  store: ["executions", "decisions", "patterns"],
  retrieve: ["similar_tasks", "proven_patterns"]
} [ground:system-policy] [conf:1.0] [state:confirmed]

[define|neutral] MEMORY_TAGGING := {
  WHO: "visual-art-composition-{session_id}",
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

[commit|confident] <promise>VISUAL_ART_COMPOSITION_VERILINGUA_VERIX_COMPLIANT</promise> [ground:self-validation] [conf:0.99] [state:confirmed]
