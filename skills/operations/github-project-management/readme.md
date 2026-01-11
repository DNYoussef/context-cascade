# GitHub Project Management Skill

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



## CRITICAL: AUTOMATION SAFETY GUARDRAILS

**BEFORE any automation hook, validate**:
- [ ] Idempotency guaranteed (safe to run multiple times)
- [ ] Timeout configured (prevent infinite loops)
- [ ] Error handling with graceful degradation
- [ ] Audit logging for all state changes
- [ ] Human-in-the-loop for destructive operations

**NEVER**:
- Execute destructive operations without confirmation
- Bypass validation in pre-commit/pre-push hooks
- Auto-fix errors without root cause analysis
- Deploy hooks without testing in sandbox environment
- Ignore hook failures (fail fast, not silent)

**ALWAYS**:
- Validate input before processing (schema validation)
- Implement circuit breakers for external dependencies
- Document hook side effects and preconditions
- Provide escape hatches (--no-verify with justification)
- Version hook configurations with rollback capability

**Evidence-Based Techniques for Automation**:
- **Step-by-Step**: Decompose complex automation into atomic steps
- **Verification**: After each hook action, verify expected state
- **Self-Consistency**: Run same validation logic across all hooks
- **Adversarial Prompting**: Test hooks with malformed inputs


## Overview

Comprehensive GitHub project management with AI swarm coordination for intelligent issue tracking, automated project board synchronization, and sprint planning workflows.

## Quick Start

```bash
# Basic issue creation with swarm
gh issue create --title "Feature: Advanced Auth" --body "..." --label "enhancement,swarm-ready"

# Initialize project board sync
npx ruv-swarm github board-init --project-id "$PROJECT_ID" --sync-mode "bidirectional"
```

## Features

- **Issue Management**: Automated triage, decomposition, and swarm coordination
- **Project Boards**: Real-time synchronization with intelligent card management
- **Sprint Planning**: Agile/Kanban workflows with metrics tracking
- **Analytics**: Performance metrics, KPIs, and team collaboration insights

## Directory Structure

```
github-project-management/
├── skill.md              # Main skill documentation
├── README.md             # This file
├── resources/
│   ├── readme.md         # Resources overview
│   ├── scripts/          # Automation scripts
│   │   ├── project-board-automation.js
│   │   ├── issue-tracker.js
│   │   ├── sprint-planner.js
│   │   └── milestone-manager.js
│   └── templates/        # Configuration templates
│       ├── project-config.yaml
│       ├── issue-template.md
│       └── sprint-template.json
├── tests/                # Test suites
│   ├── issue-management.test.js
│   ├── board-sync.test.js
│   └── sprint-planning.test.js
└── examples/             # Usage examples
    ├── kanban-automation.md
    ├── sprint-planning.md
    └── cross-repo-projects.md
```

## Usage

See `skill.md` for comprehensive documentation and `examples/` for detailed walkthroughs.

## Requirements

- GitHub CLI (`gh`) installed and authenticated
- ruv-swarm or claude-flow MCP server configured
- Repository access permissions

## Related Skills

- `github-pr-workflow` - Pull request management
- `github-release-management` - Release coordination
- `sparc-orchestrator` - Complex workflow orchestration

## Version

2.0.0 (Gold Tier)


---
*Promise: `<promise>README_VERIX_COMPLIANT</promise>`*
