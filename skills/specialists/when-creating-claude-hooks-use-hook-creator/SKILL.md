---
name: hook-creator
description: Create Claude Code hooks with proper schemas, RBAC integration, and performance requirements. Use when implementing PreToolUse, PostToolUse, SessionStart, or any of the 10 hook event types for automation, validation, or security enforcement.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
---

# SKILL: Hook Creator

## Purpose

Create production-ready Claude Code hooks that integrate with our RBAC security system,
follow official schemas, and meet performance requirements (<20ms for pre-hooks).

## When to Use This Skill

- Creating new automation hooks (pre/post operations)
- Implementing security validation hooks
- Building audit/logging hooks
- Extending the RBAC permission system
- Adding custom session management hooks

## 8-Stage Hook Creation Methodology

### Stage 1: Hook Type Selection

Identify which of the 10 hook event types you need:

| Category | Hook Type | Purpose |
|----------|-----------|---------|
| **Blocking** | UserPromptSubmit | Validate/modify user prompts |
| **Blocking** | SessionStart | Initialize session state |
| **Blocking** | PreToolUse | Validate tool operations |
| **Blocking** | PermissionRequest | Auto-approve/deny permissions |
| **Observational** | PostToolUse | Log tool results |
| **Observational** | Notification | Forward notifications |
| **Observational** | Stop | Cleanup on agent stop |
| **Observational** | SubagentStop | Track subagent completion |
| **Observational** | PreCompact | Preserve context during compaction |
| **Observational** | SessionEnd | Final session cleanup |

### Stage 2: Schema Definition

Define input/output schemas based on hook type.

**PreToolUse Input**:
```json
{
  "session_id": "string",
  "tool_name": "Bash|Read|Write|Edit|...",
  "tool_input": { "...tool-specific..." }
}
```

**Blocking Output**:
```json
{
  "continue": true|false,
  "decision": "approve|block|modify",
  "reason": "string (if blocked)",
  "suppressOutput": false,
  "updatedInput": { "..." }
}
```

**Non-Blocking Output**:
```json
{
  "suppressOutput": false
}
```

### Stage 3: Template Selection

Use our pre-built templates:

- `pre-hook-template.js` - For blocking hooks (PreToolUse, UserPromptSubmit)
- `post-hook-template.js` - For observational hooks (PostToolUse, SessionEnd)
- `session-hook-template.js` - For session lifecycle hooks

Generate from templates:
```bash
node hook-template-generator.js --type pre --name my-validator --event PreToolUse
```

### Stage 4: Core Logic Implementation

Implement the hook's core logic:

```javascript
#!/usr/bin/env node
const fs = require('fs');

// Read input from stdin
const input = JSON.parse(fs.readFileSync(0, 'utf-8'));

// Your validation/processing logic
function processHook(input) {
  // Implement your logic here
  return { continue: true, decision: "approve" };
}

// Execute and output result
try {
  const result = processHook(input);
  console.log(JSON.stringify(result));
} catch (error) {
  console.error(`[HOOK ERROR] ${error.message}`);
  console.log(JSON.stringify({ continue: true }));  // Fail open
  process.exit(1);
}
```

### Stage 5: RBAC Integration

For security hooks, integrate with our identity system:

```javascript
const { validateAgentIdentity, loadAgentIdentityByName } = require('../utils/identity');

// Verify agent identity
const identity = loadAgentIdentityByName(input.agent_name);
const validation = validateAgentIdentity(identity);

if (!validation.valid) {
  return {
    continue: false,
    decision: "block",
    reason: `Invalid agent identity: ${validation.errors.join(', ')}`
  };
}
```

### Stage 6: Performance Optimization

Meet performance targets:

| Hook Type | Target | Max |
|-----------|--------|-----|
| Pre-hooks | <20ms | 100ms |
| Post-hooks | <100ms | 1000ms |

**Optimization Patterns**:
- Cache identity lookups
- Avoid synchronous I/O in hot paths
- Use matchers to filter events
- Batch logging operations

### Stage 7: Testing

Create test scenarios:

```javascript
// test-my-hook.js
const testCases = [
  {
    name: "Should approve valid operation",
    input: { tool_name: "Read", tool_input: { file_path: "/src/app.js" } },
    expectedOutput: { continue: true, decision: "approve" }
  },
  {
    name: "Should block dangerous command",
    input: { tool_name: "Bash", tool_input: { command: "rm -rf /" } },
    expectedOutput: { continue: false, decision: "block" }
  }
];
```

### Stage 8: Registration

Register in settings.json:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "type": "command",
        "command": "node /path/to/your/hook.js",
        "timeout": 5000,
        "matcher": { "tool_name_regex": "^(Bash|Write|Edit)$" }
      }
    ]
  }
}
```

## Hook Templates

### Pre-Hook Template (Blocking)

Location: `resources/templates/pre-hook-template.js`

Features:
- Input validation
- Error handling with fail-open
- Performance timing
- RBAC integration point

### Post-Hook Template (Observational)

Location: `resources/templates/post-hook-template.js`

Features:
- Async-safe logging
- Metric collection
- Non-blocking execution
- Error isolation

## Output Artifacts

1. `{hook-name}.js` - Main hook script
2. `{hook-name}.test.js` - Test file
3. Settings entry for `.claude/settings.json`

## Integration Points

- **RBAC System**: `hooks/12fa/utils/identity.js`
- **Permission Checker**: `hooks/12fa/permission-checker.js`
- **Budget Tracker**: `hooks/12fa/budget-tracker.js`
- **Reference Docs**: `hooks/12fa/docs/CLAUDE-CODE-HOOKS-REFERENCE.md`

## Agents Used

| Agent | Role |
|-------|------|
| hook-creator | Generate hook code from templates |
| coder | Implement custom logic |
| reviewer | Validate hook implementation |
| tester | Create and run test scenarios |

## Example Invocations

**Create a command validator hook**:
```
User: "Create a hook that blocks any Bash command containing 'sudo'"

hook-creator:
  1. Hook Type: PreToolUse (blocking)
  2. Schema: PreToolUse input, blocking output
  3. Template: pre-hook-template.js
  4. Logic: Check tool_input.command for 'sudo'
  5. RBAC: Not required (simple validation)
  6. Performance: Target <10ms (regex only)
  7. Tests: Valid command, sudo command, edge cases
  8. Register in settings.json with Bash matcher
```

**Create an audit logging hook**:
```
User: "Create a hook that logs all file writes to an audit trail"

hook-creator:
  1. Hook Type: PostToolUse (observational)
  2. Schema: PostToolUse input, non-blocking output
  3. Template: post-hook-template.js
  4. Logic: Append to audit JSONL file
  5. RBAC: Load agent identity for WHO tag
  6. Performance: Target <50ms (file append)
  7. Tests: Successful write, failed write, large file
  8. Register with Write/Edit matcher
```

## Security Considerations

1. **Never log sensitive data** - Filter passwords, API keys, tokens
2. **Validate all input** - Treat hook input as untrusted
3. **Fail open for non-security hooks** - Don't block on errors
4. **Fail closed for security hooks** - Block on validation errors
5. **Use absolute paths** - Avoid path traversal vulnerabilities

## Performance Monitoring

Add performance logging to all hooks:

```javascript
const start = process.hrtime.bigint();
// ... hook logic ...
const durationMs = Number(process.hrtime.bigint() - start) / 1_000_000;
console.error(`[PERF] ${hookName} completed in ${durationMs.toFixed(2)}ms`);
```

## Related Skills

- `hooks-automation` - General hook automation patterns
- `cicd-intelligent-recovery` - Error recovery patterns
- `cascade-orchestrator` - Multi-hook coordination

---

*Last Updated: 2025-12-30*
*Integrated with: Claude Code Hooks v1.0.0*
