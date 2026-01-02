#!/bin/bash
# five-phase-enforcer.sh
# PURPOSE: Enforce 5-phase workflow on every non-trivial request
# HOOK TYPE: UserPromptSubmit (runs before Claude processes user message)
#
# This hook classifies user requests and injects 5-phase workflow requirements
# for non-trivial tasks, ensuring Claude follows the SOP.

# Read the user's message from stdin
USER_MESSAGE=$(timeout 5 cat 2>/dev/null || echo '{}')

# Extract the actual message text
MESSAGE_TEXT=$(echo "$USER_MESSAGE" | jq -r '.message // empty' 2>/dev/null || echo "$USER_MESSAGE")

# ============================================================================
# CLASSIFICATION: Is this a trivial or non-trivial request?
# ============================================================================

# Trivial patterns (skip 5-phase)
TRIVIAL_PATTERNS=(
    "^(hi|hello|hey|thanks|thank you|ok|okay|yes|no|bye)$"
    "^what (is|are|does|do) "
    "^(can you|could you) explain"
    "^(help|/help|/clear|/status)"
    "^show me"
    "^list "
    "^read "
    "^(git status|git log|ls|pwd)"
)

IS_TRIVIAL=false

for pattern in "${TRIVIAL_PATTERNS[@]}"; do
    if echo "$MESSAGE_TEXT" | grep -iqE "$pattern"; then
        IS_TRIVIAL=true
        break
    fi
done

# Non-trivial patterns (REQUIRE 5-phase)
NONTRIVIAL_PATTERNS=(
    "(build|create|implement|develop|add|make)"
    "(fix|debug|repair|resolve|solve)"
    "(refactor|optimize|improve|enhance)"
    "(analyze|audit|review|check|validate)"
    "(deploy|release|ship|publish)"
    "(test|spec|coverage)"
    "(design|architect|plan|strategy)"
)

for pattern in "${NONTRIVIAL_PATTERNS[@]}"; do
    if echo "$MESSAGE_TEXT" | grep -iqE "$pattern"; then
        IS_TRIVIAL=false
        break
    fi
done

# ============================================================================
# ENFORCEMENT: Inject 5-phase requirement for non-trivial requests
# ============================================================================

if [ "$IS_TRIVIAL" = false ]; then
    cat << 'EOF'

!! 5-PHASE WORKFLOW ENFORCEMENT !!

This appears to be a NON-TRIVIAL request. You MUST execute the 5-phase workflow:

PHASE 1: INTENT ANALYSIS (MANDATORY)
  - Invoke: Skill("intent-analyzer")
  - Output: Understood intent + confidence score
  - If confidence < 80%: Ask clarifying questions FIRST

PHASE 2: PROMPT OPTIMIZATION (MANDATORY)
  - Invoke: Skill("prompt-architect")
  - Output: Optimized request + success criteria

PHASE 3: STRATEGIC PLANNING (MANDATORY)
  - Invoke: Skill("research-driven-planning") OR Skill("planner")
  - Output: Task breakdown + dependencies + parallelization strategy

PHASE 4: PLAYBOOK/SKILL ROUTING (MANDATORY)
  - Match tasks to playbooks from catalog
  - Output: Routing decisions for each task

PHASE 5: EXECUTION (MANDATORY)
  - Execute using routed playbooks/skills
  - Spawn agents via Task() - AGENTS FROM REGISTRY ONLY
  - Track progress via TodoWrite()
  - Golden Rule: 1 MESSAGE = ALL PARALLEL OPERATIONS

DOMAIN EXPERTISE (NEW - CHECK FIRST):
  - Does domain have expertise file? Check: .claude/expertise/{domain}.yaml
  - If YES: Load and validate before Phase 3
  - If NO: Generate expertise as side effect

!! CRITICAL: SKILL EVALUATION REQUIRED !!

BEFORE proceeding with implementation, you MUST execute this 3-step evaluation:

STEP 1 - EVALUATE (MANDATORY):
For EACH skill category below, state: [skill-name] - YES/NO - [reason]

DEVELOPMENT SKILLS:
  - feature-dev-complete (12-stage feature lifecycle with research/testing)
  - smart-bug-fix (systematic debugging with root cause analysis)
  - pair-programming (collaborative coding with best practices)
  - reverse-engineering-quick (fast code understanding/documentation)
  - reverse-engineering-deep (comprehensive system analysis)

QUALITY SKILLS:
  - functionality-audit (sandbox testing + execution verification)
  - theater-detection-audit (detect fake/non-functional code)
  - code-review-assistant (multi-agent PR review with security/performance)
  - style-audit (code style + standards enforcement)
  - clarity-linter (cognitive load + readability optimization)

ORCHESTRATION SKILLS:
  - cascade-orchestrator (multi-skill workflow coordination)
  - swarm-orchestration (parallel multi-agent execution)
  - hive-mind-advanced (queen-led collective intelligence)
  - ai-dev-orchestration (5-phase app development SOP)

TESTING SKILLS:
  - testing-quality (comprehensive test suite generation)
  - reproducibility-audit (experiment reproducibility validation)
  - verification-quality (formal verification + proof checking)

INFRASTRUCTURE SKILLS:
  - infrastructure (Docker/Terraform/K8s automation)
  - cicd-intelligent-recovery (CI/CD with failure recovery)
  - deployment-readiness (production deployment validation)
  - network-security-setup (network security automation)

RESEARCH SKILLS:
  - deep-research-orchestrator (9-pipeline research lifecycle)
  - literature-synthesis (literature review + gap analysis)
  - method-development (novel ML method development)
  - holistic-evaluation (multi-dimensional model evaluation)
  - baseline-replication (reproduce published experiments)

GITHUB SKILLS:
  - github-workflow-automation (GitHub Actions + CI/CD)
  - github-code-review (AI-powered GitHub PR review)
  - github-project-management (issue tracking + sprint planning)
  - github-release-management (versioning + deployment)
  - github-multi-repo (multi-repository coordination)

AGENT CREATION SKILLS:
  - agent-creator (create specialized agents with 5-phase SOP)
  - skill-creator-agent (create new skills)
  - agent-selector (intelligent agent selection from registry)

DATABASE SKILLS:
  - agentdb-vector-search (semantic search + RAG systems)
  - agentdb-memory-patterns (persistent agent memory)
  - agentdb-learning (reinforcement learning plugins)
  - agentdb-optimization (performance optimization)
  - database-specialists (SQL/NoSQL expertise)

PLATFORM SKILLS:
  - flow-nexus-platform (sandbox + deployment management)
  - flow-nexus-swarm (cloud swarm deployment)
  - flow-nexus-neural (distributed neural network training)

DOCUMENTATION SKILLS:
  - documentation (code docs + API docs + READMEs)
  - pptx-generation (PowerPoint presentation generation)

SPECIALIZED SKILLS:
  - i18n-automation (internationalization workflows)
  - sandbox-configurator (E2B sandbox setup)
  - performance-analysis (performance profiling + optimization)
  - debugging (systematic debugging hub)
  - security (security audit + compliance hub)
  - observability (monitoring + logging setup)

STEP 2 - ACTIVATE (MANDATORY):
If ANY skills matched YES in Step 1:
  - Use Skill(skill-name) tool for EACH relevant skill NOW
  - DO NOT proceed to implementation until skills are invoked
  - FAILURE TO INVOKE = VIOLATION OF PROTOCOL

If NO skills matched:
  - State "SKILL EVALUATION COMPLETE - No specialized skills needed"
  - Proceed with standard implementation

STEP 3 - IMPLEMENT (MANDATORY):
  - Only after Step 2 is complete, proceed with implementation
  - Use skill outputs to inform your approach
  - DO NOT skip or assume skill results

!! THIS IS A BLOCKING REQUIREMENT !!
You CANNOT proceed to implementation without completing Steps 1-3.
Skipping skill evaluation is a CRITICAL PROTOCOL VIOLATION.

DO NOT skip phases. DO NOT skip skill evaluation. DO NOT use generic agents.

EOF
fi

# Return success (hook continues)
exit 0
