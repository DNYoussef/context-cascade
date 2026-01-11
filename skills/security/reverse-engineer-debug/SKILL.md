/*============================================================================*/
/* SKILL SKILL :: VERILINGUA x VERIX EDITION                      */
/*============================================================================*/

---
name: SKILL
version: 1.1.0
description: |
  [assert|neutral] Perform systematic reverse engineering root cause analysis to debug issues and find real underlying problems [ground:given] [conf:0.95] [state:confirmed]
category: security
tags:
- debugging
- rca
- root-cause-analysis
- reverse-engineering
- investigation
author: system
cognitive_frame:
  primary: evidential
  goal_analysis:
    first_order: "Execute SKILL workflow"
    second_order: "Ensure quality and consistency"
    third_order: "Enable systematic security processes"
---

/*----------------------------------------------------------------------------*/
/* S0 META-IDENTITY                                                            */
/*----------------------------------------------------------------------------*/

[define|neutral] SKILL := {
  name: "SKILL",
  category: "security",
  version: "1.1.0",
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
  keywords: ["SKILL", "security", "workflow"],
  context: "user needs SKILL capability"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S3 CORE CONTENT                                                             */
/*----------------------------------------------------------------------------*/

# Reverse Engineer Debug Skill

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



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

**SYMPTOM**: [Observable error o

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
  pattern: "skills/security/SKILL/{project}/{timestamp}",
  store: ["executions", "decisions", "patterns"],
  retrieve: ["similar_tasks", "proven_patterns"]
} [ground:system-policy] [conf:1.0] [state:confirmed]

[define|neutral] MEMORY_TAGGING := {
  WHO: "SKILL-{session_id}",
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

[commit|confident] <promise>SKILL_VERILINGUA_VERIX_COMPLIANT</promise> [ground:self-validation] [conf:0.99] [state:confirmed]
