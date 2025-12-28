# Ralph Wiggum Integration for Context Cascade

## Overview

This directory contains the Ralph Wiggum persistence loop integration for the Context Cascade plugin system. It enables continuous self-referential AI loops for iterative development until task completion.

## What is Ralph Wiggum?

Named after the character from The Simpsons, Ralph is a development methodology based on continuous AI agent loops. The philosophy is simple: **persistence wins**.

Instead of Claude trying once and giving up, Ralph creates a loop that keeps trying until:
1. A completion promise is found in the output
2. Maximum iterations are reached

## How It Works

```
1. User runs /ralph-loop "task" --completion-promise "DONE" --max-iterations 30
2. Claude works on the task
3. Claude tries to exit
4. Stop hook intercepts exit attempt
5. If <promise>DONE</promise> NOT found in output:
   - Increment iteration counter
   - Re-inject the SAME prompt
   - Loop continues
6. If promise found OR max iterations reached:
   - Allow normal exit
   - Report results
```

## Files

| File | Purpose |
|------|---------|
| `ralph-loop-setup.sh` | Initializes a new Ralph loop, creates state file |
| `ralph-loop-stop-hook.sh` | Stop hook that blocks exit and re-injects prompt |
| `cancel-ralph.sh` | Cancels an active Ralph loop |
| `README.md` | This documentation |

## State File

Location: `~/.claude/ralph-wiggum/loop-state.md`

Format:
```yaml
---
session_id: 20251228-143022-12345
iteration: 0
max_iterations: 50
completion_promise: "COMPLETE"
started_at: 2025-12-28T14:30:22
active: true
---

[Original prompt here]
```

## Commands

### /ralph-loop

Start a persistence loop:

```bash
/ralph-loop "Build a REST API with tests.
Run tests after each change.
Fix failing tests.
Output <promise>DONE</promise> when ALL tests pass." \
  --completion-promise "DONE" \
  --max-iterations 30
```

### /cancel-ralph

Cancel an active loop:

```bash
/cancel-ralph
```

## Integration with Context Cascade

### Hook Chain

The Ralph stop hook runs FIRST in the Stop hook chain:

1. `ralph-loop-stop-hook.sh` - Check for active loop, block if needed
2. `state-tracker.sh check_compliance` - Existing compliance check
3. Session ending reminders

### Compatibility with 5-Phase Workflow

Ralph loops work best AFTER Phase 4 (routing):

```
Phase 1: Intent Analysis
Phase 2: Prompt Optimization
Phase 3: Planning
Phase 4: Routing
Phase 5: Execution with /ralph-loop for iterative tasks
```

### Integration with Three-Loop System

| Three-Loop | Ralph Integration |
|------------|-------------------|
| Loop 1: Planning | Use 5-phase for planning |
| Loop 2: Implementation | Ralph handles single-agent iteration |
| Loop 3: CI/CD Recovery | Ralph can drive fix-until-pass loops |

## Best Practices

### 1. Always Set Max Iterations

```bash
# ALWAYS include --max-iterations
/ralph-loop "..." --max-iterations 25
```

### 2. Use Verifiable Completion Criteria

Good:
- Tests pass
- Linter clean
- Coverage > 80%

Bad:
- "Make it good"
- "Improve quality"
- "Fix issues"

### 3. Include Self-Correction Instructions

```
If tests fail, debug and fix.
If linter errors, resolve them.
If blocked, document why.
```

### 4. Use XML Tags for Promise

```
Output <promise>COMPLETE</promise> when done.
```

## Troubleshooting

### Loop Not Activating

1. Check state file exists: `cat ~/.claude/ralph-wiggum/loop-state.md`
2. Verify `active: true` in frontmatter
3. Check Stop hook is configured in settings.json

### Loop Not Stopping

1. Verify completion promise matches exactly
2. Check iteration count vs max_iterations
3. Use `/cancel-ralph` to force stop

### Windows Compatibility

- Requires bash (Git Bash, WSL, or similar)
- State files use Unix line endings
- Paths use forward slashes in bash

## History Log

Location: `~/.claude/ralph-wiggum/loop-history.log`

Records:
- Loop starts
- Iteration counts
- Completion events
- Cancellations

## Credits

Based on Anthropic's official Ralph Wiggum plugin for Claude Code.
Original technique by Geoffrey Huntley: https://ghuntley.com/ralph/

## Sources

- [Anthropic Claude Code Ralph Wiggum Plugin](https://github.com/anthropics/claude-code/tree/main/plugins/ralph-wiggum)
- [Ralph Wiggum Autonomous Loops Article](https://paddo.dev/blog/ralph-wiggum-autonomous-loops/)
- [Claude Code Hooks Documentation](https://code.claude.com/docs/en/hooks)
