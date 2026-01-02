# Reverse Engineering Firmware Analysis (Extended)

## Purpose
Deep firmware analysis for embedded/IoT images with extraction, attack-surface mapping, and emulation-based validation. Built with **skill-forge** structure-first expectations and **prompt-architect** explicit constraints/confidence ceilings.

## Quick Flow
1. **Scope & Safety**: Authorization, hashes, device/model/arch, objectives; isolate with snapshots.
2. **Extract & Map**: Unpack partitions, identify file systems/startup flows, and map services/update channels.
3. **Review**: Search for credentials/keys/endpoints, unsafe defaults, crypto misuse, outdated components (CVE mapping).
4. **Emulate (if allowed)**: qemu/chroot service runs with logging/tracing; validate persistence/update behavior.
5. **Deliver**: Firmware report, SBOM, remediation plan, and evidence archived at `skills/security/reverse-engineering-extended/reverse-engineering-firmware-analysis/{project}/{timestamp}` with MCP tags (`WHO=reverse-engineering-firmware-analysis-{session}`, `WHY=skill-execution`).

## Guardrails
- Authorized firmware only; respect licensing/export rules.
- Isolation and snapshots required; no production flashing.
- Evidence + confidence ceiling for every claim; dual validation for critical items.

Confidence: 0.71 (ceiling: inference 0.70) - README aligned to the extended firmware SOP.
