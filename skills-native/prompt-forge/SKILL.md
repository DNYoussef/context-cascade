---
name: prompt-forge
description: Meta-prompt that generates improved prompts and templates. Can improve other prompts including Skill Forge and even itself. All improvements are gated by frozen eval harness. Use when optimizing prompts, creating prompt diffs, or running the recursive improvement loop.
---

# Prompt Forge (Meta-Prompt)

## Purpose

Generate improved prompts and templates with:
- Explicit rationale for each change
- Predicted improvement metrics
- Risk assessment
- Actionable diffs

**Key Innovation**: Can improve Skill Forge prompts, then Skill Forge can improve Prompt Forge prompts - creating a recursive improvement loop.

## When to Use

- Optimizing existing prompts for better performance
- Creating prompt diffs with clear rationale
- Running the recursive improvement loop
- Auditing prompts for common issues

## MCP Requirements

### memory-mcp (Required)

**Purpose**: Store proposals, test results, version history

**Activation**:
```bash
claude mcp add memory-mcp npx @modelcontextprotocol/server-memory
```

 a/skills/skill-forge/SKILL.md
+++ b/skills/skill-forge/SKILL.md
@@ -45,7 +45,15 @@ Phase 2: Use Case Crystallization

 ## Phase 3: Structural Architecture

-Design the skill's structure based on progressive disclosure.
+Design the skill's structure based on progressive disclosure.
+
+### Failure Handling (NEW)
+
+For each operation in the skill:
+1. Identify possible failure modes
+2. Define explicit error messages
+3. Specify recovery actions
+4. Include timeout handling
+
+Example:
+```yaml
+error_handling:
+  timeout:
+    threshold: 30s
+    action: "Return partial results with warning"
+  invalid_input:
+    detection: "Validate against schema"
+    action: "Return clear error message with fix suggestion"
+```
```

### Operation 5: Self-Improvement (Recursive)

Improve Prompt Forge itself (with safeguards).

```yaml
self_improvement:
  target: "prompt-forge/SKILL.md"
  safeguards:
    - "Changes must pass eval harness"
    - "Requires 2+ auditor approval"
    - "Previous version archived before commit"
    - "Rollback available for 30 days"

  process:
    1. "Analyze current Prompt Forge for weaknesses"
    2. "Generate improvement proposals"
    3. "Run proposals through eval harness"
    4. "If improved: Create new version"
    5. "If regressed: Reject and log"

  forbidden_changes:
    - "Removing safeguards"
    - "Bypassing eval harness"
    - "Modifying frozen benchmarks"
    - "Disabling rollback"
```

### Operation 6: Apply Cognitive Frame Enhancement [NEW in v2.0]

Transform prompts by embedding cognitive frame activation for improved reasoning.

#### 6.1 Analyze Prompt for Frame Fit

```yaml
frame_analysis:
  target_prompt: "{prompt_content}"

  cognitive_demands:
    completion_tracking: 0.0-1.0  # Aspectual
    source_verification: 0.0-1.0  # Evidential
    audience_calibration: 0.0-1.0  # Hierarchical
    semantic_analysis: 0.0-1.0     # Morphological
    object_comparison: 0.0-1.0     # Classifier

  recommended_frame: {frame}
  confidence: 0.0-1.0
```

#### 6.2 Frame Enhancement Patterns

**Evidential Frame Enhancement (Turkish)**:
```markdown
BEFORE:
"Review this code and report issues."

AFTER:
"## Kanitsal Kod Incelemesi

Review this code. For each finding, mark evidence type:
- [DOGRUDAN/DIRECT]: I tested this and confirmed
- [CIKARIM/INFERRED]: Pattern suggests this could cause problems
- [BILDIRILEN/REPORTED]: Documentation or linter flagged this

Output:
- Issue: {description}
- Evidence: [DIRECT|INFERRED|REPORTED]
- Confidence: {0.0-1.0}"
```

**Aspectual Frame Enhancement (Russian)**:
```markdown
BEFORE:
"Check deployment status."

AFTER:
"## Proverka Statusa Razvertyvaniya

Track each component state:
- [SV:COMPLETED] Polnost'yu zaversheno - Ready
- [NSV:IN_PROGRESS] V protsesse - Working
- [BLOCKED] Ozhidaet zavisimosti - Waiting

Report format:
Component | State | Next Action"
```

**Hierarchical Frame Enhancement (Japanese)**:
```markdown
BEFORE:
"Write documentation for the API."

AFTER:
"## API Dokumento Sakusei

Calibrate register to audience:
- [SONKEIGO] Executives: Formal summary with recommendations
- [TEINEIGO] Developers: Technical details, professional tone
- [CASUAL] Internal notes: Brief, direct

Select register: _______________"
```

#### 6.3 Apply Frame Enhancement

```yaml
enhancement_output:
  original_prompt: "..."
  frame_applied: evidential
  enhanced_prompt: |
    ## Kanitsal Cerceve
    [Original prompt with frame activation and markers]

  markers_added:
    - "[DIRECT]"
    - "[INFERRED]"
    - "[REPORTED]"

  expected_improvement:
    source_tracking: +0.40
    claim_confidence: +0.35
```

#### When to Use Operation 6

- Prompts involving fact-checking or claims -> Evidential
- Prompts tracking completion/progress -> Aspectual
- Prompts for different audiences -> Hierarchical
- Prompts analyzing concepts/terminology -> Morphological
- Prompts comparing/categorizing objects -> Classifier



## Integration with Recursive Loop

### Prompt Forge -> Skill Forge

```javascript
// Prompt Forge improves Skill Forge
Task("Prompt Forge",
  `Analyze skill-forge/SKILL.md and generate improvement proposals:
   - Focus on Phase 2 (Use Case Crystallization)
   - Apply self-consistency technique
   - Add explicit failure handling

   Output: Improvement proposal with diff`,
  "prompt-forge")
```

### Skill Forge -> Prompt Forge

```javascript
// Skill Forge rebuilds improved Prompt Forge
Task("Skill Forge",
  `Using the improvement proposal from Prompt Forge:
   - Apply changes to prompt-forge/SKILL.md
   - Validate against skill creation standards
   - Generate test cases for new version

   Output: prompt-forge-v{N+1}/SKILL.md`,
  "skill-forge")
```

### Eval Harness Gate

```javascript
// All changes gated by frozen eval
Task("Eval Runner",
  `Run eval harness on proposed changes:
   - Benchmark suite: prompt-generation-v1
   - Regression tests: prompt-forge-regression-v1

   Requirements:
   - Improvement > 0% on primary metric
   - 0 regressions
   - No new test failures

   Output: ACCEPT or REJECT with reasoning`,
  "eval-runner")
```



## Version History

Prompt Forge versions itself:

```
prompt-forge/
  SKILL.md           # Current version (v1.0.0)
  .archive/
    SKILL-v0.9.0.md  # Previous versions
  CHANGELOG.md       # What changed and why
  METRICS.md         # Performance over time
```



## Version History

### v2.0.1 (2025-12-19)
- Standardized confidence format from percentage (80%, 50%) to float (0.80, 0.50)
- Standardized expected improvement metrics from percentage (+40%, +35%) to float (+0.40, +0.35)
- Added cross-skill coordination section with all four foundry skills
- Added integration points for cognitive-lensing, skill-forge, agent-creator, eval-harness
- Clarified recursive improvement loop between Skill Forge and Prompt Forge

### v2.0.0 (2025-12-18)
- Added Operation 6: Cognitive Frame Enhancement
- Added frame analysis for prompts (evidential, aspectual, hierarchical, morphological, classifier)
- Added frame enhancement patterns with multi-lingual activation phrases
- Added Principle 4: Cognitive Frame Enhancement to core principles
- Added cognitive-frames tag to metadata
- Enhanced prompt optimization with cross-linguistic reasoning activation
- Expected improvements: +40% source tracking (evidential), +35% claim confidence
- Backward compatible with v1.0.0 operations

### v1.0.0 (Initial Release)
- Core operations: Analyze, Propose, Apply, Diff, Self-Improvement
- Evidence-based techniques: Self-consistency, Program-of-Thought, Plan-and-Solve, Uncertainty Handling
- Frozen eval harness integration
- Recursive improvement loop with safeguards
- Integration with Skill Forge



## Common Anti-Patterns

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| **Improvement Without Metrics** | Proposing changes without predicted impact or success criteria creates unmeasurable modifications that may regress performance | Always include predicted_improvement field with primary_metric, expected_delta, confidence score, and reasoning based on similar improvements |
| **Skipping Risk Assessment** | Applying changes without evaluating regression risk, affected components, or rollback complexity leads to production failures | Require risk_assessment section with regression_risk level (low/medium/high), affected_components list, and rollback_complexity rating before any change |
| **Forced Certainty Under Uncertainty** | Presenting uncertain conclusions as certain creates false confidence and poor decisions when evidence is weak | Implement confidence thresholds - if confidence <0.50 explicitly state uncertainty, list unknowns, propose information-gathering steps, and never guess or fabricate |



## Conclusion

Prompt Forge represents a meta-prompting system designed for recursive self-improvement with rigorous safety constraints. By requiring explicit reasoning, evidence-based techniques, and frozen evaluation gates, it enables systematic prompt enhancement while preventing regression. The key insight is that improvement without measurement and validation is indistinguishable from random change.

This skill excels at optimizing existing prompts for better performance, creating transparent diffs with clear rationale, and running recursive improvement loops where Skill Forge and Prompt Forge improve each other. Use this when you need to enhance prompt quality with confidence that changes actually improve outcomes rather than introduce subtle degradation.

The recursive capability - where Prompt Forge can improve Skill Forge prompts, and Skill Forge can rebuild improved Prompt Forge prompts - creates a powerful self-improvement loop bounded by evaluation harness constraints. This prevents the common failure mode of meta-systems: confident drift into increasingly sophisticated but less effective prompts. The frozen eval harness acts as an objective reality check, ensuring all improvements are genuine rather than illusory.