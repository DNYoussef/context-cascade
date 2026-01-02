# Utility: PPTX Generation

Use this wrapper when the user needs a slide deck. It collects the brief and routes to `pptx-generation`.

## Steps
1. Capture audience, goal, brand kit, slide count, and deadline.
2. Call `pptx-generation` with the structured brief.
3. Share outline/deck output, validation notes, and `Confidence: X.XX (ceiling: TYPE Y.YY)`.
4. Tag memory for traceability.

Guardrails: enforce brand/accessibility constraints and follow Prompt Architect constraint ordering.
