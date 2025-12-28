---
name: github-project-management
description: Comprehensive GitHub project management with swarm-coordinated issue tracking, project board automation, and sprint planning
---

# GitHub Project Management

## Overview

A comprehensive skill for managing GitHub projects using AI swarm coordination. This skill combines intelligent issue management, automated project board synchronization, and swarm-based coordination for efficient project delivery.

## Quick Start

### Basic Issue Creation with Swarm Coordination

```bash
# Create a coordinated issue
gh issue create \
  --title "Feature: Advanced Authentication" \
  --body "Implement OAuth2 with social login..." \
  --label "enhancement,swarm-ready"

# Initialize swarm for issue
npx claude-flow@alpha hooks pre-task --description "Feature implementation"
```

### Project Board Quick Setup

```bash
# Get project ID
PROJECT_ID=$(gh project list --owner @me --format json | \
  jq -r '.projects[0].id')

# Initialize board sync
npx ruv-swarm github board-init \
  --project-id "$PROJECT_ID" \
  --sync-mode "bidirectional"
```

🤖 Automated update by swarm agent"')

gh issue comment 456 --body "$SUMMARY"

# Update labels based on progress
if [[ $(echo "$PROGRESS" | jq -r '.completion') -eq 100 ]]; then
  gh issue edit 456 --add-label "ready-for-review" --remove-label "in-progress"
fi
```

</details>

<details>
<summary><strong>Stale Issue Management</strong></summary>

#### Auto-Close Stale Issues with Swarm Analysis

```bash
# Find stale issues
STALE_DATE=$(date -d '30 days ago' --iso-8601)
STALE_ISSUES=$(gh issue list --state open --json number,title,updatedAt,labels \
  --jq ".[] | select(.updatedAt < \"$STALE_DATE\")")

# Analyze each stale issue
echo "$STALE_ISSUES" | jq -r '.number' | while read -r num; do
  # Get full issue context
  ISSUE=$(gh issue view $num --json title,body,comments,labels)

  # Analyze with swarm
  ACTION=$(npx ruv-swarm github analyze-stale \
    --issue "$ISSUE" \
    --suggest-action)

  case "$ACTION" in
    "close")
      gh issue comment $num --body "This issue has been inactive for 30 days and will be closed in 7 days if there's no further activity."
      gh issue edit $num --add-label "stale"
      ;;
    "keep")
      gh issue edit $num --remove-label "stale" 2>/dev/null || true
      ;;
    "needs-info")
      gh issue comment $num --body "This issue needs more information. Please provide additional context or it may be closed as stale."
      gh issue edit $num --add-label "needs-info"
      ;;
  esac
done

# Close issues that have been stale for 37+ days
gh issue list --label stale --state open --json number,updatedAt \
  --jq ".[] | select(.updatedAt < \"$(date -d '37 days ago' --iso-8601)\") | .number" | \
  while read -r num; do
    gh issue close $num --comment "Closing due to inactivity. Feel free to reopen if this is still relevant."
  done
```

</details>

### 2. Project Board Automation

<details>
<summary><strong>Board Initialization & Configuration</strong></summary>

#### Connect Swarm to GitHub Project

```bash
# Get project details
PROJECT_ID=$(gh project list --owner @me --format json | \
  jq -r '.projects[] | select(.title == "Development Board") | .id')

# Initialize swarm with project
npx ruv-swarm github board-init \
  --project-id "$PROJECT_ID" \
  --sync-mode "bidirectional" \
  --create-views "swarm-status,agent-workload,priority"

# Create project fields for swarm tracking
gh project field-create $PROJECT_ID --owner @me \
  --name "Swarm Status" \
  --data-type "SINGLE_SELECT" \
  --single-select-options "pending,in_progress,completed"
```

#### Board Mapping Configuration

```yaml
# .github/board-sync.yml
project:
  name: "AI Development Board"
  number: 1

mapping:
  # Map swarm task status to board columns
  status:
    pending: "Backlog"
    assigned: "Ready"
    in_progress: "In Progress"
    review: "Review"
    completed: "Done"
    blocked: "Blocked"

  # Map agent types to labels
  agents:
    coder: "🔧 Development"
    tester: "🧪 Testing"
    analyst: "📊 Analysis"
    designer: "🎨 Design"
    architect: "🏗️ Architecture"

  # Map priority to project fields
  priority:
    critical: "🔴 Critical"
    high: "🟡 High"
    medium: "🟢 Medium"
    low: "⚪ Low"

  # Custom fields
  fields:
    - name: "Agent Count"
      type: number
      source: task.agents.length
    - name: "Complexity"
      type: select
      source: task.complexity
    - name: "ETA"
      type: date
      source: task.estimatedCompletion
```

</details>

<details>
<summary><strong>Task Synchronization</strong></summary>

#### Real-time Board Sync

```bash
# Sync swarm tasks with project cards
npx ruv-swarm github board-sync \
  --map-status '{
    "todo": "To Do",
    "in_progress": "In Progress",
    "review": "Review",
    "done": "Done"
  }' \
  --auto-move-cards \
  --update-metadata

# Enable real-time board updates
npx ruv-swarm github board-realtime \
  --webhook-endpoint "https://api.example.com/github-sync" \
  --update-frequency "immediate" \
  --batch-updates false
```

#### Convert Issues to Project Cards

```bash
# List issues with label
ISSUES=$(gh issue list --label "enhancement" --json number,title,body)

# Add issues to project
echo "$ISSUES" | jq -r '.[].number' | while read -r issue; do
  gh project item-add $PROJECT_ID --owner @me --url "https://github.com/$GITHUB_REPOSITORY/issues/$issue"
done

# Process with swarm
npx ruv-swarm github board-import-issues \
  --issues "$ISSUES" \
  --add-to-column "Backlog" \
  --parse-checklist \
  --assign-agents
```

</details>

<details>
<summary><strong>Smart Card Management</strong></summary>

#### Auto-Assignment

```bash
# Automatically assign cards to agents
npx ruv-swarm github board-auto-assign \
  --strategy "load-balanced" \
  --consider "expertise,workload,availability" \
  --update-cards
```

#### Intelligent Card State Transitions

```bash
# Smart card movement based on rules
npx ruv-swarm github board-smart-move \
  --rules '{
    "auto-progress": "when:all-subtasks-done",
    "auto-review": "when:tests-pass",
    "auto-done": "when:pr-merged"
  }'
```

#### Bulk Operations

```bash
# Bulk card operations
npx ruv-swarm github board-bulk \
  --filter "status:blocked" \
  --action "add-label:needs-attention" \
  --notify-assignees
```

</details>

<details>
<summary><strong>Custom Views & Dashboards</strong></summary>

#### View Configuration

```javascript
// Custom board views
{
  "views": [
    {
      "name": "Swarm Overview",
      "type": "board",
      "groupBy": "status",
      "filters": ["is:open"],
      "sort": "priority:desc"
    },
    {
      "name": "Agent Workload",
      "type": "table",
      "groupBy": "assignedAgent",
      "columns": ["title", "status", "priority", "eta"],
      "sort": "eta:asc"
    },
    {
      "name": "Sprint Progress",
      "type": "roadmap",
      "dateField": "eta",
      "groupBy": "milestone"
    }
  ]
}
```

#### Dashboard Configuration

```javascript
// Dashboard with performance widgets
{
  "dashboard": {
    "widgets": [
      {
        "type": "chart",
        "title": "Task Completion Rate",
        "data": "completed-per-day",
        "visualization": "line"
      },
      {
        "type": "gauge",
        "title": "Sprint Progress",
        "data": "sprint-completion",
        "target": 100
      },
      {
        "type": "heatmap",
        "title": "Agent Activity",
        "data": "agent-tasks-per-day"
      }
    ]
  }
}
```

</details>

### 3. Sprint Planning & Tracking

<details>
<summary><strong>Sprint Management</strong></summary>

#### Initialize Sprint with Swarm Coordination

```bash
# Manage sprints with swarms
npx ruv-swarm github sprint-manage \
  --sprint "Sprint 23" \
  --auto-populate \
  --capacity-planning \
  --track-velocity

# Track milestone progress
npx ruv-swarm github milestone-track \
  --milestone "v2.0 Release" \
  --update-board \
  --show-dependencies \
  --predict-completion
```

#### Agile Development Board Setup

```bash
# Setup agile board
npx ruv-swarm github agile-board \
  --methodology "scrum" \
  --sprint-length "2w" \
  --ceremonies "planning,review,retro" \
  --metrics "velocity,burndown"
```

#### Kanban Flow Board Setup

```bash
# Setup kanban board
npx ruv-swarm github kanban-board \
  --wip-limits '{
    "In Progress": 5,
    "Review": 3
  }' \
  --cycle-time-tracking \
  --continuous-flow
```

</details>

<details>
<summary><strong>Progress Tracking & Analytics</strong></summary>

#### Board Analytics

```bash
# Fetch project data
PROJECT_DATA=$(gh project item-list $PROJECT_ID --owner @me --format json)

# Get issue metrics
ISSUE_METRICS=$(echo "$PROJECT_DATA" | jq -r '.items[] | select(.content.type == "Issue")' | \
  while read -r item; do
    ISSUE_NUM=$(echo "$item" | jq -r '.content.number')
    gh issue view $ISSUE_NUM --json createdAt,closedAt,labels,assignees
  done)

# Generate analytics with swarm
npx ruv-swarm github board-analytics \
  --project-data "$PROJECT_DATA" \
  --issue-metrics "$ISSUE_METRICS" \
  --metrics "throughput,cycle-time,wip" \
  --group-by "agent,priority,type" \
  --time-range "30d" \
  --export "dashboard"
```

#### Performance Reports

```bash
# Track and visualize progress
npx ruv-swarm github board-progress \
  --show "burndown,velocity,cycle-time" \
  --time-period "sprint" \
  --export-metrics

# Generate reports
npx ruv-swarm github board-report \
  --type "sprint-summary" \
  --format "markdown" \
  --include "velocity,burndown,blockers" \
  --distribute "slack,email"
```

#### KPI Tracking

```bash
# Track board performance
npx ruv-swarm github board-kpis \
  --metrics '[
    "average-cycle-time",
    "throughput-per-sprint",
    "blocked-time-percentage",
    "first-time-pass-rate"
  ]' \
  --dashboard-url

# Track team performance
npx ruv-swarm github team-metrics \
  --board "Development" \
  --per-member \
  --include "velocity,quality,collaboration" \
  --anonymous-option
```

</details>

<details>
<summary><strong>Release Planning</strong></summary>

#### Release Coordination

```bash
# Plan releases using board data
npx ruv-swarm github release-plan-board \
  --analyze-velocity \
  --estimate-completion \
  --identify-risks \
  --optimize-scope
```

</details>

### 4. Advanced Coordination

<details>
<summary><strong>Multi-Board Synchronization</strong></summary>

#### Cross-Board Sync

```bash
# Sync across multiple boards
npx ruv-swarm github multi-board-sync \
  --boards "Development,QA,Release" \
  --sync-rules '{
    "Development->QA": "when:ready-for-test",
    "QA->Release": "when:tests-pass"
  }'

# Cross-organization sync
npx ruv-swarm github cross-org-sync \
  --source "org1/Project-A" \
  --target "org2/Project-B" \
  --field-mapping "custom" \
  --conflict-resolution "source-wins"
```

</details>

<details>
<summary><strong>Issue Dependencies & Epic Management</strong></summary>

#### Dependency Resolution

```bash
# Handle issue dependencies
npx ruv-swarm github issue-deps 456 \
  --resolve-order \
  --parallel-safe \
  --update-blocking
```

#### Epic Coordination

```bash
# Coordinate epic-level swarms
npx ruv-swarm github epic-swarm \
  --epic 123 \
  --child-issues "456,457,458" \
  --orchestrate
```

</details>

<details>
<summary><strong>Cross-Repository Coordination</strong></summary>

#### Multi-Repo Issue Management

```bash
# Handle issues across repositories
npx ruv-swarm github cross-repo \
  --issue "org/repo#456" \
  --related "org/other-repo#123" \
  --coordinate
```

</details>

<details>
<summary><strong>Team Collaboration</strong></summary>

#### Work Distribution

```bash
# Distribute work among team
npx ruv-swarm github board-distribute \
  --strategy "skills-based" \
  --balance-workload \
  --respect-preferences \
  --notify-assignments
```

#### Standup Automation

```bash
# Generate standup reports
npx ruv-swarm github standup-report \
  --team "frontend" \
  --include "yesterday,today,blockers" \
  --format "slack" \
  --schedule "daily-9am"
```

#### Review Coordination

```bash
# Coordinate reviews via board
npx ruv-swarm github review-coordinate \
  --board "Code Review" \
  --assign-reviewers \
  --track-feedback \
  --ensure-coverage
```

</details>

🤖 Generated with Claude Code
```

### Bug Report Template

```markdown
## 🐛 Bug Report

### Problem Description
[Clear description of the issue]

### Expected Behavior
[What should happen]

### Actual Behavior
[What actually happens]

### Reproduction Steps
1. [Step 1]
2. [Step 2]
3. [Step 3]

### Environment
- Package: [package name and version]
- Node.js: [version]
- OS: [operating system]

### Investigation Plan
- [ ] Root cause analysis
- [ ] Fix implementation
- [ ] Testing and validation
- [ ] Regression testing

### Swarm Assignment
- **Debugger**: Issue investigation
- **Coder**: Fix implementation
- **Tester**: Validation and testing

🤖 Generated with Claude Code
```

### Swarm Task Template

```markdown
<!-- .github/ISSUE_TEMPLATE/swarm-task.yml -->

body:
  - type: dropdown
    id: topology
    attributes:
      label: Swarm Topology
      options:
        - mesh
        - hierarchical
        - ring
        - star
  - type: input
    id: agents
    attributes:
      label: Required Agents
      placeholder: "coder, tester, analyst"
  - type: textarea
    id: tasks
    attributes:
      label: Task Breakdown
      placeholder: |
        1. Task one description
        2. Task two description
```

## Specialized Issue Strategies

### Bug Investigation Swarm

```bash
# Specialized bug handling
npx ruv-swarm github bug-swarm 456 \
  --reproduce \
  --isolate \
  --fix \
  --test
```

### Feature Implementation Swarm

```bash
# Feature implementation swarm
npx ruv-swarm github feature-swarm 456 \
  --design \
  --implement \
  --document \
  --demo
```

### Technical Debt Refactoring

```bash
# Refactoring swarm
npx ruv-swarm github debt-swarm 456 \
  --analyze-impact \
  --plan-migration \
  --execute \
  --validate
```

## Troubleshooting

### Sync Issues

```bash
# Diagnose sync problems
npx ruv-swarm github board-diagnose \
  --check "permissions,webhooks,rate-limits" \
  --test-sync \
  --show-conflicts
```

### Performance Optimization

```bash
# Optimize board performance
npx ruv-swarm github board-optimize \
  --analyze-size \
  --archive-completed \
  --index-fields \
  --cache-views
```

### Data Recovery

```bash
# Recover board data
npx ruv-swarm github board-recover \
  --backup-id "2024-01-15" \
  --restore-cards \
  --preserve-current \
  --merge-conflicts
```

## Security & Permissions

1. **Command Authorization**: Validate user permissions before executing commands
2. **Rate Limiting**: Prevent spam and abuse of issue commands
3. **Audit Logging**: Track all swarm operations on issues and boards
4. **Data Privacy**: Respect private repository settings
5. **Access Control**: Proper GitHub permissions for board operations
6. **Webhook Security**: Secure webhook endpoints for real-time updates

## Complete Workflow Example

### Full-Stack Feature Development

```bash
# 1. Create feature issue with swarm coordination
gh issue create \
  --title "Feature: Real-time Collaboration" \
  --body "$(cat <<EOF
## Feature: Real-time Collaboration

### Overview
Implement real-time collaboration features using WebSockets.

### Objectives
- [ ] WebSocket server setup
- [ ] Client-side integration
- [ ] Presence tracking
- [ ] Conflict resolution
- [ ] Testing and documentation

### Swarm Coordination
This feature will use mesh topology for parallel development.
EOF
)" \
  --label "enhancement,swarm-ready,high-priority"

# 2. Initialize swarm and decompose tasks
ISSUE_NUM=$(gh issue list --label "swarm-ready" --limit 1 --json number --jq '.[0].number')
npx ruv-swarm github issue-init $ISSUE_NUM \
  --topology mesh \
  --auto-decompose \
  --assign-agents "architect,coder,tester"

# 3. Add to project board
PROJECT_ID=$(gh project list --owner @me --format json | jq -r '.projects[0].id')
gh project item-add $PROJECT_ID --owner @me \
  --url "https://github.com/$GITHUB_REPOSITORY/issues/$ISSUE_NUM"

# 4. Set up automated tracking
npx ruv-swarm github board-sync \
  --auto-move-cards \
  --update-metadata

# 5. Monitor progress
npx ruv-swarm github issue-progress $ISSUE_NUM \
  --auto-update-comments \
  --notify-on-completion
```

## Additional Resources

- [GitHub CLI Documentation](https://cli.github.com/manual/)
- [GitHub Projects Documentation](https://docs.github.com/en/issues/planning-and-tracking-with-projects)
- [Swarm Coordination Guide](https://github.com/ruvnet/ruv-swarm)
- [Claude Flow Documentation](https://github.com/ruvnet/claude-flow)

## Core Principles

GitHub Project Management operates on 3 fundamental principles:

### Principle 1: Bidirectional Board Synchronization
Project boards are living documents, not static snapshots. Changes in code, PRs, and issues must automatically flow to boards, and board state changes must propagate to development workflow.

In practice:
- Implement real-time board sync with GitHub Actions webhooks (issue state -> card movement)
- Map swarm agent task statuses to project board columns automatically
- Use custom fields to track swarm-specific metadata (agent count, complexity, ETA)

### Principle 2: Task Decomposition with Dependency Tracking
Large issues become unmanageable without decomposition. Break down epics into actionable subtasks with explicit dependency chains.

In practice:
- Use swarm agents to automatically decompose issues into 5-10 subtasks with priority ranking
- Track dependencies between subtasks using checklist linking (#456 blocks #457)
- Prevent premature work on blocked tasks through automated status validation

### Principle 3: Progress Transparency Through Automated Updates
Manual status updates are always stale. Automate progress tracking through swarm agent reporting and checklist completion monitoring.

In practice:
- Swarm agents post automated progress updates with completion percentages and ETA
- Use checklist parsing to calculate issue completion metrics (5/10 tasks done = 50%)
- Generate sprint burndown and velocity charts from automated progress data

-----------|---------|----------|
| **Manual Board Updates** | Team members forget to move cards, leading to stale board state that doesn't reflect reality | Implement automated board sync with GitHub Actions. Map issue state changes to column transitions |
| **Monolithic Issues Without Subtasks** | Large issues (>8 hours) with single checkbox are impossible to track progress mid-sprint | Use swarm task decomposition to break issues into 5-10 actionable subtasks with dependencies |
| **Stale Issues Without Triage** | Unlabeled and unprioritized issues accumulate, making backlog unmanageable | Implement automated triage with swarm content analysis to suggest labels and priority based on keywords |
| **No Sprint Velocity Tracking** | Teams can't estimate capacity or predict sprint completion without historical velocity data | Use swarm analytics to calculate throughput, cycle time, and velocity from historical issue data |
| **Missing Cross-Repo Coordination** | Multi-repo projects lack unified view of progress when issues span repositories | Use swarm cross-repo coordination to link related issues and synchronize project boards |

---

## Conclusion

GitHub Project Management transforms project boards from static planning tools into dynamic, AI-coordinated execution hubs. By combining swarm-based issue decomposition, automated board synchronization, and intelligent progress tracking, it enables teams to maintain up-to-date project state without manual overhead.

This skill is essential when managing Agile/Scrum workflows on GitHub Projects, coordinating multi-repository development efforts, or tracking complex features with many interdependent tasks. It excels at automated triage, dependency management, and progress transparency that manual board updates cannot sustain.

Use this skill when setting up project boards for new teams, when existing boards have low adoption due to manual update burden, or when you need cross-repository sprint coordination with unified reporting. The swarm coordination patterns enable parallel task decomposition, automated progress updates, and intelligent work distribution that traditional project management tools require manual effort to achieve.