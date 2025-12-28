---
name: general-research-workflow
description: Systematic 6-phase research methodology for history, mythology, and literature implementing Red's (OSP) evidence-based approach. Use when researching topics outside academic ML scope that require primary/secondary source evaluation, credibility analysis, and evidence-based thesis formation. Sequential agent workflow (researcher, analyst, coordinator) over 6-10 hours with Quality Gates ensuring rigorous source validation and synthesis.
---

# General Research Workflow

## Purpose

Execute systematic general-purpose research across history, mythology, literature, and non-ML domains using Red's (OSP) 6-phase evidence-based methodology with rigorous source evaluation and synthesis.

## When to Use This Skill

**Use this skill when:**
- ✅ Researching historical events, mythological topics, or literary analysis
- ✅ Need to evaluate primary vs secondary sources
- ✅ Building evidence-based arguments with citations
- ✅ Topic requires source credibility analysis
- ✅ Have 6+ hours for thorough research

**Do NOT use for:**
- ❌ Academic ML research (use `literature-synthesis` instead)
- ❌ Quick fact-checking (<30 min)
- ❌ Literature reviews for academic papers (use `deep-research-orchestrator`)

**Decision Tree**: See `references/decision-tree.md`

## Quick Reference

| Step | Agent | Deliverable | Duration | Quality Gate |
|------|-------|-------------|----------|--------------|
| 0 | researcher | Wikipedia verification OR fallback plan | 5-10 min | ≥1 viable starting source |
| 1 | researcher | 10+ citations from Wikipedia references | 15-30 min | ≥10 citations, ≥3 categories |
| 2 | researcher | 20+ sources with metadata + relevance scores | 1-2 hours | ≥20 sources, ≥50% accessible |
| 3 | analyst | Classified sources with credibility/bias/priority scores | 30-60 min | ≥5 primaries, ≥80% credibility ≥3 |
| 4 | researcher | Context profiles for 10+ sources, 3+ time periods | 1-2 hours | ≥10 contextualized, ≥3 periods |
| 5 | researcher | 50+ notes, 20+ quotes with pages, 5+ cross-links | 2-3 hours | All quotas met |
| 6 | coordinator | Evidence-based thesis + final report | 1-2 hours | ≥5 sources support thesis, validated |

## Agent Coordination Protocol

### Sequential Execution
Each step passes deliverables to the next step. Do NOT proceed if Quality Gate fails.

### Agent Roles
- **researcher**: Discovery, analysis, note-taking (Steps 0, 1, 2, 4, 5, Phase A-B of Step 6)
- **analyst**: Validation, classification, quality checks (Step 3, Phase C of Step 6)
- **coordinator**: Synthesis orchestration (Phase D of Step 6)

### Memory MCP Tags
ALL stored data must include: `WHO=[agent]`, `WHEN=[timestamp]`, `PROJECT=[research-topic]`, `WHY=[intent]`

## Glossary

See `references/glossary.md` for complete definitions:
- **Primary Source**: Original documents/eyewitness accounts from the time period
- **Secondary Source**: Analysis/interpretation created after the events
- **Credibility Score (1-5)**: Reliability based on expertise, venue, citations
- **Bias Risk Score (1-5)**: Likelihood of systematic distortion
- **WorldCat**: worldcat.org - Global library catalog
- **Google Scholar**: scholar.google.com - Academic publication search



### STEP 1: Wikipedia Mining
**Agent**: researcher
**Goal**: Extract reference trail from Wikipedia

**Procedure**:
1. Read Wikipedia article for overview
2. Navigate to "References" section
3. Extract ALL citations with metadata:
   - ✅ Author(s) [REQUIRED]
   - ✅ Title [REQUIRED]
   - ✅ Year [REQUIRED]
   - ⚠️ ISBN/DOI [OPTIONAL]
4. Extract "Further Reading" citations
5. Categorize by type: Books, Papers, News, Websites
6. Store with Memory MCP tags

**Example**: See `examples/wikipedia-citation-example.json`

**Deliverable**: JSON array of 10+ citations

**Quality Gate 1**: STOP if <10 citations. Expand to related Wikipedia articles.



### STEP 3: Source Classification
**Agent**: analyst (with researcher support)
**Goal**: Classify sources using systematic rubrics

**Procedure**:

**A. Primary vs Secondary**:
- **Primary**: Original documents, eyewitness accounts, contemporary records, original data
- **Secondary**: Analysis of primaries, textbooks, biographies (written after)

**B. Credibility Score (1-5) - Program-of-Thought**:
```
Start: 3 (neutral)

ADD +1 for EACH:
✅ Peer-reviewed (academic journal, university press)
✅ Author has PhD/recognized expertise
✅ Cites primary sources, provides references
✅ Reputable institution

SUBTRACT -1 for EACH:
❌ Self-published or vanity press
❌ No author credentials
❌ No citations/references
❌ Known conflicts of interest

Final: 1-5 (capped)
```

**C. Bias Risk Score (1-5)**:
```
Start: 2 (low bias)

ADD +1 for EACH:
⚠️ Advocacy organization affiliation
⚠️ Funding from interested party
⚠️ Strong ideological language
⚠️ Cherry-picked/one-sided presentation

Final: 1-5
(1=minimal, 3=moderate, 5=high bias)
```

**D. Reading Priority (1-5)**:
```
Formula:
Priority = (Relevance × 0.4) + (Credibility × 0.3) +
           (Primary=+2, Secondary=0) + (Accessible=+1, Not=-1)

Bands:
5 = Read IMMEDIATELY
4 = Read soon
3 = Read if time
2 = Defer to end
1 = Skip unless critical
```

**Flag sources**:
- 💡 Priority 4-5: Immediate queue
- ⏸️ Priority 1-3: Defer
- ⚠️ Conflicting: Cross-check
- 🚨 Bias ≥4: Extra scrutiny

**Example**: See `examples/source-classification-example.md`

**Deliverable**: Classified inventory with scores

**Quality Gate 3**: STOP if <5 primaries OR <80% credibility ≥3.

**Exception**: If NO primaries available (ancient topics), proceed with ≥10 credibility ≥4 secondaries, document.



### STEP 5: Comprehensive Note-Taking
**Agent**: researcher
**Goal**: Extract claims, evidence, quotes with page numbers

**Procedure**:
Read sources in priority order. For EACH source use template:

```markdown
## SOURCE: [Title] - [Author] ([Year])
TYPE: [Primary/Secondary] | CREDIBILITY: [Score] | BIAS: [Score]

### ✅ KEY CLAIMS [REQUIRED - Min 2]
- Claim 1 (page X): "[quote or paraphrase]"
- Claim 2 (page Y): "[quote or paraphrase]"

### ✅ SUPPORTING EVIDENCE [REQUIRED]
- For Claim 1 (pages X-Y): [How supported? Data/sources/reasoning?]
- For Claim 2 (pages Y-Z): [How supported?]

### ✅ QUOTABLE PASSAGES [REQUIRED - Min 2 with pages]
- "Notable quote 1" (page X)
- "Notable quote 2" (page Y)

### ⚠️ CONTRADICTIONS [OPTIONAL - If detected]
- Conflicts with [Source B] on [point] (page X vs page Y)

### ⚠️ BIAS/AGENDA [OPTIONAL - If bias score ≥3]
- Observable patterns: [Examples]

### ⚠️ CROSS-REFERENCES [OPTIONAL - If relevant]
- Links to [Source C] on [topic]
- Supports/refutes [Source D]
```

Tag with: `#primary-source` or `#secondary-source`, `#key-claim`, `#needs-verification`, `#high-confidence`/`#uncertain`, `#[topic-keywords]`

**Template**: See `examples/note-template.md`

**Deliverable**: 50+ notes, 20+ quotes with pages, 5+ cross-links

**Quality Gate 5**: STOP if quotas not met. Re-read sources.



## Red's Research Principles

This workflow embeds Red's (OSP) methodology:

| Principle | Implementation |
|-----------|---------------|
| **"Trust No One"** | Step 3: Systematic credibility + bias scoring |
| **"Context is Everything"** | Step 4: Temporal/cultural/historiographical analysis |
| **"Thesis from Evidence"** | Step 6: Thesis EMERGES, not imposed. "INCONCLUSIVE" option |
| **"Wikipedia is a Gateway"** | Step 1: Mine references, not final authority. Gate 0 fallback |
| **"Primary Sources Matter"** | Step 3: ≥2 primaries required (or exception) |
| **"Page Numbers Save Lives"** | Step 5: All quotes/claims MUST have page refs |

See `references/red-methodology.md` for full explanation.



## Error Handling

| Failure | Gate | Resolution |
|---------|------|------------|
| No Wikipedia article | 0 | Google Scholar fallback |
| <10 citations | 1 | Related articles, alt terms |
| <20 sources | 2 | Different discovery methods |
| <50% accessible | 2 | Prioritize accessible, document |
| <5 primaries | 3 | Continue OR document exception |
| <80% credibility ≥3 | 3 | Return to Step 2 |
| Non-English sources | 0, 2 | Flag for translation OR document |
| Contradictory evidence | 6B | "INCONCLUSIVE" option |
| Logical fallacies | 6C | Return to Phase B |
| Unsupported claims | 6C | Add sources OR remove claims |



## Process Visualization

See `general-research-process.dot` for complete workflow diagram showing all steps, gates, and decision points.

---

**Red's Research Principles**: "Trust No One, Context is Everything, Thesis from Evidence, Wikipedia is a Gateway, Primary Sources Matter, Page Numbers Save Lives"