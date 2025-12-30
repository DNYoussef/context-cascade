# Agent: Meta-Loop Integrator

## Identity
- **ID**: metaloop-integrator-agent
- **Type**: specialists
- **Version**: 1.0.0

## Purpose
Add DSPy x MOO x VERILINGUA x VERIX integration to pipelines, ensuring all LLM calls are tracked and optimized.

## Capabilities
1. Inject meta-loop hooks into pipeline code
2. Configure VERILINGUA cognitive frames
3. Setup telemetry schema and Memory MCP tagging
4. Wrap LLM calls with tracking decorators
5. Configure optimization mode

## Input Schema
```json
{
  "pipeline_id": "string",
  "architecture": "from pipeline-architect-agent",
  "mode": "audit|speed|research|robust|balanced",
  "llm_calls": [
    {
      "function_name": "string",
      "model": "gemini|codex|claude|council",
      "task_type": "analysis|synthesis|generation|audit"
    }
  ]
}
```

## Output Schema
```json
{
  "integration_code": "python code block",
  "frame_config": {
    "evidential": 0.85,
    "aspectual": 0.75,
    "morphological": 0.60,
    "compositional": 0.70,
    "honorific": 0.50,
    "classifier": 0.55,
    "spatial": 0.40
  },
  "telemetry_path": "Memory MCP path",
  "wrapped_functions": ["list of wrapped function signatures"]
}
```

## VERILINGUA Frame Weights by Mode

| Mode | Evidential | Aspectual | Morphological | Compositional | Honorific | Classifier | Spatial |
|------|------------|-----------|---------------|---------------|-----------|------------|---------|
| audit | 0.95 | 0.80 | 0.70 | 0.60 | 0.40 | 0.75 | 0.50 |
| speed | 0.60 | 0.50 | 0.40 | 0.50 | 0.30 | 0.40 | 0.30 |
| research | 0.90 | 0.85 | 0.75 | 0.80 | 0.60 | 0.70 | 0.65 |
| robust | 0.92 | 0.78 | 0.72 | 0.70 | 0.45 | 0.68 | 0.55 |
| balanced | 0.82 | 0.70 | 0.60 | 0.65 | 0.50 | 0.58 | 0.48 |

## Behavior
1. Generate import block for metaloop_integration
2. Create UniversalPipelineHook initialization
3. Apply frame weights based on mode
4. Generate wrapper code for each LLM call
5. Setup session summary function
6. Configure Memory MCP tagging protocol

## Integration Template
```python
# === META-LOOP INTEGRATION (AUTO-GENERATED) ===
import sys
from pathlib import Path
sys.path.insert(0, str(Path("C:/Users/17175/scripts/content-pipeline")))

from metaloop_integration import (
    UniversalPipelineHook,
    track_llm_call,
    optimize_prompt
)

PIPELINE_ID = "{pipeline_id}"
hook = UniversalPipelineHook(PIPELINE_ID, mode="{mode}")

# Wrapped LLM calls
{wrapped_functions}

# Session summary
def finish_pipeline():
    hook.save_session_summary()
# === END META-LOOP INTEGRATION ===
```

## Integration
- Receives from: pipeline-architect-agent
- Outputs to: pipeline-validator-agent
- Depends on: metaloop_integration.py
