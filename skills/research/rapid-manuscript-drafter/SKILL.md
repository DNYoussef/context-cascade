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

name: rapid-manuscript-drafter
description: Generate structured research manuscript drafts in 10-15 minutes with
  proper academic sections (Abstract, Introduction, Methods, Results, Discussion).
  Creates scaffolded drafts with placeholders for data, not fabricated content. Use
  for quickly producing first drafts from research ideas, speeding up the writing
  process while maintaining academic integrity.
version: 1.0.0
category: research
tags:
- research
- writing
- manuscript
- academic
- drafting
- rapid
author: ruv
mcp_servers:
  required: [memory-mcp]
  optional: [sequential-thinking]
  auto_enable: true
---

# Rapid Manuscript Drafter

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



## Purpose

Generate structured, scaffolded research manuscript drafts in 10-15 minutes that provide a solid foundation for academic writing. Unlike tools that fabricate content, this skill creates honest drafts with clear placeholders for user-provided data and findings.

## Critical Ethical Stance

**This skill NEVER fabricates research results or data.**

What we DO:
- Generate document structure and section scaffolding
- Write introduction and background based on known literature
- Create methodology templates based on described approach
- Provide results section structure with [YOUR_DATA] placeholders
- Draft discussion frameworks with logical argument structure

What we DON'T DO:
- Invent experimental results
- Fabricate statistical findings
- Create fake tables or figures with made-up numbers
- Generate citations to non-existent papers

## When to Use This Skill

Activate this skill when:
- Have a research idea ready to write up
- Need to quickly produce a first draft
- Want to overcome blank page syndrome
- Preparing a manuscript outline for collaborators
- Writing conference paper with tight deadline
- Need structured template for thesis chapter

**DO NOT** use this skill for:
- Final polished manuscripts (this is a first draft tool)
- Generating fake research (we don't do that)
- Replacing actual research work

## Manuscript Types Supported

1. **Research Article** (IMRaD format)
2. **Conference Paper** (shorter, focused)
3. **Review Article** (literature synthesis)
4. **Technical Report**
5. **Thesis Chapter**
6. **Grant Proposal Section**

## Input Contract

```yaml
input:
  manuscript_type: enum[research_article, conference_paper, review, technical_report, thesis_chapter, grant_section] (required)

  research_content:
    title: string (required)
    abstract_points: array[string] (optional)
    research_question: string (required)
    hypotheses: array[string] (optional)
    methodology_description: string (required)
    key_findings_summary: string (optional, will use placeholders if empty)
    contribution_claims: array[string] (required)

  literature_context:
    key_papers: array[object] (optional)
      title: string
      authors: string
      year: number
      relevance: string
    research_gap: string (required)

  target_venue:
    name: string (optional)
    word_limit: number (optional)
    style: enum[ieee, acm, nature, apa, chicago] (default: apa)

  output_preferences:
    include_placeholders: boolean (default: true)
    include_writing_tips: boolean (default: true)
    generate_outline_first: boolean (default: true)
```

## Output Contract

```yaml
output:
  manuscript:
    title: string
    sections: array[object]
      name: string
      content: string
      word_count: number
      completeness: percentage
      placeholders: array[string]

  outline:
    structure: object (hierarchical outline)

  metadata:
    total_words: number
    total_placeholders: number
    sections_complete: number
    sections_scaffolded: number
    generation_time: number

  next_steps:
    required_additions: array[string]
    recommended_revisions: array[string]
```

## SOP Phase 1: Outline Generation

Create hierarchical document structure:

```markdown
## Manuscript Outline: [TITLE]

### 1.

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
