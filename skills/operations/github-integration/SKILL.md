---
name: github-integration
description: Build reliable GitHub integrations, webhooks, and automation bridges
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
x-version: 3.2.0
x-category: operations
x-vcl-compliance: v3.1.1
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---



---

## LIBRARY-FIRST PROTOCOL (MANDATORY)

**Before writing ANY code, you MUST check:**

### Step 1: Library Catalog
- Location: `.claude/library/catalog.json`
- If match >70%: REUSE or ADAPT

### Step 2: Patterns Guide
- Location: `.claude/docs/inventories/LIBRARY-PATTERNS-GUIDE.md`
- If pattern exists: FOLLOW documented approach

### Step 3: Existing Projects
- Location: `D:\Projects\*`
- If found: EXTRACT and adapt

### Decision Matrix
| Match | Action |
|-------|--------|
| Library >90% | REUSE directly |
| Library 70-90% | ADAPT minimally |
| Pattern exists | FOLLOW pattern |
| In project | EXTRACT |
| No match | BUILD (add to library after) |

---

## STANDARD OPERATING PROCEDURE

### Purpose
Design and implement GitHub-centric integrations (API, Apps, webhooks) with secure auth, observability, and rollback-ready automation.

### Trigger Conditions
- **Positive:** Need GitHub automation or webhook bridge; Integrating GitHub with external systems; Auditable GitHub API usage across repos
- **Negative:** Release orchestration (route to github-release-management); Cross-repo campaign (route to github-multi-repo); Project board design (route to github-project-management)

### Guardrails
- Structure-first: keep SKILL.md aligned with examples/, tests/, and any resources/references so downstream agents always have scaffolding.
- Adversarial validation is mandatory: cover boundary cases, failure paths, and rollback drills before declaring the SOP complete.
- Prompt hygiene: separate hard vs. soft vs. inferred constraints and confirm inferred constraints before acting.
- Explicit confidence ceilings: format as 'Confidence: X.XX (ceiling: TYPE Y.YY)' and never exceed the ceiling for the claim type.
- MCP traceability: tag sessions WHO=operations-{name}-{session_id}, WHY=skill-execution, and capture evidence links in outputs.
- Avoid anti-patterns: undocumented changes, missing rollback paths, skipped tests, or unbounded automation without approvals.

### Required Artifacts
- SKILL.md (this SOP)
- readme.md with usage examples
- examples/ for integration flows
- tests/ for scripts/actions
- resources/ and shared-scripts/ for reuse
- references/ with API constraints

### Execution Phases
1. **Assess integration surface**
   - Map repos, events, and permissions required
   - Confirm auth model (GitHub App, PAT, OIDC) and rotation plan
   - Identify rate limits and audit requirements

2. **Design event and API flows**
   - Define webhook payload handling, retries, and signature validation
   - Specify idempotency, deduplication, and backoff policies
   - Plan data mapping and error handling between systems

3. **Implement automation**
   - Build or reuse scripts/actions with least privilege
   - Add logging/metrics and sandbox tests
   - Gate production rollout with dry runs and approvals

4. **Validate and operate**
   - Run integration tests and failure-injection scenarios
   - Set up monitoring, alerts, and dashboards
   - Document runbooks, fallbacks, and support contacts

### Output Format
- Integration design doc with events, permissions, and rate-limit posture
- Auth and secret management plan with rotation cadence
- Implemented automation artifacts (scripts/actions) with test evidence
- Monitoring and alert plan with dashboards/links
- Runbook with rollback/disablement steps and owners

### Validation Checklist
- Tokens/keys scoped to least privilege and rotated
- Webhook verification, retries, and idempotency tested
- Integration tested in staging or dry-run mode
- Audit trail and observability hooks enabled
- Confidence ceiling stated for go-live

Confidence: 0.70 (ceiling: inference 0.70) - GitHub integration steps follow validated automation guardrails
