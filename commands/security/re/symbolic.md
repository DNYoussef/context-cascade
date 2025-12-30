/*============================================================================*/
/* RE:SYMBOLIC COMMAND :: VERILINGUA x VERIX EDITION                   */
/*============================================================================*/

---
name: re:symbolic
version: 1.0.0
binding: skill:agent:RE-Symbolic-Solver
category: reverse-engineering
---

/*----------------------------------------------------------------------------*/
/* S0 COMMAND IDENTITY                                                         */
/*----------------------------------------------------------------------------*/

[define|neutral] COMMAND := {
  name: "re:symbolic",
  binding: "skill:agent:RE-Symbolic-Solver",
  category: "reverse-engineering",
  layer: L1
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S1 PURPOSE                                                                  */
/*----------------------------------------------------------------------------*/

[assert|neutral] PURPOSE := {
  action: "### Phase 1: Binary Loading 1. **Load into Angr**: Create Angr project from binary 2. **Identify Architecture**: Extract from ELF/PE headers 3. **Find",
  outcome: "Workflow completion with quality metrics",
  use_when: "User invokes /re:symbolic"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S2 USAGE SYNTAX                                                             */
/*----------------------------------------------------------------------------*/

[define|neutral] SYNTAX := "/re:symbolic [args]" [ground:given] [conf:1.0] [state:confirmed]

[define|neutral] PARAMETERS := {
  required: {
    binary-path: { type: "string", description: "Path to binary/executable to analyze" }
  },
  optional: {
    options: { type: "object", description: "Additional options" }
  },
  flags: {
    "--target-addr": { description: "Target address to reach (hex, e.g., 0x401337) (req", default: "false" },
    "--target-symbol": { description: "Target symbol/function to reach (e.g., "win", "suc", default: "false" },
    "--avoid-addrs": { description: "Comma-separated addresses to avoid (default: none)", default: "false" }
  }
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S3 EXECUTION FLOW                                                           */
/*----------------------------------------------------------------------------*/

[define|neutral] EXECUTION_STAGES := [
  { stage: 1, action: "**Load into Angr**: Create Angr project from binary", model: "Claude" },
  { stage: 2, action: "**Identify Architecture**: Extract from ELF/PE headers", model: "Claude" },
  { stage: 3, action: "**Find Entry Point**: main(), _start, or custom", model: "Claude" },
  { stage: 4, action: "**Resolve Symbols**: Map function names to addresses", model: "Claude" },
  { stage: 5, action: "**Setup Hooks**: Hook library calls (printf, scanf, etc.)", model: "Claude" }
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
  { command: "/re:symbolic crackme.exe --target-addr 0x401337", description: "Example usage" },
  { command: "/re:symbolic ctf-challenge.elf --target-symbol win", description: "Example usage" },
  { command: "/re:symbolic keygen.exe --target-symbol success --avoid-symb", description: "Example usage" }
] [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S9 CHAIN PATTERNS                                                           */
/*----------------------------------------------------------------------------*/

[define|neutral] CHAINS_WITH := {
  sequential: [
    "/re:symbolic -> /review -> /deploy"
  ],
  parallel: [
    "parallel ::: '/re:symbolic arg1' '/re:symbolic arg2'"
  ]
} [ground:given] [conf:0.95] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S10 RELATED COMMANDS                                                        */
/*----------------------------------------------------------------------------*/

[define|neutral] RELATED := {
  complementary: ["/functionality-audit"],
  alternatives: [],
  prerequisites: []
} [ground:given] [conf:0.95] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S11 META-LOOP INTEGRATION                                                   */
/*----------------------------------------------------------------------------*/

[define|neutral] META_LOOP := {
  expertise_check: {
    domain: "reverse-engineering",
    file: ".claude/expertise/reverse-engineering.yaml",
    fallback: "discovery_mode"
  },
  benchmark: "re:symbolic-benchmark-v1",
  tests: [
    "command_execution_success",
    "workflow_validation"
  ],
  success_threshold: 0.90,
  namespace: "commands/reverse-engineering/re:symbolic/{project}/{timestamp}",
  uncertainty_threshold: 0.85,
  coordination: {
    related_skills: ["agent:RE-Symbolic-Solver"],
    related_agents: ["coder", "tester"]
  }
} [ground:system-policy] [conf:0.98] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S12 MEMORY TAGGING                                                          */
/*----------------------------------------------------------------------------*/

[define|neutral] MEMORY_TAGGING := {
  WHO: "re:symbolic-{session_id}",
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

[commit|confident] <promise>RE:SYMBOLIC_VERILINGUA_VERIX_COMPLIANT</promise> [ground:self-validation] [conf:0.99] [state:confirmed]
