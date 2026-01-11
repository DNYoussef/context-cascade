# extract-all-skills.ps1
# Extracts all .skill packages to proper folder structure for Claude Code discovery
# Created: 2026-01-11

param(
    [switch]$Force,
    [switch]$Verbose
)

$PackagedDir = "C:\Users\17175\claude-code-plugins\context-cascade\skills\packaged"
$SkillsRoot = "C:\Users\17175\claude-code-plugins\context-cascade\skills"

Write-Host "=== Extract All Skill Packages ===" -ForegroundColor Cyan
Write-Host "Source: $PackagedDir"
Write-Host "Target: $SkillsRoot"
Write-Host ""

# Category mapping based on skill names/prefixes
$CategoryMap = @{
    "delivery" = @("feature-dev-complete", "smart-bug-fix", "pair-programming", "debugging", "i18n-automation", "sop-api-development", "api-docs", "landing-page-generator", "sparc-methodology")
    "quality" = @("code-review-assistant", "functionality-audit", "theater-detection", "style-audit", "verification-quality", "github-code-review", "quick-quality-check", "connascence-quality-gate", "gate-validation", "holistic-evaluation", "audit-pipeline", "dogfooding-system", "sop-code-review", "sop-dogfooding", "testing-quality", "verification-and-quality")
    "research" = @("deep-research-orchestrator", "literature-synthesis", "baseline-replication", "method-development", "interactive-planner", "academic-reading-workflow", "general-research-workflow", "observability", "intent-analyzer", "research-driven-planning", "research-gap", "research-publication", "reproducibility-audit", "source-credibility")
    "orchestration" = @("cascade-orchestrator", "swarm-orchestration", "hive-mind", "stream-chain", "slash-command-encoder", "web-cli-teleport", "flow-nexus-swarm", "hooks-automation", "workflow-automation", "sparc-workflow", "swarm-advanced", "coordination", "advanced-coordination", "ai-dev-orchestration", "meta-loop-orchestrator", "parallel-swarm", "ralph-loop", "ralph-multimodel", "safe-task-spawn", "llm-council")
    "foundry" = @("skill-forge", "agent-creator", "prompt-architect", "hook-creator", "skill-builder", "skill-gap", "token-budget", "prompt-optimization", "prompt-forge", "agent-creation", "agent-selector", "base-template-generator", "cognitive-lensing", "meta-tools", "micro-skill-creator", "playbook-architect", "skill-creator-agent", "template-extractor")
    "operations" = @("production-readiness", "cicd-intelligent-recovery", "cloud-platforms", "performance-analysis", "performance-profiler", "github-project-management", "github-multi-repo", "github-release-management", "deployment-readiness", "docker-containerization", "github-workflow-automation", "infrastructure", "kubernetes-specialist", "opentelemetry-observability", "terraform-iac", "aws-specialist", "github-integration", "sop-product-launch", "platform-integration")
    "security" = @("network-security-setup", "sandbox-configurator", "security-analyzer", "reverse-engineering", "compliance", "security", "reconnaissance")
    "platforms" = @("ml-expert", "ml-training-debugger", "flow-nexus-platform", "agentdb", "machine-learning", "flow-nexus-neural", "codex", "gemini", "multi-model", "reasoningbank", "platform", "ml", "sql-database")
    "specialists" = @("python-specialist", "typescript-specialist", "rust-specialist", "go-specialist", "frontend-specialists", "react-specialist", "language-specialists", "expertise-manager", "system-design-architect", "ui-ux-excellence", "wcag-accessibility", "visual-asset", "pptx-generation", "image-gen", "rapid-idea", "rapid-manuscript")
    "tooling" = @("documentation", "dependencies", "bootstrap-loop", "eval-harness", "improvement-pipeline", "clarity-linter", "reflect", "pilot-1-code-formatter")
}

# Build reverse lookup
$SkillToCategory = @{}
foreach ($Category in $CategoryMap.Keys) {
    foreach ($Prefix in $CategoryMap[$Category]) {
        $SkillToCategory[$Prefix] = $Category
    }
}

function Get-SkillCategory {
    param([string]$SkillName)

    # Check exact matches and prefix matches
    foreach ($Prefix in $SkillToCategory.Keys) {
        if ($SkillName -eq $Prefix -or $SkillName.StartsWith("$Prefix-") -or $SkillName.StartsWith("when-") -and $SkillName -match $Prefix) {
            return $SkillToCategory[$Prefix]
        }
    }

    # Default category based on common patterns
    if ($SkillName -match "sop-") { return "delivery" }
    if ($SkillName -match "agentdb") { return "platforms" }
    if ($SkillName -match "codex|gemini") { return "platforms" }
    if ($SkillName -match "reverse-engineer") { return "security" }
    if ($SkillName -match "swarm|orchestrat") { return "orchestration" }
    if ($SkillName -match "test|quality|audit|review") { return "quality" }
    if ($SkillName -match "research|analysis") { return "research" }

    return "tooling"  # Default fallback
}

$Extracted = 0
$Skipped = 0
$Errors = 0

Get-ChildItem -Path $PackagedDir -Filter "*.skill" | ForEach-Object {
    $SkillFile = $_
    $SkillName = $SkillFile.BaseName
    $Category = Get-SkillCategory -SkillName $SkillName

    $TargetDir = Join-Path $SkillsRoot "$Category\$SkillName"

    # Check if already extracted
    if ((Test-Path $TargetDir) -and -not $Force) {
        if ($Verbose) { Write-Host "[SKIP] $SkillName (already exists)" -ForegroundColor Yellow }
        $Skipped++
        return
    }

    # Create target directory
    New-Item -ItemType Directory -Path $TargetDir -Force | Out-Null

    # Extract .skill (it's a zip file)
    $TempZip = Join-Path $env:TEMP "$SkillName.zip"
    try {
        Copy-Item -Path $SkillFile.FullName -Destination $TempZip -Force
        Expand-Archive -Path $TempZip -DestinationPath $TargetDir -Force
        Remove-Item $TempZip -Force

        Write-Host "[EXTRACTED] $Category/$SkillName" -ForegroundColor Green
        $Extracted++
    } catch {
        Write-Host "[ERROR] $SkillName : $_" -ForegroundColor Red
        $Errors++
    }
}

Write-Host ""
Write-Host "=== Summary ===" -ForegroundColor Cyan
Write-Host "Extracted: $Extracted"
Write-Host "Skipped: $Skipped"
Write-Host "Errors: $Errors"
Write-Host ""
Write-Host "Skills are now accessible at:"
Write-Host "  $SkillsRoot/{category}/{skill-name}/SKILL.md"
