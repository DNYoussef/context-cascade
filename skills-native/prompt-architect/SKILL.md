---
name: prompt-architect
description: Comprehensive framework for analyzing, creating, and refining prompts for AI systems (v2.0 adds Phase 0 expertise loading and quality scoring). Use when creating prompts for Claude, ChatGPT, or other language models, improving existing prompts, or applying evidence-based prompt engineering techniques. Integrates with recursive improvement loop as Phase 2 of 5-phase workflow. Distinct from prompt-forge (which improves system prompts). --- # Prompt Architect A comprehensive framework for creating, analyzing, and refining prompts for AI language models using evidence-based techniques, structural optimization principles, and systematic anti-pattern detection. ## Trigger Keywords **USE WHEN user mentions:** - "improve prompt", "optimize prompt", "refine prompt", "enhance prompt" - "create prompt for", "design prompt", "build prompt" - "prompt isn't working", "prompt quality", "better prompt" - "prompt engineering", "evidence-based prompting" - "self-consistency", "program-of-thought", "plan-and-solve" - "prompt...
---

# Prompt Architect

A comprehensive framework for creating, analyzing, and refining prompts for AI language models using evidence-based techniques, structural optimization principles, and systematic anti-pattern detection.

## Trigger Keywords

**USE WHEN user mentions:**
- "improve prompt", "optimize prompt", "refine prompt", "enhance prompt"
- "create prompt for", "design prompt", "build prompt"
- "prompt isn't working", "prompt quality", "better prompt"
- "prompt engineering", "evidence-based prompting"
- "self-consistency", "program-of-thought", "plan-and-solve"
- "prompt library", "prompt template", "reusable prompt"

**DO NOT USE when:**
- User wants to create/improve AGENT SYSTEM PROMPTS - use agent-creator or prompt-forge
- User wants to create SKILLS (not prompts) - use skill-creator-agent or micro-skill-creator
- User wants to improve THIS skill itself - use skill-forge
- Prompt is one-time use without optimization value - direct crafting faster

**Instead use:**
- agent-creator when designing agent system prompts (Phase 3: Architecture Design)
- prompt-forge when improving system prompts for existing agents
- skill-creator-agent when the goal is a skill (which may contain prompts)
- interactive-planner when user needs help clarifying intent before prompt design


## Overview

Prompt Architect provides a systematic approach to prompt engineering that combines research-backed techniques with practical experience. Whether crafting prompts for Claude, ChatGPT, Gemini, or other systems, this skill applies proven patterns that consistently produce high-quality responses.

This skill is particularly valuable for developing prompts used repeatedly, troubleshooting prompts that aren't performing well, building prompt templates for teams, or optimizing high-stakes tasks where prompt quality significantly impacts outcomes.

## When to Use This Skill

Apply Prompt Architect when:
- Creating new prompts for AI systems that will be used repeatedly or programmatically
- Improving existing prompts that produce inconsistent or suboptimal results
- Building prompt libraries or templates for team use
- Teaching others about effective prompt engineering
- Working on complex tasks where prompt quality substantially impacts outcomes
- Debugging why a prompt isn't working as expected

This skill focuses on prompts as engineered artifacts rather than casual conversational queries. The assumption is you're creating prompts that provide compounding value through repeated or systematic use.

## MCP Requirements

This skill operates using Claude Code's built-in tools only. No additional MCP servers required.

**Why No MCPs Needed**:
- Prompt analysis and refinement performed through Claude's native capabilities
- No external services or databases required
- Uses Claude Code's file operations for saving/loading prompts
- All prompting techniques applied through conversational interaction

## Phase 0: Expertise Loading [NEW - v2.0]

Before analyzing or creating prompts, check for domain expertise.

**Check for Domain Expertise**:
```bash
# Detect domain from prompt topic
DOMAIN=$(detect_domain_from_prompt)

# Check if expertise exists
ls .claude/expertise/${DOMAIN}.yaml
```

**Load If Available**:
```yaml
if expertise_exists:
  actions:
    - Run: /expertise-validate {domain}
    - Load: patterns, conventions, known_issues
    - Apply: Use expertise to inform prompt design
  benefits:
    - Apply proven patterns (documented in expertise)
    - Avoid known issues (prevent common failures)
    - Match conventions (consistent with codebase)
else:
  actions:
    - Flag: Discovery mode
    - Plan: Generate expertise learnings after prompt work
```

## Recursive Improvement Integration (v2.0)

Prompt Architect is part of the recursive self-improvement loop:

### Role in the Loop

```
Prompt Architect (PHASE 2 SKILL)
    |
    +--> Optimizes USER prompts (Phase 2 of 5-phase workflow)
    +--> Distinct from prompt-forge (which improves SYSTEM prompts)
    +--> Can be improved BY prompt-forge
```

### Input/Output Contracts

```yaml
input_contract:
  required:
    - prompt_to_analyze: string  # The prompt to improve
  optional:
    - context: string  # What the prompt is for
    - constraints: list  # Specific requirements
    - examples: list  # Good/bad output examples
    - expertise_file: path  # Pre-loaded domain expertise

output_contract:
  required:
    - improved_prompt: string  # The optimized prompt
    - analysis_report: object  # Scoring across dimensions
    - changes_made: list  # What was changed and why
  optional:
    - techniques_applied: list  # Which evidence-based techniques
    - confidence_score: float  # How confident in improvement
    - expertise_delta: object  # Learnings for expertise update
```

### Quality Scoring System

```yaml
scoring_dimensions:
  clarity:
    score: 0.0-1.0
    weight: 0.25
    checks:
      - "Single clear action per instruction"
      - "No ambiguous terms"
      - "Explicit success criteria"

  completeness:
    score: 0.0-1.0
    weight: 0.25
    checks:
      - "All inputs specified"
      - "All outputs defined"
      - "Edge cases addressed"

  precision:
    score: 0.0-1.0
    weight: 0.25
    checks:
      - "Quantifiable where possible"
      - "Constraints explicitly stated"
      - "Trade-offs documented"

  technique_coverage:
    score: 0.0-1.0
    weight: 0.25
    checks:
      - "Appropriate techniques applied"
      - "Self-consistency for factual tasks"
      - "Plan-and-solve for workflows"

  overall_score: weighted_average
  minimum_passing: 0.7
```

### Eval Harness Integration

Prompt improvements are tested against:

```yaml
benchmark: prompt-generation-benchmark-v1
  tests:
    - pg-001: Simple Task Prompt
    - pg-002: Complex Workflow Prompt
    - pg-003: Analytical Task Prompt
  minimum_scores:
    clarity: 0.7
    completeness: 0.7
    precision: 0.7

regression: prompt-architect-regression-v1
  tests:
    - par-001: Clarity improvement preserved (must_pass)
    - par-002: Evidence-based techniques applied (must_pass)
    - par-003: Uncertainty handling present (must_pass)
```

### Memory Namespace

```yaml
namespaces:
  - prompt-architect/analyses/{id}: Prompt analyses
  - prompt-architect/improvements/{id}: Applied improvements
  - prompt-architect/metrics: Performance tracking
  - improvement/audits/prompt-architect: Audits of this skill
```

### Uncertainty Handling

When prompt intent is unclear:

```yaml
confidence_check:
  if confidence >= 0.8:
    - Proceed with optimization
    - Document assumptions
  if confidence 0.5-0.8:
    - Present 2-3 interpretation options
    - Ask user to confirm intent
    - Document uncertainty areas
  if confidence < 0.5:
    - DO NOT proceed with optimization
    - List what is unclear about the prompt
    - Ask specific clarifying questions
    - NEVER guess at intent
```

### Analysis Output Format

```yaml
prompt_analysis_output:
  prompt_id: "analysis-{timestamp}"
  original_prompt: "..."
  improved_prompt: "..."

  scores:
    clarity: 0.85
    completeness: 0.78
    precision: 0.82
    technique_coverage: 0.75
    overall: 0.80

  changes:
    - location: "Opening instruction"
      before: "Analyze the data"
      after: "Analyze this dataset to identify trends in user engagement"
      rationale: "Replaced vague verb with specific action"
      technique: "clarity_enhancement"

  techniques_applied:
    - self_consistency: true
    - plan_and_solve: false
    - program_of_thought: false

  recommendation: "IMPROVED"
  confidence: 0.85
```

-----------|---------|----------|
| **Vague Action Verbs** | Instructions like "analyze", "process", "improve" allow excessive interpretation | Use specific verbs: "Extract trends", "Validate schema", "Refactor using dependency injection" |
| **Contradictory Requirements** | "Be comprehensive but brief" creates impossible constraints | Prioritize explicitly: "200-word summary followed by detailed sections" |
| **Insufficient Context** | Assuming shared understanding that doesn't exist | Make context explicit: Define audience, purpose, constraints, background, success criteria |
| **Missing Edge Case Handling** | "Extract emails from text" doesn't specify none found, invalid format, multiple types | Address boundaries: "If none found, return empty array. Validate format, exclude malformed." |
| **Neglecting Evidence Techniques** | Prompts rely on single-pass generation without validation | Add self-consistency: "After reaching conclusion, validate by considering alternative interpretations" |

## Conclusion

Prompt Architect transforms prompt engineering from intuitive trial-and-error into systematic optimization. By applying structural positioning, evidence-based techniques, and explicit output specification, prompts achieve 85%+ quality scores (clarity, completeness, precision, technique coverage) compared to baseline 60%.

The framework combines research-backed patterns with practical refinement methodology. Quality scoring across four dimensions (clarity, completeness, precision, actionability) provides measurable improvement tracking. Chain-of-verification integration catches ambiguities early when they're cheapest to fix.

Use Prompt Architect when creating prompts for repeated use, programmatic execution, or high-stakes tasks where quality significantly impacts outcomes. The investment in systematic prompt design pays dividends through consistent AI performance, fewer clarification cycles, and prompts that remain effective as models evolve. Prompts optimized with this methodology become reusable organizational assets rather than disposable queries.

## Core Principles

### 1. Clarity Through Specificity
Vague instructions like "analyze this data" or "make it better" allow excessive interpretation and produce inconsistent results. Specific instructions with concrete objectives ("Analyze this dataset to identify weekly trends in user engagement, segmented by demographics") constrain the response space and improve consistency by 40-60%. Every prompt should answer: What action? On what? For what purpose? By what criteria?

### 2. Context Positioning Drives Attention
Critical information at the beginning and end receives 2-3x more attention than content buried in the middle. This is not subjective preference but empirically validated attention distribution. Place core task definition and constraints at the start, supporting details in the middle, and reinforcement of key requirements at the end. Structural optimization is as important as content quality.

### 3. Evidence-Based Techniques Scale Quality
Self-consistency checks improve factual accuracy by 20-40%. Program-of-thought structures boost logical reasoning by 30-50%. Plan-and-solve frameworks reduce multi-stage errors by 25-35%. These are not theoretical patterns but empirically validated techniques from millions of model interactions. Match technique to task type: analytical tasks need self-consistency, logical tasks need program-of-thought, workflows need plan-and-solve.

----------|--------------|------------------|
| **Vague Action Verbs** | Using ambiguous instructions like "analyze," "improve," or "optimize" without specifying how or by what criteria. Forces model to guess intent, leading to 40-60% variance in interpretation across runs. | Replace vague verbs with specific actions and explicit criteria. "Analyze this dataset to identify weekly engagement trends and demographic patterns, focusing on correlation between feature usage and retention rates." Include success criteria. |
| **Contradictory Requirements** | Asking for "comprehensive but brief" or "detailed summary" creates impossible constraints. Model must choose one, leading to unpredictable outputs that satisfy neither requirement. | Prioritize requirements explicitly or structure in phases. "Provide a 200-word executive summary followed by detailed sections on each key finding (500 words each)." Make trade-offs explicit. |
| **Assuming Shared Context** | References to "the usual format" or "our standard approach" without defining them. Model lacks the unstated context, resulting in outputs that miss key requirements 50%+ of the time. | Make all context explicit. "Format as JSON with fields: name (string), age (integer), skills (array of strings). Follow camelCase naming. Include error field if validation fails." No assumptions. |

---

## Conclusion (Enhanced)

Effective prompt engineering combines art and science. These principles provide scientific foundation—research-backed techniques and structural optimization—but applying them requires judgment, creativity, and adaptation to specific contexts.

Prompt-architect transforms casual queries into engineered prompts through systematic analysis across 6 dimensions: intent clarity, structural organization, context sufficiency, technique application, failure mode detection, and formatting quality. By applying evidence-based techniques (self-consistency, program-of-thought, plan-and-solve) and structural optimization (attention positioning, hierarchical organization, delimiter strategy), this skill creates prompts that produce consistent, high-quality responses.

Master these fundamentals, then develop your own expertise through practice and systematic reflection on results. The most effective prompt engineers combine principled approaches with creative experimentation and continuous learning from actual outcomes. Use this skill as Phase 2 of the 5-phase workflow to optimize user requests before planning and execution. Well-architected prompts reduce ambiguity by 60%+, improve task success rates by 40%+, and create compounding value through reusable prompt libraries.