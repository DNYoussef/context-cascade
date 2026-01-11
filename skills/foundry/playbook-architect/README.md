# Playbook Architect

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



A foundry skill for creating, analyzing, and optimizing playbooks that orchestrate skill sequences.

## Quick Start

```javascript
// Invoke when creating or improving playbooks
Skill("playbook-architect")
```

## When to Use

- Creating new playbooks for recurring workflow patterns
- Improving existing playbooks with suboptimal routing
- Building playbook libraries for team standardization
- Gap analysis (MECE coverage of user intents)

## Key Features

### 7-Dimensional Playbook Analysis
1. Intent Mapping Assessment
2. Skill Sequence Validation
3. Dependency Analysis
4. MCP Requirements Evaluation
5. Success Criteria Definition
6. Failure Mode Detection
7. Complexity and Timing Assessment

### 4-Phase Creation Methodology
1. **Workflow Analysis** (15-30 min) - Understand the orchestration
2. **Playbook Architecture** (20-30 min) - Design the structure
3. **Success Criteria & Guardrails** (15-20 min) - Define quality
4. **Integration & Testing** (20-30 min) - Validate in practice

## Playbook Template

```yaml
playbook: [name]
version: 1.0.0

triggers:
  keywords: [trigger keywords]
  negative: [exclusion keywords]

phases:
  - name: "Phase 1"
    type: sequential
    skills: [skill-list]

  - name: "Phase 2"
    type: parallel
    prerequisites: [Phase 1]
    skills: [skill-list]

success_criteria:
  primary: "[measurable outcome]"
  acceptance_gates: [list]

guardrails:
  NEVER: [anti-patterns]
  ALWAYS: [requirements]

mcp_requirements:
  required: [mcps]
  optional: [mcps]
```

## Related Files

- **Skill Definition**: `skill.md`
- **Playbook Guardrails**: `docs/PLAYBOOK-META-LOOP-GUARDRAILS.md`
- **Quick Reference**: `docs/PLAYBOOK-QUICK-REFERENCE-V3.0.md`
- **Enhanced System**: `docs/ENHANCED-PLAYBOOK-SYSTEM.md`

## Success Metrics
- [assert|neutral] Playbook routes correctly >95% of time [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] Execution completes without manual intervention [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] Time estimate within 20% of actual [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] All guardrails enforced [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] Promise: `<promise>README_VERIX_COMPLIANT</promise>`* [ground:acceptance-criteria] [conf:0.90] [state:provisional]
