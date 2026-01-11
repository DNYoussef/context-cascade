# Codex Safe Experiment Skill

> Try risky changes in complete isolation before committing.

## Quick Start

```bash
# Via codex-yolo.sh (sandbox mode)
./scripts/multi-model/codex-yolo.sh "Refactor auth system" task-id "." 10 sandbox

# Via delegate.sh
./scripts/multi-model/delegate.sh codex "Try experimental approach" --sandbox

# Direct Codex
bash -lc "codex --sandbox workspace-write exec 'Experiment with X'"
```

## Sandbox Isolation

| Layer | Protection |
|-------|------------|
| Network | DISABLED - no external connections |
| Filesystem | CWD only - no parent access |
| OS-Level | Seatbelt (macOS) / Docker |
| Commands | Blocked: rm -rf, sudo, etc. |

## When to Use

- Major refactoring
- Library migrations
- Architectural changes
- Security-sensitive experiments
- Testing destructive operations

## When NOT to Use

- Simple, low-risk changes
- When network access needed
- When accessing files outside project
- Production debugging

## Workflow

1. **Design**: Define experiment and success criteria
2. **Execute**: Run in sandbox
3. **Evaluate**: Check results against criteria
4. **Decide**: Apply, modify, or discard

## Files in This Skill

```
codex-safe-experiment/
  SKILL.md           # Main skill definition
  ANTI-PATTERNS.md   # Common mistakes to avoid
  README.md          # This file
  examples/
    example-1-major-refactor.md
    example-2-library-migration.md
```

## Decision Framework

| Result | Action |
|--------|--------|
| All tests pass | Apply changes |
| Minor failures | Fix then apply |
| Major failures | Discard, try different approach |
| Unexpected behavior | Investigate first |

## Safety Protocol

1. ALWAYS define success criteria first
2. ALWAYS review sandbox diffs before applying
3. ALWAYS have rollback ready (git commit before)
4. NEVER apply blindly to production
5. NEVER expect network/db access in sandbox

## Memory Tags

Results stored with:
- WHO: codex-safe-experiment
- WHY: sandboxed-trial
- Key pattern: `multi-model/codex/experiment/{project}/{task_id}`
