# INSTALL.ps1
# Purpose: Install enforcement hook system

$ErrorActionPreference = "SilentlyContinue"

$ENFORCEMENT_DIR = Split-Path -Parent $MyInvocation.MyCommand.Path
$SETTINGS_FILE = "$env:USERPROFILE\.claude\settings.json"
$RUNTIME_DIR = "$env:USERPROFILE\.claude\runtime\enforcement"

Write-Host "=== Installing Enforcement Hook System ==="
Write-Host ""

# Step 1: Create runtime directory
Write-Host "Step 1: Creating runtime directory..."
New-Item -ItemType Directory -Path "$RUNTIME_DIR\archive" -Force | Out-Null
Write-Host "  Created: $RUNTIME_DIR"
Write-Host "  Created: $RUNTIME_DIR\archive"
Write-Host ""

# Step 2: Backup existing settings
Write-Host "Step 2: Backing up existing settings..."
if (Test-Path $SETTINGS_FILE) {
    $BACKUP_FILE = "$SETTINGS_FILE.backup-$(Get-Date -Format 'yyyyMMdd-HHmmss')"
    Copy-Item $SETTINGS_FILE $BACKUP_FILE
    Write-Host "  Backed up to: $BACKUP_FILE"
} else {
    Write-Host "  No existing settings file found"
}
Write-Host ""

# Step 3: Display merge instructions
Write-Host "Step 3: Configuration merge instructions"
Write-Host ""
Write-Host "The enforcement hooks need to be added to your .claude/settings.json file."
Write-Host ""
Write-Host "OPTION 1 - Manual Merge (Recommended):"
Write-Host "  1. Open: $SETTINGS_FILE"
Write-Host "  2. Open: $ENFORCEMENT_DIR\CONFIGURATION.json"
Write-Host "  3. Copy the 'hooks' section from CONFIGURATION.json"
Write-Host "  4. Merge with existing hooks in settings.json"
Write-Host ""

# Step 4: Display next steps
Write-Host "=== Installation Complete ==="
Write-Host ""
Write-Host "NEXT STEPS:"
Write-Host ""
Write-Host "1. Merge hook configuration (see Step 3 above)"
Write-Host "2. Restart Claude Code to load new hooks"
Write-Host "3. Test with a non-trivial request"
Write-Host "4. Check state: powershell $ENFORCEMENT_DIR\generate-report.ps1"
Write-Host ""
Write-Host "FILES CREATED:"
Write-Host "  State file: $RUNTIME_DIR\enforcement-state.json (will be created on first use)"
Write-Host "  Archive dir: $RUNTIME_DIR\archive\"
Write-Host ""
Write-Host "Installation script complete."
