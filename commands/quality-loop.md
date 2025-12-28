# /quality-loop

## Description
Start a quality-gated Ralph Wiggum persistence loop with Connascence Safety Analyzer integration. Code is automatically audited after each change, and the loop continues until all quality issues are resolved.

## Usage
```
/quality-loop "<task description>" [--max-iterations N] [--promise "<text>"]
```

## Arguments
- `task`: The task to complete (required)
- `--max-iterations`: Maximum loop iterations (default: 25)
- `--promise`: Custom completion promise (default: CODE_QUALITY_PASSED)

## Examples

### Basic Usage
```
/quality-loop "Implement user authentication with JWT tokens"
```

### With Custom Settings
```
/quality-loop "Refactor database module for clean code" --max-iterations 30 --promise "REFACTOR_COMPLETE"
```

### TDD Loop
```
/quality-loop "Build REST API endpoints with full test coverage. Run tests after each change."
```

## How It Works

1. **Initialize**: Creates loop state with quality_gate: true
2. **Work**: You write/edit code normally
3. **Audit**: Each file change triggers Connascence analyzer
4. **Feedback**: If issues found, they're shown in the output
5. **Loop**: If quality gate fails, loop continues automatically
6. **Complete**: When quality passes AND you output the promise

## Quality Thresholds

| Severity | Threshold | Blocking |
|----------|-----------|----------|
| CRITICAL | 0 allowed | YES |
| HIGH | Max 3 | YES (if exceeded) |
| MEDIUM | Unlimited | NO |
| LOW | Unlimited | NO |

## Files Created

- `~/.claude/ralph-wiggum/loop-state.md` - Loop state
- `~/.claude/connascence-audit/latest-results.json` - Audit results
- `~/.claude/connascence-audit/pending-issues.md` - Issues to fix

## Related Commands

- `/ralph-loop` - Base persistence loop (without quality gate)
- `/cancel-ralph` - Cancel active loop
- `/audit-code` - Run one-time audit

## Implementation

This command invokes:
```bash
bash ~/.claude/hooks/connascence-audit/setup-quality-loop.sh "<task>" <max_iterations> "<promise>"
```

And uses the enhanced stop hook:
```bash
~/.claude/hooks/ralph-wiggum/quality-gate-stop-hook.sh
```
