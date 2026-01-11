# AI Dev Orchestration - Quick Reference v2.1.0

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



## 5-Phase SOP at a Glance

```
Phase 1: PRODUCT FRAMING (planner)
  |-> Define scope, success criteria
  |-> Create Do-Not-Touch list
  |-> Apply Feature Prompt Framework

Phase 2: SETUP & FOUNDATIONS (system-architect)
  |-> Architecture review
  |-> Foundation setup
  |-> [MANUAL GATE: Architecture Approval]

Phase 3: FEATURE DEV LOOP (coder + tester + reviewer)
  |-> Fresh context per feature
  |-> Implement -> Test -> Review
  |-> [MANUAL GATE: Feature Approval]

Phase 4: TESTING & REFACTORS (tester + coder)
  |-> Integration testing
  |-> Refactoring & cleanup
  |-> [MANUAL GATE: Quality Approval]

Phase 5: DEPLOYMENT (cicd-engineer)
  |-> Deployment preparation
  |-> Deploy to production
```

## Behavioral Guardrails

| Guardrail | Description |
|-----------|-------------|
| Fresh Context | Start each feature with clean context |
| Do-Not-Touch List | Protected files/modules list |
| Feature Prompt Framework | Structured prompt template |
| Manual Testing Gates | Human approval checkpoints |

## Required Artifacts

1. **Do-Not-Touch Template** - `.artifacts/Do-Not-Touch-Template.md`
2. **Feature Prompt Framework** - `.artifacts/Feature-Prompt-Framework.md`
3. **Foundation Prompt Template** - `.artifacts/Foundation-Prompt-Template.md`
4. **Compliance Checklist** - `.artifacts/Compliance-Checklist.md`

## Agent Assignments

| Phase | Agent | Role |
|-------|-------|------|
| 1 | planner | Scope & framing |
| 2 | system-architect | Architecture |
| 3 | coder | Implementation |
| 3 | tester | Testing |
| 3 | reviewer | Code review |
| 4 | tester + coder | Integration |
| 5 | cicd-engineer | Deployment |

## Quick Commands

```bash
# Invoke for new feature
Use ai-dev-orchestration for: [feature description]

# Invoke for bug fix
Use ai-dev-orchestration to fix: [bug description]
```

## Manual Gates Checklist

### Gate 1: Architecture Approval
- [ ] Architecture aligns with existing patterns
- [ ] Dependencies are justified
- [ ] Do-Not-Touch list respected

### Gate 2: Feature Approval
- [ ] Feature meets acceptance criteria
- [ ] Tests pass
- [ ] Code review approved

### Gate 3: Quality Approval
- [ ] Integration tests pass
- [ ] No regressions
- [ ] Performance acceptable

## Related Skills

- **parallel-swarm-implementation** - Loop 2 execution
- **cicd-intelligent-recovery** - Loop 3 deployment
- **research-driven-planning** - Loop 1 planning


---
*Promise: `<promise>QUICK_REFERENCE_VERIX_COMPLIANT</promise>`*
