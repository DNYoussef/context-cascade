---
name: micro-skill-creator
description: Rapidly creates atomic, focused skills optimized with evidence-based prompting, specialist agents, and systematic testing. Each micro-skill does one thing exceptionally well using self-consistency, program-of-thought, and plan-and-solve patterns. Enhanced with agent-creator principles and functionality-audit validation. Perfect for building composable workflow components.
---

<!-- SKILL SOP IMPROVEMENT v1.0 -->
## Skill Execution Criteria

### When to Use This Skill
- Building atomic, reusable workflow components
- Creating focused skills that do one thing exceptionally well
- Establishing building blocks for cascade orchestration
- Developing domain-specific micro-capabilities
- When repeatability and composability are critical

### When NOT to Use This Skill
- For complex multi-step workflows (use cascade-orchestrator instead)
- For one-off exploratory tasks without reuse value
- When task is too simple to benefit from skill abstraction
- When external tools already handle the capability better

### Success Criteria
- primary_outcome: "Atomic skill with single responsibility, clean interface, specialist agent, and systematic validation"
- quality_threshold: 0.95
- verification_method: "Skill executes successfully in isolation, composes cleanly with other skills, passes functionality-audit validation"

### Edge Cases
- case: "Skill scope creep (trying to do too much)"
  handling: "Decompose into multiple micro-skills with clear interfaces, apply Unix philosophy"
- case: "Unclear input/output contract"
  handling: "Define explicit schema, add validation, document expected formats"
- case: "Skill depends on external state"
  handling: "Make dependencies explicit parameters, document preconditions, add state validation"

### Skill Guardrails
NEVER:
  - "Create skills with multiple responsibilities (violates atomic principle)"
  - "Use generic agents instead of domain specialists"
  - "Skip validation testing (functionality-audit required)"
  - "Create skills without clear composability in mind"
ALWAYS:
  - "Follow single responsibility principle (one skill, one purpose)"
  - "Design specialist agent with evidence-based prompting (self-consistency, program-of-thought, plan-and-solve)"
  - "Define clean input/output contracts with validation"
  - "Test in isolation AND in composition with other skills"
  - "Integrate with neural training for continuous improvement"

### Evidence-Based Execution
self_consistency: "After skill creation, execute multiple times with same input to verify deterministic behavior and consistent quality"
program_of_thought: "Decompose creation into: 1) Define single responsibility, 2) Design specialist agent, 3) Build input/output contract, 4) Implement core logic, 5) Validate systematically, 6) Test composability"
plan_and_solve: "Plan: Identify atomic operation + specialist expertise -> Execute: Build agent + validate -> Verify: Isolation test + composition test + neural training integration"
<!-- END SKILL SOP IMPROVEMENT -->

# Micro-Skill Creator (Enhanced)

## Trigger Keywords

**USE WHEN user mentions:**
- "create micro-skill", "atomic skill", "small skill", "focused skill"
- "single-purpose skill", "one task skill"
- "building block", "composable skill", "cascade component"
- "reusable [domain] skill", "skill for [specific task]"
- "Unix philosophy skill", "do one thing well"
- "skill using [evidence technique]" (self-consistency, program-of-thought, plan-and-solve)

**DO NOT USE when:**
- User wants COMPLEX multi-step skill - use skill-creator-agent
- User wants to create AGENT (not skill) - use agent-creator
- User wants to IMPROVE existing skill - use recursive-improvement or skill-forge
- User wants to optimize PROMPTS - use prompt-architect
- Task is one-off without reuse value - direct implementation faster
- Task already handled by external tools - integration better than recreation

**Instead use:**
- skill-creator-agent when skill needs multiple coordinated agents or complex workflow
- agent-creator when goal is standalone agent (no skill wrapper needed)
- cascade-orchestrator when composing existing skills into workflows
- prompt-architect when optimizing prompts (not creating skills)


## Overview
Creates small, focused skills that each spawn a specialist agent optimized for a specific task using evidence-based prompting techniques. This enhanced version integrates agent-creator principles, prompt-architect patterns, and systematic testing from functionality-audit.

## Philosophy: Atomic Excellence

**Unix Philosophy for AI**: Do one thing and do it well, with clean interfaces for composition.

**Evidence-Based Agents**: Every micro-skill spawns a specialist agent using research-validated techniques:
- **Self-consistency** for factual tasks
- **Program-of-thought** for analytical tasks
- **Plan-and-solve** for complex tasks
- **Neural training** integration for continuous improvement

**Key Principles**:
1. Single responsibility per skill
2. Specialist agent per domain
3. Clean input/output contracts
4. Systematic validation
5. Composability first

## When to Create Micro-Skills

✅ **Perfect For**:
- Tasks you perform repeatedly
- Operations needing specialist expertise
- Building blocks for cascades
- Capabilities for slash commands
- Domain-specific workflows

❌ **Don't Use For**:
- One-off exploratory tasks
- Tasks too simple for specialization
- Better handled by external tools

## Enhanced Creation Workflow

### Step 1: Define Single Responsibility

State in ONE sentence what this skill does:
- "Extract structured data from unstructured documents"
- "Validate API responses against OpenAPI schemas"
- "Refactor code to use dependency injection patterns"

**Trigger Pattern**: Define keywords for Claude Code discovery.

### Step 2: Design Specialist Agent (Enhanced)

Using **agent-creator** + **prompt-architect** principles:

#### A. Identity & Expertise
```markdown
I am a [domain] specialist with expertise in:
- [Core competency 1]
- [Core competency 2]
- [Edge case handling]
- [Output quality standards]
```

#### B. Evidence-Based Methodology

**For Factual Tasks (Self-Consistency)**:
```markdown
Methodology:
1. Extract information from multiple perspectives
2. Cross-reference findings for consistency
3. Flag any inconsistencies or ambiguities
4. Provide confidence scores
5. Return validated results
```

**For Analytical Tasks (Program-of-Thought)**:
```markdown
Methodology:
1. Decompose problem into logical components
2. Work through each component systematically
3. Show intermediate reasoning
4. Validate logical consistency
5. Synthesize final analysis
```

**For Complex Tasks (Plan-and-Solve)**:
```markdown
Methodology:
1. Create comprehensive plan with dependencies
2. Break into executable steps
3. Execute plan systematically
4. Validate completion at each step
5. Return complete solution
```

#### C. Output Specification
Precise format enables reliable composition:
```yaml
output:
  format: json | markdown | code
  structure:
    required_fields: [...]
    optional_fields: [...]
  validation_rules: [...]
  quality_standards: [...]
```

#### D. Failure Mode Awareness
```markdown
Common Failure Modes & Mitigations:
- [Failure type 1]: [How to detect and handle]
- [Failure type 2]: [How to detect and handle]
```

### Step 3: Create Skill Structure

**SKILL.md Template**:
```markdown
# Skill Name

## Purpose
[Clear, single-sentence purpose]

## Specialist Agent
[Agent system prompt using evidence-based patterns]

## Input Contract
[Explicit input requirements]

## Output Contract
[Explicit output format and validation]

## Integration Points
- Cascades: [How it composes]
- Commands: [Slash command bindings]
- Other Skills: [Dependencies or companions]
```

### Step 4: Add Validation & Testing

**Systematic Testing** (from functionality-audit):
```markdown
Test Cases:
1. Normal operation with typical inputs
2. Boundary conditions
3. Error cases with invalid inputs
4. Edge cases
5. Performance stress tests
```

**Validation Checklist**:
- [ ] Skill triggers correctly
- [ ] Agent executes with domain expertise
- [ ] Output matches specifications
- [ ] Errors handled gracefully
- [ ] Composes with other skills
- [ ] Performance acceptable

### Step 5: Neural Training Integration

**Enable Learning** (from ruv-swarm):
```yaml
training:
  pattern: [cognitive pattern type]
  feedback_collection: true
  improvement_iteration: true
  success_tracking: true
```

## Micro-Skill Templates (Enhanced)

### 1. Data Extraction Micro-Skill

**Agent System Prompt**:
```markdown
I am an extraction specialist using self-consistency checking for accuracy.

Methodology (Self-Consistency Pattern):
1. Scan source from multiple angles
2. Extract candidate information
3. Cross-validate findings
4. Flag confidence levels and ambiguities
5. Return structured data with metadata

Failure Modes:
- Ambiguous source: Flag for human review
- Missing information: Explicitly note gaps
- Low confidence: Provide alternative interpretations
```

**Input/Output**:
```yaml
input:
  source_document: string | file_path
  target_schema: json_schema
  confidence_threshold: number (default: 0.8)

output:
  extracted_data: object (matches target_schema)
  confidence_scores: object (per field)
  ambiguities: array[string]
  metadata:
    extraction_quality: high | medium | low
    processing_time: number
```

### 2. Validation Micro-Skill

**Agent System Prompt**:
```markdown
I am a validation specialist using program-of-thought decomposition.

Methodology (Program-of-Thought Pattern):
1. Parse input systematically
2. Load specification/rules
3. Check each rule with clear reasoning
4. Show validation logic step-by-step
5. Categorize violations by severity

Failure Modes:
- Ambiguous rules: Request clarification
- Conflicting rules: Flag inconsistencies
- Edge cases: Apply conservative interpretation
```

**Input/Output**:
```yaml
input:
  data: object | array
  specification: schema | rules_file
  strictness: lenient | normal | strict

output:
  validation_result:
    status: pass | fail | warning
    violations: array[{rule, location, severity, message}]
    summary: {errors: number, warnings: number}
  suggested_fixes: array[{location, fix, confidence}]
```

### 3. Generation Micro-Skill

**Agent System Prompt**:
```markdown
I am a generation specialist using plan-and-solve framework.

Methodology (Plan-and-Solve Pattern):
1. Parse specification and understand requirements
2. Create comprehensive generation plan
3. Execute plan systematically
4. Validate output against requirements
5. Review for completeness and correctness

Failure Modes:
- Incomplete specification: Request missing details
- Ambiguous requirements: Provide multiple options
- Validation failures: Iterate with fixes
```

**Input/Output**:
```yaml
input:
  specification: object | markdown
  templates: array[template] (optional)
  config: object (generation parameters)

output:
  generated_artifact: string | object
  generation_metadata:
    decisions_made: array[{decision, rationale}]
    completeness_check: pass | partial | fail
    warnings: array[string]
```

### 4. Analysis Micro-Skill

**Agent System Prompt**:
```markdown
I am an analysis specialist combining program-of-thought and self-consistency.

Methodology:
1. Gather data systematically
2. Apply analytical framework (program-of-thought)
3. Identify patterns and anomalies
4. Validate conclusions (self-consistency)
5. Prioritize findings by importance

Failure Modes:
- Insufficient data: Flag and request more
- Conflicting indicators: Present both interpretations
- Uncertain conclusions: Provide confidence levels
```

**Input/Output**:
```yaml
input:
  data: object | array | file_path
  analysis_type: quality | security | performance | etc
  depth: shallow | normal | deep

output:
  analysis_report:
    key_findings: array[{finding, evidence, severity}]
    recommendations: array[{action, priority, rationale}]
    confidence_levels: object (per finding)
    supporting_data: object
```

## Integration with Cascade Workflows

**Composition Patterns**:
```yaml
# Sequential
extract-data → validate-data → transform-data → generate-report

# Parallel
input → [validate-schema + security-scan + quality-check] → merge-results

# Conditional
validate → (if pass: deploy) OR (if fail: generate-error-report)

# Map-Reduce
collection → map(analyze-item) → reduce(aggregate-results)

# Iterative
refactor → check-quality → (repeat if below threshold)
```

## Integration with Slash Commands

**Command Binding Example**:
```yaml
command:
  name: /validate-api
  binding:
    type: micro-skill
    target: validate-api-response
    parameter_mapping:
      file: ${file_path}
      schema: ${schema_path}
      strict: ${--strict flag}
```

## Best Practices (Enhanced)

### Skill Design
1. ✅ Truly atomic - one responsibility
2. ✅ Evidence-based agent methodology
3. ✅ Explicit input/output contracts
4. ✅ Comprehensive error handling
5. ✅ Systematic validation testing
6. ✅ Neural training enabled

### Agent Optimization
1. ✅ Use appropriate evidence technique
2. ✅ Include failure mode awareness
3. ✅ Specify exact output formats
4. ✅ Add self-validation steps
5. ✅ Enable continuous learning

### Composition
1. ✅ Clean interfaces for chaining
2. ✅ Standardized error formats
3. ✅ Idempotent when possible
4. ✅ Version interfaces carefully
5. ✅ Document dependencies

## Working with Micro-Skill Creator

**Invocation**:
"Create a micro-skill that [single responsibility] using [evidence technique] with [domain expertise]"

**The creator will**:
1. Guide you through agent design with evidence-based patterns
2. Generate skill structure with proper contracts
3. Create validation test cases
4. Set up neural training integration
5. Produce production-ready micro-skill

**Integration**:
- Works with **agent-creator** for agent design
- Works with **cascade-orchestrator** for workflow composition
- Works with **slash-command-encoder** for /command access
- Works with **functionality-audit** for validation
- Works with **ruv-swarm MCP** for neural training

-----------|---------|----------|
| **Scope Creep Beyond Single Responsibility** | Skill tries to extract, validate, and transform data in one operation | Decompose into 3 micro-skills: extract-data, validate-data, transform-data with clean interfaces |
| **Generic Agents Instead of Specialists** | Using "coder" agent for specialized tasks instead of domain experts | Design specialist agent with evidence-based methodology and domain-specific failure awareness |
| **Implicit Input/Output Contracts** | Skills assume data formats without validation, causing cascade failures | Define explicit JSON schemas for inputs/outputs, add validation, document edge case handling |
| **Skipping Isolation Testing** | Skills only tested as part of larger cascades, making bugs hard to isolate | Test micro-skill independently with all 5 case types before cascade integration |
| **Stateful Dependencies Without Documentation** | Skill depends on external state (files, env vars) without declaring it | Make dependencies explicit parameters, document preconditions, add state validation checks |

## Conclusion

Micro-Skill Creator enables the construction of robust, composable AI workflows through atomic skill design. By adhering to single-responsibility principle, designing specialist agents with evidence-based methodologies, and enforcing systematic validation, micro-skills become reliable building blocks for complex cascades.

The framework integrates agent-creator principles for specialist design, prompt-architect patterns for optimization, and functionality-audit validation for systematic testing. Skills created with this methodology compose predictably, fail gracefully, and improve continuously through neural training integration.

Use Micro-Skill Creator when building reusable workflow components, establishing domain-specific capabilities, or constructing cascade orchestration pipelines. The 30-45 minute investment per micro-skill yields atomic units that can be composed in seconds, tested in isolation, and reused across multiple workflows. As your micro-skill library grows, complex tasks become assembly of proven components rather than bespoke implementations.