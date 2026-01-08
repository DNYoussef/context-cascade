---
name: qa-pipeline
description: Self-validating QA loop extracted from AutoClaude - reviews acceptance criteria and auto-fixes issues until approval or escalation.
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - Glob
  - Grep
  - Task
  - TodoWrite
model: sonnet
x-version: 1.0.0
x-category: quality
x-vcl-compliance: v3.1.1
x-cognitive-frames:
  - EVD
  - ASP
  - SPC
x-life-os-integration: true
---

## STANDARD OPERATING PROCEDURE

### Purpose
Run a self-validating QA loop that reviews implementation against acceptance criteria, auto-fixes issues, and iterates until approval or human escalation.

### Trigger Conditions
- **Positive:** Post-build validation, acceptance criteria verification, before merge to main.
- **Negative:** Unit tests (use tester agent), style-only checks (use linter), security scans (use security-auditor).

### Prerequisites
- Life OS Dashboard backend at `D:\Projects\life-os-dashboard\backend`
- ANTHROPIC_API_KEY environment variable set
- Memory MCP running (optional, for context persistence)
- Spec directory with `implementation_plan.json` containing acceptance criteria

### Guardrails
- **Max Iterations:** 50 (configurable via QAConfig.MAX_QA_ITERATIONS)
- **Recurring Issue Threshold:** 3 occurrences triggers human escalation
- **Consecutive Errors:** 3 errors without progress escalates
- **Confidence ceiling:** Use observation 0.95 for test results, inference 0.70 for analysis

### Execution Phases

1. **Validation Check**
   - Verify build is complete (all subtasks marked done)
   - Check if already approved (skip if so)
   - Detect human feedback file (process first if present)

2. **QA Reviewer Session**
   - Load Memory MCP context for similar past issues
   - Generate review prompt with project context
   - Claude reviews against acceptance criteria
   - Update `implementation_plan.json` with qa_signoff status

3. **Issue Analysis**
   - Parse issues from qa_signoff
   - Check for recurring issues (similarity > 0.8)
   - Escalate to human if recurring threshold exceeded

4. **QA Fixer Session** (if rejected)
   - Generate fixer prompt with issues and context
   - Claude proposes and applies fixes
   - Store fix patterns in Memory MCP for learning

5. **Iteration Loop**
   - Re-run reviewer after fixes
   - Continue until approved or max iterations
   - Track iteration history for analysis

### Python API Usage

```python
from app.qa import run_wired_qa_loop, quick_qa_check

# Full QA loop with infrastructure wired
success = await run_wired_qa_loop(
    project_dir=Path("D:/Projects/my-project"),
    spec_dir=Path("D:/Projects/my-project/.specs/feature-x"),
    model="sonnet",
    verbose=True,
)

# Quick single-iteration check
result = await quick_qa_check(
    project_dir=Path("D:/Projects/my-project"),
    spec_dir=Path("D:/Projects/my-project/.specs/feature-x"),
)
print(f"Status: {result['status']}")
```

### CLI Invocation (via Claude Code)

```bash
# Run QA validation
python -c "
import asyncio
from pathlib import Path
from app.qa import run_wired_qa_loop

asyncio.run(run_wired_qa_loop(
    Path('D:/Projects/my-project'),
    Path('D:/Projects/my-project/.specs/feature-x'),
    verbose=True
))
"
```

### Output Format
- Status: APPROVED | REJECTED | ERROR
- Iteration count and history
- Issues found with file:line references
- Fix recommendations applied
- Escalation report if recurring issues detected

### Files Produced
- `implementation_plan.json` - Updated with qa_signoff
- `QA_REPORT.md` - Detailed review findings
- `QA_FIX_REQUEST.md` - Human-readable fix requests
- `QA_ESCALATION.md` - Created if recurring issues detected
- `MANUAL_TEST_PLAN.md` - For no-test projects

### Integration with Memory MCP
- **Context Retrieval:** Fetches similar past issues and fix patterns
- **Session Saving:** Stores outcomes for future reference
- **Fix Pattern Learning:** Successful fixes stored as expertise

### Validation Checklist
- [ ] Build marked complete in spec
- [ ] Acceptance criteria defined in implementation_plan.json
- [ ] ANTHROPIC_API_KEY set
- [ ] Memory MCP running (optional)
- [ ] Confidence ceiling included in output

Confidence: 0.85 (ceiling: observation 0.95) - Skill documented based on implemented QA pipeline infrastructure.
