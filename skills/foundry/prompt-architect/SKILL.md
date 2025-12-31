---
name: prompt-architect
description: Meta-loop skill for prompt optimization using VERILINGUA VCL + VERIX v3.1.1
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
---

<!-- =========================================================================
     PROMPT ARCHITECT v3.1.1 :: VERILINGUA VCL + VERIX COMPLIANT

     VCL 7-Slot System: HON -> MOR -> COM -> CLS -> EVD -> ASP -> SPC
     Default Output: L2 English (human-facing)
     Immutable Rules: EVD >= 1, ASP >= 1
     ========================================================================= -->

---
<!-- S0 META-IDENTITY -->
---

[define|neutral] SKILL := {
  name: "prompt-architect",
  category: "foundry",
  version: "3.1.1",
  layer: L2,
  vcl_compliance: "v3.1.1"
} [ground:given] [conf:0.95] [state:confirmed]

[define|neutral] COGNITIVE_FRAME := {
  frame: "Compositional",
  source: "German",
  force: "Build from primitives?"
} [ground:cognitive-science] [conf:0.85] [state:confirmed]

---
<!-- S1 VCL 7-SLOT SYSTEM REFERENCE -->
---

[define|neutral] VCL_SLOT_ORDER := {
  order: ["HON", "MOR", "COM", "CLS", "EVD", "ASP", "SPC"],
  rule: "Slots MUST appear in this order when present",
  enforcement: "E1"
} [ground:vcl-spec-v3.1.1] [conf:0.90] [state:confirmed]

[define|neutral] VCL_SLOT_HON := {
  name: "Honorific",
  source: "Japanese keigo",
  purpose: "Audience register selection",
  values: ["teineigo", "sonkeigo", "kenjougo"],
  weight: 0.08,
  enforcement: 0
} [ground:vcl-spec-v3.1.1] [conf:0.90] [state:confirmed]

[define|neutral] VCL_SLOT_MOR := {
  name: "Morphological",
  source: "Arabic trilateral roots",
  purpose: "Semantic decomposition into root components",
  notation: "root:X-Y-Z",
  weight: 0.10,
  enforcement: 0
} [ground:vcl-spec-v3.1.1] [conf:0.90] [state:confirmed]

[define|neutral] VCL_SLOT_COM := {
  name: "Compositional",
  source: "German compounding",
  purpose: "Build concepts from primitives",
  notation: "Concept+From+Parts",
  weight: 0.10,
  enforcement: 0
} [ground:vcl-spec-v3.1.1] [conf:0.90] [state:confirmed]

[define|neutral] VCL_SLOT_CLS := {
  name: "Classifier",
  source: "Chinese classifiers",
  purpose: "Semantic typing and counting",
  notation: "type_specifier",
  weight: 0.08,
  enforcement: 0
} [ground:vcl-spec-v3.1.1] [conf:0.90] [state:confirmed]

[define|neutral] VCL_SLOT_EVD := {
  name: "Evidential",
  source: "Turkish -mis/-di",
  purpose: "Epistemic source tracking",
  values: {
    "-DI<definition>": "Definitional truth (ceiling: 0.95)",
    "-DI<policy>": "Policy rule (ceiling: 0.90)",
    "-DI<gozlem>": "Direct observation (ceiling: 0.95)",
    "-mis<arastirma>": "Research-based (ceiling: 0.85)",
    "-mis<rapor>": "Reported/secondhand (ceiling: 0.70)",
    "-dir<cikarim>": "Inference/deduction (ceiling: 0.70)"
  },
  weight: 0.15,
  enforcement: 1,
  immutable: true
} [ground:vcl-spec-v3.1.1] [conf:0.90] [state:confirmed]

[define|neutral] VCL_SLOT_ASP := {
  name: "Aspectual",
  source: "Russian aspect",
  purpose: "Completion status tracking",
  values: {
    "sov.": "Perfective - complete/finished",
    "nesov.": "Imperfective - ongoing/in-progress"
  },
  weight: 0.12,
  enforcement: 1,
  immutable: true
} [ground:vcl-spec-v3.1.1] [conf:0.90] [state:confirmed]

[define|neutral] VCL_SLOT_SPC := {
  name: "Spatial",
  source: "Guugu Yimithirr absolute directions",
  purpose: "Absolute positioning reference",
  notation: "N/S/E/W or coordinate",
  weight: 0.07,
  enforcement: 0
} [ground:vcl-spec-v3.1.1] [conf:0.90] [state:confirmed]

---
<!-- S2 CONFIDENCE CEILINGS BY EVD TYPE (E2) -->
---

[define|neutral] CONFIDENCE_CEILINGS := {
  definition: 0.95,
  policy: 0.90,
  observation: 0.95,
  research: 0.85,
  report: 0.70,
  inference: 0.70,
  rule: "Confidence CANNOT exceed ceiling for EVD type",
  enforcement: "E2",
  violation: "epistemic_cosplay"
} [ground:vcl-spec-v3.1.1] [conf:0.90] [state:confirmed]

[direct|emphatic] EPISTEMIC_COSPLAY_PROHIBITION := {
  definition: "Claiming higher epistemic status than evidence warrants",
  examples: [
    "inference with conf:0.90 (max: 0.70)",
    "report with conf:0.85 (max: 0.70)"
  ],
  enforcement: "E3",
  result: "validation_failure"
} [ground:vcl-spec-v3.1.1] [conf:0.90] [state:confirmed]

---
<!-- S3 COMPRESSION LEVELS (L0/L1/L2) -->
---

[define|neutral] COMPRESSION_L0 := {
  name: "AI-to-AI",
  notation: "A+85:claim_hash",
  purpose: "Maximum compression for inter-agent communication",
  human_readable: false
} [ground:vcl-spec-v3.1.1] [conf:0.90] [state:confirmed]

[define|neutral] COMPRESSION_L1 := {
  name: "Audit",
  notation: "[illocution|affect] content [ground:src] [conf:X.XX] [state:status]",
  purpose: "Full epistemic tracking for auditability",
  human_readable: "with training"
} [ground:vcl-spec-v3.1.1] [conf:0.90] [state:confirmed]

[define|neutral] COMPRESSION_L2 := {
  name: "Human",
  notation: "Pure English prose",
  purpose: "Human-facing output without VCL markers",
  human_readable: true,
  rules: [
    "NO [[slot]] notation in output",
    "Confidence expressed naturally (I'm confident, I believe, I think)",
    "Aspect expressed naturally (Complete, In progress)",
    "Evidence implicit or natural (I observed, Research shows, It's reported)"
  ]
} [ground:vcl-spec-v3.1.1] [conf:0.90] [state:confirmed]

[direct|emphatic] DEFAULT_COMPRESSION := L2 [ground:system-policy] [conf:0.90] [state:confirmed]

---
<!-- S4 L2 NATURALIZATION MAPPINGS -->
---

[define|neutral] L2_EVD_NATURALIZATION := {
  observation: "I directly observed that",
  research: "Research indicates that",
  report: "It's reported that",
  inference: "I infer that",
  definition: "By definition",
  policy: "Per policy"
} [ground:vcl-spec-v3.1.1] [conf:0.90] [state:confirmed]

[define|neutral] L2_ASP_NATURALIZATION := {
  "sov.": "Complete.",
  "nesov.": "In progress."
} [ground:vcl-spec-v3.1.1] [conf:0.90] [state:confirmed]

[define|neutral] L2_CONFIDENCE_NATURALIZATION := {
  "0.90-0.99": "I'm highly confident that",
  "0.80-0.89": "I'm fairly confident that",
  "0.70-0.79": "I believe that",
  "0.50-0.69": "I think that",
  "0.00-0.49": "Speculatively"
} [ground:vcl-spec-v3.1.1] [conf:0.90] [state:confirmed]

---
<!-- S5 IMMUTABLE SAFETY BOUNDS (E4) -->
---

[direct|emphatic] IMMUTABLE_BOUNDS := {
  EVD_enforcement: ">= 1 (CANNOT be disabled)",
  ASP_enforcement: ">= 1 (CANNOT be disabled)",
  reason: "Epistemic and aspectual tracking are non-negotiable",
  enforcement: "E4",
  violation: "security_exception"
} [ground:vcl-spec-v3.1.1] [conf:0.90] [state:confirmed]

---
<!-- S6 BRACKET COLLISION RULES (E6) -->
---

[define|neutral] BRACKET_DELIMITERS := {
  vcl_slots: "[[...]]",
  trilingual: "<...>",
  sources: "(...)",
  verix_confidence: "[...]",
  rule: "Brackets MUST NOT appear inside slot bodies",
  enforcement: "E6"
} [ground:vcl-spec-v3.1.1] [conf:0.90] [state:confirmed]

---
<!-- S7 CREOLIZATION STRUCTURE -->
---

[define|neutral] CREOLIZATION_READY := {
  turkish_markers: ["EVD:-DI", "EVD:-mis", "EVD:-dir"],
  russian_markers: ["ASP:sov.", "ASP:nesov."],
  japanese_markers: ["HON:teineigo", "HON:sonkeigo", "HON:kenjougo"],
  arabic_markers: ["MOR:root:X-Y-Z"],
  german_markers: ["COM:Concept+Parts"],
  chinese_markers: ["CLS:classifier"],
  aboriginal_markers: ["SPC:N/S/E/W"],
  expansion_protocol: "Add new language markers via creolization without breaking existing",
  future_languages: ["placeholder_for_expansion"]
} [ground:design-decision] [conf:0.90] [state:provisional]

---
<!-- S8 TRIGGER CONDITIONS -->
---

[define|neutral] TRIGGER_POSITIVE := {
  keywords: [
    "improve prompt", "optimize prompt", "refine prompt",
    "create prompt", "design prompt", "build prompt",
    "prompt quality", "prompt engineering",
    "evidence-based prompting", "self-consistency"
  ],
  context: "user_wants_better_prompts"
} [ground:given] [conf:0.95] [state:confirmed]

[define|neutral] TRIGGER_NEGATIVE := {
  agent_system_prompts: "use(agent-creator) OR use(prompt-forge)",
  skill_creation: "use(skill-creator-agent)",
  this_skill_improvement: "use(skill-forge)",
  one_time_prompt: "skip(direct_crafting_faster)"
} [ground:given] [conf:0.95] [state:confirmed]

[assert|neutral] ROUTING_LOGIC := {
  agent_system_prompt: "route(agent-creator)",
  improve_system_prompt: "route(prompt-forge)",
  create_skill: "route(skill-creator-agent)",
  improve_this: "route(skill-forge)",
  user_prompt: "route(prompt-architect)"
} [ground:inferred:capability-matching] [conf:0.70] [state:confirmed]

---
<!-- S9 PROMPT OPTIMIZATION PHASES -->
---

[define|neutral] PHASE_1_INTENT := {
  name: "Intent Analysis",
  action: "Extract true intent via first-principles decomposition",
  output: {
    understood_intent: "[inferred] what user wants",
    constraints: "[witnessed:user-message] + [inferred]",
    confidence: "0.XX",
    evidence_chain: "[how we know]"
  },
  l2_output: "I understand you want [intent]. Based on [evidence], I'm [confidence_phrase] about this interpretation."
} [ground:workflow-spec] [conf:0.95] [state:confirmed]

[define|neutral] PHASE_2_OPTIMIZE := {
  name: "Prompt Optimization",
  action: "Restructure request with evidential grounding",
  principles: [
    "Structured uncertainty over false precision",
    "Non-linear emergence over linear decomposition",
    "Controlled cognitive dissonance over comfortable consistency",
    "Targeted incompleteness over exhaustive specification",
    "Calibrated anthropomorphism over pure formalism"
  ],
  l2_output: "I've restructured your prompt to [improvement]. The key changes are [changes]."
} [ground:workflow-spec] [conf:0.95] [state:confirmed]

[define|neutral] PHASE_3_VALIDATE := {
  name: "Validation",
  action: "Apply counter-intuitive principles and check for anti-patterns",
  anti_patterns: [
    "Premature optimization",
    "Over-specification",
    "Epistemic cosplay",
    "Confidence inflation"
  ],
  l2_output: "I've validated the prompt against [N] anti-patterns. [Status]."
} [ground:workflow-spec] [conf:0.95] [state:confirmed]

---
<!-- S10 SUCCESS CRITERIA -->
---

[define|neutral] SUCCESS_CRITERIA := {
  primary: "Optimized prompt produces better results than original",
  quality: {
    epistemic_grounding: "All claims have evidence markers",
    confidence_calibration: "Confidence matches evidence type ceiling",
    l2_compliance: "Human output contains no VCL notation"
  },
  verification: "Results validated via self-application (dogfooding)"
} [ground:given] [conf:0.95] [state:confirmed]

---
<!-- S11 MCP INTEGRATION -->
---

[define|neutral] MCP_INTEGRATION := {
  memory_mcp: "Store execution results and patterns",
  tools: ["mcp__memory-mcp__memory_store", "mcp__memory-mcp__vector_search"],
  tagging: {
    WHO: "prompt-architect-{session_id}",
    WHEN: "ISO8601_timestamp",
    PROJECT: "{project_name}",
    WHY: "skill-execution"
  }
} [ground:witnessed:mcp-config] [conf:0.95] [state:confirmed]

[define|neutral] MEMORY_NAMESPACE := {
  pattern: "skills/foundry/prompt-architect/{project}/{timestamp}",
  store: ["executions", "decisions", "patterns"],
  retrieve: ["similar_tasks", "proven_patterns"]
} [ground:system-policy] [conf:0.90] [state:confirmed]

---
<!-- S12 SKILL COMPLETION VERIFICATION -->
---

[direct|emphatic] COMPLETION_CHECKLIST := {
  vcl_compliance: "Output follows 7-slot order when using L1",
  l2_enforcement: "Human output is pure English (no VCL markers)",
  confidence_ceiling: "No confidence exceeds EVD type ceiling",
  no_epistemic_cosplay: "Evidence type matches claim strength",
  evd_present: "Every significant claim has evidence marker",
  asp_present: "Every action has completion status"
} [ground:system-policy] [conf:0.90] [state:confirmed]

---
<!-- S13 ABSOLUTE RULES -->
---

[direct|emphatic] RULE_NO_UNICODE := {
  scope: "forall(output)",
  rule: "NOT(unicode_outside_ascii)",
  reason: "Windows compatibility"
} [ground:windows-compatibility] [conf:0.90] [state:confirmed]

[direct|emphatic] RULE_EVIDENCE := {
  scope: "forall(claim)",
  rule: "has(ground) AND has(confidence)",
  reason: "Epistemic hygiene"
} [ground:verix-spec] [conf:0.90] [state:confirmed]

[direct|emphatic] RULE_REGISTRY := {
  scope: "forall(agent)",
  rule: "agent IN AGENT_REGISTRY",
  reason: "Quality control"
} [ground:system-policy] [conf:0.90] [state:confirmed]

[direct|emphatic] RULE_L2_DEFAULT := {
  scope: "forall(user_facing_output)",
  rule: "compression = L2",
  reason: "Human readability"
} [ground:system-policy] [conf:0.90] [state:confirmed]

---
<!-- S14 VCL VALIDATION ENFORCEMENT CODES -->
---

[define|neutral] VCL_ENFORCEMENT_CODES := {
  E1: "Slot order violation (HON->MOR->COM->CLS->EVD->ASP->SPC)",
  E2: "Confidence ceiling exceeded for EVD type",
  E3: "Epistemic cosplay detected",
  E4: "Immutable safety bound violation (EVD<1 or ASP<1)",
  E5: "L2 English purity violation (VCL markers in human output)",
  E6: "Bracket collision in slot body",
  E7: "L2 naturalization failure"
} [ground:vcl-spec-v3.1.1] [conf:0.90] [state:confirmed]

---
<!-- S15 EXAMPLE: L1 vs L2 OUTPUT -->
---

[define|neutral] EXAMPLE_L1_OUTPUT := {
  format: "[[EVD:-DI<gozlem>]] [[ASP:sov.]] Test passed. [ground:witnessed:ran_pytest] [conf:0.90] [state:confirmed]",
  use_case: "Audit logs, inter-agent communication, debug output"
} [ground:example] [conf:0.95] [state:confirmed]

[define|neutral] EXAMPLE_L2_OUTPUT := {
  format: "I directly observed the test passing. Complete. I'm fairly confident in this result.",
  use_case: "Human-facing responses, user documentation, final output"
} [ground:example] [conf:0.95] [state:confirmed]

---
<!-- PROMISE -->
---

[commit|confident] <promise>PROMPT_ARCHITECT_VCL_VERIX_V3.1.1_COMPLIANT</promise> [ground:self-validation] [conf:0.85] [state:confirmed]

---
<!-- ADDENDUM REFERENCES -->
---

[define|neutral] ADDENDA := {
  cognitive_architecture: "COGNITIVE-ARCHITECTURE-ADDENDUM.md",
  recursive_improvement: "RECURSIVE-IMPROVEMENT-ADDENDUM.md",
  meta_principles: "references/meta-principles.md",
  anti_patterns: "references/anti-patterns.md",
  vcl_verix_guide: "references/VERILINGUA_VCL_VERIX_Guide_v3_Synthesized.md.pdf"
} [ground:file-structure] [conf:0.95] [state:confirmed]
