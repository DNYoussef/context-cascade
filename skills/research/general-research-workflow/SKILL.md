/*============================================================================*/
/* GENERAL-RESEARCH-WORKFLOW SKILL :: VERILINGUA x VERIX EDITION                      */
/*============================================================================*/

---
name: general-research-workflow
version: 3.0
description: |
  [assert|neutral] Systematic 6-phase research methodology for history, mythology, and literature implementing Red's (OSP) evidence-based approach. Use when researching topics outside academic ML scope that require prim [ground:given] [conf:0.95] [state:confirmed]
category: research
tags:
- general
author: system
cognitive_frame:
  primary: evidential
  goal_analysis:
    first_order: "Execute general-research-workflow workflow"
    second_order: "Ensure quality and consistency"
    third_order: "Enable systematic research processes"
---

/*----------------------------------------------------------------------------*/
/* S0 META-IDENTITY                                                            */
/*----------------------------------------------------------------------------*/

[define|neutral] SKILL := {
  name: "general-research-workflow",
  category: "research",
  version: "3.0",
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
  keywords: ["general-research-workflow", "research", "workflow"],
  context: "user needs general-research-workflow capability"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S3 CORE CONTENT                                                             */
/*----------------------------------------------------------------------------*/

# General Research Workflow

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



## Purpose

Execute systematic general-purpose research across history, mythology, literature, and non-ML domains using Red's (OSP) 6-phase evidence-based methodology with rigorous source evaluation and synthesis.

## When to Use This Skill

**Use this skill when:**
- ✅ Researching historical events, mythological topics, or literary analysis
- ✅ Need to evaluate primary vs secondary sources
- ✅ Building evidence-based arguments with citations
- ✅ Topic requires source credibility analysis
- ✅ Have 6+ hours for thorough research

**Do NOT use for:**
- ❌ Academic ML research (use `literature-synthesis` instead)
- ❌ Quick fact-checking (<30 min)
- ❌ Literature reviews for academic papers (use `deep-research-orchestrator`)

**Decision Tree**: See `references/decision-tree.md`

## Quick Reference

| Step | Agent | Deliverable | Duration | Quality Gate |
|------|-------|-------------|----------|--------------|
| 0 | researcher | Wikipedia verification OR fallback plan | 5-10 min | ≥1 viable starting source |
| 1 | researcher | 10+ citations from Wikipedia references | 15-30 min | ≥10 citations, ≥3 categories |
| 2 | researcher | 20+ sources with metadata + relevance scores | 1-2 hours | ≥20 sources, ≥50% accessible |
| 3 | analyst | Classified sources with credibility/bias/priority scores | 30-60 min | ≥5 primaries, ≥80% credibility ≥3 |
| 4 | researcher | Context profiles for 10+ sources, 3+ time periods | 1-2 hours | ≥10 contextualized, ≥3 periods |
| 5 | researcher | 50+ notes, 20+ quotes with pages, 5+ cross-links | 2-3 hours | All quotas met |
| 6 | coordinator | Evidence-based thesis + final report | 1-2 hours | ≥5 sources support thesis, validated |

## Agent Coordination Protocol

### Sequential Execution
Each step passes deliverables to the next step. Do NOT proceed if Quality Gate fails.

### Agent Roles
- **researcher**: Discovery, analysis, note-taking (Steps 0, 1, 2, 4, 5, Phase A-B of Step 6)
- **analyst**: Validation, classification, quality checks (Step 3, Phase C of Step 6)
- **coordinator**: Synthesis orchestration (Phase D of Step 6)

### Memory MCP Tags
ALL stored data must include: `WHO=[agent]`, `WHEN=[timestamp]`, `PROJECT=[research-topic]`, `WHY=[intent]`

## Glossary

See `references/glossary.md` for complete definitions:
- **Primary Source**: Original documents/eyewitness accounts from the time period
- **Secondary Source**: Analysis/interpretation created after the events
- **Credibility Score (1-5)**: Reliability based on expertise, venue, citations
- **Bias Risk Score (1-5)**: Likelihood of systematic distortion
- **WorldCat**: worldcat.org - Global library catalog
- **Google Scholar**: scholar.google.com - Academic publication search

---

## Step-by-Step Workflow

### STEP 0: Pre-Flight Check (Gate 0)
**Agent**: researcher
**Goal**: Verify Wikipedia article exists OR establish fallback plan

**Procedure**:
1. Search Wikipedia for research topic
2. **IF article exists**: ✅ Proceed to Step 1
3. **IF NO article**:
   - Try related/broader topics, alternative spellings
   - **FALLBACK**: Start with Google Scholar search instead
   - Extract ≥10 citations from Scholar results
   - Document: "No Wikipedia article, started with Google Scholar"
4. Check language accessibility:
   - Flag non-English sources for translation assessment
   - Document language limitation if proceeding without translations

**Deliverable**: Confirmation of viable starting point

**Quality Gate 0**: STOP if no viable sources. Escalate to user for topic clarification.

---

### STEP 1: Wikipedia Mining
**Agent**: researcher
**Goal**: Extract reference trail from Wikipedia

**Procedure**:
1. Read Wikipedia article for overview
2. Navigate to "References" section
3. Extract ALL citations with metadata:
   - ✅ Author(s) [REQUIRED]
   - ✅ Title [REQUIRED]
   - ✅ Year [REQUIRED]
   - ⚠️ ISBN/DOI [OPTIONAL]
4. Extract "Further Read

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
  pattern: "skills/research/general-research-workflow/{project}/{timestamp}",
  store: ["executions", "decisions", "patterns"],
  retrieve: ["similar_tasks", "proven_patterns"]
} [ground:system-policy] [conf:1.0] [state:confirmed]

[define|neutral] MEMORY_TAGGING := {
  WHO: "general-research-workflow-{session_id}",
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

[commit|confident] <promise>GENERAL_RESEARCH_WORKFLOW_VERILINGUA_VERIX_COMPLIANT</promise> [ground:self-validation] [conf:0.99] [state:confirmed]
