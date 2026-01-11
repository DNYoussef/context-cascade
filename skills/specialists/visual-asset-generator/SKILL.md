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

name: visual-asset-generator
description: Automatically generate research diagrams, charts, tables, and visualizations
  from data or descriptions. Creates publication-ready visual assets including PRISMA
  flow diagrams, methodology flowcharts, results charts, comparison tables, and architecture
  diagrams. Use when preparing manuscripts, presentations, or documentation that requires
  professional visual elements.
version: 1.0.0
category: research
tags:
- research
- visualization
- diagrams
- charts
- tables
- publication
author: ruv
mcp_servers:
  required: [memory-mcp]
  optional: []
  auto_enable: true
---

# Visual Asset Generator

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



## Purpose

Automatically generate publication-ready visual assets (diagrams, charts, tables) from data or descriptions in seconds, filling the gap between text-based research and visual communication.

## When to Use This Skill

Activate this skill when:
- Preparing figures for a research manuscript
- Creating methodology flowcharts
- Generating PRISMA flow diagrams for systematic reviews
- Building comparison tables from research data
- Designing architecture diagrams for systems/methods
- Creating presentation slides with data visualizations
- Documenting experimental pipelines

**DO NOT** use this skill for:
- Fabricating data (this is unethical - we only visualize real data)
- Complex statistical analysis (use appropriate analysis tools first)
- Interactive dashboards (use dedicated BI tools)

## Critical Design Principle

**This skill NEVER fabricates data.**

This skill only visualizes:
1. Data explicitly provided by the user
2. Placeholder templates clearly marked as "[YOUR DATA HERE]"
3. Structural diagrams (flowcharts, architectures) without data

## Supported Visual Asset Types

### 1. Research Diagrams
- PRISMA flow diagrams
- Methodology flowcharts
- Experimental pipeline diagrams
- System architecture diagrams
- Conceptual framework diagrams
- Decision trees

### 2. Data Visualizations
- Bar charts (comparison)
- Line charts (trends)
- Scatter plots (correlations)
- Box plots (distributions)
- Heatmaps (matrices)
- Confusion matrices

### 3. Tables
- Comparison tables (methods, results)
- Summary statistics tables
- Feature matrices
- Literature summary tables
- Hyperparameter tables

### 4. Specialized Research Figures
- Model architecture diagrams
- Ablation study visualizations
- Training curves
- ROC/PR curves (from data)
- Attention visualizations

## Input Contract

```yaml
input:
  asset_type: enum[diagram, chart, table, specialized] (required)

  subtype: string (required)
    # For diagrams: "prisma", "methodology", "pipeline", "architecture", "conceptual"
    # For charts: "bar", "line", "scatter", "box", "heatmap"
    # For tables: "comparison", "summary", "feature_matrix", "literature"
    # For specialized: "model_architecture", "ablation", "training_curves"

  data: object | array | null
    # Actual data to visualize (required for charts)
    # NULL for structural diagrams (will generate template)

  description: string (required for diagrams)
    # Natural language description of what to visualize

  style:
    format: enum[svg, mermaid, graphviz, ascii, markdown] (default: mermaid)
    color_scheme: enum[default, publication, presentation, minimal]
    size: enum[small, medium, large, full_page]

  output_preferences:
    include_caption: boolean (default: true)
    include_source_note: boolean (default: true)
    latex_compatible: boolean (default: false)
```

## Output Contract

```yaml
output:
  visual_asset:
    type: string
    subtype: string
    format: string
    content: string  # The actual diagram/chart/table code

  rendering:
    code: string  # Mermaid/GraphViz/Markdown code
    preview_instructions: string
    export_commands: array[string]

  caption:
    short: string
    long: string

  metadata:
    data_source: string  # "user_provided" | "template_placeholder"
 

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
