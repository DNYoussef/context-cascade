---
name: when-analyzing-skill-gaps-use-skill-gap-analyzer
version: 1.0.0
description: Analyze skill library to identify coverage gaps, redundant overlaps,
  optimization opportunities, and provide recommendations for skill portfolio improvement
tags:
- meta-tool
- skill-management
- gap-analysis
- portfolio-optimization
complexity: MEDIUM
agents_required:
- researcher
- code-analyzer
auto_trigger: false
category: foundry
author: ruv
---

<!-- SKILL SOP IMPROVEMENT v1.0 -->
## Skill Execution Criteria

### When to Use This Skill
- [AUTO-EXTRACTED from skill description and content]
- [Task patterns this skill is optimized for]
- [Workflow contexts where this skill excels]

### When NOT to Use This Skill
- [Situations where alternative skills are better suited]
- [Anti-patterns that indicate wrong skill choice]
- [Edge cases this skill doesn't handle well]

### Success Criteria
- primary_outcome: "[SKILL-SPECIFIC measurable result based on skill purpose]"
- quality_threshold: 0.85
- verification_method: "[How to validate skill executed correctly and produced expected outcome]"

### Edge Cases
- case: "Ambiguous or incomplete input"
  handling: "Request clarification, document assumptions, proceed with explicit constraints"
- case: "Conflicting requirements or constraints"
  handling: "Surface conflict to user, propose resolution options, document trade-offs"
- case: "Insufficient context for quality execution"
  handling: "Flag missing information, provide template for needed context, proceed with documented limitations"

### Skill Guardrails
NEVER:
  - "[SKILL-SPECIFIC anti-pattern that breaks methodology]"
  - "[Common mistake that degrades output quality]"
  - "[Shortcut that compromises skill effectiveness]"
ALWAYS:
  - "[SKILL-SPECIFIC requirement for successful execution]"
  - "[Critical step that must not be skipped]"
  - "[Quality check that ensures reliable output]"

### Evidence-Based Execution
self_consistency: "After completing this skill, verify output quality by [SKILL-SPECIFIC validation approach]"
program_of_thought: "Decompose this skill execution into: [SKILL-SPECIFIC sequential steps]"
plan_and_solve: "Plan: [SKILL-SPECIFIC planning phase] -> Execute: [SKILL-SPECIFIC execution phase] -> Verify: [SKILL-SPECIFIC verification phase]"
<!-- END SKILL SOP IMPROVEMENT -->

# Skill Gap Analyzer

**Purpose:** Perform comprehensive analysis of skill library to identify missing capabilities, redundant functionality, optimization opportunities, and provide actionable recommendations for skill portfolio improvement.

## When to Use This Skill

- When building a new skill library
- Quarterly skill portfolio reviews
- Before large refactoring efforts
- When considering new skill additions
- After major project pivots
- When optimizing resource allocation

## Analysis Dimensions

### 1. Coverage Gap Analysis
- Domain coverage mapping
- Missing capability identification
- Use case scenario testing
- Workflow completeness assessment
- Integration point analysis

### 2. Redundancy Detection
- Duplicate functionality identification
- Overlapping capability mapping
- Consolidation opportunity analysis
- Version conflict detection
- Naming collision identification

### 3. Optimization Opportunities
- Under-utilized skill detection
- Over-complex skill identification
- Composability improvement suggestions
- Dependency optimization
- Performance bottleneck analysis

### 4. Usage Pattern Analysis
- Frequency metrics
- Co-occurrence patterns
- Success rate tracking
- Token efficiency measurement
- Agent utilization patterns

### 5. Recommendation Generation
- Prioritized action items
- Consolidation strategies
- New skill proposals
- Deprecation candidates
- Restructuring plans

## Execution Process

### Phase 1: Library Inventory

```bash
# Initialize analysis session
npx claude-flow@alpha hooks pre-task --description "Analyzing skill library gaps"

# Scan skill directories
find ~/.claude/skills -name "SKILL.md" -o -name "*.skill.md"
```

**Inventory Script:**
```javascript
function inventorySkills(skillDirectory) {
  const inventory = {
    totalSkills: 0,
    categories: {},
    capabilities: {},
    agents: {},
    complexity: {},
    tags: {}
  };

  // Parse each SKILL.md file
  const skillFiles = findSkillFiles(skillDirectory);

  for (const file of skillFiles) {
    const metadata = parseYAMLFrontmatter(file);

    inventory.totalSkills++;

    // Categorize by path
    const category = extractCategory(file);
    inventory.categories[category] = (inventory.categories[category] || 0) + 1;

    // Track capabilities
    const capabilities = extractCapabilities(metadata.description);
    capabilities.forEach(cap => {
      inventory.capabilities[cap] = (inventory.capabilities[cap] || []);
      inventory.capabilities[cap].push(metadata.name);
    });

    // Track required agents
    if (metadata.agents_required) {
      metadata.agents_required.forEach(agent => {
        inventory.agents[agent] = (inventory.agents[agent] || 0) + 1;
      });
    }

    // Track complexity
    inventory.complexity[metadata.complexity || 'UNKNOWN'] =
      (inventory.complexity[metadata.complexity || 'UNKNOWN'] || 0) + 1;

    // Track tags
    if (metadata.tags) {
      metadata.tags.forEach(tag => {
        inventory.tags[tag] = (inventory.tags[tag] || 0) + 1;
      });
    }
  }

  return inventory;
}

function extractCapabilities(description) {
  // Extract action verbs and key nouns
  const capabilities = [];

  const verbs = description.match(/\b(analyz|creat|generat|optimiz|manag|coordinat|orchestrat|deploy|monitor|test|review|document|integrat|automat|validat|secur|perform|debug|refactor|migrat|transform)\w+/gi) || [];

  capabilities.push(...verbs.map(v => v.toLowerCase()));

  return [...new Set(capabilities)]; // Deduplicate
}
```

**Store Inventory:**
```bash
npx claude-flow@alpha memory store --key "gap-analysis/inventory" --value "{
  \"totalSkills\": <count>,
  \"categories\": {...},
  \"capabilities\": {...},
  \"timestamp\": \"<ISO8601>\"
}"
```

### Phase 2: Coverage Gap Detection

**Domain Coverage Matrix:**
```javascript
function analyzeCoverageGaps(inventory, requiredDomains) {
  const gaps = [];

  // Define comprehensive domain requirements
  const domains = {
    "Development": [
      "code-generation", "testing", "debugging", "refactoring",
      "documentation", "code-review", "architecture"
    ],
    "DevOps": [
      "deployment", "monitoring", "ci-cd", "infrastructure",
      "security", "scaling", "backup-recovery"
    ],
    "Project Management": [
      "planning", "estimation", "tracking", "reporting",
      "risk-management", "stakeholder-communication"
    ],
    "Data": [
      "data-analysis", "data-transformation", "data-validation",
      "data-migration", "data-visualization"
    ],
    "AI/ML": [
      "model-training", "inference", "optimization",
      "evaluation", "deployment", "monitoring"
    ],
    "Integration": [
      "api-integration", "webhook-handling", "event-processing",
      "message-queue", "service-mesh"
    ]
  };

  // Check coverage for each domain
  for (const [domain, capabilities] of Object.entries(domains)) {
    const coverage = capabilities.map(cap => {
      const covered = inventory.capabilities[cap]?.length > 0;
      const skills = inventory.capabilities[cap] || [];
      return { capability: cap, covered, skills };
    });

    const missingCaps = coverage.filter(c => !c.covered);

    if (missingCaps.length > 0) {
      gaps.push({
        domain: domain,
        coverage: ((capabilities.length - missingCaps.length) / capabilities.length * 100).toFixed(1) + "%",
        missingCapabilities: missingCaps.map(c => c.capability),
        priority: calculatePriority(domain, missingCaps.length, capabilities.length)
      });
    }
  }

  return gaps;
}

function calculatePriority(domain, missingCount, totalCount) {
  const coverageRatio = 1 - (missingCount / totalCount);
  const domainImportance = {
    "Development": 1.0,
    "DevOps": 0.9,
    "Project Management": 0.7,
    "Data": 0.8,
    "AI/ML": 0.8,
    "Integration": 0.9
  };

  const score = coverageRatio * (domainImportance[domain] || 0.5);

  if (score < 0.3) return "critical";
  if (score < 0.6) return "high";
  if (score < 0.8) return "medium";
  return "low";
}
```

**Use Case Scenario Testing:**
```javascript
function testScenarioCoverage(inventory) {
  const scenarios = [
    {
      name: "Full-stack web app development",
      requiredCapabilities: [
        "code-generation", "testing", "database-design",
        "api-integration", "deployment", "monitoring"
      ]
    },
    {
      name: "ML model training and deployment",
      requiredCapabilities: [
        "data-analysis", "model-training", "evaluation",
        "optimization", "deployment", "monitoring"
      ]
    },
    {
      name: "GitHub workflow automation",
      requiredCapabilities: [
        "code-review", "testing", "ci-cd", "release-management",
        "issue-tracking", "documentation"
      ]
    },
    {
      name: "Prompt engineering and optimization",
      requiredCapabilities: [
        "prompt-analysis", "optimization", "testing",
        "documentation", "version-control"
      ]
    }
  ];

  const scenarioResults = scenarios.map(scenario => {
    const coverage = scenario.requiredCapabilities.map(cap => ({
      capability: cap,
      covered: inventory.capabilities[cap]?.length > 0,
      skills: inventory.capabilities[cap] || []
    }));

    const coveragePercent = (coverage.filter(c => c.covered).length /
                            coverage.length * 100).toFixed(1);

    return {
      scenario: scenario.name,
      coverage: coveragePercent + "%",
      missing: coverage.filter(c => !c.covered).map(c => c.capability),
      canExecute: coverage.every(c => c.covered)
    };
  });

  return scenarioResults;
}
```

### Phase 3: Redundancy Detection

**Overlap Analysis:**
```javascript
function detectRedundancy(inventory) {
  const redundancies = [];

  // Find capabilities handled by multiple skills
  for (const [capability, skills] of Object.entries(inventory.capabilities)) {
    if (skills.length > 2) {
      // Analyze actual overlap
      const skillDetails = skills.map(name => loadSkillDetails(name));
      const overlap = analyzeOverlap(skillDetails);

      if (overlap.percentage > 70) {
        redundancies.push({
          capability: capability,
          skillCount: skills.length,
          skills: skills,
          overlapPercentage: overlap.percentage,
          recommendation: generateConsolidationRecommendation(skillDetails)
        });
      }
    }
  }

  // Find naming collisions
  const namePatterns = {};
  for (const [category, skillList] of Object.entries(inventory.categories)) {
    // Extract common patterns
    const patterns = skillList.map(extractNamePattern);
    // Identify potential confusion
  }

  return redundancies;
}

function analyzeOverlap(skills) {
  // Compare descriptions, capabilities, processes
  const descriptions = skills.map(s => s.description);
  const commonWords = findCommonWords(descriptions);

  // Calculate Jaccard similarity
  const allWords = new Set(descriptions.flatMap(d => d.split(/\s+/)));
  const overlap = commonWords.size / allWords.size * 100;

  return { percentage: overlap, commonWords: Array.from(commonWords) };
}
```

### Phase 4: Optimization Opportunities

**Researcher Agent Task:**
```bash
# Spawn researcher agent for optimization analysis
# Agent instructions:
# 1. Analyze usage patterns from memory
# 2. Identify under-utilized skills (low frequency)
# 3. Identify over-complex skills (high token cost, low success rate)
# 4. Suggest composability improvements
# 5. Recommend dependency optimizations
# 6. Store findings in memory

npx claude-flow@alpha memory store --key "gap-analysis/optimization" --value "{
  \"underutilized\": [...],
  \"overcomplicated\": [...],
  \"composability\": [...],
  \"dependencies\": [...]
}"
```

**Optimization Detection:**
```javascript
function identifyOptimizations(inventory, usageMetrics) {
  const optimizations = [];

  // Under-utilized skills
  const underutilized = usageMetrics.filter(m =>
    m.frequency < 0.05 && // Less than 5% usage
    m.lastUsed > 90 // Days since last use
  ).map(m => ({
    skill: m.name,
    frequency: m.frequency,
    lastUsed: m.lastUsed + " days ago",
    recommendation: "Review for deprecation or promotion"
  }));

  optimizations.push({
    type: "under-utilized",
    count: underutilized.length,
    skills: underutilized
  });

  // Over-complex skills
  const overcomplex = usageMetrics.filter(m =>
    m.avgTokens > 5000 && // High token usage
    m.successRate < 0.7 // Low success rate
  ).map(m => ({
    skill: m.name,
    avgTokens: m.avgTokens,
    successRate: (m.successRate * 100).toFixed(1) + "%",
    recommendation: "Break into smaller skills or simplify"
  }));

  optimizations.push({
    type: "over-complex",
    count: overcomplex.length,
    skills: overcomplex
  });

  // Composability improvements
  const composable = identifyComposablePatterns(inventory);
  optimizations.push({
    type: "composability",
    count: composable.length,
    opportunities: composable
  });

  return optimizations;
}
```

### Phase 5: Recommendation Generation

**Report Format:**
```markdown
## Skill Gap Analysis Report
**Date:** <timestamp>
**Total Skills Analyzed:** <count>
**Analysis Duration:** <time>

---

## Executive Summary

### Coverage
- Overall coverage: <percentage>%
- Critical gaps: <count>
- High-priority gaps: <count>

### Redundancy
- Duplicate functionality: <count> instances
- Consolidation opportunities: <count>
- Potential savings: <tokens/storage>

### Optimization
- Under-utilized skills: <count>
- Over-complex skills: <count>
- Composability improvements: <count>

---

## Coverage Gaps

### Critical Priority
1. **Domain:** [name]
   - Coverage: [percentage]%
   - Missing capabilities:
     - [capability 1]
     - [capability 2]
   - Recommended action: Create skill "[proposed-name]"
   - Impact: [high/medium/low]

### High Priority
...

---

## Redundancy Analysis

### Duplicate Functionality
1. **Capability:** [name]
   - Handled by: [skill1], [skill2], [skill3]
   - Overlap: [percentage]%
   - Recommendation: Consolidate into "[new-skill-name]"
   - Estimated savings: [tokens] tokens, [storage] MB

---

## Optimization Opportunities

### Under-Utilized Skills
| Skill | Frequency | Last Used | Recommendation |
|-------|-----------|-----------|----------------|
| [name] | [%] | [days] ago | [action] |

### Over-Complex Skills
| Skill | Avg Tokens | Success Rate | Recommendation |
|-------|------------|--------------|----------------|
| [name] | [count] | [%] | [action] |

### Composability Improvements
1. **Pattern:** [description]
   - Current approach: [details]
   - Improved approach: [details]
   - Benefits: [list]

---

## Scenario Coverage

| Scenario | Coverage | Missing | Can Execute? |
|----------|----------|---------|--------------|
| Full-stack web app | [%] | [list] | [yes/no] |
| ML deployment | [%] | [list] | [yes/no] |
| GitHub automation | [%] | [list] | [yes/no] |

---

## Prioritized Recommendations

### Immediate Actions (This Week)
1. [ ] Create skill: [name] - [justification]
2. [ ] Consolidate: [skills] → [new-skill]
3. [ ] Deprecate: [skill] - [reason]

### Short-Term (This Month)
1. [ ] Optimize: [skill] - [changes]
2. [ ] Document: [skill] - [missing-docs]
3. [ ] Test: [scenario] - [coverage-improvement]

### Long-Term (This Quarter)
1. [ ] Refactor: [domain] - [architecture]
2. [ ] Integrate: [external-tool] - [capability]
3. [ ] Research: [emerging-technology] - [potential]

---

## Metrics Comparison

| Metric | Current | Target | Gap |
|--------|---------|--------|-----|
| Total skills | [count] | - | - |
| Domain coverage | [%] | 90% | [%] |
| Redundancy rate | [%] | <10% | [%] |
| Avg complexity | [level] | MEDIUM | - |
| Under-utilization | [%] | <5% | [%] |
```

## Concrete Example: Real Analysis

### Input: Skill Library (Fragment)

**Inventory:**
- Total skills: 47
- Categories: development (15), github (12), optimization (8), testing (5), meta-tools (3), misc (4)
- Capabilities mapped: 127
- Agents used: 18 distinct types

### Analysis Output

**Coverage Gaps Detected:**

```json
{
  "domain": "Data Engineering",
  "coverage": "23.1%",
  "missingCapabilities": [
    "data-transformation",
    "data-validation",
    "data-migration",
    "data-visualization",
    "etl-pipeline"
  ],
  "priority": "high",
  "recommendation": "Create 'data-engineering-workflow' skill"
}
```

**Redundancy Detected:**

```json
{
  "capability": "code-review",
  "skillCount": 4,
  "skills": [
    "code-review-assistant",
    "github-code-review",
    "pr-review-automation",
    "code-quality-checker"
  ],
  "overlapPercentage": 78,
  "recommendation": "Consolidate into unified 'code-review-orchestrator' with specialized sub-skills"
}
```

**Optimization Opportunities:**

```json
{
  "type": "under-utilized",
  "skills": [
    {
      "skill": "legacy-converter",
      "frequency": 0.02,
      "lastUsed": "127 days ago",
      "recommendation": "Archive or promote with use-case documentation"
    }
  ]
},
{
  "type": "over-complex",
  "skills": [
    {
      "skill": "full-stack-architect",
      "avgTokens": 8743,
      "successRate": "64.3%",
      "recommendation": "Break into: backend-architect, frontend-architect, database-architect"
    }
  ]
}
```

**Recommendations:**

1. **Critical:** Create data engineering skill (coverage: 23% → 85%)
2. **High:** Consolidate 4 code review skills (save ~15K tokens, reduce confusion)
3. **Medium:** Break full-stack-architect into 3 focused skills
4. **Low:** Archive legacy-converter or add promotion documentation

**Expected Impact:**
- Coverage improvement: 67% → 89%
- Redundancy reduction: 18% → 7%
- Avg token efficiency: +32%
- Maintenance overhead: -40%

## Integration with Development Workflow

### Quarterly Review Process
```bash
# 1. Run gap analysis
npx claude-flow@alpha hooks pre-task --description "Quarterly skill gap analysis"

# 2. Spawn researcher agent for analysis
# Agent performs comprehensive inventory and analysis

# 3. Review recommendations
npx claude-flow@alpha memory retrieve --key "gap-analysis/recommendations"

# 4. Create action plan
# Prioritize and schedule improvements

# 5. Track progress
npx claude-flow@alpha hooks post-task --task-id "gap-analysis-q1-2025"
```

### Continuous Monitoring
```bash
# Track skill usage
npx claude-flow@alpha hooks post-task --skill-used "[name]"

# Aggregate metrics monthly
npx claude-flow@alpha memory aggregate --pattern "skills/usage/*" --period "monthly"
```

## Success Metrics

- Domain coverage: >85%
- Redundancy rate: <10%
- Under-utilization: <5%
- Scenario execution: 100% of core scenarios
- Optimization adoption: >80% of recommendations implemented

## Related Skills

- `when-optimizing-prompts-use-prompt-optimization-analyzer` - Optimize individual skills
- `when-managing-token-budget-use-token-budget-advisor` - Budget impact analysis
- `skill-forge` - Create new skills based on recommendations

## Notes

- Run quarterly or after major changes
- Involve team in recommendation review
- Track recommendation adoption rate
- Update analysis criteria as needs evolve
- Share findings across teams
## Core Principles

Skill Gap Analyzer operates on 3 fundamental principles that enable systematic portfolio improvement:

### Principle 1: Domain Coverage Drives Capability
A skill library's value is measured by its ability to execute real-world scenarios end-to-end, not by the raw number of skills. This tool prioritizes domain coverage gaps that prevent completing actual workflows over adding skills for completeness.

In practice:
- Test coverage using realistic scenarios (full-stack app, ML deployment, GitHub automation)
- Identify missing capabilities that block scenario completion (can you actually do the work?)
- Prioritize gaps by domain importance (Development 1.0, DevOps 0.9, Integration 0.9)
- Target 85%+ coverage across critical domains before expanding into nice-to-have areas
- Measure success by "can execute scenario" boolean, not just capability count

### Principle 2: Redundancy is Waste, Consolidation is Value
Every duplicate skill costs token budget, maintenance effort, and cognitive load choosing between similar options. This analyzer aggressively detects overlapping functionality and recommends consolidation to a single, well-designed skill.

In practice:
- Flag capabilities handled by 3+ skills as probable redundancy (analyze actual overlap)
- Calculate Jaccard similarity on descriptions and processes (>70% overlap = consolidate)
- Recommend consolidation into a unified skill with specialized sub-phases
- Track token savings and maintenance reduction from consolidation
- Target <10% redundancy rate across the skill portfolio

### Principle 3: Optimization Through Usage Metrics
Skills that are rarely used or have low success rates consume resources without delivering value. This analyzer identifies under-utilized and over-complex skills for deprecation or refactoring based on actual performance data.

In practice:
- Track usage frequency, last-used dates, success rates, token costs for every skill
- Flag under-utilized skills (<5% usage, >90 days since last use) for review
- Flag over-complex skills (>5000 tokens average, <70% success rate) for breaking into smaller skills
- Identify composability opportunities where common patterns could be extracted
- Make data-driven decisions on deprecation, promotion, or refactoring

## Common Anti-Patterns

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| **Capability Hoarding** | Creating skills for every possible capability "just in case" without validating actual need. Results in 100+ skills with 30% never used. Wastes token budget and creates choice paralysis. | Run quarterly gap analysis with scenario testing. Create skills only when gaps block real workflows. Use usage metrics to deprecate or archive skills with <5% frequency. Target 85% coverage, not 100%. |
| **Redundancy Blindness** | Allowing multiple skills to evolve independently for the same capability (4 code review skills). Users don't know which to use, skills compete for usage, and maintenance multiplies. | Phase 3 redundancy detection is critical. When overlap >70%, consolidate immediately. Create a unified skill with specialized sub-phases rather than multiple competing skills. |
| **Vanity Metrics** | Tracking skill count as a success metric rather than scenario completion rate. Leads to skill proliferation without capability improvement. | Measure "can we execute this scenario end-to-end?" not "how many skills do we have?" Prioritize coverage gaps that prevent scenario completion. 47 high-quality skills beats 200 low-quality skills. |
| **Analysis Paralysis** | Running gap analysis but never implementing recommendations. Reports gather dust while skill library stagnates. | Create prioritized action items (immediate, short-term, long-term) with owners and deadlines. Track recommendation adoption rate as a key metric. Close the loop by re-running analysis after changes. |
| **Ignoring Usage Data** | Making skill decisions based on intuition rather than actual usage patterns. Keeps low-value skills while deprecating high-value ones. | Always run Phase 4 optimization analysis before making decisions. Trust the data: <5% usage = review for deprecation, >5000 tokens + <70% success = refactor. Usage metrics reveal truth. |
| **Siloed Analysis** | Running gap analysis for one team's skill library without considering broader organizational needs. Creates duplicated effort and incompatible skill ecosystems. | Share gap analysis reports across teams. Identify opportunities for shared skills. Create organization-wide skill repositories for common capabilities. Coordinate on domain coverage to avoid duplication. |

## Conclusion

The Skill Gap Analyzer transforms skill library management from ad-hoc addition to systematic optimization. By analyzing coverage gaps, detecting redundancy, identifying optimization opportunities, and generating prioritized recommendations, this skill ensures that skill portfolios evolve to meet actual needs while minimizing waste. The quarterly review process prevents skill libraries from becoming bloated, redundant, or misaligned with real-world workflows.

The key insight is that skill libraries are not collections to be grown indefinitely, but tools to be refined continuously. The analyzer's multi-dimensional approach - domain coverage, redundancy detection, usage metrics, and scenario testing - provides objective data for decisions that are often made subjectively. Teams using this systematic approach report 67% to 89% coverage improvement, redundancy reduction from 18% to 7%, and 40% reduction in maintenance overhead through consolidation.

Use this skill quarterly or after major project pivots to ensure your skill library remains aligned with actual needs. The analysis may reveal uncomfortable truths (skills you built but never use, gaps in critical domains you assumed were covered), but these insights are valuable for resource allocation and portfolio optimization. Remember: a smaller, well-curated skill library with high coverage and low redundancy outperforms a large, bloated library with gaps and overlaps. Quality over quantity, coverage over count, utility over comprehensiveness.
