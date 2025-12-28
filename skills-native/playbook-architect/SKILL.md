---
name: playbook-architect
description: Comprehensive framework for creating, analyzing, and optimizing playbooks
  that orchestrate skill sequences. Use when creating new playbooks, improving existing
  playbook workflows, or applying evidence-based orchestration patterns. Applies
  7-dimensional playbook analysis, dependency optimization, and parallelization strategies
  to transform playbooks into highly effective orchestration sequences.
version: 1.0.0
category: foundry
tags:
- foundry
- creation
- meta-tools
- orchestration
author: ruv
---

<!-- SKILL SOP IMPROVEMENT v1.0 -->
## Skill Execution Criteria

### When to Use This Skill
- Creating new playbooks for recurring workflow patterns
- Improving existing playbooks with inconsistent or suboptimal routing
- Building playbook libraries for team standardization
- Optimizing high-stakes workflows where execution order impacts outcomes
- Debugging why playbooks aren't producing expected results
- Adding new categories of playbooks (gap analysis)
- Consolidating overlapping playbooks

### When NOT to Use This Skill
- For single-skill invocations (use skill directly)
- When existing playbook already covers the workflow optimally
- For one-off tasks without reuse value
- When task is purely conversational without orchestration needs

### Success Criteria
- primary_outcome: "Optimized playbook with clear trigger conditions, correct skill sequencing, proper dependency handling, and maximized parallelization"
- quality_threshold: 0.92
- verification_method: "Playbook executes successfully across diverse test cases, routes correctly based on intent keywords, and achieves stated success metrics"

### Edge Cases
- case: "Overlapping trigger keywords with existing playbooks"
  handling: "Apply MECE analysis to disambiguate, add priority weights or more specific keywords"
- case: "Circular dependencies between skills in sequence"
  handling: "Detect cycles, restructure into DAG (Directed Acyclic Graph), split if necessary"
- case: "Missing MCP requirements for skill execution"
  handling: "Add mcp_requirements section, validate MCPs are available before routing"

### Skill Guardrails
NEVER:
  - "Create playbooks without validating skill availability (skills must exist in registry)"
  - "Sequence skills with unmet dependencies (prerequisites must complete before dependents)"
  - "Skip parallelization analysis (concurrent execution is 2-8x faster)"
  - "Duplicate existing playbooks without clear differentiation"
  - "Create playbooks with vague trigger conditions (keywords must be specific)"
ALWAYS:
  - "Validate all skills in sequence exist in skills/ directory"
  - "Apply dependency analysis to identify sequential vs parallel phases"
  - "Include success criteria with measurable metrics"
  - "Document MCP requirements for each playbook"
  - "Add fallback skills for critical steps"

### Evidence-Based Execution
self_consistency: "After playbook creation, trace execution path with multiple test intents to verify consistent routing and skill activation"
program_of_thought: "Decompose playbook design into: 1) Intent analysis, 2) Skill mapping, 3) Dependency detection, 4) Parallelization optimization, 5) MCP requirements, 6) Success criteria definition"
plan_and_solve: "Plan: Analyze workflow requirements -> Execute: Design skill sequence with dependencies -> Verify: Test with diverse trigger conditions + edge cases"
<!-- END SKILL SOP IMPROVEMENT -->

# Playbook Architect - META-PLAYBOOK Creation Framework

A comprehensive framework for creating, analyzing, and optimizing playbooks that orchestrate skill sequences. This skill applies the same evidence-based methodology used in prompt-architect and agent-creator to the playbook layer of the system.

## Overview

Playbooks are **orchestrated sequences of skills** that execute in response to specific user intents. Unlike individual skills (which do ONE thing well), playbooks coordinate MULTIPLE skills to accomplish complex workflows.

The Playbook Architect provides systematic methods to:
- Create new playbooks with proper structure and routing
- Analyze existing playbooks for optimization opportunities
- Apply evidence-based orchestration patterns
- Maximize parallelization while respecting dependencies
- Ensure MECE (Mutually Exclusive, Collectively Exhaustive) coverage

## The Playbook Hierarchy

```
USER INTENT
    |
    v
PLAYBOOK (orchestration layer)
    |
    +-- Skill 1 (intent-analyzer) -- ALWAYS FIRST
    |       |
    |       +-- Agent(s) spawned by skill
    |
    +-- Skill 2 (prompt-architect) -- ALWAYS SECOND
    |       |
    |       +-- Agent(s) spawned by skill
    |
    +-- Skill 3-N (domain-specific)
    |       |
    |       +-- Agent(s) spawned by skill
    |
    +-- Skill N+1 (validation) -- ALWAYS LAST
            |
            +-- Agent(s) spawned by skill
```

## 7-Dimensional Playbook Analysis Framework

When analyzing or creating playbooks, evaluate across these dimensions:

### 1. Intent Mapping Assessment
- Are trigger keywords specific and unambiguous?
- Do triggers overlap with other playbooks (violating MECE)?
- Are negative triggers defined (when NOT to use)?
- Is intent coverage complete for the domain?

**Strong playbooks** have specific trigger conditions that clearly distinguish them from alternatives.

### 2. Skill Sequence Validation
- Do all skills in the sequence exist in the registry?
- Is the sequence order logically correct?
- Are there missing skills that should be included?
- Are there redundant skills that could be removed?

**Effective sequences** include exactly the skills needed, no more, no less.

### 3. Dependency Analysis
- Which skills depend on outputs from previous skills?
- Which skills are independent and can run in parallel?
- Are there circular dependencies (error condition)?
- Is the critical path optimized for speed?

**Optimized playbooks** maximize parallelization while respecting true dependencies.

### 4. MCP Requirements Evaluation
- What MCPs are required for each skill in the sequence?
- Are MCPs correctly specified in the playbook?
- What happens if required MCPs are unavailable?
- Are there fallback MCPs or skills?

**Robust playbooks** declare MCP requirements and handle unavailability gracefully.

### 5. Success Criteria Definition
- Are success metrics explicitly defined?
- Are metrics measurable and verifiable?
- Is there a clear "definition of done"?
- Are partial success scenarios handled?

**Production-ready playbooks** have explicit, measurable success criteria.

### 6. Failure Mode Detection
- What can go wrong in each phase?
- Are there fallback skills for critical steps?
- Is escalation path defined for unrecoverable failures?
- Are retry strategies appropriate?

**Resilient playbooks** anticipate failures and have recovery strategies.

### 7. Complexity and Timing Assessment
- Is complexity rating accurate (Low/Medium/High/Very High)?
- Are time estimates realistic?
- Is the playbook appropriately scoped?
- Should it be split into smaller playbooks?

**Well-scoped playbooks** are neither too simple nor too complex for their purpose.

## Playbook Creation Methodology (4-Phase SOP)

### Phase 1: Workflow Analysis (15-30 minutes)

**Objective**: Understand the workflow being orchestrated.

**Activities**:
1. **Intent Definition**
   - What user goals trigger this playbook?
   - What keywords indicate this workflow?
   - What distinguishes this from similar workflows?

2. **Skill Inventory**
   - What skills are needed to accomplish the goal?
   - What order must they execute?
   - What are the inputs/outputs of each skill?

3. **Dependency Mapping**
   - Which skills depend on which?
   - Which can run in parallel?
   - What is the critical path?

**Validation Gate**:
- [ ] Trigger keywords are specific and unique
- [ ] All required skills exist in registry
- [ ] Dependencies are clearly identified
- [ ] No circular dependencies exist

**Outputs**:
- Intent definition document
- Skill sequence diagram
- Dependency graph

---

### Phase 2: Playbook Architecture (20-30 minutes)

**Objective**: Design the playbook structure.

**Activities**:
1. **Sequence Design**
   ```yaml
   playbook: [playbook-name]
   version: 1.0.0

   triggers:
     keywords: [list of trigger keywords]
     patterns: [regex patterns]
     negative: [keywords that exclude this playbook]

   phases:
     - name: "Phase 1: [Name]"
       type: sequential
       skills:
         - skill: intent-analyzer
           purpose: "Analyze user intent"
           output: intent_analysis
         - skill: prompt-architect
           purpose: "Optimize request"
           input: intent_analysis
           output: optimized_request

     - name: "Phase 2: [Name]"
       type: parallel
       prerequisites: [Phase 1]
       skills:
         - skill: [skill-1]
           purpose: "[Purpose]"
           agent: [agent-name]
         - skill: [skill-2]
           purpose: "[Purpose]"
           agent: [agent-name]

     - name: "Phase 3: [Name]"
       type: sequential
       prerequisites: [Phase 2]
       skills:
         - skill: [validation-skill]
           purpose: "Validate output"
   ```

2. **Parallelization Strategy**
   - Group independent skills into parallel phases
   - Ensure prerequisites complete before dependents
   - Calculate expected time savings

3. **MCP Configuration**
   ```yaml
   mcp_requirements:
     required: [memory-mcp, sequential-thinking]
     optional: [playwright, ruv-swarm]
     fallbacks:
       playwright: manual-testing-skill
   ```

**Validation Gate**:
- [ ] Structure follows standard template
- [ ] Parallel phases are correctly grouped
- [ ] MCP requirements are complete
- [ ] Fallbacks are defined for critical skills

**Outputs**:
- Playbook YAML/Markdown structure
- Parallelization diagram
- MCP dependency matrix

---

### Phase 3: Success Criteria and Guardrails (15-20 minutes)

**Objective**: Define what success looks like and what to avoid.

**Activities**:
1. **Success Metrics**
   ```yaml
   success_criteria:
     primary_metric: "[What defines success]"
     secondary_metrics:
       - execution_time: "<[time]"
       - quality_score: ">[threshold]"
       - test_coverage: ">[percentage]"

     acceptance_gates:
       - "[Gate 1]: [Condition]"
       - "[Gate 2]: [Condition]"

   definition_of_done:
     - "[Criterion 1]"
     - "[Criterion 2]"
     - "[Criterion 3]"
   ```

2. **Guardrails Definition**
   ```yaml
   guardrails:
     NEVER:
       - "[Anti-pattern 1 with rationale]"
       - "[Anti-pattern 2 with rationale]"
     ALWAYS:
       - "[Required behavior 1]"
       - "[Required behavior 2]"

   failure_modes:
     - trigger: "[Condition]"
       action: "[Recovery step]"
       escalate_to: "[human/agent]"
   ```

3. **Edge Case Handling**
   ```yaml
   edge_cases:
     - case: "[Edge case 1]"
       detection: "[How to detect]"
       handling: "[What to do]"
     - case: "[Edge case 2]"
       detection: "[How to detect]"
       handling: "[What to do]"
   ```

**Validation Gate**:
- [ ] Success criteria are measurable
- [ ] Guardrails are actionable
- [ ] Edge cases are comprehensive
- [ ] Failure modes have recovery strategies

**Outputs**:
- Success criteria document
- Guardrails specification
- Edge case inventory

---

### Phase 4: Integration and Testing (20-30 minutes)

**Objective**: Validate playbook works in practice.

**Activities**:
1. **Trigger Testing**
   - Test with various phrasings of target intent
   - Verify correct routing vs. similar playbooks
   - Test negative triggers (should NOT activate)

2. **Execution Testing**
   - Run playbook end-to-end
   - Verify skill sequence executes correctly
   - Measure actual vs. estimated time
   - Validate parallel phases run concurrently

3. **Failure Injection**
   - Simulate skill failures
   - Verify fallbacks activate
   - Test recovery strategies
   - Confirm escalation works

4. **Documentation**
   - Add to playbook quick reference
   - Update MECE coverage matrix
   - Document any gaps identified

**Validation Gate**:
- [ ] Triggers route correctly 95%+ of time
- [ ] Full execution completes successfully
- [ ] Failure recovery works as expected
- [ ] Documentation is complete

**Outputs**:
- Test results report
- Performance metrics
- Updated playbook documentation

---

## Playbook Categories and Patterns

### Delivery Playbooks
**Purpose**: Ship features and functionality
**Common Skills**: sparc-methodology, feature-dev-complete, smart-bug-fix
**Pattern**: Research -> Plan -> Implement -> Test -> Deploy

### Research Playbooks
**Purpose**: Investigate and analyze
**Common Skills**: deep-research-orchestrator, literature-synthesis, gemini-search
**Pattern**: Question -> Search -> Synthesize -> Validate -> Report

### Operations Playbooks
**Purpose**: Infrastructure and deployment
**Common Skills**: cicd-intelligent-recovery, deployment-readiness, kubernetes-specialist
**Pattern**: Prepare -> Deploy -> Validate -> Monitor -> Recover

### Quality Playbooks
**Purpose**: Audit and improve code quality
**Common Skills**: clarity-linter, code-review-assistant, theater-detection-audit
**Pattern**: Collect -> Analyze -> Report -> Fix -> Verify

### Security Playbooks
**Purpose**: Security analysis and hardening
**Common Skills**: reverse-engineering-quick-triage, compliance, security-audit
**Pattern**: Assess -> Scan -> Analyze -> Remediate -> Validate

---

## Playbook Optimization Strategies

### 1. Parallelization Maximization
- Identify skills without dependencies
- Group into parallel execution phases
- Expected speedup: 2-8x depending on skill count

### 2. Critical Path Optimization
- Identify longest dependency chain
- Look for opportunities to parallelize parts
- Consider skill substitution for faster alternatives

### 3. Skill Consolidation
- Combine related skills when possible
- Remove redundant validation steps
- Streamline handoffs between skills

### 4. Failure Resilience
- Add fallback skills for critical steps
- Implement retry with exponential backoff
- Define clear escalation paths

### 5. MCP Efficiency
- Use Core MCPs by default (lowest token cost)
- Load situational MCPs only when needed
- Batch MCP operations where possible

---

## Playbook Improvement Template

When improving existing playbooks, apply this template:

```markdown
## Playbook: [Name]

### Trigger Conditions
**When to Use**:
- [Specific trigger 1]
- [Specific trigger 2]

**When NOT to Use**:
- [Negative trigger 1]
- [Negative trigger 2]

### Skill Sequence
| Phase | Type | Skills | Purpose | Prerequisites |
|-------|------|--------|---------|---------------|
| 1 | Sequential | intent-analyzer, prompt-architect | Intent + Optimization | None |
| 2 | Parallel | [skill-a], [skill-b], [skill-c] | [Purposes] | Phase 1 |
| 3 | Sequential | [validation-skill] | Validation | Phase 2 |

### Success Criteria
- **Primary**: [Measurable outcome]
- **Acceptance Gates**: [List of gates]
- **Definition of Done**: [Clear completion criteria]

### Edge Cases
| Case | Detection | Handling |
|------|-----------|----------|
| [Case 1] | [Detection method] | [Recovery action] |
| [Case 2] | [Detection method] | [Recovery action] |

### Guardrails
**NEVER**:
- [Anti-pattern 1]
- [Anti-pattern 2]

**ALWAYS**:
- [Required behavior 1]
- [Required behavior 2]

### MCP Requirements
- **Required**: [List]
- **Optional**: [List]
- **Fallbacks**: [Mapping]

### Complexity and Timing
- **Complexity**: [Low/Medium/High/Very High]
- **Estimated Time**: [Duration]
- **Agent Count**: [Number]
```

---

## MECE Gap Analysis Process

To ensure complete playbook coverage:

1. **List All User Intent Categories**
   - Development, Research, Operations, Quality, Security, etc.

2. **Map Existing Playbooks to Categories**
   - Identify which intents are covered
   - Note any overlaps (violates ME)
   - Note any gaps (violates CE)

3. **Design Missing Playbooks**
   - Use this skill to create new playbooks
   - Ensure they don't overlap with existing
   - Validate trigger conditions are unique

4. **Validate MECE Property**
   - Every possible intent maps to exactly one playbook
   - No intent is unhandled (CE)
   - No intent triggers multiple playbooks (ME)

---

## Quick Reference

### When to Create a New Playbook
- Recurring workflow pattern (used 3+ times)
- Complex multi-skill orchestration (3+ skills)
- Team standardization need
- Gap in current MECE coverage

### When to Improve an Existing Playbook
- Suboptimal routing (wrong playbook selected)
- Performance issues (too slow)
- Missing parallelization opportunities
- Unclear success criteria
- Failure recovery not working

### Playbook Health Checklist
- [ ] Trigger conditions are specific and unique
- [ ] All skills exist in registry
- [ ] Dependencies are correctly identified
- [ ] Parallelization is maximized
- [ ] MCP requirements are complete
- [ ] Success criteria are measurable
- [ ] Guardrails are actionable
- [ ] Edge cases are handled
- [ ] Failure recovery is defined
- [ ] Documentation is complete

---

## Conclusion

Playbook Architect provides the systematic methodology for creating and optimizing playbooks at the same quality level as skills and agents. By applying 7-dimensional analysis, 4-phase creation methodology, and evidence-based patterns, this skill ensures playbooks are:

- Correctly triggered by user intent
- Optimally sequenced for efficiency
- Maximally parallelized for speed
- Resilient to failures
- Measurably successful

Use this skill whenever creating new playbooks or improving existing ones to maintain consistency and quality across the entire playbook ecosystem.

## Core Principles

### 1. Parallelization Maximizes Throughput
Independent skills MUST execute in parallel, not sequentially. A playbook with 3 independent skills running sequentially takes 3x longer than running them concurrently. Identify dependencies through explicit prerequisite analysis: if Skill B needs output from Skill A, they are sequential; if Skills B, C, D all only depend on Skill A, they run in parallel. Expected speedup from proper parallelization: 2-8x depending on skill count and dependency structure.

### 2. MECE Coverage Prevents Routing Ambiguity
Every possible user intent must trigger exactly one playbook (Mutually Exclusive, Collectively Exhaustive). Overlapping trigger keywords create routing conflicts where multiple playbooks match, forcing arbitrary selection. Gaps in coverage create unhandled intents where no playbook matches. Apply MECE analysis: map all intent categories, ensure each maps to exactly one playbook, validate no overlaps through keyword disambiguation and priority weights.

### 3. Explicit Success Criteria Enable Validation
Playbooks without measurable success criteria cannot be validated, improved, or trusted. Define primary metrics (what defines success), secondary metrics (execution time, quality score), acceptance gates (go/no-go checkpoints), and definition of done (clear completion criteria). Vague criteria like "works well" or "good quality" are unactionable. Quantifiable criteria (>95% test coverage, <30s execution time, 0.9+ quality score) enable objective validation and continuous improvement.

---

## Anti-Patterns

| Anti-Pattern | Why It Fails | Correct Approach |
|-------------|--------------|------------------|
| **Sequential Bias** | Running all skills sequentially even when dependencies don't require it. A 5-skill playbook that could run 3 skills in parallel takes 5x time instead of 3x time, reducing throughput by 40%. | Apply dependency analysis to every playbook. Group independent skills into parallel phases. Only sequential phases should block execution. Draw dependency graph (DAG) to visualize critical path and identify parallelization opportunities. |
| **Vague Trigger Keywords** | Using broad keywords like "build" or "test" that match 10+ playbooks. Creates routing ambiguity where multiple playbooks have equal match scores, forcing arbitrary selection or user disambiguation. | Use specific, contextual trigger keywords. Instead of "build," use "build REST API" or "build React component" or "build Docker container." Add negative triggers (when NOT to use) and priority weights to disambiguate close matches. |
| **Missing Fallback Skills** | Not defining fallback skills for critical steps that depend on external MCPs or services. When primary skill fails due to unavailable MCP (e.g., playwright), playbook halts with no recovery strategy. | Define fallback skills for every critical step. If primary skill needs playwright MCP, fallback to manual-testing-skill. If skill needs Memory MCP, fallback to file-based storage. Map mcp_requirements.fallbacks for all external dependencies. |

---

## Conclusion (Enhanced)

Playbook Architect provides the systematic methodology for creating and optimizing playbooks at the same quality level as skills and agents. By applying 7-dimensional analysis, 4-phase creation methodology, and evidence-based patterns, this skill ensures playbooks are:

- Correctly triggered by user intent through specific, disambiguated keywords
- Optimally sequenced for efficiency through dependency analysis
- Maximally parallelized for speed through concurrent execution of independent skills
- Resilient to failures through fallback skills and recovery strategies
- Measurably successful through explicit, quantifiable success criteria

Playbooks are the orchestration layer that transforms the 180+ skill ecosystem from isolated capabilities into coordinated workflows. A well-designed playbook applies the right skills, in the right order, with maximum parallelization and minimum failure risk. This skill elevates playbook design from ad-hoc sequences to engineered workflows with predictable performance characteristics.

Use this skill whenever creating new playbooks or improving existing ones to maintain consistency and quality across the entire playbook ecosystem. The 4-phase SOP (Workflow Analysis, Playbook Architecture, Success Criteria, Integration) ensures every playbook meets production standards: MECE-compliant triggers, dependency-optimized sequences, parallelized execution, and validated success metrics. Build playbooks as you would build production systems, with rigor and measurement.
