---
name: academic-reading-workflow
description: Systematic reading methodology for academic papers and complex texts implementing Blue's (OSP) 3-phase approach. Use when reading papers/books that require deep understanding, searchable annotation system with keyword tagging ("command-F in real life"), and evidence-based writing with citations. Sequential workflow (researcher, analyst) over 2-6 hours with annotation quality validation.
---

# Academic Reading Workflow

## Purpose

Execute systematic reading of academic papers, books, and complex texts using Blue's (OSP) 3-phase methodology: summary-first reading, active annotation with searchable keyword system, and evidence-based writing.

## When to Use This Skill

**Use this skill when:**
- ✅ Reading academic papers or dense books requiring deep understanding
- ✅ Building searchable knowledge base from readings
- ✅ Need to retain and find information later ("command-F in real life")
- ✅ Preparing to write evidence-based essays/analyses with citations

**Do NOT use for:**
- ❌ Quick skimming (<30 min)
- ❌ Casual reading without note-taking
- ❌ Fiction/entertainment reading
- ❌ Already familiar material (just creating citations)

**Decision Tree**: See `references/decision-tree.md`

## Quick Reference

| Step | Agent | Deliverable | Duration | Quality Gate |
|------|-------|-------------|----------|--------------|
| 0 | researcher | Master keyword list (if multi-source project) | 5-10 min | Keyword vocabulary defined |
| 1 | researcher | Reading roadmap with critical sections identified | 15-30 min | Clear thesis + sections |
| 2 | researcher | 20-50 searchable annotations with keyword tags | 1-4 hours | ≥20 notes, ≥5 keywords |
| 3 | analyst | Validated annotation set + keyword index | 15-30 min | Searchable, <30% quote-paraphrases |

**Optional**: Use `evidence-based-writing` skill separately when ready to write (not part of this workflow)


source: "[Title] - [Author] ([Year])"
page: [number]
keywords: [keyword1, keyword2, keyword3]
date_annotated: [YYYY-MM-DD]
project: [research-topic-slug]
annotation_id: [unique-id]


## Blue's Core Principles

This workflow embeds Blue's (OSP) methodology:

| Principle | Implementation |
|-----------|---------------|
| **"Read the Roadmap Before You Get Lost"** | Step 1: Summary-first, create plan BEFORE deep reading |
| **"Annotation is Command-F in Real Life"** | Step 2: Keyword tagging for searchable notes |
| **"Paraphrase > Highlighting"** | Step 2: Force genuine paraphrase, not quote-rewording |
| **"Write Like You Speak"** | (Evidence-based-writing skill): Natural draft, polish later |
| **"Thesis Comes LAST"** | (Evidence-based-writing skill): Let thesis emerge from notes |
| **"Every Claim Needs Source"** | (Evidence-based-writing skill): All assertions cited with pages |

See `references/blue-methodology.md` for full explanation.



### STEP 1: Summary-First Reading (Roadmap Phase)
**Agent**: researcher
**Objective**: Create reading roadmap BEFORE deep dive to avoid getting lost

**Procedure**:

**A. Read Summary Materials FIRST** (priority order):
1. Abstract (for papers)
2. Introduction + Conclusion chapters (for books)
3. Table of Contents
4. Section headers
5. Wikipedia article on topic (if exists)
6. Existing reviews/summaries

**B. Create Reading Roadmap**:
```markdown
# READING ROADMAP: [Source Title]

## Main Argument/Thesis
[1-2 sentences - or "No clear thesis, exploratory paper" if applicable]

## Key Questions (if no thesis)
- Question 1
- Question 2

## Critical Sections (Read Carefully + Annotate Heavily)
1. [Chapter/Section] (pages X-Y) - **Why critical**: [Reason]
2. [Chapter/Section] (pages A-B) - **Why critical**: [Reason]

## Supplementary Sections (Skim for Key Points)
1. [Chapter/Section] (pages M-N) - **Extract**: [What to get]

## Skip Sections
1. [Chapter/Section] - **Why skipping**: [Reason]

## Reading Focus Question
[What am I trying to learn from this source?]

## Estimated Reading Time
- Critical sections: [X] hours
- Supplementary: [Y] hours
- **Total**: [Z] hours
```

**C. Handle Edge Cases**:
- **No clear thesis**: List "key questions" paper explores instead
- **Too technical/unfamiliar**: Add "Define unfamiliar terms" sub-step
  - Create glossary section for domain-specific terms
  - Define before attempting to paraphrase

**Deliverable**: Reading roadmap with sections categorized

**Quality Gate 1**:
- **GO**: Main argument OR key questions identified, critical sections listed with page ranges
- **NO-GO**: Vague roadmap → Re-read intro/conclusion for clarity


source: "[Title] - [Author] ([Year])"
page: [X]
keywords: [keyword1, keyword2, keyword3]
date_annotated: [YYYY-MM-DD]
project: [project-slug]
annotation_id: [source-slug]-p[page]


### STEP 3: Annotation Quality Check
**Agent**: analyst
**Objective**: Validate annotations are searchable, useful, and complete

**Procedure**:

**A. Completeness Check**

For each annotation, verify:
- ✅ Has ≥2 keyword tags?
- ✅ Has page number?
- ✅ Has genuine paraphrase (own words)?
- ⚠️ If quote claimed, has exact text in "quotes"?
- ⚠️ If cross-reference claimed, has specific page/source link?

**Flag incomplete** → return to Step 2

**B. Keyword Consistency Check**

1. Extract all keywords used
2. Check for duplicates/synonyms:
   - `#method` vs `#methodology` → **Standardize to one**
   - `#keypoint` → **Too vague, make specific**
3. If multi-source project:
   - Compare to master keyword list (Step 0)
   - Flag deviations → update to match master list
4. Create keyword index:

```markdown
# KEYWORD INDEX: [Source Title]

## Keywords Used (Alphabetical)
- #argument (pages 15, 42, 88) - [3 uses]
- #bias (pages 23, 67) - [2 uses]
- #evidence (pages 15, 28, 35, 49, 72) - [5 uses]
- #key-claim (pages 12, 34, 56) - [3 uses]
- #limitation (pages 89, 91) - [2 uses]
- #methodology (pages 8, 10, 45) - [3 uses]

**Total keywords**: 6
**Total annotations**: 32
**Average annotations per keyword**: 5.3
```

**C. Paraphrase Quality Check**

Sample 5-10 annotations randomly. For each:
- Is it in reader's OWN words (not just slightly reworded)?
- Does it capture essence without source?
- Understandable 6 months later?

**If >30% are quote-paraphrases** → return to Step 2, force genuine paraphrasing

**D. Searchability Test**

1. Pick 3 concepts from the source
2. Search annotations using keywords
3. Can you find ALL relevant passages quickly?
4. Are notes useful on their own?

**Example**:
- Search `#methodology` → Should find all passages about research methods
- Search `#byzantine-trade` → Should find all passages about Byzantine commerce

**Quality Gate 3**:
- **GO**: ≥20 annotations, ≥5 keywords, <30% quote-paraphrases, searchability works
- **NO-GO**: Return to Step 2 for improved annotation depth or keyword consistency

**Deliverable**:
- Validated annotation set
- Keyword index
- Quality assessment report



## Error Handling

| Failure Mode | Gate | Resolution |
|--------------|------|------------|
| **Vague roadmap** | 1 | Re-read abstract/intro, clarify argument OR list key questions |
| **Getting lost while reading** | 1 | Return to roadmap, refocus on critical sections |
| **<20 annotations** | 2 | Extend reading, annotate more thoroughly |
| **<5 keywords** | 2 | Review notes, add specific keywords |
| **>30% quote-paraphrases** | 3 | Force genuine paraphrasing, re-read if needed |
| **Keyword inconsistency** | 3 | Standardize terms, update master list |
| **Can't find via keywords** | 3 | Add more keywords, improve tagging |
| **Unfamiliar domain** | 2 | Define terms inline before paraphrasing |
| **No clear thesis** | 1 | Identify "key questions" instead |
| **Annotation overflow (100+)** | 2 | Create summary notes every 50 pages |
| **Keyword drift (multi-source)** | 3 | Update master keyword list, standardize |



## Process Visualization

See `academic-reading-process.dot` for complete workflow diagram showing all steps, gates, and decision points.


source: "Byzantium and Renaissance - Wilson 1992"
page: 45
keywords: [greek-migration, manuscripts, bessarion]
date_annotated: 2025-01-06
project: byzantine-renaissance-italy
annotation_id: wilson1992-p45
type: annotation


**Blue's Annotation Principles**: "Read the Roadmap, Command-F in Real Life, Paraphrase > Highlighting, Write for Future You"