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

name: researcher
description: Multi-level research with Gemini Search integration supporting 3 research
  depths. Use when gathering information, conducting systematic analysis, or synthesizing
  knowledge from multiple sources. Applies 90%+ credibility scoring and comprehensive
  source evaluation.
version: 1.0.0
category: research
tags:
- research
- analysis
- planning
author: ruv
---

# Researcher - Systematic Information Gathering

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



Systematic multi-level research with integrated Gemini Search for comprehensive knowledge synthesis.

## When to Use This Skill

Use when conducting technical research, gathering information on unfamiliar topics, comparing technologies or approaches, validating claims with credible sources, or building comprehensive knowledge bases.

## 3-Level Research Methodology

### Level 1: Basic Research (< 5 minutes)
- Quick factual queries
- Single-source validation
- Surface-level understanding
- Immediate answers needed

**Process**:
1. Query Gemini Search for primary information
2. Validate source credibility (>70%)
3. Extract key facts
4. Provide concise summary

### Level 2: Multi-Source Research (15-30 minutes)
- Cross-reference multiple sources
- Deeper analysis required
- Technical understanding needed
- Comprehensive overview desired

**Process**:
1. Query 3-5 authoritative sources
2. Compare and contrast findings
3. Identify consensus and disagreements
4. Synthesize into coherent analysis
5. Score sources for credibility (>85%)

### Level 3: Deep Dive Research (1+ hours)
- Extensive investigation
- Academic rigor required
- Complex topic with nuances
- Publication-ready research

**Process**:
1. Systematic literature review
2. Query 10+ diverse sources
3. Analyze methodology and evidence
4. Identify research gaps
5. Synthesize comprehensive report
6. Ensure 90%+ source credibility

## Source Evaluation Criteria

### Credibility Scoring (0-100%)
- **Authority** (30%): Expert author, institutional backing
- **Accuracy** (25%): Fact-checked, peer-reviewed, verifiable
- **Objectivity** (20%): Minimal bias, balanced perspective
- **Currency** (15%): Recent publication, up-to-date information
- **Coverage** (10%): Comprehensive treatment of topic

### Source Types by Reliability
1. **Tier 1 (90-100%)**: Peer-reviewed journals, official documentation
2. **Tier 2 (75-89%)**: Industry reports, credible news outlets
3. **Tier 3 (60-74%)**: Blog posts from experts, technical forums
4. **Tier 4 (<60%)**: Unverified sources, opinion pieces

## Gemini Search Integration

- Use `gemini-search` skill for web queries
- Enable grounded search for factual accuracy
- Leverage Google Search API for broad coverage
- Apply source verification automatically

## Output Formats

- **Summary**: Key findings in bullet points
- **Synthesis**: Coherent narrative combining sources
- **Bibliography**: Annotated source list with credibility scores
- **Analysis**: Detailed evaluation with evidence
## Core Principles

Researcher operates on 3 fundamental principles:

### Principle 1: Credibility-First Source Evaluation
Every source is scored using a multi-dimensional rubric (Authority, Accuracy, Objectivity, Currency, Coverage) before incorporation. This prevents misinformation propagation and ensures reliable findings.

In practice:
- Tier 1 sources (90-100%) prioritized for critical claims
- Cross-validation required when using Tier 3 sources (60-74%)
- Automatic rejection of sources scoring below 60% credibility

### Principle 2: Multi-Source Triangulation
Claims are validated through independent corroboration from 3+ sources at different tiers. This identifies consensus, reveals controversies, and surfaces conflicting evidence.

In practice:
- Key technical findings backed by peer-reviewed journals plus official documentation
- Contradictory evidence explicitly reported with analysis of disagreement sources
- Single-source claims flagged and ma

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
