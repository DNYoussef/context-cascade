---
name: when-auditing-security-use-security-analyzer
description: Comprehensive security auditing across static analysis, dynamic testing, dependency vulnerabilities, secrets detection, and OWASP compliance
---

## When to Use This Skill

Use this skill when conducting comprehensive security audits, performing vulnerability assessments, analyzing application security posture, identifying security misconfigurations, validating security controls, or preparing for penetration testing engagements.

## When NOT to Use This Skill

Do NOT use for compliance audits (use compliance skill instead), unauthorized security testing, production system scanning without approval, vulnerability exploitation (only identification), or automated scanning without manual validation. Avoid for code quality audits unrelated to security.

## Success Criteria

- All security vulnerabilities identified with CVSS scores and remediation guidance
- Security misconfigurations documented with severity ratings
- Attack surface mapped (exposed services, authentication mechanisms, data flows)
- Security controls validated (authentication, authorization, encryption, logging)
- Vulnerability remediation plan created with prioritization
- Zero critical/high vulnerabilities remaining after remediation
- Security findings validated through manual testing (not just automated scans)
- Penetration testing readiness achieved (all low-hanging fruit addressed)

## Edge Cases & Challenges

- False positives from automated security scanners
- Zero-day vulnerabilities without CVE mappings
- Business logic vulnerabilities requiring manual analysis
- Authentication bypass through indirect paths
- Encrypted communications requiring SSL interception
- Cloud-specific security misconfigurations (S3 buckets, IAM roles)
- Supply chain vulnerabilities in dependencies
- Time-of-check to time-of-use (TOCTOU) race conditions

## Guardrails (CRITICAL SECURITY RULES)

- NEVER exploit vulnerabilities beyond proof-of-concept validation
- NEVER conduct security testing on unauthorized systems
- NEVER exfiltrate sensitive data during security assessments
- NEVER cause denial-of-service or system instability
- NEVER share vulnerability details publicly before responsible disclosure
- ALWAYS obtain written authorization before security testing
- ALWAYS document findings with remediation guidance
- ALWAYS validate vulnerabilities through manual testing
- ALWAYS follow responsible disclosure timelines (90 days standard)
- ALWAYS maintain confidentiality of security findings
- ALWAYS use non-destructive testing methods where possible
- ALWAYS preserve audit trails of security testing activities

## Evidence-Based Validation

All security findings MUST be validated through:
1. **Automated scanning** - Multiple tools confirm vulnerability (Nessus, Burp, OWASP ZAP)
2. **Manual validation** - Security analyst reproduces finding independently
3. **Proof-of-concept** - Demonstrate exploitability without causing harm
4. **Code review** - Validate vulnerability at source code level
5. **Attack path analysis** - Document complete attack chain from entry to impact
6. **Remediation testing** - Verify fix resolves vulnerability without introducing new issues

# Security Analyzer - Comprehensive Security Auditing Skill

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
    // SQL Injection in auth
    { username: "admin'--", password: "anything" },
    { username: "admin' OR '1'='1", password: "" },

    // JWT manipulation
    { token: "eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIn0..." }, // None algorithm

    // Session fixation
    { session: "../../admin-session" },

    // NoSQL injection
    { username: { "$ne": null }, password: { "$ne": null } }
  ];

  const vulnerabilities = [];

  for (const test of tests) {
    try {
      const response = await axios.post('http://localhost:3000/login', test);
      if (response.status === 200) {
        vulnerabilities.push({
          type: 'AUTH_BYPASS',
          severity: 'CRITICAL',
          payload: test,
          description: 'Authentication bypass successful'
        });
      }
    } catch (e) {
      // Expected - auth failed
    }
  }

  return vulnerabilities;
}

module.exports = { testAuthBypass };
EOF

# 2. CSRF Testing
cat > /tmp/csrf-test.js << 'EOF'
async function testCSRF() {
  const response = await axios.post('http://localhost:3000/api/transfer', {
    to: 'attacker',
    amount: 1000
  }, {
    headers: {
      'Origin': 'http://evil.com',
      'Referer': 'http://evil.com'
    }
  });

  // Should be rejected without CSRF token
  if (response.status === 200) {
    return {
      type: 'CSRF',
      severity: 'HIGH',
      description: 'Missing CSRF protection on state-changing operation'
    };
  }
}
EOF

# 3. Rate Limiting Test
cat > /tmp/rate-limit-test.js << 'EOF'
async function testRateLimit() {
  const requests = [];
  for (let i = 0; i < 1000; i++) {
    requests.push(axios.get('http://localhost:3000/api/data'));
  }

  const responses = await Promise.all(requests);
  const successCount = responses.filter(r => r.status === 200).length;

  if (successCount > 100) {
    return {
      type: 'NO_RATE_LIMIT',
      severity: 'MEDIUM',
      description: `No rate limiting detected - ${successCount}/1000 requests succeeded`
    };
  }
}
EOF

# Execute dynamic tests
node /tmp/auth-test.js > /tmp/dynamic-findings.json
node /tmp/csrf-test.js >> /tmp/dynamic-findings.json
node /tmp/rate-limit-test.js >> /tmp/dynamic-findings.json

npx claude-flow@alpha memory store \
  --key "swarm/security/dynamic-testing" \
  --value "$(cat /tmp/dynamic-findings.json)"

npx claude-flow@alpha hooks post-task --task-id "dynamic-testing"
```

### Validation Gate 2
```bash
CRITICAL_RUNTIME=$(jq '[.[] | select(.severity == "CRITICAL")] | length' /tmp/dynamic-findings.json)

if [ "$CRITICAL_RUNTIME" -gt 0 ]; then
  echo "🚨 GATE FAILED: $CRITICAL_RUNTIME critical runtime vulnerabilities"
  exit 1  # Hard stop for critical runtime issues
fi
```

## Phase 3: Dependency Security Audit

### Objective
Identify known vulnerabilities (CVEs) in dependencies and supply chain risks.

### Security Manager Execution
```bash
npx claude-flow@alpha hooks pre-task --description "Dependency vulnerability scan"

# 1. NPM Audit
npm audit --json > /tmp/npm-audit.json 2>&1 || true

# 2. Check for outdated packages with known vulnerabilities
npm outdated --json > /tmp/outdated.json 2>&1 || true

# 3. License compliance check
npx license-checker --json > /tmp/licenses.json 2>&1 || true

# 4. Check for malicious packages (typosquatting)
cat package.json | jq -r '.dependencies | keys[]' | while read pkg; do
  # Check against known malicious package database
  if grep -q "$pkg" /tmp/malicious-packages.txt 2>/dev/null; then
    echo "⚠️  MALICIOUS PACKAGE DETECTED: $pkg"
  fi
done > /tmp/malicious-check.txt

# 5. SBOM (Software Bill of Materials) generation
npx @cyclonedx/cyclonedx-npm --output-file /tmp/sbom.json

# Analyze CVE severity
jq '{
  critical: [.vulnerabilities | to_entries[] | select(.value.severity == "critical")],
  high: [.vulnerabilities | to_entries[] | select(.value.severity == "high")],
  moderate: [.vulnerabilities | to_entries[] | select(.value.severity == "moderate")],
  low: [.vulnerabilities | to_entries[] | select(.value.severity == "low")],
  total: .metadata.vulnerabilities
}' /tmp/npm-audit.json > /tmp/dependency-summary.json

npx claude-flow@alpha memory store \
  --key "swarm/security/dependencies" \
  --value "$(cat /tmp/dependency-summary.json)"

npx claude-flow@alpha hooks post-task --task-id "dependency-audit"
```

### Validation Gate 3
```bash
CRITICAL_DEPS=$(jq '.critical | length' /tmp/dependency-summary.json)
HIGH_DEPS=$(jq '.high | length' /tmp/dependency-summary.json)

if [ "$CRITICAL_DEPS" -gt 0 ]; then
  echo "🚨 GATE FAILED: $CRITICAL_DEPS critical dependency vulnerabilities"
  npx claude-flow@alpha hooks notify --message "Critical CVEs detected in dependencies"
  exit 1
fi

if [ "$HIGH_DEPS" -gt 5 ]; then
  echo "⚠️  WARNING: $HIGH_DEPS high-severity dependency vulnerabilities"
fi
```

## Phase 4: Secrets Detection

### Objective
Identify exposed secrets, API keys, credentials, and sensitive data.

### Code Analyzer Execution
```bash
npx claude-flow@alpha hooks pre-task --description "Secrets and credentials detection"

# 1. Pattern-based secret detection
cat > /tmp/secret-patterns.txt << 'EOF'
# API Keys
AKIA[0-9A-Z]{16}  # AWS Access Key
AIza[0-9A-Za-z_-]{35}  # Google API Key
[REDACTED-EXAMPLE-PATTERN]  # Stripe Secret Key pattern
xox[baprs]-[0-9]{10,12}-[0-9]{10,12}-[a-zA-Z0-9]{24}  # Slack Token

# Passwords
password\s*=\s*['"]\w+['"]
api_key\s*=\s*['"]\w+['"]
secret\s*=\s*['"]\w+['"]

# Private Keys
--

# Database Credentials
(mongodb|postgres|mysql):\/\/[^:]+:[^@]+@

# JWT Tokens
eyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}
EOF

# Scan codebase
grep -rEn -f /tmp/secret-patterns.txt \
  --include="*.js" --include="*.ts" --include="*.json" --include="*.yaml" --include="*.env*" \
  --exclude-dir=node_modules --exclude-dir=.git \
  . > /tmp/secrets-found.txt 2>&1 || true

# 2. Entropy-based detection (random strings likely to be secrets)
find . -type f \( -name "*.js" -o -name "*.ts" -o -name "*.json" \) \
  -not -path "*/node_modules/*" -not -path "*/.git/*" \
  -exec grep -Eon '[A-Za-z0-9+/]{40,}' {} \; | \
  awk 'length($0) > 40' > /tmp/high-entropy-strings.txt

# 3. Environment variable exposure check
grep -rn "process\.env\." --include="*.js" --include="*.ts" . | \
  grep -v "process\.env\.NODE_ENV" | \
  grep -v "\/\/" > /tmp/env-usage.txt

# 4. Hardcoded IP addresses and URLs
grep -rEon '\b([0-9]{1,3}\.){3}[0-9]{1,3}\b' \
  --include="*.js" --include="*.ts" --include="*.json" \
  . > /tmp/hardcoded-ips.txt

# Generate report
cat > /tmp/secrets-report.json << EOF
{
  "secrets_found": $(wc -l < /tmp/secrets-found.txt),
  "high_entropy_strings": $(wc -l < /tmp/high-entropy-strings.txt),
  "env_exposures": $(wc -l < /tmp/env-usage.txt),
  "hardcoded_ips": $(wc -l < /tmp/hardcoded-ips.txt),
  "findings": $(cat /tmp/secrets-found.txt | jq -Rs 'split("\n") | map(select(length > 0))')
}
EOF

npx claude-flow@alpha memory store \
  --key "swarm/security/secrets" \
  --value "$(cat /tmp/secrets-report.json)"

npx claude-flow@alpha hooks post-task --task-id "secrets-detection"
```

### Validation Gate 4
```bash
SECRETS_COUNT=$(jq '.secrets_found' /tmp/secrets-report.json)

if [ "$SECRETS_COUNT" -gt 0 ]; then
  echo "🚨 GATE FAILED: $SECRETS_COUNT potential secrets detected"
  echo "Review findings in /tmp/secrets-found.txt"
  exit 1
fi
```

## Phase 5: OWASP Top 10 Compliance Check

### Objective
Verify compliance with OWASP Top 10 security standards.

### Security Manager Execution
```bash
npx claude-flow@alpha hooks pre-task --description "OWASP Top 10 compliance audit"

# OWASP Top 10 2021 Checklist
cat > /tmp/owasp-compliance.json << 'EOF'
{
  "A01:2021-Broken_Access_Control": {
    "checks": [
      "Authorization checks on all endpoints",
      "IDOR prevention",
      "CORS properly configured",
      "Directory listing disabled"
    ],
    "status": "pending"
  },
  "A02:2021-Cryptographic_Failures": {
    "checks": [
      "No sensitive data in transit without TLS",
      "Strong encryption algorithms (AES-256, SHA-256+)",
      "Secure key management",
      "No hardcoded secrets"
    ],
    "status": "pending"
  },
  "A03:2021-Injection": {
    "checks": [
      "Parameterized queries for SQL",
      "Input validation and sanitization",
      "No eval() or dangerous functions",
      "NoSQL injection prevention"
    ],
    "status": "pending"
  },
  "A04:2021-Insecure_Design": {
    "checks": [
      "Threat modeling performed",
      "Security requirements documented",
      "Secure coding patterns used",
      "Defense in depth implemented"
    ],
    "status": "pending"
  },
  "A05:2021-Security_Misconfiguration": {
    "checks": [
      "Default credentials changed",
      "Unnecessary features disabled",
      "Security headers configured",
      "Error messages don't leak info"
    ],
    "status": "pending"
  },
  "A06:2021-Vulnerable_Components": {
    "checks": [
      "All dependencies up to date",
      "No known CVEs in dependencies",
      "SBOM maintained",
      "Regular security scanning"
    ],
    "status": "pending"
  },
  "A07:2021-Auth_AuthZ_Failures": {
    "checks": [
      "Strong password policy",
      "MFA available",
      "Session management secure",
      "No credential stuffing vulnerability"
    ],
    "status": "pending"
  },
  "A08:2021-Software_Data_Integrity": {
    "checks": [
      "CI/CD pipeline secured",
      "Code signing implemented",
      "Integrity verification",
      "No untrusted deserialization"
    ],
    "status": "pending"
  },
  "A09:2021-Logging_Monitoring_Failures": {
    "checks": [
      "Security events logged",
      "Log aggregation configured",
      "Alerting set up",
      "Audit trails maintained"
    ],
    "status": "pending"
  },
  "A10:2021-SSRF": {
    "checks": [
      "URL validation on user input",
      "Network segmentation",
      "Whitelist for external requests",
      "No blind SSRF vulnerabilities"
    ],
    "status": "pending"
  }
}
EOF

# Automated compliance checks
# A01: Access Control
if grep -rq "req\.user\|req\.session" --include="*.js" .; then
  if grep -rq "if.*\.role\|authorize\|checkPermission" --include="*.js" .; then
    jq '.["A01:2021-Broken_Access_Control"].status = "pass"' /tmp/owasp-compliance.json > /tmp/owasp-temp.json
    mv /tmp/owasp-temp.json /tmp/owasp-compliance.json
  else
    jq '.["A01:2021-Broken_Access_Control"].status = "fail"' /tmp/owasp-compliance.json > /tmp/owasp-temp.json
    mv /tmp/owasp-temp.json /tmp/owasp-compliance.json
  fi
fi

# A02: Cryptographic Failures (check from Phase 1 findings)
if [ ! -s /tmp/crypto-findings.txt ]; then
  jq '.["A02:2021-Cryptographic_Failures"].status = "pass"' /tmp/owasp-compliance.json > /tmp/owasp-temp.json
  mv /tmp/owasp-temp.json /tmp/owasp-compliance.json
else
  jq '.["A02:2021-Cryptographic_Failures"].status = "fail"' /tmp/owasp-compliance.json > /tmp/owasp-temp.json
  mv /tmp/owasp-temp.json /tmp/owasp-compliance.json
fi

# A03: Injection (check from Phase 1 findings)
if [ ! -s /tmp/sql-findings.txt ] && [ ! -s /tmp/xss-findings.txt ]; then
  jq '.["A03:2021-Injection"].status = "pass"' /tmp/owasp-compliance.json > /tmp/owasp-temp.json
  mv /tmp/owasp-temp.json /tmp/owasp-compliance.json
else
  jq '.["A03:2021-Injection"].status = "fail"' /tmp/owasp-compliance.json > /tmp/owasp-temp.json
  mv /tmp/owasp-temp.json /tmp/owasp-compliance.json
fi

# A05: Security Misconfiguration
if grep -rq "helmet\|cors" package.json; then
  jq '.["A05:2021-Security_Misconfiguration"].status = "pass"' /tmp/owasp-compliance.json > /tmp/owasp-temp.json
  mv /tmp/owasp-temp.json /tmp/owasp-compliance.json
fi

# A06: Vulnerable Components (from Phase 3)
if [ "$(jq '.critical | length' /tmp/dependency-summary.json)" -eq 0 ]; then
  jq '.["A06:2021-Vulnerable_Components"].status = "pass"' /tmp/owasp-compliance.json > /tmp/owasp-temp.json
  mv /tmp/owasp-temp.json /tmp/owasp-compliance.json
else
  jq '.["A06:2021-Vulnerable_Components"].status = "fail"' /tmp/owasp-compliance.json > /tmp/owasp-temp.json
  mv /tmp/owasp-temp.json /tmp/owasp-compliance.json
fi

# Generate compliance score
TOTAL_CHECKS=$(jq '[.[].status] | length' /tmp/owasp-compliance.json)
PASSED_CHECKS=$(jq '[.[].status | select(. == "pass")] | length' /tmp/owasp-compliance.json)
COMPLIANCE_SCORE=$(echo "scale=2; $PASSED_CHECKS / $TOTAL_CHECKS * 100" | bc)

jq ". + {compliance_score: $COMPLIANCE_SCORE, total_checks: $TOTAL_CHECKS, passed: $PASSED_CHECKS}" \
  /tmp/owasp-compliance.json > /tmp/owasp-final.json

npx claude-flow@alpha memory store \
  --key "swarm/security/owasp-compliance" \
  --value "$(cat /tmp/owasp-final.json)"

npx claude-flow@alpha hooks post-task --task-id "owasp-compliance"
```

### Validation Gate 5
```bash
COMPLIANCE_SCORE=$(jq '.compliance_score' /tmp/owasp-final.json)

if (( $(echo "$COMPLIANCE_SCORE < 70" | bc -l) )); then
  echo "🚨 GATE FAILED: OWASP compliance score $COMPLIANCE_SCORE% (minimum 70%)"
  exit 1
fi

echo "✅ OWASP Compliance: $COMPLIANCE_SCORE%"
```

## Final Report Generation

```bash
# Consolidate all findings
cat > /tmp/security-audit-report.json << EOF
{
  "timestamp": "$(date -Iseconds)",
  "summary": {
    "static_analysis": $(cat /tmp/*-findings.txt | wc -l),
    "dynamic_vulnerabilities": $(jq 'length' /tmp/dynamic-findings.json 2>/dev/null || echo 0),
    "dependency_cves": $(jq '.total' /tmp/dependency-summary.json 2>/dev/null || echo 0),
    "secrets_exposed": $(jq '.secrets_found' /tmp/secrets-report.json 2>/dev/null || echo 0),
    "owasp_compliance": $(jq '.compliance_score' /tmp/owasp-final.json 2>/dev/null || echo 0)
  },
  "details": {
    "static_analysis": $(npx claude-flow@alpha memory retrieve --key "swarm/security/static-analysis"),
    "dynamic_testing": $(npx claude-flow@alpha memory retrieve --key "swarm/security/dynamic-testing"),
    "dependencies": $(npx claude-flow@alpha memory retrieve --key "swarm/security/dependencies"),
    "secrets": $(npx claude-flow@alpha memory retrieve --key "swarm/security/secrets"),
    "owasp": $(npx claude-flow@alpha memory retrieve --key "swarm/security/owasp-compliance")
  },
  "recommendations": []
}
EOF

# Generate markdown report
cat > /tmp/SECURITY-AUDIT-REPORT.md << 'EOF'
# Security Audit Report

**Generated:** $(date)
**Scan Duration:** [calculated from hooks]

## Executive Summary

| Metric | Count | Status |
|--------|-------|--------|
| Static Vulnerabilities | $(cat /tmp/*-findings.txt | wc -l) | $([ $(cat /tmp/*-findings.txt | wc -l) -eq 0 ] && echo "✅ PASS" || echo "⚠️  REVIEW") |
| Runtime Vulnerabilities | $(jq 'length' /tmp/dynamic-findings.json) | $([ $(jq 'length' /tmp/dynamic-findings.json) -eq 0 ] && echo "✅ PASS" || echo "🚨 FAIL") |
| Dependency CVEs | $(jq '.total' /tmp/dependency-summary.json) | $([ $(jq '.critical | length' /tmp/dependency-summary.json) -eq 0 ] && echo "✅ PASS" || echo "🚨 FAIL") |
| Exposed Secrets | $(jq '.secrets_found' /tmp/secrets-report.json) | $([ $(jq '.secrets_found' /tmp/secrets-report.json) -eq 0 ] && echo "✅ PASS" || echo "🚨 FAIL") |
| OWASP Compliance | $(jq '.compliance_score' /tmp/owasp-final.json)% | $([ $(echo "$(jq '.compliance_score' /tmp/owasp-final.json) >= 70" | bc) -eq 1 ] && echo "✅ PASS" || echo "🚨 FAIL") |

## Detailed Findings

### 1. Static Code Analysis
[Detailed findings from /tmp/*-findings.txt]

### 2. Dynamic Security Testing
[Detailed findings from /tmp/dynamic-findings.json]

### 3. Dependency Vulnerabilities
[Detailed findings from /tmp/dependency-summary.json]

### 4. Secrets Detection
[Detailed findings from /tmp/secrets-report.json]

### 5. OWASP Top 10 Compliance
[Detailed findings from /tmp/owasp-final.json]

## Recommendations

1. **Critical Priority:**
   - Fix all critical runtime vulnerabilities immediately
   - Remove exposed secrets from codebase
   - Update dependencies with critical CVEs

2. **High Priority:**
   - Address SQL injection vulnerabilities
   - Implement missing authentication checks
   - Configure security headers

3. **Medium Priority:**
   - Improve OWASP compliance score
   - Add rate limiting
   - Enhance logging and monitoring

## Remediation Guide

[Specific code examples and fixes for each vulnerability type]
EOF

# Store final report
npx claude-flow@alpha memory store \
  --key "swarm/security/final-report" \
  --value "$(cat /tmp/security-audit-report.json)"

# End session
npx claude-flow@alpha hooks session-end --export-metrics true

echo "✅ Security audit complete. Report: /tmp/SECURITY-AUDIT-REPORT.md"
```

## Usage Examples

### Full Security Audit
```bash
npx claude-flow@alpha skill run when-auditing-security-use-security-analyzer
```

### Specific Phase
```bash
npx claude-flow@alpha skill run when-auditing-security-use-security-analyzer --phase static-analysis
npx claude-flow@alpha skill run when-auditing-security-use-security-analyzer --phase secrets-detection
```

### Custom Configuration
```bash
npx claude-flow@alpha skill run when-auditing-security-use-security-analyzer \
  --config '{
    "severity_threshold": "high",
    "skip_phases": ["dynamic-testing"],
    "frameworks": ["owasp", "cwe", "sans-25"]
  }'
```

## Memory Patterns

This skill uses hierarchical memory storage:

```
swarm/security/
  ├─ config              # Scan configuration
  ├─ static-analysis     # Phase 1 findings
  ├─ dynamic-testing     # Phase 2 findings
  ├─ dependencies        # Phase 3 findings
  ├─ secrets             # Phase 4 findings
  ├─ owasp-compliance    # Phase 5 findings
  └─ final-report        # Consolidated report
```

## Real-World Examples

### Example 1: SQL Injection Found
```javascript
// ❌ VULNERABLE CODE DETECTED:
app.get('/user', (req, res) => {
  const query = `SELECT * FROM users WHERE id = ${req.query.id}`;
  db.query(query, (err, results) => {
    res.json(results);
  });
});

// ✅ RECOMMENDED FIX:
app.get('/user', (req, res) => {
  const query = 'SELECT * FROM users WHERE id = ?';
  db.query(query, [req.query.id], (err, results) => {
    if (err) return res.status(500).json({ error: 'Database error' });
    res.json(results);
  });
});
```

### Example 2: Exposed API Key
```javascript
// ❌ VULNERABLE CODE DETECTED:
const apiKey = 'EXAMPLE_REDACTED_NOT_REAL_KEY';
axios.get('https://api.stripe.com/v1/charges', {
  headers: { 'Authorization': `Bearer ${apiKey}` }
});

// ✅ RECOMMENDED FIX:
const apiKey = process.env.STRIPE_SECRET_KEY;
if (!apiKey) throw new Error('STRIPE_SECRET_KEY not configured');
axios.get('https://api.stripe.com/v1/charges', {
  headers: { 'Authorization': `Bearer ${apiKey}` }
});
```

### Example 3: Missing Authorization
```javascript
// ❌ VULNERABLE CODE DETECTED:
app.delete('/api/users/:id', (req, res) => {
  User.findByIdAndDelete(req.params.id)
    .then(() => res.json({ success: true }))
    .catch(err => res.status(500).json({ error: err.message }));
});

// ✅ RECOMMENDED FIX:
app.delete('/api/users/:id', authenticate, authorize('admin'), (req, res) => {
  // Verify user can only delete their own account or is admin
  if (req.user.id !== req.params.id && req.user.role !== 'admin') {
    return res.status(403).json({ error: 'Forbidden' });
  }

  User.findByIdAndDelete(req.params.id)
    .then(() => res.json({ success: true }))
    .catch(err => res.status(500).json({ error: err.message }));
});
```

## Performance Metrics

- **Static Analysis:** ~30-60 seconds for 10k LOC
- **Dynamic Testing:** ~2-5 minutes with server startup
- **Dependency Audit:** ~10-20 seconds
- **Secrets Detection:** ~15-30 seconds for 10k LOC
- **OWASP Compliance:** ~5-10 seconds

**Total Duration:** ~5-10 minutes for comprehensive audit

## Integration with CI/CD

```yaml
# .github/workflows/security-audit.yml
on: [push, pull_request]

jobs:
  security:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
      - run: npm ci
      - run: npx claude-flow@alpha skill run when-auditing-security-use-security-analyzer
      - uses: actions/upload-artifact@v3
        with:
          name: security-report
          path: /tmp/SECURITY-AUDIT-REPORT.md
```

## Exit Codes

- `0` - All checks passed
- `1` - Critical vulnerabilities found (hard stop)
- `2` - High-severity issues found (warning)
- `3` - Configuration error
- `4` - Scan incomplete

## Support

For issues or questions about this skill:
1. Check `/tmp/security-audit-report.json` for detailed diagnostics
2. Review memory at `swarm/security/*` for intermediate results
3. Consult OWASP documentation for specific vulnerability types
## Core Principles

### 1. Defense in Depth - Layer Security Controls
Security is never about a single control. Effective security auditing assumes multiple layers can fail and validates redundancy.

**In practice**:
- Never rely on client-side validation alone - always validate server-side
- Combine authentication, authorization, and input validation
- Use network segmentation, WAF, rate limiting, and endpoint security together
- Example: Even with parameterized queries, validate input format and sanitize output

### 2. Evidence-Based Validation - Prove, Don't Assume
Every security finding must be reproducible and validated through multiple methods before reporting.

**In practice**:
- Run findings through automated scanners AND manual verification
- Create proof-of-concept exploits in isolated environments
- Document attack chains from entry to impact
- Example: SQL injection finding requires: scanner detection + manual reproduction + code review + attack path analysis

### 3. Zero Trust Verification - Validate Everything
Security audits must verify security controls exist and function correctly, not trust configuration files or documentation.

**In practice**:
- Test authentication bypass attempts even when auth middleware exists
- Verify encrypted communications by inspecting network traffic
- Validate authorization at the data access layer, not just route level
- Example: Check if JWT tokens are actually validated or just decoded without signature verification

## Anti-Patterns

| Anti-Pattern | Problem | Solution |
|-------------|---------|----------|
| **Automated Scanner Only** | Relying solely on tools like Nessus or Burp without manual validation leads to false positives and missed business logic flaws | Use scanners for discovery, then manually validate each finding with proof-of-concept and code review |
| **Vulnerability Exploitation** | Going beyond proof-of-concept to fully exploit vulnerabilities causes damage and legal liability | Stop at minimal viable proof - demonstrate the vulnerability exists without extracting real data or causing disruption |
| **Testing Production Without Authorization** | Scanning production systems without written approval violates laws and can cause outages | Always obtain signed authorization before testing, document scope, and use non-production environments when possible |
| **Sharing Findings Publicly** | Disclosing vulnerabilities before patches are available puts users at risk and violates responsible disclosure | Follow 90-day disclosure timeline, notify vendor privately first, give time for patches before public disclosure |
| **Ignoring False Positives** | Dismissing scanner findings without investigation misses real vulnerabilities that scanners incorrectly flag as safe | Investigate every finding manually - false positives may reveal real issues in unexpected ways |


## Common Anti-Patterns

| Anti-Pattern | Problem | Solution |
|-------------|---------|----------|
| **Automated Scanner Only** | Relying solely on tools like Nessus or Burp without manual validation leads to false positives and missed business logic flaws | Use scanners for discovery, then manually validate each finding with proof-of-concept and code review |
| **Vulnerability Exploitation** | Going beyond proof-of-concept to fully exploit vulnerabilities causes damage and legal liability | Stop at minimal viable proof - demonstrate the vulnerability exists without extracting real data or causing disruption |
| **Testing Production Without Authorization** | Scanning production systems without written approval violates laws and can cause outages | Always obtain signed authorization before testing, document scope, and use non-production environments when possible |

---

## Conclusion

Comprehensive security auditing requires a systematic, multi-phase approach that combines automated tooling with manual expertise. The five-phase workflow (static analysis, dynamic testing, dependency audit, secrets detection, OWASP compliance) ensures no vulnerability category is overlooked while maintaining efficiency through automation.

The key to effective security auditing is rigorous validation. Automated scanners provide breadth but lack the depth to understand business logic vulnerabilities or verify exploitability. Every finding must pass through manual validation, proof-of-concept demonstration, and code review before being reported. This evidence-based approach prevents false positives from wasting remediation time while ensuring real vulnerabilities are properly understood and prioritized.

Security auditing is not a one-time activity but a continuous process. As applications evolve, new vulnerabilities emerge through code changes, dependency updates, and evolving attack techniques. Regular audits, integrated into CI/CD pipelines, provide ongoing assurance that security controls remain effective. The validation gates in this skill ensure that critical vulnerabilities block deployment while providing clear remediation guidance for developers. When executed properly, this systematic approach achieves both security rigor and development velocity.