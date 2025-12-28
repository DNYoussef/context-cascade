---
name: source-credibility-analyzer
description: Standalone tool for automated source evaluation using program-of-thought scoring rubrics. Outputs credibility (1-5), bias (1-5), and priority (1-5) scores with transparent explanations. Use when evaluating research sources, automating general-research-workflow Step 3, or scoring large batches consistently. Single analyst agent workflow (5-15 min per source).
---

# Source Credibility Analyzer

## Purpose

Automate evaluation of research sources using transparent program-of-thought rubrics. Outputs structured JSON with credibility, bias, and priority scores (1-5) plus explanations showing calculation logic. Can be used as standalone tool OR integrated into general-research-workflow Step 3.

## When to Use This Tool

**Use this tool when:**
- ✅ Evaluating research sources for academic projects
- ✅ Automating source classification (general-research-workflow Step 3)
- ✅ Scoring large batches of sources consistently
- ✅ Getting objective second opinion on source quality

**Do NOT use for:**
- ❌ Entertainment content (movies, novels) - not designed for this
- ❌ Source quality already obvious (Nature paper = high, random blog = low)
- ❌ Unique/irreplaceable source (only source on obscure topic) - read anyway

**Decision Tree**: If manual source evaluation takes >10 min → use this tool (saves 15-45 min per source)

## Quick Reference

| Step | Objective | Deliverable | Duration | Quality Gate |
|------|-----------|-------------|----------|--------------|
| 0 | Validate inputs | Confirmed metadata | 30 sec | Required fields present |
| 0.5 | Classify source type | Source category | 1 min | Type assigned |
| 1 | Calculate credibility | Score 1-5 + explanation | 2-5 min | Score justified |
| 2 | Calculate bias | Score 1-5 + explanation | 2-5 min | Score justified |
| 3 | Calculate priority | Score 1-5 + explanation | 1-3 min | Score justified |
| 4 | Resolve conflicts | Final recommendation | 1 min | Logic correct |
| 5 | Generate output | JSON + storage | 1 min | Complete + stored |



## Step-by-Step Workflow

### STEP 0: Validate Input Metadata
**Agent**: analyst
**Objective**: Ensure required metadata is present and valid

**Procedure**:
1. Check for ✅ **required** fields:
   - `title` (string, non-empty)
   - `author` (string, non-empty)
   - `year` (integer, 1500-2025)
   - `venue` (string, non-empty)
   - `type` (string, non-empty)

2. Note ⚠️ **optional** fields if present:
   - `citations` (improves credibility scoring)
   - `doi` (improves credibility scoring)
   - `institution` (improves credibility scoring)
   - `credentials` (improves credibility scoring)
   - `url` (for reference)

3. Validate data types and ranges:
   - Year must be integer 1500-2025
   - All required strings non-empty

4. If validation fails → Return error with missing/invalid field name

**Deliverable**: Validated metadata object

**Quality Gate 0**:
- **GO**: All required fields present, year valid (1500-2025)
- **NO-GO**: Missing/invalid field → Return error to user

-------|---------------------|-------|----------|
| **ACADEMIC** | 4 | Peer-reviewed, standard rubric | Journals, academic books, conference papers |
| **INSTITUTIONAL** | 3 | Check funding source | Government reports, white papers |
| **GENERAL** | 3 | Verify against other sources | Wikipedia, reputable news, expert blogs |
| **PREPRINTS** | 3 | Not yet peer-reviewed, verify claims | arXiv, bioRxiv, SSRN |
| **UNVERIFIED** | 2 | Use with extreme caution | Personal blogs, social media |

**Special Cases**:

1. **Wikipedia**:
   - Credibility: 3 (verifiable, crowd-sourced)
   - Bias: 4 (NPOV policy)
   - Priority: 2 (background only, not citable in academic work)
   - Action: READ_LATER (gateway to primary sources)

2. **Preprints** (arXiv, bioRxiv):
   - Credibility: 3 (not peer-reviewed but often high-quality)
   - Bias: 4 (assume good faith)
   - Priority: Depends on recency and relevance
   - Action: VERIFY_CLAIMS (read but cross-check against peer-reviewed sources)

3. **Gray Literature** (government reports, NGO papers):
   - Credibility: 3-4 (depends on institution reputation)
   - Bias: Check funding source carefully
   - Priority: Depends on topic match

4. **Expert Blogs** (Gwern, LessWrong, Scott Alexander):
   - Credibility: 3 (no formal peer review)
   - Bias: 3-4 (depends on author's agenda)
   - Priority: Depends on expertise match with topic

**💡 Tip**: When category is ambiguous → Default to GENERAL and note uncertainty in output

**Deliverable**: Source category (ACADEMIC | INSTITUTIONAL | GENERAL | PREPRINTS | UNVERIFIED)

**Quality Gate 0.5**:
- **GO**: Category assigned based on decision tree
- **NO-GO**: Unable to classify → Default to GENERAL, flag uncertainty



### STEP 2: Calculate Bias Score (1-5)
**Agent**: analyst
**Objective**: Assess source objectivity and potential bias

**Program-of-Thought Rubric**:

**Baseline Score**:
- Standard: Start at 3 (Neutral)
- **Special Baselines**:
  - Primary sources (historical documents, datasets): Start at 5 (factual records)
  - Opinion pieces (editorials, op-eds): Start at 2 (explicitly opinionated)

**Add +1 for EACH** (max +3):
- ✅ Academic/scholarly source with peer review
- ✅ Presents multiple perspectives or counterarguments
- ✅ Clearly distinguishes facts from opinions
- ✅ Transparent about methodology and limitations
- ✅ No financial conflicts of interest
- ✅ Published by neutral/academic institution (not advocacy group)

**Subtract -1 for EACH** (max -3):
- ❌ Advocacy organization or political think tank
- ❌ Funded by interested party with conflicts (Exxon-funded climate study)
- ❌ One-sided presentation (no counterarguments/limitations)
- ❌ Opinion piece or editorial without labeling
- ❌ Sensationalist language or clickbait title
- ❌ Known partisan publication (Breitbart, Jacobin)

**🚨 Borderline Score Policy**:
- If final score = 2.5 or 3.5 → **Round UP** (benefit of doubt for bias)
- Example: 2.5 → 3, 3.5 → 4

**Final Bias Score**: [1-5, where 5 = least biased, 1 = most biased]

**Calculation Procedure**:
1. Determine baseline (3, or special baseline)
2. Apply each applicable rule (+1 or -1)
3. Sum: Baseline + Adjustments
4. Apply borderline rounding if score ends in .5
5. Cap at 1 (minimum) and 5 (maximum)
6. Generate explanation

**Example**:
```
Source: "Climate Change Impacts Study" by Heartland Institute (2021)
Category: INSTITUTIONAL

Calculation:
Baseline: 3
-1 (Heartland Institute - known climate denial advocacy group)
-1 (Funded by fossil fuel industry - conflicts of interest)
-1 (One-sided - dismisses consensus without balanced counterarguments)
= 0 → capped at 1

Final Bias: 1/5 (highly biased)
Explanation: "Institutional baseline 3, -1 advocacy org, -1 industry funding, -1 one-sided = 0 capped at 1. Strong bias, verify all claims independently."
```

**Deliverable**: Bias score (1-5) + explanation showing baseline + rules + final

**Quality Gate 2**:
- **GO**: Score 1-5, explanation lists baseline and applied rules
- **NO-GO**: Score outside 1-5 or no explanation → Recalculate



### STEP 4: Resolve Conflicting Scores
**Agent**: analyst
**Objective**: Handle edge cases where credibility/bias/priority conflict

**Conflict Resolution Matrix**:

| Credibility | Bias | Priority | Recommendation | Reasoning |
|-------------|------|----------|----------------|-----------|
| ≥4 | ≥3 | ≥4 | **READ_FIRST** | Ideal source: credible + unbiased + relevant |
| ≥3 | ≥3 | ≥3 | **READ_LATER** | Solid source: good quality, moderate priority |
| ≥4 | ≤2 | ANY | **VERIFY_CLAIMS** | Credible but biased: useful but verify |
| ≤2 | ANY | ANY | **SKIP** | Not credible: find better alternative |
| ANY | ≤2 | ≥4 | **VERIFY_CLAIMS** | Needed but biased: read critically |
| ≥4 | ≥3 | ≤2 | **READ_LATER** | Quality background material |

**Conflict Type Handlers**:

**Type 1: High Credibility + High Bias**
- Example: Peer-reviewed paper in advocacy journal (Credibility 4, Bias 2)
- Resolution: VERIFY_CLAIMS
- Reason: "Credible source but biased presentation. Read critically, verify against independent sources."

**Type 2: Low Credibility + Low Bias**
- Example: Anonymous blog with balanced presentation (Credibility 2, Bias 4)
- Resolution: SKIP
- Reason: "Unbiased but not credible. Find authoritative alternative."

**Type 3: High Priority + Low Credibility**
- Example: Only source on obscure topic (Priority 5, Credibility 2)
- Resolution: READ_LATER (with warning)
- Reason: "Relevant but low credibility. Read as last resort, verify everything."

**Type 4: High Credibility + Low Priority**
- Example: Tangential textbook (Credibility 5, Priority 2)
- Resolution: READ_LATER
- Reason: "Authoritative but not directly relevant. Read for context if time permits."

**Deliverable**: Final recommendation (READ_FIRST | READ_LATER | VERIFY_CLAIMS | SKIP) + reasoning + conflict explanation if applicable

**Quality Gate 4**:
- **GO**: Recommendation matches matrix, conflicts explained
- **NO-GO**: Recommendation doesn't match scores → Reapply matrix logic



## Success Metrics

### Quantitative
- ✅ All 3 scores calculated (credibility, bias, priority)
- ✅ All scores valid range (1-5)
- ✅ Explanations show calculations
- ✅ Recommendation matches decision matrix
- ✅ Execution time 5-15 min per source
- ✅ Output stored in Memory MCP

### Qualitative
- ✅ Scores match manual scoring within ±1 point
- ✅ Explanations clearly justify scores with explicit rules
- ✅ Recommendation is actionable
- ✅ Edge cases handled (Wikipedia, preprints, gray literature)
- ✅ Conflicts resolved transparently

-----------|------|------------|
| **Missing required metadata** | 0 | Return error with field name |
| **Invalid year** | 0 | Reject, request correction |
| **Score outside 1-5** | 1-3 | Recalculate with capping |
| **No explanation** | 1-3 | Regenerate with explicit rules |
| **Borderline score (X.5)** | 1-3 | Apply rounding policy |
| **Ambiguous source type** | 0.5 | Default to GENERAL, flag uncertainty |
| **Conflicting scores** | 4 | Apply conflict resolution matrix |
| **Recommendation mismatch** | 4 | Reapply matrix, document conflict |
| **Memory MCP storage fails** | 5 | Retry 3x, fallback to local JSON |



## Process Visualization

See `source-credibility-analyzer-process.dot` for complete workflow diagram showing all steps, gates, and decision points.



**Program-of-Thought Principle**: "Make scoring transparent, auditable, and reproducible through explicit calculations"