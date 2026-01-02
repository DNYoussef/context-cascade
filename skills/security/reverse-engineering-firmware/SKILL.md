---
name: reverse-engineering-firmware
description: Firmware-focused reverse engineering for embedded/IoT images with extraction, partition analysis, and secure handling.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
x-version: 3.2.0
x-category: security
x-vcl-compliance: v3.1.1
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

## Purpose
Analyze firmware images (routers/IoT/embedded) to extract file systems, configs, and vulnerabilities. Built with **skill-forge** structure-first discipline and **prompt-architect** constraint/confidence hygiene.

## Use When / Redirect When
- **Use when:** handling BIN/IMG/IPK/UPK firmware for security review, vulnerability hunting, or SBOM extraction.
- **Redirect when:** generic binaries (`reverse-engineer-debug`/`-deep`) or quick IOC triage (`reverse-engineering-quick`).

## Guardrails
- Authorized hardware/firmware only; respect licensing and export controls.
- Work in isolated environments; never flash to production devices.
- Sanitize secrets; avoid external uploads without approval.
- Confidence ceilings enforced (inference/report ≤0.70, research 0.85, observation/definition 0.95).

## Prompt Architecture Overlay
1. HARD/SOFT/INFERRED constraints (device model, architecture, target findings, tool allowlist).
2. Two-pass refinement: structure (coverage + safety) then epistemic (evidence + ceilings).
3. English-only output with explicit confidence line.

## SOP (Firmware Loop)
1. **Scope & Preparation**
   - Confirm authorization, obtain hashes, and identify format/architecture.
   - Gather available docs/bootloader info; set isolated workspace.
2. **Extraction**
   - Use binwalk/dd to extract partitions; identify file systems (squashfs/ubifs/jffs2).
   - Rebuild file systems read-only; catalog binaries/configs/scripts.
3. **Static Analysis**
   - Search for credentials/keys, hardcoded endpoints, and unsafe services.
   - Review init scripts/startup flows; map attack surface (ports, daemons, update paths).
4. **Dynamic/Emulation (if allowed)**
   - Emulate with qemu/chroot; monitor network/IPC/filesystem changes in isolation.
   - Capture logs/traces for services; test update/rollback paths safely.
5. **Validation & Delivery**
   - Cross-check static vs. dynamic findings; map to CVE/CWE/OWASP IoT.
   - Deliver report, IOC set, remediation plan, and SBOM; archive to `skills/security/reverse-engineering-firmware/{project}/{timestamp}` with MCP tags (`WHO=reverse-engineering-firmware-{session}`, `WHY=skill-execution`).

## Deliverables
- Firmware report (attack surface, findings, CVE/CWE map) and SBOM.
- Evidence bundle (extraction logs, configs, hashes) with timestamps.
- Remediation and hardening recommendations; safe update/rollback guidance.

## Quality Gates
- Structure-first documentation; missing resources/examples/tests noted for backlog.
- Chain-of-custody recorded (hashes, env, tools).
- Evidence + confidence ceiling per claim; dual validation for critical/high.
- No dynamic execution without isolation and approval.

## Anti-Patterns
- Flashing unknown firmware to production hardware.
- Publishing secrets or proprietary code.
- Assuming architecture without verification.
- Skipping SBOM or attack-surface mapping.

## Output Format
- Scope + constraints table (HARD/SOFT/INFERRED).
- Extraction summary, findings (with evidence), and SBOM/high-level IOCs.
- Remediation and validation log.
- Confidence line: `Confidence: X.XX (ceiling: TYPE Y.YY) - reason`.

Confidence: 0.72 (ceiling: inference 0.70) - Firmware SOP rebuilt with skill-forge structure and prompt-architect constraint handling.
