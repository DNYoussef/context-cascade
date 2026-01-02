# Process

1. Verify the request involves suspected fake/non-executable code; reroute if not.
2. Bucket constraints into HARD / SOFT / INFERRED (must-run requirements, environments, risk tolerance, audience).
3. Execute `theater-detection` with the code, expected behavior, and environment details.
4. Capture findings with repro steps/evidence and explicit confidence ceilings.
5. Recommend actions and store artifacts for traceability.

Confidence: 0.80 (ceiling: inference 0.70) - reflects validated theater-detection flow.
