# Academic Reading Workflow Skill

**Version**: 2.0 (Production-Ready)
**Created**: 2025-01-06
**Methodology**: Skill-Forge 7-Phase Process + Prompt-Architect Optimization

---

## What This Skill Does

Executes systematic reading of academic papers and complex texts using **Blue's (OSP) 3-phase methodology**: summary-first reading, searchable keyword annotation system ("command-F in real life"), and evidence-based writing principles.

**Duration**: 2-6 hours per source
**Agents**: researcher, analyst
**Quality Gates**: 3 (Gate 0-2)

---

## Skill Structure

```
academic-reading-workflow/
├── SKILL.md                          # Main skill file (core SOP)
├── README.md                         # This file
├── academic-reading-process.dot      # GraphViz process visualization
├── references/
│   └── blue-methodology.md           # Blue's 6 principles explained
└── examples/
    └── annotation-example.md         # Full annotation with good vs bad comparisons
```

---

## When to Use This Skill

**✅ USE FOR**:
- Reading academic papers requiring deep understanding
- Dense books needing systematic note-taking
- Building searchable knowledge base from readings
- Preparing to write evidence-based essays with citations

**❌ DO NOT USE FOR**:
- Quick skimming (<30 min)
- Casual reading without note-taking
- Fiction/entertainment
- Already familiar material (just need citations)

---

## Key Features

### 1. Sequential Agent Workflow
- **researcher**: Roadmap creation, reading, annotation (Steps 0, 1, 2)
- **analyst**: Validation, keyword standardization, quality checks (Step 3)

### 2. Searchable Annotation System ("Command-F in Real Life")

**Core Innovation**: Keyword tagging system allows searching notes like Ctrl+F

**Example**:
```
Later when writing at 2am:
"Where did I read about Byzantine trade methodology?"
→ Search annotations: #byzantine-trade AND #methodology
→ Found: Page 42 annotation
→ Go directly to relevant passage
```

**Storage Format**: Markdown with YAML frontmatter
```yaml
---
source: "Title - Author Year"
page: 45
keywords: [keyword1, keyword2, keyword3]
project: research-topic-slug
---

**Summary**: [Genuine paraphrase in own words]
**Quote**: "[Exact text]" (p. 45)
**Why This Matters**: [Connection to research]
```

### 3. Three Quality Gates

| Gate | After Step | Requirement | Example |
|------|-----------|-------------|---------|
| 0 | Master Keywords | Keyword vocabulary defined | 10-20 standard terms for project |
| 1 | Roadmap | Clear thesis OR key questions | Main argument identified |
| 2 | Annotation | ≥20 notes, ≥5 keywords | 32 notes with 6 keywords |
| 3 | Validation | Searchable, <30% quote-paraphrases | Can find passages via keywords |

### 4. Blue's 6 Principles Embedded

| Principle | Implementation |
|-----------|---------------|
| **Read the Roadmap First** | Step 1: Summary-first (abstract, intro, conclusion) BEFORE deep reading |
| **Command-F in Real Life** | Step 2: Keyword tagging for searchability |
| **Paraphrase > Highlighting** | Step 2: Force genuine paraphrase, Step 3: <30% quote-paraphrases |
| **Write Like You Speak** | (evidence-based-writing skill): Natural draft, polish later |
| **Thesis Comes LAST** | (evidence-based-writing skill): Thesis emerges from evidence |
| **Every Claim = Source** | (evidence-based-writing skill): All assertions cited with pages |

### 5. Anti-Pattern Detection

**Step 3 catches common mistakes**:
- ❌ "Important!" (too vague) → Require specific explanation
- ❌ Copy-paste with slight rewording → Force genuine paraphrase
- ❌ Keywords like "#page15" → Must be conceptually searchable
- ❌ Highlighting without notes → Require paraphrase section
- ❌ Inconsistent keywords → Standardize to master list

**Examples**: See `examples/annotation-example.md` for good vs bad comparisons

### 6. Multi-Source Coordination

**Step 0** (optional): Initialize master keyword list across all sources
- Use SAME keywords for SAME concepts across all readings
- Example: #methodology in 5 different papers → can search ALL papers at once
- Prevents keyword drift (#method vs #methodology vs #methods)

---

## How It Was Built

### Design Process (Skill-Forge 7 Phases)

1. **Intent Archaeology** ✅
   - Analyzed Blue's (OSP) methodology from YouTube transcript
   - Mapped 3-phase approach to agent workflows
   - Defined searchable annotation system requirements

2. **Use Case Crystallization** ✅
   - Example: Reading "Byzantium and Renaissance" (300-page academic book)
   - Pattern: Roadmap (30 min) → Annotate critical sections (3 hours) → Validate (20 min)

3. **Structural Architecture** ✅
   - SKILL.md: Core SOP workflow (Steps 0-3)
   - Bundled resources: Process diagram, methodology, annotation examples
   - Markdown + YAML frontmatter storage format

4. **Metadata Engineering** ✅
   - Name: `academic-reading-workflow`
   - Description optimized for discovery (academic papers, searchable annotations, keyword tagging)
   - Trigger conditions explicit (2-6 hours, deep understanding needed)

5. **Instruction Crafting** ✅
   - Imperative voice throughout
   - ✅ Required vs ⚠️ Optional visual markers
   - Quality Gates with GO/NO-GO criteria
   - Anti-pattern examples (good vs bad annotations)

6. **Resource Development** ✅
   - **Process diagram**: `academic-reading-process.dot` (GraphViz)
   - **Methodology**: Blue's 6 principles with examples and tests
   - **Example**: Full annotation with 4 bad examples for comparison

7. **Validation** ✅
   - Prompt-architect analysis identified improvements needed
   - v2 implemented Priority 1 changes:
     - Few-shot example with good vs bad annotations
     - Explicit storage format (Markdown + YAML)
     - 4 missing failure modes (unfamiliar domain, no thesis, annotation overflow, keyword drift)
     - Visual markers (✅⚠️)
     - Master keyword list for multi-source projects

---

## Optimization History

### Version 1 → Version 2 (Prompt-Architect Optimized)

**Added** (Priority 1 Critical):
- **Step 0**: Master keyword list for multi-source projects
- **Annotation example**: Full page with 4 bad examples (copy-paste, vague, missing pages, just highlighting)
- **Storage format**: Markdown + YAML frontmatter specification
- **Failure modes**: Unfamiliar domain (define terms), no thesis (key questions), annotation overflow (summary notes), keyword drift (master list)
- **Visual markers**: ✅ Required, ⚠️ Optional (consistent with general-research-workflow)
- **Anti-pattern detection**: Quote-paraphrase checker, keyword consistency validator

**Improved**:
- Clarified Step 4 scope (moved to separate `evidence-based-writing` skill)
- Added searchability test in Step 3
- Specified Memory MCP tagging format
- Added "Why This Matters" with 3 lenses (Research Question, Argument Structure, Cross-Reference)

---

## Success Metrics

### Quantitative
- ✅ Reading roadmap created (Step 1)
- ✅ ≥20 annotations for full paper/chapter
- ✅ ≥5 consistent keywords used
- ✅ ≥2 keywords per annotation
- ✅ Page numbers for ALL quotes
- ✅ <30% quote-paraphrases
- ✅ Keyword index searchable

### Qualitative
- ✅ Can find passages using keyword search
- ✅ Paraphrases understandable without source
- ✅ Annotations useful 6 months later (Blue's "Six-Month Test")
- ✅ Links between passages documented
- ✅ If multi-source: keywords consistent across all

---

## Integration with Other Skills

**Before This Skill**:
- `general-research-workflow` Steps 2-3 - Find and classify sources first
- Prioritize which sources to read deeply using credibility/priority scores

**During This Skill**:
- Can annotate multiple sources in parallel
- Use SAME keyword vocabulary across all sources (Step 0)
- Annotations feed into `general-research-workflow` Step 5 (note-taking)

**After This Skill**:
- `evidence-based-writing` - Turn annotations into essay/analysis (separate skill)
- Export keyword index to build personal knowledge base
- Search annotations across ALL sources using shared keywords

---

## Example Workflow Execution

```
Source: "Byzantium and the Renaissance" by N.G. Wilson (300 pages)

Step 0 (10 min, multi-source project):
- Created master keyword list for "Byzantine influence on Renaissance" project
- 15 keywords: #greek-migration, #manuscripts, #pedagogy, #venice, #florence, etc.

Step 1 (30 min):
- Read: Abstract, Intro (pp. 1-10), Conclusion (pp. 290-300), Table of Contents
- Roadmap: Thesis = "Greek scholars transformed Italian humanism via teaching + manuscripts"
- Critical sections: Chapters 2-4 (Greek migration, pp. 45-150)
- Supplementary: Chapters 5-6 (Cultural impact, pp. 151-240)
- Skip: Appendices (pp. 250-289)
- Reading focus: "How did Greek scholarship specifically influence methods, not just content?"

Step 2 (3.5 hours):
- Read Chapters 2-4 carefully (105 pages)
- Created 45 annotations using YAML template
- Keywords used: #greek-migration (12x), #manuscripts (8x), #bessarion (6x), #pedagogy (9x), #venice (7x), #plethon (3x)
- Extracted 9 direct quotes with page numbers
- Linked related passages (e.g., p.45 → p.67 on Bessarion's methods)
- Skimmed Chapters 5-6 (8 annotations)
- Total: 53 annotations

Step 3 (25 min):
- Analyst validation:
  - All notes have ≥2 keywords ✓
  - Page numbers present ✓
  - Paraphrase check: 87% genuine (good, <30% threshold) ✓
- Keyword index: 6 primary keywords, avg 7.5 uses each ✓
- Searchability test:
  - Searched #manuscripts → Found all 8 passages ✓
  - Searched #pedagogy AND #venice → Found 4 passages about Venetian teaching methods ✓
- Result: PASS all gates

Output: 53 searchable annotations, 6-keyword index, ready for writing or cross-source search
```

---

## Files Created

1. **C:\Users\17175\skills\academic-reading-workflow\SKILL.md**
   - Main skill file (5,500 words)
   - Complete SOP with 4 steps, 3 Quality Gates
   - Annotation template with visual markers
   - Blue's principles embedded

2. **C:\Users\17175\skills\academic-reading-workflow\academic-reading-process.dot**
   - GraphViz workflow visualization
   - Shows roadmap → annotation → validation flow
   - Decision points for multi-source, unfamiliar domain, long books

3. **C:\Users\17175\skills\academic-reading-workflow\references\blue-methodology.md**
   - Blue's 6 principles explained (6,500 words)
   - 7 common mistakes and solutions
   - 5 self-check tests
   - Complete workflow integration

4. **C:\Users\17175\skills\academic-reading-workflow\examples\annotation-example.md**
   - Full annotation of 1 academic paper page (2,800 words)
   - ✅ 1 correct annotation example
   - ❌ 4 bad annotation examples (copy-paste, vague, missing pages, just highlighting)
   - Side-by-side comparison table
   - Blue's tests for good annotations

---

## Companion Skill

**evidence-based-writing** (Separate skill, not yet built):
- Use when: Ready to write essay/analysis based on annotations
- Input: Validated annotations from Step 3 of this skill
- Output: Draft with citations, relativist language, evidence-based thesis
- Implements Blue's writing principles (Thesis LAST, Every Claim = Source, Write Like You Speak)

**Why Separate**: Writing is optional after reading. Many users annotate now, write later.

---

## Design Comparison

| Aspect | v1 Draft | v2 Optimized |
|--------|----------|--------------|
| Storage Format | "Searchable format" (vague) | Markdown + YAML frontmatter (explicit) |
| Examples | 0 | 1 full example + 4 bad examples |
| Failure Modes | 8 covered | 12 covered (added 4) |
| Multi-Source | Not addressed | Step 0 master keyword list |
| Visual Markers | None | ✅⚠️ systematic |
| Anti-Patterns | Mentioned | Examples + detection |
| Step 4 Clarity | "Optional" (ambiguous) | Separate `evidence-based-writing` skill |

---

## Next Steps

This is **Skill 2 of 9** from the MECE gap analysis. Remaining Priority 1 skill:

3. **source-credibility-analyzer** (Standalone tool)
   - Automates credibility/bias/priority scoring
   - Can be used independently OR within general-research-workflow Step 3
   - Implements program-of-thought rubrics as reusable tool

After Priority 1 complete (3 skills), move to Priority 2 (digital-annotation-system, research-milestone-planner, wikipedia-citation-extractor).

---

## Credits

**Methodology Source**: Blue (Overly Sarcastic Productions) - "How to Read Books and Write Essays" YouTube video
**Design Framework**: Skill-Forge 7-Phase Process
**Optimization**: Prompt-Architect evidence-based analysis
**Implementation**: 2-iteration refinement (Draft → Optimized)

---

**Production Status**: ✅ READY FOR USE
**Last Updated**: 2025-01-06
**Version**: 2.0 (Optimized)
