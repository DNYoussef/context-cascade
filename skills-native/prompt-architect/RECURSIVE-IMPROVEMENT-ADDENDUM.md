# Prompt Architect - Recursive Improvement Addendum

## Purpose

This addendum connects **prompt-architect** (Phase 2 in 5-phase workflow) with the **Recursive Self-Improvement System**.

## Distinction: prompt-architect vs prompt-forge

| Aspect | prompt-architect | prompt-forge |
|--------|------------------|--------------|
| **Purpose** | Optimize USER prompts for better AI responses | Self-improve SYSTEM prompts and skills |
| **Target** | User-provided prompts | Internal skills, agents, expertise |
| **Scope** | Single-use optimization | Recursive improvement loop |
| **Output** | Improved user prompt | Proposals + diffs + eval results |
| **Gate** | None (direct use) | Frozen eval harness |

## When to Use Which

```
USER wants better prompt output
  -> Use prompt-architect (Phase 2)
  -> Optimizes their prompt
  -> Returns improved prompt

SYSTEM wants to improve itself
  -> Use prompt-forge (recursive improvement)
  -> Analyzes internal skills/prompts
  -> Generates proposals
  -> Tests against eval harness
  -> Commits if improved
```

## Integration Points

### prompt-architect as Improvement Target

prompt-architect itself can be improved by the recursive loop:

```yaml
improvement_cycle:
  target: "prompt-architect/SKILL.md"

  process:
    - step: "prompt-auditor analyzes prompt-architect"
      checks:
        - technique_coverage
        - failure_handling
        - clarity

    - step: "prompt-forge generates proposals"
      areas:
        - "Add uncertainty handling section"
        - "Enhance anti-pattern detection"

    - step: "skill-forge applies proposals"
      output: "prompt-architect-v{N+1}"

    - step: "eval-harness tests"
      benchmark: "prompt-generation-benchmark-v1"
      regression: "prompt-forge-regression-v1"

    - step: "If improved: commit"
```

### prompt-architect Informing prompt-forge

The techniques in prompt-architect are USED BY prompt-forge:

```yaml
technique_usage:
  self_consistency:
    in_prompt_architect: "Teaching users to apply"
    in_prompt_forge: "Applied when generating proposals"

  program_of_thought:
    in_prompt_architect: "Teaching users to structure"
    in_prompt_forge: "Used in improvement analysis"

  plan_and_solve:
    in_prompt_architect: "Teaching users to separate phases"
    in_prompt_forge: "Core of improvement cycle"
```

## Dual Role Architecture

```
                    +-------------------+
                    |   User Request    |
                    +-------------------+
                            |
                            v
                    +-------------------+
                    | Phase 2: prompt-  |
                    |     architect     |  <-- For USER prompts
                    +-------------------+
                            |
                            v
                    +-------------------+
                    | Optimized Prompt  |
                    +-------------------+

                           ---

                    +-------------------+
                    | Self-Improvement  |
                    |     Request       |
                    +-------------------+
                            |
                            v
                    +-------------------+
                    |   prompt-forge    |  <-- For SYSTEM self-improvement
                    +-------------------+
                            |
                            v
                    +-------------------+
                    |   eval-harness    |
                    +-------------------+
                            |
                            v
                    +-------------------+
                    |  Improved System  |
                    +-------------------+
```

## Cross-Pollination

Improvements discovered in prompt-forge can inform prompt-architect:

```yaml
cross_pollination:
  direction: "prompt-forge -> prompt-architect"

  mechanism:
    - "When prompt-forge discovers effective technique"
    - "Document in prompt-forge learnings"
    - "prompt-auditor flags for prompt-architect update"
    - "Run improvement cycle on prompt-architect"
    - "Add technique to user-facing skill"

  example:
    discovery: "Self-consistency with 3 perspectives optimal"
    current: "Consider multiple perspectives"
    proposed: "Consider exactly 3 perspectives: analytical, practical, contrarian"
    gate: "Must pass prompt-generation-benchmark-v1"
```

## Shared Techniques Reference

Both skills use these evidence-based techniques:

| Technique | In prompt-architect | In prompt-forge |
|-----------|---------------------|-----------------|
| Self-Consistency | Teaching to users | Applied in proposal generation |
| Program-of-Thought | Teaching to users | Applied in analysis |
| Plan-and-Solve | Teaching to users | Core cycle structure |
| Few-Shot | Teaching to users | Used in examples |
| Chain-of-Thought | Teaching to users | Applied in rationale |
| Uncertainty Handling | Should teach | CRITICAL for proposals |

## Feedback Loop

```
prompt-architect (teaches techniques)
       |
       v
Users apply techniques
       |
       v
prompt-forge improves prompt-architect
       |
       v
Better technique teaching
       |
       v
Better user outcomes
       |
       v
(cycle continues)
```

## Memory Namespaces

| Namespace | Purpose |
|-----------|---------|
| `prompt-architect/sessions/{id}` | User optimization sessions |
| `prompt-forge/proposals/{id}` | Self-improvement proposals |
| `improvement/audits/prompt-architect` | Audits of prompt-architect |
| `improvement/cycles/prompt-architect` | Improvement cycles run |

## Usage in 5-Phase Workflow

```
Phase 1: intent-analyzer
  -> Detects: "optimize my prompt" vs "improve system"

Phase 2: prompt-architect (USER prompts)
  -> IF intent = "optimize my prompt"
  -> Apply evidence-based techniques
  -> Return improved prompt

Phase 2-ALT: prompt-forge (SYSTEM prompts)
  -> IF intent = "improve system"
  -> Analyze target skill/prompt
  -> Generate proposals
  -> Gate through eval-harness
```

---

**Version**: 2.1.0
**Last Updated**: 2025-12-15
**Key Insight**: prompt-architect teaches, prompt-forge applies (and improves the teacher)
