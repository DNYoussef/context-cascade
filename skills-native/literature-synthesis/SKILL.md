---
name: literature-synthesis
description: Systematic literature review and synthesis for Deep Research SOP Pipeline A. Use when starting research projects, conducting SOTA analysis, identifying research gaps, or preparing academic papers. Implements PRISMA-compliant systematic review methodology with automated search, screening, and synthesis across ArXiv, Semantic Scholar, and Papers with Code.
---

A. Use when starting research projects, conducting SOTA analysis, identifying research
  gaps, or preparing academic papers. Implements PRISMA-compliant systematic review
  methodology with automated search, screening, and synthesis across ArXiv, Semantic
  Scholar, and Papers with Code.
## Quick Start

### 1. Define Search Query
```bash
# Store research question in memory
npx claude-flow@alpha memory store \
  --key "sop/literature-review/research-question" \
  --value "How does multi-scale attention improve long-range dependency modeling in vision transformers?"

# Define search terms
search_terms="(multi-scale OR hierarchical) AND (attention OR transformer) AND (vision OR image)"
```

### 2. Database Search
```bash
# Search ArXiv
python scripts/search_arxiv.py \
  --query "$search_terms" \
  --start-date "2020-01-01" \
  --max-results 500 \
  --output literature/arxiv_results.json

# Search Semantic Scholar
python scripts/search_semantic_scholar.py \
  --query "$search_terms" \
  --fields "title,abstract,authors,year,citationCount,venue" \
  --min-citations 10 \
  --output literature/semantic_scholar_results.json

# Search Papers with Code
python scripts/search_papers_with_code.py \
  --task "image-classification" \
  --method "transformer" \
  --output literature/pwc_results.json
```

### 3. Screening and Selection
```bash
# Title/abstract screening
python scripts/screen_papers.py \
  --input literature/*_results.json \
  --inclusion-criteria literature/inclusion_criteria.yaml \
  --output literature/screened_papers.json

# Full-text review
python scripts/full_text_review.py \
  --input literature/screened_papers.json \
  --download-dir literature/pdfs/ \
  --output literature/selected_papers.json
```

### 4. Synthesis
```bash
# Extract SOTA benchmarks
python scripts/extract_sota_benchmarks.py \
  --papers literature/selected_papers.json \
  --datasets "ImageNet,CIFAR-10,CIFAR-100" \
  --output literature/sota_benchmarks.csv

# Identify research gaps
python scripts/identify_gaps.py \
  --papers literature/selected_papers.json \
  --output literature/research_gaps.md
```

### 5. Generate Literature Review
```bash
# Generate review document
python scripts/generate_literature_review.py \
  --papers literature/selected_papers.json \
  --benchmarks literature/sota_benchmarks.csv \
  --gaps literature/research_gaps.md \
  --template templates/literature_review_template.md \
  --output docs/literature_review.md
```

### Phase 2: Database Search (2-4 hours)

**Objective**: Retrieve papers from multiple databases

**Steps**:

#### 2.1 ArXiv Search
```python
# scripts/search_arxiv.py
import arxiv

client = arxiv.Client()
search = arxiv.Search(
    query="(multi-scale OR hierarchical) AND (attention OR transformer) AND vision",
    max_results=500,
    sort_by=arxiv.SortCriterion.SubmittedDate,
    sort_order=arxiv.SortOrder.Descending
)

results = []
for paper in client.results(search):
    results.append({
        "title": paper.title,
        "authors": [author.name for author in paper.authors],
        "abstract": paper.summary,
        "published": paper.published.isoformat(),
        "arxiv_id": paper.entry_id.split("/")[-1],
        "pdf_url": paper.pdf_url,
        "categories": paper.categories
    })

# Save results
import json
with open("literature/arxiv_results.json", "w") as f:
    json.dump(results, f, indent=2)

print(f"Retrieved {len(results)} papers from ArXiv")
```

#### 2.2 Semantic Scholar Search
```python
# scripts/search_semantic_scholar.py
import requests

API_KEY = "YOUR_S2_API_KEY"
ENDPOINT = "https://api.semanticscholar.org/graph/v1/paper/search"

params = {
    "query": "(multi-scale OR hierarchical) AND (attention OR transformer) AND vision",
    "fields": "title,abstract,authors,year,citationCount,venue,publicationDate",
    "limit": 100,
    "minCitationCount": 10,
    "year": "2020-"
}

response = requests.get(ENDPOINT, params=params, headers={"x-api-key": API_KEY})
papers = response.json()["data"]

# Save results
with open("literature/semantic_scholar_results.json", "w") as f:
    json.dump(papers, f, indent=2)

print(f"Retrieved {len(papers)} papers from Semantic Scholar")
```

#### 2.3 Papers with Code Search
```bash
# Download Papers with Code dataset
curl -o literature/pwc_dataset.json \
  https://paperswithcode.com/api/v1/papers/?tasks=image-classification&methods=transformer

# Filter relevant papers
python scripts/filter_pwc_papers.py \
  --input literature/pwc_dataset.json \
  --keywords "attention,multi-scale,hierarchical" \
  --output literature/pwc_results.json
```

**Deliverable**: Combined database of ~200-500 papers

### Phase 4: Full-Text Review (3-5 days)

**Objective**: Review full papers for final inclusion

**Steps**:

#### 4.1 Download PDFs
```python
# scripts/download_pdfs.py
import requests
from pathlib import Path

pdf_dir = Path("literature/pdfs")
pdf_dir.mkdir(exist_ok=True)

for paper in screened_papers:
    pdf_url = paper.get("pdf_url") or paper.get("openAccessPdf", {}).get("url")
    if pdf_url:
        filename = f"{paper['arxiv_id'] or paper['paperId']}.pdf"
        response = requests.get(pdf_url)
        (pdf_dir / filename).write_bytes(response.content)
        print(f"Downloaded: {filename}")
```

#### 4.2 Extract Key Information
```python
# scripts/extract_paper_info.py

def extract_info(paper_pdf):
    """Extract key information from paper."""
    info = {
        "methods": [],  # Novel methods proposed
        "datasets": [],  # Datasets used
        "metrics": {},  # Performance metrics
        "comparisons": [],  # Baseline comparisons
        "limitations": [],  # Reported limitations
        "future_work": []  # Suggested future work
    }

    # Use PyPDF2 or pdfplumber to extract text
    # Use regex or NLP to extract structured information
    # (Implementation details omitted for brevity)

    return info

# Extract info from all papers
for paper in screened_papers:
    pdf_path = f"literature/pdfs/{paper['arxiv_id']}.pdf"
    if Path(pdf_path).exists():
        paper["extracted_info"] = extract_info(pdf_path)
```

#### 4.3 Final Inclusion Decision
```python
# Manual review criteria
def final_review(paper):
    """Final inclusion decision based on full text."""
    info = paper.get("extracted_info", {})

    # Must report quantitative results
    if not info.get("metrics"):
        return False, "No quantitative results"

    # Must use standard benchmarks
    standard_datasets = ["ImageNet", "CIFAR-10", "CIFAR-100", "COCO"]
    if not any(ds in info.get("datasets", []) for ds in standard_datasets):
        return False, "No standard benchmarks"

    # Must compare with baselines
    if not info.get("comparisons"):
        return False, "No baseline comparisons"

    return True, "Included"

# Final review
selected_papers = []
for paper in screened_papers:
    include, reason = final_review(paper)
    if include:
        selected_papers.append(paper)

print(f"{len(selected_papers)} papers selected for synthesis")
```

**Deliverable**: 50-70 final selected papers

### Phase 6: Writing (1-2 days)

**Objective**: Write comprehensive literature review

**Steps**:

#### 6.1 Structure Literature Review
```markdown
# Literature Review: Multi-Scale Attention in Vision Transformers

## 1. Introduction
- Research question and motivation
- Scope of review (50+ papers, 2020-2025)
- Organization of review

## 2. Background
- Vision Transformers fundamentals
- Attention mechanisms overview
- Multi-scale representations in vision

## 3. Attention Mechanisms in Vision
### 3.1 Self-Attention
- Vanilla self-attention (Vaswani et al., 2017)
- Vision Transformer (Dosovitskiy et al., 2021)

### 3.2 Hierarchical Attention
- Swin Transformer (Liu et al., 2021)
- Pyramid Vision Transformer (Wang et al., 2021)

### 3.3 Multi-Scale Attention
- CrossViT (Chen et al., 2021)
- Multi-Scale Vision Transformer (Fan et al., 2021)

## 4. State-of-the-Art Performance
[Table of SOTA benchmarks]

## 5. Research Gaps
- Methodological gaps
- Application gaps
- Evaluation gaps

## 6. Proposed Direction
- Hypotheses based on gaps
- Expected contributions

## 7. Conclusion
```

#### 6.2 Generate BibTeX Citations
```python
# scripts/generate_bibtex.py

def paper_to_bibtex(paper):
    """Convert paper to BibTeX entry."""
    authors = " and ".join(paper["authors"])
    year = paper["year"]
    title = paper["title"]
    venue = paper.get("venue", "arXiv")

    bibtex_key = f"{paper['authors'][0].split()[-1]}{year}"

    return f"""@inproceedings{{{bibtex_key},
  title={{{title}}},
  author={{{authors}}},
  booktitle={{{venue}}},
  year={{{year}}}
}}"""

# Generate bibliography
with open("literature/bibliography.bib", "w") as f:
    for paper in selected_papers:
        f.write(paper_to_bibtex(paper) + "\n\n")
```

**Deliverable**: Complete literature review document

## Integration with Deep Research SOP

### Pipeline Integration
- **Pipeline A (Literature Synthesis)**: This skill implements the complete literature review phase
- **Phase 1 (Foundations)**: Required before baseline replication
- **Quality Gate 1**: Minimum 50 papers required

### Agent Coordination
```
researcher agent:
  - Conducts database searches
  - Screens papers
  - Extracts key information
  - Synthesizes findings
  - Formulates hypotheses
```

### Memory Coordination
```bash
# Store literature review in memory
npx claude-flow@alpha memory store \
  --key "sop/phase1/literature-review" \
  --value "$(cat docs/literature_review.md)"

# Store SOTA benchmarks
npx claude-flow@alpha memory store \
  --key "sop/phase1/sota-benchmarks" \
  --value "$(cat literature/sota_benchmarks.csv)"
```

## Related Skills and Commands

### Prerequisites
- None (first skill in Deep Research SOP workflow)

### Next Steps
- `baseline-replication` - Replicate SOTA baselines identified in literature review
- `gate-validation --gate 1` - Validate Phase 1 completion

### Related Commands
- `/prisma-init` - Initialize PRISMA systematic review (researcher agent)

## Core Principles

Literature Synthesis operates on 3 fundamental principles:

### Principle 1: PRISMA-Compliant Systematic Methodology
All literature reviews follow PRISMA (Preferred Reporting Items for Systematic Reviews and Meta-Analyses) guidelines with documented search strategy, inclusion/exclusion criteria, and screening process. This ensures reproducible and comprehensive coverage.

In practice:
- Pre-registered search terms and databases before screening begins
- PRISMA flow diagram documents identification, screening, eligibility, and inclusion phases
- Minimum 50 papers reviewed for Quality Gate 1 compliance

### Principle 2: Multi-Source Triangulation for SOTA Validation
State-of-the-art claims are cross-validated across ArXiv, Semantic Scholar, and Papers with Code to identify consensus performance benchmarks and conflicting results. This prevents reliance on single-source biases.

In practice:
- SOTA benchmarks extracted from 3+ independent sources (papers, leaderboards, reproducibility studies)
- Conflicting results reported with methodology analysis to explain divergence
- Citation counts and venue tier (h-index, acceptance rates) used as credibility filters

### Principle 3: Transparent Research Gap Identification
Research gaps are identified through systematic evidence rather than intuition, with explicit documentation of what was searched, what was found, and what remains unexplored. This enables hypothesis formulation grounded in literature.

In practice:
- Methodological gaps: Attention types explored vs unexplored (self, cross, multi-scale, sparse)
- Application gaps: Datasets used vs underexplored (ImageNet covered, Cityscapes underexplored)
- Evaluation gaps: Metrics reported (accuracy) vs missing (fairness, robustness)

## Common Anti-Patterns

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| **Cherry-Picking Papers** | Selecting only papers supporting predetermined conclusions creates confirmation bias and misses contradictory evidence | Use systematic search with pre-registered criteria, report contradictory findings explicitly |
| **Claiming Gaps Without Evidence** | Asserting novelty without systematic search allows claims like "no prior work on X" when X exists in literature | Document search queries used, databases consulted, and negative results (searched but found nothing) |
| **Single-Source SOTA Benchmarks** | Relying on one paper's reported SOTA creates vulnerability to errors, non-reproducible results, or outdated information | Cross-validate SOTA across Papers with Code leaderboards, reproducibility studies, and multiple independent papers |

## Conclusion

Literature Synthesis provides PRISMA-compliant systematic literature review methodology for identifying state-of-the-art methods, performance benchmarks, and research gaps. By enforcing multi-source triangulation, transparent search documentation, and explicit gap analysis, this skill ensures literature reviews meet academic publication standards and Quality Gate 1 requirements.

Use this skill at the start of research projects (Deep Research SOP Phase 1) when conducting SOTA analysis, preparing related work sections, or validating novelty claims. The 7-phase workflow (search strategy, database search, screening, full-text review, synthesis, writing, PRISMA documentation) produces comprehensive reviews with 50-100+ papers, SOTA benchmark tables, and evidence-backed research gap identification. The result is a solid foundation for hypothesis formulation and method development with clear understanding of what exists, what performs best, and what remains unexplored.

---