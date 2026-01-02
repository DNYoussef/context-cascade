# When Validating Code Works, Use Functionality Audit

Router ensuring functional validation requests leverage the `functionality-audit` SOP with constraint and confidence hygiene.

## Steps
1. Confirm the need is functionality validation; reroute otherwise.
2. Capture HARD / SOFT / INFERRED constraints (coverage, environments, inputs, latency).
3. Run `functionality-audit` with scenarios, expected behaviors, and environments.
4. Collect findings with repro steps, evidence, and confidence ceilings.
5. Summarize remediation actions and store outputs.

Confidence: 0.81 (ceiling: observation 0.95) - based on validated functional checks.
