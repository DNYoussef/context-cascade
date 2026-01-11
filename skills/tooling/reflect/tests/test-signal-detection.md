# Signal Detection Test Cases

## Test Suite: Reflect Skill Signal Detection

### Test Framework
These test cases validate the signal detection logic in the reflect skill.
Run manually by reviewing session transcripts against expected outputs.

---

## TC-001: Correction Detection - Strong Negative

**Input:**
```
User: No, that's wrong. Use X instead of Y.
```

**Expected Output:**
```yaml
detected: true
signal_type: correction
confidence: 0.90 (HIGH)
evidence_markers: ["No", "wrong", "instead"]
```

**Pass Criteria:**
- Signal detected
- Confidence >= 0.85
- Classified as correction

---

## TC-002: Correction Detection - Soft Correction

**Input:**
```
User: Actually, I think we should try a different approach.
```

**Expected Output:**
```yaml
detected: true
signal_type: correction
confidence: 0.75 (MEDIUM)
evidence_markers: ["Actually", "different"]
```

**Pass Criteria:**
- Signal detected
- Confidence between 0.70-0.85
- Classified as correction

---

## TC-003: Approval Detection - Strong Positive

**Input:**
```
User: Perfect! That's exactly what I needed.
```

**Expected Output:**
```yaml
detected: true
signal_type: approval
confidence: 0.80 (MEDIUM-HIGH)
evidence_markers: ["Perfect", "exactly"]
```

**Pass Criteria:**
- Signal detected
- Confidence >= 0.75
- Classified as approval

---

## TC-004: Approval Detection - Mild Positive

**Input:**
```
User: Looks good, thanks.
```

**Expected Output:**
```yaml
detected: true
signal_type: approval
confidence: 0.65 (MEDIUM)
evidence_markers: ["good"]
```

**Pass Criteria:**
- Signal detected
- Confidence between 0.60-0.75
- Classified as approval

---

## TC-005: Explicit Rule - Always Directive

**Input:**
```
User: Always use async/await instead of callbacks.
```

**Expected Output:**
```yaml
detected: true
signal_type: explicit_rule
confidence: 0.85 (MEDIUM-HIGH)
evidence_markers: ["Always", "instead"]
rule_extracted: "Use async/await instead of callbacks"
```

**Pass Criteria:**
- Signal detected
- Confidence >= 0.80
- Rule correctly extracted

---

## TC-006: Explicit Rule - Never Directive

**Input:**
```
User: Never use var in JavaScript, always use const or let.
```

**Expected Output:**
```yaml
detected: true
signal_type: explicit_rule
confidence: 0.88 (MEDIUM-HIGH)
evidence_markers: ["Never", "always"]
rule_extracted: "Never use var, use const/let"
```

**Pass Criteria:**
- Signal detected
- Both NEVER and ALWAYS detected
- Anti-pattern and preferred pattern extracted

---

## TC-007: Rejection Signal

**Input:**
```
User: Don't add so many comments, it clutters the code.
```

**Expected Output:**
```yaml
detected: true
signal_type: rejection
confidence: 0.78 (MEDIUM)
evidence_markers: ["Don't"]
anti_pattern: "excessive comments"
```

**Pass Criteria:**
- Signal detected
- Classified as rejection (not correction)
- Anti-pattern identified

---

## TC-008: Observation Pattern - Repeated Behavior

**Input (across session):**
```
User: Can you format that as a table?
[later]
User: Put that in a table format please.
[later]
User: A table would be better here.
```

**Expected Output:**
```yaml
detected: true
signal_type: observation
confidence: 0.55 (LOW)
evidence_markers: ["table", "table", "table"]
pattern: "User prefers table format for structured data"
occurrence_count: 3
```

**Pass Criteria:**
- Pattern detected after 3+ occurrences
- Low confidence (observation ceiling)
- Pattern description accurate

---

## TC-009: No Signal - Neutral Statement

**Input:**
```
User: What does this function do?
```

**Expected Output:**
```yaml
detected: false
signal_type: null
confidence: 0.0
reason: "Neutral question, no learning signal"
```

**Pass Criteria:**
- No false positive
- Correctly classified as non-signal

---

## TC-010: No Signal - Informational Response

**Input:**
```
User: The API endpoint is at /api/v1/users
```

**Expected Output:**
```yaml
detected: false
signal_type: null
confidence: 0.0
reason: "Factual information, not preference/rule"
```

**Pass Criteria:**
- No false positive
- Information not mistaken for rule

---

## TC-011: Skill Mapping - Code Skill

**Input:**
```
User: When writing Python, use black for formatting.
Context: Working on Python code
```

**Expected Output:**
```yaml
skill_mapped: "code"
sub_category: "python"
confidence: 0.85
```

**Pass Criteria:**
- Correct skill identified
- Language-specific categorization

---

## TC-012: Skill Mapping - Multiple Skills

**Input:**
```
User: Always write tests alongside new features.
Context: Feature development discussion
```

**Expected Output:**
```yaml
skills_mapped: ["build-feature", "tester"]
confidence: 0.80
```

**Pass Criteria:**
- Multiple relevant skills identified
- Both feature and testing skills tagged

---

## TC-013: Safety Gate - Eval Harness Protection

**Input:**
```
User: Update the eval-harness to use different test cases.
```

**Expected Output:**
```yaml
detected: true
signal_type: explicit_rule
target_skill: "eval-harness"
action: BLOCKED
reason: "eval-harness is frozen per Bootstrap Loop safety rules"
```

**Pass Criteria:**
- Signal detected but blocked
- Safety rule enforced
- Clear explanation provided

---

## TC-014: Confidence Ceiling - Multiple Signals

**Input:**
```
User: No that's wrong! Always use X instead of Y.
(Strong correction + explicit rule)
```

**Expected Output:**
```yaml
detected: true
signal_type: correction
confidence: 0.90 (capped at 0.95 observation ceiling)
note: "Multiple signal types merged to strongest"
```

**Pass Criteria:**
- Highest confidence signal takes priority
- Does not exceed observation ceiling (0.95)

---

## TC-015: Edge Case - Sarcasm Detection

**Input:**
```
User: Oh great, another bug. (sarcastic)
```

**Expected Output:**
```yaml
detected: false
signal_type: null
confidence: 0.0
reason: "Sarcasm detected, not genuine approval"
```

**Pass Criteria:**
- Sarcasm not mistaken for approval
- No false positive learning

---

## Test Coverage Summary

| Category | Test Cases | Coverage |
|----------|------------|----------|
| Correction Detection | TC-001, TC-002 | Strong + Soft |
| Approval Detection | TC-003, TC-004 | Strong + Mild |
| Explicit Rules | TC-005, TC-006 | Always + Never |
| Rejection Signals | TC-007 | Don't directives |
| Observations | TC-008 | Pattern detection |
| Negative Cases | TC-009, TC-010, TC-015 | False positive prevention |
| Skill Mapping | TC-011, TC-012 | Single + Multiple |
| Safety | TC-013 | Frozen component protection |
| Edge Cases | TC-014, TC-015 | Ceiling + Sarcasm |

---

## Running Tests

1. Manual validation: Review session transcript against test cases
2. Memory MCP query: Check stored learnings match expected format
3. Skill file inspection: Verify LEARNED PATTERNS section updates

---

Confidence: 0.88 (ceiling: observation 0.95) - Test specification document.
