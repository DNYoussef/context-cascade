# Utility: Prompt Architect

Wrapper for routing prompt-optimization requests to `prompt-architect`.

## Steps
1. Capture the original prompt, goals, constraints, and missing context.
2. Invoke `prompt-architect` and request explicit confidence ceiling.
3. Share optimized prompt and constraint list with `Confidence: X.XX (ceiling: TYPE Y.YY)`.
4. Tag memory for reuse.

Guardrails: keep outputs English-only; enforce confidence ceilings and constraint clarity.
