---
name: reverse-engineer-debug
description: Rapid triage and debug of binaries or artifacts with static + light dynamic analysis for safe insights.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
x-version: 3.2.0
x-category: security
x-vcl-compliance: v3.1.1
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

## Purpose
Provide quick-turn reverse engineering triage (strings, headers, symbols, lightweight emulation) to answer “what is this binary doing?” without deep instrumentation. Aligns with **skill-forge** structure-first and **prompt-architect** constraint/evidence rules.

## Use When / Redirect When
- **Use when:** you need rapid classification, capability hints, or safe behavior summaries.
- **Redirect when:** deep dynamic work (`reverse-engineering-deep`), firmware (`reverse-engineering-firmware`), or quick IOC-only triage (`reverse-engineering-quick`).

## Guardrails
- Analyze only in isolated sandboxes with no production connectivity.
- Never execute unknown binaries outside instrumentation; prefer emulation/snapshots.
- Strip/neutralize secrets; avoid uploading malware to third-party services.
- Confidence ceilings: inference/report ≤0.70, research 0.85, observation/definition 0.95.

## Prompt Architecture Overlay
1. HARD/SOFT/INFERRED constraints (platform, architecture, goals, allowed tooling, time budget).
2. Two passes: structure (coverage, safety) then epistemic (evidence, ceilings).
3. English-only output with explicit confidence line.

## SOP (Triage Loop)
1. **Scope & Safety**
   - Confirm authorization, sample hashes, and isolation settings.
   - Select toolchain (strings, objdump, yara, ghidra-lite, qemu/strace in safe mode).
2. **Static Recon**
   - Identify format/arch, imports/exports, packers/obfuscation, and suspicious strings/URLs.
   - Run YARA/signature checks and entropy/section analysis.
3. **Light Dynamic**
   - Use emulation or sandboxed execution with blocked network; capture syscalls, file/registry/process activity.
   - Stop if behavior exceeds scope (spawn self-modifying code, persistence attempts).
4. **Assessment**
   - Summarize capabilities, indicators (IOCs), and risk level.
   - Recommend next steps (deep analysis, memory dump, firmware path).
5. **Validation & Delivery**
   - Cross-check static vs. dynamic observations; ensure evidence per claim.
   - Archive artifacts under `skills/security/reverse-engineer-debug/{project}/{timestamp}` with MCP tags (`WHO=reverse-engineer-debug-{session}`, `WHY=skill-execution`).

## Deliverables
- Capability summary, IOC list (hashes/domains/paths), and risk assessment.
- Evidence bundle (tool outputs, hashes, logs) with timestamps.
- Recommended follow-up (e.g., deep analysis, detonation plan).

## Quality Gates
- Structure-first documentation; missing resources/examples/tests noted for follow-up.
- Evidence attached to every claim; confidence ceiling stated.
- Safety controls verified (network blocked or allowlisted, snapshots taken).
- Triaged within agreed time budget; escalation path documented.

## Anti-Patterns
- Running unknown binaries with unrestricted network access.
- Publishing results without hashes or evidence.
- Overstating confidence beyond ceiling.
- Skipping routing to deeper skills when needed.

## Output Format
- Scope + constraints table (HARD/SOFT/INFERRED).
- Findings (static + light dynamic) with evidence and IOCs.
- Next-step recommendations and safety notes.
- Confidence line: `Confidence: X.XX (ceiling: TYPE Y.YY) - reason`.

Confidence: 0.71 (ceiling: inference 0.70) - Triage SOP rebuilt with skill-forge structure and prompt-architect constraint discipline.
