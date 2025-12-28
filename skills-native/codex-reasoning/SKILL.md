---
name: codex-reasoning
description: Get alternative perspectives from GPT-5-Codex - second opinions on architecture and algorithms
allowed-tools: Bash, Read, Write, TodoWrite
---

# Codex Reasoning Skill

## Purpose

Leverage GPT-5-Codex's different reasoning patterns to get alternative perspectives, second opinions, and specialized algorithmic solutions.

## Unique Capability

**What This Adds**: Different AI reasoning:
- GPT-5-Codex optimized for agentic coding
- Different algorithmic approaches
- Alternative architecture perspectives
- Fast one-shot reasoning

## When to Use

### Perfect For:
- Getting second opinion on architecture
- Exploring alternative implementations
- Algorithmic optimization problems
- When stuck (different perspective helps)
- Comparing solution approaches
- Performance-critical algorithms

### Don't Use When:
- Claude's solution is clearly working
- Simple tasks (no need for alternatives)
- Consistency with existing Claude code matters

## Usage

```bash
# Second opinion
/codex-reasoning "What's an alternative approach to user authentication?"

# Algorithm comparison
/codex-reasoning "Optimize this sorting algorithm for large datasets"

# Architecture alternative
/codex-reasoning "What's an alternative to microservices for our scale?"
```

## CLI Command

```bash
codex
> /model gpt-5-codex
> "Your reasoning question"

# Or directly
codex "What's an alternative approach to X?"
```

## Why Use Both Models?

| Aspect | Claude | GPT-5-Codex |
|--------|--------|-------------|
| Deep reasoning | Excellent | Good |
| One-shot prompting | Good | Excellent |
| Documentation | Excellent | Good |
| Fast prototyping | Good | Excellent |
| Algorithm alternatives | Good | Excellent |

## Real Example

```
Architecture Decision:
- Claude suggests: Event-driven with message queue
- GPT-5-Codex suggests: REST with polling + webhooks

Result: Hybrid approach combining benefits of both
```

## Integration Pattern

```javascript
// Get both perspectives
const claudeApproach = await claudeArchitect("Design auth system");
const codexApproach = await codexReasoning("Alternative auth approach?");

// Use LLM Council for consensus
const consensus = await llmCouncil(`
  Claude: ${claudeApproach}
  Codex: ${codexApproach}
  Which is better for our use case?
`);
```

## Memory Integration

- Key: `multi-model/codex/reasoning/{task_id}`
- Tags: WHO=codex-cli:reasoning, WHY=alternative-perspective
