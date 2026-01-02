# Process – Intent Analyzer Utility

1. Detect if the request needs intent analysis (ambiguity, routing, missing constraints).
2. Collect context (domain, urgency, constraints already known).
3. Call `intent-analyzer` with the request and context; require confidence ceiling.
4. Relay outputs: intent classification, constraints, recommended skill, open questions.
5. Store summary with WHO/WHY/PROJECT/WHEN tags.

Confidence: 0.70 (ceiling: inference 0.70).
