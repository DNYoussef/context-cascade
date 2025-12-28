---
name: research-driven-planning
description: Loop 1 of the Three-Loop Integrated Development System. Research-driven requirements analysis with iterative risk mitigation through 5x pre-mortem cycles using multi-agent consensus. Feeds validated, risk-mitigated plans to parallel-swarm-implementation. Use when starting new features or projects requiring comprehensive planning with <3% failure confidence and evidence-based technology selection.
---

requirements analysis with iterative risk mitigation through 5x pre-mortem cycles
  using multi-agent consensus. Feeds validated, risk-mitigated plans to parallel-swarm-implementation.
  Use when starting new features or projects requiring comprehensive planning with
  <3% failure confidence and evidence-based technology selection.
- research
- analysis
- planning


## When to Use This Skill

Activate this skill when:
- Starting a new feature or project requiring comprehensive planning
- Need to prevent problems before coding begins (85-95% failure prevention)
- Want research-backed solutions instead of assumptions (30-60% time savings)
- Require risk analysis with <3% failure confidence
- Building something complex with multiple failure modes
- Need evidence-based planning that feeds into implementation

**DO NOT** use this skill for:
- Quick fixes or trivial changes (use direct implementation)
- Well-understood repetitive tasks (use existing patterns)
- Emergency hotfixes (skip to Loop 2)



## SOP Phase 1: Specification

**Objective**: Define initial requirements with clarity and structure.

### Create SPEC.md

Generate a comprehensive specification document in the project root:

```markdown
# Project Specification

## Overview
[High-level description of what needs to be built]

## Requirements
### Functional Requirements
1. [Core feature 1]
2. [Core feature 2]
...

### Non-Functional Requirements
- Performance: [metrics]
- Security: [requirements]
- Scalability: [targets]
- Compliance: [standards]

## Constraints
- Technical: [language, framework, dependencies]
- Timeline: [deadlines, milestones]
- Resources: [team size, budget, infrastructure]

## Success Criteria
1. [Measurable outcome 1]
2. [Measurable outcome 2]
...

## Out of Scope
- [Explicitly excluded features]
```

### Store Initial Context

```bash
npx claude-flow@alpha memory store \
  "project_spec" \
  "$(cat SPEC.md)" \
  --namespace "loop1/specification"
```

**Output**: Structured SPEC.md file and memory-stored specification



## SOP Phase 3: Planning

**Objective**: Generate structured implementation plans with comprehensive context.

### Step 1: Convert SPEC.md to Structured Plan

Use the spec-to-plan transformation:

```bash
/spec:plan
```

This auto-generates `plan.json` with:
- **Task Breakdown**: Hierarchical task decomposition (MECE: Mutually Exclusive, Collectively Exhaustive)
- **Dependencies**: Task ordering and prerequisites
- **Resource Estimates**: Time, complexity, agent assignments
- **Risk Flags**: Tasks identified as high-risk

### Step 2: Enhance Plan with Research Context

Enrich the plan with research findings:

```bash
# Integration script
node <<'EOF'
const plan = require('./plan.json');
const research = require('./.claude/.artifacts/research-synthesis.json');

// Merge research recommendations into plan tasks
plan.tasks.forEach(task => {
  const relevantPatterns = research.patterns.filter(p =>
    p.relevance.includes(task.domain)
  );
  task.recommendedApproaches = relevantPatterns;
  task.knownRisks = research.risks.filter(r => r.applies_to.includes(task.type));
  task.evidenceSources = relevantPatterns.flatMap(p => p.sources);
});

require('fs').writeFileSync('plan-enhanced.json', JSON.stringify(plan, null, 2));
console.log('✅ Plan enhanced with research context');
EOF
```

### Step 3: Store Enhanced Plan

```bash
npx claude-flow@alpha memory store \
  "enhanced_plan" \
  "$(cat plan-enhanced.json)" \
  --namespace "loop1/planning"
```

**Validation Checkpoint**: Enhanced plan must cover all SPEC.md requirements with research-backed approaches.

**Output**: Structured, research-backed implementation plan



## SOP Phase 5: Knowledge (Planning Package Generation)

**Objective**: Package and persist validated planning data for Loop 2 and future iterations.

### Step 1: Generate Planning Package

Create comprehensive planning artifact for Loop 2 integration:

```bash
node <<'EOF'
const fs = require('fs');

const planningPackage = {
  metadata: {
    loop: 1,
    phase: 'research-driven-planning',
    timestamp: new Date().toISOString(),
    nextLoop: 'parallel-swarm-implementation',
    version: '1.0.0'
  },
  specification: {
    file: 'SPEC.md',
    content: fs.readFileSync('SPEC.md', 'utf8'),
    requirements_count: (fs.readFileSync('SPEC.md', 'utf8').match(/^###/gm) || []).length
  },
  research: {
    synthesis: JSON.parse(fs.readFileSync('.claude/.artifacts/research-synthesis.json', 'utf8')),
    evidence_sources: JSON.parse(fs.readFileSync('.claude/.artifacts/research-synthesis.json', 'utf8')).total_sources,
    confidence_score: JSON.parse(fs.readFileSync('.claude/.artifacts/research-synthesis.json', 'utf8')).overall_confidence
  },
  planning: {
    enhanced_plan: JSON.parse(fs.readFileSync('plan-enhanced.json', 'utf8')),
    total_tasks: JSON.parse(fs.readFileSync('plan-enhanced.json', 'utf8')).tasks.length,
    estimated_complexity: JSON.parse(fs.readFileSync('plan-enhanced.json', 'utf8')).metadata.complexity
  },
  risk_analysis: {
    premortem: JSON.parse(fs.readFileSync('.claude/.artifacts/premortem-final.json', 'utf8')),
    final_failure_confidence: JSON.parse(fs.readFileSync('.claude/.artifacts/premortem-final.json', 'utf8')).final_failure_confidence,
    critical_risks_mitigated: JSON.parse(fs.readFileSync('.claude/.artifacts/premortem-final.json', 'utf8')).critical_risks_mitigated
  },
  integrationPoints: {
    feedsTo: 'parallel-swarm-implementation',
    receivesFrom: 'cicd-intelligent-recovery',
    memoryNamespaces: {
      specification: 'loop1/specification',
      research: 'loop1/research',
      planning: 'loop1/planning',
      execution: 'loop1/execution',
      output: 'integration/loop1-to-loop2',
      feedback: 'integration/loop3-feedback'
    }
  }
};

fs.writeFileSync(
  '.claude/.artifacts/loop1-planning-package.json',
  JSON.stringify(planningPackage, null, 2)
);

console.log('✅ Planning package created for Loop 2 integration');
console.log(`   Location: .claude/.artifacts/loop1-planning-package.json`);
console.log(`   Research sources: ${planningPackage.research.evidence_sources}`);
console.log(`   Tasks: ${planningPackage.planning.total_tasks}`);
console.log(`   Failure confidence: ${planningPackage.risk_analysis.final_failure_confidence}%`);
EOF
```

### Step 2: Store in Cross-Loop Memory

```bash
# Store for Loop 2 consumption
npx claude-flow@alpha memory store \
  "loop1_complete" \
  "$(cat .claude/.artifacts/loop1-planning-package.json)" \
  --namespace "integration/loop1-to-loop2"

# Tag for Loop 3 feedback integration
npx claude-flow@alpha memory store \
  "loop1_baseline" \
  "$(cat .claude/.artifacts/loop1-planning-package.json)" \
  --namespace "integration/loop3-feedback"

echo "✅ Planning package stored in cross-loop memory"
echo "   Namespace: integration/loop1-to-loop2"
```

### Step 3: Generate Loop 1 Report

Create human-readable summary:

```bash
cat > docs/loop1-report.md <<'EOF'
# Loop 1: Research-Driven Planning - Complete

## Specification Summary
$(head -20 SPEC.md | tail -15)

## Research Findings
- **Evidence Sources**: $(jq '.research.evidence_sources' .claude/.artifacts/loop1-planning-package.json) sources
- **Top Solution**: $(jq -r '.research.synthesis.recommendations[0].solution' .claude/.artifacts/loop1-planning-package.json)
- **Confidence Score**: $(jq '.research.confidence_score' .claude/.artifacts/loop1-planning-package.json)%

## Enhanced Plan
- **Total Tasks**: $(jq '.planning.total_tasks' .claude/.artifacts/loop1-planning-package.json) tasks
- **Estimated Complexity**: $(jq -r '.planning.estimated_complexity' .claude/.artifacts/loop1-planning-package.json)

## Risk Mitigation
- **Pre-mortem Iterations**: $(jq '.risk_analysis.premortem.iterations_completed' .claude/.artifacts/loop1-planning-package.json)
- **Final Failure Confidence**: $(jq '.risk_analysis.final_failure_confidence' .claude/.artifacts/loop1-planning-package.json)% (Target: <3%)
- **Critical Risks Mitigated**: $(jq '.risk_analysis.critical_risks_mitigated' .claude/.artifacts/loop1-planning-package.json)

## Ready for Loop 2
✅ Planning package: .claude/.artifacts/loop1-planning-package.json
✅ Memory namespace: integration/loop1-to-loop2
✅ Next: Execute parallel-swarm-implementation skill
EOF

echo "✅ Loop 1 report generated: docs/loop1-report.md"
```

**Validation Checkpoint**: Planning package must include all required fields and pass schema validation.

**Output**: Complete planning package ready for Loop 2 integration, stored in both filesystem and persistent memory



## Integration with Loop 3 (Feedback)

Loop 3 (CI/CD Intelligent Recovery) feeds failure analysis **back to Loop 1** for next iteration:

### Receiving Loop 3 Feedback

When Loop 3 completes, retrieve failure patterns:

```bash
npx claude-flow@alpha memory query "loop3_failure_patterns" \
  --namespace "integration/loop3-feedback"
```

### Incorporate into Next Pre-mortem

Use failure data to enhance future risk analysis:

```bash
# Next project's pre-mortem receives historical data
# The Realistic Failure Mode Analyst will automatically load this data
```

This creates **continuous improvement** where:
- Real failures inform future risk analysis
- Pre-mortem becomes more accurate over time
- Planning improves with each project cycle

-----|---------------------|--------------------------|
| Time | 2-4 hours | 6-11 hours |
| Research Sources | 0-2 | 10-30+ (6-agent parallel) |
| Risk Analysis | Ad-hoc | 5-iteration Byzantine consensus |
| Failure Prevention | 30-50% | 85-95% |
| ROI | 1x | 2-3x |



## Success Criteria

Loop 1 is successful when:
- ✅ SPEC.md captures all requirements completely
- ✅ Research provides evidence-based recommendations (≥3 sources per major decision)
- ✅ Research confidence score ≥70%
- ✅ Plan covers all SPEC.md requirements with task breakdown
- ✅ Pre-mortem achieves <3% failure confidence
- ✅ Byzantine consensus ≥66% agreement on all critical risks
- ✅ All critical risks have documented mitigation strategies with positive ROI
- ✅ Planning package successfully loads in Loop 2
- ✅ Memory namespaces populated with complete data

**Validation Command**:
```bash
npx claude-flow@alpha memory query "loop1_complete" \
  --namespace "integration/loop1-to-loop2" \
  --validate-schema
```

--------|---------|-----------|-----------|
| `loop1/specification` | SPEC.md and requirements | Specification phase | Loop 1, Loop 2 |
| `loop1/research` | Research findings and evidence | 6-agent research swarm | Loop 1, Loop 2 |
| `loop1/planning` | Enhanced plans and task breakdowns | Planning phase | Loop 2 |
| `loop1/execution` | Pre-mortem results and risk analysis | 8-agent pre-mortem swarm | Loop 2, Loop 3 |
| `integration/loop1-to-loop2` | Planning package for Loop 2 | Knowledge phase | Loop 2 |
| `integration/loop3-feedback` | Failure patterns from Loop 3 | Loop 3 | Loop 1 (next iteration) |



## Example: Complete Loop 1 Execution

### User Authentication System

```bash
# ===== PHASE 1: SPECIFICATION =====
cat > SPEC.md <<'EOF'
# User Authentication System

## Requirements
### Functional
- JWT-based authentication with refresh tokens
- Role-based access control (RBAC)
- Password reset functionality
- Two-factor authentication (TOTP)

### Non-Functional
- Performance: <100ms auth check
- Security: OWASP Top 10 compliance
- Scalability: 10,000 concurrent users

## Constraints
- Must integrate with existing Express.js API
- PostgreSQL database
- Deploy to AWS Lambda

## Success Criteria
1. 100% auth endpoint coverage
2. Zero critical vulnerabilities
3. <100ms 99th percentile latency
EOF

npx claude-flow@alpha memory store "project_spec" "$(cat SPEC.md)" --namespace "loop1/specification"

# ===== PHASE 2: RESEARCH (6-Agent Parallel) =====
# (Execute 6-agent research SOP as documented above)
# Results in .claude/.artifacts/research-synthesis.json

# ===== PHASE 3: PLANNING =====
/spec:plan
node scripts/enhance-plan-with-research.js

# ===== PHASE 4: EXECUTION (8-Agent × 5 Iterations Pre-mortem) =====
# (Execute 8-agent Byzantine consensus pre-mortem as documented above)
# Results in .claude/.artifacts/premortem-final.json

# ===== PHASE 5: KNOWLEDGE =====
node scripts/generate-planning-package.js

# ===== VERIFY SUCCESS =====
echo "✅ Loop 1 Complete"
echo "📊 Results:"
jq '{
  research_sources: .research.evidence_sources,
  tasks: .planning.total_tasks,
  failure_confidence: .risk_analysis.final_failure_confidence,
  ready: true
}' .claude/.artifacts/loop1-planning-package.json

echo ""
echo "➡️  Next: Execute parallel-swarm-implementation skill"
```

## Core Principles

### 1. Evidence-Based Planning Over Assumption-Based Design
Most project failures stem from untested assumptions made during planning. This skill replaces gut-feeling decisions with research-backed evidence from actual implementations, creating plans grounded in proven patterns rather than theoretical ideals.

**In practice:**
- Use 6-agent parallel research to gather 10-30+ credible sources for every major technical decision
- Require minimum 3 sources per architectural choice with explicit citations
- Cross-validate conflicting recommendations using self-consistency (multiple agents must agree)
- Document confidence scores for each decision (70%+ required to proceed)
- Store research findings in memory for future project reference and pattern building

### 2. Iterative Risk Mitigation Through Pre-Mortem Consensus
Catching problems before coding begins prevents 85-95% of implementation failures. Byzantine consensus with multiple failure analysis perspectives ensures comprehensive risk coverage that single-analyst approaches miss.

**In practice:**
- Run 5 pre-mortem iterations using 8 specialized agents (optimistic, pessimistic, realistic analysts)
- Require 2/3 Byzantine consensus agreement on risk severity classifications
- Continue iterations until <3% failure confidence is achieved or explain why threshold unreachable
- Use Root Cause Detective agents with 5-Whys and fishbone analysis to trace symptoms to actual causes
- Apply defense-in-depth mitigations with cost-benefit analysis (positive ROI required)

### 3. Continuous Learning Through Loop 3 Feedback Integration
Every project generates failure pattern data that should inform future planning. This skill closes the learning loop by incorporating actual production failures into future risk analysis, making pre-mortems progressively more accurate.

**In practice:**
- Store all Loop 3 failure patterns in integration/loop3-feedback memory namespace
- Load historical failure data into Realistic Failure Mode Analyst for next project's pre-mortem
- Track planning accuracy improvement over time (measure pre-mortem predictions vs actual failures)
- Use failure data to refine research queries (what types of sources predict actual problems?)
- Build organizational knowledge base of domain-specific failure modes

-----------|---------|----------|
| Skipping research phase for "familiar" technologies | Confidence bias leads to outdated patterns; miss recent security vulnerabilities or better approaches; reinvent solved problems | ALWAYS run research phase regardless of familiarity. Even well-known tech evolves (new best practices, security patches, performance optimizations). Set minimum research time (2 hours) as non-negotiable. |
| Converging pre-mortem too quickly (<3 iterations) | Early consensus often reflects groupthink rather than comprehensive analysis; miss non-obvious failure modes that emerge in later iterations | Require minimum 5 iterations regardless of early agreement. Track new risks discovered per iteration - if iteration 4-5 still finding critical risks, extend to 7-10 cycles. |
| Ignoring low-agreement risks in Byzantine consensus | Minority-flagged risks are often the most critical - they represent failure modes majority didn't consider; dismissing <66% agreement risks loses valuable edge-case coverage | Create separate "low-agreement high-severity" risk register. Investigate WHY agents disagree (different assumptions? missing info?). Require explicit mitigation or justification for dismissal. |

---

## Conclusion

Research-driven planning represents a fundamental shift from traditional software planning methodologies. Where conventional approaches rely on individual expertise and intuition, this skill orchestrates multi-agent research and consensus-driven risk analysis to achieve >97% planning accuracy. The 6-11 hour investment in comprehensive planning prevents 85-95% of potential failures, delivering 2-3x ROI through reduced rework and avoided dead ends.

The three-phase architecture (research, planning, execution) with Byzantine consensus ensures that plans are not only thorough but battle-tested against multiple analytical perspectives. The integration with Loop 3 creates a continuous improvement cycle where each project's actual failures refine future planning accuracy. This transforms planning from a one-time guess into an evolving, evidence-based discipline that becomes more effective with each iteration.

As software complexity increases and the cost of failed implementations rises, the value of rigorous upfront planning grows proportionally. Research-driven planning demonstrates that the apparent trade-off between planning speed and quality is false - by parallelizing research agents and automating pre-mortem analysis, this skill delivers both comprehensive planning and reasonable timelines. The result is a sustainable approach to complex project delivery that prevents problems rather than merely reacting to them.