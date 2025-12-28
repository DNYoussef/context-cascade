# General Research Workflow Skill

**Version**: 3.0 (Production-Ready)
**Created**: 2025-01-06
**Methodology**: Skill-Forge 7-Phase Process + Prompt-Architect Optimization

---

## What This Skill Does

Executes systematic general-purpose research for history, mythology, and literature using **Red's (OSP) 6-phase evidence-based methodology**. Coordinates 3 agents (researcher, analyst, coordinator) through 7 steps with Quality Gates ensuring rigorous source validation.

**Duration**: 6-10 hours
**Agents**: researcher, analyst, coordinator
**Quality Gates**: 7 (Gate 0-6)

---

## Skill Structure

```
general-research-workflow/
├── SKILL.md                          # Main skill file (core SOP)
├── README.md                         # This file
├── general-research-process.dot      # GraphViz process visualization
├── references/
│   ├── glossary.md                   # Comprehensive glossary (sources, scoring, tools)
│   └── red-methodology.md            # Red's 6 principles explained
└── examples/
    └── source-classification-example.md  # Step 3 output example with scoring
```

---

## When to Use This Skill

**✅ USE FOR**:
- Historical events (Byzantine Empire, Renaissance, etc.)
- Mythological topics (Greek mythology, Norse sagas, etc.)
- Literary analysis (Shakespeare, ancient texts, etc.)
- Topics requiring primary/secondary source evaluation
- Building evidence-based arguments with citations

**❌ DO NOT USE FOR**:
- Academic ML research → use `literature-synthesis`
- Quick fact-checking (<30 min) → use web search
- Literature reviews for papers → use `deep-research-orchestrator`

---

## Key Features

### 1. Sequential Agent Workflow
- **researcher**: Discovery, analysis, note-taking (Steps 0, 1, 2, 4, 5)
- **analyst**: Validation, classification, quality checks (Step 3, 6C)
- **coordinator**: Synthesis orchestration (Step 6D)

### 2. 7 Quality Gates
Each step has quantitative thresholds. NO progression until requirements met.

| Gate | After Step | Requirement | Example |
|------|-----------|-------------|---------|
| 0 | Pre-Flight | ≥1 viable source | Wikipedia OR Google Scholar |
| 1 | Wikipedia Mining | ≥10 citations | Must have 10+ refs from Wikipedia |
| 2 | Source Discovery | ≥20 sources, ≥50% accessible | 20+ sources, half full-text |
| 3 | Classification | ≥5 primaries, ≥80% credibility ≥3 | 5 primary sources minimum |
| 4 | Context Analysis | ≥10 contextualized, ≥3 periods | 10 sources, 3 time periods |
| 5 | Note-Taking | ≥50 notes, ≥20 quotes, ≥5 links | 50 notes with page numbers |
| 6 | Synthesis | Thesis supported, validated | 5+ sources, no fallacies |

### 3. Program-of-Thought Scoring Rubrics

**Credibility Score** (1-5):
```
Start: 3
+1 for: Peer-reviewed, PhD author, Cites sources, Reputable institution
-1 for: Self-published, No credentials, No citations, Conflicts
Final: 1-5 (capped)
```

**Bias Risk Score** (1-5):
```
Start: 2
+1 for: Advocacy org, Interested funding, Ideological language, Cherry-picking
Final: 1-5
```

**Reading Priority** (1-5):
```
Formula: (Relevance × 0.4) + (Credibility × 0.3) + (Primary=+2) + (Accessible=+1)
Bands: 5=Immediate, 4=Soon, 3=If time, 2=Defer, 1=Skip
```

### 4. Red's 6 Principles Embedded

| Principle | Implementation |
|-----------|---------------|
| **Trust No One** | Step 3: Systematic credibility + bias scoring |
| **Context is Everything** | Step 4: Temporal/Cultural/Historiographical analysis |
| **Thesis from Evidence** | Step 6: Let thesis EMERGE, "INCONCLUSIVE" option |
| **Wikipedia is Gateway** | Step 1: Mine references, Gate 0 fallback to Scholar |
| **Primary Sources Matter** | ≥2-5 primary sources required in Gates 3 & 6 |
| **Page Numbers Save Lives** | Step 5: ALL quotes require page numbers |

### 5. Error Handling & Failure Modes
- No Wikipedia article? → Google Scholar fallback (Gate 0)
- Can't find primaries? → Document exception, use ≥10 high-cred secondaries
- Evidence contradictory? → "INCONCLUSIVE" thesis with explanation
- Logical fallacies? → Analyst returns to Phase B for revision

---

## How It Was Built

### Design Process (Skill-Forge 7 Phases)

1. **Intent Archaeology** ✅
   - Analyzed Red's (OSP) methodology from YouTube transcript
   - Mapped 6-phase research approach to agent workflows
   - Defined success criteria and Quality Gates

2. **Use Case Crystallization** ✅
   - Example: "Byzantine Empire's influence on Renaissance Italy"
   - Identified pattern: Wikipedia → Sources → Classification → Context → Notes → Synthesis

3. **Structural Architecture** ✅
   - SKILL.md: Core SOP workflow (Steps 0-6)
   - Bundled resources: Process diagram, glossary, methodology, examples
   - Progressive disclosure: Metadata → SKILL.md → References/Examples

4. **Metadata Engineering** ✅
   - Name: `general-research-workflow`
   - Description optimized for discovery (history, mythology, literature keywords)
   - Trigger conditions explicit (6+ hours, source evaluation needed)

5. **Instruction Crafting** ✅
   - Imperative voice throughout
   - Numbered steps with clear objectives
   - Required (✅) vs Optional (⚠️) visual markers
   - Quality Gates with GO/NO-GO criteria

6. **Resource Development** ✅
   - **Process diagram**: `general-research-process.dot` (GraphViz)
   - **Glossary**: Comprehensive definitions (sources, scoring, tools, MCP tagging)
   - **Methodology**: Red's 6 principles with examples and pitfalls
   - **Example**: Source classification with complete scoring calculations

7. **Validation** ✅
   - Prompt-architect analysis identified 22 gaps in v1
   - v2 addressed core structure
   - v3 implemented Priority 1 improvements:
     - Few-shot examples (Step 3 source classification)
     - Missing failure modes (no Wikipedia, no primaries, non-English)
     - Program-of-thought scoring rubrics
     - Gate 0 pre-flight check

---

## Optimization History

### Version 1 → Version 2
- **Changed**: Generic implementation → Proper SOP structure
- **Added**: Agent coordination table, step-by-step workflow, handoffs
- **Removed**: Script-like bash commands

### Version 2 → Version 3 (Prompt-Architect Optimized)
- **Added** (Priority 1 Critical):
  - Gate 0: Pre-flight check (Wikipedia existence verification)
  - Few-shot example: Source classification with scoring calculations
  - Program-of-thought rubrics for credibility/bias/priority
  - Failure modes: No Wikipedia, no primaries, non-English sources, inconclusive evidence
  - Visual markers: ✅ Required, ⚠️ Optional, 💡 Tips, 🚨 Warnings
  - Glossary: Detailed definitions for all technical terms
  - Red's methodology: Full explanation of 6 principles

- **Improved**:
  - Decision tree for "when to use"
  - Error handling table with resolution strategies
  - Success metrics (quantitative + qualitative)
  - Memory MCP tagging requirements explicit

---

## Success Metrics

### Quantitative
- ✅ ≥20 sources in inventory
- ✅ ≥5 primary sources (OR exception documented)
- ✅ ≥80% sources credibility ≥3
- ✅ ≥50 notes captured
- ✅ ≥20 quotes with page numbers
- ✅ ≥5 cross-source links
- ✅ Thesis supported by ≥5 sources (OR "INCONCLUSIVE")
- ✅ ≥2 primaries cited (OR exception)
- ✅ 6-10 hours duration

### Qualitative
- ✅ Context explained for ≥10 sources
- ✅ Biases identified in ≥3 sources
- ✅ Thesis emerges from evidence (not imposed)
- ✅ All claims have citations + page numbers
- ✅ ≥1 limitation acknowledged
- ✅ Alternative interpretations acknowledged
- ✅ NO logical fallacies in final report

---

## Integration with Other Skills

**Before This Skill**:
- `intent-analyzer` - If research question is vague

**During This Skill**:
- `literature-synthesis` - Can run parallel for ML research components
- `source-credibility-analyzer` - Automates Step 3 scoring (if available)

**After This Skill**:
- `academic-reading-workflow` - Deep reading of specific sources (Blue's methodology)
- `research-publication` - Turn findings into academic paper

---

## Example Workflow Execution

```
User: "Research Byzantine Empire's influence on Renaissance Italy"

Step 0 (Gate 0): researcher verifies Wikipedia article exists → PASS
Step 1 (Gate 1): researcher extracts 12 citations from Wikipedia → PASS
Step 2 (Gate 2): researcher finds 23 sources, 14 accessible → PASS
Step 3 (Gate 3): analyst classifies sources → 3 primaries found → FAIL
  Action: Return to Step 2, find 2 more primary sources
  Result: 5 primaries found → PASS

Step 4 (Gate 4): researcher contextualizes 11 sources across 4 time periods → PASS
Step 5 (Gate 5): researcher captures 67 notes, 28 quotes, 7 cross-links → PASS
Step 6 (Gate 6):
  Phase A: researcher identifies 4 recurring themes
  Phase B: researcher drafts thesis supported by 7 sources (3 primaries)
  Phase C: analyst validates - NO fallacies, all claims cited → PASS
  Phase D: coordinator compiles final report

Output: 8-page research report with evidence-based thesis, 23 sources (5 primaries, 18 secondaries), complete citations
```

---

## Files Created

1. **C:\Users\17175\skills\general-research-workflow\SKILL.md**
   - Main skill file (9,500 words)
   - Complete SOP with 7 steps, 7 Quality Gates
   - Agent coordination protocol
   - Red's principles embedded

2. **C:\Users\17175\skills\general-research-workflow\general-research-process.dot**
   - GraphViz workflow visualization
   - Shows all steps, gates, decision points, agent roles
   - Semantic shapes (diamonds=decisions, octagons=gates, cylinders=external refs)

3. **C:\Users\17175\skills\general-research-workflow\references\glossary.md**
   - Comprehensive glossary (4,000 words)
   - Definitions: Primary/secondary sources, scoring systems
   - Tools: WorldCat, Google Scholar, Google Books
   - Memory MCP tagging protocol

4. **C:\Users\17175\skills\general-research-workflow\references\red-methodology.md**
   - Red's 6 principles explained (5,000 words)
   - Implementation in each workflow step
   - Common pitfalls and how to avoid them
   - Direct quotes from OSP video

5. **C:\Users\17175\skills\general-research-workflow\examples\source-classification-example.md**
   - Step 3 output example (2,500 words)
   - 5 sources with complete scoring calculations
   - Shows rubric application
   - Demonstrates Gate 3 failure → retry logic

---

## Design Comparison

| Aspect | v1 Draft | v2 SOP | v3 Optimized |
|--------|----------|--------|--------------|
| Structure | Script-like | Agent SOP | Agent SOP + Examples |
| Failure Modes | 4 covered | 9 covered | 13 covered (all major) |
| Examples | 0 | 0 | 5 (appendices + bundled) |
| Quality Gates | 4 gates | 6 gates | 7 gates (added Gate 0) |
| Scoring Rubrics | Vague | Described | Program-of-thought (explicit) |
| Visual Markers | None | Some | ✅⚠️💡🚨 (systematic) |
| Documentation | Inline | Inline | Inline + Bundled Resources |
| Process Diagram | None | None | GraphViz .dot file |

---

## Next Steps

This is **Skill 1 of 9** from the MECE gap analysis. Remaining Priority 1 skills:

2. **academic-reading-workflow** (Blue's methodology)
   - Summary-first reading
   - Active annotation system
   - Searchable notes ("command-F in real life")

3. **source-credibility-analyzer** (Standalone tool)
   - Automates Step 3 scoring
   - Can be used independently or within general-research-workflow

After these 3 Priority 1 skills are built, move to Priority 2 (digital-annotation-system, research-milestone-planner, wikipedia-citation-extractor).

---

## Credits

**Methodology Source**: Red (Overly Sarcastic Productions) - "How to Do Research" YouTube video
**Design Framework**: Skill-Forge 7-Phase Process
**Optimization**: Prompt-Architect evidence-based analysis
**Implementation**: 3-iteration refinement (Draft → SOP → Optimized)

---

**Production Status**: ✅ READY FOR USE
**Last Updated**: 2025-01-06
**Version**: 3.0 (Optimized)
