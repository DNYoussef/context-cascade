/*============================================================================*/
/* SMART-BUG-FIX SKILL :: VERILINGUA x VERIX EDITION                      */
/*============================================================================*/

---
name: smart-bug-fix
version: 1.1.0
description: |
  [assert|neutral] Intelligent bug fixing workflow combining root cause analysis, multi-model reasoning, Codex auto-fix, and comprehensive testing. Uses RCA agent, Codex iteration, and validation to systematically fix b [ground:given] [conf:0.95] [state:confirmed]
category: delivery
tags:
- debugging
- rca
- codex
- testing
- essential
author: ruv
cognitive_frame:
  primary: evidential
  goal_analysis:
    first_order: "Execute smart-bug-fix workflow"
    second_order: "Ensure quality and consistency"
    third_order: "Enable systematic delivery processes"
---

/*----------------------------------------------------------------------------*/
/* S0 META-IDENTITY                                                            */
/*----------------------------------------------------------------------------*/

[define|neutral] SKILL := {
  name: "smart-bug-fix",
  category: "delivery",
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
  keywords: ["smart-bug-fix", "delivery", "workflow"],
  context: "user needs smart-bug-fix capability"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S3 CORE CONTENT                                                             */
/*----------------------------------------------------------------------------*/

# Smart Bug Fix

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



## Kanitsal Hata Ayiklama (Evidential Debugging)

Every bug hypothesis requires evidence. The evidential frame ensures no fix is applied without proof of causation.

**Evidence Requirements**:
- **GOZLEM** (Observation): Bug observed with concrete reproduction steps
- **HIPOTEZ** (Hypothesis): Theory X based on evidence Y
- **DOGRULAMA** (Verification): Fix verified by test results Z
- **RED** (Rejection): Hypothesis rejected due to counter-evidence W

**Example**:
```
GOZLEM: API timeout after 30s under load (reproduction: 1000 concurrent requests)
HIPOTEZ: Database connection pool exhausted (evidence: pool size=10, active=10, waiting=990)
DOGRULAMA: Increased pool to 100, timeout resolved (evidence: 0 timeouts in 10k requests)
```

## Al-Itar al-Sarfi li-Tahlil al-Sabab (Root Cause Morphology)

Symptoms are composed of causes. Decompose systematically using the "Why Chain" until the root is reached.

**Morphological Decomposition**:
- **SYMPTOM**: Observable error or behavior (surface manifestation)
- **CAUSE-1**: Immediate cause (why-1: "Why did this symptom occur?")
- **CAUSE-2**: Deeper cause (why-2: "Why did cause-1 occur?")
- **ROOT**: True root cause (why-N: "Why did cause-(N-1) occur?" until no further "why" exists)

**Example**:
```
SYMPTOM: Login fails on Firefox
CAUSE-1: JWT token not in cookie (why-1)
CAUSE-2: SameSite=Strict blocks cross-site cookies (why-2)
ROOT: Auth server on different subdomain than app (why-3 - architectural root)
```

**NASA 5 Whys Integration**:
The morphological frame is implemented through the 5 Whys methodology:
1. Why-1: Immediate cause (technical layer)
2. Why-2: Systemic cause (design layer)
3. Why-3: Process cause (architectural layer)
4. Why-4: Cultural cause (organizational layer)
5. Why-5: Root cause (foundational layer)

## When to Use This Skill

- **Domain-Specific Work**: Tasks requiring specialized domain knowledge
- **Complex Problems**: Multi-faceted challenges needing systematic approach
- **Best Practice Implementation**: Following industry-standard methodologies
- **Quality-Critical Work**: Production code requiring high standards
- **Team Collaboration**: Coordinated work following shared processes

## When NOT to Use This Skill

- **Outside Domain**: Tasks outside this skill specialty area
- **Incompatible Tech Stack**: Technologies not covered by this skill
- **Simple Tasks**: Trivial work not requiring specialized knowledge
- **Exploratory Work**: Experimental code without production requirements

## Success Criteria

- [ ] Implementation complete and functional
- [ ] Tests passing with adequate coverage
- [ ] Code reviewed and approved
- [ ] Documentation updated
- [ ] Performance benchmarks met
- [ ] Security considerations addressed
- [ ] Deployed or integrated successfully

## Edge Cases to Handle

- **Legacy Integration**: Working with older codebases or deprecated APIs
- **Missing Dependencies**: Unavailable libraries or external services
- **Version Conflicts**: Dependency version incompatibilities
- **Data Issues**: Malformed input or edge case data
- **Concurrency**: Race conditions or synchronization challenges
- **Error Handling**: Graceful degradation and recovery

## Guardrails

- **NEVER** skip testing to ship faster
- **ALWAYS** follow domain-specific best practices
- **NEVER** commit untested or broken code
- **ALWAYS** document complex logic and decisions
- **NEVER** hardcode sensitive data or credentials
- **ALWAYS** validate input and handle errors gracefully
- **NEVER** deploy without reviewing changes

## Evidence-Based Validation

- [ ] Automated tests passing
- [ ] Code linter/formatter passing
- [ ] Security scan completed
- [ ] Performance within acceptable range
- [ ] Manual testing completed
- [ ] Peer review approved
- [ ] Documentation reviewed

## Purpose

Systematically debug and fix bugs using root cause analysis, multi-model reasoning, 

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
  pattern: "skills/delivery/smart-bug-fix/{project}/{timestamp}",
  store: ["executions", "decisions", "patterns"],
  retrieve: ["similar_tasks", "proven_patterns"]
} [ground:system-policy] [conf:1.0] [state:confirmed]

[define|neutral] MEMORY_TAGGING := {
  WHO: "smart-bug-fix-{session_id}",
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

[commit|confident] <promise>SMART_BUG_FIX_VERILINGUA_VERIX_COMPLIANT</promise> [ground:self-validation] [conf:0.99] [state:confirmed]
