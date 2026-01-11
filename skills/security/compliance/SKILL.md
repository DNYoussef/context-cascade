/*============================================================================*/
/* COMPLIANCE SKILL :: VERILINGUA x VERIX EDITION                      */
/*============================================================================*/

---
name: compliance
version: 1.0.0
description: |
  [assert|neutral] Regulatory compliance validation and documentation for GDPR, HIPAA, SOC 2, PCI-DSS, and ISO 27001. Use when implementing compliance controls, conducting compliance audits, or preparing for certificati [ground:given] [conf:0.95] [state:confirmed]
category: security
tags:
- security
- compliance
- safety
author: ruv
cognitive_frame:
  primary: evidential
  goal_analysis:
    first_order: "Execute compliance workflow"
    second_order: "Ensure quality and consistency"
    third_order: "Enable systematic security processes"
---

/*----------------------------------------------------------------------------*/
/* S0 META-IDENTITY                                                            */
/*----------------------------------------------------------------------------*/

[define|neutral] SKILL := {
  name: "compliance",
  category: "security",
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
  keywords: ["compliance", "security", "workflow"],
  context: "user needs compliance capability"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S3 CORE CONTENT                                                             */
/*----------------------------------------------------------------------------*/

## When to Use This Skill

Use this skill when conducting compliance audits, implementing regulatory controls, preparing for certification audits, validating GDPR/HIPAA/SOC2/PCI-DSS/ISO27001 adherence, or documenting security and privacy practices for regulated industries.

## When NOT to Use This Skill

Do NOT use for non-regulated applications, internal tools without compliance requirements, proof-of-concept projects, or general security audits (use security-analyzer instead). Avoid using for unauthorized compliance testing of third-party systems.

## Success Criteria
- [assert|neutral] All applicable regulatory requirements identified with evidence mapping [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] Compliance gaps documented with severity ratings (critical/high/medium/low) [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] Controls implemented with validation tests (automated where possible) [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] Evidence collection automated with audit trail timestamps [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] Remediation plans created for all gaps with assigned owners [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] Compliance score >90% for target framework [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] Zero critical violations remaining before certification [ground:acceptance-criteria] [conf:0.90] [state:provisional]

## Edge Cases & Challenges

- Multi-jurisdiction compliance (GDPR + CCPA + local regulations)
- Legacy systems without compliance documentation
- Third-party services requiring BAA/DPA agreements
- Encrypted data requiring key escrow for compliance
- Real-time compliance monitoring vs periodic audits
- Conflicting requirements between frameworks
- Continuous compliance vs point-in-time certification

## Guardrails (CRITICAL SECURITY RULES)
- [assert|emphatic] NEVER: implement compliance controls on unauthorized systems [ground:policy] [conf:0.98] [state:confirmed]
- [assert|emphatic] NEVER: collect or store PII/PHI without proper encryption and access controls [ground:policy] [conf:0.98] [state:confirmed]
- [assert|emphatic] NEVER: bypass security controls to achieve compliance scores [ground:policy] [conf:0.98] [state:confirmed]
- [assert|emphatic] NEVER: generate false compliance evidence or documentation [ground:policy] [conf:0.98] [state:confirmed]
- [assert|neutral] ALWAYS: document evidence collection methods with timestamps [ground:policy] [conf:0.98] [state:confirmed]
- [assert|neutral] ALWAYS: validate controls through independent testing [ground:policy] [conf:0.98] [state:confirmed]
- [assert|neutral] ALWAYS: obtain legal review for compliance interpretations [ground:policy] [conf:0.98] [state:confirmed]
- [assert|neutral] ALWAYS: maintain audit trails for all compliance activities [ground:policy] [conf:0.98] [state:confirmed]
- [assert|neutral] ALWAYS: use encryption at rest and in transit for sensitive data [ground:policy] [conf:0.98] [state:confirmed]
- [assert|neutral] ALWAYS: implement least-privilege access for compliance tools [ground:policy] [conf:0.98] [state:confirmed]

## Evidence-Based Validation

All compliance findings MUST be validated through:
1. **Automated scanning** - Use compliance scanning tools with documented results
2. **Manual verification** - Independent review of at least 20% of automated findings
3. **Evidence collection** - Screenshots, logs, configurations with timestamps
4. **Cross-validation** - Multiple methods confirm same finding (tool + manual + audit)
5. **Expert review** - Compliance specialist validates critical findings
6. **Remediation testing** - Verify fixes resolve violations without introducing new gaps

# Compliance - Regulatory Standards Validation

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



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
  pattern: "skills/security/compliance/{project}/{timestamp}",
  store: ["executions", "decisions", "patterns"],
  retrieve: ["similar_tasks", "proven_patterns"]
} [ground:system-policy] [conf:1.0] [state:confirmed]

[define|neutral] MEMORY_TAGGING := {
  WHO: "compliance-{session_id}",
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

[commit|confident] <promise>COMPLIANCE_VERILINGUA_VERIX_COMPLIANT</promise> [ground:self-validation] [conf:0.99] [state:confirmed]
