/*============================================================================*/
/* WHEN-REVIEWING-PULL-REQUEST-ORCHESTRATE-COMPREHENSIVE-CODE-REVIEW SKILL :: VERILINGUA x VERIX EDITION                      */
/*============================================================================*/

---
name: when-reviewing-pull-request-orchestrate-comprehensive-code-review
version: 1.0.0
description: |
  [assert|neutral] Use when conducting comprehensive code review for pull requests across multiple quality dimensions. Orchestrates 12-15 specialized reviewer agents across 4 phases using star topology coordination. Cov [ground:given] [conf:0.95] [state:confirmed]
category: orchestration
tags:
- general
author: system
cognitive_frame:
  primary: compositional
  goal_analysis:
    first_order: "Execute when-reviewing-pull-request-orchestrate-comprehensive-code-review workflow"
    second_order: "Ensure quality and consistency"
    third_order: "Enable systematic orchestration processes"
---

/*----------------------------------------------------------------------------*/
/* S0 META-IDENTITY                                                            */
/*----------------------------------------------------------------------------*/

[define|neutral] SKILL := {
  name: "when-reviewing-pull-request-orchestrate-comprehensive-code-review",
  category: "orchestration",
  version: "1.0.0",
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
  keywords: ["when-reviewing-pull-request-orchestrate-comprehensive-code-review", "orchestration", "workflow"],
  context: "user needs when-reviewing-pull-request-orchestrate-comprehensive-code-review capability"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S3 CORE CONTENT                                                             */
/*----------------------------------------------------------------------------*/

# Code Review Orchestration Workflow

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



Comprehensive code review workflow orchestrating 12-15 specialized reviewers across automated checks, parallel expert reviews, integration analysis, and final approval recommendation. Designed for thorough quality validation across security, performance, architecture, testing, and documentation dimensions in a systematic 4-hour process.

## Overview

This SOP implements a multi-dimensional code review process using star topology coordination where a central PR manager orchestrates specialized reviewers operating in parallel. The workflow emphasizes both thoroughness and efficiency by running automated checks first (gate 1), then parallelizing specialized human-centric reviews, followed by integration impact analysis, and finally synthesizing all findings into actionable recommendations.

The star pattern enables each specialist to focus deeply on their domain while the coordinator ensures comprehensive coverage and prevents conflicting feedback. Memory coordination allows reviewers to reference findings from other specialists, creating a holistic review experience.

## Trigger Conditions

Use this workflow when:
- Reviewing pull requests requiring comprehensive quality validation
- Changes span multiple quality dimensions (code, security, performance, architecture)
- Need systematic review from multiple specialist perspectives
- PR introduces significant functionality or architectural changes
- Merge decision requires evidence-based go/no-go recommendation
- Team wants consistent, repeatable review process
- Code review SLA is within 4 hours (business hours)

## Orchestrated Agents (15 Total)

### Coordination Agent
- **`pr-manager`** - PR coordination, review orchestration, findings aggregation, author notification

### Automated Check Agents (Phase 1)
- **`code-analyzer`** - Linting, static analysis, code complexity metrics
- **`tester`** - Test execution, test suite validation
- **`qa-engineer`** - Coverage analysis, test quality assessment

### Specialized Review Agents (Phase 2)
- **`code-analyzer`** - Code quality, readability, maintainability, DRY, SOLID principles
- **`security-manager`** - Security vulnerabilities, OWASP compliance, secrets scanning, auth/auth
- **`performance-analyzer`** - Performance regressions, algorithmic efficiency, resource optimization
- **`system-architect`** - Architectural consistency, design patterns, scalability, integration fit
- **`api-documentation-specialist`** - Code documentation, API docs, comments, examples
- **`style-auditor`** - Code style consistency, formatting standards
- **`dependency-analyzer`** - Dependency audit, outdated packages, security vulnerabilities
- **`test-coverage-reviewer`** - Coverage metrics, uncovered code paths, edge case testing
- **`documentation-reviewer`** - README updates, changelog, migration guides

### Integration Analysis Agents (Phase 3)
- **`system-integrator`** - Integration impact, breaking changes, backward compatibility
- **`devops-engineer`** - Deployment impact, infrastructure changes, rollback planning
- **`code-reviewer`** - Risk assessment, blast radius analysis

## Workflow Phases

### Phase 1: Automated Checks (30 Minutes, Parallel Gate)

**Duration**: 30 minutes
**Execution Mode**: Parallel automated validation (fast fail-fast gate)
**Agents**: `code-analyzer`, `tester`, `qa-engineer`, `pr-manager`

**Process**:

1. **Initialize Review Swarm**
   ```bash
   PR_ID="$1"  # e.g., "repo-name/pulls/123"
   PR_NUMBER=$(echo $PR_ID | cut -d'/' -f3)

   npx claude-flow hooks pre-task --description "Code review: PR #${PR_NUMBER}"
   npx claude-flow swarm init --topology star --max-agents 15 --strategy specialized
   npx claude-flow agent spawn --type pr-manager
   ```

   **PR Manager** retrieves PR metadata:
   - Changed files and line counts
   - Commit history and messages
   - Branch comparison (base vs head)
   - PR des

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
  pattern: "skills/orchestration/when-reviewing-pull-request-orchestrate-comprehensive-code-review/{project}/{timestamp}",
  store: ["executions", "decisions", "patterns"],
  retrieve: ["similar_tasks", "proven_patterns"]
} [ground:system-policy] [conf:1.0] [state:confirmed]

[define|neutral] MEMORY_TAGGING := {
  WHO: "when-reviewing-pull-request-orchestrate-comprehensive-code-review-{session_id}",
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

[commit|confident] <promise>WHEN_REVIEWING_PULL_REQUEST_ORCHESTRATE_COMPREHENSIVE_CODE_REVIEW_VERILINGUA_VERIX_COMPLIANT</promise> [ground:self-validation] [conf:0.99] [state:confirmed]
