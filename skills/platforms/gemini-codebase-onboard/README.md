# Gemini Codebase Onboard Skill

> Understand entire codebases in one pass with 1M token context.

## Quick Start

```bash
# Via delegate.sh
./scripts/multi-model/delegate.sh gemini "Map full architecture" --all-files

# Via gemini-yolo.sh
./scripts/multi-model/gemini-yolo.sh "Analyze architecture" task-id megacontext

# Via router
./scripts/multi-model/multi-model-router.sh "Map entire architecture"

# Direct Gemini
bash -lc "gemini --all-files 'Analyze entire codebase and document architecture'"
```

## Context Window Specs

| Metric | Value |
|--------|-------|
| Capacity | 1 million tokens |
| Equivalent | ~1,500 pages |
| Lines of Code | ~30,000 LOC |
| Best for | Projects under 30K LOC |

## When to Use

- Onboarding to new codebase
- Understanding full architecture
- Mapping dependencies
- Finding patterns/anti-patterns
- Migration planning
- Security audits

## When NOT to Use

- Single file work (use Claude)
- Complex reasoning (Claude is better)
- Writing new features (Gemini loops)
- Iterative refinement (use Codex)

## Files in This Skill

```
gemini-codebase-onboard/
  SKILL.md           # Main skill definition
  ANTI-PATTERNS.md   # Common mistakes to avoid
  README.md          # This file
  examples/
    example-1-new-project.md
    example-2-security-audit.md
```

## Query Patterns

```bash
# Architecture
gemini --all-files "Document the full system architecture"

# Dependencies
gemini --all-files "Create a dependency graph"

# Patterns
gemini --all-files "Identify design patterns and assess consistency"

# API Documentation
gemini --all-files "Document all API endpoints"
```

## Limitations (Real Feedback)

- May generate errors (missing XML tags)
- Can get stuck in loops fixing mistakes
- Switches to Flash model after 5 minutes
- Slower than Claude for complex reasoning
- Not great for implementation

## Strengths

- Excellent breadth of analysis
- Can summarize entire folders
- Great for onboarding/auditing
- Powerful architectural understanding

## Memory Tags

Results stored with:
- WHO: gemini-megacontext
- WHY: codebase-analysis
- Key pattern: `multi-model/gemini/onboard/{project}/{task_id}`
