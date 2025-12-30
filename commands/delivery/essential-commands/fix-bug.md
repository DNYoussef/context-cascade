/*============================================================================*/
/* FIX-BUG COMMAND :: VERILINGUA x VERIX EDITION                   */
/*============================================================================*/

---
name: fix-bug
version: 1.0.0
binding: skill:fix-bug
category: delivery
---

/*----------------------------------------------------------------------------*/
/* S0 COMMAND IDENTITY                                                         */
/*----------------------------------------------------------------------------*/

[define|neutral] COMMAND := {
  name: "fix-bug",
  binding: "skill:fix-bug",
  category: "delivery",
  layer: L1
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S1 PURPOSE                                                                  */
/*----------------------------------------------------------------------------*/

[assert|neutral] PURPOSE := {
  action: "[Define what this command does - the specific action it triggers]",
  outcome: "Workflow completion with quality metrics",
  use_when: "User invokes /fix-bug"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S2 USAGE SYNTAX                                                             */
/*----------------------------------------------------------------------------*/

[define|neutral] SYNTAX := "/fix-bug [args]" [ground:given] [conf:1.0] [state:confirmed]

[define|neutral] PARAMETERS := {
  required: {
    bug_description: { type: "string", description: "Description of the bug" },
    context_path: { type: "string", description: "Directory or file context" }
  },
  optional: {
    options: { type: "object", description: "Additional options" }
  },
  flags: {
    "--depth": { description: "Investigation depth: shallow|normal|deep (default:", default: "false" },
    "--reproduction-steps": { description: "Steps to reproduce (optional)", default: "false" },
    "--error-logs": { description: "Path to error logs (optional)", default: "false" }
  }
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S3 EXECUTION FLOW                                                           */
/*----------------------------------------------------------------------------*/

[define|neutral] EXECUTION_STAGES := [
  { stage: 1, action: "🔍 Deep root cause analysis (Claude RCA Agent)", model: "Claude" },
  { stage: 2, action: "🧠 Context analysis (Gemini MegaContext if large codebase)", model: "Gemini" },
  { stage: 3, action: "💡 Alternative solutions (Multi-model reasoning)", model: "Claude" },
  { stage: 4, action: "🔧 Implement fix (Codex Auto in sandbox)", model: "Codex" },
  { stage: 5, action: "✅ Comprehensive testing (Codex iteration, max 5x)", model: "Codex" },
  { stage: 6, action: "📊 Performance impact analysis", model: "Claude" }
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
  { command: "/fix-bug "API timeout under load" src/api/", description: "Example usage" },
  { command: "/fix-bug "Login fails on Firefox" src/auth/ \", description: "Example usage" },
  { command: "/fix-bug "Database connection fails" src/db/ \", description: "Example usage" }
] [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S9 CHAIN PATTERNS                                                           */
/*----------------------------------------------------------------------------*/

[define|neutral] CHAINS_WITH := {
  sequential: [
    "/fix-bug -> /review -> /deploy"
  ],
  parallel: [
    "parallel ::: '/fix-bug arg1' '/fix-bug arg2'"
  ]
} [ground:given] [conf:0.95] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S10 RELATED COMMANDS                                                        */
/*----------------------------------------------------------------------------*/

[define|neutral] RELATED := {
  complementary: ["/functionality-audit", "/agent-rca", "/codex-auto"],
  alternatives: [],
  prerequisites: []
} [ground:given] [conf:0.95] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S11 META-LOOP INTEGRATION                                                   */
/*----------------------------------------------------------------------------*/

[define|neutral] META_LOOP := {
  expertise_check: {
    domain: "delivery",
    file: ".claude/expertise/delivery.yaml",
    fallback: "discovery_mode"
  },
  benchmark: "fix-bug-benchmark-v1",
  tests: [
    "command_execution_success",
    "workflow_validation"
  ],
  success_threshold: 0.90,
  namespace: "commands/delivery/fix-bug/{project}/{timestamp}",
  uncertainty_threshold: 0.85,
  coordination: {
    related_skills: ["fix-bug"],
    related_agents: ["coder", "tester"]
  }
} [ground:system-policy] [conf:0.98] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S12 MEMORY TAGGING                                                          */
/*----------------------------------------------------------------------------*/

[define|neutral] MEMORY_TAGGING := {
  WHO: "fix-bug-{session_id}",
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

[commit|confident] <promise>FIX_BUG_VERILINGUA_VERIX_COMPLIANT</promise> [ground:self-validation] [conf:0.99] [state:confirmed]
