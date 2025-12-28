---
name: when-optimizing-prompts-use-prompt-optimization-analyzer
version: 1.0.0
description: Active diagnostic tool for analyzing prompt quality, detecting anti-patterns,
  identifying token waste, and providing optimization recommendations
tags:
- meta-tool
- prompt-engineering
- optimization
- analysis
- diagnostics
complexity: MEDIUM
agents_required:
- code-analyzer
- researcher
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

# Prompt Optimization Analyzer

**Purpose:** Analyze prompt quality and provide actionable optimization recommendations to reduce token waste, improve clarity, and enhance effectiveness.

## When to Use This Skill

- Before publishing new skills or slash commands
- When prompts exceed token budgets
- When responses are inconsistent or unclear
- During skill maintenance and refinement
- When analyzing existing prompt libraries

## Analysis Dimensions

### 1. Token Efficiency Analysis
- Redundancy detection (repeated concepts, phrases)
- Verbosity measurement (word count vs. information density)
- Compression opportunities (equivalent shorter forms)
- Example bloat (excessive or redundant examples)

### 2. Anti-Pattern Detection
- Vague instructions ("do something good")
- Ambiguous terminology (undefined jargon)
- Conflicting requirements (contradictory rules)
- Missing context (insufficient background)
- Over-specification (unnecessary constraints)

### 3. Trigger Issue Analysis
- Unclear activation conditions
- Overlapping trigger patterns
- Missing edge cases
- Too broad/narrow scope

### 4. Structural Optimization
- Information architecture (logical flow)
- Section organization (grouping, hierarchy)
- Reference efficiency (cross-references, links)
- Progressive disclosure (layered detail)

## Execution Process

### Phase 1: Token Waste Detection

```bash
# Analyze prompt for redundancy
npx claude-flow@alpha hooks pre-task --description "Analyzing prompt for token waste"

# Store original metrics
npx claude-flow@alpha memory store --key "optimization/original-tokens" --value "{
  \"total_tokens\": <count>,
  \"redundancy_score\": <0-100>,
  \"verbosity_score\": <0-100>
}"
```

**Analysis Script:**
```javascript
// Embedded token analysis
function analyzeTokenWaste(promptText) {
  const metrics = {
    totalWords: promptText.split(/\s+/).length,
    totalChars: promptText.length,
    redundancyScore: 0,
    verbosityScore: 0,
    issues: []
  };

  // Detect phrase repetition
  const phrases = extractPhrases(promptText, 3); // 3-word phrases
  const phraseCounts = countOccurrences(phrases);
  const repeated = Object.entries(phraseCounts).filter(([_, count]) => count > 2);

  if (repeated.length > 0) {
    metrics.redundancyScore += repeated.length * 10;
    metrics.issues.push({
      type: "redundancy",
      severity: "medium",
      count: repeated.length,
      examples: repeated.slice(0, 3).map(([phrase]) => phrase)
    });
  }

  // Measure verbosity
  const avgWordLength = promptText.split(/\s+/)
    .reduce((sum, word) => sum + word.length, 0) / metrics.totalWords;

  if (avgWordLength > 6) {
    metrics.verbosityScore += 20;
    metrics.issues.push({
      type: "verbosity",
      severity: "low",
      avgWordLength: avgWordLength.toFixed(2),
      suggestion: "Consider shorter, clearer words"
    });
  }

  // Detect filler words
  const fillerWords = ["very", "really", "just", "actually", "basically", "simply"];
  const fillerCount = fillerWords.reduce((count, filler) => {
    const regex = new RegExp(`\\b${filler}\\b`, 'gi');
    return count + (promptText.match(regex) || []).length;
  }, 0);

  if (fillerCount > 5) {
    metrics.redundancyScore += fillerCount * 2;
    metrics.issues.push({
      type: "filler-words",
      severity: "low",
      count: fillerCount,
      suggestion: "Remove unnecessary filler words"
    });
  }

  return metrics;
}

function extractPhrases(text, wordCount) {
  const words = text.toLowerCase().split(/\s+/);
  const phrases = [];
  for (let i = 0; i <= words.length - wordCount; i++) {
    phrases.push(words.slice(i, i + wordCount).join(' '));
  }
  return phrases;
}

function countOccurrences(items) {
  return items.reduce((counts, item) => {
    counts[item] = (counts[item] || 0) + 1;
    return counts;
  }, {});
}
```

### Phase 2: Anti-Pattern Detection

**Common Anti-Patterns:**

1. **Vague Instructions**
   - ❌ "Make it better"
   - ✅ "Reduce token count by 20% while maintaining clarity"

2. **Ambiguous Terminology**
   - ❌ "Handle errors appropriately"
   - ✅ "Catch exceptions, log to memory, return user-friendly message"

3. **Conflicting Requirements**
   - ❌ "Be concise but provide detailed explanations"
   - ✅ "Provide concise summaries with optional detail links"

4. **Missing Context**
   - ❌ "Use the standard format"
   - ✅ "Use JSON format: {type, severity, description}"

5. **Over-Specification**
   - ❌ "Always use exactly 4 spaces, never tabs, indent 2 levels..."
   - ✅ "Follow project .editorconfig settings"

**Detection Script:**
```javascript
function detectAntiPatterns(promptText) {
  const patterns = [];

  // Vague instruction markers
  const vagueMarkers = ["better", "good", "appropriate", "proper", "suitable"];
  vagueMarkers.forEach(marker => {
    if (new RegExp(`\\b${marker}\\b`, 'i').test(promptText)) {
      patterns.push({
        type: "vague-instruction",
        marker: marker,
        severity: "high",
        suggestion: "Replace with specific, measurable criteria"
      });
    }
  });

  // Missing definitions
  const technicalTerms = promptText.match(/\b[A-Z][A-Za-z]*(?:[A-Z][a-z]*)+\b/g) || [];
  const definedTerms = (promptText.match(/\*\*[^*]+\*\*:/g) || []).length;

  if (technicalTerms.length > 5 && definedTerms < technicalTerms.length * 0.3) {
    patterns.push({
      type: "undefined-jargon",
      severity: "medium",
      technicalTermCount: technicalTerms.length,
      definedCount: definedTerms,
      suggestion: "Add definitions for technical terms"
    });
  }

  // Conflicting modal verbs
  const mustStatements = (promptText.match(/\b(must|required|mandatory)\b/gi) || []).length;
  const shouldStatements = (promptText.match(/\b(should|recommended|optional)\b/gi) || []).length;

  if (mustStatements > 10 && shouldStatements > 10) {
    patterns.push({
      type: "requirement-confusion",
      severity: "medium",
      mustCount: mustStatements,
      shouldCount: shouldStatements,
      suggestion: "Separate MUST vs SHOULD requirements clearly"
    });
  }

  return patterns;
}
```

### Phase 3: Trigger Analysis

```javascript
function analyzeTriggers(triggerText) {
  const issues = [];

  // Check clarity
  if (!triggerText.includes("when") && !triggerText.includes("if")) {
    issues.push({
      type: "unclear-condition",
      severity: "high",
      suggestion: "Use explicit 'when' or 'if' conditions"
    });
  }

  // Check specificity
  const vagueTerms = ["thing", "stuff", "something", "anything"];
  vagueTerms.forEach(term => {
    if (new RegExp(`\\b${term}\\b`, 'i').test(triggerText)) {
      issues.push({
        type: "vague-trigger",
        term: term,
        severity: "high",
        suggestion: "Replace with specific entity or action"
      });
    }
  });

  // Check scope
  if (triggerText.split(/\s+/).length < 5) {
    issues.push({
      type: "too-narrow",
      severity: "medium",
      wordCount: triggerText.split(/\s+/).length,
      suggestion: "Consider broader applicability"
    });
  }

  return issues;
}
```

### Phase 4: Optimization Recommendations

**Code Analyzer Agent Task:**
```bash
# Spawn analyzer agent
# Agent instructions:
# 1. Analyze prompt structure and flow
# 2. Identify optimization opportunities
# 3. Generate before/after comparisons
# 4. Calculate token savings
# 5. Store recommendations in memory

npx claude-flow@alpha memory store --key "optimization/recommendations" --value "{
  \"structural\": [...],
  \"content\": [...],
  \"examples\": [...],
  \"estimated_savings\": \"X tokens (Y%)\"
}"
```

### Phase 5: Before/After Comparison

**Optimization Report Format:**

```markdown
## Prompt Optimization Report

### Original Metrics
- Total tokens: <count>
- Redundancy score: <0-100>
- Verbosity score: <0-100>
- Anti-patterns found: <count>

### Issues Detected

#### High Severity
1. [Type] <description>
   - Location: <section>
   - Impact: <token/clarity impact>
   - Fix: <recommendation>

#### Medium Severity
...

#### Low Severity
...

### Recommended Changes

#### Structural
- [ ] Reorganize sections for logical flow
- [ ] Consolidate redundant examples
- [ ] Extract repetitive content to references

#### Content
- [ ] Replace vague terms with specific criteria
- [ ] Add missing definitions
- [ ] Remove filler words (identified: <count>)

#### Examples
- [ ] Reduce example count from <old> to <new>
- [ ] Consolidate similar examples
- [ ] Add missing edge cases

### Estimated Improvements
- Token reduction: <count> tokens (<percentage>%)
- Clarity score: +<points>
- Maintainability: +<points>

### Before/After Comparison

**Before (excerpt):**
```
<original problematic section>
```

**After (optimized):**
```
<optimized version>
```

**Savings:** <tokens> tokens, <improvement description>
```

## Concrete Example: Real Analysis

### Input Prompt (Fragment)
```markdown
You are a code reviewer. Your job is to review code and make sure it's good.
You should look at the code and find problems. When you find problems, you
should tell the user about them. Make sure to check for bugs and also check
for style issues. You should be thorough and careful. Don't miss anything
important. Always be professional and constructive in your feedback. Try to
help the developer improve. Make suggestions that are actually helpful and
not just critical. Be nice but also be honest. Make sure your reviews are
really good and comprehensive.
```

### Analysis Output

**Token Waste Analysis:**
```json
{
  "totalWords": 98,
  "totalTokens": 124,
  "redundancyScore": 45,
  "verbosityScore": 30,
  "issues": [
    {
      "type": "redundancy",
      "severity": "high",
      "examples": [
        "make sure" (3 occurrences),
        "you should" (4 occurrences),
        "be [adjective]" (3 occurrences)
      ]
    },
    {
      "type": "vague-instructions",
      "severity": "high",
      "examples": [
        "good", "thorough", "careful", "helpful",
        "important", "professional", "constructive"
      ]
    },
    {
      "type": "filler-words",
      "severity": "medium",
      "count": 8,
      "examples": ["really", "actually", "just"]
    }
  ]
}
```

**Optimization Recommendations:**
1. Remove repeated "you should" → use imperative mood
2. Replace vague terms with specific criteria
3. Consolidate feedback guidelines into structured list
4. Remove redundant emphasis phrases

### Optimized Output
```markdown
You are a code reviewer analyzing pull requests for quality and correctness.

Review Process:
1. Scan for logic errors, null checks, edge cases
2. Verify style compliance (linting, formatting)
3. Assess test coverage (>80% target)
4. Check documentation completeness

Feedback Format:
- Issue: [category] - [specific finding]
- Impact: [low/medium/high]
- Fix: [concrete suggestion with code example]

Tone: Professional, constructive, solution-focused
```

**Results:**
- Original: 124 tokens
- Optimized: 67 tokens
- Savings: 57 tokens (46% reduction)
- Clarity: Improved (specific criteria vs. vague terms)
- Actionability: Improved (structured process vs. general instructions)

## Integration with Development Workflow

### Pre-Publish Checklist
```bash
# 1. Analyze new skill
npx claude-flow@alpha hooks pre-task --description "Optimizing new skill prompt"

# 2. Run analysis (spawn analyzer agent)
# Agent performs full analysis as documented above

# 3. Review recommendations
npx claude-flow@alpha memory retrieve --key "optimization/recommendations"

# 4. Apply fixes
# Make recommended changes to skill

# 5. Re-analyze and verify improvements
# Re-run analysis, compare metrics

# 6. Store final metrics
npx claude-flow@alpha hooks post-task --task-id "skill-optimization"
```

## Success Metrics

- Token reduction: 20-50% typical
- Clarity score: +30-50 points
- Trigger precision: 90%+ accuracy
- Anti-pattern elimination: 100% high-severity
- Maintainability: Easier to update and extend

## Related Skills

- `when-analyzing-skill-gaps-use-skill-gap-analyzer` - Analyze overall library
- `when-managing-token-budget-use-token-budget-advisor` - Budget planning
- `prompt-architect` - Advanced prompt engineering

## Notes

- Run before publishing new skills
- Re-analyze periodically (monthly maintenance)
- Track improvements over time
- Share optimization patterns across team
- Update analysis scripts as new anti-patterns emerge
## Core Principles

Prompt Optimization Analyzer operates on 3 fundamental principles that maximize prompt effectiveness while minimizing token waste:

### Principle 1: Information Density Over Word Count
Every token in a prompt should carry actionable information. Verbose explanations, redundant phrases, and filler words waste token budget without improving outcomes. This analyzer prioritizes concise, high-information-density prompts that communicate precisely.

In practice:
- Replace vague terms ("good", "thorough", "appropriate") with specific criteria ("90% test coverage", "O(n log n) complexity")
- Remove filler words ("very", "really", "just", "actually") that add no semantic value
- Consolidate repeated phrases ("you should" appears 4 times) into single imperative statements
- Use structured lists instead of prose paragraphs for instructions
- Target 20-50% token reduction while maintaining or improving clarity
- Measure information density as meaningful directives per 100 tokens

### Principle 2: Specificity Beats Ambiguity
Generic instructions like "handle errors appropriately" leave room for interpretation and inconsistent execution. This analyzer detects ambiguous terminology and replaces it with concrete, measurable criteria that eliminate guesswork.

In practice:
- Define technical terms inline (don't assume shared vocabulary)
- Specify exact formats (JSON structure, file paths, naming conventions)
- Provide concrete examples showing the expected pattern, not just descriptions
- Replace modal verb ambiguity (10 "must" + 10 "should") with clear MUST vs SHOULD separation
- Include success criteria that can be objectively validated
- Ensure triggers use explicit "when" or "if" conditions, not vague scenarios

### Principle 3: Structural Clarity Through Organization
Well-organized prompts are easier to parse, reducing cognitive load and improving execution accuracy. This analyzer optimizes information architecture for logical flow and progressive disclosure.

In practice:
- Group related concepts into clear sections with descriptive headers
- Use hierarchy (H1, H2, H3) to show relationships between concepts
- Place critical instructions before optional details (progressive disclosure)
- Extract repetitive content into references to avoid duplication
- Use tables for multi-dimensional comparisons (anti-patterns, routing decisions)
- Maintain consistent formatting (code blocks, bullet lists, examples) throughout

## Common Anti-Patterns

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| **Vague Instructions** | Using subjective terms like "make it better", "handle appropriately", or "be thorough" without defining measurable criteria. Leads to inconsistent execution and unclear expectations. | Replace with specific, measurable criteria: "reduce token count by 20%", "catch exceptions and log to memory", "90% test coverage". Every directive should have an objective validation method. |
| **Redundancy Bloat** | Repeating the same phrase ("you should", "make sure") or concept multiple times throughout the prompt. Wastes tokens and adds no new information. | Use imperative mood instead of "you should" repetition. Consolidate similar instructions into single statements. Remove phrase repetition detected by analysis scripts. Target <10 redundancy score. |
| **Example Overload** | Providing 5-10 examples when 2-3 would suffice, or showing redundant variations of the same pattern. Bloats token count without improving understanding. | Include 2-3 diverse examples covering edge cases, not 10 similar ones. Consolidate examples showing the same pattern. Focus on illustrating different scenarios, not repetition for emphasis. |
| **Wall of Text** | Writing prompts as dense paragraphs without structure, lists, or examples. Reduces readability and increases cognitive load for parsing instructions. | Break into sections with clear headers. Use bullet lists for sequential steps. Include code examples in blocks. Add tables for multi-dimensional info. Structure improves both human and AI comprehension. |
| **Missing Context** | Referencing "the standard format" or "the usual approach" without defining what that means. Assumes shared knowledge that may not exist. | Define all technical terms inline. Specify exact formats with examples. Provide concrete templates rather than references to undefined standards. Make prompts self-contained. |
| **Over-Specification** | Providing excessive detail on trivial formatting choices while leaving critical logic undefined. Misallocates attention and token budget. | Focus token budget on critical logic and success criteria. Defer trivial details to configuration files (.editorconfig, linting rules). Specify "what" and "why", let tools handle "how" for formatting. |

## Conclusion

The Prompt Optimization Analyzer transforms prompt engineering from subjective writing to objective optimization. By detecting token waste, identifying anti-patterns, and generating concrete optimization recommendations, this skill ensures that prompts communicate effectively while respecting token budget constraints. The systematic analysis - token efficiency, anti-pattern detection, trigger analysis, structural optimization - provides actionable data for improving prompt quality across all skills.

The key insight demonstrated by the real-world example is dramatic: the original verbose prompt (124 tokens, vague instructions, repetitive phrases) was reduced to an optimized version (67 tokens, specific criteria, structured format) - a 46% reduction while significantly improving clarity and actionability. This pattern repeats across prompt optimization efforts: typical reductions of 20-50% with simultaneous clarity improvements. The analyzer's value lies not just in token savings, but in the forcing function to replace vague generalities with specific, measurable criteria.

Use this skill before publishing new skills or slash commands, during skill maintenance, or when prompts approach token budget limits. The pre-publish checklist ensures that skills go into production with optimized prompts rather than verbose first drafts. Remember: every token saved in prompts is budget available for execution. A well-optimized skill library with 20-50% token reduction across prompts can handle significantly more complex tasks within the same budget limits. Write less, communicate more, execute better.
