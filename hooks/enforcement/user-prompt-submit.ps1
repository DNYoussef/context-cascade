# user-prompt-submit.ps1
# Hook: UserPromptSubmit
# Purpose: Initialize workflow state, match skills, and inject context
#
# INTEGRATED SKILL ROUTER - Matches user request to relevant skills

$ErrorActionPreference = "SilentlyContinue"

$SCRIPT_DIR = Split-Path -Parent $MyInvocation.MyCommand.Path
$STATE_TRACKER = Join-Path $SCRIPT_DIR "state-tracker.ps1"

# Read user message from stdin
$inputJson = ""
try {
    $inputJson = [Console]::In.ReadToEnd()
} catch {
    $inputJson = "{}"
}

if (-not $inputJson) { $inputJson = "{}" }

# Extract prompt text
$messageText = ""
try {
    $inputData = $inputJson | ConvertFrom-Json
    if ($inputData.prompt) {
        $messageText = $inputData.prompt
    } elseif ($inputData.message) {
        $messageText = $inputData.message
    }
} catch {
    $messageText = $inputJson
}

# Classify request as trivial or non-trivial
$isTrivial = $false

# Trivial patterns (skip enforcement)
$trivialPatterns = @(
    "^(hi|hello|hey|thanks|thank you|ok|okay|yes|no|bye)$",
    "^what (is|are|does|do) ",
    "^(can you|could you) explain",
    "^(help|/help|/clear|/status)",
    "^show me",
    "^list ",
    "^read ",
    "^(git status|git log|ls|pwd)",
    "^search ",
    "^find ",
    "^grep "
)

foreach ($pattern in $trivialPatterns) {
    if ($messageText -match $pattern) {
        $isTrivial = $true
        break
    }
}

# Non-trivial patterns (REQUIRE 5-phase)
$nonTrivialPatterns = @(
    "(build|create|implement|develop|add|make)",
    "(fix|debug|repair|resolve|solve)",
    "(refactor|optimize|improve|enhance)",
    "(analyze|audit|review|check|validate)",
    "(deploy|release|ship|publish)",
    "(test|spec|coverage)",
    "(design|architect|plan|strategy)"
)

foreach ($pattern in $nonTrivialPatterns) {
    if ($messageText -match $pattern) {
        $isTrivial = $false
        break
    }
}

# For non-trivial requests, initialize state and display workflow
if (-not $isTrivial) {
    # Initialize workflow state
    if (Test-Path $STATE_TRACKER) {
        & powershell -ExecutionPolicy Bypass -File $STATE_TRACKER init_state 2>$null
    }

    Write-Host @"

================================================================
!! 5-PHASE WORKFLOW ACTIVE !!
================================================================

This appears to be a NON-TRIVIAL request.

WORKFLOW INSTRUCTIONS:
================================================================

1. INTENT ANALYSIS - Understand what user wants
2. PLANNING - Break down into tasks
3. SKILL ROUTING - Find relevant skills in:
   skills/packaged/     - All packaged skills (.skill files)
4. EXECUTION - Skill -> Task -> TodoWrite pattern
5. VERIFICATION - Check outputs against requirements

EXECUTION PATTERN:
  Read(skill_path + "SKILL.md")   // Load the SOP
       |
       v
  Task("Agent", "...", "type")    // Execute via registry agent
       |
       v
  TodoWrite({ todos: [...] })     // Track progress

Agent Registry: claude-code-plugins/context-cascade/agents/
Fallbacks: coder, researcher, tester, reviewer

GOLDEN RULE: 1 MESSAGE = ALL PARALLEL Task() CALLS
================================================================

"@
}

exit 0
