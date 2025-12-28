---
name: security
description: Security specialists hub for application security, vulnerability assessment, and secure coding. Routes to specialists for OWASP, penetration testing, and security hardening. Use for security audits, vulnerability fixes, and secure architecture.
---

# Security

Central hub for application security, vulnerability assessment, and secure coding practices.

## Phase 0: Expertise Loading

```yaml
expertise_check:
  domain: security
  file: .claude/expertise/security.yaml

  if_exists:
    - Load vulnerability patterns
    - Load OWASP guidelines
    - Apply security baselines

  if_not_exists:
    - Flag discovery mode
    - Document patterns learned
```

## Cognitive Frame Activation

### Kanitsal Guvenlik Denetimi (Evidential Security Audit)

Every security finding MUST include evidence. No vulnerabilities without proof.

**Evidence Structure**:
```yaml
vulnerability:
  id: VULN-001
  cve_cwe: "CWE-89 (SQL Injection)" or "CVE-2024-12345"
  lokasyon: "[file:line] src/api/users.js:42"
  kanit: |
    Proof of concept:
    curl -X POST /api/login -d "username=admin' OR '1'='1"
    Result: Bypassed authentication
  siddet: "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H (Score: 9.8)"
  evidence_type: "[DOGRUDAN]"
```

**Evidence Type Taxonomy**:
- **[DOGRUDAN]** (Direct): Vulnerability directly exploited in testing
  - Example: Successfully injected SQL, achieved RCE
- **[CIKARIM]** (Inferred): Pattern analysis suggests vulnerability
  - Example: User input concatenated to query without sanitization
- **[BILDIRILEN]** (Reported): Scanner/tool detected issue
  - Example: npm audit flagged CVE-2024-12345

**Mandatory Fields**:
1. **CVE/CWE**: Standard vulnerability reference
2. **LOKASYON**: Exact code location [file:line]
3. **KANIT**: Proof of concept or exploit evidence
4. **SIDDET**: CVSS score with vector breakdown

### Al-Itar al-Sarfi lil-Amn (Security Attack Morphology)

Decompose attack vectors into root causes. Fix the ROOT, not symptoms.

**Attack Vector Decomposition Template**:
```yaml
attack_morphology:
  vector: "SQL Injection (A03:2021)"

  decomposition:
    ROOT:
      type: "Insufficient Input Validation"
      location: "src/db/queries.js"
      pattern: "String concatenation in SQL queries"

    DERIVED_1:
      from: ROOT
      type: "User-Controlled Query Parameter"
      location: "req.body.username (unvalidated)"

    DERIVED_2:
      from: ROOT
      type: "Missing Parameterized Queries"
      location: "db.query() uses template literals"

    DERIVED_3:
      from: DERIVED_1
      type: "No Allowlist Validation"
      location: "Username accepts special characters"

  remediation:
    target: ROOT
    fix: "Implement parameterized queries (prepared statements)"
    cascading_fixes:
      - "Add input validation schema (Joi/Yup)"
      - "Implement allowlist for usernames"
      - "Remove string concatenation in all queries"

    why_not_symptom: |
      Escaping special characters (DERIVED_3) treats symptom.
      Using parameterized queries (ROOT) prevents vulnerability class.
```

**Morphological Rules**:
1. **Identify ROOT cause** (the fundamental flaw)
2. **Map DERIVED vulnerabilities** (cascading from ROOT)
3. **Target ROOT in remediation** (fix once, prevent many)
4. **Explain why not symptom** (justify root cause focus)

## When to Use This Skill

Use security when:
- Auditing code for vulnerabilities
- Fixing security issues
- Implementing authentication/authorization
- Hardening infrastructure
- Security code review

## Security Finding Template (Evidence-Based)

Use this template for ALL security findings:

```yaml
finding:
  id: "VULN-{number}"
  title: "{Vulnerability Name}"

  # EVIDENTIAL REQUIREMENTS (Turkish Frame)
  evidence:
    cve_cwe: "CWE-{number} ({Name})" # or CVE-YYYY-NNNNN
    lokasyon: "[file:line] {path}:{line_number}"
    kanit: |
      {Proof of concept exploit}
      {Test results showing vulnerability}
    siddet: "CVSS:3.1/{vector_string} (Score: {0.0-10.0})"
    evidence_type: "[DOGRUDAN|CIKARIM|BILDIRILEN]"

  # MORPHOLOGICAL ANALYSIS (Arabic Frame)
  attack_morphology:
    vector: "{Attack Type} (OWASP {category})"
    decomposition:
      ROOT:
        type: "{Fundamental vulnerability class}"
        location: "{Where root cause exists}"
        pattern: "{Code pattern enabling vulnerability}"
      DERIVED_N:
        from: "{ROOT or DERIVED_N-1}"
        type: "{Cascading vulnerability}"
        location: "{Specific instance}"

  # REMEDIATION (Target ROOT)
  remediation:
    target: "ROOT"
    priority: "[CRITICAL|HIGH|MEDIUM|LOW]"
    fix: "{Root cause solution}"
    cascading_fixes:
      - "{Fix derived vulnerability 1}"
      - "{Fix derived vulnerability 2}"
    why_not_symptom: |
      {Explain why targeting ROOT vs treating symptoms}

  # CVSS BREAKDOWN
  cvss:
    score: {0.0-10.0}
    vector: "CVSS:3.1/AV:{N|A|L|P}/AC:{L|H}/PR:{N|L|H}/UI:{N|R}/S:{U|C}/C:{N|L|H}/I:{N|L|H}/A:{N|L|H}"
    breakdown:
      attack_vector: "{Network|Adjacent|Local|Physical}"
      attack_complexity: "{Low|High}"
      privileges_required: "{None|Low|High}"
      user_interaction: "{None|Required}"
      scope: "{Unchanged|Changed}"
      confidentiality: "{None|Low|High}"
      integrity: "{None|Low|High}"
      availability: "{None|Low|High}"
```

## Security Domains

| Domain | Focus |
|--------|-------|
| AppSec | OWASP Top 10, secure coding |
| AuthN/AuthZ | OAuth, JWT, RBAC |
| Cryptography | Encryption, hashing, keys |
| Infrastructure | Hardening, firewalls, secrets |

## OWASP Top 10

```yaml
vulnerabilities:
  - A01: Broken Access Control
  - A02: Cryptographic Failures
  - A03: Injection
  - A04: Insecure Design
  - A05: Security Misconfiguration
  - A06: Vulnerable Components
  - A07: Auth Failures
  - A08: Data Integrity Failures
  - A09: Logging Failures
  - A10: SSRF
```

## Secure Coding Patterns

### Input Validation
```yaml
pattern: input_validation
rules:
  - Validate all inputs
  - Use allowlists
  - Parameterize queries
  - Encode outputs
```

### Authentication
```yaml
pattern: authentication
rules:
  - Use strong hashing (bcrypt/argon2)
  - Implement MFA
  - Secure session management
  - Rate limit attempts
```

## MCP Requirements

- **claude-flow**: For orchestration
- **Bash**: For security tools

## Recursive Improvement Integration (v2.1)

### Eval Harness Integration

```yaml
benchmark: security-benchmark-v1
  tests:
    - sec-001: Vulnerability detection
    - sec-002: Fix effectiveness
  minimum_scores:
    detection_rate: 0.90
    fix_quality: 0.95
```

### Memory Namespace

```yaml
namespaces:
  - security/audits/{id}: Security audits
  - security/vulnerabilities: Known patterns
  - improvement/audits/security: Skill audits
```

### Uncertainty Handling

```yaml
confidence_check:
  if confidence >= 0.8:
    - Proceed with fix
  if confidence 0.5-0.8:
    - Flag for review
  if confidence < 0.5:
    - Escalate to security expert
```

### Cross-Skill Coordination

Works with: **code-review-assistant**, **compliance**, **deployment-readiness**



## Core Principles

### 1. Defense in Depth
Security is never a single layer. Multiple independent security controls create redundancy that protects even when individual layers fail.

**In practice:**
- Combine input validation, parameterized queries, AND least-privilege database access for SQL injection defense
- Use authentication, authorization, AND audit logging for access control
- Layer network firewalls, application-level access controls, AND resource-level permissions
- Assume every layer can be compromised and design accordingly

### 2. Least Privilege
Grant only the minimum permissions required for functionality. Excessive permissions create unnecessary attack surface.

**In practice:**
- Database connections use read-only accounts unless write operations are explicitly required
- API keys have scoped permissions limited to specific resources and operations
- Service accounts cannot access user data or perform administrative actions
- Default to deny, explicitly allow only what is necessary

### 3. Security by Design, Not Afterthought
Security controls integrated during design are more effective and less costly than retrofitted protections.

**In practice:**
- Threat modeling happens in planning phase, not after implementation
- Security requirements are defined alongside functional requirements
- Code reviews include security checks before merge
- Automated security testing runs in CI/CD pipeline before deployment
- Security is a success criterion, not a post-launch audit

-----------|---------|----------|
| **Trusting user input** (using unsanitized data in queries, commands, or eval) | Enables injection attacks (SQL, XSS, command injection). User input is adversarial by default. | Validate all inputs against allowlists, parameterize queries, encode outputs, never use eval or dynamic code execution with user data. |
| **Hardcoded secrets** (API keys, passwords in source code) | Secrets in version control are public. Anyone with repo access gains credentials. | Use environment variables, secret management systems (HashiCorp Vault, AWS Secrets Manager), never commit secrets. |
| **Weak cryptography** (MD5, SHA1, DES, custom algorithms) | Broken algorithms provide false sense of security. Data appears protected but is trivially compromised. | Use modern algorithms: bcrypt/argon2 for passwords, AES-256-GCM for encryption, SHA-256+ for hashing. |
| **Security through obscurity** (hiding endpoints, relying on non-public URLs) | Obscurity is not security. Attackers find hidden resources through enumeration, logs, referrers. | Implement proper authentication and authorization. Assume all endpoints are discoverable. |
| **Ignoring dependency vulnerabilities** (never updating packages, ignoring npm audit warnings) | Known CVEs in dependencies are low-hanging fruit for attackers. Exploits are public and automated. | Regular dependency updates, automated vulnerability scanning (npm audit, Snyk, Dependabot), patch critical CVEs immediately. |
| **Overly broad CORS policies** (`Access-Control-Allow-Origin: *`) | Allows any website to make authenticated requests to your API, enabling CSRF and data exfiltration. | Use specific origin allowlists, never use wildcard with credentials, validate Origin header. |

-----------|---------|----------|
| **Trusting user input** (using unsanitized data in queries, commands, or eval) | Enables injection attacks (SQL, XSS, command injection). User input is adversarial by default. | Validate all inputs against allowlists, parameterize queries, encode outputs, never use eval or dynamic code execution with user data. |
| **Hardcoded secrets** (API keys, passwords in source code) | Secrets in version control are public. Anyone with repo access gains credentials. | Use environment variables, secret management systems (HashiCorp Vault, AWS Secrets Manager), never commit secrets. |
| **Weak cryptography** (MD5, SHA1, DES, custom algorithms) | Broken algorithms provide false sense of security. Data appears protected but is trivially compromised. | Use modern algorithms: bcrypt/argon2 for passwords, AES-256-GCM for encryption, SHA-256+ for hashing. |



## CHANGELOG

### v2.2.0 (2025-12-19)
**Cognitive Lensing Applied**: Evidential (Turkish) + Morphological (Arabic) frames

**Added**:
- Cognitive frame metadata in YAML frontmatter
  - Primary: evidential (Turkish - evidence-backed findings)
  - Secondary: morphological (Arabic - attack vector decomposition)
- Kanitsal Guvenlik Denetimi (Evidential Security Audit) section
  - Evidence structure template with CVE/CWE, lokasyon, kanit, siddet fields
  - Evidence type taxonomy: [DOGRUDAN], [CIKARIM], [BILDIRILEN]
  - Mandatory fields enforcement (CVE/CWE, LOKASYON, KANIT, SIDDET)
- Al-Itar al-Sarfi lil-Amn (Security Attack Morphology) section
  - Attack vector decomposition template (ROOT -> DERIVED chain)
  - Morphological rules for identifying root causes
  - Remediation focus on ROOT vs symptoms
- Security Finding Template with:
  - Full evidential requirements (Turkish frame)
  - Complete morphological analysis (Arabic frame)
  - CVSS 3.1 score breakdown with vector string
  - Priority classification and cascading fixes
  - Justification for root cause targeting

**Rationale**:
Security auditing requires:
1. Evidence-backed findings - No vulnerability claims without CVE/CWE references and proof of concept
2. Attack vector decomposition - Identify ROOT causes (fundamental flaws) vs DERIVED vulnerabilities (symptoms)
3. Systematic remediation - Fix root causes to prevent entire vulnerability classes, not just treat symptoms

**Impact**:
- Forces evidence citation for all security findings (prevents false positives)
- Decomposes complex attack vectors to foundational issues (more effective fixes)
- Prioritizes root cause remediation over symptom treatment (prevents recurrence)

### v2.1.0 (2024-11-XX)
- Added Recursive Improvement Integration (eval harness, memory namespace, uncertainty handling)
- Added cross-skill coordination with code-review-assistant, compliance, deployment-readiness
- Added skill completion verification checklist

### v2.0.0 (2024-XX-XX)
- Initial security skill with OWASP Top 10, secure coding patterns, authentication patterns
- Added defense in depth, least privilege, security by design principles
- Added anti-patterns table with solutions