# skill-router-hook.ps1
# PURPOSE: Smart skill routing via keyword matching with CASCADE DISCOVERY
# HOOK TYPE: UserPromptSubmit (runs before Claude processes user message)

$ErrorActionPreference = "SilentlyContinue"

$SCRIPT_DIR = Split-Path -Parent $MyInvocation.MyCommand.Path
$PLUGIN_DIR = Split-Path -Parent $SCRIPT_DIR
$ROUTER = "$PLUGIN_DIR\scripts\skill-index\route-skill.sh"
$INDEX_FILE = "$PLUGIN_DIR\scripts\skill-index\skill-index.json"
$COMMANDS_INDEX = "$env:USERPROFILE\.claude\commands\COMMANDS_INDEX.yaml"

# Read user message from stdin
$inputJson = ""
try {
    $inputJson = [Console]::In.ReadToEnd()
} catch {
    $inputJson = "{}"
}

$MESSAGE_TEXT = ""
try {
    $inputData = $inputJson | ConvertFrom-Json
    $MESSAGE_TEXT = $inputData.message
} catch {
    $MESSAGE_TEXT = $inputJson
}

if (-not $MESSAGE_TEXT) { exit 0 }

$MESSAGE_LOWER = $MESSAGE_TEXT.ToLower()

# Skip trivial requests
$TRIVIAL_PATTERNS = "^(hi|hello|hey|thanks|ok|yes|no|bye|help|/help|continue|proceed)$"
if ($MESSAGE_TEXT -match $TRIVIAL_PATTERNS) { exit 0 }

# === TIER 1: Check COMMANDS_INDEX.yaml for explicit matches ===
if (Test-Path $COMMANDS_INDEX) {
    $content = Get-Content $COMMANDS_INDEX -Raw
    $lines = $content -split "`n"
    $trigger = ""

    foreach ($line in $lines) {
        if ($line -match 'trigger:.*"(.+)"') {
            $trigger = $matches[1]
        } elseif ($line -match 'skill:.*"(.+)"' -and $trigger) {
            $skill = $matches[1]
            if ($MESSAGE_LOWER -match [regex]::Escape($trigger)) {
                Write-Host ""
                Write-Host "!! CASCADE ROUTER (EXPLICIT) !!"
                Write-Host "Trigger: `"$trigger`" -> Skill: $skill"
                Write-Host "Read: skills/*/$($skill -replace ' ','-')/SKILL.md"
                Write-Host ""
                exit 0
            }
            $trigger = ""
        }
    }
}

# === TIER 2: Fuzzy keyword matching ===
if (-not (Test-Path $ROUTER) -or -not (Test-Path $INDEX_FILE)) { exit 0 }

$ROUTER_OUTPUT = bash $ROUTER $MESSAGE_TEXT 2>$null

if (-not $ROUTER_OUTPUT -or $ROUTER_OUTPUT -match "No matching") { exit 0 }

Write-Host ""
Write-Host "!! CASCADE SKILL ROUTER !!"
Write-Host "================================================================"
Write-Host $ROUTER_OUTPUT
Write-Host "================================================================"
Write-Host ""

exit 0
