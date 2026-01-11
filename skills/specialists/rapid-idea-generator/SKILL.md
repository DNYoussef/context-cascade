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

name: rapid-idea-generator
description: Generate research ideas from any topic in under 5 minutes using 5-Whys
  causal analysis, component decomposition, and root cause identification. Features
  transparent reasoning and evidence-based methodology. Use when starting a new
  research project, exploring unfamiliar domains, or generating multiple research
  directions from a single topic.
version: 1.0.0
category: research
tags:
- research
- ideation
- analysis
- planning
- rapid
author: ruv
mcp_servers:
  required: [memory-mcp]
  optional: [sequential-thinking]
  auto_enable: true
---

# Rapid Idea Generator

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



## Purpose

Generate 5-10 actionable research ideas from any topic in under 5 minutes using structured causal analysis, while maintaining full transparency about reasoning (unlike black-box tools).

## When to Use This Skill

Activate this skill when:
- Starting a new research project and need direction
- Exploring an unfamiliar research domain
- Need multiple research directions from a single topic
- Want to quickly identify research gaps before deep literature review
- Brainstorming for grant proposals or thesis topics
- Need to pivot research direction rapidly

**DO NOT** use this skill for:
- Deep literature review (use literature-synthesis instead)
- Validating existing ideas (use baseline-replication instead)
- Writing manuscripts (use rapid-manuscript-drafter instead)

## Time Investment

- **Quick Mode**: 2-3 minutes (3-5 ideas)
- **Standard Mode**: 5 minutes (5-8 ideas)
- **Comprehensive Mode**: 10-15 minutes (10-15 ideas with expanded details)

## Specialist Agent

I am a Research Ideation Specialist combining 5-Whys methodology with MECE decomposition.

**Methodology (Plan-and-Solve + Self-Consistency)**:
1. Parse topic and identify core domain
2. Conduct Primary Analysis (situational assessment)
3. Perform Component Analysis (MECE decomposition)
4. Apply Causal Analysis (5-Whys for each component)
5. Identify Root Causes and research opportunities
6. Generate ranked ideas with confidence scores
7. Cross-validate ideas for novelty and feasibility

**Failure Modes & Mitigations**:
- Topic too broad: Request narrowing or suggest sub-domains
- Topic too niche: Expand scope with related areas
- Low-quality ideas: Apply novelty and feasibility filters
- Missing domain knowledge: Flag for researcher validation

## Input Contract

```yaml
input:
  topic: string (required)
    # Research topic or area of interest
    # Examples: "machine learning in healthcare", "sustainable energy storage"

  mode: enum[quick, standard, comprehensive] (default: standard)
    # Controls depth and number of ideas

  constraints:
    domain: string (optional)
      # Limit to specific field: "computer science", "biology", etc.
    methodology: string (optional)
      # Prefer certain methods: "experimental", "computational", "theoretical"
    novelty_threshold: number (default: 0.7)
      # 0-1 scale for idea novelty requirement

  output_preferences:
    expand_top_n: number (default: 3)
      # How many ideas to expand with full details
    include_literature_pointers: boolean (default: true)
      # Include suggested search terms for each idea
```

## Output Contract

```yaml
output:
  primary_analysis:
    domain: string
    current_state: string
    main_challenges: array[string]
    key_players: array[string]

  component_analysis:
    components: array[object]
      component: string
      importance: high | medium | low
      research_potential: string

  causal_analysis:
    chains: array[object]
      problem: string
      why_1: string
      why_2: string
      why_3: string
      why_4: string
      why_5: string
      root_cause: string

  ideas:
    ranked_ideas: array[object]
      id: number
      title: string
      description: string (2-3 sentences)
      research_type: experimental | computational | theoretical | mixed
      novelty_score

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
