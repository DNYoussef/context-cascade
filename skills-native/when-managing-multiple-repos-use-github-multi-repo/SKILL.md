---
name: when-managing-multiple-repos-use-github-multi-repo
description: Multi-repository coordination, synchronization, and architecture management with AI swarm orchestration. Coordinates repo-architect, code-analyzer, and coordinator agents across multiple repositories to maintain consistency, propagate changes, manage dependencies, and ensure architectural alignment. Handles monorepo-to-multi-repo migrations, cross-repo refactoring, and synchronized releases. Use when managing microservices, multi-package ecosystems, or coordinating changes across related repositories.
---

# GitHub Multi-Repository Management Skill

## Overview

Orchestrate complex operations across multiple related GitHub repositories with intelligent agent coordination. This skill enables consistent architecture enforcement, synchronized dependency updates, cross-repo refactoring, and coordinated releases for microservices, multi-package ecosystems, and distributed system architectures.

## When to Use This Skill

Activate this skill when managing microservices architectures spanning multiple repositories, coordinating changes across frontend/backend/infrastructure repos, migrating from monorepo to multi-repo structure, propagating breaking changes across dependent repositories, maintaining consistent coding standards across teams, synchronizing releases for multi-package systems, or enforcing architectural patterns across an organization.

Use for both small-scale coordination (2-5 repos) and large-scale orchestration (10+ repositories), one-time migrations or ongoing maintenance, and establishing governance for multi-repo ecosystems.

## Agent Coordination Architecture

### Swarm Topology

Initialize a **hierarchical topology** with a coordinator agent managing specialized worker agents. Hierarchical structure enables centralized decision-making for consistency while delegating specialized tasks to expert agents.

```bash
# Initialize hierarchical swarm for multi-repo coordination
npx claude-flow@alpha swarm init --topology hierarchical --max-agents 8 --strategy adaptive
```

### Specialized Agent Roles

**Hierarchical Coordinator** (`hierarchical-coordinator`): Top-level orchestrator that maintains global view of all repositories, makes architectural decisions, coordinates cross-repo operations, and ensures consistency. Acts as the single source of truth for multi-repo strategy.

**Repository Architect** (`repo-architect`): Analyzes repository structures, defines architectural patterns, creates dependency graphs, identifies coupling issues, and designs migration strategies. Maintains the architectural vision across repositories.

**Code Analyzer** (`code-analyzer`): Scans codebases for patterns, dependencies, and inconsistencies. Identifies code duplication across repos, tracks API contracts, and validates architectural compliance.

**CI/CD Engineer** (`cicd-engineer`): Manages build pipelines, deployment workflows, and release orchestration. Coordinates continuous integration across repositories and handles versioning strategies.

**Worker Agents** (spawned dynamically): Execute repository-specific tasks such as refactoring, testing, documentation updates, and dependency bumps. Scaled based on number of target repositories.

## Multi-Repository Workflows (SOP)

### Workflow 1: Cross-Repository Change Propagation

Propagate breaking changes, API updates, or architectural patterns across multiple repositories.

**Phase 1: Impact Analysis**

**Step 1.1: Initialize Hierarchical Coordination**

```bash
# Set up hierarchical swarm
mcp__claude-flow__swarm_init topology=hierarchical maxAgents=8 strategy=adaptive

# Spawn coordinator and specialists
mcp__claude-flow__agent_spawn type=coordinator name=hierarchical-coordinator
mcp__claude-flow__agent_spawn type=analyst name=repo-architect
mcp__claude-flow__agent_spawn type=analyst name=code-analyzer
mcp__claude-flow__agent_spawn type=coder name=cicd-engineer
```

**Step 1.2: Analyze Repository Dependencies**

Use `scripts/repo-graph.sh` to build dependency graph:

```bash
# Generate dependency graph across all repositories
bash scripts/repo-graph.sh build-graph \
  --repos "repo1,repo2,repo3" \
  --output "references/dependency-graph.dot"
```

Visualize the dependency graph to identify impact scope:

```bash
# Render graph visualization
dot -Tpng references/dependency-graph.dot -o dependency-graph.png
```

**Step 1.3: Identify Affected Repositories**

Launch coordinator to analyze impact:

```plaintext
Task("Hierarchical Coordinator", "
  Analyze the impact of <CHANGE_DESCRIPTION> across all repositories:

  1. Review dependency graph at references/dependency-graph.dot
  2. Identify direct dependents (repositories importing affected code)
  3. Identify transitive dependents (downstream consumers)
  4. Categorize changes by risk level (breaking/compatible/enhancement)
  5. Create propagation strategy with sequencing

  Store impact analysis in memory: multi-repo/impact-analysis
  Use scripts/repo-graph.sh for dependency traversal
  Run hooks: npx claude-flow@alpha hooks pre-task --description 'impact analysis'
", "hierarchical-coordinator")
```

**Phase 2: Parallel Repository Updates**

Execute coordinated updates across all affected repositories.

**Step 2.1: Spawn Worker Agents per Repository**

For each affected repository, spawn a dedicated worker agent:

```plaintext
Task("Worker: Repository 1", "
  Apply changes to repository <REPO_1>:

  1. Clone repository: bash scripts/multi-repo.sh clone <REPO_1>
  2. Create feature branch: change-propagation-<DATE>
  3. Apply code changes based on coordinator strategy
  4. Update tests to reflect new API contracts
  5. Validate build passes: npm test / cargo test
  6. Commit changes with standardized message
  7. Push branch and create draft PR

  Store results in memory: multi-repo/updates/<REPO_1>
  Run hooks for coordination
", "coder")

Task("Worker: Repository 2", "
  Apply changes to repository <REPO_2>:
  [Same steps as above, tailored to REPO_2]

  Store results in memory: multi-repo/updates/<REPO_2>
", "coder")

# Spawn additional workers for each repository
# All workers execute in parallel
```

**Step 2.2: Coordinate Test Execution**

After all workers complete, test repositories together:

```plaintext
Task("CI/CD Engineer", "
  Validate changes across all repositories:

  1. Set up integration test environment
  2. Build all modified repositories in dependency order
  3. Run integration tests with new versions
  4. Check for breaking changes in API contracts
  5. Validate performance hasn't degraded

  Use scripts/integration-test.sh for orchestration
  Store test results in memory: multi-repo/test-results
", "cicd-engineer")
```

**Phase 3: Synchronized Release**

Coordinate pull request creation and merging across repositories.

**Step 3.1: Create Pull Requests**

Generate PRs for all repositories simultaneously:

```bash
# Create PRs across all repos
bash scripts/multi-repo.sh create-prs \
  --repos "repo1,repo2,repo3" \
  --title "Propagate: <CHANGE_DESCRIPTION>" \
  --body-template "references/pr-template.md" \
  --labels "multi-repo-sync,automated"
```

**Step 3.2: Coordinate Review and Merge**

Track PR status and coordinate merging in dependency order:

```plaintext
Task("Hierarchical Coordinator", "
  Coordinate PR review and merge process:

  1. Monitor PR status using scripts/multi-repo.sh pr-status
  2. Ensure PRs are reviewed in dependency order
  3. Merge upstream dependencies first (libraries, shared code)
  4. Wait for CI to pass on each merge
  5. Merge downstream consumers after dependencies released
  6. Verify no build breaks in dependency chain

  Use scripts/multi-repo.sh merge-sequence for ordering
  Store merge sequence in memory: multi-repo/merge-plan
", "hierarchical-coordinator")
```

**Step 3.3: Tag and Release**

Create coordinated releases across repositories:

```bash
# Execute synchronized releases
bash scripts/multi-repo.sh synchronized-release \
  --repos "repo1,repo2,repo3" \
  --version-strategy "minor" \
  --release-notes-dir "references/release-notes"
```

### Workflow 2: Monorepo to Multi-Repo Migration

Migrate a monolithic repository into multiple focused repositories while preserving history.

**Phase 1: Architecture Planning**

**Step 1.1: Analyze Monorepo Structure**

```plaintext
Task("Repository Architect", "
  Analyze monorepo structure and design migration strategy:

  1. Map directory structure and module boundaries
  2. Identify logical separation points (services, packages, layers)
  3. Analyze import/dependency patterns using scripts/analyze-deps.sh
  4. Detect circular dependencies that need refactoring
  5. Create proposed repository structure
  6. Design shared library strategy for common code

  Reference references/migration-best-practices.md
  Store architecture plan in memory: multi-repo/migration-plan
", "repo-architect")
```

**Step 1.2: Generate Dependency Graph**

Create comprehensive dependency visualization:

```bash
# Analyze monorepo dependencies
bash scripts/analyze-deps.sh \
  --monorepo-path <PATH> \
  --output references/monorepo-dependencies.json

# Generate split recommendations
bash scripts/repo-graph.sh recommend-split \
  --deps references/monorepo-dependencies.json \
  --output references/split-strategy.md
```

**Phase 2: Repository Creation and History Preservation**

**Step 2.1: Create Target Repositories**

```bash
# Create new repositories with proper structure
bash scripts/multi-repo.sh create-repos \
  --org <ORGANIZATION> \
  --repos-config references/new-repos.json \
  --template "references/repo-template"
```

**Step 2.2: Extract Code with History**

For each target repository, extract relevant code while preserving Git history:

```bash
# Extract subdirectory with full history
bash scripts/migration.sh extract-with-history \
  --source <MONOREPO_PATH> \
  --subdirectory <SUBDIR> \
  --target-repo <NEW_REPO> \
  --preserve-authors true
```

**Step 2.3: Refactor Cross-Repository Dependencies**

```plaintext
Task("Code Analyzer", "
  Refactor dependencies for multi-repo structure:

  1. Identify hard-coded paths that need updating
  2. Convert internal imports to package dependencies
  3. Extract shared code to common library repository
  4. Update build configurations for new structure
  5. Generate package.json / Cargo.toml with correct dependencies

  Use scripts/refactor-imports.sh for automated conversion
  Store refactoring changes in memory: multi-repo/refactoring
", "code-analyzer")
```

**Phase 3: Validation and Cutover**

**Step 3.1: Parallel Build Validation**

Ensure all new repositories build independently:

```plaintext
Task("CI/CD Engineer", "
  Validate all new repositories build and test successfully:

  1. Set up CI pipelines for each new repository
  2. Configure dependency resolution (npm registry, cargo)
  3. Run full test suites in each repository
  4. Validate integration between repositories
  5. Compare test results with monorepo baseline

  Use scripts/validate-migration.sh
  Store validation results in memory: multi-repo/validation
", "cicd-engineer")
```

**Step 3.2: Gradual Migration Plan**

Create phased cutover strategy:

```bash
# Generate migration timeline
bash scripts/migration.sh create-timeline \
  --repos references/new-repos.json \
  --risk-assessment references/risk-analysis.md \
  --output references/migration-timeline.md
```

### Workflow 3: Architectural Pattern Enforcement

Ensure consistent architectural patterns across all repositories.

**Phase 1: Pattern Definition**

**Step 1.1: Define Architectural Standards**

Create comprehensive architecture documentation in `references/architecture-standards.md` covering:
- Directory structure conventions
- Module organization patterns
- API design guidelines
- Testing strategies
- Documentation requirements
- CI/CD pipeline standards

**Step 1.2: Create Enforcement Rules**

Define linting rules and validation checks in `references/enforcement-rules.json`:
- Static analysis rules
- Dependency policy (allowed/forbidden packages)
- File naming conventions
- Code complexity thresholds
- Test coverage minimums

**Phase 2: Compliance Scanning**

**Step 2.1: Scan All Repositories**

```plaintext
Task("Code Analyzer", "
  Scan all repositories for architectural compliance:

  1. Clone all repositories: bash scripts/multi-repo.sh clone-all
  2. Run architectural linting: bash scripts/arch-lint.sh --config references/enforcement-rules.json
  3. Generate compliance report for each repository
  4. Identify violations by severity (critical/high/medium/low)
  5. Create prioritized remediation plan

  Store compliance reports in memory: multi-repo/compliance
", "code-analyzer")
```

**Step 2.2: Automated Remediation**

For common violations, generate automated fixes:

```bash
# Apply automated fixes where safe
bash scripts/auto-fix-violations.sh \
  --repos-dir <CLONED_REPOS> \
  --rules references/enforcement-rules.json \
  --create-prs true
```

**Phase 3: Continuous Monitoring**

**Step 3.1: Set Up Compliance Tracking**

```bash
# Create dashboard for ongoing monitoring
bash scripts/compliance-dashboard.sh setup \
  --repos references/repo-list.txt \
  --rules references/enforcement-rules.json \
  --output-dir compliance-dashboard
```

**Step 3.2: Automated Alerts**

Configure alerts for architectural violations:

```bash
# Set up GitHub Actions for compliance checks
bash scripts/setup-compliance-ci.sh \
  --repos references/repo-list.txt \
  --workflow-template references/compliance-workflow.yml
```

## MCP Tool Integration

### Repository Analysis

```bash
# Analyze each repository's structure and quality
mcp__flow-nexus__github_repo_analyze repo=<owner/repo1> analysis_type=code_quality
mcp__flow-nexus__github_repo_analyze repo=<owner/repo2> analysis_type=performance
mcp__flow-nexus__github_repo_analyze repo=<owner/repo3> analysis_type=security
```

### Swarm Orchestration

```bash
# Monitor multi-repo operation progress
mcp__claude-flow__swarm_status verbose=true

# Track task completion across repositories
mcp__claude-flow__task_status detailed=true

# Get performance metrics
mcp__claude-flow__agent_metrics metric=performance
```

## Best Practices

**Hierarchical Coordination**: Always use a single coordinator agent to maintain consistency and make global decisions. Worker agents handle repository-specific tasks but report to coordinator.

**Dependency-Order Execution**: Respect dependency graphs when applying changes. Update upstream dependencies before downstream consumers to avoid build breaks.

**Atomic Operations**: Group related changes across repositories into single coordinated operations. Use draft PRs and synchronized merges to maintain atomicity.

**History Preservation**: When migrating or refactoring, preserve Git history. Use `git filter-branch` or `git subtree` to maintain commit provenance.

**Testing Integration**: Always test repositories together after multi-repo changes. Individual repository tests may pass while integration fails.

**Rollback Strategy**: Maintain ability to rollback changes across all repositories. Use Git tags and release branches to enable coordinated rollback.

**Communication**: Keep stakeholders informed of multi-repo operations. Use consistent PR descriptions, labels, and commit messages across repositories.

## Error Handling

**Partial Failure Recovery**: If some repositories update successfully while others fail, coordinate rollback or forward-fix strategy based on dependency relationships.

**Merge Conflict Resolution**: For cross-repo conflicts, use coordinator to determine resolution strategy. Prioritize maintaining API contracts and build stability.

**Network Failures**: Implement retry logic with exponential backoff for GitHub API calls. Cache repository metadata to reduce API dependencies.

**Circular Dependency Detection**: If circular dependencies detected during analysis, coordinator must create refactoring plan to break cycles before migration proceeds.

## References

- `references/architecture-standards.md` - Organizational architecture patterns
- `references/enforcement-rules.json` - Automated compliance rules
- `references/migration-best-practices.md` - Repository migration guidelines
- `references/pr-template.md` - Standardized PR description template
- `references/repo-template/` - Template structure for new repositories
- `scripts/multi-repo.sh` - Multi-repository operation utilities
- `scripts/repo-graph.sh` - Dependency graph analysis
- `scripts/migration.sh` - Monorepo migration tools
- `scripts/analyze-deps.sh` - Dependency analysis
- `scripts/arch-lint.sh` - Architectural linting
- `scripts/integration-test.sh` - Cross-repo integration testing

## Core Principles

### 1. Dependency Order is Non-Negotiable Physics
In multi-repo architectures, dependency graphs define execution order constraints that cannot be violated without breaking the system. If Service B imports library from Service A, you MUST deploy Service A changes before Service B can consume them. Attempting to parallelize updates across this dependency boundary creates race conditions where Service B deploys code expecting new Service A API that doesn't exist yet, causing production outages.

**In practice**: Before any multi-repo operation, run `scripts/repo-graph.sh build-graph` to generate dependency visualization. This reveals the DAG (directed acyclic graph) of repository relationships. When propagating changes, the hierarchical-coordinator agent topologically sorts repositories: deploy upstream dependencies first (libraries, shared code), wait for CI validation, then deploy downstream consumers (services importing those libraries). For a 10-repo microservices architecture, this might create 4 deployment waves: Wave 1 (shared library), Wave 2 (3 services depending on library), Wave 3 (2 services depending on Wave 2 services), Wave 4 (aggregation layer depending on all services). Violating this order = production incidents.

### 2. Monorepo-to-Multi-Repo is One-Way Door, Plan Accordingly
Splitting a monorepo into multiple repositories is architecturally irreversible - once code is separated, teams diverge, tooling fragments, and the coordination overhead of reunification exceeds the cost of maintaining fragmentation. This means monorepo-to-multi-repo migrations require extraordinary planning discipline because the failure mode is permanent organizational complexity.

**In practice**: Before migration, repo-architect agent performs impact analysis: identify module boundaries (logical separation points with minimal cross-cutting concerns), analyze import patterns (`scripts/analyze-deps.sh` detects 500+ cross-module imports = high coupling, bad split candidate), detect circular dependencies (must be refactored before split or repositories will have bidirectional dependencies creating deployment gridlock), and design shared library strategy (common code extracted to separate library repo or duplicated across services). The migration plan must address: How will cross-repo refactoring work? (harder than monorepo global search-replace), How will versioning be managed? (semver for libraries, coordinated releases for services), How will testing work? (integration tests spanning repositories need orchestration). Get this wrong and you've permanently increased organizational friction.

### 3. Architectural Consistency Requires Active Enforcement, Not Documentation
Documenting coding standards in `references/architecture-standards.md` does nothing without enforcement mechanisms. Developers working under deadline pressure will violate conventions (nested ternaries, god objects, inconsistent error handling) if violations are only caught during manual code review. By that point, the code is written, tests pass, and "we'll refactor later" becomes permanent technical debt.

**In practice**: Implement automated architectural linting in CI pipelines. The code-analyzer agent runs `scripts/arch-lint.sh` on every PR, checking against `references/enforcement-rules.json`: directory structure compliance (all repositories use src/api/services/models/ structure), dependency policy (services cannot import other services directly, must use shared library), code complexity thresholds (cyclomatic complexity <10, function length <50 lines, max parameters <6), and test coverage minimums (>80% unit coverage, >60% integration coverage). Violations block PR merge. This prevents architectural drift - 30 repositories don't diverge into 30 different organizational patterns because enforcement is automatic and non-negotiable.

## Anti-Patterns

| Anti-Pattern | Problem | Solution |
|-------------|---------|----------|
| **Parallel Updates Ignoring Dependencies** | Deploy Service A v2.0 (breaking API changes) and Service B v1.5 (expects Service A v2.0 API) simultaneously across 2 repos. Service B deploys first due to faster CI pipeline. Service B calls Service A expecting new API, gets old API, crashes with "method not found" errors. Production outage for 45 minutes until rollback. | Use dependency-aware deployment sequencing: hierarchical-coordinator analyzes dependency graph from `scripts/repo-graph.sh`, topologically sorts repositories (upstream dependencies first), deploys in waves with validation gates (Wave 1 deploys, CI validates, then Wave 2 deploys). For Service A/B example: Deploy Service A v2.0, wait for health checks to pass, THEN deploy Service B v1.5. Deployment time increases (sequential vs parallel) but eliminates dependency-ordering outages. |
| **Monorepo Migration Without Circular Dependency Analysis** | Split monorepo into 3 repos without analyzing import patterns. Module A imports from Module B, Module B imports from Module C, Module C imports from Module A (circular dependency invisible in monorepo). After split, Repo A depends on Repo B, Repo B depends on Repo C, Repo C depends on Repo A = deployment gridlock (can't deploy any repo without deploying all 3 atomically, which defeats purpose of splitting). | Run `scripts/analyze-deps.sh` BEFORE migration to detect circular dependencies. If found, refactor to break cycles: extract shared code to new library (Module D contains common code, A/B/C all depend on D but not each other), or invert dependencies (use dependency injection so Module C depends on abstraction, Module A implements abstraction). Only proceed with migration after dependency graph is acyclic (DAG topology). |
| **Documented Standards Without Enforcement** | Publish comprehensive architecture guide: "All repos must use MVC pattern, max function length 50 lines, test coverage >80%". 6 months later, audit reveals: 12 of 20 repos don't use MVC, average function length 120 lines, test coverage 45%. Architecture guide is ignored because violations have no consequences. | Codify standards in `references/enforcement-rules.json` and run automated checks via `scripts/arch-lint.sh` in CI. Violations block PR merge (pre-commit hooks + CI pipeline enforcement). For existing violations, code-analyzer agent generates refactoring plan: prioritize by severity (god objects with 50+ methods = critical, inconsistent directory structure = low), create tracking issues, allocate 10% of sprint capacity to addressing architectural debt. Enforcement transforms architecture guide from aspirational documentation to executable specification. |

## Common Anti-Patterns

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| **Parallel Updates Ignoring Dependencies** | Deploy Service A v2.0 (breaking API) and Service B v1.5 (expects v2.0 API) simultaneously. Service B deploys first due to faster CI. Service B crashes with "method not found". 45min production outage until rollback. | Use dependency-aware deployment sequencing: hierarchical-coordinator analyzes dependency graph, topologically sorts repos (upstream first), deploys in waves with validation gates. For A/B: Deploy A v2.0, wait for health checks, THEN deploy B v1.5. Sequential deployment prevents dependency-ordering outages. |
| **Monorepo Migration Without Cycle Analysis** | Split monorepo into 3 repos without analyzing imports. Module A imports B, B imports C, C imports A (circular dependency invisible in monorepo). After split: deployment gridlock - can't deploy any repo without deploying all 3 atomically. | Run analyze-deps.sh BEFORE migration to detect circular dependencies. If found, refactor to break cycles: extract shared code to new library (Module D), or invert dependencies (use dependency injection). Only proceed after dependency graph is acyclic (DAG topology). |
| **Documented Standards Without Enforcement** | Publish architecture guide: "All repos use MVC, max function 50 lines, coverage >80%". 6 months later: 12 of 20 repos don't use MVC, avg function 120 lines, coverage 45%. Guide ignored because violations have no consequences. | Codify standards in enforcement-rules.json and run arch-lint.sh in CI. Violations block PR merge. For existing violations, code-analyzer generates refactoring plan prioritized by severity. Allocate 10% sprint capacity to architectural debt. Enforcement transforms guide from aspirational to executable. |

---

## Conclusion

Multi-repository management scales organizational complexity through deliberate architecture and automated coordination. The workflows documented here (dependency-aware change propagation, history-preserving monorepo migration, automated architectural enforcement) transform multi-repo operations from error-prone manual processes into orchestrated agent workflows. The fundamental challenge: maintaining consistency across distributed codebases without central coordination overhead.

Success requires three architectural commitments: dependency graph discipline (understand and respect dependency order, visualize with `repo-graph.sh`, enforce with topological deployment sequencing), migration planning rigor (monorepo-to-multi-repo is one-way door, requires exhaustive dependency analysis and circular dependency elimination), and automated enforcement (architectural standards codified in `enforcement-rules.json` and checked in CI, not documented in ignored wikis). Without these commitments, multi-repo architectures degrade into fragmented codebases with inconsistent patterns, broken dependencies, and deployment gridlock.

The hierarchical agent topology (central coordinator orchestrating repository-specific workers) enables parallel execution within dependency constraints while maintaining global consistency. This is critical for large-scale operations: propagating API changes across 20 repositories requires parallel updates (serial execution would take days) but must respect dependency order (upstream before downstream). The coordinator maintains the dependency graph, workers execute repository-specific tasks, and the topology ensures both parallelism and correctness.

Implementation sequencing matters: Start with dependency graph visualization (`repo-graph.sh build-graph` for all repositories), then implement automated architectural linting (`arch-lint.sh` in CI pipelines), then attempt coordinated operations (cross-repo refactoring, synchronized releases). Attempting multi-repo operations without dependency understanding and enforcement infrastructure results in production outages and permanent architectural drift. The upfront investment in coordination infrastructure (typically 1-2 weeks) prevents months of firefighting dependency conflicts and architectural inconsistency.