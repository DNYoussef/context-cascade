/*============================================================================*/
/* WHEN-DETECTING-FAKE-CODE-USE-THEATER-DETECTION SKILL :: VERILINGUA x VERIX EDITION                      */
/*============================================================================*/

---
name: when-detecting-fake-code-use-theater-detection
version: 1.0.0
description: |
  [assert|neutral] Detects non-functional 'theater' code that appears complete but doesn't actually work. Use this skill to identify code that looks correct in static analysis but fails during execution, preventing fake [ground:given] [conf:0.95] [state:confirmed]
category: research
tags:
- general
author: system
cognitive_frame:
  primary: evidential
  goal_analysis:
    first_order: "Execute when-detecting-fake-code-use-theater-detection workflow"
    second_order: "Ensure quality and consistency"
    third_order: "Enable systematic research processes"
---

/*----------------------------------------------------------------------------*/
/* S0 META-IDENTITY                                                            */
/*----------------------------------------------------------------------------*/

[define|neutral] SKILL := {
  name: "when-detecting-fake-code-use-theater-detection",
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
  keywords: ["when-detecting-fake-code-use-theater-detection", "research", "workflow"],
  context: "user needs when-detecting-fake-code-use-theater-detection capability"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S3 CORE CONTENT                                                             */
/*----------------------------------------------------------------------------*/

# Theater Code Detection

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



## When to Use This Skill

**Trigger Conditions:**
- Before merging AI-generated code into main branch
- When code review reveals suspiciously complete implementations
- After detecting inconsistencies between documentation and behavior
- As pre-deployment quality gate for critical systems
- When integrating third-party or unfamiliar code
- During security audits to identify fake security measures

**Situations Requiring Theater Detection:**
- Code that compiles but doesn't execute meaningful logic
- Functions with proper signatures but no-op implementations
- Tests that always pass regardless of code changes
- Security checks that can be bypassed trivially
- Error handling that catches but doesn't handle errors
- Mock implementations accidentally left in production code

## Overview

Theater code is code that "performs" correctness without delivering actual functionality. It passes static analysis, looks structurally sound, and may even have tests—but fails to implement the intended behavior. This skill systematically identifies theater code through pattern recognition, execution analysis, and behavioral validation.

The detection process scans codebases for suspicious patterns (empty catch blocks, no-op functions, always-passing tests), analyzes implementations for meaningful logic, executes code to validate actual behavior, and reports findings with actionable recommendations for remediation.

## Phase 1: Scan Codebase (Parallel)

**Agents**: code-analyzer (lead), reviewer (validation)
**Duration**: 10-15 minutes

**Scripts**:
```bash
# Initialize phase
npx claude-flow hooks pre-task --description "Phase 1: Scan Codebase for Theater Patterns"
npx claude-flow swarm init --topology mesh --max-agents 2

# Spawn agents
npx claude-flow agent spawn --type code-analyzer --capabilities "pattern-matching,ast-analysis,static-analysis"
npx claude-flow agent spawn --type reviewer --capabilities "code-quality,suspicious-pattern-detection"

# Memory coordination - define scan parameters
npx claude-flow memory store --key "testing/theater-detection/phase-1/analyzer/scan-config" --value '{"patterns":["empty-catch","no-op-function","always-pass-test"],"severity":"high"}'

# Execute phase work
# 1. Scan for empty catch blocks
echo "Scanning for empty error handlers..."
grep -r "catch\s*(\w*)\s*{\s*}" --include="*.js" --include="*.ts" . > empty-catches.txt || true

# 2. Scan for no-op functions
grep -r "function\s+\w+.*{\s*return\s*[;}]" --include="*.js" --include="*.ts" . > noop-functions.txt || true

# 3. Scan for always-passing tests
grep -r "expect(true).toBe(true)" --include="*.test.js" --include="*.test.ts" . > always-pass-tests.txt || true

# 4. Scan for TODO/FIXME/HACK comments indicating incomplete work
grep -rn "TODO\|FIXME\|HACK" --include="*.js" --include="*.ts" . > incomplete-markers.txt || true

# 5. Scan for suspicious imports (unused, test doubles in production)
echo "Analyzing imports..."
cat > scan-imports.js << 'EOF'
const fs = require('fs');
const path = require('path');

function scanImports(dir) {
  const suspicious = [];

  function walkDir(currentPath) {
    const files = fs.readdirSync(currentPath);

    files.forEach(file => {
      const filePath = path.join(currentPath, file);
      const stat = fs.statSync(filePath);

      if (stat.isDirectory() && !file.includes('node_modules')) {
        walkDir(filePath);
      } else if (file.endsWith('.js') || file.endsWith('.ts')) {
        const content = fs.readFileSync(filePath, 'utf-8');

        // Check for mock imports in production code
        if (!filePath.includes('test') && content.includes("'mock'")) {
          suspicious.push({
            file: filePath,
            reason: 'Mock import in production code',
            line: content.split('\n').findIndex(l => l.includes("'mock'")) + 1
          });
        }

        // Check for unused imports
       

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
  pattern: "skills/research/when-detecting-fake-code-use-theater-detection/{project}/{timestamp}",
  store: ["executions", "decisions", "patterns"],
  retrieve: ["similar_tasks", "proven_patterns"]
} [ground:system-policy] [conf:1.0] [state:confirmed]

[define|neutral] MEMORY_TAGGING := {
  WHO: "when-detecting-fake-code-use-theater-detection-{session_id}",
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

[commit|confident] <promise>WHEN_DETECTING_FAKE_CODE_USE_THEATER_DETECTION_VERILINGUA_VERIX_COMPLIANT</promise> [ground:self-validation] [conf:0.99] [state:confirmed]
