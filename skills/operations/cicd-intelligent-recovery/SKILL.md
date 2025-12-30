/*============================================================================*/
/* SKILL SKILL :: VERILINGUA x VERIX EDITION                      */
/*============================================================================*/

---
name: SKILL
version: 1.0.0
description: |
  [assert|neutral] SKILL skill for operations workflows [ground:given] [conf:0.95] [state:confirmed]
category: operations
tags:
- general
author: system
cognitive_frame:
  primary: aspectual
  goal_analysis:
    first_order: "Execute SKILL workflow"
    second_order: "Ensure quality and consistency"
    third_order: "Enable systematic operations processes"
---

/*----------------------------------------------------------------------------*/
/* S0 META-IDENTITY                                                            */
/*----------------------------------------------------------------------------*/

[define|neutral] SKILL := {
  name: "SKILL",
  category: "operations",
  version: "1.0.0",
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
  keywords: ["SKILL", "operations", "workflow"],
  context: "user needs SKILL capability"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S3 CORE CONTENT                                                             */
/*----------------------------------------------------------------------------*/

# CI/CD Quality & Debugging Loop (Loop 3)

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



**Purpose**: Continuous integration with automated failure recovery and authentic quality validation.

**SOP Workflow**: Specification → Research → Planning → Execution → Knowledge

**Output**: 100% test success rate with authentic quality improvements and failure pattern analysis

**Integration**: This is Loop 3 of 3. Receives from `parallel-swarm-implementation` (Loop 2), feeds failure data back to `research-driven-planning` (Loop 1).

**Version**: 2.0.0
**Optimization**: Evidence-based prompting with explicit agent SOPs

---

## When to Use This Skill

Activate this skill when:
- Have complete implementation from Loop 2 (parallel-swarm-implementation)
- Need CI/CD pipeline automation with intelligent recovery
- Require root cause analysis for test failures
- Want automated repair with connascence-aware fixes
- Need validation of authentic quality (no theater)
- Generating failure patterns for Loop 1 feedback

**DO NOT** use this skill for:
- Initial development (use Loop 2 first)
- Manual debugging without CI/CD integration
- Quality checks during development (use Loop 2 theater detection)

---

## Input/Output Contracts

### Input Requirements

```yaml
input:
  loop2_delivery_package:
    location: .claude/.artifacts/loop2-delivery-package.json
    schema:
      implementation: object (complete codebase)
      tests: object (test suite)
      theater_baseline: object (theater metrics from Loop 2)
      integration_points: array[string]
    validation:
      - Must exist and be valid JSON
      - Must include theater_baseline for differential analysis

  ci_cd_failures:
    source: GitHub Actions workflow runs
    format: JSON array of failure objects
    required_fields: [file, line, column, testName, errorMessage, runId]

  github_credentials:
    required: gh CLI authenticated
    check: gh auth status
```

### Output Guarantees

```yaml
output:
  test_success_rate: 100% (guaranteed)

  quality_validation:
    theater_audit: PASSED (no false improvements)
    sandbox_validation: 100% test pass
    differential_analysis: improvement metrics

  failure_patterns:
    location: .claude/.artifacts/loop3-failure-patterns.json
    feeds_to: Loop 1 (next iteration)
    schema:
      patterns: array[failure_pattern]
      recommendations: object (planning/architecture/testing)

  delivery_package:
    location: .claude/.artifacts/loop3-delivery-package.json
    contains:
      - quality metrics (test success, failures fixed)
      - analysis data (root causes, connascence context)
      - validation results (theater, sandbox, differential)
      - feedback for Loop 1
```

---

## Prerequisites

Before starting Loop 3, ensure Loop 2 completion:

```bash
# Verify Loop 2 delivery package exists
test -f .claude/.artifacts/loop2-delivery-package.json && echo "✅ Ready" || echo "❌ Run parallel-swarm-implementation first"

# Load implementation data
npx claude-flow@alpha memory query "loop2_complete" --namespace "integration/loop2-to-loop3"

# Verify GitHub CLI authenticated
gh auth status || gh auth login
```

---

## 8-Step CI/CD Process Overview

```
Step 1: GitHub Hook Integration (Download CI/CD failure reports)
        ↓
Step 2: AI-Powered Analysis (Gemini + 7-agent synthesis with Byzantine consensus)
        ↓
Step 3: Root Cause Detection (Graph analysis + Raft consensus)
        ↓
Step 4: Intelligent Fixes (Program-of-thought: Plan → Execute → Validate → Approve)
        ↓
Step 5: Theater Detection Audit (6-agent Byzantine consensus validation)
        ↓
Step 6: Sandbox Validation (Isolated production-like testing)
        ↓
Step 7: Differential Analysis (Compare to baseline with metrics)
        ↓
Step 8: GitHub Feedback (Automated reporting and loop closure)
```

---

## Step 1: GitHub Hook Integration

**Objective**: Download and process CI/CD pipeline failure reports from GitHub Actions.

**Agent Coordi

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
  pattern: "skills/operations/SKILL/{project}/{timestamp}",
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
