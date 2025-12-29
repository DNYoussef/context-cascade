# Setup Scheduled Task for Cognitive Architecture MOO Optimization
# Runs every 3 days at 3:00 AM

$TaskName = "CognitiveArchMOO"
$ScriptPath = "$PSScriptRoot\run_scheduled_optimization.py"
$PythonPath = "python"  # Assumes python is in PATH

# Create the action
$Action = New-ScheduledTaskAction -Execute $PythonPath -Argument "$ScriptPath --days 3 --cascade" -WorkingDirectory $PSScriptRoot

# Create trigger (every 3 days at 3 AM)
$Trigger = New-ScheduledTaskTrigger -Daily -DaysInterval 3 -At "3:00AM"

# Create settings
$Settings = New-ScheduledTaskSettingsSet -StartWhenAvailable -DontStopOnIdleEnd

# Check if task exists and remove it
$ExistingTask = Get-ScheduledTask -TaskName $TaskName -ErrorAction SilentlyContinue
if ($ExistingTask) {
    Write-Host "Removing existing task..."
    Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false
}

# Register the task
Write-Host "Creating scheduled task: $TaskName"
Register-ScheduledTask -TaskName $TaskName -Action $Action -Trigger $Trigger -Settings $Settings -Description "Cognitive Architecture MOO Optimization (every 3 days)"

Write-Host ""
Write-Host "Task created successfully!"
Write-Host "  Name: $TaskName"
Write-Host "  Schedule: Every 3 days at 3:00 AM"
Write-Host "  Script: $ScriptPath"
Write-Host ""
Write-Host "To run manually: schtasks /run /tn `"$TaskName`""
Write-Host "To delete: schtasks /delete /tn `"$TaskName`" /f"
