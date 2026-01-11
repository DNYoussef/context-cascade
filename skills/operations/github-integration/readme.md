# GitHub Integration

Design GitHub Apps, webhooks, and API automations with safe auth and observability.

## When to Use
- Building or hardening GitHub webhooks/bridges
- Integrating GitHub events with external systems
- Auditable automation that respects rate limits and permissions

## When Not to Use
- Release orchestration (use github-release-management)
- Cross-repo campaigns (use github-multi-repo)
- Project governance (use github-project-management)

## Workflow Snapshot
1. Map events, repos, permissions, and auth models.
2. Design payload handling, retries/backoff, and idempotency.
3. Implement actions/scripts with logging and sandbox tests.
4. Validate in staging, wire monitoring, and document fallbacks.

## Artifacts
- SKILL.md SOP, examples/, tests/, resources/, shared-scripts/, and references/

## Quality Gates
- Least-privilege tokens with rotation plans
- Webhook signature, retry, and idempotency validation
- Explicit confidence ceilings on go-live readiness
