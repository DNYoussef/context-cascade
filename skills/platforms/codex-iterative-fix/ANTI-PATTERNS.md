# Codex Iterative Fix Anti-Patterns

## Anti-Pattern 1: Running on Production Code Without Review

**Problem**: Letting Codex modify production code without human verification.

```text
BAD:
[Codex fixes tests]
[Auto-deploy to production]

GOOD:
[Codex fixes tests]
[Human reviews changes]
[Run CI/CD pipeline]
[Deploy after approval]
```

**Why it matters**: Autonomous fixes may introduce subtle bugs or security issues.

## Anti-Pattern 2: Infinite Iteration Loop

**Problem**: Not setting iteration limits, letting Codex run forever.

```text
BAD:
./scripts/multi-model/codex-yolo.sh "Fix tests" task-id "." 999 full-auto

GOOD:
./scripts/multi-model/codex-yolo.sh "Fix tests" task-id "." 10 full-auto
[If still failing after 10 iterations, stop and analyze]
```

**Why it matters**: Some problems need human insight, not more iterations.

## Anti-Pattern 3: Ignoring New Failures

**Problem**: Celebrating passed tests while ignoring new failures.

```text
BAD:
Before: 5 tests failing
After: 0 original tests failing, 3 NEW tests failing
Result: "Success!"

GOOD:
Before: 5 tests failing
After: All tests passing (including new ones)
Result: True success
```

**Why it matters**: Fixes that break other things are not fixes.

## Anti-Pattern 4: Using for Research Tasks

**Problem**: Using iterative-fix when you need discovery.

```text
BAD:
Skill("codex-iterative-fix")
Task: "Figure out how auth should work"

GOOD:
Skill("multi-model-discovery")
Task: "Find auth best practices"
THEN
Skill("codex-iterative-fix")
Task: "Implement auth following discovered patterns"
```

**Why it matters**: Codex iterates on implementation, not research.

## Anti-Pattern 5: No Baseline Verification

**Problem**: Starting fixes without knowing what's actually broken.

```text
BAD:
[Run codex-iterative-fix immediately]

GOOD:
[Run tests first to establish baseline]
[Document which tests fail and why]
[Then run codex-iterative-fix]
[Verify all baseline failures fixed]
```

**Why it matters**: Can't measure success without knowing the starting point.

## Anti-Pattern 6: Skipping Sandbox for Risky Changes

**Problem**: Using full-auto mode for potentially destructive changes.

```text
BAD:
[Major refactoring]
./scripts/multi-model/codex-yolo.sh "Refactor entire auth system" task full-auto

GOOD:
[Major refactoring]
./scripts/multi-model/codex-yolo.sh "Refactor entire auth system" task sandbox
[Review sandbox results]
[If good, apply to real codebase]
```

**Why it matters**: Risky changes need isolation first.

## Anti-Pattern 7: Not Documenting What Changed

**Problem**: Fixes applied but no record of what was changed.

```text
BAD:
[Tests pass now]
[No record of what Codex did]

GOOD:
[Tests pass now]
[Git diff reviewed and committed]
[Memory-MCP updated with fix summary]
[Root causes documented]
```

**Why it matters**: Understanding the fix prevents recurrence.

## Recovery Protocol

If you find yourself in an anti-pattern:

1. STOP Codex iteration immediately
2. Review what changes were made (git diff)
3. Reset if necessary (git checkout)
4. Apply correct approach
5. Document lesson learned
