# reflect-state.ps1
# Utility script for managing reflect state
#
# Usage:
#   .\reflect-state.ps1 enable   - Enable automatic reflection
#   .\reflect-state.ps1 disable  - Disable automatic reflection
#   .\reflect-state.ps1 status   - Check current state
#   .\reflect-state.ps1 history  - Show recent reflection history

param(
    [Parameter(Position=0)]
    [string]$Command = "status"
)

$STATE_DIR = "$env:USERPROFILE\.claude"
$STATE_FILE = "$STATE_DIR\reflect-enabled"
$LOG_FILE = "$STATE_DIR\reflect-history.log"

# Ensure state directory exists
if (-not (Test-Path $STATE_DIR)) {
    New-Item -ItemType Directory -Path $STATE_DIR -Force | Out-Null
}

switch ($Command.ToLower()) {
    { $_ -in "enable", "on" } {
        "true" | Out-File -FilePath $STATE_FILE -Encoding utf8 -NoNewline
        Write-Host "Automatic reflection ENABLED"
        $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
        Add-Content -Path $LOG_FILE -Value "[$timestamp] Reflection enabled"
    }

    { $_ -in "disable", "off" } {
        "false" | Out-File -FilePath $STATE_FILE -Encoding utf8 -NoNewline
        Write-Host "Automatic reflection DISABLED"
        $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
        Add-Content -Path $LOG_FILE -Value "[$timestamp] Reflection disabled"
    }

    "status" {
        if (Test-Path $STATE_FILE) {
            $CURRENT = (Get-Content $STATE_FILE -Raw).Trim()
            if ($CURRENT -eq "true") {
                Write-Host "Status: ENABLED"
                Write-Host "Sessions will auto-reflect on end"
            } else {
                Write-Host "Status: DISABLED"
                Write-Host "Manual /reflect required"
            }
        } else {
            Write-Host "Status: NOT CONFIGURED"
            Write-Host "Run 'reflect-state.ps1 enable' to enable"
        }
    }

    "history" {
        if (Test-Path $LOG_FILE) {
            Write-Host "=== Recent Reflection History ==="
            Get-Content $LOG_FILE -Tail 20
        } else {
            Write-Host "No reflection history found"
        }
    }

    default {
        Write-Host "Usage: .\reflect-state.ps1 {enable|disable|status|history}"
        Write-Host ""
        Write-Host "Commands:"
        Write-Host "  enable   Enable automatic session reflection"
        Write-Host "  disable  Disable automatic session reflection"
        Write-Host "  status   Show current reflection state"
        Write-Host "  history  Show recent reflection history"
        exit 1
    }
}

exit 0
