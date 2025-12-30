# SKILL: Pipeline Creator

## Metadata
- **ID**: pipeline-creator
- **Version**: 1.0.0
- **Category**: specialists/meta
- **Trigger**: "create pipeline", "new pipeline", "integrate metaloop", "pipeline from template"
- **Dependencies**: metaloop_integration.py, Memory MCP, Context Cascade

## Purpose

Create new automated pipelines that integrate with the full DSPy x MOO x VERILINGUA x VERIX optimization stack. Every pipeline created by this skill automatically:

1. Integrates with the meta-loop optimization system
2. Records telemetry to Memory MCP
3. Uses VERILINGUA cognitive frames
4. Validates against VERIX epistemic requirements
5. Participates in bi-weekly MOO language evolution

## 12-Stage Pipeline Creation Process

### Stage 1: Intent Analysis
- Identify pipeline purpose (content, trading, monitoring, etc.)
- Determine schedule (realtime, daily, weekly, event-driven)
- Map to existing pipeline patterns

### Stage 1.5: Gate Planning (MANDATORY)
For EACH pipeline, identify:
1. **Synchronization Gates**: Where must all parallel work complete before proceeding?
2. **Quality Gates**: Where must output pass quality threshold?
3. **Ralph Wiggum Loops**: Which stages need retry-until-pass patterns?

Gate Types:
```
SYNC_GATE: Wait for all parallel operations to complete
  Example: Wait for all transcripts before analysis

QUALITY_GATE: Output must pass audit before proceeding
  Example: Slop score < 30%

DEPENDENCY_GATE: Wait for upstream output
  Example: Wait for debate before implications

COMPILE_GATE: Final validation before publish
  Example: All files exist, no errors
```

Ralph Wiggum Loop Pattern:
```python
async def ralph_wiggum_loop(
    generate_fn: Callable,
    audit_fn: Callable,
    max_iterations: int = 3,
    pass_threshold: float = 0.7
) -> Tuple[Any, AuditResult]:
    for i in range(max_iterations):
        result = await generate_fn()
        audit = await audit_fn(result)
        if audit.score >= pass_threshold:
            return result, audit
        generate_fn = partial(generate_fn, feedback=audit.feedback)
    return result, audit
```

### Stage 2: Mode Selection
Select optimization mode based on pipeline type:

| Mode | Use Case | Accuracy | Efficiency |
|------|----------|----------|------------|
| audit | Compliance, code review | 0.960 | 0.763 |
| speed | Quick tasks, prototyping | 0.734 | 0.950 |
| research | Content analysis, deep work | 0.980 | 0.824 |
| robust | Production code, critical paths | 0.960 | 0.769 |
| balanced | General purpose | 0.882 | 0.928 |

### Stage 3: Template Selection
Choose base template:
- `content-pipeline-template.py` - For content ingestion/analysis
- `monitoring-pipeline-template.py` - For system monitoring
- `trading-pipeline-template.py` - For financial automation
- `research-pipeline-template.py` - For research workflows
- `generic-pipeline-template.py` - For custom pipelines

### Stage 4: Meta-Loop Integration
Inject the universal meta-loop hook:

```python
from metaloop_integration import (
    UniversalPipelineHook,
    track_llm_call,
    optimize_prompt,
    get_content_pipeline_hook
)

hook = UniversalPipelineHook("{pipeline-id}", mode="{selected-mode}")
```

### Stage 5: VERILINGUA Frame Configuration
Configure cognitive frames based on task type:

```python
FRAME_CONFIG = {
    "evidential": 0.85,      # "How do you know?"
    "aspectual": 0.75,       # "Complete or ongoing?"
    "morphological": 0.60,   # "What are components?"
    "compositional": 0.70,   # "Build from primitives?"
    "honorific": 0.50,       # "Who is the audience?"
    "classifier": 0.55,      # "What type/count?"
    "spatial": 0.40          # "Absolute position?"
}
```

### Stage 6: Telemetry Schema Definition
Define what gets tracked:

```python
TELEMETRY_SCHEMA = {
    "task_id": "exec-{uuid}",
    "pipeline_id": "{your-pipeline}",
    "model_name": "gemini|codex|claude",
    "task_type": "analysis|synthesis|generation|audit",
    "config_vector": {...},
    "frame_scores": {...},
    "verix_compliance_score": float,
    "latency_ms": int,
    "task_success": bool,
    "metadata": {
        "WHO": "agent-via-pipeline",
        "WHEN": "ISO8601",
        "PROJECT": "pipeline-id",
        "WHY": "task-type"
    }
}
```

### Stage 7: Memory MCP Tagging Protocol
Ensure all writes follow WHO/WHEN/PROJECT/WHY:

```python
def get_memory_tags(agent_name: str, task_type: str) -> dict:
    return {
        "WHO": f"{agent_name}-via-{PIPELINE_ID}",
        "WHEN": datetime.now().isoformat(),
        "PROJECT": PIPELINE_ID,
        "WHY": task_type
    }
```

### Stage 8: LLM Call Wrapping
Wrap ALL LLM calls with tracking:

```python
async def tracked_llm_call(prompt: str, task_type: str = "general"):
    optimized_prompt = hook.optimize_prompt(prompt, task_type)

    with hook.track_execution("model-name", optimized_prompt, task_type) as ctx:
        response = await call_model(optimized_prompt)
        ctx.record_response(response)

    return response
```

### Stage 9: Error Handling & Recovery
Add CICD-intelligent-recovery patterns:

```python
@retry(max_attempts=3, backoff="exponential")
async def resilient_call(func, *args, **kwargs):
    try:
        return await func(*args, **kwargs)
    except RateLimitError:
        hook.record_error("rate_limit")
        await asyncio.sleep(60)
        raise
    except TimeoutError:
        hook.record_error("timeout")
        raise
```

### Stage 10: Session Summary
Save session summary at pipeline end:

```python
def finish_pipeline():
    summary = {
        "pipeline_id": PIPELINE_ID,
        "completed_at": datetime.now().isoformat(),
        "total_calls": hook.call_count,
        "success_rate": hook.success_rate,
        "avg_latency_ms": hook.avg_latency,
        "mode": hook.mode
    }
    hook.save_session_summary(summary)
```

### Stage 11: Scheduling Setup
Generate Task Scheduler XML or cron entry:

```xml
<Task>
  <RegistrationInfo>
    <Description>{pipeline_name} - Automated Pipeline</Description>
  </RegistrationInfo>
  <Triggers>
    <CalendarTrigger>
      <StartBoundary>{start_time}</StartBoundary>
      <ScheduleByDay><DaysInterval>{interval}</DaysInterval></ScheduleByDay>
    </CalendarTrigger>
  </Triggers>
  <Actions>
    <Exec>
      <Command>python</Command>
      <Arguments>{pipeline_path}</Arguments>
    </Exec>
  </Actions>
</Task>
```

### Stage 12: Validation & Registration
- Run pipeline with --dry-run flag
- Verify telemetry appears in Memory MCP
- Add to pipeline inventory in 2025-LIFE-AUTOMATION-TODO.md
- Add to bi-weekly MOO aggregation list

## Output Artifacts

1. `{pipeline_name}.py` - Main pipeline script
2. `{pipeline_name}_config.yaml` - Configuration file
3. `{pipeline_name}_schedule.xml` - Task Scheduler definition
4. Update to `2025-LIFE-AUTOMATION-TODO.md` - Inventory entry

## Agents Used

| Agent | Role |
|-------|------|
| pipeline-architect-agent | Design pipeline structure |
| metaloop-integrator-agent | Add DSPy x MOO x VERILINGUA x VERIX |
| pipeline-validator-agent | Validate requirements |
| telemetry-configurator-agent | Setup Memory MCP tagging |

## Example Invocation

```
User: "Create a pipeline for monitoring GitHub repository stars"

pipeline-creator:
  1. Intent: monitoring, event-driven (webhook) or daily poll
  2. Mode: balanced (general purpose monitoring)
  3. Template: monitoring-pipeline-template.py
  4. Integrate meta-loop with "balanced" mode
  5. Configure frames (evidential=0.7, spatial=0.8 for repo tracking)
  6. Define telemetry (repo_name, stars_count, delta)
  7. Setup WHO/WHEN/PROJECT/WHY tagging
  8. Wrap GitHub API calls with tracking
  9. Add retry for rate limits
  10. Session summary with star trends
  11. Schedule: Daily 9:00 AM
  12. Validate and register
```

## Integration Points

- **Memory MCP**: `C:\Users\17175\.claude\memory-mcp-data\telemetry\`
- **Meta-Loop**: `C:\Users\17175\scripts\content-pipeline\metaloop_integration.py`
- **Inventory**: `C:\Users\17175\2025-LIFE-AUTOMATION-TODO.md`
- **MOO Scripts**: `C:\Users\17175\claude-code-plugins\ruv-sparc-three-loop-system\cognitive-architecture\optimization\`

## Related Skills

- `cascade-orchestrator` - Multi-skill workflow coordination
- `cicd-intelligent-recovery` - Failure recovery patterns
- `deep-research-orchestrator` - Research pipeline patterns
- `feature-dev-complete` - Full development lifecycle

---

*Last Updated: 2025-12-29*
*Integrated with: DSPy x MOO x VERILINGUA x VERIX*
