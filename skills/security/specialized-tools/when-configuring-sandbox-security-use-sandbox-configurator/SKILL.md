---
name: when-configuring-sandbox-security-use-sandbox-configurator
description: Specialized entry that routes sandbox security requests to the sandbox-configurator SOP with clear scope and safety controls.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
x-version: 3.2.0
x-category: security
x-vcl-compliance: v3.1.1
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

## Purpose
Activate the `sandbox-configurator` workflow for sandbox policy design (filesystem, network, secrets, observability) using **skill-forge** structure-first and **prompt-architect** constraint/confidence rules.

## SOP (Routing)
1. **Scope**: Capture HARD/SOFT/INFERRED constraints (runtime, mounts, network needs, secrets, observability).
2. **Safety**: Require isolation, deny-by-default network, secure secret handling, and rollback plan.
3. **Execute**: Invoke `sandbox-configurator` SOP; record MCP tags (`WHO=sandbox-configurator-{session}`, `WHY=skill-execution`).
4. **Validate**: Ensure allowed workflows pass and blocked paths fail; attach evidence with confidence ceilings.
5. **Deliver**: Policy pack + validation log archived under `skills/security/specialized-tools/when-configuring-sandbox-security-use-sandbox-configurator/{project}/{timestamp}`.

## Output Format
- Scope/constraints table, routed actions, validation summary, and confidence line.

Confidence: 0.70 (ceiling: inference 0.70) - Routing skill synced with updated sandbox-configurator SOP.
