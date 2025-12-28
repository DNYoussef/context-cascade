---
name: ralph-loop
description: Start a Ralph Wiggum persistence loop that iterates until task completion
category: orchestration
aliases:
  - /raffloop
  - /ralph
allowed_tools:
  - Bash
---

# /ralph-loop

Start a Ralph Wiggum persistence loop in the current session.

## Usage

```bash
/ralph-loop "<prompt>" [--max-iterations N] [--completion-promise "<text>"]
```

## Options

| Option | Default | Description |
|--------|---------|-------------|
| `--max-iterations` | 50 | Maximum iterations before forced stop (safety limit) |
| `--completion-promise` | (none) | Exact text that signals task completion |

## How It Works

1. You run `/ralph-loop` ONCE with your task
2. Claude works on the task
3. When Claude tries to exit, the Stop hook intercepts
4. If completion promise not found, prompt is re-injected
5. Loop continues until: promise found OR max iterations reached

The prompt NEVER changes between iterations. Claude sees:
- Modified files from previous iterations
- Git history of changes
- Test outputs and error messages

## Examples

### Basic Loop (Tests Must Pass)

```bash
/ralph-loop "Build a REST API for user management.
Requirements:
- CRUD operations for users
- Input validation
- Comprehensive tests
- Run tests after each change
- Fix any failing tests
Do not stop until ALL tests pass.
Output <promise>COMPLETE</promise> when done." --completion-promise "COMPLETE" --max-iterations 30
```

### Test Coverage Loop

```bash
/ralph-loop "Write unit tests until code coverage reaches 80%.
Run coverage report after each test addition.
Output <promise>COVERAGE_MET</promise> when 80% is achieved." --completion-promise "COVERAGE_MET" --max-iterations 20
```

### Refactoring Loop

```bash
/ralph-loop "Refactor this module to remove all code smells.
After each change:
1. Run linter
2. Run tests
3. Check for remaining issues
Output <promise>CLEAN</promise> when no issues remain." --completion-promise "CLEAN" --max-iterations 15
```

## Prompt Best Practices

### 1. Clear Completion Criteria
Define exactly what "done" means:
- Tests passing (coverage > 80%)
- Linter clean
- All endpoints working
- Documentation complete

### 2. Self-Correction Instructions
Tell Claude to fix its own mistakes:
```
If tests fail, debug and fix.
If linter errors, resolve them.
If blocked, document why.
```

### 3. Always Use Max Iterations
Never run without a safety limit:
```bash
/ralph-loop "..." --max-iterations 25
```

### 4. Completion Promise Format
Use XML tags for the promise:
```
Output <promise>DONE</promise> when complete.
```

## Canceling

To stop an active loop:
```bash
/cancel-ralph
```

## Integration with 5-Phase Workflow

Ralph loops can be used AFTER Phase 4 (routing) for execution:

1. Phase 1-4: Plan and route the task
2. Phase 5: Use `/ralph-loop` for persistent execution
3. The loop handles iteration, testing, and debugging

## Philosophy

> "Iteration > Perfection" - Don't aim for perfect on first try
> "Failures Are Data" - Use test output to refine work
> "Persistence Wins" - The loop handles retry logic automatically

## When to Use

**Good for:**
- Well-defined tasks with clear success criteria
- Tasks requiring iteration (TDD, test coverage)
- Greenfield projects
- Tasks with automatic verification

**Not for:**
- Tasks requiring human judgment
- One-shot operations
- Unclear success criteria
- Production debugging

## State Files

- Loop state: `~/.claude/ralph-wiggum/loop-state.md`
- History log: `~/.claude/ralph-wiggum/loop-history.log`
