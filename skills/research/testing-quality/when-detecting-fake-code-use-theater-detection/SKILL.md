---
name: when-detecting-fake-code-use-theater-detection
description: Route suspected fake or theatrical code to the theater-detection skill with clear constraints and evidence.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
x-version: 3.2.0
x-category: research
x-vcl-compliance: v3.1.1
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

## STANDARD OPERATING PROCEDURE

### Purpose
- Detect fake, non-executable, or theatrical code by invoking `theater-detection` with proper guardrails.

### Trigger Conditions
- **Positive:** suspicion of fabricated code snippets, demos that may not run, or hallucinated APIs.
- **Negative:** normal code review or functionality checks (use other sub-skills).

### Guardrails
- Constraints bucketed: HARD (must-run, environment), SOFT (style expectations), INFERRED (risk tolerance, audience).
- Two-pass loop: identify and route → validate evidence and ceilings from detection.
- Findings must include reproduction attempts and explicit confidence ceilings.

### Inputs
- Code snippet or repo, expected behavior/environment, and suspected issues.

### Workflow
1. **Scope & Route**: Confirm theater/fake-code concern; capture constraints.
2. **Invoke Theater-Detection**: Provide code, environment, and expectations.
3. **Validate Findings**: Look for non-existent APIs, missing deps, inconsistencies; ensure evidence and ceilings.
4. **Report & Store**: Summarize risks, repro steps, and actions; archive outputs.

### Validation & Quality Gates
- Routing decision documented; constraints captured.
- Findings include concrete evidence of fakery or confirmation of validity.
- Confidence ceilings aligned to evidence type.

### Response Template
```
**Routing**: Using theater-detection because ...
**Constraints**: HARD / SOFT / INFERRED.
**Findings**: issue → evidence/repro → severity → confidence ceiling.
**Actions**: ...

Confidence: 0.80 (ceiling: inference 0.70) - based on detection evidence.
```

Confidence: 0.80 (ceiling: inference 0.70) - reflects validated theater-detection outputs.
