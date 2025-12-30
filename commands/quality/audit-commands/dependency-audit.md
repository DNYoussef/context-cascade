/*============================================================================*/
/* DEPENDENCY-AUDIT COMMAND :: VERILINGUA x VERIX EDITION                   */
/*============================================================================*/

---
name: dependency-audit
version: 1.0.0
binding: skill:dependency-audit
category: audit
---

/*----------------------------------------------------------------------------*/
/* S0 COMMAND IDENTITY                                                         */
/*----------------------------------------------------------------------------*/

[define|neutral] COMMAND := {
  name: "dependency-audit",
  binding: "skill:dependency-audit",
  category: "audit",
  layer: L1
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S1 PURPOSE                                                                  */
/*----------------------------------------------------------------------------*/

[assert|neutral] PURPOSE := {
  action: "**Comprehensive Dependency Analysis**: 1. 🔍 Scan for known CVEs (Common Vulnerabilities and Exposures) 2. 📦 Check package integrity and checksums 3. ⚖",
  outcome: "Workflow completion with quality metrics",
  use_when: "User invokes /dependency-audit"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S2 USAGE SYNTAX                                                             */
/*----------------------------------------------------------------------------*/

[define|neutral] SYNTAX := "/dependency-audit [args]" [ground:given] [conf:1.0] [state:confirmed]

[define|neutral] PARAMETERS := {
  required: {
    input: { type: "string", description: "Primary input" }
  },
  optional: {
    options: { type: "object", description: "Additional options" }
  },
  flags: {
    "--severity": { description: "Minimum severity: low|moderate|high|critical (defa", default: "false" },
    "--update": { description: "Auto-update vulnerable packages (default: false)", default: "false" },
    "--fix-auto": { description: "Auto-fix with compatible versions (default: false)", default: "false" }
  }
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S3 EXECUTION FLOW                                                           */
/*----------------------------------------------------------------------------*/

[define|neutral] EXECUTION_STAGES := [
  { stage: 1, action: "🔍 Scan for known CVEs (Common Vulnerabilities and Exposures)", model: "Claude" },
  { stage: 2, action: "📦 Check package integrity and checksums", model: "Claude" },
  { stage: 3, action: "⚖️ License compliance validation", model: "Claude" },
  { stage: 4, action: "📅 Identify outdated dependencies", model: "Claude" },
  { stage: 5, action: "🔗 Analyze transitive dependencies", model: "Claude" },
  { stage: 6, action: "🎯 Risk scoring and prioritization", model: "Claude" }
] [ground:witnessed:workflow-design] [conf:0.95] [state:confirmed]

[define|neutral] MULTI_MODEL_STRATEGY := {
  gemini_search: "Research and web search tasks",
  gemini_megacontext: "Large codebase analysis",
  codex: "Code generation and prototyping",
  claude: "Architecture and testing"
} [ground:given] [conf:0.95] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S4 INPUT CONTRACT                                                           */
/*----------------------------------------------------------------------------*/

[define|neutral] INPUT_CONTRACT := {
  required: {
    command_args: "string - Command arguments"
  },
  optional: {
    flags: "object - Command flags",
    context: "string - Additional context"
  },
  prerequisites: [
    "Valid project directory",
    "Required tools installed"
  ]
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S5 OUTPUT CONTRACT                                                          */
/*----------------------------------------------------------------------------*/

[define|neutral] OUTPUT_CONTRACT := {
  artifacts: [
    "Execution log",
    "Quality metrics report"
  ],
  metrics: {
    success_rate: "Percentage of successful executions",
    quality_score: "Overall quality assessment"
  },
  state_changes: [
    "Workflow state updated"
  ]
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S6 SUCCESS INDICATORS                                                       */
/*----------------------------------------------------------------------------*/

[define|neutral] SUCCESS_CRITERIA := {
  pass_conditions: [
    "Command executes without errors",
    "Output meets quality thresholds"
  ],
  quality_thresholds: {
    execution_success: ">= 0.95",
    quality_score: ">= 0.80"
  }
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S7 ERROR HANDLING                                                           */
/*----------------------------------------------------------------------------*/

[define|neutral] ERROR_HANDLERS := {
  missing_input: {
    symptom: "Required input not provided",
    cause: "User omitted required argument",
    recovery: "Prompt user for missing input"
  },
  execution_failure: {
    symptom: "Command fails to complete",
    cause: "Underlying tool or service error",
    recovery: "Retry with verbose logging"
  }
} [ground:witnessed:failure-analysis] [conf:0.92] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S8 EXAMPLES                                                                 */
/*----------------------------------------------------------------------------*/

[define|neutral] EXAMPLES := [
  { command: "/dependency-audit", description: "Example usage" },
  { command: "/dependency-audit --update true", description: "Example usage" },
  { command: "/dependency-audit --severity critical", description: "Example usage" }
] [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S9 CHAIN PATTERNS                                                           */
/*----------------------------------------------------------------------------*/

[define|neutral] CHAINS_WITH := {
  sequential: [
    "/dependency-audit -> /review -> /deploy"
  ],
  parallel: [
    "parallel ::: '/dependency-audit arg1' '/dependency-audit arg2'"
  ]
} [ground:given] [conf:0.95] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S10 RELATED COMMANDS                                                        */
/*----------------------------------------------------------------------------*/

[define|neutral] RELATED := {
  complementary: ["/security-audit", "/production-readiness", "/monitoring-configure", "/license-audit"],
  alternatives: [],
  prerequisites: []
} [ground:given] [conf:0.95] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S11 META-LOOP INTEGRATION                                                   */
/*----------------------------------------------------------------------------*/

[define|neutral] META_LOOP := {
  expertise_check: {
    domain: "audit",
    file: ".claude/expertise/audit.yaml",
    fallback: "discovery_mode"
  },
  benchmark: "dependency-audit-benchmark-v1",
  tests: [
    "command_execution_success",
    "workflow_validation"
  ],
  success_threshold: 0.90,
  namespace: "commands/audit/dependency-audit/{project}/{timestamp}",
  uncertainty_threshold: 0.85,
  coordination: {
    related_skills: ["dependency-audit"],
    related_agents: ["coder", "tester"]
  }
} [ground:system-policy] [conf:0.98] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S12 MEMORY TAGGING                                                          */
/*----------------------------------------------------------------------------*/

[define|neutral] MEMORY_TAGGING := {
  WHO: "dependency-audit-{session_id}",
  WHEN: "ISO8601_timestamp",
  PROJECT: "{project-name}",
  WHY: "command-execution"
} [ground:system-policy] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S13 ABSOLUTE RULES                                                          */
/*----------------------------------------------------------------------------*/

[direct|emphatic] RULE_NO_UNICODE := forall(output): NOT(unicode_outside_ascii) [ground:windows-compatibility] [conf:1.0] [state:confirmed]

[direct|emphatic] RULE_EVIDENCE := forall(claim): has(ground) AND has(confidence) [ground:verix-spec] [conf:1.0] [state:confirmed]

[direct|emphatic] RULE_REGISTRY := forall(agent): agent IN AGENT_REGISTRY [ground:system-policy] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* PROMISE                                                                     */
/*----------------------------------------------------------------------------*/

[commit|confident] <promise>DEPENDENCY_AUDIT_VERILINGUA_VERIX_COMPLIANT</promise> [ground:self-validation] [conf:0.99] [state:confirmed]
