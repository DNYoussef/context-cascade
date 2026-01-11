# Example 2: Security Audit

## Scenario

Security review needed before production deployment. Need to identify all sensitive data handling, authentication patterns, and potential vulnerabilities.

## Process

### Step 1: Security-Focused Megacontext Query

```bash
./scripts/multi-model/delegate.sh gemini \
  "Security audit: Analyze entire codebase for:
   1. All PII and sensitive data handling
   2. Authentication and authorization patterns
   3. Input validation practices
   4. SQL injection / XSS / CSRF protection
   5. Secret management
   6. Logging of sensitive data
   7. Third-party dependency risks" \
  --all-files
```

### Step 2: Gemini Security Analysis

```yaml
pii_handling:
  database_fields:
    - table: users
      sensitive_columns: ["email", "password_hash", "phone", "address"]
      encryption: "password_hash uses bcrypt"

    - table: payment_methods
      sensitive_columns: ["card_last_four", "stripe_customer_id"]
      encryption: "Stored at Stripe, only IDs locally"

    - table: user_preferences
      sensitive_columns: ["notification_preferences"]
      encryption: "None (not PII)"

  pii_locations:
    - "src/models/User.ts"
    - "src/services/PaymentService.ts"
    - "src/controllers/UserController.ts"

authentication:
  method: "JWT with refresh tokens"
  implementation: "src/middleware/auth.ts"

  findings:
    good:
      - "Refresh tokens rotated on use"
      - "Access tokens expire in 15 minutes"
      - "Password hashing uses bcrypt (cost factor 12)"

    concerns:
      - "Refresh tokens don't have family tracking"
      - "No rate limiting on login endpoint"

authorization:
  method: "Role-based (RBAC)"
  implementation: "src/middleware/rbac.ts"

  findings:
    good:
      - "Centralized permission checking"
      - "Roles defined in constants (not strings)"

    concerns:
      - "Admin routes at /api/admin/* missing RBAC middleware"
        file: "src/routes/admin.ts:15-30"
        severity: HIGH

input_validation:
  library: "zod schemas"

  findings:
    good:
      - "All API inputs validated with schemas"
      - "Type coercion handled properly"

    concerns:
      - "File upload missing size limit"
        file: "src/controllers/UploadController.ts:45"
        severity: MEDIUM

      - "Search query not sanitized for SQL"
        file: "src/repositories/ProductRepository.ts:78"
        severity: HIGH

injection_protection:
  sql:
    orm: "Prisma (parameterized queries)"
    raw_queries: 2 instances found
    concerns:
      - "Raw SQL in search function"
        file: "src/repositories/ProductRepository.ts:78"
        code: "prisma.$queryRaw`SELECT * FROM products WHERE name LIKE '%${query}%'`"
        severity: HIGH

  xss:
    template_engine: "React (auto-escapes)"
    concerns:
      - "dangerouslySetInnerHTML usage"
        file: "src/components/RichText.tsx:23"
        severity: MEDIUM
        recommendation: "Use DOMPurify"

  csrf:
    protection: "SameSite cookies + CSRF tokens"
    concerns: None

secrets_management:
  method: "Environment variables"

  findings:
    good:
      - ".env in .gitignore"
      - "Secrets loaded via dotenv"

    concerns:
      - "API key hardcoded in test file"
        file: "tests/integration/payment.test.ts:8"
        severity: LOW (test env only)

logging:
  library: "pino"

  findings:
    concerns:
      - "User email logged on registration"
        file: "src/services/AuthService.ts:45"
        code: "logger.info({ email: user.email }, 'User registered')"
        severity: MEDIUM

      - "Full request body logged on error"
        file: "src/middleware/errorHandler.ts:12"
        severity: HIGH (may include passwords)

dependency_risks:
  critical: []
  high:
    - package: "moment@2.29.1"
      issue: "Path traversal in moment-timezone"
      recommendation: "Upgrade to 2.29.4+"
  medium:
    - package: "lodash@4.17.19"
      issue: "Prototype pollution"
      recommendation: "Upgrade to 4.17.21+"
```

### Step 3: Priority Ranking

```yaml
critical_issues: []

high_priority:
  1:
    issue: "SQL injection in search"
    file: "src/repositories/ProductRepository.ts:78"
    fix: "Use parameterized query"

  2:
    issue: "Admin routes missing RBAC"
    file: "src/routes/admin.ts:15-30"
    fix: "Add requireRole('admin') middleware"

  3:
    issue: "Request body logged with passwords"
    file: "src/middleware/errorHandler.ts:12"
    fix: "Redact sensitive fields before logging"

medium_priority:
  1:
    issue: "No rate limiting on login"
    fix: "Add express-rate-limit to auth routes"

  2:
    issue: "File upload no size limit"
    fix: "Add multer limits configuration"
```

### Step 4: Generate Report

```bash
Write docs/SECURITY-AUDIT-2024.md with:
- Executive summary
- Critical/High findings with remediation steps
- Medium/Low findings for backlog
- Dependency update recommendations
```

### Step 5: Store Findings

```bash
mcp__memory-mcp__memory_store \
  --key "security/myproject/audit-2024" \
  --value '{"high_issues": 3, "medium_issues": 4, "critical": 0, "status": "remediation_needed"}' \
  --tags "WHO=gemini-megacontext,WHY=security-audit,PROJECT=myproject"
```

## Outcome

- **Issues found**: 3 high, 4 medium, 1 low
- **Critical**: None (can proceed with remediation)
- **Time**: ~45 minutes (vs days of manual review)
- **Output**: Prioritized remediation list
