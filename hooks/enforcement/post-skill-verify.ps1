# post-skill-verify.ps1
# PostToolUse hook for Skill - verifies skill outputs match expected patterns

$ErrorActionPreference = "SilentlyContinue"

$SCRIPT_DIR = Split-Path -Parent $MyInvocation.MyCommand.Path
$STATE_FILE = "$env:USERPROFILE\.claude\runtime\enforcement-state.json"
$PATTERNS_FILE = "$SCRIPT_DIR\skill-patterns.json"
$VERIFICATION_LOG = "$env:USERPROFILE\.claude\runtime\skill-verification.log"

# Ensure log directory exists
$logDir = Split-Path -Parent $VERIFICATION_LOG
if (-not (Test-Path $logDir)) {
    New-Item -ItemType Directory -Path $logDir -Force | Out-Null
}

function Log-Verification($skill, $status, $message) {
    $timestamp = Get-Date -Format "yyyy-MM-ddTHH:mm:ssZ"
    Add-Content -Path $VERIFICATION_LOG -Value "[$timestamp] [$status] ${skill}: $message"
}

function Get-LastSkill {
    if (Test-Path $STATE_FILE) {
        try {
            $state = Get-Content $STATE_FILE -Raw | ConvertFrom-Json
            if ($state.skill_invocations -and $state.skill_invocations.Count -gt 0) {
                return $state.skill_invocations[-1].skill_name
            }
        } catch { }
    }
    return "unknown"
}

function Get-Pattern($skill) {
    if (Test-Path $PATTERNS_FILE) {
        try {
            $patterns = Get-Content $PATTERNS_FILE -Raw | ConvertFrom-Json
            if ($patterns.patterns.$skill) {
                return $patterns.patterns.$skill
            }
            return $patterns.default_pattern
        } catch { }
    }
    return @{}
}

function Check-Actions($skill) {
    if (-not (Test-Path $STATE_FILE)) {
        return "STATE_FILE_MISSING"
    }

    if (-not (Test-Path $PATTERNS_FILE)) {
        return $null
    }

    $missing_actions = @()

    try {
        $state = Get-Content $STATE_FILE -Raw | ConvertFrom-Json
        $patterns = Get-Content $PATTERNS_FILE -Raw | ConvertFrom-Json

        $expected = $patterns.patterns.$skill.expected_actions
        if (-not $expected) { $expected = $patterns.default_pattern.expected_actions }

        # Check for Task requirement
        if ($expected -contains "Task") {
            $task_count = 0
            if ($state.agent_spawns) { $task_count = $state.agent_spawns.Count }
            if ($task_count -eq 0) {
                $missing_actions += "Task(agent_spawn)"
            }
        }

        # Check for TodoWrite requirement
        if ($expected -contains "TodoWrite") {
            if ($state.todos_created -ne $true) {
                $missing_actions += "TodoWrite"
            }
        }
    } catch { }

    if ($missing_actions.Count -gt 0) {
        return ($missing_actions -join " ")
    }
    return $null
}

# Main verification
function Main {
    $skill = Get-LastSkill

    if ($skill -eq "unknown") {
        Write-Host "!! SKILL VERIFICATION: No skill found in state !!" -ForegroundColor Yellow
        return
    }

    $pattern = Get-Pattern $skill
    $verification_msg = "No verification message"
    if ($pattern.verification_message) {
        $verification_msg = $pattern.verification_message
    }

    Write-Host ""
    Write-Host "================================================================"
    Write-Host "!! SKILL COMPLETION VERIFICATION: $skill !!"
    Write-Host "================================================================"
    Write-Host ""
    Write-Host "Expected: $verification_msg"
    Write-Host ""

    $missing = Check-Actions $skill

    if ($missing) {
        Write-Host "!! WARNING: Missing expected actions: $missing !!" -ForegroundColor Red
        Write-Host ""
        Write-Host "REMINDER: After invoking a skill, you MUST:"
        Write-Host "  1. Spawn agents via Task() to execute the skill's workflow"
        Write-Host "  2. Track progress via TodoWrite() with 5-10 todos"
        Write-Host "  3. Complete all skill-specific outputs"
        Write-Host ""
        Log-Verification $skill "WARNING" "Missing actions: $missing"

        # Update state with verification failure
        if (Test-Path $STATE_FILE) {
            try {
                $state = Get-Content $STATE_FILE -Raw | ConvertFrom-Json
                if ($state.skill_invocations -and $state.skill_invocations.Count -gt 0) {
                    $state.skill_invocations[-1].sop_followed = $false
                    $state.skill_invocations[-1].missing_actions = $missing
                    $state | ConvertTo-Json -Depth 10 | Out-File -FilePath $STATE_FILE -Encoding utf8
                }
            } catch { }
        }
    } else {
        Write-Host "VERIFICATION: Skill pattern compliance detected" -ForegroundColor Green
        Log-Verification $skill "PASS" "All expected actions found"

        # Update state with verification success
        if (Test-Path $STATE_FILE) {
            try {
                $state = Get-Content $STATE_FILE -Raw | ConvertFrom-Json
                if ($state.skill_invocations -and $state.skill_invocations.Count -gt 0) {
                    $state.skill_invocations[-1].sop_followed = $true
                    $state | ConvertTo-Json -Depth 10 | Out-File -FilePath $STATE_FILE -Encoding utf8
                }
            } catch { }
        }
    }

    Write-Host "================================================================"
    Write-Host ""
}

Main
