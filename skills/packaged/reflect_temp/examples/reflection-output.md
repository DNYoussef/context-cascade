# Reflection Output Examples

## Example 1: Correction Detection (HIGH Confidence)

### Session Fragment
```
User: Fix the login bug
Claude: I'll add a try-catch around the auth call...
User: No, don't wrap it in try-catch. Use the error boundary at the component level instead.
Claude: You're right, using the ErrorBoundary component is cleaner...
```

### Detected Learning
```yaml
signal_type: correction
confidence: 0.90 (HIGH)
evidence: "No, don't" + alternative provided
skill_target: fix-bug
learning: |
  PATTERN: Error handling in React components
  RULE: Use ErrorBoundary at component level rather than try-catch in async calls
  CONTEXT: React error handling, auth flows
  SOURCE: User correction [session:2026-01-05-abc123]
action: requires_approval
```

### Skill Update (After Approval)
```markdown
## LEARNED PATTERNS

### Error Handling in React (2026-01-05)
- Use ErrorBoundary at component level for React error handling
- Avoid try-catch wrapping for async auth calls
- Source: User correction [conf:0.90]
```

---

## Example 2: Approval Pattern (MEDIUM Confidence)

### Session Fragment
```
User: Write a test for the user service
Claude: I'll create a test file with describe blocks...

[Test code written]

User: Perfect, that's exactly the structure I wanted
```

### Detected Learning
```yaml
signal_type: approval
confidence: 0.75 (MEDIUM)
evidence: "Perfect" + "exactly"
skill_target: tester
learning: |
  PATTERN: Test structure for services
  RULE: Use describe/it blocks with setup/teardown
  CONTEXT: Unit testing, service layer
  SOURCE: User approval [session:2026-01-05-abc123]
action: auto_apply
```

### Skill Update (Auto-Applied)
```markdown
## LEARNED PATTERNS

### Service Test Structure (2026-01-05)
- User preference: describe/it blocks with setup/teardown
- Apply to: service layer unit tests
- Source: User approval [conf:0.75]
```

---

## Example 3: Explicit Rule (MEDIUM-HIGH Confidence)

### Session Fragment
```
User: When writing Python code, always use type hints
Claude: Understood, I'll include type annotations...
```

### Detected Learning
```yaml
signal_type: explicit_rule
confidence: 0.85 (MEDIUM-HIGH)
evidence: "always" directive
skill_target: code
learning: |
  PATTERN: Python code style
  RULE: Always include type hints in Python code
  CONTEXT: Python development, this user's projects
  SOURCE: Explicit user directive [session:2026-01-05-abc123]
action: auto_apply
```

---

## Example 4: Observation Pattern (LOW Confidence)

### Session Fragment
```
[User consistently asks for bullet points in summaries]
[No explicit statement, just repeated pattern]
```

### Detected Learning
```yaml
signal_type: observation
confidence: 0.55 (LOW)
evidence: 3+ occurrences in session
skill_target: documenter
learning: |
  PATTERN: Summary format preference
  RULE: User prefers bullet points in summaries
  CONTEXT: Documentation, summaries
  SOURCE: Behavioral observation [session:2026-01-05-abc123]
action: auto_apply
```

---

## Example 5: Rejection Signal (NEGATIVE)

### Session Fragment
```
User: Don't add comments to every line
Claude: I'll reduce the comment density...
```

### Detected Learning
```yaml
signal_type: rejection
confidence: 0.80 (MEDIUM-HIGH)
evidence: "Don't" directive
skill_target: code
learning: |
  PATTERN: Comment density
  ANTI-RULE: Avoid excessive line-by-line comments
  CONTEXT: Code style
  SOURCE: User rejection [session:2026-01-05-abc123]
action: auto_apply
```

---

## Reflection Summary Output

After `/reflect` completes, output looks like:

```
==========================================
   REFLECTION COMPLETE
==========================================

Learnings Captured: 5
- HIGH confidence (requires approval): 1
- MEDIUM confidence (auto-applied): 3
- LOW confidence (auto-applied): 1

Skills Updated:
- fix-bug: 1 pattern added (pending approval)
- tester: 1 pattern added
- code: 2 patterns added
- documenter: 1 pattern added

Memory MCP Tags:
- sessions/reflect/context-cascade/2026-01-05

Next Actions:
- Review HIGH confidence learning in fix-bug skill
- Run /reflect-status to see full history

==========================================
```

---

## Memory MCP Storage Format

```json
{
  "WHO": "reflect-skill:session-2026-01-05-abc123",
  "WHEN": "2026-01-05T15:30:00Z",
  "PROJECT": "context-cascade",
  "WHY": "skill-improvement",
  "learnings": [
    {
      "signal_type": "correction",
      "confidence": 0.90,
      "skill": "fix-bug",
      "pattern": "Error handling in React components",
      "rule": "Use ErrorBoundary at component level",
      "status": "pending_approval"
    }
  ]
}
```

---

Confidence: 0.88 (ceiling: observation 0.95) - Example documentation.
