---
name: cancel-ralph
description: Cancel an active Ralph Wiggum persistence loop
category: orchestration
aliases:
  - /stop-ralph
  - /ralph-cancel
allowed_tools:
  - Bash
---

# /cancel-ralph

Cancel an active Ralph Wiggum persistence loop.

## Usage

```bash
/cancel-ralph
```

## What It Does

1. Marks the active loop as inactive
2. Logs the cancellation to history
3. Allows normal session exit

## When to Use

- Task is impossible to complete
- You want to change the prompt
- Loop is stuck in an unproductive cycle
- You need to take over manually

## Example

```bash
# Start a loop
/ralph-loop "Build feature X" --max-iterations 20

# ... after some iterations, decide to cancel
/cancel-ralph

# Now you can exit normally or start a new loop
```

## Alternative Method

You can also cancel by running the script directly:

```bash
bash ~/.claude/hooks/ralph-wiggum/cancel-ralph.sh
```

## Notes

- Canceling preserves all work done in files
- Git history shows all iterations
- You can review progress before deciding next steps
