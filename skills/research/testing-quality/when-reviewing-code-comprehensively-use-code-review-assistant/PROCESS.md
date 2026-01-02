# Process

1. Determine if the request requires a comprehensive code review; reroute if not.
2. Capture constraints (HARD / SOFT / INFERRED) including security, compliance, style, and risk tolerance.
3. Run `code-review-assistant` with the context, scope, and constraints.
4. Collect findings with evidence, severity, and explicit confidence ceilings.
5. Summarize remediation actions with owners and store artifacts.

Confidence: 0.80 (ceiling: inference 0.70) - reflects the validated routing and review flow.
