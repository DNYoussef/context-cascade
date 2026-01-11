# Example 1: Major Auth System Refactoring

## Scenario

Need to refactor the entire authentication system from session-based to JWT tokens.

## Risk Assessment

```yaml
risk_factors:
  - Breaking change to all protected routes
  - Session invalidation logic changes
  - Frontend token handling needed
  - Security implications

risk_level: HIGH
recommendation: USE SANDBOX
```

## Process

### Step 1: Define Success Criteria

```yaml
success_criteria:
  functional:
    - All auth tests pass
    - Login returns JWT token
    - Token refresh works
    - Logout invalidates tokens
    - Protected routes require valid token

  security:
    - Tokens expire appropriately
    - Refresh tokens are rotated
    - No sensitive data in token payload
    - HTTPS only for token transmission

  compatibility:
    - API contract unchanged (request/response shapes)
    - Existing clients can migrate gradually
```

### Step 2: Create Git Checkpoint

```bash
git add .
git commit -m "checkpoint: before auth refactoring experiment"
```

### Step 3: Execute Sandbox Experiment

```bash
./scripts/multi-model/codex-yolo.sh \
  "Refactor authentication from sessions to JWT:
   1. Replace express-session with jsonwebtoken
   2. Add token refresh endpoint
   3. Update auth middleware
   4. Update logout to blacklist tokens
   5. Keep API contracts unchanged
   Run tests after each change." \
  auth-refactor-001 \
  "." \
  15 \
  sandbox
```

### Step 4: Sandbox Execution Log

```text
[SANDBOX] Network: DISABLED
[SANDBOX] Filesystem: CWD only
[SANDBOX] Starting experiment...

[Iteration 1] Installing jsonwebtoken (from cache)
[Iteration 2] Creating TokenService
[Iteration 3] Updating auth middleware
[Iteration 4] Updating login endpoint
[Iteration 5] Adding refresh endpoint
[Iteration 6] Updating logout (token blacklist)
[Iteration 7] Running tests... 3 failures
[Iteration 8] Fixing test failures
[Iteration 9] Running tests... 0 failures

[SANDBOX] Experiment complete
[SANDBOX] Status: SUCCESS
```

### Step 5: Review Sandbox Results

```bash
# Codex provides diff summary
git diff --sandbox  # (hypothetical command)

# Changes summary:
# + src/services/TokenService.ts (new)
# + src/middleware/jwtAuth.ts (new)
# - src/middleware/sessionAuth.ts (removed)
# ~ src/routes/auth.ts (modified)
# ~ src/routes/protected.ts (modified)
# + src/utils/tokenBlacklist.ts (new)
```

### Step 6: Security Review

```yaml
security_checklist:
  - [ ] Token secret stored in env var: YES
  - [ ] Expiry time reasonable (15min access, 7d refresh): YES
  - [ ] No sensitive data in payload: YES (only userId, role)
  - [ ] Blacklist storage appropriate: YES (Redis)
  - [ ] HTTPS enforced: YES (middleware check)
```

### Step 7: Decision

```yaml
experiment_result: SUCCESS
tests_passing: ALL
security_review: PASSED
decision: APPLY TO REAL CODEBASE
```

### Step 8: Apply Changes

```bash
# Apply sandbox changes to real codebase
git apply sandbox-changes.patch

# Run tests in real environment
npm test  # All passing

# Commit
git add .
git commit -m "refactor: Migrate auth from sessions to JWT

- Added TokenService for JWT generation/validation
- Implemented token refresh with rotation
- Added token blacklist for logout
- Updated all protected routes

Tested in sandbox first (experiment: auth-refactor-001)
All 47 auth tests passing"
```

## Outcome

- **Experiment**: Successful in sandbox
- **Risk mitigated**: No production impact during experimentation
- **Confidence**: High (sandbox proved viability)
- **Rollback available**: Git checkpoint preserved
