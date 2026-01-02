# When Reviewing Code Comprehensively, Use Code Review Assistant

Router that ensures full code reviews run through the `code-review-assistant` SOP with constraint and confidence hygiene.

## Steps
1. Confirm the need is a comprehensive review (not just functionality or style).
2. Capture HARD / SOFT / INFERRED constraints (security, compliance, style, risk tolerance).
3. Invoke `code-review-assistant` with context and priorities.
4. Verify findings include evidence, severity, and confidence ceilings.
5. Summarize actions and store outputs.

Confidence: 0.80 (ceiling: inference 0.70) - based on validated routing and review outputs.
