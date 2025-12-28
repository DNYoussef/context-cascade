---
name: when-managing-github-projects-use-github-project-management
description: Comprehensive GitHub project management with swarm-coordinated issue tracking, project board automation, and sprint planning. Coordinates planner, issue-tracker, and project-board-sync agents to automate issue triage, sprint planning, milestone tracking, and project board updates. Integrates with GitHub Projects v2 API for advanced automation, custom fields, and workflow orchestration. Use when managing development projects, coordinating team workflows, or automating project management tasks.
---

# GitHub Project Management Skill

## Overview

Automate and orchestrate GitHub project management workflows using intelligent agent coordination. This skill provides comprehensive project management capabilities including automated issue triage, sprint planning, milestone tracking, project board synchronization, and team coordination through GitHub Projects v2 integration.

## When to Use This Skill

Activate this skill when planning and executing development sprints, managing issue backlogs and triage queues, coordinating work across distributed teams, automating project board updates and status tracking, tracking milestones and release schedules, or establishing project management workflows for new teams.

Use for both small team projects (2-5 developers) and large-scale coordination (10+ team members), agile/scrum sprint management, kanban-style continuous delivery, or hybrid project management approaches.

## Agent Coordination Architecture

### Swarm Topology

Initialize a **star topology** with a central coordinator agent managing specialized agents for issue tracking, planning, and board synchronization. Star topology enables centralized control with efficient communication to specialized agents.

```bash
# Initialize star swarm for project management
npx claude-flow@alpha swarm init --topology star --max-agents 6 --strategy balanced
```

### Specialized Agent Roles

**Central Coordinator** (`coordinator`): Hub agent that orchestrates all project management activities. Makes prioritization decisions, coordinates between teams, and ensures consistency across project artifacts. Acts as project manager.

**Planner** (`planner`): Handles sprint planning, capacity estimation, and resource allocation. Creates sprint goals, breaks down epics into stories, estimates effort, and balances workload across team members.

**Issue Tracker** (`issue-tracker`): Automates issue triage, labeling, assignment, and lifecycle management. Monitors new issues, applies initial classification, routes to appropriate team members, and tracks resolution progress.

**Project Board Sync** (`project-board-sync`): Maintains GitHub Projects v2 boards, updates issue status, manages custom fields, and enforces workflow automation. Ensures boards accurately reflect current project state.

## Project Management Workflows (SOP)

### Workflow 1: Automated Issue Triage

Process incoming issues with intelligent classification and routing.

**Phase 1: Issue Ingestion**

**Step 1.1: Initialize Star Topology**

```bash
# Set up star swarm with coordinator hub
mcp__claude-flow__swarm_init topology=star maxAgents=6 strategy=balanced

# Spawn coordinator and specialists
mcp__claude-flow__agent_spawn type=coordinator name=coordinator
mcp__claude-flow__agent_spawn type=researcher name=issue-tracker
mcp__claude-flow__agent_spawn type=researcher name=planner
mcp__claude-flow__agent_spawn type=coordinator name=project-board-sync
```

**Step 1.2: Monitor New Issues**

Set up real-time monitoring for new issues:

```bash
# Subscribe to new issues
bash scripts/github-webhook.sh subscribe \
  --repo <owner/repo> \
  --events "issues" \
  --callback "scripts/process-new-issue.sh"
```

Or use MCP real-time subscription if Flow-Nexus available:

```bash
mcp__flow-nexus__realtime_subscribe table=issues event=INSERT
```

**Step 1.3: Fetch Issue Details**

When new issue created, fetch comprehensive context:

```bash
# Get issue details with comments and reactions
bash scripts/github-api.sh fetch-issue \
  --repo <owner/repo> \
  --issue <number> \
  --include-comments true
```

**Phase 2: Intelligent Classification**

**Step 2.1: Analyze Issue Content**

```plaintext
Task("Issue Tracker", "
  Analyze and classify new issue #<NUMBER>:

  1. Read issue body and comments from memory: github/issues/<NUMBER>
  2. Classify issue type: bug|feature|enhancement|documentation|question
  3. Determine severity: critical|high|medium|low
  4. Identify affected components using references/component-map.md
  5. Estimate complexity: simple|moderate|complex
  6. Check for duplicates using similarity search
  7. Extract key entities: affected files, error messages, user impact

  Use scripts/issue-classifier.sh for ML-based classification
  Store classification in memory: github/triage/<NUMBER>
  Run hooks: npx claude-flow@alpha hooks pre-task --description 'issue triage'
", "issue-tracker")
```

**Step 2.2: Apply Labels and Metadata**

Based on classification, apply appropriate labels:

```bash
# Apply automated labels
bash scripts/github-api.sh add-labels \
  --repo <owner/repo> \
  --issue <number> \
  --labels "<type>,<severity>,<component>"

# Set custom fields in project board
bash scripts/project-api.sh set-field \
  --project <project-id> \
  --issue <number> \
  --field "Complexity" \
  --value "<complexity>"
```

**Step 2.3: Assign Team Member**

Route to appropriate team member based on expertise:

```plaintext
Task("Coordinator", "
  Assign issue #<NUMBER> to appropriate team member:

  1. Review team expertise map in references/team-skills.md
  2. Check current workload using scripts/team-capacity.sh
  3. Match issue requirements with team member skills
  4. Consider time zone and availability
  5. Assign issue via GitHub API

  Store assignment decision in memory: github/assignments/<NUMBER>
", "coordinator")
```

```bash
# Assign issue
bash scripts/github-api.sh assign-issue \
  --repo <owner/repo> \
  --issue <number> \
  --assignee <username>
```

**Phase 3: Priority and Milestone Assignment**

**Step 3.1: Determine Priority**

```plaintext
Task("Planner", "
  Prioritize issue #<NUMBER> within backlog:

  1. Assess business impact (user-facing, revenue, compliance)
  2. Evaluate technical risk (security, stability, data loss)
  3. Consider dependencies (blocking other work?)
  4. Review stakeholder input from issue comments
  5. Calculate priority score using references/priority-matrix.md

  Store priority in memory: github/priorities/<NUMBER>
", "planner")
```

**Step 3.2: Assign to Milestone**

Based on priority and current sprint capacity:

```bash
# Add to appropriate milestone
bash scripts/github-api.sh set-milestone \
  --repo <owner/repo> \
  --issue <number> \
  --milestone "<sprint-name>"
```

**Step 3.3: Update Project Board**

```plaintext
Task("Project Board Sync", "
  Add issue #<NUMBER> to project board:

  1. Determine appropriate project board (team, initiative, sprint)
  2. Add issue to board in 'Triage' column
  3. Set custom fields: Priority, Complexity, Sprint, Team
  4. Link related issues and PRs
  5. Add to sprint view if assigned to active sprint

  Use scripts/project-api.sh for Projects v2 API
  Store board update in memory: github/boards/<NUMBER>
", "project-board-sync")
```

### Workflow 2: Sprint Planning Automation

Plan and execute development sprints with agent coordination.

**Phase 1: Sprint Preparation**

**Step 1.1: Analyze Team Capacity**

```bash
# Calculate available capacity for next sprint
bash scripts/team-capacity.sh calculate \
  --team <team-name> \
  --start-date <YYYY-MM-DD> \
  --duration-days 14 \
  --include-pto true \
  --output references/sprint-capacity.json
```

**Step 1.2: Review Backlog**

```plaintext
Task("Planner", "
  Prepare sprint planning meeting:

  1. Fetch all backlog items using scripts/github-api.sh list-issues
  2. Filter by priority (high and critical first)
  3. Identify dependencies between issues
  4. Group related issues into themes
  5. Create preliminary sprint proposal based on capacity

  Reference references/sprint-capacity.json for team availability
  Store sprint proposal in memory: github/sprint/proposal
", "planner")
```

**Phase 2: Sprint Composition**

**Step 2.1: Create Sprint Milestone**

```bash
# Create new sprint milestone
bash scripts/github-api.sh create-milestone \
  --repo <owner/repo> \
  --title "Sprint <number>: <theme>" \
  --due-date <YYYY-MM-DD> \
  --description "Sprint goals: ..."
```

**Step 2.2: Assign Issues to Sprint**

```plaintext
Task("Coordinator", "
  Compose sprint backlog:

  1. Review planner's proposal from memory: github/sprint/proposal
  2. Validate capacity vs proposed work
  3. Ensure mix of feature work, bugs, and technical debt
  4. Balance workload across team members
  5. Assign issues to sprint milestone
  6. Create sprint goal document

  Use scripts/sprint-composer.sh for optimization
  Store final sprint composition in memory: github/sprint/final
", "coordinator")
```

**Step 2.3: Initialize Sprint Board**

```bash
# Create sprint project board
bash scripts/project-api.sh create-sprint-board \
  --title "Sprint <number>" \
  --template "references/sprint-board-template.json" \
  --issues-milestone "<milestone-name>"
```

**Phase 3: Sprint Execution Tracking**

**Step 3.1: Daily Status Updates**

```plaintext
Task("Project Board Sync", "
  Update sprint board daily:

  1. Sync issue statuses from PR activity
  2. Move completed issues to 'Done' column
  3. Flag blocked issues with 'blocked' label
  4. Update burndown chart data
  5. Identify issues without recent activity
  6. Generate daily standup summary

  Use scripts/sprint-tracker.sh for automation
  Store daily metrics in memory: github/sprint/daily/<DATE>
", "project-board-sync")
```

**Step 3.2: Generate Sprint Reports**

```bash
# Generate sprint health report
bash scripts/sprint-reporter.sh generate \
  --sprint "<milestone-name>" \
  --metrics "velocity,burndown,completion-rate,blocked-count" \
  --output "references/sprint-report-<DATE>.md"
```

**Step 3.3: Sprint Retrospective Data**

At sprint end, collect retrospective data:

```plaintext
Task("Planner", "
  Prepare sprint retrospective report:

  1. Calculate actual vs planned velocity
  2. Analyze completion rate by issue type
  3. Identify bottlenecks and blockers
  4. Collect cycle time metrics
  5. Generate improvement recommendations

  Use scripts/sprint-analytics.sh for metrics
  Store retrospective in memory: github/sprint/retro
", "planner")
```

### Workflow 3: Milestone and Release Tracking

Track progress toward major milestones and releases.

**Phase 1: Milestone Definition**

**Step 1.1: Create Milestone Structure**

```bash
# Create milestone with metadata
bash scripts/github-api.sh create-milestone \
  --repo <owner/repo> \
  --title "v2.0.0 Release" \
  --due-date <YYYY-MM-DD> \
  --description "$(cat references/v2-release-plan.md)"
```

**Step 1.2: Break Down Release Plan**

```plaintext
Task("Planner", "
  Decompose release plan into actionable items:

  1. Read release requirements from references/v2-release-plan.md
  2. Break down features into user stories
  3. Create issues for each story with acceptance criteria
  4. Estimate effort for each issue
  5. Assign to milestone
  6. Identify dependencies and critical path

  Use scripts/release-planner.sh for decomposition
  Store release breakdown in memory: github/releases/v2.0.0
", "planner")
```

**Phase 2: Progress Monitoring**

**Step 2.1: Track Milestone Progress**

```bash
# Generate milestone progress report
bash scripts/milestone-tracker.sh report \
  --milestone "v2.0.0 Release" \
  --include-burndown true \
  --output "references/milestone-progress.md"
```

**Step 2.2: Identify Risks**

```plaintext
Task("Coordinator", "
  Monitor release health and identify risks:

  1. Check milestone progress vs timeline
  2. Identify issues at risk of missing deadline
  3. Flag critical path issues with blockers
  4. Assess scope creep (new issues added to milestone)
  5. Generate risk mitigation recommendations

  Use scripts/risk-analyzer.sh
  Store risk assessment in memory: github/releases/risks
", "coordinator")
```

**Step 2.3: Stakeholder Communication**

```bash
# Generate stakeholder update
bash scripts/stakeholder-report.sh generate \
  --milestone "v2.0.0 Release" \
  --format "executive-summary" \
  --include-risks true \
  --output "references/stakeholder-update-<DATE>.md"
```

**Phase 3: Release Coordination**

**Step 3.1: Pre-Release Checklist**

```plaintext
Task("Project Board Sync", "
  Validate release readiness:

  1. Verify all milestone issues completed
  2. Check PR review status for milestone
  3. Validate CI/CD pipeline status
  4. Confirm documentation updates
  5. Check release notes completeness
  6. Verify deployment plan exists

  Use references/release-checklist.md
  Store readiness status in memory: github/releases/readiness
", "project-board-sync")
```

**Step 3.2: Create Release**

```bash
# Create GitHub release
bash scripts/github-api.sh create-release \
  --repo <owner/repo> \
  --tag "v2.0.0" \
  --name "Version 2.0.0" \
  --body-file "references/release-notes-v2.0.0.md" \
  --prerelease false
```

## Advanced Features

### Custom Field Automation

Configure GitHub Projects v2 custom fields with automated updates:

```bash
# Set up custom field automation
bash scripts/project-api.sh configure-fields \
  --project <project-id> \
  --config "references/custom-fields.json"
```

Custom field examples:
- **Complexity**: Auto-calculate from file changes
- **Priority Score**: Weighted algorithm based on impact/urgency
- **Cycle Time**: Auto-track time from start to completion
- **Review Status**: Sync with PR approval status
- **Team**: Auto-assign based on component ownership

### Integration with External Tools

Connect project management with external systems:

```bash
# Sync with Jira
bash scripts/external-sync.sh jira \
  --project <jira-project> \
  --github-repo <owner/repo> \
  --sync-direction "bidirectional"

# Push to Slack
bash scripts/notifications.sh slack \
  --webhook <slack-webhook> \
  --events "issue-created,pr-merged,milestone-completed"
```

### Analytics and Insights

Generate comprehensive project analytics:

```bash
# Run analytics suite
bash scripts/project-analytics.sh analyze \
  --repo <owner/repo> \
  --period "last-quarter" \
  --metrics "velocity,lead-time,cycle-time,throughput" \
  --visualize true \
  --output "references/analytics-report.html"
```

## MCP Tool Integration

### Task Orchestration

```bash
# Orchestrate complex project management workflow
mcp__claude-flow__task_orchestrate \
  task="Plan and initialize Sprint 42" \
  strategy=sequential \
  maxAgents=4 \
  priority=high
```

### Swarm Monitoring

```bash
# Monitor project management agent activity
mcp__claude-flow__swarm_status verbose=true

# Get agent performance metrics
mcp__claude-flow__agent_metrics metric=tasks
```

## Best Practices

**Consistent Labeling**: Use standardized label taxonomy across all repositories. Document label meanings in `references/label-taxonomy.md`.

**Automated Triage**: Run triage automation within 1 hour of issue creation to ensure responsive project management.

**Capacity Planning**: Always validate sprint capacity before committing work. Include buffer for unplanned work and meetings.

**Board Hygiene**: Run daily board sync to keep project boards accurate. Stale boards reduce team trust in project management.

**Retrospective Action**: Convert retrospective insights into concrete process improvements. Track improvement initiatives as issues.

**Clear Ownership**: Every issue should have exactly one assignee. Shared ownership leads to unclear accountability.

**Regular Communication**: Generate automated status reports for stakeholders. Transparency builds trust and reduces status meetings.

## Error Handling

**API Rate Limiting**: Implement caching and batching for GitHub API calls. Use GraphQL for complex queries to reduce request count.

**Conflict Resolution**: If issue assigned to multiple milestones, coordinator resolves based on priority and capacity constraints.

**Missing Data**: If issue lacks required classification data, flag for human review rather than making incorrect assumptions.

**Board Sync Failures**: Maintain local state cache to recover from transient API failures. Retry with exponential backoff.

## References

- `references/priority-matrix.md` - Issue prioritization framework
- `references/team-skills.md` - Team member expertise and capacity
- `references/component-map.md` - Repository component ownership
- `references/sprint-board-template.json` - Sprint board configuration
- `references/custom-fields.json` - Projects v2 custom field definitions
- `references/label-taxonomy.md` - Standardized label system
- `references/release-checklist.md` - Release readiness validation
- `scripts/github-api.sh` - GitHub REST/GraphQL API utilities
- `scripts/project-api.sh` - GitHub Projects v2 API integration
- `scripts/issue-classifier.sh` - ML-based issue classification
- `scripts/team-capacity.sh` - Team capacity calculation
- `scripts/sprint-tracker.sh` - Sprint progress tracking
- `scripts/milestone-tracker.sh` - Milestone monitoring
- `scripts/project-analytics.sh` - Project metrics and insights

## Core Principles

### 1. Metadata is Project Memory, Not Decoration
Labels, custom fields, and milestones are not cosmetic organization tools - they are the distributed memory system for your project. When an issue is labeled "high-priority, backend, security", that metadata enables automated routing (issue-tracker agent assigns to backend security specialist), priority sorting (planner agent schedules in current sprint), and historical analysis (project-analytics generates "security issues resolved per sprint" trends). Without rich metadata, automation degrades to manual triage and agents lose context.

**In practice**: Define label taxonomy in `references/label-taxonomy.md` covering type (bug/feature/docs), severity (critical/high/medium/low), component (backend/frontend/infra), and lifecycle (triage/in-progress/review/done). Every issue MUST have at minimum: one type label, one severity label, one component label. This enables 90% of automation workflows to function without human intervention.

### 2. Board State Reflects Reality, Not Aspirations
Project boards lose value when they diverge from actual work status. The "In Progress" column showing 15 issues while only 3 have recent commits signals organizational dysfunction - teams stop trusting the board and revert to Slack threads for status updates. Board hygiene is not optional maintenance, it is the foundation of distributed coordination across time zones and asynchronous workflows.

**In practice**: Run `project-board-sync` agent daily (automated via cron or GitHub Actions). This agent: syncs issue status from PR activity (PR opened = "In Review", PR merged = "Done"), flags stale issues (no activity for 7 days = "blocked" label + comment requesting update), updates burndown chart data (calculates remaining work vs sprint timeline), and generates daily standup summary (auto-posts to team Slack channel). Zero manual board updates required.

### 3. Capacity Planning is Physics, Not Estimation Theater
Sprint capacity is governed by hard constraints: available developer-hours (team size x working days x hours per day x utilization rate), task dependencies (critical path determines minimum timeline), and historical velocity (past performance predicts future capacity). Teams that ignore these constraints enter perpetual overcommitment cycles - sprints end with 40% completion rates, burnout increases, and planning meetings devolve into arguing about why estimates were wrong instead of delivering value.

**In practice**: Use `scripts/team-capacity.sh` to calculate objective capacity: If team has 5 developers, 10-day sprint, 6 productive hours per day, 0.75 utilization (accounting for meetings, interruptions, PTO), capacity is 5 x 10 x 6 x 0.75 = 225 developer-hours. Historical velocity shows team completes 200 hours per sprint on average. Planner agent commits maximum 180 hours to new work (90% of historical velocity, leaving buffer for unplanned work). This eliminates estimation arguments and creates predictable delivery.

## Anti-Patterns

| Anti-Pattern | Problem | Solution |
|-------------|---------|----------|
| **Manual Issue Triage as Bottleneck** | New issues sit unassigned for 24+ hours because product manager is in back-to-back meetings. Team doesn't know what to work on next. Velocity drops 30% due to context switching as developers self-assign issues without priority context. | Automate triage with `issue-tracker` agent running on webhook (issue created -> classify type/severity/component -> assign based on `references/team-skills.md` -> add to appropriate milestone -> post to team channel). Triage latency drops from 24 hours to <5 minutes. Human involvement only for edge cases (ambiguous requirements, cross-team dependencies). |
| **Sprint Planning Without Capacity Validation** | Team commits to 25 story points in sprint planning. Halfway through sprint, 3 developers take PTO (forgotten during planning), 2 critical bugs discovered (unplanned work), 1 dependency blocked (external API delayed). Sprint ends with 12 points completed, team morale drops, stakeholders lose trust. | Run `scripts/team-capacity.sh` BEFORE sprint planning to get objective capacity (accounts for PTO, holidays, on-call rotations). Planner agent validates proposed sprint backlog against capacity: If backlog = 280 hours but capacity = 180 hours, agent flags overcommitment and recommends removing 100 hours of work. Include 20% buffer for unplanned work (bugs, production incidents, support requests). |
| **Stale Boards as Single Source of Lies** | Project board shows "In Progress: 42 issues, Done: 8 issues" but actual code commits show 30 PRs merged this week. Team stops looking at board because it's inaccurate. Manager asks "what's the status?" and gets 5 different answers from 5 developers because there's no shared reality. Coordination breaks down. | Enable automated board sync: `project-board-sync` agent runs daily via cron. Syncs issue status from Git activity (last commit <24h ago = In Progress, PR merged = Done, no activity for 7 days = Blocked). Human intervention only needed for blocked issues requiring escalation. Board becomes automatic byproduct of actual development work, not manual status reporting theater. |

## Common Anti-Patterns

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| **Manual Issue Triage as Bottleneck** | New issues sit unassigned for 24+ hours because PM is in meetings. Team doesn't know what to work on. Velocity drops 30% from context switching as devs self-assign without priority context. | Automate triage with issue-tracker agent on webhook (issue created -> classify type/severity/component -> assign based on team-skills.md -> add to milestone -> post to team channel). Triage latency drops from 24h to <5min. Human involvement only for edge cases. |
| **Sprint Planning Without Capacity** | Team commits to 25 story points. Mid-sprint: 3 devs take PTO (forgotten), 2 critical bugs (unplanned), 1 dependency blocked. Sprint ends with 12 points completed, morale drops, stakeholders lose trust. | Run team-capacity.sh BEFORE sprint planning for objective capacity (accounts for PTO, holidays, on-call). Planner validates proposed backlog vs capacity. If backlog=280h but capacity=180h, flag overcommitment. Include 20% buffer for unplanned work. |
| **Stale Boards as Source of Lies** | Board shows "In Progress: 42, Done: 8" but git shows 30 PRs merged this week. Team stops trusting board. Manager gets 5 different status answers from 5 devs. Coordination breaks down. | Enable automated board sync: project-board-sync agent runs daily via cron. Syncs status from git activity (last commit <24h = In Progress, PR merged = Done, no activity 7d = Blocked). Board becomes automatic byproduct of dev work, not manual status theater. |

---

## Conclusion

GitHub project management automation transforms project boards from status reporting overhead into distributed coordination infrastructure. The workflows documented here (automated issue triage, sprint planning with capacity validation, milestone tracking with risk analysis) eliminate 80% of manual project management work while improving accuracy and responsiveness. The key insight: project management is a coordination problem, not a documentation problem.

Effective automation requires three foundations: rich metadata (labels, custom fields, milestones provide routing and prioritization data), automated synchronization (boards reflect actual development activity via `project-board-sync` agent), and objective capacity planning (`team-capacity.sh` provides physics-based constraints for sprint commitments). Without these foundations, automation degrades to brittle scripts that break on edge cases.

The agent coordination patterns (star topology with central coordinator, specialized agents for triage/planning/board-sync) enable parallel processing of project management workflows while maintaining consistency. This is critical for distributed teams spanning time zones - automation doesn't sleep, doesn't forget, and doesn't get stuck in meetings. The human role shifts from manual status tracking to high-leverage decision making: resolving ambiguous requirements, handling cross-team dependencies, and setting strategic direction.

Implementation recommendation: Start with automated issue triage (highest ROI, minimal complexity), then add board synchronization (eliminates manual status updates), then integrate capacity planning (prevents overcommitment cycles). Full automation deployment typically takes 2-4 weeks but pays back within first sprint through reduced coordination overhead and improved delivery predictability.