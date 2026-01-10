# Pre-commit hook: Validate cross-platform hook parity
# Fails commit if .ps1 files are missing .sh counterparts or vice versa

$ErrorActionPreference = "SilentlyContinue"
$HOOKS_DIR = Split-Path -Parent $PSScriptRoot
$ERRORS = 0

Write-Host "[pre-commit] Validating cross-platform hook parity..."

# Find all .ps1 files (excluding node_modules)
$ps1Files = Get-ChildItem -Path $HOOKS_DIR -Filter "*.ps1" -Recurse |
    Where-Object { $_.FullName -notmatch "node_modules" }

foreach ($ps1File in $ps1Files) {
    $shFile = $ps1File.FullName -replace '\.ps1$', '.sh'
    if (-not (Test-Path $shFile)) {
        Write-Host "  [ERROR] Missing: $(Split-Path -Leaf $shFile) (for $($ps1File.Name))"
        $ERRORS++
    }
}

# Find all .sh files (excluding node_modules and validation scripts)
$shFiles = Get-ChildItem -Path $HOOKS_DIR -Filter "*.sh" -Recurse |
    Where-Object { $_.FullName -notmatch "node_modules" -and $_.Name -notmatch "validate-cross-platform" }

foreach ($shFile in $shFiles) {
    $ps1File = $shFile.FullName -replace '\.sh$', '.ps1'
    if (-not (Test-Path $ps1File)) {
        Write-Host "  [ERROR] Missing: $(Split-Path -Leaf $ps1File) (for $($shFile.Name))"
        $ERRORS++
    }
}

if ($ERRORS -gt 0) {
    Write-Host ""
    Write-Host "[pre-commit] BLOCKED: $ERRORS cross-platform counterparts missing"
    Write-Host "             Create the missing files before committing"
    exit 1
}

Write-Host "[pre-commit] PASS: All hooks have cross-platform counterparts"
exit 0
