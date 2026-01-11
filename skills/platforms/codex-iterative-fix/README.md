# Codex Iterative Fix Skill

> Autonomous test fixing and debugging with iteration until success.

## Quick Start

```bash
# Via codex-yolo.sh (recommended)
./scripts/multi-model/codex-yolo.sh "Fix all failing tests" task-id "." 15 full-auto

# Via delegate.sh
./scripts/multi-model/delegate.sh codex "Fix all failing tests" --full-auto

# Via router (auto-detected)
./scripts/multi-model/multi-model-router.sh "Fix all failing tests"

# Direct Codex
bash -lc "codex --full-auto exec 'Fix all failing tests and verify they pass'"
```

## Modes

| Mode | Flag | Risk | Use Case |
|------|------|------|----------|
| full-auto | `--full-auto` | Medium | Standard iteration |
| sandbox | `--sandbox workspace-write` | Low | Risky refactors |
| yolo | `--yolo` | High | Speed critical |

## When to Use

- Multiple tests failing
- Type errors blocking build
- CI/CD pipeline failures
- Iterative debugging

## When NOT to Use

- Research tasks (use multi-model-discovery)
- Understanding codebase (use gemini-codebase-onboard)
- Critical production (use sandbox first)

## Files in This Skill

```
codex-iterative-fix/
  SKILL.md           # Main skill definition
  ANTI-PATTERNS.md   # Common mistakes to avoid
  README.md          # This file
  examples/
    example-1-test-suite-fix.md
    example-2-type-errors.md
```

## Safety Protocol

1. ALWAYS establish baseline first
2. ALWAYS set iteration limit (10-15 recommended)
3. ALWAYS review changes before commit
4. NEVER run on production without review
5. USE sandbox mode for risky changes

## Memory Tags

Results stored with:
- WHO: codex-iterative-fix
- WHY: autonomous-fixing
- Key pattern: `multi-model/codex/iterative-fix/{project}/{task_id}`
