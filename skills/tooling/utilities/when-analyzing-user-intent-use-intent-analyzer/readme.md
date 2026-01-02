# Utility: Intent Analyzer

Use this wrapper when a request needs clarification or routing before execution.

## Steps
1. Capture the raw ask and context.
2. Invoke `intent-analyzer` to extract intent, constraints, and success criteria.
3. Return recommended skill and confidence line `Confidence: X.XX (ceiling: TYPE Y.YY)`.
4. Tag memory for traceability.

Guardrails: keep outputs in English, avoid overconfident routing, and follow Prompt Architect constraint order.
