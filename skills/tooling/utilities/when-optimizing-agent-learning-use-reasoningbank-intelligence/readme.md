# Utility: Agent Learning (ReasoningBank Intelligence)

Wrapper for routing learning-improvement requests to `reasoningbank-intelligence`.

## Steps
1. Capture target agent, goals, datasets, and constraints.
2. Invoke `reasoningbank-intelligence` with context and eval requirements.
3. Share plan/results plus `Confidence: X.XX (ceiling: TYPE Y.YY)`.
4. Tag memory for traceability.

Guardrails: avoid overclaiming without evidence; follow Prompt Architect constraint ordering.
