---
name: github-release-management
description: Comprehensive GitHub release orchestration with AI swarm coordination for automated versioning, testing, deployment, and rollback management
---

# GitHub Release Management Skill

Intelligent release automation and orchestration using AI swarms for comprehensive software releases - from changelog generation to multi-platform deployment with rollback capabilities.

## Quick Start

### Simple Release Flow
```bash
# Plan and create a release
gh release create v2.0.0 \
  --draft \
  --generate-notes \
  --title "Release v2.0.0"

# Orchestrate with swarm
npx claude-flow github release-create \
  --version "2.0.0" \
  --build-artifacts \
  --deploy-targets "npm,docker,github"
```

### Full Automated Release
```bash
# Initialize release swarm
npx claude-flow swarm init --topology hierarchical

# Execute complete release pipeline
npx claude-flow sparc pipeline "Release v2.0.0 with full validation"
```

## Progressive Disclosure: Level 1 - Basic Usage

### Essential Release Commands

#### Create Release Draft
```bash
# Get last release tag
LAST_TAG=$(gh release list --limit 1 --json tagName -q '.[0].tagName')

# Generate changelog from commits
CHANGELOG=$(gh api repos/:owner/:repo/compare/${LAST_TAG}...HEAD \
  --jq '.commits[].commit.message')

# Create draft release
gh release create v2.0.0 \
  --draft \
  --title "Release v2.0.0" \
  --notes "$CHANGELOG" \
  --target main
```

#### Basic Version Bump
```bash
# Update package.json version
npm version patch  # or minor, major

# Push version tag
git push --follow-tags
```

#### Simple Deployment
```bash
# Build and publish npm package
npm run build
npm publish

# Create GitHub release
gh release create $(npm pkg get version) \
  --generate-notes
```

### Quick Integration Example
```javascript
// Simple release preparation in Claude Code
[Single Message]:
  // Update version files
  Edit("package.json", { old: '"version": "1.0.0"', new: '"version": "2.0.0"' })

  // Generate changelog
  Bash("gh api repos/:owner/:repo/compare/v1.0.0...HEAD --jq '.commits[].commit.message' > CHANGELOG.md")

  // Create release branch
  Bash("git checkout -b release/v2.0.0")
  Bash("git add -A && git commit -m 'release: Prepare v2.0.0'")

  // Create PR
  Bash("gh pr create --title 'Release v2.0.0' --body 'Automated release preparation'")
```

## Progressive Disclosure: Level 3 - Advanced Workflows

### Multi-Package Release Coordination

#### Monorepo Release Strategy
```javascript
[Single Message - Multi-Package Release]:
  // Initialize mesh topology for cross-package coordination
  mcp__claude-flow__swarm_init { topology: "mesh", maxAgents: 8 }

  // Spawn package-specific agents
  Task("Package A Manager", "Coordinate claude-flow package release v1.0.72", "coder")
  Task("Package B Manager", "Coordinate ruv-swarm package release v1.0.12", "coder")
  Task("Integration Tester", "Validate cross-package compatibility", "tester")
  Task("Version Coordinator", "Align dependencies and versions", "coordinator")

  // Update all packages simultaneously
  Write("packages/claude-flow/package.json", "[v1.0.72 content]")
  Write("packages/ruv-swarm/package.json", "[v1.0.12 content]")
  Write("CHANGELOG.md", "[consolidated changelog]")

  // Run cross-package validation
  Bash("cd packages/claude-flow && npm install && npm test")
  Bash("cd packages/ruv-swarm && npm install && npm test")
  Bash("npm run test:integration")

  // Create unified release PR
  Bash(`gh pr create \
    --title "Release: claude-flow v1.0.72, ruv-swarm v1.0.12" \
    --body "Multi-package coordinated release with cross-compatibility validation"`)
```

### Progressive Deployment Strategy

#### Staged Rollout Configuration
```yaml
# .github/release-deployment.yml
deployment:
  strategy: progressive
  stages:
    - name: canary
      percentage: 5
      duration: 1h
      metrics:
        - error-rate < 0.1%
        - latency-p99 < 200ms
      auto-advance: true

    - name: partial
      percentage: 25
      duration: 4h
      validation: automated-tests
      approval: qa-team

    - name: rollout
      percentage: 50
      duration: 8h
      monitor: true

    - name: full
      percentage: 100
      approval: release-manager
      rollback-enabled: true
```

#### Execute Staged Deployment
```bash
# Deploy with progressive rollout
npx claude-flow github release-deploy \
  --version v2.0.0 \
  --strategy progressive \
  --config .github/release-deployment.yml \
  --monitor-metrics \
  --auto-rollback-on-error
```

### Multi-Repository Coordination

#### Coordinated Multi-Repo Release
```bash
# Synchronize releases across repositories
npx claude-flow github multi-release \
  --repos "frontend:v2.0.0,backend:v2.1.0,cli:v1.5.0" \
  --ensure-compatibility \
  --atomic-release \
  --synchronized \
  --rollback-all-on-failure
```

#### Cross-Repo Dependency Management
```javascript
[Single Message - Cross-Repo Release]:
  // Initialize star topology for centralized coordination
  mcp__claude-flow__swarm_init { topology: "star", maxAgents: 6 }

  // Spawn repo-specific coordinators
  Task("Frontend Release", "Release frontend v2.0.0 with API compatibility", "coordinator")
  Task("Backend Release", "Release backend v2.1.0 with breaking changes", "coordinator")
  Task("CLI Release", "Release CLI v1.5.0 with new commands", "coordinator")
  Task("Compatibility Checker", "Validate cross-repo compatibility", "researcher")

  // Coordinate version updates across repos
  Bash("gh api repos/org/frontend/dispatches --method POST -f event_type='release' -F client_payload[version]=v2.0.0")
  Bash("gh api repos/org/backend/dispatches --method POST -f event_type='release' -F client_payload[version]=v2.1.0")
  Bash("gh api repos/org/cli/dispatches --method POST -f event_type='release' -F client_payload[version]=v1.5.0")

  // Monitor all releases
  mcp__claude-flow__swarm_monitor { interval: 5, duration: 300 }
```

### Hotfix Emergency Procedures

#### Emergency Hotfix Workflow
```bash
# Fast-track critical bug fix
npx claude-flow github emergency-release \
  --issue 789 \
  --severity critical \
  --target-version v1.2.4 \
  --cherry-pick-commits \
  --bypass-checks security-only \
  --fast-track \
  --notify-all
```

#### Automated Hotfix Process
```javascript
[Single Message - Emergency Hotfix]:
  // Create hotfix branch from last stable release
  Bash("git checkout -b hotfix/v1.2.4 v1.2.3")

  // Cherry-pick critical fixes
  Bash("git cherry-pick abc123def")

  // Fast validation
  Bash("npm run test:critical && npm run build")

  // Create emergency release
  Bash(`gh release create v1.2.4 \
    --title "HOTFIX v1.2.4: Critical Security Patch" \
    --notes "Emergency release addressing CVE-2024-XXXX" \
    --prerelease=false`)

  // Immediate deployment
  Bash("npm publish --tag hotfix")

  // Notify stakeholders
  Bash(`gh issue create \
    --title "🚨 HOTFIX v1.2.4 Deployed" \
    --body "Critical security patch deployed. Please update immediately." \
    --label "critical,security,hotfix"`)
```

## GitHub Actions Integration

### Complete Release Workflow
```yaml
# .github/workflows/release.yml
on:
  push:
    tags: ['v*']

jobs:
  release-orchestration:
    runs-on: ubuntu-latest
    permissions:
      contents: write
      packages: write
      issues: write

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v3
        with:
          fetch-depth: 0

      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '20'
          cache: 'npm'

      - name: Authenticate GitHub CLI
        run: echo "${{ secrets.GITHUB_TOKEN }}" | gh auth login --with-token

      - name: Initialize Release Swarm
        run: |
          # Extract version from tag
          RELEASE_TAG=${{ github.ref_name }}
          PREV_TAG=$(gh release list --limit 2 --json tagName -q '.[1].tagName')

          # Get merged PRs for changelog
          PRS=$(gh pr list --state merged --base main --json number,title,labels,author,mergedAt \
            --jq ".[] | select(.mergedAt > \"$(gh release view $PREV_TAG --json publishedAt -q .publishedAt)\")")

          # Get commit history
          COMMITS=$(gh api repos/${{ github.repository }}/compare/${PREV_TAG}...HEAD \
            --jq '.commits[].commit.message')

          # Initialize swarm coordination
          npx claude-flow@alpha swarm init --topology hierarchical

          # Store release context
          echo "$PRS" > /tmp/release-prs.json
          echo "$COMMITS" > /tmp/release-commits.txt

      - name: Generate Release Changelog
        run: |
          # Generate intelligent changelog
          CHANGELOG=$(npx claude-flow@alpha github changelog \
            --prs "$(cat /tmp/release-prs.json)" \
            --commits "$(cat /tmp/release-commits.txt)" \
            --from $PREV_TAG \
            --to $RELEASE_TAG \
            --categorize \
            --add-migration-guide \
            --format markdown)

          echo "$CHANGELOG" > RELEASE_CHANGELOG.md

      - name: Build Release Artifacts
        run: |
          # Install dependencies
          npm ci

          # Run comprehensive validation
          npm run lint
          npm run typecheck
          npm run test:all
          npm run build

          # Build platform-specific binaries
          npx claude-flow@alpha github release-build \
            --platforms "linux,macos,windows" \
            --architectures "x64,arm64" \
            --parallel

      - name: Security Scan
        run: |
          # Run security validation
          npm audit --audit-level=moderate

          npx claude-flow@alpha github release-security \
            --scan-dependencies \
            --check-secrets \
            --sign-artifacts

      - name: Create GitHub Release
        run: |
          # Update release with generated changelog
          gh release edit ${{ github.ref_name }} \
            --notes "$(cat RELEASE_CHANGELOG.md)" \
            --draft=false

          # Upload all artifacts
          for file in dist/*; do
            gh release upload ${{ github.ref_name }} "$file"
          done

      - name: Deploy to Package Registries
        run: |
          # Publish to npm
          echo "//registry.npmjs.org/:_authToken=${{ secrets.NPM_TOKEN }}" > .npmrc
          npm publish

          # Build and push Docker images
          docker build -t ${{ github.repository }}:${{ github.ref_name }} .
          docker push ${{ github.repository }}:${{ github.ref_name }}

      - name: Post-Release Validation
        run: |
          # Run smoke tests
          npm run test:smoke

          # Validate deployment
          npx claude-flow@alpha github release-validate \
            --version ${{ github.ref_name }} \
            --smoke-tests \
            --health-checks

      - name: Create Release Announcement
        run: |
          # Create announcement issue
          gh issue create \
            --title "🎉 Released ${{ github.ref_name }}" \
            --body "$(cat RELEASE_CHANGELOG.md)" \
            --label "announcement,release"

          # Notify via discussion
          gh api repos/${{ github.repository }}/discussions \
            --method POST \
            -f title="Release ${{ github.ref_name }} Now Available" \
            -f body="$(cat RELEASE_CHANGELOG.md)" \
            -f category_id="$(gh api repos/${{ github.repository }}/discussions/categories --jq '.[] | select(.slug=="announcements") | .id')"

      - name: Monitor Release
        run: |
          # Start release monitoring
          npx claude-flow@alpha github release-monitor \
            --version ${{ github.ref_name }} \
            --duration 1h \
            --alert-on-errors &
```

### Hotfix Workflow
```yaml
# .github/workflows/hotfix.yml
on:
  issues:
    types: [labeled]

jobs:
  emergency-hotfix:
    if: contains(github.event.issue.labels.*.name, 'critical-hotfix')
    runs-on: ubuntu-latest

    steps:
      - name: Create Hotfix Branch
        run: |
          LAST_STABLE=$(gh release list --limit 1 --json tagName -q '.[0].tagName')
          HOTFIX_VERSION=$(echo $LAST_STABLE | awk -F. '{print $1"."$2"."$3+1}')

          git checkout -b hotfix/$HOTFIX_VERSION $LAST_STABLE

      - name: Fast-Track Testing
        run: |
          npm ci
          npm run test:critical
          npm run build

      - name: Emergency Release
        run: |
          npx claude-flow@alpha github emergency-release \
            --issue ${{ github.event.issue.number }} \
            --severity critical \
            --fast-track \
            --notify-all
```

## Troubleshooting & Common Issues

### Issue: Failed Release Build
```bash
# Debug build failures
npx claude-flow@alpha diagnostic-run \
  --component build \
  --verbose

# Retry with isolated environment
docker run --rm -v $(pwd):/app node:20 \
  bash -c "cd /app && npm ci && npm run build"
```

### Issue: Test Failures in CI
```bash
# Run tests with detailed output
npm run test -- --verbose --coverage

# Check for environment-specific issues
npm run test:ci

# Compare local vs CI environment
npx claude-flow@alpha github compat-test \
  --environments "local,ci" \
  --compare
```

### Issue: Deployment Rollback Needed
```bash
# Immediate rollback to previous version
npx claude-flow@alpha github rollback \
  --to-version v1.9.9 \
  --reason "Critical bug in v2.0.0" \
  --preserve-data \
  --notify-users

# Investigate rollback cause
npx claude-flow@alpha github release-analytics \
  --version v2.0.0 \
  --identify-issues
```

### Issue: Version Conflicts
```bash
# Check and resolve version conflicts
npx claude-flow@alpha github release-validate \
  --checks version-conflicts \
  --auto-resolve

# Align multi-package versions
npx claude-flow@alpha github version-sync \
  --packages "package-a,package-b" \
  --strategy semantic
```

## Related Resources

### Documentation
- [GitHub CLI Documentation](https://cli.github.com/manual/)
- [Semantic Versioning Spec](https://semver.org/)
- [Claude Flow SPARC Guide](../../docs/sparc-methodology.md)
- [Swarm Coordination Patterns](../../docs/swarm-patterns.md)

### Related Skills
- **github-pr-management**: PR review and merge automation
- **github-workflow-automation**: CI/CD workflow orchestration
- **multi-repo-coordination**: Cross-repository synchronization
- **deployment-orchestration**: Advanced deployment strategies

### Support & Community
- Issues: https://github.com/ruvnet/claude-flow/issues
- Discussions: https://github.com/ruvnet/claude-flow/discussions
- Documentation: https://claude-flow.dev/docs

**Version**: 2.0.0
**Last Updated**: 2025-10-19
**Maintained By**: Claude Flow Team

## Common Anti-Patterns

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| **Manual Version Bumping** | Human-selected version numbers don't reflect breaking changes, leading to SemVer violations | Use swarm version analysis to scan commits and PRs for breaking changes and auto-suggest version bump |
| **No Staged Rollout** | Deploying to 100% traffic immediately amplifies impact of bugs, causing widespread user impact | Implement progressive deployment (5% -> 25% -> 50% -> 100%) with health checks between stages |
| **Sequential Artifact Builds** | Building npm package, then Docker image, then binaries serially wastes 2-3x time | Use parallel swarm coordination to build all artifacts concurrently, validate, then publish atomically |
| **Missing Rollback Plan** | Deployments fail with no automated rollback, requiring manual intervention during incidents | Configure auto-rollback based on error rate and health check metrics with 5-minute grace period |
| **Incomplete Changelogs** | Release notes missing migration guides for breaking changes frustrate users upgrading | Use swarm changelog agent to categorize changes and generate migration guides for breaking changes |

---

## Conclusion

GitHub Release Management orchestrates complex, multi-platform releases with AI swarm coordination to ensure reliability, completeness, and user confidence. By combining semantic version analysis, progressive deployment strategies, and parallel artifact coordination, it transforms manual release processes into automated, auditable pipelines.

This skill is essential when managing production releases for multi-platform software, coordinating monorepo releases across packages, or implementing progressive deployment with automated rollback. It excels at version decision automation, breaking change detection, and multi-registry publishing that manual release processes struggle to coordinate consistently.

Use this skill when setting up release workflows for new projects, when existing releases have high failure rates or incomplete changelogs, or when you need emergency hotfix capabilities with fast-track testing. The swarm coordination patterns enable parallel builds, intelligent changelog generation, and automated rollback that traditional release scripts require significant manual effort to achieve.