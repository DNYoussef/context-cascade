# ML Training Debugger Guide

Use this skill when training jobs fail, diverge, or regress.

## Fast Path
1. Gather evidence: logs, configs, seeds, hardware, recent changes.
2. Reproduce on smallest slice; fix seeds and disable nondeterminism.
3. Isolate variables (data/model/optimizer/precision) with targeted experiments.
4. Apply minimal fix, validate with metrics and regression checks, and document rollback.

## Guardrails
- Keep SKILL.md, README, examples, tests, resources, agents synchronized; fill missing docs first.
- Preserve artifacts; never overwrite checkpoints without backup.
- Confidence ceiling required on every finding (inference/report 0.70; research 0.85; observation/definition 0.95).
- MCP tags: `WHO=ml-training-debugger-{session}`, `WHY=skill-execution`.

Confidence: 0.72 (ceiling: inference 0.70) - Guide refreshed to mirror the new SOP.
