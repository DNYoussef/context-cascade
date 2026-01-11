# Example 1: Test Suite Failures

## Scenario

CI pipeline failing with 12 test errors after a dependency upgrade.

## Process

### Step 1: Establish Baseline

```bash
# Run tests to capture current state
npm test 2>&1 | tee test-baseline.log

# Output:
# FAIL src/auth/login.test.ts
# FAIL src/auth/logout.test.ts
# FAIL src/api/users.test.ts
# ... (12 failures total)
```

### Step 2: Analyze Failure Patterns

```yaml
failure_analysis:
  pattern_1:
    count: 8
    type: "Mock type mismatch"
    root_cause: "Updated library changed return types"

  pattern_2:
    count: 3
    type: "Timeout errors"
    root_cause: "Async behavior changed"

  pattern_3:
    count: 1
    type: "Missing property"
    root_cause: "API response shape changed"
```

### Step 3: Execute Codex Iterative Fix

```bash
./scripts/multi-model/codex-yolo.sh \
  "Fix all 12 failing tests. Issues are:
   1. Mock type mismatches (8 tests) - update mock types
   2. Timeout errors (3 tests) - fix async/await patterns
   3. Missing property (1 test) - update expected response shape" \
  fix-tests-001 \
  "." \
  15 \
  full-auto
```

### Step 4: Codex Iteration Log

```text
[Iteration 1] Running tests... 12 failures
[Iteration 1] Analyzing: Mock type mismatch in login.test.ts
[Iteration 1] Fix: Updated MockAuthService type
[Iteration 2] Running tests... 11 failures
[Iteration 2] Analyzing: Same pattern in logout.test.ts
[Iteration 2] Fix: Applied same mock fix
...
[Iteration 8] Running tests... 3 failures (timeouts)
[Iteration 8] Analyzing: Async pattern issue
[Iteration 8] Fix: Added proper await, increased timeout
...
[Iteration 12] Running tests... 0 failures
[Iteration 12] SUCCESS - All tests passing
```

### Step 5: Review Changes

```bash
git diff --stat

# Output:
# src/auth/login.test.ts     | 15 ++++++-----
# src/auth/logout.test.ts    | 12 ++++----
# src/api/users.test.ts      | 8 ++---
# src/mocks/AuthService.ts   | 25 +++++++++++----
# src/test-utils/async.ts    | 10 +++++++
# 5 files changed, 45 insertions(+), 25 deletions(-)
```

### Step 6: Verify and Document

```bash
# Run full test suite one more time
npm test

# All 247 tests passing

# Document in Memory-MCP
mcp__memory-mcp__memory_store \
  --key "fixes/test-suite/dep-upgrade-2024" \
  --value '{
    "fixed_count": 12,
    "patterns": ["mock_types", "async_timeout", "api_response"],
    "files_changed": 5,
    "iterations": 12,
    "root_cause": "library dependency upgrade"
  }' \
  --tags "WHO=codex-iterative-fix,WHY=ci-failure,PROJECT=my-app"
```

### Step 7: Commit

```bash
git add .
git commit -m "fix: Update tests for library v3 upgrade

- Updated mock types for new AuthService interface
- Fixed async/await patterns in timeout tests
- Updated API response expectations

Fixes: 12 test failures from dep upgrade
Codex iterations: 12
"
```

## Outcome

- **Tests fixed**: 12/12
- **Time**: ~15 minutes (vs hours manually)
- **Side effects**: None (ran full suite)
- **Documentation**: Captured for future upgrades
