# MCP Integration Guide – GitHub Skills

Use MCP servers consistently across GitHub subskills with Prompt Architect clarity and Skill Forge guardrails.

## Servers
- **Claude Flow (required):** swarm coordination and agent orchestration.
- **Flow Nexus (optional):** advanced GitHub features; use when cloud integration is needed.

## Setup
```bash
# Required
claude mcp add claude-flow npx claude-flow@alpha mcp start
claude mcp list

# Optional
claude mcp add flow-nexus npx flow-nexus@latest mcp start
npx flow-nexus@latest login
```

Tag sessions: `WHO=github-integration-{session}`, `WHY=skill-execution`, `PROJECT=<repo>`, `WHEN=<iso>`.

## Core Tools (Claude Flow)
- `mcp__claude-flow__swarm_init(topology, maxAgents, strategy)` – choose mesh (PR reviews), hierarchical (releases/multi-repo), star (projects), or ring (sequential workflows).
- `mcp__claude-flow__spawn_agent(role, task, tools)` – provision reviewers, coordinators, testers.
- `mcp__claude-flow__memory_store/retrieve` – store findings, decisions, and rerun context.

## Usage Patterns by Subskill
- **PR Review:** mesh topology; reviewers (security, perf, quality) + coordinator; store SARIF/notes.
- **Multi-Repo:** hierarchical topology; repo-architect coordinates workers; record dependency graph.
- **Projects:** star topology; planner hub with issue trackers; sync board states.
- **Release Management:** hierarchical; release-manager + testers + docs; log versioning and rollout plan.
- **Workflow Automation:** mesh; CICD engineer + security auditor + tester; ensure action pinning and least privilege.

## Guardrails
- Least-privilege tokens; never echo secrets.
- Log commands and outcomes; keep rollback notes for automation changes.
- Confidence ceilings on analyses and automation steps.
- Memory tagging for every run; archive outputs under `skills/tooling/github-integration/{project}/{timestamp}`.

Confidence: 0.70 (ceiling: inference 0.70) – Guide rewritten to Skill Forge format with Prompt Architect constraint ordering.
