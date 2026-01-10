# run-audit.ps1
# PURPOSE: Run Connascence Safety Analyzer on code changes
# HOOK TYPE: PostToolUse for Write/Edit/MultiEdit operations

$ErrorActionPreference = "SilentlyContinue"

$STATE_DIR = "$env:USERPROFILE\.claude\connascence-audit"
$RESULTS_FILE = "$STATE_DIR\latest-results.json"
$ISSUES_FILE = "$STATE_DIR\pending-issues.md"
$LOG_FILE = "$STATE_DIR\audit-history.log"

# Create state directory if needed
if (-not (Test-Path $STATE_DIR)) {
    New-Item -ItemType Directory -Path $STATE_DIR -Force | Out-Null
}

# Get the file path from stdin
$inputJson = [Console]::In.ReadToEnd()
$FILE_PATH = ""
try {
    $inputData = $inputJson | ConvertFrom-Json
    $FILE_PATH = $inputData.tool_input.file_path
    if (-not $FILE_PATH) { $FILE_PATH = $inputData.tool_input.path }
} catch { }

if (-not $FILE_PATH) { exit 0 }

# Only audit Python files
if ($FILE_PATH -notmatch '\.py$') { exit 0 }

# Check if file exists
if (-not (Test-Path $FILE_PATH)) { exit 0 }

function Log-Message($msg) {
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Add-Content -Path $LOG_FILE -Value "[$timestamp] $msg"
}

Log-Message "Auditing: $FILE_PATH"

# Run the connascence analyzer
Push-Location "D:\Projects\connascence" -ErrorAction SilentlyContinue
if (-not $?) { exit 0 }

$pythonScript = @"
import sys
import json
try:
    from analyzer.core import ConnascenceAnalyzer
    analyzer = ConnascenceAnalyzer()
    result = analyzer.analyze_path('$FILE_PATH', policy='strict-core')
    violations = result.get('violations', [])
    critical = [v for v in violations if v.get('severity') == 'critical']
    high = [v for v in violations if v.get('severity') == 'high']
    output = {
        'success': result.get('success', False),
        'file': '$FILE_PATH',
        'total_violations': len(violations),
        'critical_count': len(critical),
        'high_count': len(high),
        'violations': violations[:10],
        'has_blocking_issues': len(critical) > 0 or len(high) > 3
    }
    print(json.dumps(output))
except Exception as e:
    print(json.dumps({'success': False, 'error': str(e)}))
"@

$ANALYSIS_OUTPUT = python -c $pythonScript 2>$null
Pop-Location

# Save results
$ANALYSIS_OUTPUT | Out-File -FilePath $RESULTS_FILE -Encoding utf8

# Parse results
$results = $ANALYSIS_OUTPUT | ConvertFrom-Json
$TOTAL = $results.total_violations
$CRITICAL = $results.critical_count
$HIGH = $results.high_count
$BLOCKING = $results.has_blocking_issues

Log-Message "Results: $TOTAL violations ($CRITICAL critical, $HIGH high)"

# Output summary for Claude if blocking
if ($BLOCKING) {
    Write-Host ""
    Write-Host "=========================================="
    Write-Host "   CONNASCENCE AUDIT: ISSUES FOUND"
    Write-Host "=========================================="
    Write-Host "File: $FILE_PATH"
    Write-Host "Critical: $CRITICAL | High: $HIGH | Total: $TOTAL"
    Write-Host ""
    Write-Host "BLOCKING ISSUES detected. Code quality gate FAILED."
    Write-Host "Fix issues and re-submit code."
    Write-Host ""
}

exit 0
