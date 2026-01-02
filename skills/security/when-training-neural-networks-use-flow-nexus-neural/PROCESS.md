# Flow Nexus Neural Training Process

## Inputs
- Authorization, data classification/licensing, objectives, and environment.
- Constraints: compute budget, timeline, safety requirements, and allowed tools.

## Steps
1. **Scope & Safety**
   - Capture HARD/SOFT/INFERRED constraints (per prompt-architect).
   - Select sandbox/network profile; tag MCP (`WHO=flow-nexus-neural-{session}`, `WHY=skill-execution`).
2. **Plan**
   - Choose workflow (train/fine-tune/eval), model family, resources, checkpoints, and data ingress/egress controls.
   - Define encryption, retention, and key management.
3. **Execute**
   - Run Flow Nexus neural pipeline; monitor metrics and resource usage.
4. **Validate**
   - Safety/adversarial checks, PII leakage checks, and license compliance verification.
   - Confidence ceilings attached to findings/metrics.
5. **Deliver**
   - Training summary, artifacts, evaluation metrics, risks, and mitigations archived at `skills/security/when-training-neural-networks-use-flow-nexus-neural/{project}/{timestamp}`.

Confidence: 0.70 (ceiling: inference 0.70) - Process aligned to skill-forge structure and prompt-architect constraint handling.
