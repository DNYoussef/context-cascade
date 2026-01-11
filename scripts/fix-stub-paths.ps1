# fix-stub-paths.ps1
# Updates stub files in ~/.claude/commands/ to reference correct packaged skill locations
# Created: 2026-01-11

$CommandsDir = "C:\Users\17175\.claude\commands"
$PackagedDir = "C:\Users\17175\claude-code-plugins\context-cascade\skills\packaged"

Write-Host "=== Fix Stub Paths ===" -ForegroundColor Cyan
Write-Host "Commands Dir: $CommandsDir"
Write-Host "Packaged Dir: $PackagedDir"
Write-Host ""

# Get list of packaged skills
$PackagedSkills = Get-ChildItem -Path $PackagedDir -Filter "*.skill" | ForEach-Object { $_.BaseName }
Write-Host "Found $($PackagedSkills.Count) packaged skills"

$Updated = 0
$Skipped = 0

# Process each command file
Get-ChildItem -Path $CommandsDir -Filter "*.md" | ForEach-Object {
    $File = $_
    $SkillName = $File.BaseName

    # Check if this skill has a packaged version
    if ($PackagedSkills -contains $SkillName) {
        $Content = Get-Content -Path $File.FullName -Raw

        # Pattern to match old Source line
        $OldPattern = "Context Cascade: skills/[^/]+/$SkillName/SKILL\.md"
        $NewSource = "Context Cascade: skills/packaged/$SkillName.skill (extract to view SKILL.md)"

        if ($Content -match $OldPattern) {
            $NewContent = $Content -replace $OldPattern, $NewSource
            Set-Content -Path $File.FullName -Value $NewContent -NoNewline
            Write-Host "[UPDATED] $SkillName" -ForegroundColor Green
            $Updated++
        } else {
            $Skipped++
        }
    }
}

Write-Host ""
Write-Host "=== Summary ===" -ForegroundColor Cyan
Write-Host "Updated: $Updated"
Write-Host "Skipped: $Skipped"
Write-Host "Total packaged skills: $($PackagedSkills.Count)"
