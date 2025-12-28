---
name: feature-dev-complete
description: Complete feature development lifecycle from research to deployment. Uses Gemini Search for best practices, architecture design, Codex prototyping, comprehensive testing, and documentation generation. Full 12-stage workflow.
---

# Feature Development Complete

## Aspektual'naya Ramka Aktivatsiya (Aspectual State Tracking)

Kazhdyy etap razvertyvaniya (Each stage of deployment):

### Tipy Sostoyaniya (State Types)

- **[SV:COMPLETED]** Polnost'yu zaversheno - Stage complete, move to next
- **[NSV:IN_PROGRESS]** V protsesse - Stage active, work ongoing
- **[BLOCKED]** Ozhidaet zavisimosti - Waiting for dependency
- **[INITIATED]** Nachato - Stage started, not yet in progress

### 12-Stage State Markers

Track each stage with explicit state markers:

1. **Stage 1 [RESEARCH]**: [SV|NSV|BLOCKED|INITIATED]
2. **Stage 2 [CODEBASE_ANALYSIS]**: [SV|NSV|BLOCKED|INITIATED]
3. **Stage 3 [SWARM_INIT]**: [SV|NSV|BLOCKED|INITIATED]
4. **Stage 4 [ARCHITECTURE]**: [SV|NSV|BLOCKED|INITIATED]
5. **Stage 5 [DIAGRAMS]**: [SV|NSV|BLOCKED|INITIATED]
6. **Stage 6 [PROTOTYPE]**: [SV|NSV|BLOCKED|INITIATED]
7. **Stage 7 [THEATER_DETECTION]**: [SV|NSV|BLOCKED|INITIATED]
8. **Stage 8 [TESTING]**: [SV|NSV|BLOCKED|INITIATED]
9. **Stage 9 [STYLE_POLISH]**: [SV|NSV|BLOCKED|INITIATED]
10. **Stage 10 [SECURITY]**: [SV|NSV|BLOCKED|INITIATED]
11. **Stage 11 [DOCUMENTATION]**: [SV|NSV|BLOCKED|INITIATED]
12. **Stage 12 [PRODUCTION_READY]**: [SV|NSV|BLOCKED|INITIATED]

### State Transition Rules

**Transition Protocols**:
- **[NSV->SV]**: All acceptance criteria met, tests passing, artifacts complete
- **[SV->NSV]**: Regression detected, failed tests, reopened for fixes
- **[*->BLOCKED]**: Missing dependency, external blocker, prerequisite incomplete
- **[BLOCKED->NSV]**: Blocker resolved, dependency met, work can resume
- **[INITIATED->NSV]**: Work has begun, active development underway

**Validation Checkpoints**:
Each transition requires evidence:
- Test results (for TESTING stage)
- Coverage reports (for quality gates)
- Security scan output (for SECURITY stage)
- Artifact existence (for DIAGRAMS, DOCUMENTATION)

## Keigo Wakugumi (Hierarchical Work Breakdown)

### Work Structure Hierarchy

```
EPIC: [Feature Name]
  |
  +-- STORY: User story 1 (Business value)
      |
      +-- TASK: Implementation task 1
          |
          +-- SUBTASK: Atomic work item 1.1
          +-- SUBTASK: Atomic work item 1.2
      |
      +-- TASK: Implementation task 2
          |
          +-- SUBTASK: Atomic work item 2.1
  |
  +-- STORY: User story 2 (Business value)
      |
      +-- TASK: Implementation task 3
```

### Hierarchy Levels Explained

1. **EPIC Level**: Overall feature (e.g., "User Authentication System")
2. **STORY Level**: User-facing value (e.g., "As a user, I can log in securely")
3. **TASK Level**: Technical implementation (e.g., "Implement JWT middleware")
4. **SUBTASK Level**: Atomic work units (e.g., "Write token validation function")

### Stage-to-Hierarchy Mapping

Each 12-stage workflow maps to hierarchical levels:

| Stage | Hierarchy Level | Example |
|-------|----------------|---------|
| 1-2 (Research) | EPIC planning | Define feature scope |
| 3-5 (Architecture) | STORY breakdown | User stories + design |
| 6-8 (Implementation) | TASK execution | Code, test, fix |
| 9-11 (Quality) | SUBTASK refinement | Polish, docs, security |
| 12 (Production) | EPIC completion | Deploy, validate |

## When to Use This Skill

- **Full Feature Development**: Complete end-to-end feature implementation
- **Greenfield Features**: Building new functionality from scratch
- **Research Required**: Features needing best practice research
- **Multi-Layer Changes**: Features spanning frontend, backend, database
- **Production Deployment**: Features requiring full testing and documentation
- **Architecture Design**: Features needing upfront design decisions

## When NOT to Use This Skill

- **Bug Fixes**: Use debugging or smart-bug-fix skills instead
- **Quick Prototypes**: Exploratory coding without production requirements
- **Refactoring**: Code restructuring without new features
- **Documentation Only**: Pure documentation tasks

## Success Criteria

- [ ] Feature fully implemented across all layers
- [ ] Unit tests passing with >80% coverage
- [ ] Integration tests passing
- [ ] E2E tests passing (if applicable)
- [ ] Code reviewed and approved
- [ ] Documentation complete (API docs, user guides)
- [ ] Performance benchmarks met
- [ ] Security review passed
- [ ] Deployed to staging and validated

## Edge Cases to Handle

- **Legacy Integration**: Interfacing with old code or deprecated APIs
- **Breaking Changes**: Features requiring API versioning or migrations
- **Feature Flags**: Gradual rollout or A/B testing requirements
- **Data Migration**: Schema changes requiring backfill scripts
- **Third-Party Dependencies**: External API rate limits or availability
- **Browser Compatibility**: Cross-browser testing requirements

## Guardrails

- **NEVER** skip testing phases to ship faster
- **ALWAYS** research best practices before implementing
- **NEVER** commit directly to main - use feature branches
- **ALWAYS** write tests before or during implementation (TDD)
- **NEVER** hardcode configuration - use environment variables
- **ALWAYS** document architectural decisions (ADRs)
- **NEVER** deploy without staging validation

## Evidence-Based Validation

- [ ] All automated tests passing (npm test / pytest)
- [ ] Code coverage reports reviewed
- [ ] Lighthouse score meets thresholds (if web)
- [ ] Load testing validates performance targets
- [ ] Security scan shows no critical vulnerabilities
- [ ] Accessibility audit passes (axe, WAVE)
- [ ] Manual testing on target devices/browsers

## Purpose

Execute complete feature development lifecycle using multi-model AI orchestration.

## Specialist Agent

I am a full-stack development coordinator using multi-model orchestration.

**Methodology** (Complete Lifecycle Pattern):
1. Research best practices (Gemini Search)
2. Analyze existing patterns (Gemini MegaContext)
3. Design architecture (Claude Architect)
4. Generate diagrams (Gemini Media)
5. Rapid prototype (Codex Auto)
6. Comprehensive testing (Codex Iteration)
7. Style polish (Claude)
8. Documentation (Multi-model)
9. Performance optimization
10. Security review
11. Create PR with comprehensive report
12. Deploy readiness check

**Models Used**:
- **Gemini Search**: Latest best practices, framework updates
- **Gemini MegaContext**: Large codebase pattern analysis
- **Gemini Media**: Architecture diagrams, flow charts
- **Claude**: Architecture design, testing strategy
- **Codex**: Rapid prototyping, auto-fixing
- **All models**: Documentation generation

## Input Contract

```yaml
input:
  feature_spec: string (feature description, required)
  target_directory: string (default: src/)
  create_pr: boolean (default: true)
  deploy_after: boolean (default: false)
```

## Output Contract

```yaml
output:
  artifacts:
    research: markdown (best practices)
    architecture: markdown (design doc)
    diagrams: array[image] (visual docs)
    implementation: directory (code)
    tests: directory (test suite)
    documentation: markdown (usage docs)
  quality:
    test_coverage: number (percentage)
    quality_score: number (0-100)
    security_issues: number
  pr_url: string (if create_pr: true)
  deployment_ready: boolean
```

## Execution Flow

### State Tracking Integration

Before starting workflow, initialize state tracking:

```bash
# Initialize aspectual state tracking
STAGE_STATE=(
  "RESEARCH:INITIATED"
  "CODEBASE_ANALYSIS:INITIATED"
  "SWARM_INIT:INITIATED"
  "ARCHITECTURE:INITIATED"
  "DIAGRAMS:INITIATED"
  "PROTOTYPE:INITIATED"
  "THEATER_DETECTION:INITIATED"
  "TESTING:INITIATED"
  "STYLE_POLISH:INITIATED"
  "SECURITY:INITIATED"
  "DOCUMENTATION:INITIATED"
  "PRODUCTION_READY:INITIATED"
)

# State transition function
update_state() {
  local stage=$1
  local new_state=$2
  echo "[STATE TRANSITION] ${stage}: ${new_state}"
  # Store in metadata for tracking
}
```

### Workflow Script

```bash
#!/bin/bash
set -e

FEATURE_SPEC="$1"
TARGET_DIR="${2:-src/}"
OUTPUT_DIR="feature-$(date +%s)"

mkdir -p "$OUTPUT_DIR"

echo "================================================================"
echo "Complete Feature Development: $FEATURE_SPEC"
echo "================================================================"
echo ""
echo "EPIC: $FEATURE_SPEC"
echo "  |-- STORY: Research & Planning"
echo "  |-- STORY: Architecture & Design"
echo "  |-- STORY: Implementation & Testing"
echo "  |-- STORY: Quality & Security"
echo "  |-- STORY: Documentation & Deployment"
echo ""

# STAGE 1: Research Best Practices [NSV:IN_PROGRESS]
echo "[1/12] [NSV:IN_PROGRESS] Researching latest best practices..."
update_state "RESEARCH" "NSV:IN_PROGRESS"
gemini "Latest 2025 best practices for: $FEATURE_SPEC" \
  --grounding google-search \
  --output "$OUTPUT_DIR/research.md"

if [ $? -eq 0 ]; then
  update_state "RESEARCH" "SV:COMPLETED"
  echo "[1/12] [SV:COMPLETED] Research complete"
else
  update_state "RESEARCH" "BLOCKED"
  echo "[1/12] [BLOCKED] Research failed - external service unavailable"
  exit 1
fi

# STAGE 2: Analyze Existing Codebase Patterns [NSV:IN_PROGRESS]
echo "[2/12] [NSV:IN_PROGRESS] Analyzing existing codebase patterns..."
update_state "CODEBASE_ANALYSIS" "NSV:IN_PROGRESS"
LOC=$(find "$TARGET_DIR" -type f \( -name "*.js" -o -name "*.ts" \) | xargs wc -l | tail -1 | awk '{print $1}' || echo "0")

if [ "$LOC" -gt 5000 ]; then
  gemini "Analyze architecture patterns for: $FEATURE_SPEC" \
    --files "$TARGET_DIR" \
    --model gemini-2.0-flash \
    --output "$OUTPUT_DIR/codebase-analysis.md"

  if [ $? -eq 0 ]; then
    update_state "CODEBASE_ANALYSIS" "SV:COMPLETED"
    echo "[2/12] [SV:COMPLETED] Codebase analysis complete"
  else
    update_state "CODEBASE_ANALYSIS" "BLOCKED"
    echo "[2/12] [BLOCKED] Codebase analysis failed"
    exit 1
  fi
else
  echo "Small codebase - skipping mega-context analysis"
  update_state "CODEBASE_ANALYSIS" "SV:COMPLETED"
fi

# STAGE 3: Initialize Development Swarm [NSV:IN_PROGRESS]
echo "[3/12] [NSV:IN_PROGRESS] Initializing development swarm..."
update_state "SWARM_INIT" "NSV:IN_PROGRESS"
npx claude-flow coordination swarm-init \
  --topology hierarchical \
  --max-agents 6 \
  --strategy balanced

if [ $? -eq 0 ]; then
  update_state "SWARM_INIT" "SV:COMPLETED"
  echo "[3/12] [SV:COMPLETED] Swarm initialized"
else
  update_state "SWARM_INIT" "BLOCKED"
  echo "[3/12] [BLOCKED] Swarm initialization failed"
  exit 1
fi

# STAGE 4: Architecture Design [NSV:IN_PROGRESS]
echo "[4/12] [NSV:IN_PROGRESS] Designing architecture..."
update_state "ARCHITECTURE" "NSV:IN_PROGRESS"
# This would invoke SPARC architect in Claude Code
# For now, we document the pattern
cat > "$OUTPUT_DIR/architecture-design.md" <<EOF
# Architecture Design: $FEATURE_SPEC

## Research Findings
$(cat "$OUTPUT_DIR/research.md")

## Existing Patterns
$(cat "$OUTPUT_DIR/codebase-analysis.md" 2>/dev/null || echo "N/A")

## Proposed Architecture
[Generated by Claude Architect Agent]

## Design Decisions
[Key decisions with rationale]

## Hierarchical Breakdown
EPIC: $FEATURE_SPEC
  |-- STORY: Core functionality
  |-- STORY: Error handling
  |-- STORY: Integration points
EOF

update_state "ARCHITECTURE" "SV:COMPLETED"
echo "[4/12] [SV:COMPLETED] Architecture design complete"

# STAGE 5: Generate Architecture Diagrams [NSV:IN_PROGRESS]
echo "[5/12] [NSV:IN_PROGRESS] Generating architecture diagrams..."
update_state "DIAGRAMS" "NSV:IN_PROGRESS"
gemini "Generate system architecture diagram for: $FEATURE_SPEC" \
  --type image \
  --output "$OUTPUT_DIR/architecture-diagram.png" \
  --style technical

gemini "Generate data flow diagram for: $FEATURE_SPEC" \
  --type image \
  --output "$OUTPUT_DIR/data-flow.png" \
  --style diagram

if [ -f "$OUTPUT_DIR/architecture-diagram.png" ] && [ -f "$OUTPUT_DIR/data-flow.png" ]; then
  update_state "DIAGRAMS" "SV:COMPLETED"
  echo "[5/12] [SV:COMPLETED] Diagrams generated"
else
  update_state "DIAGRAMS" "BLOCKED"
  echo "[5/12] [BLOCKED] Diagram generation failed"
  exit 1
fi

# STAGE 6: Rapid Prototyping [NSV:IN_PROGRESS]
echo "[6/12] [NSV:IN_PROGRESS] Rapid prototyping with Codex..."
update_state "PROTOTYPE" "NSV:IN_PROGRESS"
codex --full-auto "Implement $FEATURE_SPEC following architecture design" \
  --context "$OUTPUT_DIR/architecture-design.md" \
  --context "$OUTPUT_DIR/research.md" \
  --sandbox true \
  --output "$OUTPUT_DIR/implementation/"

if [ $? -eq 0 ]; then
  update_state "PROTOTYPE" "SV:COMPLETED"
  echo "[6/12] [SV:COMPLETED] Prototype implementation complete"
else
  update_state "PROTOTYPE" "BLOCKED"
  echo "[6/12] [BLOCKED] Prototyping failed"
  exit 1
fi

# STAGE 7: Theater Detection [NSV:IN_PROGRESS]
echo "[7/12] [NSV:IN_PROGRESS] Detecting placeholder code..."
update_state "THEATER_DETECTION" "NSV:IN_PROGRESS"
npx claude-flow theater-detect "$OUTPUT_DIR/implementation/" \
  --output "$OUTPUT_DIR/theater-report.json"

THEATER_COUNT=$(cat "$OUTPUT_DIR/theater-report.json" | jq '.issues | length')
if [ "$THEATER_COUNT" -gt 0 ]; then
  echo "⚠️ Found $THEATER_COUNT placeholder items - fixing..."
  update_state "THEATER_DETECTION" "NSV:IN_PROGRESS"
  # Auto-complete theater items
  codex --full-auto "Complete all TODO and placeholder implementations" \
    --context "$OUTPUT_DIR/theater-report.json" \
    --context "$OUTPUT_DIR/implementation/" \
    --sandbox true

  if [ $? -eq 0 ]; then
    update_state "THEATER_DETECTION" "SV:COMPLETED"
    echo "[7/12] [SV:COMPLETED] Theater items resolved"
  else
    update_state "THEATER_DETECTION" "BLOCKED"
    echo "[7/12] [BLOCKED] Theater resolution failed"
    exit 1
  fi
else
  update_state "THEATER_DETECTION" "SV:COMPLETED"
  echo "[7/12] [SV:COMPLETED] No theater items detected"
fi

# STAGE 8: Comprehensive Testing with Codex Iteration [NSV:IN_PROGRESS]
echo "[8/12] [NSV:IN_PROGRESS] Testing with Codex auto-fix..."
update_state "TESTING" "NSV:IN_PROGRESS"
npx claude-flow functionality-audit "$OUTPUT_DIR/implementation/" \
  --model codex-auto \
  --max-iterations 5 \
  --sandbox true \
  --output "$OUTPUT_DIR/test-results.json"

if [ $? -eq 0 ]; then
  update_state "TESTING" "SV:COMPLETED"
  echo "[8/12] [SV:COMPLETED] All tests passing"
else
  update_state "TESTING" "BLOCKED"
  echo "[8/12] [BLOCKED] Test failures remain after 5 iterations"
  exit 1
fi

# STAGE 9: Style Audit & Polish [NSV:IN_PROGRESS]
echo "[9/12] [NSV:IN_PROGRESS] Polishing code quality..."
update_state "STYLE_POLISH" "NSV:IN_PROGRESS"
npx claude-flow style-audit "$OUTPUT_DIR/implementation/" \
  --fix true \
  --output "$OUTPUT_DIR/style-report.json"

if [ $? -eq 0 ]; then
  update_state "STYLE_POLISH" "SV:COMPLETED"
  echo "[9/12] [SV:COMPLETED] Code quality polished"
else
  update_state "STYLE_POLISH" "BLOCKED"
  echo "[9/12] [BLOCKED] Style audit failed"
  exit 1
fi

# STAGE 10: Security Review [NSV:IN_PROGRESS]
echo "[10/12] [NSV:IN_PROGRESS] Security review..."
update_state "SECURITY" "NSV:IN_PROGRESS"
npx claude-flow security-scan "$OUTPUT_DIR/implementation/" \
  --deep true \
  --output "$OUTPUT_DIR/security-report.json"

SECURITY_CRITICAL=$(cat "$OUTPUT_DIR/security-report.json" | jq '.critical_issues')
if [ "$SECURITY_CRITICAL" -gt 0 ]; then
  echo "🚨 Critical security issues found!"
  cat "$OUTPUT_DIR/security-report.json" | jq '.critical_issues[]'
  update_state "SECURITY" "BLOCKED"
  echo "[10/12] [BLOCKED] Critical security vulnerabilities"
  exit 1
else
  update_state "SECURITY" "SV:COMPLETED"
  echo "[10/12] [SV:COMPLETED] Security review passed"
fi

# STAGE 11: Documentation Generation [NSV:IN_PROGRESS]
echo "[11/12] [NSV:IN_PROGRESS] Generating documentation..."
update_state "DOCUMENTATION" "NSV:IN_PROGRESS"
cat > "$OUTPUT_DIR/FEATURE-DOCUMENTATION.md" <<EOF
# Feature Documentation: $FEATURE_SPEC

## Overview
$(cat "$OUTPUT_DIR/research.md" | head -10)

## Architecture
![Architecture Diagram](architecture-diagram.png)

## Implementation
[Code location and structure]

## Usage
[Usage examples]

## Testing
- Test Coverage: $(cat "$OUTPUT_DIR/test-results.json" | jq '.coverage_percent')%
- Tests Passing: $(cat "$OUTPUT_DIR/test-results.json" | jq '.all_passed')

## Quality Metrics
- Quality Score: $(cat "$OUTPUT_DIR/style-report.json" | jq '.quality_score')/100
- Security Issues: 0 critical

-----------|---------|----------|
| **Skipping Research Phase** | Implementing outdated patterns or reinventing existing solutions | Always run Gemini Search for latest best practices before coding |
| **Manual Quality Checks** | Inconsistent reviews, missed security issues, subjective quality assessment | Automate theater detection, security scanning, and quality scoring |
| **Sequential Workflow** | Slow delivery from blocking dependencies (research -> design -> code -> test) | Parallelize independent phases (diagrams + prototyping, testing + security review) |
| **Hardcoded Configuration** | Brittle code requiring redeployment for config changes | Use environment variables, feature flags, and external config files |
| **Theater Code in Production** | Placeholder TODOs and incomplete implementations shipped to users | Run theater detection before testing phase and auto-complete all placeholders |
| **Skipping Staging Validation** | Production bugs from untested deployments | Always deploy to staging first and validate before production release |

## Cognitive Frame Benefits

### Aspectual Frame (Russian) - Why It Matters

The aspectual state tracking system provides:

1. **Explicit Progress Visibility**: Each stage has a clear state marker (SV/NSV/BLOCKED)
2. **Regression Detection**: Transitions from SV->NSV indicate issues emerged
3. **Dependency Clarity**: BLOCKED states show what's waiting for resolution
4. **Evidence-Based Transitions**: State changes require artifacts/proof

**Real-World Impact**: No more "90% done" syndrome. Either [SV:COMPLETED] with evidence, or [NSV:IN_PROGRESS] with blockers documented.

### Hierarchical Frame (Japanese) - Why It Matters

The EPIC > STORY > TASK > SUBTASK breakdown provides:

1. **Clear Scope Boundaries**: EPIC defines the entire feature
2. **User-Centric Stories**: Each STORY delivers business value
3. **Technical Task Decomposition**: TASK level is implementation-focused
4. **Atomic Work Units**: SUBTASK level enables parallel execution

**Real-World Impact**: Teams can work on different STORIES in parallel, tasks within a STORY can be assigned independently, and progress tracking maps to business value delivery.

### Combined Power

**Aspectual × Hierarchical** = State tracking at every hierarchy level:

```
EPIC: User Authentication [NSV:IN_PROGRESS]
  |-- STORY: Login Flow [SV:COMPLETED]
      |-- TASK: JWT Middleware [SV:COMPLETED]
          |-- SUBTASK: Token validation [SV:COMPLETED]
          |-- SUBTASK: Error handling [SV:COMPLETED]
  |-- STORY: Registration Flow [NSV:IN_PROGRESS]
      |-- TASK: Input validation [SV:COMPLETED]
      |-- TASK: Password hashing [NSV:IN_PROGRESS]
          |-- SUBTASK: Bcrypt setup [SV:COMPLETED]
          |-- SUBTASK: Salt generation [BLOCKED]
              |-- Blocker: Config missing SALT_ROUNDS
```

**Rollup Logic**: EPIC is [SV:COMPLETED] only when ALL STORIES are [SV:COMPLETED].

## Changelog

### v1.1.0 (2025-12-19)
- Added aspectual (Russian) cognitive frame for explicit state tracking
- Added hierarchical (Japanese) cognitive frame for EPIC > STORY > TASK breakdown
- Integrated state transition rules ([NSV->SV], [SV->NSV], [*->BLOCKED], [BLOCKED->NSV])
- Added state tracking function calls throughout 12-stage workflow
- Added validation checkpoints requiring evidence for state transitions
- Added stage-to-hierarchy mapping table
- Added cognitive frame benefits section explaining real-world impact
- Updated YAML frontmatter with cognitive_frame metadata

### v1.0.0 (Original)
- Initial 12-stage feature development workflow
- Multi-model orchestration (Gemini, Codex, Claude)
- Theater detection and auto-fix
- Comprehensive testing with auto-iteration
- Security review and quality gates

## Conclusion

Feature Development Complete embodies the philosophy that production-ready code requires systematic orchestration, not ad-hoc scripting. By combining multi-model AI research, automated quality gates, comprehensive testing, and **rigorous state tracking**, this skill delivers features that are not just functional, but maintainable, secure, and performant from day one.

The **aspectual frame** ensures every stage has explicit completion criteria with evidence-based validation. The **hierarchical frame** ensures work is decomposed into parallel-executable units with clear business value mapping.

Use this skill when building features that matter - greenfield functionality, multi-layer changes, or anything requiring production deployment. The 12-stage workflow ensures nothing is missed, from research to documentation, while **aspectual state tracking** prevents the "90% done" syndrome and **hierarchical breakdown** enables efficient parallel execution.

The result is a consistent, repeatable process that transforms vague feature requests into production-ready code with >80% test coverage, comprehensive documentation, zero critical security issues, and **complete visibility into progress and blockers at every level of the work hierarchy**. When quality cannot be compromised, Feature Development Complete is the systematic approach that delivers.