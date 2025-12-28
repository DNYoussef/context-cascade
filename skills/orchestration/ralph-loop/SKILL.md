---
name: ralph-loop
description: Persistence loop system that prevents premature task completion by using Stop hooks to re-inject prompts until success criteria are met. Named after Ralph Wiggum from The Simpsons. Use for iterative tasks requiring continuous refinement until tests pass or goals achieved.
version: 1.0.0
category: orchestration
tags:
  - orchestration
  - persistence
  - iteration
  - automation
  - tdd
author: Context Cascade (integrated from Anthropic's Ralph Wiggum plugin)
---

# Ralph Loop (Persistence Loop System)

An orchestration skill that implements continuous self-referential AI loops for iterative development until task completion.

## SKILL-SPECIFIC GUIDANCE

### When to Use This Skill

- Tasks with clear, binary success criteria (tests pass/fail)
- Iterative refinement tasks (TDD, test coverage, linting)
- Greenfield development where you can "walk away"
- Tasks requiring multiple attempts to get right
- Automated verification is possible (tests, linters, compilers)

### When NOT to Use This Skill

- Tasks requiring human judgment or design decisions
- One-shot operations with no iteration needed
- Tasks with unclear or subjective success criteria
- Production debugging (need human oversight)
- When max iterations would be reached quickly

### Success Criteria

- Task completes with completion promise output
- All automated checks pass (tests, linters)
- Work persists in files after loop ends
- Iteration count within max-iterations limit

### Edge Cases & Limitations

- Exact string matching only for completion promise
- Cannot handle subjective "quality" assessments
- May get stuck if task is truly impossible
- Windows requires bash/git-bash environment

### Critical Guardrails

- ALWAYS set --max-iterations (never run unlimited)
- ALWAYS define clear completion criteria
- NEVER use for tasks requiring human approval
- ALWAYS have escape hatch in prompt ("if blocked, document why")

## Core Concept

Ralph Loop creates a self-referential feedback loop:

```
1. User runs /ralph-loop once with task
2. Claude works on task
3. Claude tries to exit
4. Stop hook intercepts exit
5. If completion promise NOT found:
   - Increment iteration
   - Re-inject same prompt
   - Loop continues
6. If completion promise found OR max iterations:
   - Allow exit
   - Report results
```

## How It Works Under the Hood

### State File
Location: `~/.claude/ralph-wiggum/loop-state.md`

```yaml
---
session_id: 20251228-143022-12345
iteration: 3
max_iterations: 50
completion_promise: "COMPLETE"
started_at: 2025-12-28T14:30:22
active: true
---

[Original prompt here]
```

### Stop Hook Mechanism

The Stop hook (`ralph-loop-stop-hook.sh`):
1. Checks if loop is active
2. Validates iteration < max_iterations
3. Searches output for `<promise>TEXT</promise>` pattern
4. If not complete: exits with code 2 (blocks exit)
5. Re-injects original prompt with iteration info

## Integration with Three-Loop System

Ralph Loop complements the Three-Loop system:

| Loop | Purpose | Ralph Integration |
|------|---------|-------------------|
| Loop 1: Planning | Research-driven planning | N/A (planning phase) |
| Loop 2: Implementation | Parallel swarm execution | Ralph handles single-agent iteration |
| Loop 3: CI/CD | Intelligent recovery | Ralph can drive fix-until-pass loops |

### Recommended Pattern

```
Phase 1-4: Use 5-phase workflow for planning
Phase 5: Use /ralph-loop for persistent execution
```

## Commands

### /ralph-loop

Start a persistence loop.

```bash
/ralph-loop "<prompt>" --max-iterations N --completion-promise "<text>"
```

### /cancel-ralph

Cancel active loop.

```bash
/cancel-ralph
```

## Prompt Templates

### TDD Loop

```
Implement [FEATURE] using TDD:

1. Write failing tests first
2. Implement minimum code to pass
3. Run tests
4. If any fail, debug and fix
5. Refactor if needed
6. Repeat until all green

Output <promise>TESTS_PASS</promise> when ALL tests pass.
```

### Coverage Loop

```
Write tests for [MODULE] until coverage reaches [TARGET]%.

After each test:
1. Run coverage report
2. Identify uncovered lines
3. Write tests for uncovered code

Output <promise>COVERAGE_MET</promise> when target reached.
```

### Linting Loop

```
Fix all linting errors in [DIRECTORY].

After each fix:
1. Run linter
2. Check remaining errors
3. Fix next error

Output <promise>LINT_CLEAN</promise> when no errors remain.
```

### Refactoring Loop

```
Refactor [MODULE] to address these issues:
- [Issue 1]
- [Issue 2]
- [Issue 3]

After each change:
1. Run tests (must stay green)
2. Check for remaining issues

Output <promise>REFACTORED</promise> when all issues resolved.
```

## Philosophy

Four key principles:

1. **Iteration > Perfection** - Don't aim for perfect on first try; let the loop refine
2. **Failures Are Data** - Use test failures as information for next attempt
3. **Operator Skill Matters** - Success depends on writing good prompts
4. **Persistence Wins** - Keep trying until success; the loop handles retries

## Real-World Results

From the original Ralph technique:
- 6 repositories shipped overnight (YC hackathon)
- $50k contract completed for $297 in API costs
- Entire programming language built over 3 months

## Anti-Patterns

| Anti-Pattern | Why It Fails | Correct Approach |
|--------------|--------------|------------------|
| No max-iterations | Infinite loop risk | Always set --max-iterations 20-50 |
| Vague completion | Can't verify programmatically | Use tests, linters as criteria |
| "Make it good" prompts | Subjective, unverifiable | Define specific success criteria |
| Missing escape hatch | Gets stuck forever | Include "if blocked, document why" |

## Installation

The Ralph Loop system is integrated into Context Cascade via:

1. Stop hook: `hooks/ralph-wiggum/ralph-loop-stop-hook.sh`
2. Setup script: `hooks/ralph-wiggum/ralph-loop-setup.sh`
3. Cancel script: `hooks/ralph-wiggum/cancel-ralph.sh`
4. Commands: `commands/orchestration/ralph-loop.md`, `cancel-ralph.md`

## Activation

Add to Stop hook in settings.json:
```json
"Stop": [
  {
    "hooks": [
      {
        "type": "command",
        "command": "bash .claude/hooks/ralph-wiggum/ralph-loop-stop-hook.sh"
      }
    ]
  }
]
```

---

## Conclusion

Ralph Loop transforms Claude from a tool that "tries once and gives up" into a persistent loop that keeps iterating until success. It's ideal for well-defined tasks with automated verification, enabling true "fire and forget" development workflows.
