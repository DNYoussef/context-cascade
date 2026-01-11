# Multi-Model Discovery Anti-Patterns

## Anti-Pattern 1: Skipping Discovery Phase

**Problem**: Jumping straight to implementation without checking for existing solutions.

```text
BAD:
User: "Implement rate limiting"
Agent: [starts writing custom rate limiter from scratch]

GOOD:
User: "Implement rate limiting"
Agent: [first queries Gemini for existing solutions]
gemini "What are best practices for rate limiting in Node.js? Find existing libraries."
```

**Why it matters**: Reinventing the wheel wastes time and often produces inferior solutions.

## Anti-Pattern 2: Too Broad Queries

**Problem**: Vague queries that return generic results.

```text
BAD:
gemini "How do I do auth?"

GOOD:
gemini "What are best practices for JWT authentication in Express.js?
Find existing libraries and code examples for refresh token rotation."
```

**Why it matters**: Specific queries return actionable results.

## Anti-Pattern 3: Not Capturing Results

**Problem**: Using Gemini but not storing findings for future reference.

```text
BAD:
[Run Gemini query]
[Immediately implement without documenting findings]

GOOD:
[Run Gemini query]
[Store results in Memory-MCP with tags]
[Document build vs buy decision]
[Then implement]
```

**Why it matters**: Lost knowledge means repeated research.

## Anti-Pattern 4: Trusting Without Verification

**Problem**: Blindly trusting Gemini's recommendations without validation.

```text
BAD:
Gemini: "Use library X"
Agent: [immediately installs library X]

GOOD:
Gemini: "Use library X"
Agent: [checks npm downloads, GitHub stars, last update, security advisories]
Agent: [evaluates fit for project requirements]
Agent: [then decides]
```

**Why it matters**: Not all recommendations fit your specific context.

## Anti-Pattern 5: Discovery as Procrastination

**Problem**: Endless research without moving to implementation.

```text
BAD:
[Research option A]
[Research option B]
[Research option C]
[Research option D]
[Still researching...]

GOOD:
[Research top 2-3 options]
[Make decision with available evidence]
[Start implementation]
[Iterate if needed]
```

**Why it matters**: Diminishing returns on research time.

## Anti-Pattern 6: Using for Implementation

**Problem**: Using discovery skill for actual coding tasks.

```text
BAD:
Skill("multi-model-discovery")
Task: "Fix the failing tests"

GOOD:
Skill("multi-model-discovery")
Task: "Find existing testing patterns for React hooks"
THEN
Skill("codex-iterative-fix")
Task: "Fix the failing tests using discovered patterns"
```

**Why it matters**: Use the right tool for the job.

## Recovery Protocol

If you find yourself in an anti-pattern:

1. STOP current action
2. Document what went wrong
3. Apply correct pattern
4. Store lesson in Memory-MCP for future reference
