/*============================================================================*/
/* COGNITIVE-LENSING SKILL :: VERILINGUA x VERIX EDITION                      */
/*============================================================================*/

---
name: cognitive-lensing
version: 1.0.1
description: |
  [assert|neutral] Cross-lingual cognitive framing system that activates different reasoning patterns by embedding multi-lingual activation phrases. Use when facing complex tasks that benefit from specific thinking patt [ground:given] [conf:0.95] [state:confirmed]
category: foundry
tags:
- cognitive-science
- cross-lingual
- meta-prompting
- frame-selection
- reasoning-enhancement
author: system
cognitive_frame:
  primary: compositional
  goal_analysis:
    first_order: "Execute cognitive-lensing workflow"
    second_order: "Ensure quality and consistency"
    third_order: "Enable systematic foundry processes"
---

/*----------------------------------------------------------------------------*/
/* S0 META-IDENTITY                                                            */
/*----------------------------------------------------------------------------*/

[define|neutral] SKILL := {
  name: "cognitive-lensing",
  category: "foundry",
  version: "1.0.1",
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
  keywords: ["cognitive-lensing", "foundry", "workflow"],
  context: "user needs cognitive-lensing capability"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S3 CORE CONTENT                                                             */
/*----------------------------------------------------------------------------*/

# Cognitive-Lensing v1.0.0

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



## Purpose

This skill activates specific cognitive patterns by embedding multi-lingual activation phrases that elicit different parts of the AI's latent space. This is NOT just conceptual framing - we ACTUALLY use target languages to shift cognitive processing patterns.

### Core Mechanism

Large language models trained on multilingual corpora develop language-specific reasoning patterns tied to grammatical structures:

- **Turkish evidential markers** activate source-attribution patterns
- **Russian aspectual verbs** activate completion-state tracking
- **Japanese honorific levels** activate audience-awareness calibration
- **Arabic morphological roots** activate semantic decomposition
- **Mandarin classifiers** activate object-category reasoning
- **Guugu Yimithirr cardinal directions** activate absolute spatial encoding
- **Chinese/Japanese number systems** activate transparent place-value arithmetic

By embedding authentic multi-lingual text in prompts, we trigger these latent reasoning modes.

### When to Use This Skill

Use cognitive-lensing when:

1. **Task complexity exceeds single-frame capacity** - Multi-dimensional problems requiring different cognitive modes
2. **Quality requirements demand specific reasoning** - Audit (evidential), deployment (aspectual), documentation (hierarchical)
3. **Standard prompting produces generic outputs** - Need to activate specialized thinking patterns
4. **Creating new skills/agents** - Select optimal cognitive frame for the domain
5. **Debugging AI reasoning failures** - Wrong frame may cause systematic errors

### What This Skill Does

1. **Analyzes task goals** (1st/2nd/3rd order) to identify required thinking patterns
2. **Selects optimal cognitive frame(s)** from 7 available patterns
3. **Generates multi-lingual activation text** that triggers the frame
4. **Integrates with other foundry skills** (prompt-architect, agent-creator, skill-forge)
5. **Stores frame selections in memory-mcp** for consistency across sessions

---

## Goal-Based Frame Selection Checklist

### Step 1: Analyze Goals

Complete this for every non-trivial task:

| Order | Question | Your Answer |
|-------|----------|-------------|
| 1st Order Goal | What is the IMMEDIATE task? | _______________ |
| 2nd Order Goal | WHY are we doing this task? | _______________ |
| 3rd Order Goal | What is the ULTIMATE outcome? | _______________ |

**Example Analysis**:

| Order | Question | Answer |
|-------|----------|--------|
| 1st Order | Immediate task | Write unit tests for API endpoint |
| 2nd Order | Why | Verify endpoint behavior is correct |
| 3rd Order | Ultimate outcome | Ensure production reliability |

### Step 2: Identify Dominant Thought Process

| Question | If YES, Use Frame |
|----------|-------------------|
| Is tracking "done vs not done" critical? | Aspectual (Russian) |
| Is source reliability critical? | Evidential (Turkish) |
| Is audience/formality critical? | Hierarchical (Japanese) |
| Is semantic decomposition needed? | Morphological (Arabic/Hebrew) |
| Is physical/visual comparison needed? | Classifier (Mandarin) |
| Is spatial navigation needed? | Spatial-Absolute (Guugu Yimithirr) |
| Is mathematical precision needed? | Numerical-Transparent (Chinese/Japanese) |

**Example Selection**:

For "Write unit tests for API endpoint":
- Tracking done/not done: YES (need to track test coverage completion)
- Source reliability: YES (need to verify test assertions match specs)

Selected Frames:
- Primary: Aspectual (Russian) - for completion tracking
- Secondary: Evidential (Turkish) - for assertion verification

### Step 3: Select Primary Frame

Based on analysis, select:
- **Primary Frame**: _______________
- **Secondary Frame (optional)**: _______________
- **Rationale**: _______________

---

## Seven Frame Activation Protocols

### Frame 1: Evidential (Turkish - Kanitsal Cerceve)

**When to

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
  pattern: "skills/foundry/cognitive-lensing/{project}/{timestamp}",
  store: ["executions", "decisions", "patterns"],
  retrieve: ["similar_tasks", "proven_patterns"]
} [ground:system-policy] [conf:1.0] [state:confirmed]

[define|neutral] MEMORY_TAGGING := {
  WHO: "cognitive-lensing-{session_id}",
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

[commit|confident] <promise>COGNITIVE_LENSING_VERILINGUA_VERIX_COMPLIANT</promise> [ground:self-validation] [conf:0.99] [state:confirmed]
