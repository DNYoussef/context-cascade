# Reverse Engineering Firmware

## Purpose
Securely extract and analyze embedded/IoT firmware images. Follows **skill-forge** structure-first standards and **prompt-architect** explicit constraints/confidence ceilings.

## Quick Flow
1. **Scope & Safety**: Authorization, hashes, device/model/arch, and isolation plan.
2. **Extract**: Use binwalk/dd to unpack; identify partitions and file systems; rebuild read-only.
3. **Analyze**: Search for credentials/keys/endpoints, review init/startup scripts, map attack surface and update paths.
4. **Emulate (if allowed)**: qemu/chroot in isolation; capture logs/traces and service behavior.
5. **Deliver**: Findings mapped to CVE/CWE/OWASP IoT, SBOM, remediation plan, and evidence stored at `skills/security/reverse-engineering-firmware/{project}/{timestamp}` with MCP tags (`WHO=reverse-engineering-firmware-{session}`, `WHY=skill-execution`).

## Guardrails
- Authorized firmware only; respect licensing/export controls.
- Isolated environments; never flash production hardware.
- Sanitize secrets; no external uploads without approval.
- Evidence + confidence ceiling for each claim.

## Outputs
- Firmware report, SBOM, IOC/high-level indicators, and remediation guidance.
- Evidence bundle (hashes, extraction logs, configs) with timestamps.

Confidence: 0.71 (ceiling: inference 0.70) - README aligned to the updated firmware SOP.
