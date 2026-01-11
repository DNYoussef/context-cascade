# sync-stub-paths.ps1
# Updates stub files to reference extracted skill locations
# Created: 2026-01-11

$CommandsDir = "C:\Users\17175\.claude\commands"
$SkillsRoot = "C:\Users\17175\claude-code-plugins\context-cascade\skills"

Write-Host "=== Sync Stub Paths to Extracted Skills ===" -ForegroundColor Cyan

# Get all category folders (excluding packaged)
$Categories = Get-ChildItem -Path $SkillsRoot -Directory | Where-Object { $_.Name -ne "packaged" }

# Build skill-to-category map
$SkillCategoryMap = @{}
foreach ($Cat in $Categories) {
    Get-ChildItem -Path $Cat.FullName -Directory | ForEach-Object {
        $SkillCategoryMap[$_.Name] = $Cat.Name
    }
}

Write-Host "Found $($SkillCategoryMap.Count) extracted skills across $($Categories.Count) categories"

$Updated = 0

Get-ChildItem -Path $CommandsDir -Filter "*.md" -File | ForEach-Object {
    $File = $_
    $SkillName = $File.BaseName

    if ($SkillCategoryMap.ContainsKey($SkillName)) {
        $Category = $SkillCategoryMap[$SkillName]
        $Content = Get-Content -Path $File.FullName -Raw

        # Pattern to match current Source line (either old style or packaged style)
        $OldPatterns = @(
            "Context Cascade: skills/packaged/$SkillName\.skill \(extract to view SKILL\.md\)",
            "Context Cascade: skills/[^/]+/$SkillName/SKILL\.md"
        )

        $NewSource = "Context Cascade: skills/$Category/$SkillName/SKILL.md"

        foreach ($Pattern in $OldPatterns) {
            if ($Content -match $Pattern) {
                $Content = $Content -replace $Pattern, $NewSource
                Set-Content -Path $File.FullName -Value $Content -NoNewline
                Write-Host "[SYNCED] $SkillName -> $Category" -ForegroundColor Green
                $Updated++
                break
            }
        }
    }
}

Write-Host ""
Write-Host "=== Summary ===" -ForegroundColor Cyan
Write-Host "Stubs synced: $Updated"
