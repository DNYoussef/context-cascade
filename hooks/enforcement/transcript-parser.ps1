# transcript-parser.ps1
# Purpose: Parse conversation transcript to validate Task() parameters
#
# CRITICAL: This is needed because hooks CANNOT inspect Task() parameters
# This script runs async to validate agent types against registry

$ErrorActionPreference = "SilentlyContinue"

$SCRIPT_DIR = Split-Path -Parent $MyInvocation.MyCommand.Path
$STATE_TRACKER = "$SCRIPT_DIR\state-tracker.ps1"
$TRANSCRIPT_FILE = "$env:USERPROFILE\.claude\history.jsonl"
$REGISTRY_FILE = "$env:USERPROFILE\claude-code-plugins\ruv-sparc-three-loop-system\agents\REGISTRY.json"

# Agent registry categories (for validation when registry file not available)
$KNOWN_AGENT_TYPES = @(
    # Delivery
    "coder", "backend-dev", "frontend-dev", "fullstack-dev", "mobile-dev",
    "devops-engineer", "sre", "release-engineer", "api-developer", "database-dev",

    # Research
    "researcher", "analyst", "data-scientist", "ml-engineer", "experiment-designer",

    # Quality
    "tester", "qa-engineer", "security-tester", "load-tester", "reviewer",
    "code-analyzer", "auditor", "compliance-checker", "theater-detection-audit",

    # Orchestration
    "hierarchical-coordinator", "byzantine-coordinator", "workflow-orchestrator",
    "task-router", "dependency-manager",

    # Foundry
    "agent-creator", "skill-creator", "prompt-engineer", "template-generator",

    # Operations
    "cicd-engineer", "monitoring-engineer", "incident-responder", "backup-manager",

    # Platforms
    "platform-engineer", "cloud-architect", "kubernetes-expert", "terraform-expert",

    # Security
    "security-engineer", "penetration-tester", "crypto-expert", "compliance-auditor",

    # Tooling
    "build-engineer", "package-manager", "dependency-analyzer", "linter-configurator"
)

function Parse-TaskCalls {
    if (-not (Test-Path $TRANSCRIPT_FILE)) {
        Write-Host "Transcript file not found: $TRANSCRIPT_FILE" -ForegroundColor Yellow
        return
    }

    # Extract recent Task() calls from transcript
    $content = Get-Content $TRANSCRIPT_FILE -Raw
    $task_calls = [regex]::Matches($content, 'Task\([^)]*')

    if ($task_calls.Count -eq 0) {
        Write-Host "No Task() calls found in transcript" -ForegroundColor Yellow
        return
    }

    Write-Host "Found $($task_calls.Count) Task() calls, parsing..."

    # Get last 20 calls
    $recent_calls = $task_calls | Select-Object -Last 20

    foreach ($match in $recent_calls) {
        $task_line = $match.Value

        # Try to extract agent type (third parameter)
        if ($task_line -match ',\s*"([^"]+)"\s*$') {
            $agent_type = $matches[1]
            Validate-AgentType $agent_type
        }
    }
}

function Validate-AgentType($agent_type) {
    $is_valid = $KNOWN_AGENT_TYPES -contains $agent_type

    if (-not $is_valid) {
        Write-Host "INVALID AGENT TYPE: $agent_type" -ForegroundColor Red

        # Log violation via state tracker
        if (Test-Path $STATE_TRACKER) {
            & powershell -File $STATE_TRACKER log_violation "generic_agent" "Invalid agent type detected via transcript: $agent_type"
        }

        Write-Host ""
        Write-Host "!! VALIDATION FAILURE !!" -ForegroundColor Red
        Write-Host "Invalid agent type detected: $agent_type"
        Write-Host ""
        Write-Host "This agent type is NOT in the registry."
        Write-Host "Valid types: $($KNOWN_AGENT_TYPES -join ', ')"
        Write-Host ""
        Write-Host "Please use a registry agent type."
        Write-Host ""
    } else {
        Write-Host "Valid agent type: $agent_type" -ForegroundColor Green
    }
}

function Load-Registry {
    if (Test-Path $REGISTRY_FILE) {
        Write-Host "Loading agent registry from: $REGISTRY_FILE"
        try {
            $registry = Get-Content $REGISTRY_FILE -Raw | ConvertFrom-Json
            if ($registry.agents) {
                $script:KNOWN_AGENT_TYPES = $registry.agents | ForEach-Object { $_.type }
                Write-Host "Loaded $($KNOWN_AGENT_TYPES.Count) agent types from registry"
            }
        } catch {
            Write-Host "Failed to parse registry, using hardcoded types" -ForegroundColor Yellow
        }
    } else {
        Write-Host "Registry file not found, using hardcoded types" -ForegroundColor Yellow
    }
}

# Main execution
function Main {
    Write-Host "=== Transcript Parser - Agent Type Validation ==="

    # Load registry
    Load-Registry

    # Parse transcript
    Parse-TaskCalls

    Write-Host "=== Validation Complete ==="
}

Main
