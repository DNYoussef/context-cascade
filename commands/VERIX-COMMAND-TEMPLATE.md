/*============================================================================*/
/* VERIX COMMAND TEMPLATE v1.0.0                                               */
/* Use this template to convert all commands to VERILINGUA x VERIX format     */
/*============================================================================*/

---
name: {command-name}
version: {version}
binding: skill:{bound-skill}
category: {category}
---

/*----------------------------------------------------------------------------*/
/* S0 COMMAND IDENTITY                                                         */
/*----------------------------------------------------------------------------*/

[define|neutral] COMMAND := {
  name: "{command-name}",
  binding: "{bound-skill}",
  category: "{category}",
  layer: L1
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S1 PURPOSE                                                                  */
/*----------------------------------------------------------------------------*/

[assert|neutral] PURPOSE := {
  action: "{what this command does}",
  outcome: "{expected result}",
  use_when: "{trigger conditions}"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S2 USAGE SYNTAX                                                             */
/*----------------------------------------------------------------------------*/

[define|neutral] SYNTAX := "/{command-name} {required_args} [optional_args]" [ground:given] [conf:1.0] [state:confirmed]

[define|neutral] PARAMETERS := {
  required: {
    param1: { type: "string", description: "{desc}" }
  },
  optional: {
    param2: { type: "string", default: "{value}", description: "{desc}" }
  },
  flags: {
    "--flag1": { description: "{desc}", default: "{value}" }
  }
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S3 EXECUTION FLOW                                                           */
/*----------------------------------------------------------------------------*/

[define|neutral] EXECUTION_STAGES := [
  { stage: 1, action: "{step 1}", model: "{which AI}" },
  { stage: 2, action: "{step 2}", model: "{which AI}" },
  { stage: 3, action: "{step 3}", model: "{which AI}" }
] [ground:witnessed:workflow-design] [conf:0.95] [state:confirmed]

[define|neutral] MULTI_MODEL_STRATEGY := {
  gemini_search: "{when to use}",
  gemini_megacontext: "{when to use}",
  codex: "{when to use}",
  claude: "{when to use}"
} [ground:given] [conf:0.95] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S4 INPUT CONTRACT                                                           */
/*----------------------------------------------------------------------------*/

[define|neutral] INPUT_CONTRACT := {
  required: {
    field1: "type - description"
  },
  optional: {
    field2: "type - description"
  },
  prerequisites: [
    "{prerequisite 1}",
    "{prerequisite 2}"
  ]
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S5 OUTPUT CONTRACT                                                          */
/*----------------------------------------------------------------------------*/

[define|neutral] OUTPUT_CONTRACT := {
  artifacts: [
    "{artifact 1}",
    "{artifact 2}"
  ],
  metrics: {
    metric1: "{description}",
    metric2: "{description}"
  },
  state_changes: [
    "{what changes}"
  ]
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S6 SUCCESS INDICATORS                                                       */
/*----------------------------------------------------------------------------*/

[define|neutral] SUCCESS_CRITERIA := {
  pass_conditions: [
    "{condition 1}",
    "{condition 2}"
  ],
  quality_thresholds: {
    threshold1: ">= 0.XX",
    threshold2: "<= 0.XX"
  }
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S7 ERROR HANDLING                                                           */
/*----------------------------------------------------------------------------*/

[define|neutral] ERROR_HANDLERS := {
  error_type_1: {
    symptom: "{what you see}",
    cause: "{why it happens}",
    recovery: "{how to fix}"
  },
  error_type_2: {
    symptom: "{what you see}",
    cause: "{why it happens}",
    recovery: "{how to fix}"
  }
} [ground:witnessed:failure-analysis] [conf:0.92] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S8 EXAMPLES                                                                 */
/*----------------------------------------------------------------------------*/

[define|neutral] EXAMPLES := [
  {
    description: "{what this example shows}",
    command: "/{command-name} {args}",
    expected_output: "{summary of result}"
  }
] [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S9 CHAIN PATTERNS                                                           */
/*----------------------------------------------------------------------------*/

[define|neutral] CHAINS_WITH := {
  sequential: [
    "/{command-name} -> /{next-command} -> /{final-command}"
  ],
  parallel: [
    "parallel ::: '/{command-name} arg1' '/{command-name} arg2'"
  ]
} [ground:given] [conf:0.95] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S10 RELATED COMMANDS                                                        */
/*----------------------------------------------------------------------------*/

[define|neutral] RELATED := {
  complementary: ["/{cmd1}", "/{cmd2}"],
  alternatives: ["/{alt1}"],
  prerequisites: ["/{prereq1}"]
} [ground:given] [conf:0.95] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S11 META-LOOP INTEGRATION                                                   */
/*----------------------------------------------------------------------------*/

[define|neutral] META_LOOP := {
  expertise_check: {
    domain: "{domain}",
    file: ".claude/expertise/{domain}.yaml",
    fallback: "discovery_mode"
  },
  benchmark: "{command-name}-benchmark-v1",
  tests: [
    "command_execution_success",
    "workflow_validation"
  ],
  success_threshold: 0.90,
  namespace: "commands/{category}/{command-name}/{project}/{timestamp}",
  uncertainty_threshold: 0.85,
  coordination: {
    related_skills: ["{skill1}", "{skill2}"],
    related_agents: ["{agent1}", "{agent2}"]
  }
} [ground:system-policy] [conf:0.98] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S12 MEMORY TAGGING                                                          */
/*----------------------------------------------------------------------------*/

[define|neutral] MEMORY_TAGGING := {
  WHO: "{command-name}-{session_id}",
  WHEN: "ISO8601_timestamp",
  PROJECT: "{project-name}",
  WHY: "{command-execution}"
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

[commit|confident] <promise>{COMMAND_NAME}_VERILINGUA_VERIX_COMPLIANT</promise> [ground:self-validation] [conf:0.99] [state:confirmed]
