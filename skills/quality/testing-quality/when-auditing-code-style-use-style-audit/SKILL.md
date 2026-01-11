/*============================================================================*/
/* WHEN-AUDITING-CODE-STYLE-USE-STYLE-AUDIT SKILL :: VERILINGUA x VERIX EDITION                      */
/*============================================================================*/

---
name: when-auditing-code-style-use-style-audit
version: 1.0.0
description: |
  [assert|neutral] Code style and conventions audit with auto-fix capabilities for comprehensive style enforcement [ground:given] [conf:0.95] [state:confirmed]
category: testing-quality
tags:
- general
author: system
cognitive_frame:
  primary: evidential
  goal_analysis:
    first_order: "Execute when-auditing-code-style-use-style-audit workflow"
    second_order: "Ensure quality and consistency"
    third_order: "Enable systematic testing-quality processes"
---

/*----------------------------------------------------------------------------*/
/* S0 META-IDENTITY                                                            */
/*----------------------------------------------------------------------------*/

[define|neutral] SKILL := {
  name: "when-auditing-code-style-use-style-audit",
  category: "testing-quality",
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
  keywords: ["when-auditing-code-style-use-style-audit", "testing-quality", "workflow"],
  context: "user needs when-auditing-code-style-use-style-audit capability"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S3 CORE CONTENT                                                             */
/*----------------------------------------------------------------------------*/

# Code Style Audit with Auto-Fix

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



## Purpose

Perform comprehensive code style and conventions audit across the entire codebase with automated fix capabilities. Identifies style violations, enforces naming conventions, validates formatting, and applies automated corrections to ensure consistent code quality.

## Core Principles

- **Automated Enforcement**: Auto-fix for style violations where possible
- **Comprehensive Coverage**: ESLint, Prettier, TypeScript, naming conventions
- **Evidence-Based**: Measurable style compliance metrics
- **Non-Breaking**: Only applies safe, non-destructive fixes
- **Continuous Compliance**: Style validation at every commit

## Phase 1: Scan Codebase

### Objective
Identify all style violations, formatting issues, and convention inconsistencies across the codebase.

### Agent Configuration
```yaml
agent: code-analyzer
specialization: style-scanning
tools: ESLint, Prettier, TypeScript
```

### Execution Steps

**1. Initialize Style Scan**
```bash
# Pre-task setup
npx claude-flow@alpha hooks pre-task \
  --agent-id "code-analyzer" \
  --description "Comprehensive code style scanning" \
  --task-type "style-scan"

# Restore session context
npx claude-flow@alpha hooks session-restore \
  --session-id "style-audit-${AUDIT_ID}" \
  --agent-id "code-analyzer"
```

**2. ESLint Comprehensive Scan**
```bash
# Run ESLint with all rules
npx eslint . \
  --ext .js,.jsx,.ts,.tsx \
  --format json \
  --output-file eslint-report.json \
  --max-warnings 0

# Separate auto-fixable vs manual issues
npx eslint . \
  --ext .js,.jsx,.ts,.tsx \
  --format json \
  --fix-dry-run > eslint-fixable-report.json
```

**3. Prettier Formatting Check**
```bash
# Check all supported file types
npx prettier --check "**/*.{js,jsx,ts,tsx,json,css,scss,md,yaml,yml}" \
  --list-different > prettier-violations.txt

# Check configuration consistency
npx prettier --find-config-path . > prettier-config-check.txt
```

**4. TypeScript Style Validation**
```bash
# Strict type checking
npx tsc --noEmit --strict --pretty false 2> typescript-strict-errors.txt

# Check for any types
grep -r ": any" src/ --include="*.ts" --include="*.tsx" > any-types.txt

# Check for implicit any
npx tsc --noImplicitAny --noEmit 2> implicit-any-errors.txt
```

**5. Naming Convention Analysis**
```javascript
// Naming patterns validation
const namingConventions = {
  // File naming
  files: {
    pattern: /^[a-z][a-z0-9-]*\.(js|ts|jsx|tsx)$/,
    examples: ['user-service.js', 'api-client.ts'],
    violations: []
  },

  // Directory naming
  directories: {
    pattern: /^[a-z][a-z0-9-]*$/,
    examples: ['user-api', 'auth-service'],
    violations: []
  },

  // Class naming (PascalCase)
  classes: {
    pattern: /^[A-Z][a-zA-Z0-9]*$/,
    examples: ['UserService', 'ApiClient'],
    violations: []
  },

  // Function naming (camelCase)
  functions: {
    pattern: /^[a-z][a-zA-Z0-9]*$/,
    examples: ['getUserById', 'calculateTotal'],
    violations: []
  },

  // Constant naming (UPPER_SNAKE_CASE)
  constants: {
    pattern: /^[A-Z][A-Z0-9_]*$/,
    examples: ['MAX_RETRIES', 'API_BASE_URL'],
    violations: []
  },

  // React component naming (PascalCase)
  components: {
    pattern: /^[A-Z][a-zA-Z0-9]*$/,
    examples: ['UserProfile', 'LoginForm'],
    violations: []
  },

  // Private methods (leading underscore)
  privateMethods: {
    pattern: /^_[a-z][a-zA-Z0-9]*$/,
    examples: ['_validateInput', '_processData'],
    violations: []
  }
};

// Scan for naming violations
function scanNamingViolations(ast) {
  ast.walk((node) => {
    if (node.type === 'ClassDeclaration') {
      if (!namingConventions.classes.pattern.test(node.id.name)) {
        namingConventions.classes.violations.push({
          file: node.loc.source,
          line: node.loc.start.line,
          found: node.id.name,
          expected: toPascalCase(node.id.name)
        });
      }
    }
    // Simila

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
  pattern: "skills/testing-quality/when-auditing-code-style-use-style-audit/{project}/{timestamp}",
  store: ["executions", "decisions", "patterns"],
  retrieve: ["similar_tasks", "proven_patterns"]
} [ground:system-policy] [conf:1.0] [state:confirmed]

[define|neutral] MEMORY_TAGGING := {
  WHO: "when-auditing-code-style-use-style-audit-{session_id}",
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

[commit|confident] <promise>WHEN_AUDITING_CODE_STYLE_USE_STYLE_AUDIT_VERILINGUA_VERIX_COMPLIANT</promise> [ground:self-validation] [conf:0.99] [state:confirmed]
