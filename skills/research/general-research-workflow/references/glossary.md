# Glossary - General Research Workflow

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



## Source Types

### Primary Source
**Definition**: Original documents, eyewitness accounts, artifacts, contemporary records, or original research data **created AT THE TIME** of the events being studied.

**Examples**:
- Letters, diaries, journals from the period
- Official government documents from that era
- Eyewitness testimonies
- Artifacts and archaeological finds
- Contemporary newspapers
- Original research data and lab notebooks
- Photographs, audio/video recordings from the time

**Not Primary**: A biography written 100 years after someone's death, even if well-researched, is secondary.

### Secondary Source
**Definition**: Analysis, interpretation, or evaluation of primary sources **created AFTER** the events.

**Examples**:
- History textbooks
- Encyclopedias
- Biographies written after subject's death
- Review articles summarizing multiple studies
- Documentaries about historical events
- Academic analyses of primary documents

---

## Scoring Systems

### Credibility Score (1-5)
**Purpose**: Assess reliability of source based on objective criteria

**Scoring Rubric**:
- **Start at 3 (Neutral)**
- **Add +1 for each**:
  - Peer-reviewed publication (academic journal, university press)
  - Author has PhD or recognized expertise in field
  - Source cites primary sources and provides extensive references
  - Published by reputable institution
- **Subtract -1 for each**:
  - Self-published or vanity press
  - No author credentials listed
  - No citations or references provided
  - Known conflicts of interest

**Scale**:
- **5**: Highly credible (peer-reviewed, expert author, extensive citations)
- **4**: Credible (reputable publisher, qualified author)
- **3**: Neutral (some credentials, basic citations)
- **2**: Low credibility (weak credentials, few citations)
- **1**: Not credible (no credentials, no citations, conflicts)

### Bias Risk Score (1-5)
**Purpose**: Identify likelihood of systematic distortion

**Scoring Rubric**:
- **Start at 2 (Low Bias)**
- **Add +1 for each**:
  - Author affiliated with advocacy organization
  - Funding from interested party (government, corporation with stake)
  - Strong ideological language detected
  - Cherry-picked evidence or one-sided presentation

**Scale**:
- **1**: Minimal bias (objective, balanced presentation)
- **2**: Low bias (slight lean but fair coverage)
- **3**: Moderate bias (identifiable lean but still useful)
- **4**: High bias (strong partisanship, selective evidence)
- **5**: Extreme bias (propaganda, severely one-sided)

**Note**: Bias doesn't automatically disqualify a source, but requires extra scrutiny and balance with other perspectives.

### Reading Priority (1-5)
**Purpose**: Determine reading order to maximize research efficiency

**Formula**:
```
Priority = (Relevance × 0.4) + (Credibility × 0.3) +
           (Primary Source = +2, Secondary = 0) +
           (Accessible = +1, Not Accessible = -1)

Normalized to 1-5 scale
```

**Priority Bands**:
- **5**: Read IMMEDIATELY (high-quality primary sources directly addressing research question)
- **4**: Read soon (credible secondary sources or accessible primary sources)
- **3**: Read if time permits (moderate quality or tangentially related)
- **2**: Defer to end (low relevance or credibility issues)
- **1**: Skip unless critical gap (inaccessible or very low quality)

---

## Research Tools

### WorldCat
**URL**: worldcat.org
**Purpose**: Global library catalog for finding books in nearby libraries
**Usage**: Search by title, author, or ISBN to locate physical copies

### Google Scholar
**URL**: scholar.google.com
**Purpose**: Search engine for academic publications
**Features**:
- "Cited by" function to find influential papers
- PDF links when available
- Citation export (BibTeX, EndNote)
- Related articles suggestions

### Google Books
**URL**: books.google.com
**Purpose**: Search inside books, find previews
**Features**:
- Preview pages (varies by book)
- "Buy" links to purchase
- Library locations via WorldCat integration

---

## Research Concepts

### Historiography
**Definition**: The study of how history has been written and interpreted over time; the scholarly debate surrounding historical topics.

**Why It Matters**: Understanding historiographical context helps you:
- See how interpretations have evolved
- Identify which "school of thought" an author represents
- Recognize biases embedded in different time periods
- Position your own research within ongoing debates

**Example**: Different historiographical approaches to the Renaissance:
- Burckhardt (19th century): "Rebirth" of classical civilization
- Modern historians: Continuity with medieval period, regional variations
- Your task: Understand which interpretation each source reflects

### Translation Provenance
**Definition**: The history and reputation of a translation, including translator's choices and known issues.

**Why It Matters**:
- Translations can introduce biases
- Some translations are more accurate than others
- Multiple translations of same text may differ significantly

**Best Practice**: When using translated sources, note:
- Who translated it?
- When was it translated?
- Is this translation considered reliable?
- Are alternative translations available for comparison?

---

## Memory MCP Tagging Protocol

**Required Tags for ALL stored data**:

### WHO (Agent Metadata)
- Which agent performed this action?
- Example: `WHO=researcher`, `WHO=analyst`, `WHO=coordinator`

### WHEN (Timestamp)
- ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`
- Unix timestamp also acceptable
- Example: `WHEN=2025-01-06T14:30:00Z`

### PROJECT (Research Topic)
- Research question or topic identifier
- Slug format (lowercase, hyphens)
- Example: `PROJECT=byzantine-renaissance-italy`

### WHY (Intent)
- Purpose of this action
- Examples: `WHY=source-discovery`, `WHY=note-taking`, `WHY=synthesis`

**Storage Format**:
```bash
npx claude-flow@alpha memory store \
  --key "research/[topic]/[component]" \
  --value "[content]" \
  --tags "WHO=[agent],WHEN=[timestamp],PROJECT=[topic],WHY=[intent]"
```

---

## Quality Gate System

**Purpose**: Prevent progression to next step until minimum standards met

### Gate Structure
Each gate has:
- **Requirement**: Quantitative threshold (e.g., "≥10 citations")
- **GO Criteria**: What allows progression
- **NO-GO Action**: What to do if requirements not met

### All 7 Gates

| Gate | After Step | Requirement | NO-GO Action |
|------|-----------|-------------|--------------|
| 0 | Pre-Flight | ≥1 viable starting source | Escalate to user |
| 1 | Wikipedia Mining | ≥10 citations, ≥3 categories | Expand to related articles |
| 2 | Source Discovery | ≥20 sources, ≥50% accessible | Continue discovery |
| 3 | Source Classification | ≥5 primaries, ≥80% credibility ≥3 | Return to Step 2 |
| 4 | Contextual Analysis | ≥10 contextualized, ≥3 time periods | Continue analysis |
| 5 | Note-Taking | ≥50 notes, ≥20 quotes, ≥5 cross-links | Re-read sources |
| 6 | Synthesis | Thesis supported, ≥2 primaries, no fallacies | Return to Phase B |

**Philosophy**: Better to extend duration than produce low-quality research.


---
*Promise: `<promise>GLOSSARY_VERIX_COMPLIANT</promise>`*
