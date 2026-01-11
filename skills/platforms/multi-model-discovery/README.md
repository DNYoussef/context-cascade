# Multi-Model Discovery Skill

> Don't reinvent the wheel. Find existing solutions first.

## Quick Start

```bash
# Via delegate.sh
./scripts/multi-model/delegate.sh gemini "Find existing solutions for: {your goal}"

# Via router
./scripts/multi-model/multi-model-router.sh "Find existing solutions for X"

# Direct Gemini
bash -lc "gemini 'How do others implement {feature}? Find code examples and libraries.'"
```

## When to Use

- BEFORE implementing any new feature
- When researching best practices
- When evaluating libraries/frameworks
- When unsure if a problem has been solved

## When NOT to Use

- For implementation tasks (use codex-iterative-fix)
- When you know the solution exists locally
- For debugging (use smart-bug-fix)

## Files in This Skill

```
multi-model-discovery/
  SKILL.md           # Main skill definition
  ANTI-PATTERNS.md   # Common mistakes to avoid
  README.md          # This file
  examples/
    example-1-auth-discovery.md
    example-2-pdf-generation.md
```

## Integration

Works with:
- `codex-iterative-fix`: After discovery, for implementation
- `gemini-codebase-onboard`: For understanding existing codebase
- Memory-MCP: Store findings for future reference

## Memory Tags

Results stored with:
- WHO: multi-model-discovery
- WHY: avoid-reinvention
- Key pattern: `discovery/{domain}/{task_id}`
