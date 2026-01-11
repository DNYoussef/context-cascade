# Source Credibility Analyzer - Complete Scoring Examples

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



**Purpose**: 5 end-to-end examples showing input → calculations → output for diverse source types

**Pattern**: Each example shows:
1. Input metadata
2. Step-by-step calculations (Steps 0.5 → 1 → 2 → 3 → 4)
3. Output JSON
4. Explanation of scoring logic

---

## Example 1: ✅ Academic Paper (Ideal Source)

### Input Metadata
```json
{
  "title": "Attention Is All You Need",
  "author": "Vaswani et al.",
  "year": 2017,
  "venue": "NeurIPS (Neural Information Processing Systems)",
  "type": "conference paper",
  "citations": 95000,
  "doi": "10.48550/arXiv.1706.03762",
  "institution": "Google Research",
  "credentials": "PhD researchers"
}
```

### Step-by-Step Calculation

**Step 0.5: Classify Source Type**
```
Is peer-reviewed? → YES (NeurIPS is top-tier peer-reviewed conference)
Category: ACADEMIC
Credibility Baseline: 4
```

**Step 1: Calculate Credibility**
```
Baseline: 4 (ACADEMIC)
+1 (Peer-reviewed: NeurIPS)
+1 (Authors: PhDs from Google Research)
+1 (95,000 citations - extremely influential)
+1 (Has DOI)
= 8 → capped at 5

Final Credibility: 5/5
Explanation: "Academic baseline 4, +1 peer-reviewed top conference, +1 PhD researchers, +1 95k citations, +1 DOI = 8 capped at 5. Seminal paper in field."
```

**Step 2: Calculate Bias**
```
Baseline: 3
+1 (Peer-reviewed academic paper)
+1 (Transparent methodology - code released)
+1 (No conflicts of interest)
= 6 → capped at 5

Final Bias: 5/5
Explanation: "Baseline 3, +1 peer-reviewed, +1 transparent methodology, +1 no conflicts = 6 capped at 5. Objective research."
```

**Step 3: Calculate Priority**
```
Baseline: 3
+1 (Recent: 2017 for fast-moving AI field = ≤5 years acceptable, now 8 years but seminal)
+1 (Directly relevant to NLP/transformers research)
+1 (95k citations - foundational work)
+1 (Primary source - introduced transformer architecture)
= 7 → capped at 5

Check credibility/bias: Credibility 5, Bias 5 → No penalty

Final Priority: 5/5
Explanation: "Baseline 3, +1 seminal (offsets age), +1 directly relevant, +1 extremely cited, +1 primary source = 7 capped at 5. Essential reading for NLP."
```

**Step 4: Resolve Conflicts**
```
Credibility: 5, Bias: 5, Priority: 5
Matrix: ≥4 + ≥3 + ≥4 → READ_FIRST
No conflicts detected

Recommendation: READ_FIRST
Reason: "Ideal source: highest credibility, zero bias, maximum priority. Foundational paper for transformer research."
```

### Output JSON
```json
{
  "source": {
    "title": "Attention Is All You Need",
    "author": "Vaswani et al.",
    "year": 2017,
    "venue": "NeurIPS",
    "type": "conference paper",
    "category": "ACADEMIC",
    "doi": "10.48550/arXiv.1706.03762"
  },
  "scores": {
    "credibility": {
      "score": 5,
      "explanation": "Academic baseline 4, +1 peer-reviewed NeurIPS, +1 PhD researchers, +1 95k citations, +1 DOI = 8 capped at 5. Seminal paper."
    },
    "bias": {
      "score": 5,
      "explanation": "Baseline 3, +1 peer-reviewed, +1 transparent methodology, +1 no conflicts = 6 capped at 5. Objective."
    },
    "priority": {
      "score": 5,
      "explanation": "Baseline 3, +1 seminal work, +1 directly relevant, +1 95k citations, +1 primary source = 7 capped at 5. Essential."
    }
  },
  "recommendation": {
    "action": "READ_FIRST",
    "reason": "Ideal source: highest credibility, zero bias, maximum priority. Foundational for transformer/NLP research.",
    "conflicts": null
  },
  "metadata": {
    "analyzed_by": "source-credibility-analyzer",
    "timestamp": "2025-01-06T10:00:00Z",
    "version": "2.0"
  }
}
```

---

## Example 2: ✅ Think Tank Report (High Bias)

### Input Metadata
```json
{
  "title": "Climate Change Economic Impacts",
  "author": "Heartland Institute",
  "year": 2021,
  "venue": "Heartland Institute Publications",
  "type": "report",
  "citations": 15,
  "institution": "Heartland Institute"
}
```

### Step-by-Step Calculation

**Step 0.5: Classify Source Type**
```
Is peer-reviewed? → NO
Is recognized institution? → YES (but advocacy think tank)
Category: INSTITUTIONAL
Credibility Baseline: 3
```

**Step 1: Calculate Credibility**
```
Baseline: 3 (INSTITUTIONAL)
-1 (No author credentials listed - organization-authored)
-1 (Low citations: 15)
-1 (Known conflicts: Heartland Institute funded by fossil fuel industry)
= 0 → capped at 1

Final Credibility: 1/5
Explanation: "Institutional baseline 3, -1 no author credentials, -1 low citations, -1 fossil fuel funding conflicts = 0 capped at 1. Questionable credibility."
```

**Step 2: Calculate Bias**
```
Baseline: 3
-1 (Advocacy organization - known climate denial group)
-1 (Funded by interested party - fossil fuel industry)
-1 (One-sided presentation - dismisses scientific consensus)
= 0 → capped at 1

Final Bias: 1/5
Explanation: "Baseline 3, -1 advocacy org, -1 industry funding, -1 one-sided = 0 capped at 1. Extremely biased."
```

**Step 3: Calculate Priority**
```
Baseline: 3
+1 (Recent: 2021)
-1 (Low credibility: 1 from Step 1)
-1 (High bias: 1 from Step 2)
= 2

Final Priority: 2/5
Explanation: "Baseline 3, +1 recent, -1 low credibility, -1 high bias = 2. Avoid unless comparing perspectives."
```

**Step 4: Resolve Conflicts**
```
Credibility: 1, Bias: 1, Priority: 2
Matrix: ≤2 + ANY + ANY → SKIP
Conflict: None (all scores low)

Recommendation: SKIP
Reason: "Not credible (1/5) and extremely biased (1/5). Find independent, peer-reviewed sources on climate economics instead."
```

### Output JSON
```json
{
  "source": {
    "title": "Climate Change Economic Impacts",
    "author": "Heartland Institute",
    "year": 2021,
    "venue": "Heartland Institute Publications",
    "type": "report",
    "category": "INSTITUTIONAL"
  },
  "scores": {
    "credibility": {
      "score": 1,
      "explanation": "Institutional baseline 3, -1 no author credentials, -1 low citations, -1 fossil fuel conflicts = 0 capped at 1. Questionable."
    },
    "bias": {
      "score": 1,
      "explanation": "Baseline 3, -1 advocacy org, -1 industry funding, -1 one-sided = 0 capped at 1. Extremely biased."
    },
    "priority": {
      "score": 2,
      "explanation": "Baseline 3, +1 recent, -1 low credibility, -1 high bias = 2. Avoid."
    }
  },
  "recommendation": {
    "action": "SKIP",
    "reason": "Not credible (1/5) and extremely biased (1/5). Find independent peer-reviewed alternatives.",
    "conflicts": null
  },
  "metadata": {
    "analyzed_by": "source-credibility-analyzer",
    "timestamp": "2025-01-06T10:05:00Z",
    "version": "2.0"
  }
}
```

---

## Example 3: ⚠️ Preprint (Ambiguous Credibility)

### Input Metadata
```json
{
  "title": "GPT-5 Scaling Laws",
  "author": "Anonymous Researchers",
  "year": 2025,
  "venue": "arXiv preprint",
  "type": "preprint",
  "citations": 0,
  "doi": "arXiv:2501.00000",
  "url": "https://arxiv.org/abs/2501.00000"
}
```

### Step-by-Step Calculation

**Step 0.5: Classify Source Type**
```
Is peer-reviewed? → NO
Is preprint? → YES (arXiv)
Category: PREPRINTS
Credibility Baseline: 3
```

**Step 1: Calculate Credibility**
```
Baseline: 3 (PREPRINTS)
-1 (Not yet peer-reviewed)
-1 (No author credentials - anonymous)
+1 (Has arXiv DOI - reputable preprint server)
= 2

Final Credibility: 2/5
Explanation: "Preprints baseline 3, -1 not peer-reviewed, -1 anonymous authors, +1 arXiv DOI = 2. Unverified claims."
```

**Step 2: Calculate Bias**
```
Baseline: 3
+1 (Transparent methodology - code likely released on arXiv)
= 4

Final Bias: 4/5
Explanation: "Baseline 3, +1 transparent methodology = 4. Assume good faith, no conflicts detected."
```

**Step 3: Calculate Priority**
```
Baseline: 3
+1 (Recent: 2025 - cutting edge)
+1 (Directly relevant to AI scaling research)
-1 (Low credibility: 2 from Step 1)
= 4

Final Priority: 4/5
Explanation: "Baseline 3, +1 very recent, +1 directly relevant, -1 low credibility = 4. High priority despite credibility concerns."
```

**Step 4: Resolve Conflicts**
```
Credibility: 2, Bias: 4, Priority: 4
Matrix: ≤2 + ≥3 + ≥4 → VERIFY_CLAIMS (Conflict Type 3: High priority + Low credibility)

Conflict Resolution: "High priority but low credibility. Read as preprint but verify all claims when peer-reviewed version published."

Recommendation: VERIFY_CLAIMS
Reason: "Cutting-edge preprint (2025) on relevant topic, but not yet peer-reviewed and anonymous authors. Read critically, verify claims against future peer-reviewed work."
```

### Output JSON
```json
{
  "source": {
    "title": "GPT-5 Scaling Laws",
    "author": "Anonymous Researchers",
    "year": 2025,
    "venue": "arXiv preprint",
    "type": "preprint",
    "category": "PREPRINTS",
    "doi": "arXiv:2501.00000"
  },
  "scores": {
    "credibility": {
      "score": 2,
      "explanation": "Preprints baseline 3, -1 not peer-reviewed, -1 anonymous, +1 arXiv DOI = 2. Unverified."
    },
    "bias": {
      "score": 4,
      "explanation": "Baseline 3, +1 transparent = 4. Good faith assumed."
    },
    "priority": {
      "score": 4,
      "explanation": "Baseline 3, +1 very recent, +1 relevant, -1 low credibility = 4. High priority despite concerns."
    }
  },
  "recommendation": {
    "action": "VERIFY_CLAIMS",
    "reason": "Cutting-edge (2025) on relevant topic, but not peer-reviewed and anonymous. Read critically, verify later.",
    "conflicts": "High priority + Low credibility → Read but verify all claims against peer-reviewed sources."
  },
  "metadata": {
    "analyzed_by": "source-credibility-analyzer",
    "timestamp": "2025-01-06T10:10:00Z",
    "version": "2.0"
  }
}
```

---

## Example 4: ⚠️ Wikipedia Article (Background Material)

### Input Metadata
```json
{
  "title": "Byzantine Empire",
  "author": "Wikipedia Contributors",
  "year": 2024,
  "venue": "Wikipedia",
  "type": "encyclopedia article",
  "url": "https://en.wikipedia.org/wiki/Byzantine_Empire"
}
```

### Step-by-Step Calculation

**Step 0.5: Classify Source Type**
```
Is peer-reviewed? → NO
Is verifiable/documented? → YES (Wikipedia has citations + NPOV policy)
Category: GENERAL
Credibility Baseline: 3

Special Case: Wikipedia → Apply Wikipedia-specific scoring
```

**Step 1: Calculate Credibility**
```
Baseline: 3 (GENERAL)
+1 (Wikipedia: Verifiable, crowd-sourced fact-checking)
-1 (Not peer-reviewed, anyone can edit)
= 3

Final Credibility: 3/5
Explanation: "General baseline 3, +1 verifiable with citations, -1 not peer-reviewed = 3. Reliable for background, verify for citations."
```

**Step 2: Calculate Bias**
```
Baseline: 3
+1 (Wikipedia NPOV policy - neutral point of view enforced)
+1 (Multiple perspectives typically presented)
= 5

Final Bias: 5/5
Explanation: "Baseline 3, +1 NPOV policy, +1 multiple perspectives = 5. Neutral presentation."
```

**Step 3: Calculate Priority**
```
Baseline: 3
+1 (Recent: 2024 - updated regularly)
-1 (Not citable in academic work - secondary source)
= 3

Final Priority: 3/5
Explanation: "Baseline 3, +1 recent updates, -1 not citable academically = 3. Good for background, not for citations."
```

**Step 4: Resolve Conflicts**
```
Credibility: 3, Bias: 5, Priority: 3
Matrix: ≥3 + ≥3 + ≥3 → READ_LATER

No conflicts

Recommendation: READ_LATER
Reason: "Reliable background source (neutral, verifiable) but not citable in academic work. Use as gateway to find primary sources cited in article."
```

### Output JSON
```json
{
  "source": {
    "title": "Byzantine Empire",
    "author": "Wikipedia Contributors",
    "year": 2024,
    "venue": "Wikipedia",
    "type": "encyclopedia article",
    "category": "GENERAL",
    "url": "https://en.wikipedia.org/wiki/Byzantine_Empire"
  },
  "scores": {
    "credibility": {
      "score": 3,
      "explanation": "General baseline 3, +1 verifiable, -1 not peer-reviewed = 3. Reliable for background."
    },
    "bias": {
      "score": 5,
      "explanation": "Baseline 3, +1 NPOV policy, +1 multiple perspectives = 5. Neutral."
    },
    "priority": {
      "score": 3,
      "explanation": "Baseline 3, +1 recent, -1 not citable = 3. Background only."
    }
  },
  "recommendation": {
    "action": "READ_LATER",
    "reason": "Reliable background (neutral, verifiable) but not citable. Use as gateway to primary sources in citations.",
    "conflicts": null
  },
  "metadata": {
    "analyzed_by": "source-credibility-analyzer",
    "timestamp": "2025-01-06T10:15:00Z",
    "version": "2.0"
  }
}
```

---

## Example 5: ❌ Blog Post (Low Quality)

### Input Metadata
```json
{
  "title": "AI Will Destroy Everything Soon",
  "author": "Anonymous",
  "year": 2024,
  "venue": "Personal Blog",
  "type": "blog post",
  "url": "https://randomblog.com/ai-doom"
}
```

### Step-by-Step Calculation

**Step 0.5: Classify Source Type**
```
Is peer-reviewed? → NO
Is verifiable? → NO (personal blog, no citations)
Category: UNVERIFIED
Credibility Baseline: 2
```

**Step 1: Calculate Credibility**
```
Baseline: 2 (UNVERIFIED)
-1 (No author credentials - anonymous)
-1 (No citations or references)
-1 (Published on unmoderated personal blog)
= -1 → capped at 1

Final Credibility: 1/5
Explanation: "Unverified baseline 2, -1 anonymous, -1 no citations, -1 personal blog = -1 capped at 1. Not credible."
```

**Step 2: Calculate Bias**
```
Baseline: 3
-1 (Sensationalist title - "Destroy Everything Soon")
-1 (One-sided presentation - no counterarguments)
= 1

Final Bias: 1/5
Explanation: "Baseline 3, -1 sensationalist clickbait, -1 one-sided = 1. Highly biased opinion."
```

**Step 3: Calculate Priority**
```
Baseline: 3
+1 (Recent: 2024)
-1 (Low credibility: 1 from Step 1)
-1 (High bias: 1 from Step 2)
-1 (Tangentially relevant - vague fearmongering, not specific research)
= 1

Final Priority: 1/5
Explanation: "Baseline 3, +1 recent, -1 low credibility, -1 high bias, -1 tangential = 1. Skip."
```

**Step 4: Resolve Conflicts**
```
Credibility: 1, Bias: 1, Priority: 1
Matrix: ≤2 + ANY + ANY → SKIP

No conflicts (all scores consistently low)

Recommendation: SKIP
Reason: "Not credible (1/5), extremely biased (1/5), and low priority (1/5). Anonymous blog post with sensationalist claims and no citations. Find peer-reviewed sources on AI safety instead."
```

### Output JSON
```json
{
  "source": {
    "title": "AI Will Destroy Everything Soon",
    "author": "Anonymous",
    "year": 2024,
    "venue": "Personal Blog",
    "type": "blog post",
    "category": "UNVERIFIED",
    "url": "https://randomblog.com/ai-doom"
  },
  "scores": {
    "credibility": {
      "score": 1,
      "explanation": "Unverified baseline 2, -1 anonymous, -1 no citations, -1 personal blog = -1 capped at 1. Not credible."
    },
    "bias": {
      "score": 1,
      "explanation": "Baseline 3, -1 sensationalist, -1 one-sided = 1. Highly biased."
    },
    "priority": {
      "score": 1,
      "explanation": "Baseline 3, +1 recent, -1 low credibility, -1 high bias, -1 tangential = 1. Skip."
    }
  },
  "recommendation": {
    "action": "SKIP",
    "reason": "Not credible, extremely biased, low priority. Anonymous sensationalist blog. Find peer-reviewed AI safety sources.",
    "conflicts": null
  },
  "metadata": {
    "analyzed_by": "source-credibility-analyzer",
    "timestamp": "2025-01-06T10:20:00Z",
    "version": "2.0"
  }
}
```

---

## Summary Table

| Example | Category | Credibility | Bias | Priority | Recommendation | Key Lesson |
|---------|----------|-------------|------|----------|----------------|------------|
| 1. Vaswani NeurIPS | ACADEMIC | 5 | 5 | 5 | READ_FIRST | Ideal source: peer-reviewed, highly cited, foundational |
| 2. Heartland Institute | INSTITUTIONAL | 1 | 1 | 2 | SKIP | Low credibility + high bias = avoid |
| 3. arXiv Preprint | PREPRINTS | 2 | 4 | 4 | VERIFY_CLAIMS | High priority but unverified → read critically |
| 4. Wikipedia | GENERAL | 3 | 5 | 3 | READ_LATER | Reliable background, not citable → gateway to primary sources |
| 5. Random Blog | UNVERIFIED | 1 | 1 | 1 | SKIP | No credentials + sensationalist = waste of time |

---

## Key Takeaways

**✅ Trust the Rubrics**:
- Program-of-thought calculations are transparent and auditable
- Explanations show exactly which rules applied

**⚠️ Watch for Conflicts**:
- High credibility + high bias → VERIFY_CLAIMS (e.g., pharma-funded study in peer-reviewed journal)
- High priority + low credibility → VERIFY_CLAIMS (e.g., preprints on cutting-edge topics)

**💡 Category Matters**:
- ACADEMIC starts at Credibility 4 → easier to reach 5
- UNVERIFIED starts at Credibility 2 → hard to score high
- Special cases (Wikipedia, preprints) have domain-specific scoring

**🚨 Borderline Rounding**:
- Credibility: Round DOWN (conservative)
- Bias: Round UP (benefit of doubt)
- Priority: Round UP (favor reading when uncertain)

---

**Remember**: These examples show the tool working as designed. Adjust rubrics to your domain if needed (e.g., CS vs History citation thresholds).


---
*Promise: `<promise>SCORING_EXAMPLES_VERIX_COMPLIANT</promise>`*
