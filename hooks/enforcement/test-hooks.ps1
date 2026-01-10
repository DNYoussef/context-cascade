# test-hooks.ps1
# Purpose: Test enforcement hook system

$ErrorActionPreference = "SilentlyContinue"

$SCRIPT_DIR = Split-Path -Parent $MyInvocation.MyCommand.Path
$STATE_TRACKER = "$SCRIPT_DIR\state-tracker.ps1"

Write-Host "=== Testing Enforcement Hook System ==="
Write-Host ""

# Test 1: Initialize state
Write-Host "Test 1: Initialize state"
& powershell -File $STATE_TRACKER init_state
if ($LASTEXITCODE -eq 0) {
    Write-Host "  PASS: State initialized"
} else {
    Write-Host "  FAIL: State initialization failed"
}
Write-Host ""

# Test 2: Log skill invocation
Write-Host "Test 2: Log skill invocation"
& powershell -File $STATE_TRACKER log_skill "intent-analyzer"
if ($LASTEXITCODE -eq 0) {
    Write-Host "  PASS: Skill logged"
} else {
    Write-Host "  FAIL: Skill logging failed"
}
Write-Host ""

# Test 3: Log agent spawn (valid)
Write-Host "Test 3: Log agent spawn (valid registry type)"
& powershell -File $STATE_TRACKER log_agent "coder" "Code Implementation Agent" "Implement feature X"
if ($LASTEXITCODE -eq 0) {
    Write-Host "  PASS: Valid agent logged"
} else {
    Write-Host "  FAIL: Agent logging failed"
}
Write-Host ""

# Test 4: Log agent spawn (invalid)
Write-Host "Test 4: Log agent spawn (invalid generic type)"
& powershell -File $STATE_TRACKER log_agent "generic-coder" "Generic Agent" "Do stuff"
if ($LASTEXITCODE -eq 0) {
    Write-Host "  PASS: Invalid agent logged (violation expected)"
} else {
    Write-Host "  FAIL: Agent logging failed"
}
Write-Host ""

# Test 5: Mark TodoWrite
Write-Host "Test 5: Mark TodoWrite"
& powershell -File $STATE_TRACKER mark_todowrite
if ($LASTEXITCODE -eq 0) {
    Write-Host "  PASS: TodoWrite marked"
} else {
    Write-Host "  FAIL: TodoWrite marking failed"
}
Write-Host ""

# Test 6: Check compliance
Write-Host "Test 6: Check compliance"
& powershell -File $STATE_TRACKER check_compliance
$VIOLATIONS = $LASTEXITCODE
Write-Host "  Violations found: $VIOLATIONS"
Write-Host ""

# Test 7: Get state
Write-Host "Test 7: Get current state"
$STATE = & powershell -File $STATE_TRACKER get_state
if ($LASTEXITCODE -eq 0) {
    Write-Host "  PASS: State retrieved"
    Write-Host "  State summary:"
    try {
        $stateObj = $STATE | ConvertFrom-Json
        $summary = @{
            session_id = $stateObj.session_id
            workflow_phase = $stateObj.workflow_state.phase
            skills_invoked = $stateObj.skill_invocations.Count
            agents_spawned = $stateObj.agent_spawns.Count
            violations = $stateObj.violations.Count
            todos_created = $stateObj.todos_created
        }
        $summary | ConvertTo-Json
    } catch {
        Write-Host "  (Could not parse state)"
    }
} else {
    Write-Host "  FAIL: State retrieval failed"
}
Write-Host ""

# Test 8: Archive state
Write-Host "Test 8: Archive state"
& powershell -File $STATE_TRACKER archive_state
if ($LASTEXITCODE -eq 0) {
    Write-Host "  PASS: State archived"
} else {
    Write-Host "  FAIL: State archiving failed"
}
Write-Host ""

# Test 9: Test individual hooks
Write-Host "Test 9: Test UserPromptSubmit hook"
'{"message": "Implement a new feature"}' | & powershell -File "$SCRIPT_DIR\user-prompt-submit.ps1" > $null
if ($LASTEXITCODE -eq 0) {
    Write-Host "  PASS: UserPromptSubmit hook executed"
} else {
    Write-Host "  FAIL: UserPromptSubmit hook failed"
}
Write-Host ""

Write-Host "Test 10: Test PreToolUse Skill hook"
'{"tool_input": {"skill": "planner"}}' | & powershell -File "$SCRIPT_DIR\pre-skill-invoke.ps1" > $null
if ($LASTEXITCODE -eq 0) {
    Write-Host "  PASS: PreToolUse Skill hook executed"
} else {
    Write-Host "  FAIL: PreToolUse Skill hook failed"
}
Write-Host ""

Write-Host "Test 11: Test PostToolUse Skill hook"
'{"tool_name": "Skill"}' | & powershell -File "$SCRIPT_DIR\post-skill-compliance.ps1" > $null
if ($LASTEXITCODE -eq 0) {
    Write-Host "  PASS: PostToolUse Skill hook executed"
} else {
    Write-Host "  FAIL: PostToolUse Skill hook failed"
}
Write-Host ""

Write-Host "Test 12: Test PreCompact hook"
& powershell -File "$SCRIPT_DIR\pattern-retention.ps1" > $null
if ($LASTEXITCODE -eq 0) {
    Write-Host "  PASS: PreCompact hook executed"
} else {
    Write-Host "  FAIL: PreCompact hook failed"
}
Write-Host ""

Write-Host "Test 13: Test Stop hook"
& powershell -File "$SCRIPT_DIR\session-stop.ps1" > $null
if ($LASTEXITCODE -eq 0) {
    Write-Host "  PASS: Stop hook executed"
} else {
    Write-Host "  FAIL: Stop hook failed"
}
Write-Host ""

Write-Host "=== Hook System Test Complete ==="
Write-Host ""
Write-Host "Check state file: $env:USERPROFILE\.claude\runtime\enforcement-state.json"
Write-Host "Check archives: $env:USERPROFILE\.claude\runtime\enforcement\archive\"
