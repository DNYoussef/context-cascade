/*============================================================================*/
/* ACADEMIC-READING-WORKFLOW SKILL :: VERILINGUA x VERIX EDITION                      */
/*============================================================================*/

---
name: academic-reading-workflow
version: 2.0
description: |
  [assert|neutral] Systematic reading methodology for academic papers and complex texts implementing Blue's (OSP) 3-phase approach. Use when reading papers/books that require deep understanding, searchable annotation sy [ground:given] [conf:0.95] [state:confirmed]
category: research
tags:
- general
author: system
cognitive_frame:
  primary: aspectual
  goal_analysis:
    first_order: "Execute academic-reading-workflow workflow"
    second_order: "Ensure quality and consistency"
    third_order: "Enable systematic research processes"
---

/*----------------------------------------------------------------------------*/
/* S0 META-IDENTITY                                                            */
/*----------------------------------------------------------------------------*/

[define|neutral] SKILL := {
  name: "academic-reading-workflow",
  category: "research",
  version: "2.0",
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
  keywords: ["academic-reading-workflow", "research", "workflow"],
  context: "user needs academic-reading-workflow capability"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S3 CORE CONTENT                                                             */
/*----------------------------------------------------------------------------*/

# Academic Reading Workflow

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



## Purpose

Execute systematic reading of academic papers, books, and complex texts using Blue's (OSP) 3-phase methodology: summary-first reading, active annotation with searchable keyword system, and evidence-based writing.

## When to Use This Skill

**Use this skill when:**
- ✅ Reading academic papers or dense books requiring deep understanding
- ✅ Building searchable knowledge base from readings
- ✅ Need to retain and find information later ("command-F in real life")
- ✅ Preparing to write evidence-based essays/analyses with citations

**Do NOT use for:**
- ❌ Quick skimming (<30 min)
- ❌ Casual reading without note-taking
- ❌ Fiction/entertainment reading
- ❌ Already familiar material (just creating citations)

**Decision Tree**: See `references/decision-tree.md`

## Quick Reference

| Step | Agent | Deliverable | Duration | Quality Gate |
|------|-------|-------------|----------|--------------|
| 0 | researcher | Master keyword list (if multi-source project) | 5-10 min | Keyword vocabulary defined |
| 1 | researcher | Reading roadmap with critical sections identified | 15-30 min | Clear thesis + sections |
| 2 | researcher | 20-50 searchable annotations with keyword tags | 1-4 hours | ≥20 notes, ≥5 keywords |
| 3 | analyst | Validated annotation set + keyword index | 15-30 min | Searchable, <30% quote-paraphrases |

**Optional**: Use `evidence-based-writing` skill separately when ready to write (not part of this workflow)

---

## Agent Coordination Protocol

### Sequential Execution
Each step passes deliverables to next step. Do NOT proceed if Quality Gate fails.

### Agent Roles
- **researcher**: Roadmap creation, reading, annotation (Steps 0, 1, 2)
- **analyst**: Validation, quality checks, keyword standardization (Step 3)

### Annotation Storage Format
All annotations stored as **Markdown with YAML frontmatter**:

```yaml
---
source: "[Title] - [Author] ([Year])"
page: [number]
keywords: [keyword1, keyword2, keyword3]
date_annotated: [YYYY-MM-DD]
project: [research-topic-slug]
annotation_id: [unique-id]
---

**Summary**: [Your paraphrase in own words]

**Quote** (if applicable): "[Exact text]" (p. [X])

**Why This Matters**: [Connection to research question]

**Links**: See also [Page Y], Conflicts with [Source B]
```

### Memory MCP Tags
Store with: `WHO=[agent]`, `WHEN=[timestamp]`, `PROJECT=[topic]`, `WHY=annotation`, `SOURCE=[title]`, `PAGE=[number]`

---

## Blue's Core Principles

This workflow embeds Blue's (OSP) methodology:

| Principle | Implementation |
|-----------|---------------|
| **"Read the Roadmap Before You Get Lost"** | Step 1: Summary-first, create plan BEFORE deep reading |
| **"Annotation is Command-F in Real Life"** | Step 2: Keyword tagging for searchable notes |
| **"Paraphrase > Highlighting"** | Step 2: Force genuine paraphrase, not quote-rewording |
| **"Write Like You Speak"** | (Evidence-based-writing skill): Natural draft, polish later |
| **"Thesis Comes LAST"** | (Evidence-based-writing skill): Let thesis emerge from notes |
| **"Every Claim Needs Source"** | (Evidence-based-writing skill): All assertions cited with pages |

See `references/blue-methodology.md` for full explanation.

---

## Step-by-Step Workflow

### STEP 0: Initialize Master Keyword List (Multi-Source Projects)
**Agent**: researcher
**Goal**: Define consistent keyword vocabulary across all sources in project

**When to Use**:
- ✅ Reading 3+ sources for same research project
- ✅ Building cross-source knowledge base
- ❌ Skip if reading single source

**Procedure**:
1. List main topics/concepts in your research project
2. Define standard keywords for each:
   - Use domain-standard terms when possible
   - Be specific (#methodology, not #method)
   - Use consistent formatting (#snake-case)
3. Create master keyword list:

```markdown
# MASTER KEYWORD LIST: [Project Name]

## Core Concepts
- #[concept-1] - Defini

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
  pattern: "skills/research/academic-reading-workflow/{project}/{timestamp}",
  store: ["executions", "decisions", "patterns"],
  retrieve: ["similar_tasks", "proven_patterns"]
} [ground:system-policy] [conf:1.0] [state:confirmed]

[define|neutral] MEMORY_TAGGING := {
  WHO: "academic-reading-workflow-{session_id}",
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

[commit|confident] <promise>ACADEMIC_READING_WORKFLOW_VERILINGUA_VERIX_COMPLIANT</promise> [ground:self-validation] [conf:0.99] [state:confirmed]
