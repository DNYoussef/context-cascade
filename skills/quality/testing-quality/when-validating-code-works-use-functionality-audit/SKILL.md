/*============================================================================*/
/* WHEN-VALIDATING-CODE-WORKS-USE-FUNCTIONALITY-AUDIT SKILL :: VERILINGUA x VERIX EDITION                      */
/*============================================================================*/

---
name: when-validating-code-works-use-functionality-audit
version: 1.0.0
description: |
  [assert|neutral] Validates that code actually works through sandbox testing, execution verification, and systematic debugging. Use this skill after code generation or modification to ensure functionality is genuine ra [ground:given] [conf:0.95] [state:confirmed]
category: research
tags:
- general
author: system
cognitive_frame:
  primary: evidential
  goal_analysis:
    first_order: "Execute when-validating-code-works-use-functionality-audit workflow"
    second_order: "Ensure quality and consistency"
    third_order: "Enable systematic research processes"
---

/*----------------------------------------------------------------------------*/
/* S0 META-IDENTITY                                                            */
/*----------------------------------------------------------------------------*/

[define|neutral] SKILL := {
  name: "when-validating-code-works-use-functionality-audit",
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
  keywords: ["when-validating-code-works-use-functionality-audit", "research", "workflow"],
  context: "user needs when-validating-code-works-use-functionality-audit capability"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S3 CORE CONTENT                                                             */
/*----------------------------------------------------------------------------*/

# Functionality Audit - Code Execution Validation

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



## When to Use This Skill

**Trigger Conditions:**
- After generating new code or modifying existing code
- When code appears complete but actual functionality is uncertain
- Before merging PRs or deploying to production
- When debugging reported issues or unexpected behavior
- As part of quality assurance workflows
- When validating third-party code integrations

## MCP Requirements

This skill requires the following MCP servers for optimal functionality:

### focused-changes (1.8k tokens - TIER 1: Code Quality)

**Purpose**: Track file changes during validation, analyze scope, and build error trees for systematic debugging.

**Tools Used**:
- `start_tracking`: Track code before execution testing
- `analyze_changes`: Validate changes are focused during Phase 3 debugging
- `root_cause_analysis`: Build error trees from test failures to identify root causes

**Activation** (PowerShell):
```powershell
# Check if already active
claude mcp list

# Add if not present
claude mcp add focused-changes node C:/Users/17175/Documents/Cline/MCP/focused-changes-server/build/index.js
```

**Usage Example**:
```javascript
// Phase 1: Start tracking before testing
mcp__focused_changes__start_tracking({
  filepath: 'src/api/users.js',
  content: originalCode
});

// Phase 3: Analyze failures and build error tree
mcp__focused_changes__root_cause_analysis({
  testResults: testOutputLog
});

// Validate fixes are focused
mcp__focused_changes__analyze_changes({
  newContent: fixedCode
});
```

**Token Cost**: 1.8k tokens (0.9% of 200k context)
**When to Load**: When validating code functionality with systematic debugging

### flow-nexus sandbox (6.2k tokens - TIER 5: Sandboxes)

**Purpose**: Execute code in isolated testing environments for safe functionality validation.

**Tools Used**:
- `sandbox_create`: Create isolated test environment with dependencies
- `sandbox_execute`: Run code with realistic inputs in sandboxed environment
- `sandbox_upload`: Upload test files to sandbox
- `sandbox_configure`: Configure environment variables and settings
- `sandbox_status`: Check sandbox health
- `sandbox_logs`: Retrieve execution logs
- `sandbox_delete`: Clean up sandbox after testing

**Activation** (PowerShell):
```powershell
# Requires Flow-Nexus authentication first
npx flow-nexus@latest login

# Check if already active
claude mcp list

# Add if not present
claude mcp add flow-nexus npx flow-nexus@latest mcp start
```

**Usage Example**:
```javascript
// Phase 1: Create sandbox for testing
const sandbox = await mcp__flow_nexus__sandbox_create({
  template: 'node',
  env_vars: {
    NODE_ENV: 'test',
    DATABASE_URL: 'sqlite::memory:'
  },
  install_packages: ['jest', 'supertest']
});

// Phase 2: Execute tests in sandbox
const result = await mcp__flow_nexus__sandbox_execute({
  sandbox_id: sandbox.id,
  code: testCode,
  timeout: 60
});

// Phase 3: Retrieve logs if failures
const logs = await mcp__flow_nexus__sandbox_logs({
  sandbox_id: sandbox.id,
  lines: 100
});

// Phase 5: Cleanup
await mcp__flow_nexus__sandbox_delete({
  sandbox_id: sandbox.id
});
```

**Token Cost**: 6.2k tokens (3.1% of 200k context)
**When to Load**: When isolated code execution and testing environments are required

**Situations Requiring Functionality Audit:**
- Code generated by AI that needs execution validation
- Complex logic changes requiring runtime verification
- Integration of new libraries or dependencies
- Refactoring that may have introduced regressions
- Migration to new frameworks or language versions

## Overview

This skill systematically validates that code delivers its intended behavior through actual execution rather than static analysis alone. It creates isolated testing environments (sandboxes), executes code with realistic inputs, captures outputs and errors, identifies root causes of failures through systematic debuggi

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
  pattern: "skills/research/when-validating-code-works-use-functionality-audit/{project}/{timestamp}",
  store: ["executions", "decisions", "patterns"],
  retrieve: ["similar_tasks", "proven_patterns"]
} [ground:system-policy] [conf:1.0] [state:confirmed]

[define|neutral] MEMORY_TAGGING := {
  WHO: "when-validating-code-works-use-functionality-audit-{session_id}",
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

[commit|confident] <promise>WHEN_VALIDATING_CODE_WORKS_USE_FUNCTIONALITY_AUDIT_VERILINGUA_VERIX_COMPLIANT</promise> [ground:self-validation] [conf:0.99] [state:confirmed]
