# Codex Safe Experiment Anti-Patterns

## Anti-Pattern 1: Skipping Sandbox for Risky Changes

**Problem**: Using full-auto mode when sandbox is warranted.

```text
BAD:
[Major refactoring]
./scripts/multi-model/codex-yolo.sh "Refactor auth system" task-id "." 10 full-auto

GOOD:
[Major refactoring]
./scripts/multi-model/codex-yolo.sh "Refactor auth system" task-id "." 10 sandbox
[Review results]
[If good, apply to real codebase]
```

**Why it matters**: Risky changes need isolation to prevent damage.

## Anti-Pattern 2: Applying Without Review

**Problem**: Automatically applying sandbox results to production.

```text
BAD:
[Sandbox experiment completes]
[Auto-apply all changes]

GOOD:
[Sandbox experiment completes]
[Review diffs carefully]
[Evaluate side effects]
[Apply selectively if appropriate]
```

**Why it matters**: Sandbox success doesn't guarantee production success.

## Anti-Pattern 3: No Success Criteria

**Problem**: Running experiments without clear goals.

```text
BAD:
"Try some things with the auth system"

GOOD:
"Experiment: Migrate from cookies to JWT
Success criteria:
1. All auth tests pass
2. Token refresh works
3. Logout invalidates tokens
4. No security regressions"
```

**Why it matters**: Can't evaluate success without criteria.

## Anti-Pattern 4: Sandbox for Simple Changes

**Problem**: Using sandbox for trivial, low-risk changes.

```text
BAD:
[Sandbox mode]
"Fix typo in error message"

GOOD:
[Direct edit]
"Fix typo in error message"
```

**Why it matters**: Overhead not justified for simple changes.

## Anti-Pattern 5: Trusting Sandbox Results Blindly

**Problem**: Assuming sandbox success means production will work.

```text
BAD:
[Sandbox passes]
"It works in sandbox, ship it!"

GOOD:
[Sandbox passes]
"Sandbox passed. Now let's:
1. Check dependencies not in sandbox
2. Test with real database
3. Verify network behavior
4. Run integration tests"
```

**Why it matters**: Sandbox isolation means missing some real-world factors.

## Anti-Pattern 6: No Rollback Plan

**Problem**: Applying sandbox results without ability to undo.

```text
BAD:
[Apply sandbox changes]
[No git commit before]
[No backup]

GOOD:
[Git commit current state]
[Apply sandbox changes]
[If issues: git checkout]
```

**Why it matters**: Always need an escape hatch.

## Anti-Pattern 7: Using for Production Debugging

**Problem**: Trying to debug production issues in sandbox.

```text
BAD:
[Production error]
[Try to reproduce in sandbox]
[Can't - sandbox has no network/db access]

GOOD:
[Production error]
[Debug in development environment]
[Use sandbox only for trying fixes]
```

**Why it matters**: Sandbox isolation prevents debugging network/db issues.

## Anti-Pattern 8: Ignoring Sandbox Limitations

**Problem**: Expecting sandbox to support all operations.

```text
SANDBOX LIMITATIONS:
- No network access (API calls fail)
- CWD only (no parent directory access)
- No sudo/admin operations
- No external database connections

BAD:
"Install npm packages and test API calls"
(Will fail - no network)

GOOD:
"Refactor the code structure"
(Works - file operations only)
```

**Why it matters**: Know what sandbox can and can't do.

## Recovery Protocol

If you find yourself in an anti-pattern:

1. STOP applying sandbox results
2. Review what changes were proposed
3. Determine if sandbox was appropriate
4. If not, switch to correct approach
5. Document why sandbox was/wasn't right
