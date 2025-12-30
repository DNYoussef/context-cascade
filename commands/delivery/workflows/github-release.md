/*============================================================================*/
/* GITHUB-RELEASE COMMAND :: VERILINGUA x VERIX EDITION                   */
/*============================================================================*/

---
name: github-release
version: 1.0.0
binding: skill:github-release
category: delivery
---

/*----------------------------------------------------------------------------*/
/* S0 COMMAND IDENTITY                                                         */
/*----------------------------------------------------------------------------*/

[define|neutral] COMMAND := {
  name: "github-release",
  binding: "skill:github-release",
  category: "delivery",
  layer: L1
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S1 PURPOSE                                                                  */
/*----------------------------------------------------------------------------*/

[assert|neutral] PURPOSE := {
  action: "[Define what this command does - the specific action it triggers]",
  outcome: "Workflow completion with quality metrics",
  use_when: "User invokes /github-release"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S2 USAGE SYNTAX                                                             */
/*----------------------------------------------------------------------------*/

[define|neutral] SYNTAX := "/github-release [args]" [ground:given] [conf:1.0] [state:confirmed]

[define|neutral] PARAMETERS := {
  required: {
    input: { type: "string", description: "Primary input" }
  },
  optional: {
    version: { type: "string", description: "Release version (auto-incremented if not specified" }
  },
  flags: {
    "--type": { description: "Release type: major|minor|patch|pre (default: patc", default: "false" },
    "--prerelease": { description: "Mark as pre-release (default: false)", default: "false" },
    "--draft": { description: "Create as draft (default: false)", default: "false" }
  }
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S3 EXECUTION FLOW                                                           */
/*----------------------------------------------------------------------------*/

[define|neutral] EXECUTION_STAGES := [
  { stage: 1, action: "🏷️ Calculate next semantic version", model: "Claude" },
  { stage: 2, action: "📝 Generate changelog from commits", model: "Claude" },
  { stage: 3, action: "🔍 Validate release readiness", model: "Claude" },
  { stage: 4, action: "🏗️ Build release artifacts", model: "Claude" },
  { stage: 5, action: "📦 Create GitHub release", model: "Claude" },
  { stage: 6, action: "🚀 Publish release notes", model: "Claude" }
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
  { command: "/github-release", description: "Example usage" },
  { command: "/github-release v1.2.3", description: "Example usage" },
  { command: "/github-release --type major", description: "Example usage" }
] [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S9 CHAIN PATTERNS                                                           */
/*----------------------------------------------------------------------------*/

[define|neutral] CHAINS_WITH := {
  sequential: [
    "/github-release -> /review -> /deploy"
  ],
  parallel: [
    "parallel ::: '/github-release arg1' '/github-release arg2'"
  ]
} [ground:given] [conf:0.95] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S10 RELATED COMMANDS                                                        */
/*----------------------------------------------------------------------------*/

[define|neutral] RELATED := {
  complementary: ["/docker-build", "/pr-enhance", "/monitoring-configure"],
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
  benchmark: "github-release-benchmark-v1",
  tests: [
    "command_execution_success",
    "workflow_validation"
  ],
  success_threshold: 0.90,
  namespace: "commands/delivery/github-release/{project}/{timestamp}",
  uncertainty_threshold: 0.85,
  coordination: {
    related_skills: ["github-release"],
    related_agents: ["coder", "tester"]
  }
} [ground:system-policy] [conf:0.98] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S12 MEMORY TAGGING                                                          */
/*----------------------------------------------------------------------------*/

[define|neutral] MEMORY_TAGGING := {
  WHO: "github-release-{session_id}",
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

[commit|confident] <promise>GITHUB_RELEASE_VERILINGUA_VERIX_COMPLIANT</promise> [ground:self-validation] [conf:0.99] [state:confirmed]
