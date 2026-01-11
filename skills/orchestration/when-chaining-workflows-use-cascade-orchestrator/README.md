# Cascade Orchestrator - Quick Start

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



Chain workflows with sequential, parallel, and conditional execution.

## Quick Start

```bash
# 1. Design cascade
cat > cascade.yaml <<EOF
workflows:
  - {id: design, type: sequential}
  - {id: impl, type: parallel, depends_on: [design]}
  - {id: test, type: sequential, depends_on: [impl]}
EOF

# 2. Execute cascade
npx claude-flow@alpha cascade execute --definition cascade.yaml

# 3. Monitor
npx claude-flow@alpha cascade monitor --interval 10

# 4. Optimize
npx claude-flow@alpha cascade optimize --enable-parallelism
```

## Agents
- **task-orchestrator:** Workflow coordination
- **hierarchical-coordinator:** Workflow hierarchy
- **memory-coordinator:** State management

## Success Metrics
- [assert|neutral] Completion time: Within ±15% [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] Resource utilization: 70-85% [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] Success rate: >95% [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] Promise: `<promise>README_VERIX_COMPLIANT</promise>`* [ground:acceptance-criteria] [conf:0.90] [state:provisional]
