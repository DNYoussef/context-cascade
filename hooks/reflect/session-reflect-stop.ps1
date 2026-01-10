# session-reflect-stop.ps1
# Hook: Stop
# Purpose: Trigger automatic reflection when session ends (if enabled)
#
# This hook:
# 1. Checks if reflect-on is enabled
# 2. If enabled, invokes the reflect skill in quick mode
# 3. Auto-applies MEDIUM/LOW learnings
# 4. Displays summary of learnings captured

$ErrorActionPreference = "SilentlyContinue"

$STATE_DIR = "$env:USERPROFILE\.claude"
$STATE_FILE = "$STATE_DIR\reflect-enabled"
$LOG_FILE = "$STATE_DIR\reflect-history.log"
$SCRIPT_DIR = Split-Path -Parent $MyInvocation.MyCommand.Path

# Ensure state directory exists
if (-not (Test-Path $STATE_DIR)) {
    New-Item -ItemType Directory -Path $STATE_DIR -Force | Out-Null
}

function Log-Message($msg) {
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Add-Content -Path $LOG_FILE -Value "[$timestamp] $msg"
}

# Check if reflection is enabled
if (-not (Test-Path $STATE_FILE)) {
    # Not configured, skip silently
    exit 0
}

$REFLECT_ENABLED = (Get-Content $STATE_FILE -Raw -ErrorAction SilentlyContinue).Trim()

if ($REFLECT_ENABLED -ne "true") {
    # Disabled, skip silently
    exit 0
}

Log-Message "Session ending - automatic reflection triggered"

# Output reflection trigger message
Write-Host ""
Write-Host "=========================================="
Write-Host "   SESSION REFLECTION (Automatic)"
Write-Host "=========================================="
Write-Host ""
Write-Host "Reflect-on is enabled. Analyzing session for learnings..."
Write-Host ""
Write-Host "Scanning for:"
Write-Host "- Corrections (HIGH confidence - will show for approval)"
Write-Host "- Approvals and patterns (MEDIUM - auto-applied)"
Write-Host "- Observations (LOW - auto-applied)"
Write-Host ""

# Check if there's session context to analyze
$SESSION_TRANSCRIPT = "$STATE_DIR\current-session.txt"
if (Test-Path $SESSION_TRANSCRIPT) {
    $content = Get-Content $SESSION_TRANSCRIPT -Raw
    $WORD_COUNT = ($content -split '\s+').Count

    if ($WORD_COUNT -lt 100) {
        Log-Message "Session too short ($WORD_COUNT words), skipping reflection"
        Write-Host "Session too short for meaningful reflection."
        Write-Host "No learnings captured."
        Write-Host ""
        Write-Host "Use /reflect manually after longer sessions."
        Write-Host "=========================================="
        exit 0
    }
}

# Output instruction for Claude to perform reflection
Write-Host "Please analyze this session for learning signals:"
Write-Host ""
Write-Host "1. Look for corrections: `"No, use X instead`", `"That's wrong`""
Write-Host "2. Look for explicit rules: `"Always do X`", `"Never do Y`""
Write-Host "3. Look for approvals: `"Perfect`", `"Yes, exactly`""
Write-Host "4. Look for patterns that worked well"
Write-Host ""
Write-Host "For MEDIUM/LOW confidence learnings, auto-apply to skill files."
Write-Host "For HIGH confidence learnings, note them for next manual /reflect."
Write-Host ""
Write-Host "After analysis, summarize:"
Write-Host "- Skills updated"
Write-Host "- Learnings captured"
Write-Host "- Any HIGH confidence items pending approval"
Write-Host ""
Write-Host "=========================================="

Log-Message "Reflection prompt injected"

# Exit normally - Claude will handle the reflection
exit 0
