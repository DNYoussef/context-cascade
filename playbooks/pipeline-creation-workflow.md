# Playbook: Pipeline Creation Workflow

## Metadata
- **ID**: pipeline-creation-workflow
- **Version**: 1.0.0
- **Category**: meta/infrastructure
- **Trigger**: "create pipeline", "new automated workflow", "integrate metaloop"

## Purpose
End-to-end workflow for creating new automated pipelines that integrate with the full DSPy x MOO x VERILINGUA x VERIX optimization stack.

## Prerequisites
- Context Cascade plugin installed
- Memory MCP running
- metaloop_integration.py available

## Workflow Stages

```
+-------------------+     +----------------------+     +---------------------+
| 1. REQUIREMENTS   |---->| 2. ARCHITECTURE      |---->| 2.5 GATE PLANNING   |
| Gather intent     |     | Design stages        |     | Identify sync gates |
| Identify schedule |     | Map data flow        |     | Quality gates       |
| List dependencies |     | Select template      |     | Ralph Wiggum loops  |
+-------------------+     +----------------------+     +----------+----------+
                                                                  |
+-------------------+     +----------------------+     +----------v----------+
| 3. MODE SELECTION |<----| Gate definitions     |<----| Gate placement      |
| audit/speed/res.  |     | created              |     | in architecture     |
+-------------------+     +----------------------+     +---------------------+
                                                                  |
+-------------------+     +----------------------+     +----------v----------+
| 6. TELEMETRY      |<----| 5. WRAP LLM CALLS    |<----| 4. META-LOOP INJECT |
| WHO/WHEN/PROJECT/ |     | track_execution()    |     | UniversalPipelineHook|
| WHY tagging       |     | optimize_prompt()    |     | VERILINGUA frames   |
+--------+----------+     +----------------------+     +---------------------+
         |
+--------v----------+     +----------------------+     +---------------------+
| 7. ERROR HANDLING |---->| 8. SESSION SUMMARY   |---->| 9. SCHEDULING       |
| Retry decorators  |     | save_session_summary |     | Task Scheduler XML  |
| Graceful degrade  |     | Run statistics       |     | or cron entry       |
+-------------------+     +----------------------+     +----------+----------+
                                                                  |
+-------------------+     +----------------------+     +----------v----------+
| 12. REGISTER      |<----| 11. DRY RUN          |<----| 10. VALIDATE        |
| Add to inventory  |     | --dry-run flag       |     | pipeline-validator  |
| Update MOO list   |     | Check telemetry      |     | Checklist pass      |
+-------------------+     +----------------------+     +---------------------+
```

## Stage Details

### Stage 1: Requirements Gathering
**Agent**: User interaction (AskUserQuestion)
**Output**: Requirements spec

Questions to ask:
1. What does this pipeline do? (purpose)
2. How often should it run? (schedule)
3. What are the inputs? (data sources)
4. What are the outputs? (artifacts)
5. Does it need GPU? (constraints)

### Stage 2: Architecture Design
**Agent**: pipeline-architect-agent
**Input**: Requirements spec
**Output**: Architecture document

Deliverables:
- Stage definitions (ingest/transform/analyze/output)
- Data flow diagram (Mermaid)
- Dependency list

### Stage 2.5: Gate Planning (MANDATORY)
**Agent**: pipeline-architect-agent
**Input**: Architecture document
**Output**: Gate specification

For EVERY pipeline, explicitly define:

**1. Synchronization Gates (SYNC_GATE)**
Where must parallel work complete before proceeding?
```yaml
gates:
  - id: gate_transcription
    type: SYNC_GATE
    wait_for: all_transcripts_complete
    before_stage: analysis
```

**2. Quality Gates (QUALITY_GATE)**
Where must output pass quality threshold?
```yaml
gates:
  - id: gate_slop
    type: QUALITY_GATE
    threshold: 0.30
    metric: slop_score
    action_on_fail: ralph_wiggum_loop
```

**3. Ralph Wiggum Loops**
Which stages need retry-until-pass?
```yaml
ralph_wiggum_loops:
  - stage: style_rewrite
    max_iterations: 3
    pass_threshold: 0.70
    auditor: style_auditor

  - stage: slop_removal
    max_iterations: 5
    pass_threshold: 0.70  # = slop < 30%
    auditor: slop_detector

  - stage: image_generation
    max_iterations: 3
    pass_threshold: 0.70
    auditor: visual_auditor
```

**4. Dependency Gates (DEPENDENCY_GATE)**
What must complete before this can start?
```yaml
gates:
  - id: gate_debate
    type: DEPENDENCY_GATE
    requires: [gemini_zeitgeist, codex_zeitgeist, claude_zeitgeist]
    before_stage: byzantine_debate
```

**5. Compile Gate (COMPILE_GATE)**
Final validation before publish
```yaml
gates:
  - id: gate_publish
    type: COMPILE_GATE
    checks:
      - blog_file_exists
      - image_file_exists
      - slop_passed
      - style_passed
      - git_status_clean
```

### Stage 3: Mode Selection
**Agent**: pipeline-architect-agent
**Input**: Architecture
**Output**: Selected mode

Decision matrix:
| Pipeline Type | Recommended Mode |
|---------------|------------------|
| Content analysis | research |
| Code generation | robust |
| Quick queries | speed |
| Compliance/audit | audit |
| General purpose | balanced |

### Stage 4: Meta-Loop Injection
**Agent**: metaloop-integrator-agent
**Input**: Architecture + Mode
**Output**: Integration code

Inject:
```python
from metaloop_integration import UniversalPipelineHook
hook = UniversalPipelineHook(PIPELINE_ID, mode=MODE)
```

### Stage 5: Wrap LLM Calls
**Agent**: metaloop-integrator-agent
**Input**: Pipeline functions
**Output**: Wrapped functions

Pattern:
```python
async def tracked_call(prompt, task_type):
    optimized = hook.optimize_prompt(prompt, task_type)
    with hook.track_execution(model, optimized, task_type) as ctx:
        response = await call_model(optimized)
        ctx.record_response(response)
    return response
```

### Stage 6: Telemetry Configuration
**Agent**: telemetry-configurator-agent
**Input**: Pipeline ID
**Output**: Telemetry code

Configure:
- Memory MCP paths
- WHO/WHEN/PROJECT/WHY tags
- Telemetry record template

### Stage 7: Error Handling
**Agent**: metaloop-integrator-agent
**Input**: Wrapped functions
**Output**: Resilient functions

Add:
- @retry decorators
- Error recording to hook
- Fallback paths

### Stage 8: Session Summary
**Agent**: metaloop-integrator-agent
**Input**: Pipeline structure
**Output**: Summary function

Implement:
```python
def finish_pipeline():
    hook.save_session_summary()
```

### Stage 9: Scheduling
**Agent**: pipeline-architect-agent
**Input**: Schedule requirements
**Output**: Schedule configuration

Generate:
- Task Scheduler XML (Windows)
- OR cron entry (Linux)

### Stage 10: Validation
**Agent**: pipeline-validator-agent
**Input**: Complete pipeline
**Output**: Validation report

Checklist:
- Meta-loop integration (5 items)
- VERILINGUA compliance (3 items)
- Memory MCP tagging (4 items)
- Telemetry schema (6 items)
- Error handling (3 items)
- Scheduling (3 items)

### Stage 11: Dry Run
**Agent**: pipeline-validator-agent
**Input**: Validated pipeline
**Output**: Dry run results

Execute:
```bash
python {pipeline}.py --dry-run
```

Verify telemetry appears in:
`C:\Users\17175\.claude\memory-mcp-data\telemetry\executions\{today}\`

### Stage 12: Registration
**Agent**: pipeline-validator-agent
**Input**: Passed dry run
**Output**: Updated inventory

Actions:
1. Add to `2025-LIFE-AUTOMATION-TODO.md` pipeline inventory
2. Add to bi-weekly MOO aggregation list
3. Commit pipeline files to git

## Output Artifacts

| Artifact | Location |
|----------|----------|
| Pipeline script | `C:\Users\17175\scripts\{domain}\{pipeline_name}.py` |
| Config file | `C:\Users\17175\scripts\{domain}\{pipeline_name}_config.yaml` |
| Schedule XML | `C:\Users\17175\scripts\{domain}\{pipeline_name}_schedule.xml` |
| Inventory entry | `C:\Users\17175\2025-LIFE-AUTOMATION-TODO.md` |

## Example Execution

```
User: "Create a pipeline to monitor GitHub stars for my repos"

Stage 1: Requirements
  - Purpose: Track GitHub repo stars
  - Schedule: Daily 9:00 AM
  - Inputs: GitHub API
  - Outputs: Star trends to Memory MCP

Stage 2: Architecture
  - Stages: fetch -> aggregate -> analyze -> store
  - Template: monitoring-pipeline-template.py

Stage 3: Mode Selection
  - Mode: balanced (general monitoring)

Stage 4-8: Integration
  - [Generated code with meta-loop hooks]

Stage 9: Scheduling
  - Task Scheduler: Daily 9:00 AM

Stage 10-11: Validation
  - All checks passed
  - Dry run successful

Stage 12: Registration
  - Added to inventory
  - Ready for deployment
```

## Related Components

- **Skill**: pipeline-creator
- **Agents**: pipeline-architect-agent, metaloop-integrator-agent, pipeline-validator-agent, telemetry-configurator-agent
- **Integration**: metaloop_integration.py, Memory MCP

---

*Last Updated: 2025-12-29*
*Part of: DSPy x MOO x VERILINGUA x VERIX meta-system*
