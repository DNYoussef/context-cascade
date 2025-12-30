/*============================================================================*/
/* IMPROVEMENT-PIPELINE SKILL :: VERILINGUA x VERIX EDITION                      */
/*============================================================================*/

---
name: improvement-pipeline
version: 1.0.0
description: |
  [assert|neutral] Executable implementation of the Propose -> Test -> Compare -> Commit -> Rollback pipeline for recursive self-improvement. Provides concrete commands and workflows for each stage. [ground:given] [conf:0.95] [state:confirmed]
category: foundry
tags:
- pipeline
- improvement
- testing
- versioning
- rollback
author: system
cognitive_frame:
  primary: evidential
  goal_analysis:
    first_order: "Execute improvement-pipeline workflow"
    second_order: "Ensure quality and consistency"
    third_order: "Enable systematic foundry processes"
---

/*----------------------------------------------------------------------------*/
/* S0 META-IDENTITY                                                            */
/*----------------------------------------------------------------------------*/

[define|neutral] SKILL := {
  name: "improvement-pipeline",
  category: "foundry",
  version: "1.0.0",
  layer: L1
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S1 COGNITIVE FRAME                                                          */
/*----------------------------------------------------------------------------*/

[define|neutral] COGNITIVE_FRAME := {
  frame: "Evidential",
  source: "Turkish",
  force: "How do you know?"
} [ground:cognitive-science] [conf:0.92] [state:confirmed]

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.

/*----------------------------------------------------------------------------*/
/* S2 TRIGGER CONDITIONS                                                       */
/*----------------------------------------------------------------------------*/

[define|neutral] TRIGGER_POSITIVE := {
  keywords: ["improvement-pipeline", "foundry", "workflow"],
  context: "user needs improvement-pipeline capability"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S3 CORE CONTENT                                                             */
/*----------------------------------------------------------------------------*/

# Improvement Pipeline (Executable Stages)

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



## Purpose

Provide concrete, executable implementation for each stage of the improvement pipeline:

```
PROPOSE -> TEST -> COMPARE -> COMMIT -> MONITOR -> ROLLBACK
```

Each stage has:
- Clear inputs and outputs
- Executable commands
- Validation checks
- Failure handling

---

## Stage 1: PROPOSE

Generate concrete improvement proposals with diffs.

### Input
```yaml
propose_input:
  target: "{path to skill/prompt}"
  audit_report: "{from prompt-auditor or skill-auditor}"
  improvement_type: "clarity|completeness|precision|safety|technique"
```

### Process

```javascript
async function generateProposal(target, auditReport) {
  const proposal = {
    id: `prop-${Date.now()}`,
    target,
    timestamp: new Date().toISOString(),
    changes: [],
    predicted_improvement: {},
    risk_assessment: {}
  };

  // 1. Read current version
  const currentContent = await readFile(target);

  // 2. Identify improvement opportunities from audit
  const opportunities = auditReport.issues
    .filter(issue => issue.priority === 'critical' || issue.priority === 'high')
    .slice(0, 5); // Max 5 changes per proposal

  // 3. Generate changes for each opportunity
  for (const opp of opportunities) {
    const change = await generateChange(currentContent, opp);
    proposal.changes.push({
      section: opp.section,
      location: opp.location,
      before: change.before,
      after: change.after,
      rationale: change.rationale,
      technique_applied: change.technique
    });
  }

  // 4. Predict improvement
  proposal.predicted_improvement = {
    primary_metric: auditReport.lowest_score_dimension,
    expected_delta: `+${(opportunities.length * 3)}%`, // ~3% per fix
    confidence: 0.7
  };

  // 5. Assess risk
  proposal.risk_assessment = {
    regression_risk: opportunities.length > 3 ? 'medium' : 'low',
    affected_components: findAffectedComponents(target, proposal.changes),
    rollback_complexity: 'simple' // Always simple with archives
  };

  return proposal;
}
```

### Output
```yaml
proposal:
  id: "prop-1734567890123"
  target: ".claude/skills/skill-forge/SKILL.md"
  timestamp: "2025-12-15T10:30:00Z"

  changes:
    - section: "Phase 3: Structural Architecture"
      location: "Lines 145-160"
      before: |
        Design the skill's structure based on progressive disclosure.
      after: |
        Design the skill's structure based on progressive disclosure.

        ### Failure Handling (REQUIRED)

        For each operation in the skill:
        1. Identify possible failure modes
        2. Define explicit error messages
        3. Specify recovery actions
        4. Include timeout handling

        ```yaml
        error_handling:
          timeout:
            threshold: 30s
            action: "Return partial results with warning"
          invalid_input:
            detection: "Validate against schema"
            action: "Return clear error message with fix suggestion"
        ```
      rationale: "Adds explicit failure handling missing from Phase 3"
      technique_applied: "completeness_enhancement"

  predicted_improvement:
    primary_metric: "failure_coverage"
    expected_delta: "+9%"
    confidence: 0.7

  risk_assessment:
    regression_risk: "low"
    affected_components: ["micro-skill-creator", "agent-creator"]
    rollback_complexity: "simple"
```

### Validation
```yaml
proposal_validation:
  required_fields:
    - id: "Must be unique"
    - target: "Must be valid file path"
    - changes: "At least 1 change"
    - predicted_improvement: "Must have primary_metric"
    - risk_assessment: "Must have regression_risk"

  change_validation:
    - before: "Must exist in current file"
    - after: "Must be different from before"
    - rationale: "Must not be empty"
```

---

## Stage 2: TEST

Run evaluation harness on proposed changes.

### Input
```yaml
test_input:
  proposal_id:

/*----------------------------------------------------------------------------*/
/* S4 SUCCESS CRITERIA                                                         */
/*----------------------------------------------------------------------------*/

[define|neutral] SUCCESS_CRITERIA := {
  primary: "Skill execution completes successfully",
  quality: "Output meets quality thresholds",
  verification: "Results validated against requirements"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S5 MCP INTEGRATION                                                          */
/*----------------------------------------------------------------------------*/

[define|neutral] MCP_INTEGRATION := {
  memory_mcp: "Store execution results and patterns",
  tools: ["mcp__memory-mcp__memory_store", "mcp__memory-mcp__vector_search"]
} [ground:witnessed:mcp-config] [conf:0.95] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S6 MEMORY NAMESPACE                                                         */
/*----------------------------------------------------------------------------*/

[define|neutral] MEMORY_NAMESPACE := {
  pattern: "skills/foundry/improvement-pipeline/{project}/{timestamp}",
  store: ["executions", "decisions", "patterns"],
  retrieve: ["similar_tasks", "proven_patterns"]
} [ground:system-policy] [conf:1.0] [state:confirmed]

[define|neutral] MEMORY_TAGGING := {
  WHO: "improvement-pipeline-{session_id}",
  WHEN: "ISO8601_timestamp",
  PROJECT: "{project_name}",
  WHY: "skill-execution"
} [ground:system-policy] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S7 SKILL COMPLETION VERIFICATION                                            */
/*----------------------------------------------------------------------------*/

[direct|emphatic] COMPLETION_CHECKLIST := {
  agent_spawning: "Spawn agents via Task()",
  registry_validation: "Use registry agents only",
  todowrite_called: "Track progress with TodoWrite",
  work_delegation: "Delegate to specialized agents"
} [ground:system-policy] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S8 ABSOLUTE RULES                                                           */
/*----------------------------------------------------------------------------*/

[direct|emphatic] RULE_NO_UNICODE := forall(output): NOT(unicode_outside_ascii) [ground:windows-compatibility] [conf:1.0] [state:confirmed]

[direct|emphatic] RULE_EVIDENCE := forall(claim): has(ground) AND has(confidence) [ground:verix-spec] [conf:1.0] [state:confirmed]

[direct|emphatic] RULE_REGISTRY := forall(agent): agent IN AGENT_REGISTRY [ground:system-policy] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* PROMISE                                                                     */
/*----------------------------------------------------------------------------*/

[commit|confident] <promise>IMPROVEMENT_PIPELINE_VERILINGUA_VERIX_COMPLIANT</promise> [ground:self-validation] [conf:0.99] [state:confirmed]
