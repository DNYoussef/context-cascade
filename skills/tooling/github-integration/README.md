# GitHub Integration Hub

Coordinate GitHub-focused subskills (PR reviews, multi-repo, project management, releases, workflow automation) with consistent guardrails.

## Quick Start
1. Identify request type and route to the correct subskill.
2. Confirm repo scope, permissions, and risk level; configure MCP servers (Claude Flow required, Flow Nexus optional).
3. Plan actions with safety/rollback; run subskill workflows with logging.
4. Validate results (tests/checks/approvals) and record confidence ceiling.
5. Store artifacts under `skills/tooling/github-integration/{project}/{timestamp}` with WHO/WHY/PROJECT/WHEN tags.

## Subskills
- PR review (`when-reviewing-github-pr-use-github-code-review`)
- Multi-repo coordination (`when-managing-multiple-repos-use-github-multi-repo`)
- Project management (`when-managing-github-projects-use-github-project-management`)
- Release management (`when-releasing-software-use-github-release-management`)
- Workflow automation (`when-automating-github-actions-use-workflow-automation`)

## Guardrails
- Least-privilege tokens; never log secrets.
- Confidence ceilings on analyses and automations.
- Structure-first docs kept current; follow Prompt Architect constraint ordering.

Confidence: 0.70 (ceiling: inference 0.70) – README aligned to Skill Forge guardrails.
