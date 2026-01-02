---
name: when-setting-network-security-use-network-security-setup
description: Specialized entry that routes network security requests to the network-security-setup SOP with scoped allowlists and TLS posture.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
x-version: 3.2.0
x-category: security
x-vcl-compliance: v3.1.1
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

## Purpose
Activate the `network-security-setup` workflow for deny-by-default policies, trusted allowlists, and TLS hardening, following **skill-forge** structure-first and **prompt-architect** constraint/confidence practices.

## SOP (Routing)
1. **Scope**: Capture HARD/SOFT/INFERRED constraints (environments, allowed domains/IPs, proxy needs, TLS requirements).
2. **Safety**: Require authorization, change log, and isolation; avoid scanning unknown targets.
3. **Execute**: Invoke `network-security-setup`; tag MCP (`WHO=network-security-setup-{session}`, `WHY=skill-execution`).
4. **Validate**: Test allowed vs. blocked connectivity and TLS posture; attach evidence with confidence ceilings.
5. **Deliver**: Policy pack + validation log stored at `skills/security/specialized-tools/when-setting-network-security-use-network-security-setup/{project}/{timestamp}`.

## Output Format
- Scope/constraints table, routed actions, validation summary, and confidence line.

Confidence: 0.70 (ceiling: inference 0.70) - Routing skill synced with the updated network-security-setup SOP.
