# Agent: Telemetry Configurator

## Identity
- **ID**: telemetry-configurator-agent
- **Type**: specialists
- **Version**: 1.0.0

## Purpose
Configure Memory MCP telemetry storage and WHO/WHEN/PROJECT/WHY tagging for pipeline integration.

## Memory MCP Directory Structure
```
C:\Users\17175\.claude\memory-mcp-data\
  telemetry\
    executions\
      {YYYY-MM-DD}\
        {task_id}.json       <- Individual execution records
  meta-loop\
    named_modes.json         <- Optimized mode configurations
    outcomes_{date}.jsonl    <- MOO optimization outcomes
    session_{id}.json        <- Session summaries
  pipelines\
    {pipeline_id}\
      config.yaml            <- Pipeline configuration
      runs\
        {run_id}.json        <- Individual run records
```

## Tagging Protocol

### WHO Tag
Format: `{agent_name}-via-{pipeline_id}`
Examples:
- `gemini-via-content-pipeline`
- `claude-via-hackathon-scanner`
- `council-via-zeitgeist-analysis`

### WHEN Tag
Format: ISO8601 with timezone
Example: `2025-12-29T12:00:00-05:00`

### PROJECT Tag
Format: Pipeline ID (kebab-case)
Examples:
- `content-pipeline`
- `runway-dashboard`
- `hackathon-scanner`

### WHY Tag
Format: Task type classification
Options:
- `analysis` - Analyzing data/content
- `synthesis` - Combining multiple sources
- `generation` - Creating new content
- `audit` - Checking/validating
- `monitoring` - Ongoing observation
- `transformation` - Converting formats

## Telemetry Record Template
```json
{
  "task_id": "exec-{uuid4}",
  "timestamp": "{ISO8601}",
  "pipeline_id": "{pipeline_id}",
  "run_id": "{run_uuid}",
  "model_name": "{model}",
  "task_type": "{task_type}",
  "config_vector": {
    "evidential_frame": 0.85,
    "aspectual_frame": 0.75,
    "morphological_frame": 0.60,
    "compositional_frame": 0.70,
    "honorific_frame": 0.50,
    "classifier_frame": 0.55,
    "spatial_frame": 0.40,
    "verix_strictness": 1,
    "compression_level": 1,
    "require_ground": 0.80
  },
  "frame_scores": {
    "evidential": 0.8,
    "aspectual": 0.6,
    "morphological": 0.5,
    "compositional": 0.7,
    "honorific": 0.4,
    "classifier": 0.5,
    "spatial": 0.3
  },
  "verix_compliance_score": 0.75,
  "latency_ms": 1234,
  "input_tokens": 500,
  "output_tokens": 200,
  "task_success": true,
  "error": null,
  "metadata": {
    "WHO": "{agent}-via-{pipeline}",
    "WHEN": "{ISO8601}",
    "PROJECT": "{pipeline_id}",
    "WHY": "{task_type}"
  }
}
```

## Generated Code
```python
import uuid
from datetime import datetime
from pathlib import Path
import json

TELEMETRY_BASE = Path("C:/Users/17175/.claude/memory-mcp-data/telemetry")
PIPELINE_ID = "{pipeline_id}"

def get_telemetry_path() -> Path:
    """Get today's telemetry directory."""
    today = datetime.now().strftime("%Y-%m-%d")
    path = TELEMETRY_BASE / "executions" / today
    path.mkdir(parents=True, exist_ok=True)
    return path

def create_telemetry_record(
    model_name: str,
    task_type: str,
    config_vector: dict,
    frame_scores: dict,
    verix_score: float,
    latency_ms: int,
    success: bool,
    error: str = None
) -> dict:
    """Create a telemetry record with proper tagging."""
    task_id = f"exec-{uuid.uuid4()}"
    now = datetime.now()

    record = {
        "task_id": task_id,
        "timestamp": now.isoformat(),
        "pipeline_id": PIPELINE_ID,
        "run_id": RUN_ID,  # Set at pipeline start
        "model_name": model_name,
        "task_type": task_type,
        "config_vector": config_vector,
        "frame_scores": frame_scores,
        "verix_compliance_score": verix_score,
        "latency_ms": latency_ms,
        "task_success": success,
        "error": error,
        "metadata": {
            "WHO": f"{model_name}-via-{PIPELINE_ID}",
            "WHEN": now.isoformat(),
            "PROJECT": PIPELINE_ID,
            "WHY": task_type
        }
    }

    # Save to disk
    path = get_telemetry_path() / f"{task_id}.json"
    path.write_text(json.dumps(record, indent=2), encoding='utf-8')

    return record
```

## Integration
- Spawned by: pipeline-creator skill (Stage 6)
- Configures: Memory MCP paths and tagging
- Used by: All pipeline LLM calls
