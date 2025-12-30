# Claude Code Hooks Reference

## Overview

Claude Code hooks are executable scripts that run at specific points during Claude Code's
execution lifecycle. They enable automation, validation, logging, and custom behavior
without modifying Claude Code itself.

**Version**: 1.0.0
**Last Updated**: 2025-12-30
**Source**: Claude Code Official Documentation

---

## Table of Contents

1. [Hook Configuration](#hook-configuration)
2. [Hook Events (10 Types)](#hook-events)
3. [Input/Output Schemas](#inputoutput-schemas)
4. [Hook Execution Lifecycle](#hook-execution-lifecycle)
5. [Best Practices](#best-practices)
6. [Integration with RBAC System](#integration-with-rbac-system)
7. [Error Handling](#error-handling)
8. [Performance Requirements](#performance-requirements)

---

## Hook Configuration

Hooks are configured in `.claude/settings.json` or `.claude/settings.local.json`:

```json
{
  "hooks": {
    "UserPromptSubmit": [
      {
        "type": "command",
        "command": "node /path/to/hook.js",
        "timeout": 5000
      }
    ],
    "PreToolUse": [
      {
        "type": "command",
        "command": "python /path/to/validate.py",
        "timeout": 3000,
        "matcher": {
          "tool_name": "Bash"
        }
      }
    ]
  }
}
```

### Configuration Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `type` | string | Yes | Always "command" |
| `command` | string | Yes | Shell command to execute |
| `timeout` | number | No | Max execution time in ms (default: 60000) |
| `matcher` | object | No | Filter when hook runs (see Matchers) |

### Matchers

Matchers filter which events trigger the hook:

```json
{
  "matcher": {
    "tool_name": "Bash",
    "tool_name_regex": "^(Read|Write|Edit)$",
    "session_id": "specific-session-id"
  }
}
```

| Matcher Field | Description |
|---------------|-------------|
| `tool_name` | Exact tool name match |
| `tool_name_regex` | Regex pattern for tool name |
| `session_id` | Specific session ID |

---

## Hook Events

Claude Code supports 10 hook event types, divided into blocking and non-blocking categories.

### Blocking Hooks (Can Halt Execution)

These hooks can prevent operations from proceeding by returning `continue: false`.

#### 1. UserPromptSubmit

**When**: Before user prompt is processed by Claude.

**Use Cases**:
- Validate prompt content
- Add context/instructions
- Block inappropriate requests
- Log user interactions

**Input Schema**:
```json
{
  "session_id": "string",
  "prompt": "string",
  "tool_results": [
    {
      "tool_name": "string",
      "result": "any"
    }
  ]
}
```

**Output Schema**:
```json
{
  "continue": true,
  "decision": "approve",
  "reason": "string (optional)",
  "suppressOutput": false
}
```

**Example**:
```javascript
#!/usr/bin/env node
const input = JSON.parse(require('fs').readFileSync(0, 'utf-8'));

// Block prompts containing sensitive patterns
if (input.prompt.match(/password|secret|api.?key/i)) {
  console.log(JSON.stringify({
    continue: false,
    decision: "block",
    reason: "Prompt contains sensitive data patterns"
  }));
} else {
  console.log(JSON.stringify({ continue: true, decision: "approve" }));
}
```

---

#### 2. SessionStart

**When**: When a new Claude Code session is initialized.

**Use Cases**:
- Initialize session state
- Load user preferences
- Set up logging
- Verify environment

**Input Schema**:
```json
{
  "session_id": "string",
  "cwd": "string"
}
```

**Output Schema**:
```json
{
  "continue": true,
  "reason": "string (optional)",
  "suppressOutput": false
}
```

**Example**:
```javascript
#!/usr/bin/env node
const input = JSON.parse(require('fs').readFileSync(0, 'utf-8'));

// Log session start
console.error(`Session ${input.session_id} started in ${input.cwd}`);

// Allow session to continue
console.log(JSON.stringify({ continue: true }));
```

---

#### 3. PreToolUse

**When**: Before a tool (Read, Write, Bash, etc.) is invoked.

**Use Cases**:
- Validate tool inputs
- Check permissions
- Modify tool parameters
- Block dangerous operations

**Input Schema**:
```json
{
  "session_id": "string",
  "tool_name": "string",
  "tool_input": {
    "command": "string (for Bash)",
    "file_path": "string (for Read/Write/Edit)",
    "content": "string (for Write)",
    "old_string": "string (for Edit)",
    "new_string": "string (for Edit)"
  }
}
```

**Output Schema**:
```json
{
  "continue": true,
  "decision": "approve|block|modify",
  "reason": "string (required if blocked)",
  "suppressOutput": false,
  "updatedInput": {
    "...modified tool_input fields..."
  }
}
```

**Decision Values**:
- `approve`: Allow tool execution as-is
- `block`: Prevent tool execution (requires reason)
- `modify`: Allow with modified input (requires updatedInput)

**Example**:
```javascript
#!/usr/bin/env node
const input = JSON.parse(require('fs').readFileSync(0, 'utf-8'));

// Block rm -rf commands
if (input.tool_name === 'Bash' &&
    input.tool_input.command.match(/rm\s+-rf/)) {
  console.log(JSON.stringify({
    continue: false,
    decision: "block",
    reason: "Dangerous command: rm -rf is blocked"
  }));
  process.exit(0);
}

// Block writes to system directories
if (input.tool_name === 'Write' &&
    input.tool_input.file_path.startsWith('/etc/')) {
  console.log(JSON.stringify({
    continue: false,
    decision: "block",
    reason: "Cannot write to /etc/ directory"
  }));
  process.exit(0);
}

console.log(JSON.stringify({ continue: true, decision: "approve" }));
```

---

#### 4. PermissionRequest

**When**: When Claude Code needs permission for an operation.

**Use Cases**:
- Auto-approve trusted operations
- Auto-deny untrusted operations
- Log permission requests
- Implement custom approval logic

**Input Schema**:
```json
{
  "session_id": "string",
  "tool_name": "string",
  "operation": "string",
  "permission_type": "string"
}
```

**Output Schema**:
```json
{
  "decision": "approve|deny",
  "reason": "string (optional)",
  "updatedInput": {}
}
```

**Example**:
```javascript
#!/usr/bin/env node
const input = JSON.parse(require('fs').readFileSync(0, 'utf-8'));

// Auto-approve read operations
if (input.tool_name === 'Read') {
  console.log(JSON.stringify({ decision: "approve" }));
  process.exit(0);
}

// Deny network operations
if (input.operation.includes('network')) {
  console.log(JSON.stringify({
    decision: "deny",
    reason: "Network operations require manual approval"
  }));
  process.exit(0);
}

// Default: let user decide
console.log(JSON.stringify({}));
```

---

### Non-Blocking Hooks (Observational)

These hooks observe execution but cannot halt it.

#### 5. PostToolUse

**When**: After a tool completes execution.

**Use Cases**:
- Log tool results
- Analyze output patterns
- Trigger follow-up actions
- Update metrics

**Input Schema**:
```json
{
  "session_id": "string",
  "tool_name": "string",
  "tool_input": {},
  "tool_response": {
    "stdout": "string",
    "stderr": "string",
    "exit_code": 0,
    "content": "string (for Read)",
    "success": true
  }
}
```

**Output Schema**:
```json
{
  "suppressOutput": false
}
```

**Example**:
```javascript
#!/usr/bin/env node
const fs = require('fs');
const input = JSON.parse(fs.readFileSync(0, 'utf-8'));

// Log to audit file
const logEntry = {
  timestamp: new Date().toISOString(),
  session: input.session_id,
  tool: input.tool_name,
  success: input.tool_response.success || input.tool_response.exit_code === 0
};

fs.appendFileSync('/var/log/claude-audit.jsonl',
  JSON.stringify(logEntry) + '\n');

console.log(JSON.stringify({ suppressOutput: false }));
```

---

#### 6. Notification

**When**: When Claude Code emits a notification.

**Use Cases**:
- Forward notifications to external systems
- Log notification events
- Trigger alerts
- Update dashboards

**Input Schema**:
```json
{
  "session_id": "string",
  "message": "string",
  "type": "info|warning|error",
  "timestamp": "string"
}
```

**Output Schema**:
```json
{
  "suppressOutput": false
}
```

---

#### 7. Stop

**When**: Main Claude agent stops execution.

**Use Cases**:
- Cleanup operations
- Save session state
- Generate summary reports
- Trigger post-execution workflows

**Input Schema**:
```json
{
  "session_id": "string",
  "reason": "completed|error|user_cancelled|context_limit",
  "final_message": "string"
}
```

**Output Schema**:
```json
{
  "suppressOutput": false
}
```

---

#### 8. SubagentStop

**When**: A subagent (spawned via Task tool) stops.

**Use Cases**:
- Track subagent completion
- Aggregate subagent results
- Handle subagent errors
- Update progress tracking

**Input Schema**:
```json
{
  "session_id": "string",
  "parent_id": "string",
  "subagent_id": "string",
  "reason": "completed|error|timeout",
  "result": "any"
}
```

**Output Schema**:
```json
{
  "suppressOutput": false
}
```

---

#### 9. PreCompact

**When**: Before context is compacted (summarized to save tokens).

**Use Cases**:
- Inject information into summary
- Preserve critical context
- Log compaction events
- Modify compaction strategy

**Input Schema**:
```json
{
  "session_id": "string",
  "context_size": 12000,
  "target_size": 8000
}
```

**Output Schema**:
```json
{
  "summary": "string (additional context to preserve)",
  "suppressOutput": false
}
```

**Example**:
```javascript
#!/usr/bin/env node
const input = JSON.parse(require('fs').readFileSync(0, 'utf-8'));

// Add critical context that should survive compaction
const criticalContext = `
PRESERVE: Current working directory is a monorepo.
PRESERVE: User prefers TypeScript over JavaScript.
PRESERVE: All tests must pass before committing.
`;

console.log(JSON.stringify({
  summary: criticalContext,
  suppressOutput: false
}));
```

---

#### 10. SessionEnd

**When**: Session is ending (cleanup phase).

**Use Cases**:
- Final cleanup
- Save session summary
- Export logs
- Trigger post-session workflows

**Input Schema**:
```json
{
  "session_id": "string",
  "duration_ms": 180000,
  "tools_used": ["Read", "Write", "Bash"],
  "final_status": "completed|error"
}
```

**Output Schema**:
```json
{
  "suppressOutput": false
}
```

---

## Input/Output Schemas

### Standard Input Format

All hooks receive input via **stdin** as a single JSON object:

```javascript
const input = JSON.parse(require('fs').readFileSync(0, 'utf-8'));
```

### Standard Output Format

All hooks return output via **stdout** as a single JSON object:

```javascript
console.log(JSON.stringify({ continue: true }));
```

### Exit Codes

| Exit Code | Meaning |
|-----------|---------|
| 0 | Success - output is valid |
| 1 | Error - hook failed, operation continues |
| 2+ | Error - hook failed critically |

**Important**: Non-zero exit codes are logged but do NOT block operations.
Only `continue: false` in output blocks operations.

---

## Hook Execution Lifecycle

```
SESSION START
    |
    v
[SessionStart Hook] --> Can block session
    |
    v
USER PROMPT RECEIVED
    |
    v
[UserPromptSubmit Hook] --> Can block/modify prompt
    |
    v
CLAUDE PROCESSES PROMPT
    |
    v
TOOL INVOCATION REQUESTED
    |
    v
[PreToolUse Hook] --> Can block/modify tool call
    |
    v
PERMISSION CHECK (if needed)
    |
    v
[PermissionRequest Hook] --> Can auto-approve/deny
    |
    v
TOOL EXECUTES
    |
    v
[PostToolUse Hook] --> Observational only
    |
    v
(Repeat for each tool)
    |
    v
CONTEXT COMPACTION (if needed)
    |
    v
[PreCompact Hook] --> Can inject preserved context
    |
    v
AGENT STOPS
    |
    v
[Stop Hook] --> Observational only
    |
    v
[SessionEnd Hook] --> Final cleanup
```

### Execution Order Within Event

When multiple hooks are configured for the same event:

1. Hooks execute **sequentially** in array order
2. If any blocking hook returns `continue: false`, subsequent hooks are skipped
3. Non-blocking hooks always run (unless previous blocking hook failed)

---

## Best Practices

### 1. Performance

```
REQUIREMENT: Hooks must complete within timeout (default 60s)
RECOMMENDATION: Target <20ms for pre-hooks, <100ms for post-hooks
```

**Tips**:
- Avoid network calls in pre-hooks
- Use async logging (write to file, not HTTP)
- Cache expensive computations
- Use matchers to limit hook invocations

### 2. Error Handling

```javascript
#!/usr/bin/env node
try {
  const input = JSON.parse(require('fs').readFileSync(0, 'utf-8'));

  // Your logic here

  console.log(JSON.stringify({ continue: true }));
} catch (error) {
  // Log error but don't block
  console.error(`Hook error: ${error.message}`);
  console.log(JSON.stringify({ continue: true }));
  process.exit(1);
}
```

### 3. Logging

Use **stderr** for logs, **stdout** for output:

```javascript
console.error('[HOOK] Processing event...');  // Goes to logs
console.log(JSON.stringify({ continue: true }));  // Hook output
```

### 4. Security

- Never log sensitive data (passwords, API keys)
- Validate all input before processing
- Use absolute paths for commands
- Set restrictive file permissions on hook scripts

### 5. Idempotency

Hooks may be retried. Ensure operations are idempotent:

```javascript
// BAD: May double-log
fs.appendFileSync('log.txt', 'entry\n');

// GOOD: Use unique ID to prevent duplicates
const entryId = `${input.session_id}-${input.tool_name}-${Date.now()}`;
if (!seenEntries.has(entryId)) {
  fs.appendFileSync('log.txt', `${entryId}: entry\n`);
  seenEntries.add(entryId);
}
```

---

## Integration with RBAC System

This plugin's RBAC system uses hooks for security enforcement:

### Pre-Hook Pipeline

```
PreToolUse
    |
    v
1. [pre-identity-verify.js]    Priority 1 - Verify agent identity
    |
    v
2. [pre-permission-check.js]   Priority 2 - Check RBAC permissions
    |
    v
3. [pre-budget-enforce.js]     Priority 3 - Verify budget available
    |
    v
4. [pre-approval-gate.js]      Priority 4 - Final approval check
    |
    v
TOOL EXECUTES
```

### Post-Hook Pipeline

```
PostToolUse
    |
    v
5. [post-audit-trail.js]       Priority 5 - Log operation
    |
    v
6. [post-budget-deduct.js]     Priority 6 - Deduct budget
```

### RBAC Configuration

Located in `hooks/12fa/`:

```
hooks/12fa/
  |-- identity.js              Agent identity management
  |-- permission-checker.js    RBAC policy enforcement
  |-- budget-tracker.js        Token/cost budget tracking
  |-- security-hooks/
       |-- pre-identity-verify.js
       |-- pre-permission-check.js
       |-- pre-budget-enforce.js
       |-- pre-approval-gate.js
       |-- post-audit-trail.js
       |-- post-budget-deduct.js
```

---

## Error Handling

### Hook Failures

| Scenario | Behavior |
|----------|----------|
| Hook times out | Operation continues, error logged |
| Hook crashes (exit != 0) | Operation continues, error logged |
| Hook returns invalid JSON | Operation continues, error logged |
| Hook returns `continue: false` | Operation blocked |

### Graceful Degradation

Hooks should fail open (allow operation) unless security-critical:

```javascript
#!/usr/bin/env node
const FAIL_OPEN = true;  // Set to false for security-critical hooks

try {
  const input = JSON.parse(require('fs').readFileSync(0, 'utf-8'));

  // Critical security check
  if (isSecurityViolation(input)) {
    console.log(JSON.stringify({
      continue: false,
      decision: "block",
      reason: "Security violation detected"
    }));
    process.exit(0);
  }

  console.log(JSON.stringify({ continue: true }));
} catch (error) {
  console.error(`Hook error: ${error.message}`);
  console.log(JSON.stringify({ continue: FAIL_OPEN }));
  process.exit(1);
}
```

---

## Performance Requirements

### Targets

| Hook Type | Target Latency | Max Latency |
|-----------|----------------|-------------|
| Pre-hooks (blocking) | <20ms | 100ms |
| Post-hooks (observational) | <100ms | 1000ms |
| Session hooks | <500ms | 5000ms |

### Optimization Tips

1. **Minimize I/O**: Cache file reads, batch writes
2. **Avoid Network**: No HTTP calls in pre-hooks
3. **Use Matchers**: Filter events before hook execution
4. **Profile Regularly**: Monitor hook latency in production

### Benchmarking

```javascript
#!/usr/bin/env node
const start = process.hrtime.bigint();

// Hook logic here

const end = process.hrtime.bigint();
const durationMs = Number(end - start) / 1_000_000;
console.error(`[PERF] Hook completed in ${durationMs.toFixed(2)}ms`);
```

---

## Related Documentation

- [Identity System](../utils/README.md)
- [Permission Checker](../permission-checker.js)
- [Budget Tracker](../budget-tracker.js)
- [hooks-automation Skill](../../../skills/operations/hooks-automation/SKILL.md)

---

*Generated for Context Cascade Plugin v3.0.0*
*Claude Code Hooks Reference v1.0.0*
