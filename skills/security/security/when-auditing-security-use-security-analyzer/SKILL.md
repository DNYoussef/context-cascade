/*============================================================================*/
/* WHEN-AUDITING-SECURITY-USE-SECURITY-ANALYZER SKILL :: VERILINGUA x VERIX EDITION                      */
/*============================================================================*/

---
name: when-auditing-security-use-security-analyzer
version: 1.0.0
description: |
  [assert|neutral] Comprehensive security auditing across static analysis, dynamic testing, dependency vulnerabilities, secrets detection, and OWASP compliance [ground:given] [conf:0.95] [state:confirmed]
category: security
tags:
- general
author: system
cognitive_frame:
  primary: evidential
  goal_analysis:
    first_order: "Execute when-auditing-security-use-security-analyzer workflow"
    second_order: "Ensure quality and consistency"
    third_order: "Enable systematic security processes"
---

/*----------------------------------------------------------------------------*/
/* S0 META-IDENTITY                                                            */
/*----------------------------------------------------------------------------*/

[define|neutral] SKILL := {
  name: "when-auditing-security-use-security-analyzer",
  category: "security",
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
  keywords: ["when-auditing-security-use-security-analyzer", "security", "workflow"],
  context: "user needs when-auditing-security-use-security-analyzer capability"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S3 CORE CONTENT                                                             */
/*----------------------------------------------------------------------------*/

# Security Analyzer - Comprehensive Security Auditing Skill

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



## Overview

This skill provides multi-vector security analysis combining static code analysis, dynamic testing, dependency auditing, secrets detection, and OWASP Top 10 compliance checking. Uses coordinated agents with validation gates between phases.

## Architecture

```
Security Manager (Coordinator)
    ├─→ Phase 1: Static Analysis (Code Analyzer)
    ├─→ Phase 2: Dynamic Testing (Tester)
    ├─→ Phase 3: Dependency Audit (Security Manager)
    ├─→ Phase 4: Secrets Detection (Code Analyzer)
    └─→ Phase 5: Compliance Check (Security Manager)
```

## Phase 1: Static Code Analysis

### Objective
Identify code-level vulnerabilities, security anti-patterns, and unsafe practices.

### Security Manager Setup
```bash
# Initialize security audit session
npx claude-flow@alpha hooks pre-task --description "Security static analysis initialization"
npx claude-flow@alpha hooks session-restore --session-id "security-audit-${DATE}"

# Set up memory namespace
npx claude-flow@alpha memory store \
  --key "swarm/security/config" \
  --value '{
    "scan_type": "static",
    "severity_threshold": "medium",
    "frameworks": ["owasp", "cwe"],
    "timestamp": "'$(date -Iseconds)'"
  }'
```

### Code Analyzer Execution
```bash
# Spawn code analyzer agent for static analysis
# Agent performs:

# 1. SQL Injection Detection
npx claude-flow@alpha hooks pre-task --description "SQL injection vulnerability scan"

# Scan patterns:
# ❌ VULNERABLE:
#   const query = "SELECT * FROM users WHERE id = " + userId;
#   db.query("SELECT * FROM " + tableName);
#
# ✅ SECURE:
#   const query = "SELECT * FROM users WHERE id = ?";
#   db.query(query, [userId]);

grep -rn "\.query\|\.exec" --include="*.js" --include="*.ts" . | \
  grep -v "?" | grep -v "\$[0-9]" > /tmp/sql-findings.txt

# 2. XSS Vulnerability Detection
# ❌ VULNERABLE:
#   element.innerHTML = userInput;
#   eval(userInput);
#   new Function(userInput)();
#
# ✅ SECURE:
#   element.textContent = userInput;
#   JSON.parse(sanitizedInput);

grep -rn "innerHTML\|eval\|new Function" --include="*.js" --include="*.jsx" . > /tmp/xss-findings.txt

# 3. Path Traversal Detection
# ❌ VULNERABLE:
#   fs.readFile(userPath);
#   require(userInput);
#
# ✅ SECURE:
#   const safePath = path.join(baseDir, path.normalize(userPath));
#   if (!safePath.startsWith(baseDir)) throw new Error('Invalid path');

grep -rn "readFile\|writeFile\|require.*\+" --include="*.js" . > /tmp/path-traversal-findings.txt

# 4. Insecure Cryptography
# ❌ VULNERABLE:
#   crypto.createHash('md5');
#   crypto.createCipher('des', key);
#
# ✅ SECURE:
#   crypto.createHash('sha256');
#   crypto.createCipheriv('aes-256-gcm', key, iv);

grep -rn "md5\|sha1\|des\|rc4" --include="*.js" --include="*.ts" . > /tmp/crypto-findings.txt

# Store findings in memory
npx claude-flow@alpha memory store \
  --key "swarm/security/static-analysis" \
  --value "$(cat /tmp/*-findings.txt | jq -Rs '{findings: ., timestamp: now}')"

npx claude-flow@alpha hooks post-task --task-id "static-analysis"
```

### Validation Gate 1
```bash
# Check if critical vulnerabilities found
CRITICAL_COUNT=$(cat /tmp/*-findings.txt | grep -c ".")

if [ "$CRITICAL_COUNT" -gt 0 ]; then
  echo "⚠️  GATE FAILED: $CRITICAL_COUNT potential vulnerabilities found"
  npx claude-flow@alpha hooks notify --message "Static analysis found $CRITICAL_COUNT issues - review required"
  # Continue but flag for review
fi
```

## Phase 2: Dynamic Security Testing

### Objective
Runtime vulnerability detection through active testing and fuzzing.

### Tester Agent Execution
```bash
npx claude-flow@alpha hooks pre-task --description "Dynamic security testing"

# 1. Authentication Bypass Testing
cat > /tmp/auth-test.js << 'EOF'
// Test suite for authentication vulnerabilities
const axios = require('axios');

async function testAuthBypass() {
  const tests = [
    // SQL 

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
  pattern: "skills/security/when-auditing-security-use-security-analyzer/{project}/{timestamp}",
  store: ["executions", "decisions", "patterns"],
  retrieve: ["similar_tasks", "proven_patterns"]
} [ground:system-policy] [conf:1.0] [state:confirmed]

[define|neutral] MEMORY_TAGGING := {
  WHO: "when-auditing-security-use-security-analyzer-{session_id}",
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

[commit|confident] <promise>WHEN_AUDITING_SECURITY_USE_SECURITY_ANALYZER_VERILINGUA_VERIX_COMPLIANT</promise> [ground:self-validation] [conf:0.99] [state:confirmed]
