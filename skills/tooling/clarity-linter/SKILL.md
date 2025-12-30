/*============================================================================*/
/* CLARITY-LINTER SKILL :: VERILINGUA x VERIX EDITION                      */
/*============================================================================*/

---
name: clarity-linter
version: 2.1.0
description: |
  [assert|neutral] Machine-readable code clarity auditing with cognitive load optimization. 3-phase SOP - Metrics Collection (code-analyzer) -> Rubric Evaluation (reviewer) -> Fix Generation (coder + analyst). Detects t [ground:given] [conf:0.95] [state:confirmed]
category: quality
tags:
- general
author: system
cognitive_frame:
  primary: evidential
  goal_analysis:
    first_order: "Execute clarity-linter workflow"
    second_order: "Ensure quality and consistency"
    third_order: "Enable systematic quality processes"
---

/*----------------------------------------------------------------------------*/
/* S0 META-IDENTITY                                                            */
/*----------------------------------------------------------------------------*/

[define|neutral] SKILL := {
  name: "clarity-linter",
  category: "quality",
  version: "2.1.0",
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
  keywords: ["clarity-linter", "quality", "workflow"],
  context: "user needs clarity-linter capability"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S3 CORE CONTENT                                                             */
/*----------------------------------------------------------------------------*/

# Clarity Linter

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



## Phase 0: Expertise Loading

Before linting for clarity:

1. **Detect Domain**: Identify codebase language and patterns
2. **Check Expertise**: Look for `.claude/expertise/clarity-${lang}.yaml`
3. **Load Context**: If exists, load clarity thresholds and naming conventions
4. **Apply Configuration**: Use expertise for context-aware linting

**Purpose**: Evaluate code clarity and cognitive load using machine-readable rubric with weighted scoring

**Timeline**: 35-105 seconds (Metrics 10-30s + Evaluation 5-15s + Fixes 20-60s)

**Integration**: Runs alongside connascence-analyzer in dogfooding quality detection cycles

---

## System Architecture

```
[Code Implementation]
    ↓
[Metrics Collection] (code-analyzer)
    ↓  (func_lines, nesting_depth, call_count, name_semantic_score, etc.)
    ↓
[Rubric Evaluation] (reviewer)
    ↓  (5 dimensions: indirection, size, call depth, duplication, comments)
    ↓
[Scoring & Verdict] (ACCEPT ≥0.8 | REFINE 0.6-0.79 | REJECT <0.6)
    ↓
[Fix Generation] (coder + analyst)
    ↓  (Auto-fix PRs + Human-readable reports)
    ↓
[Memory-MCP Storage] (with WHO/WHEN/PROJECT/WHY tags)
```

---

## When to Use This Skill

Activate this skill when:
- Code quality audit focused on **readability and cognitive load** (not just coupling)
- Detecting thin helpers that add useless indirection
- Analyzing call chain depth and excessive layering
- Evaluating function size and cohesion
- Identifying poor naming patterns that hide complexity
- Checking comment density (over-commented vs under-explained)
- Complementing connascence analysis with clarity-specific patterns

**DO NOT** use this skill for:
- Pure coupling analysis (use connascence-analyzer)
- Security vulnerabilities (use security-testing-agent)
- Performance bottlenecks (use performance-testing-agent)
- Quick lint checks (use quick-quality-check)

---

## Input Contract

```yaml
input:
  target:
    type: enum[file, directory, workspace]
    path: string (required)
      # Absolute path to analyze

  rubric_config:
    rubric_path: string (default: .claude/skills/clarity-linter/.artifacts/clarity_rubric.json)
    policy: enum[strict, standard, lenient] (default: standard)
      # Affects threshold values in rubric

  metrics:
    collect_call_graph: boolean (default: true)
    analyze_naming: boolean (default: true)
    detect_duplication: boolean (default: true)

  options:
    auto_fix: boolean (default: false)
      # Generate auto-fix PRs for high-confidence violations
    report_format: enum[json, markdown, html] (default: markdown)
    min_score_threshold: number (default: 0.6, range: 0-1)
```

## Output Contract

```yaml
output:
  metrics:
    functions_analyzed: number
    files_analyzed: number
    total_metrics_collected: number
    collection_time_ms: number

  evaluation:
    overall_score: number (0-1)
    verdict: enum[ACCEPT, REFINE, REJECT]
    dimension_scores:
      thin_helpers_indirection: number (0-1)
      function_size_cohesion: number (0-1)
      indirection_call_depth: number (0-1)
      duplication_vs_dry: number (0-1)
      comments_explanation: number (0-1)

  violations:
    total_count: number
    by_severity:
      critical: number
      warning: number
      info: number
    by_check_id: object
      THIN_HELPER_SIZE: number
      PASS_THROUGH_WRAPPER: number
      SOFT_TOO_LONG_FUNCTION: number
      # ... (18 total checks from rubric)

  fixes:
    auto_fix_prs: array[object] (if auto_fix enabled)
      file: string
      violation_id: string
      diff: string
    suggested_fixes: array[object]
      file: string
      line: number
      check_id: string
      message: string
      suggested_fix: string

  reports:
    markdown_report: path
    json_detailed: path
    memory_namespace: string
```

---

## SOP Phase 1: Metrics Collection (10-30 sec)

**Objective**: Collect code metrics for clarity rubric evaluation



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
  pattern: "skills/quality/clarity-linter/{project}/{timestamp}",
  store: ["executions", "decisions", "patterns"],
  retrieve: ["similar_tasks", "proven_patterns"]
} [ground:system-policy] [conf:1.0] [state:confirmed]

[define|neutral] MEMORY_TAGGING := {
  WHO: "clarity-linter-{session_id}",
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

[commit|confident] <promise>CLARITY_LINTER_VERILINGUA_VERIX_COMPLIANT</promise> [ground:self-validation] [conf:0.99] [state:confirmed]
