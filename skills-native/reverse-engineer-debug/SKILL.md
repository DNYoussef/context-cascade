---
name: reverse-engineer-debug
description: Skill for reverse-engineer-debug
---

# Reverse Engineer Debug Skill

## Kanitsal Kok Neden Analizi (Evidential Root Cause Analysis)

Every causal link in the investigation MUST have supporting evidence. No speculation without proof.

**Evidence Requirements**:
- **DOGRUDAN** (Direct): Direct observation, log entry, stack trace, metric
- **CIKARIM** (Inference): Pattern-based inference from multiple signals
- **KORELASYON** (Correlation): Time-based correlation (not causation, flag as hypothesis)

**Evidential Investigation Protocol**:
```markdown
WHY-1: [immediate cause]
  - EVIDENCE: [log entry | stack trace | metric | observation]
  - CONFIDENCE: [0.0-1.0]
  - TYPE: DOGRUDAN | CIKARIM | KORELASYON

WHY-2: [deeper cause]
  - EVIDENCE: [code inspection | config analysis | dependency check]
  - CONFIDENCE: [0.0-1.0]
  - TYPE: DOGRUDAN | CIKARIM | KORELASYON

WHY-N: [ROOT CAUSE]
  - EVIDENCE: [comprehensive analysis supporting root diagnosis]
  - CONFIDENCE: [0.0-1.0]
  - TYPE: DOGRUDAN | CIKARIM
```

## Al-Itar al-Sarfi li-Tahlil al-Sabab (Morphological Decomposition)

Symptoms compose into causes through systematic decomposition. Each "Why?" peels away one layer.

**Morphological Structure**:
```
SYMPTOM (Observable Error)
  |
  +-- WHY-1 (Technical Layer: immediate code failure)
      |
      +-- WHY-2 (Design Layer: why code was written this way)
          |
          +-- WHY-3 (Architectural Layer: why design exists)
              |
              +-- WHY-4 (Organizational Layer: process/culture)
                  |
                  +-- WHY-5 (ROOT: foundational assumption or requirement)
```

**NASA 5-Whys Integration**:
1. **Technical**: Code-level failure (syntax, runtime, logic)
2. **Systemic**: Design pattern or implementation choice
3. **Architectural**: System structure or coupling decisions
4. **Process**: Development workflow or testing gaps
5. **Foundational**: Core requirements or assumptions

## Purpose
This skill performs deep reverse engineering root cause analysis (RCA) to debug complex issues, trace problems to their source, and identify the real underlying causes rather than surface symptoms.

## When to Use
- Debugging mysterious or intermittent bugs
- Investigating production incidents
- Analyzing system failures or crashes
- Finding root causes of performance issues
- Reverse engineering legacy code problems
- Tracing error propagation through systems
- Understanding why something broke after changes
- Investigating integration or deployment failures

## How It Works
This skill spawns a specialized **Root Cause Analyzer Agent** that:
1. Systematically collects symptoms and evidence
2. Works backwards from failure points to root causes
3. Generates and tests multiple hypotheses
4. Distinguishes symptoms from true root causes
5. Provides actionable solutions and prevention strategies

## Usage

### Basic Investigation
```
/reverse-engineer-debug
```
You'll be prompted to describe the issue, or you can provide it directly:

### With Issue Description
```
/reverse-engineer-debug "Users report timeout errors on checkout page after latest deployment"
```

### With Detailed Context
```
/reverse-engineer-debug "API returning 500 errors intermittently. Error: 'Cannot read property 'id' of undefined' in user service. Started after database migration yesterday. Affects ~10% of requests."
```

## Input Requirements

The skill works best when you provide:
- **Error Messages**: Exact error text and stack traces
- **Reproduction Steps**: How to trigger the issue
- **Context**: What changed recently (deployments, configs, dependencies)
- **Frequency**: How often it occurs and any patterns
- **Environment**: Where it happens (dev, staging, production)
- **Logs**: Relevant log excerpts if available

## Output

The agent provides a comprehensive evidential RCA report following this template:

```markdown
### Evidential Root Cause Analysis Report

**SYMPTOM**: [Observable error or behavior]
  - Evidence: [reproduction steps with logs/metrics]
  - Status: [VERIFIED | INTERMITTENT | NOT_REPRODUCIBLE]

**WHY-CHAIN** (Morphological Decomposition):
- **WHY-1** (Technical): [immediate cause]
  - EVIDENCE: [log entry | stack trace | error message]
  - TYPE: DOGRUDAN (direct observation)
  - CONFIDENCE: [0.0-1.0]

- **WHY-2** (Systemic): [design/implementation cause]
  - EVIDENCE: [code inspection | design pattern analysis]
  - TYPE: CIKARIM (inference from code)
  - CONFIDENCE: [0.0-1.0]

- **WHY-3** (Architectural): [system structure cause]
  - EVIDENCE: [dependency analysis | coupling metrics]
  - TYPE: DOGRUDAN | CIKARIM
  - CONFIDENCE: [0.0-1.0]

- **WHY-4** (Process): [workflow/testing gap]
  - EVIDENCE: [missing tests | review gaps]
  - TYPE: CIKARIM
  - CONFIDENCE: [0.0-1.0]

- **ROOT CAUSE** (Foundational): [true root]
  - EVIDENCE: [comprehensive analysis]
  - TYPE: DOGRUDAN | CIKARIM
  - CONFIDENCE: [0.0-1.0]

**HYPOTHESES TESTED**:
1. **HIPOTEZ-1**: [hypothesis]
   - Evidence For: [supporting evidence]
   - Evidence Against: [counter-evidence]
   - Status: [VERIFIED | REJECTED]
   - Confidence: [0.0-1.0]

2. **HIPOTEZ-2**: [hypothesis]
   - Evidence For: [supporting evidence]
   - Evidence Against: [counter-evidence]
   - Status: [VERIFIED | REJECTED]
   - Confidence: [0.0-1.0]

**SOLUTION DESIGN**:
- Approach: [fix strategy addressing root cause]
- Files: [specific locations to change]
- Rationale: [why this addresses the ROOT, not symptoms]

**VALIDATION PLAN** (DOGRULAMA):
- Tests Before: [expected failures with evidence]
- Tests After: [expected passes with evidence]
- Verification: [how to prove fix worked]

**PREVENTION STRATEGY**:
- Root Cause Pattern: [category for future reference]
- Pre-mortem Question: [what-if for future planning]
- Safeguards: [tests/checks to prevent recurrence]

**CONFIDENCE SCORE**: [0.0-1.0]
- Based on: [evidence quality | reproduction reliability | hypothesis validation]
```

Standard sections included:
1. **Executive Summary**: Quick overview with confidence score
2. **Symptom Analysis**: Evidence-backed observations
3. **Investigation Trail**: All hypotheses with evidence for/against
4. **Root Cause**: 5-Whys chain with confidence at each level
5. **Solution Design**: Fix addressing root, not symptoms
6. **Validation Plan**: Evidence-based verification
7. **Prevention Strategy**: Pattern extraction for Loop 1 feedback
8. **Code References**: Specific file:line locations

## Examples

### Example 1: Production Error
```
Issue: "Application crashes with 'out of memory' error after running for 2-3 hours"

Agent finds:
- Root Cause: Memory leak in event listener registration
- Location: src/services/eventBus.js:45
- Problem: Event listeners added but never removed
- Solution: Implement cleanup in component unmount
- Prevention: Add memory profiling to CI/CD
```

### Example 2: Integration Failure
```
Issue: "Third-party API calls failing with 401 Unauthorized after token refresh"

Agent finds:
- Root Cause: Token expiry check uses local time, API expects UTC
- Location: src/auth/tokenManager.js:78
- Problem: Timezone mismatch causes premature expiry
- Solution: Use UTC for all time comparisons
- Prevention: Add timezone test cases
```

### Example 3: Performance Regression
```
Issue: "Dashboard load time increased from 2s to 30s after recent update"

Agent finds:
- Root Cause: N+1 query problem introduced in ORM migration
- Location: src/models/Dashboard.js:122
- Problem: Missing eager loading of related entities
- Solution: Add .include() to query with proper joins
- Prevention: Add performance benchmarks to test suite
```

## Advanced Features

### Multi-Layer Analysis
The agent analyzes multiple layers:
- **Code**: Logic errors, type issues, edge cases
- **System**: Resource contention, timing issues, race conditions
- **Integration**: API contracts, data formats, error handling
- **Environment**: Configuration, dependencies, infrastructure
- **Design**: Architectural flaws, missing requirements

### Forensic Techniques
- Stack trace dissection and call path analysis
- Dependency chain mapping and version conflict detection
- Timeline reconstruction of events leading to failure
- Differential analysis (working vs. broken versions)
- Environmental factor isolation

### Evidence-Based Investigation
- Generates multiple hypotheses
- Tests each with targeted experiments
- Rules out unlikely causes systematically
- Validates root cause explains ALL symptoms
- Provides clear evidence trail

## Best Practices

### Provide Complete Context
✅ Include error messages verbatim
✅ Describe reproduction steps clearly
✅ Mention recent changes (code, config, deploys)
✅ Note any patterns (time-based, load-based, etc.)
✅ Share relevant logs or stack traces

### Don't Pre-Diagnose
❌ Avoid "I think it's a memory leak"
✅ Instead: "App slows down over time and crashes"

Let the agent investigate objectively without bias.

### Follow Up Investigation
If the agent needs more information:
- Run suggested commands or tests
- Provide requested logs or configs
- Test hypotheses in your environment
- Verify findings and solutions

## Integration with SPARC

This skill complements SPARC workflows:
- **Debugging phase**: Find root causes before implementing fixes
- **Refinement phase**: Investigate test failures and edge cases
- **Code review**: Analyze potential issues before deployment
- **Post-deployment**: Investigate production incidents

## Technical Details

### Agent Type
`root-cause-analyzer` - Specialized investigative agent

### Capabilities
- File analysis and code tracing
- Log parsing and pattern recognition
- Hypothesis generation and testing
- Systematic elimination of causes
- Solution design and validation

### Tools Used
- Read, Grep, Glob for code examination
- Bash for environment inspection and testing
- Comparative analysis and differential debugging
- Memory and performance profiling guidance

## Troubleshooting

### Agent needs more context
Provide additional information requested:
- Run diagnostic commands suggested
- Share configuration files
- Provide more detailed logs
- Test specific scenarios

### Multiple root causes found
The agent will prioritize by:
- Impact on users
- Ease of reproduction
- Severity of consequences
- Order of occurrence

### Can't reproduce issue
Provide more details about:
- Specific environment (OS, versions, config)
- Data or state that triggers the issue
- Timing or load conditions
- External dependencies or services

## Related Skills

- `functionality-audit`: Validate code actually works
- `theater-detection-audit`: Find placeholder/incomplete code
- `style-audit`: Ensure code quality after fixes

## Success Indicators

✅ Root cause clearly identified with evidence (all WHY levels have DOGRUDAN or CIKARIM support)
✅ Confidence scores >= 0.7 for each WHY level
✅ All hypotheses tested with evidence for/against
✅ Solution addresses ROOT cause, not symptoms (verified by WHY-5 level)
✅ Validation plan has DOGRUDAN evidence requirements
✅ Prevention strategy includes pre-mortem question for Loop 1
✅ Investigation process fully documented with evidence chain

---

**Remember**: This skill finds THE REAL PROBLEM through evidential reasoning and morphological decomposition. Every causal claim requires evidence. Every symptom decomposes through 5-Whys until the root is reached. No speculation without proof. No fixes without addressing the foundational cause.

## Changelog

### v1.1.0 (2025-12-19)
- Applied cognitive lensing with evidential (Turkish) and morphological (Arabic) frames
- Added "Kanitsal Kok Neden Analizi" section requiring evidence for all causal claims
- Added "Al-Itar al-Sarfi li-Tahlil al-Sabab" section for systematic symptom decomposition
- Introduced evidential RCA output template with:
  - Why-Chain decomposition (WHY-1 through ROOT with evidence types and confidence)
  - Hypothesis testing protocol with evidence for/against
  - Evidence type classification (DOGRUDAN, CIKARIM, KORELASYON)
  - Confidence scoring at each level
- Integrated NASA 5-Whys methodology (technical -> systemic -> architectural -> process -> foundational)
- Enhanced output template with evidence requirements throughout
- Added success criteria requiring evidence-backed causal chains
- Enhanced cognitive_frame metadata in YAML frontmatter

### v1.0.0 (Initial Release)
- Systematic reverse engineering root cause analysis
- Deep investigation for complex issues
- Hypothesis generation and testing
- Solution design and validation planning
- Prevention strategies