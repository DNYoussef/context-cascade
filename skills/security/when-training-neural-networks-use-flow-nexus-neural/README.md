# When Training Neural Networks, Use Flow Nexus Neural

## Purpose
Route ML training/fine-tuning requests through the secure Flow Nexus neural pipeline with sandboxing, data governance, and safety checks. Uses **skill-forge** structure-first discipline and **prompt-architect** explicit constraints/confidence ceilings.

## Quick Flow
1. **Intake**: Authorization, data classification/licensing, objectives (train/fine-tune/eval), and environment.
2. **Plan**: Select Flow Nexus neural workflow, resources, checkpoints, and data ingress/egress controls.
3. **Execute**: Run pipeline in isolated/sandboxed environment with deny-by-default networking and encrypted storage.
4. **Validate**: Review logs/metrics, run safety/adversarial checks, and confirm no PII leakage or license violations.
5. **Deliver**: Training summary, artifact locations, evaluation metrics, and risks. Archive at `skills/security/when-training-neural-networks-use-flow-nexus-neural/{project}/{timestamp}` with MCP tags (`WHO=flow-nexus-neural-{session}`, `WHY=skill-execution`).

## Guardrails
- Approved data only; verify provenance and licensing.
- Isolated compute with controlled network; protect secrets and keys.
- Evidence + confidence ceiling for every claim; safety evals required.

Confidence: 0.70 (ceiling: inference 0.70) - README aligned to the Flow Nexus neural routing SOP.
