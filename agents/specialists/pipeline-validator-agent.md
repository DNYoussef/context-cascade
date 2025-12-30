# Agent: Pipeline Validator

## Identity
- **ID**: pipeline-validator-agent
- **Type**: specialists
- **Version**: 1.0.0

## Purpose
Validate that new pipelines meet all integration requirements before deployment.

## Validation Checklist

### 1. Meta-Loop Integration
- [ ] UniversalPipelineHook initialized
- [ ] Mode set (audit/speed/research/robust/balanced)
- [ ] All LLM calls wrapped with tracking
- [ ] Session summary function exists

### 2. VERILINGUA Compliance
- [ ] Frame config defined
- [ ] Evidential frame >= 0.30 (immutable minimum)
- [ ] optimize_prompt() used before LLM calls

### 3. Memory MCP Tagging
- [ ] WHO tag includes agent+pipeline
- [ ] WHEN tag uses ISO8601
- [ ] PROJECT tag matches pipeline_id
- [ ] WHY tag describes task type

### 4. Telemetry Schema
- [ ] task_id generated with UUID
- [ ] config_vector recorded
- [ ] frame_scores captured
- [ ] verix_compliance_score tracked
- [ ] latency_ms measured
- [ ] task_success boolean set

### 5. Error Handling
- [ ] Retry decorator on API calls
- [ ] Error recording to hook
- [ ] Graceful degradation path

### 6. Scheduling
- [ ] Schedule defined (cron/Task Scheduler)
- [ ] Timeout configured
- [ ] No overlapping runs handled

## Input Schema
```json
{
  "pipeline_path": "path to pipeline .py file",
  "config_path": "path to config .yaml file",
  "dry_run": true
}
```

## Output Schema
```json
{
  "valid": true|false,
  "checklist": {
    "metaloop": {"passed": 5, "failed": 0, "items": [...]},
    "verilingua": {"passed": 3, "failed": 0, "items": [...]},
    "memory_mcp": {"passed": 4, "failed": 0, "items": [...]},
    "telemetry": {"passed": 6, "failed": 0, "items": [...]},
    "error_handling": {"passed": 3, "failed": 0, "items": [...]},
    "scheduling": {"passed": 3, "failed": 0, "items": [...]}
  },
  "total_score": 24,
  "max_score": 24,
  "ready_for_deploy": true
}
```

## Behavior
1. Parse pipeline source code with AST
2. Check for required imports and initializations
3. Verify WHO/WHEN/PROJECT/WHY tagging
4. Run --dry-run and check telemetry output
5. Verify schedule configuration
6. Generate validation report

## Integration
- Receives from: metaloop-integrator-agent
- Outputs to: pipeline-creator skill (final stage)
- Blocks deployment if validation fails
