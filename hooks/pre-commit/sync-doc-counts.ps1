# Pre-commit hook: Sync documentation counts
#
# PURPOSE: Automatically update component counts in docs before each commit
# INSTALL: Copy to .git/hooks/pre-commit or reference from main pre-commit hook
#
# This ensures documentation always reflects actual component counts.

$ErrorActionPreference = "SilentlyContinue"

$SCRIPT_DIR = Split-Path -Parent $MyInvocation.MyCommand.Path
$PLUGIN_ROOT = Split-Path -Parent (Split-Path -Parent $SCRIPT_DIR)

Write-Host "=== Pre-commit: Syncing documentation counts ==="

# Run the sync script
$syncScript = "$PLUGIN_ROOT\scripts\sync-doc-counts.js"
if (Test-Path $syncScript) {
    node $syncScript update
}

# Check if any docs were modified
$MODIFIED_DOCS = git diff --name-only -- "*.md" "docs/COMPONENT-COUNTS.json" 2>$null

if ($MODIFIED_DOCS) {
    Write-Host ""
    Write-Host "Documentation updated with current counts:"
    Write-Host $MODIFIED_DOCS
    Write-Host ""
    Write-Host "Adding updated docs to commit..."

    foreach ($doc in ($MODIFIED_DOCS -split "`n")) {
        if ($doc.Trim()) {
            git add $doc.Trim()
        }
    }
}

Write-Host "=== Pre-commit complete ==="
exit 0
