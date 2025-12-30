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

# GitHub Workflow Automation Skill

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



## Overview

This skill provides comprehensive GitHub Actions automation with AI swarm coordination. It integrates intelligent CI/CD pipelines, workflow orchestration, and repository management to create self-organizing, adaptive GitHub workflows.

## Quick Start

<details>
<summary>💡 Basic Usage - Click to expand</summary>

### Initialize GitHub Workflow Automation
```bash
# Start with a simple workflow
npx ruv-swarm actions generate-workflow \
  --analyze-codebase \
  --detect-languages \
  --create-optimal-pipeline
```

### Common Commands
```bash
# Optimize existing workflow
npx ruv-swarm actions optimize \
  --workflow ".github/workflows/ci.yml" \
  --suggest-parallelization

# Analyze failed runs
gh run view <run-id> --json jobs,conclusion | \
  npx ruv-swarm actions analyze-failure \
    --suggest-fixes
```

</details>

## Core Capabilities

### 🤖 Swarm-Powered GitHub Modes

<details>
<summary>Available GitHub Integration Modes</summary>

#### 1. gh-coordinator
**GitHub workflow orchestration and coordination**
- **Coordination Mode**: Hierarchical
- **Max Parallel Operations**: 10
- **Batch Optimized**: Yes
- **Best For**: Complex GitHub workflows, multi-repo coordination

```bash
# Usage example
npx claude-flow@alpha github gh-coordinator \
  "Coordinate multi-repo release across 5 repositories"
```

#### 2. pr-manager
**Pull request management and review coordination**
- **Review Mode**: Automated
- **Multi-reviewer**: Yes
- **Conflict Resolution**: Intelligent

```bash
# Create PR with automated review
gh pr create --title "Feature: New capability" \
  --body "Automated PR with swarm review" | \
  npx ruv-swarm actions pr-validate \
    --spawn-agents "linter,tester,security,docs"
```

#### 3. issue-tracker
**Issue management and project coordination**
- **Issue Workflow**: Automated
- **Label Management**: Smart
- **Progress Tracking**: Real-time

```bash
# Create coordinated issue workflow
npx claude-flow@alpha github issue-tracker \
  "Manage sprint issues with automated tracking"
```

#### 4. release-manager
**Release coordination and deployment**
- **Release Pipeline**: Automated
- **Versioning**: Semantic
- **Deployment**: Multi-stage

```bash
# Automated release management
npx claude-flow@alpha github release-manager \
  "Create v2.0.0 release with changelog and deployment"
```

#### 5. repo-architect
**Repository structure and organization**
- **Structure Optimization**: Yes
- **Multi-repo Support**: Yes
- **Template Management**: Advanced

```bash
# Optimize repository structure
npx claude-flow@alpha github repo-architect \
  "Restructure monorepo with optimal organization"
```

#### 6. code-reviewer
**Automated code review and quality assurance**
- **Review Quality**: Deep
- **Security Analysis**: Yes
- **Performance Check**: Automated

```bash
# Automated code review
gh pr view 123 --json files | \
  npx ruv-swarm actions pr-validate \
    --deep-review \
    --security-scan
```

#### 7. ci-orchestrator
**CI/CD pipeline coordination**
- **Pipeline Management**: Advanced
- **Test Coordination**: Parallel
- **Deployment**: Automated

```bash
# Orchestrate CI/CD pipeline
npx claude-flow@alpha github ci-orchestrator \
  "Setup parallel test execution with smart caching"
```

#### 8. security-guardian
**Security and compliance management**
- **Security Scan**: Automated
- **Compliance Check**: Continuous
- **Vulnerability Management**: Proactive

```bash
# Security audit
npx ruv-swarm actions security \
  --deep-scan \
  --compliance-check \
  --create-issues
```

</details>

### 🔧 Workflow Templates

<details>
<summary>Production-Ready GitHub Actions Templates</summary>

#### 1. Intelligent CI with Swarms
```yaml
# .github/workflows/swarm-ci.yml
name: Intelligent CI with Swarms
on: [push, pull_request]

jobs:
  swarm-analysis:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkou

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
