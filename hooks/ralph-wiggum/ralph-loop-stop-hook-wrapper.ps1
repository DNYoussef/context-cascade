# ralph-loop-stop-hook-wrapper.ps1
# PURPOSE: Wrapper that delegates to enhanced JS hook when available
# HOOK TYPE: Stop (runs when Claude tries to end session)
#
# This wrapper:
# 1. Checks if Node.js is available
# 2. Checks if enhanced JS hook exists
# 3. Delegates to JS hook for Memory-MCP integration
# 4. Falls back to shell script if JS unavailable
#
# @version 3.0.0
# @see docs/META-LOOP-ENHANCEMENT-PLAN-v4.md Phase E

$ErrorActionPreference = "SilentlyContinue"

$SCRIPT_DIR = Split-Path -Parent $MyInvocation.MyCommand.Path
$ENHANCED_HOOK = "$SCRIPT_DIR\ralph-loop-stop-hook-enhanced.js"
$FALLBACK_HOOK = "$SCRIPT_DIR\ralph-loop-stop-hook.ps1"

# Check if Node.js is available
$nodeAvailable = Get-Command node -ErrorAction SilentlyContinue

if ($nodeAvailable -and (Test-Path $ENHANCED_HOOK)) {
    # Delegate to enhanced JS hook
    # Pass stdin through to the JS hook
    $input | node $ENHANCED_HOOK
    exit $LASTEXITCODE
} else {
    # Fall back to PowerShell script
    if (Test-Path $FALLBACK_HOOK) {
        $input | & powershell -File $FALLBACK_HOOK
        exit $LASTEXITCODE
    } else {
        # No hook available, allow exit
        exit 0
    }
}
