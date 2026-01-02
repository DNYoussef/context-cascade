---
name: reverse-engineering-deep-analysis
description: Extended deep-dive reverse engineering with advanced tracing, deobfuscation, and exploit validation.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
x-version: 3.2.0
x-category: security
x-vcl-compliance: v3.1.1
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

## Purpose
Perform extended, high-effort reverse engineering that blends static/dynamic/symbolic analysis and deobfuscation to reach hard paths and validate exploitability. Built on **skill-forge** structure-first rules and **prompt-architect** explicit constraints/confidence ceilings.

## Use When / Redirect When
- **Use when:** complex obfuscation, layered packers, VM-based protections, or exploit research requiring end-to-end proof.
- **Redirect when:** firmware focus (`reverse-engineering-firmware`), quick IOC triage (`reverse-engineering-quick`), or lighter triage (`reverse-engineer-debug`).

## Guardrails
- Isolated sandboxes with snapshots; controlled network (block or explicit allowlist).
- Preserve chain-of-custody (hashes, timestamps, env/tool versions).
- Avoid external service uploads without approval.
- Confidence ceilings enforced (inference/report ≤0.70, research 0.85, observation/definition 0.95).

## Prompt Architecture Overlay
1. HARD/SOFT/INFERRED constraints (arch, protections, goals, time/effort budget, tooling).
2. Two-pass refinement: structure → epistemic.
3. English-only output with explicit confidence line.

## SOP (Extended Deep Loop)
1. **Scope & Toolchain**: Confirm authorization, hashes, targets, and success criteria; select deobfuscation, unpacking, tracing, and symbolic tools.
2. **Preparation**: Detect packers/anti-debug/VM tricks; set breakpoints/hooks; craft harnesses and inputs.
3. **Execution**: Iteratively unpack/decrypt stages, trace control/data flows, and capture memory dumps.
4. **Exploit Research**: Validate reachability, build PoCs, and map mitigations (ASLR/DEP/CFI).
5. **Validation & Delivery**: Cross-check across methods; provide IOC set, exploitability verdict, mitigations, and archive artifacts at `skills/security/reverse-engineering-extended/reverse-engineering-deep-analysis/{project}/{timestamp}` with MCP tags (`WHO=reverse-engineering-deep-analysis-{session}`, `WHY=skill-execution`).

## Deliverables
- Detailed analysis report, PoCs (where permitted), IOC inventory, and mitigation guidance.
- Evidence bundle (traces, dumps with hashes, configs, tool versions).

## Quality Gates
- Structure-first documentation; missing resources/examples/tests tracked.
- Safety controls verified; dual validation for critical conclusions.
- Confidence ceilings stated for each claim; chain-of-custody recorded.

## Anti-Patterns
- Skipping unpacking validation; trusting single-tool results.
- Executing with open network access.
- Claiming exploitability without demonstrated reach.

## Output Format
- Scope + constraints table (HARD/SOFT/INFERRED).
- Findings, PoCs, and IOCs with evidence.
- Mitigations and validation log.
- Confidence line: `Confidence: X.XX (ceiling: TYPE Y.YY) - reason`.

Confidence: 0.72 (ceiling: inference 0.70) - Extended deep analysis aligned with skill-forge and prompt-architect standards.
