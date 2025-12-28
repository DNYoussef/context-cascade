# SKILL: connascence-quality-gate

## METADATA
- **Name**: Connascence Quality Gate
- **Category**: quality
- **Version**: 1.0.0
- **Triggers**: "quality gate", "code audit", "connascence check", "perfect code", "code quality loop"
- **Dependencies**: ralph-loop, connascence-analyzer
- **MCP Servers**: memory-mcp (optional)

## PURPOSE

Integrates the Connascence Safety Analyzer with the Ralph Wiggum persistence loop to create an automated code quality feedback system. Code is audited after each change, and the loop continues until all quality issues are resolved.

## WHEN TO USE

- After completing any code task to verify quality
- During TDD/refactoring loops to ensure code stays clean
- Before marking a task as complete
- When user wants "perfect" code with no violations

## CORE CONCEPT

```
Write Code -> Audit -> Issues Found? -> Fix -> Repeat
                 |
                 v (No Issues)
            Mark Complete
```

## STANDARD OPERATING PROCEDURE

### Phase 1: Initialize Quality Loop (30s)

1. **Setup State**
   ```bash
   mkdir -p ~/.claude/connascence-audit
   mkdir -p ~/.claude/ralph-wiggum
   ```

2. **Configure Loop**
   ```yaml
   # ~/.claude/ralph-wiggum/loop-state.md
   ---
   session_id: quality-gate-{timestamp}
   active: true
   iteration: 0
   max_iterations: 25
   quality_gate: true
   completion_promise: "CODE_QUALITY_PASSED"
   ---
   {original task prompt}
   ```

3. **Enable Hooks**
   - PostToolUse:Write/Edit runs connascence audit
   - Stop hook checks quality gate before allowing exit

### Phase 2: Development Loop (iterative)

For each iteration:

1. **Write/Edit Code**
   - Implement feature or fix
   - Save changes to file

2. **Automatic Audit** (triggered by hook)
   ```python
   from analyzer.core import ConnascenceAnalyzer
   analyzer = ConnascenceAnalyzer()
   result = analyzer.analyze_path(file_path, policy='strict-core')
   ```

3. **Quality Check**
   - CRITICAL violations: MUST fix immediately
   - HIGH violations: Max 3 allowed
   - MEDIUM/LOW: Recommendations only

4. **Feedback Loop**
   - If issues found: Show violations, continue loop
   - If clean: Allow completion promise

### Phase 3: Completion (when quality passes)

1. **All checks pass**:
   ```
   <promise>CODE_QUALITY_PASSED</promise>
   ```

2. **Quality Gate verified**:
   - No critical violations
   - Max 3 high violations
   - Connascence score > 80%

## INTEGRATION COMMANDS

### Start Quality Gate Loop

```bash
/ralph-loop "Implement {feature} with production-quality code.

QUALITY REQUIREMENTS:
- No critical connascence violations
- Max 3 high-severity issues
- All tests must pass

The Connascence Safety Analyzer will audit your code after each change.
Fix all issues before completing.

Output <promise>CODE_QUALITY_PASSED</promise> when quality gate passes." \
  --completion-promise "CODE_QUALITY_PASSED" \
  --max-iterations 25 \
  --quality-gate true
```

### Manual Audit

```bash
cd D:/Projects/connascence
python -c "
from analyzer.core import ConnascenceAnalyzer
analyzer = ConnascenceAnalyzer()
result = analyzer.analyze_path('path/to/file.py', policy='strict-core')
print(f'Violations: {len(result.get(\"violations\", []))}')
"
```

### View Audit Results

```bash
cat ~/.claude/connascence-audit/latest-results.json | jq .
cat ~/.claude/connascence-audit/pending-issues.md
```

## QUALITY THRESHOLDS

| Severity | Threshold | Blocking |
|----------|-----------|----------|
| CRITICAL | 0 allowed | YES |
| HIGH | Max 3 | YES (if > 3) |
| MEDIUM | Unlimited | NO |
| LOW | Unlimited | NO |

## VIOLATION TYPES CHECKED

The Connascence Safety Analyzer detects:

1. **CoM (Connascence of Meaning)**: Magic literals
2. **CoP (Connascence of Position)**: Parameter bombs (>4 params)
3. **CoA (Connascence of Algorithm)**: Duplicated logic
4. **God Objects**: Classes with >15 methods
5. **NASA Rule Violations**: Deep nesting, long functions
6. **Cyclomatic Complexity**: >10 complexity score

## EXAMPLE WORKFLOW

```
User: "Build a user authentication module with perfect code quality"

Claude:
1. Skill("connascence-quality-gate")
2. Initialize Ralph loop with quality_gate: true
3. Write initial auth.py
4. [Hook triggers audit]
5. Found: 2 magic literals (CoM), 1 param bomb (CoP)
6. Fix violations
7. [Hook triggers audit]
8. Found: 0 violations
9. <promise>CODE_QUALITY_PASSED</promise>
10. Loop exits successfully
```

## FILES

- Hook: `~/.claude/hooks/connascence-audit/run-audit.sh`
- Stop Hook: `~/.claude/hooks/ralph-wiggum/quality-gate-stop-hook.sh`
- Results: `~/.claude/connascence-audit/latest-results.json`
- Issues: `~/.claude/connascence-audit/pending-issues.md`
- State: `~/.claude/ralph-wiggum/loop-state.md`

## RELATED SKILLS

- `ralph-loop`: Base persistence loop
- `clarity-linter`: Cognitive load analysis
- `code-review-assistant`: Multi-agent review
- `testing-quality`: Test coverage verification

## SUCCESS CRITERIA

- All code changes automatically audited
- Quality issues surfaced immediately
- Loop continues until quality passes
- Final code has 0 critical, <=3 high violations
- Completion promise only accepted when quality gate passes
