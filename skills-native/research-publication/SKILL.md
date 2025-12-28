---
name: research-publication
description: Academic publication preparation for Deep Research SOP Pipeline I including paper writing, reproducibility artifacts, and venue submission. Use when preparing research for publication after Gate 3 APPROVED, submitting to conferences (NeurIPS, ICML, CVPR), or creating ACM artifact submissions. Ensures reproducibility checklists complete, supplementary materials prepared, and all artifacts publicly accessible.
---

paper writing, reproducibility artifacts, and venue submission. Use when preparing
  research for publication after Gate 3 APPROVED, submitting to conferences (NeurIPS,
  ICML, CVPR), or creating ACM artifact submissions. Ensures reproducibility checklists
  complete, supplementary materials prepared, and all artifacts publicly accessible.
- research
- analysis
- planning


## Quick Start

### 1. Initialize Publication Project
```bash
# Create publication structure
mkdir -p publication/{paper,supplementary,code,slides}

# Initialize LaTeX project
cd publication/paper/
git init
cp ~/templates/neurips_2024.tex main.tex
```

### 2. Generate Paper Sections
```bash
# Auto-generate sections from research artifacts
python scripts/generate_paper_sections.py \
  --literature-review ../phase1-foundations/literature_review.md \
  --method-description ../phase2-development/method_card.md \
  --evaluation-results ../phase2-development/holistic_evaluation/report.md \
  --output paper/auto_generated/
```

### 3. Reproducibility Checklist
```bash
# Generate NeurIPS reproducibility checklist
python scripts/generate_reproducibility_checklist.py \
  --venue neurips \
  --artifacts ../phase3-production/ \
  --output paper/reproducibility_checklist.pdf
```

### 4. Supplementary Materials
```bash
# Package supplementary materials
python scripts/package_supplementary.py \
  --ablation-results ../phase2-development/ablations/ \
  --hyperparameters ../phase2-development/hparams/ \
  --additional-experiments ../phase2-development/experiments/ \
  --output supplementary/supplementary.pdf
```

### 5. Artifact Submission
```bash
# Prepare ACM artifact submission
python scripts/prepare_acm_artifact.py \
  --reproducibility-package ../phase3-production/reproducibility-package/ \
  --badge-level "Reproduced+Reusable" \
  --output publication/acm_artifact/
```



#### 1.2 Auto-Generate Sections from Artifacts
```python
# scripts/generate_paper_sections.py

def generate_related_work(literature_review_path):
    """Generate Related Work section from literature synthesis."""
    with open(literature_review_path) as f:
        lit_review = f.read()

    # Extract key papers and organize by themes
    papers = extract_papers(lit_review)
    themes = organize_by_themes(papers)

    latex_output = "\\section{Related Work}\n\n"
    for theme, theme_papers in themes.items():
        latex_output += f"\\subsection{{{theme}}}\n\n"
        for paper in theme_papers:
            latex_output += f"{paper['summary']} \\cite{{{paper['cite_key']}}}.\n"
        latex_output += "\n"

    return latex_output

def generate_method_section(method_card_path):
    """Generate Method section from method card."""
    with open(method_card_path) as f:
        method_card = f.read()

    # Extract architecture details
    architecture = extract_architecture(method_card)

    latex_output = "\\section{Method}\n\n"
    latex_output += "\\subsection{Architecture}\n\n"
    latex_output += architecture["description"] + "\n\n"

    # Add figure
    latex_output += "\\begin{figure}[h]\n"
    latex_output += "  \\centering\n"
    latex_output += f"  \\includegraphics[width=0.8\\linewidth]{{figures/{architecture['diagram']}}}\n"
    latex_output += f"  \\caption{{{architecture['caption']}}}\n"
    latex_output += "\\end{figure}\n\n"

    return latex_output

def generate_results_section(evaluation_report_path):
    """Generate Results section from holistic evaluation."""
    with open(evaluation_report_path) as f:
        eval_report = f.read()

    # Extract tables and figures
    tables = extract_tables(eval_report)
    figures = extract_figures(eval_report)

    latex_output = "\\section{Results}\n\n"

    # Main results table
    latex_output += "\\subsection{Main Results}\n\n"
    latex_output += tables["main_results"] + "\n\n"

    # Ablation studies
    latex_output += "\\subsection{Ablation Studies}\n\n"
    latex_output += tables["ablations"] + "\n\n"

    return latex_output

# Generate all sections
generate_related_work("../phase1-foundations/literature_review.md")
generate_method_section("../phase2-development/method_card.md")
generate_results_section("../phase2-development/holistic_evaluation/report.md")
```

**Deliverable**: Auto-generated paper sections



#### 2.2 Generate Checklist Automatically
```python
# scripts/generate_reproducibility_checklist.py

def generate_checklist(venue, artifacts_path):
    """Generate reproducibility checklist for venue."""
    checklist = {
        "neurips": neurips_checklist_template(),
        "icml": icml_checklist_template(),
        "cvpr": cvpr_checklist_template()
    }

    template = checklist[venue]

    # Auto-fill from artifacts
    template["code_url"] = extract_github_url(artifacts_path)
    template["data_url"] = extract_zenodo_url(artifacts_path, "dataset")
    template["model_url"] = extract_huggingface_url(artifacts_path)

    # Generate PDF
    generate_pdf(template, output_path)

    return template
```

**Deliverable**: Auto-generated reproducibility checklist PDF



#### 3.2 Additional Visualizations
```python
# scripts/generate_supplementary_figures.py

# Attention visualization
attention_weights = extract_attention_weights(model, test_images)
plot_attention_maps(attention_weights, save_path="figures/attention_supp.pdf")

# Ablation study visualizations
ablation_results = load_ablation_results("../phase2-development/ablations/")
plot_ablation_heatmap(ablation_results, save_path="figures/ablation_supp.pdf")

# Hyperparameter sensitivity
hparam_results = load_hparam_results("../phase2-development/hparams/")
plot_sensitivity_curves(hparam_results, save_path="figures/sensitivity_supp.pdf")
```

**Deliverable**: Supplementary figures



### Phase 5: Code Release (2-3 days)

**Objective**: Publish code on GitHub with Zenodo DOI

**Steps**:

#### 5.1 GitHub Repository Setup
```bash
# Create GitHub repository
gh repo create multi-scale-vit --public --description "Multi-Scale Attention for Vision Transformers"

# Initialize repository
git init
git add .
git commit -m "Initial commit: Multi-Scale Attention for Vision Transformers"
git branch -M main
git remote add origin https://github.com/username/multi-scale-vit.git
git push -u origin main

# Create release
git tag -a v1.0.0 -m "Release for paper submission"
git push origin v1.0.0

# Create GitHub release
gh release create v1.0.0 --title "v1.0.0 - Paper Submission" --notes "Code release for Multi-Scale Attention for Vision Transformers paper"
```

#### 5.2 Zenodo DOI Assignment
```bash
# Link GitHub to Zenodo
# 1. Go to https://zenodo.org/account/settings/github/
# 2. Enable repository
# 3. Create new release on GitHub
# 4. Zenodo automatically creates DOI

# Update README with DOI
echo "[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.123456.svg)](https://doi.org/10.5281/zenodo.123456)" >> README.md
git add README.md
git commit -m "Add Zenodo DOI badge"
git push
```

**Deliverable**: GitHub repository with Zenodo DOI



## Integration with Deep Research SOP

### Pipeline Integration
- **Pipeline I (Publication)**: This skill implements the complete publication phase
- **Quality Gate 3**: Must be APPROVED before publication

### Agent Coordination
```
researcher agent writes paper and creates presentation
archivist agent prepares artifact submission and code release
```



## Related Skills and Commands

### Prerequisites
- `gate-validation --gate 3` - Must be APPROVED
- `reproducibility-audit` - Validates artifact quality
- `deployment-readiness` - Validates production deployment

### Related Commands
- All Phase 1-3 outputs (literature review, method card, holistic evaluation)

## Core Principles

Research Publication operates on 3 fundamental principles:

### Principle 1: Reproducibility as Publication Standard
Academic publication without reproducibility artifacts is incomplete scholarship. Code, data, pre-trained models, and environment specifications must be publicly accessible for peer validation and scientific progress.

In practice:
- Reproducibility checklist (NeurIPS, ICML, CVPR) completed with ALL items marked YES or justified N/A
- GitHub repository with Zenodo DOI assigned before paper submission (permanent archival)
- Reproducibility package tested independently (5 steps to reproduce, fresh Docker, public datasets)

### Principle 2: Transparency in Methodology and Results
Every claim must be verifiable. Statistical significance tests, error bars, hyperparameter search details, and baseline comparisons must be documented for peer scrutiny.

In practice:
- 3+ runs per configuration with mean ± std reported in all tables
- Paired t-tests with p-values for statistical significance (p < 0.05 required)
- Complete hyperparameter search details (Bayesian optimization, grid search ranges) in appendix
- Ablation studies (5+ components) validate each novel contribution

### Principle 3: Ethics and Broader Impact Assessment
Publication without societal impact discussion is irresponsible. Data bias, fairness metrics, potential misuse, and limitations must be addressed for ethical research dissemination.

In practice:
- Ethics review APPROVED at Quality Gate 3 (deployment safety, fairness audit, privacy assessment)
- Broader impact statement includes: potential negative societal impacts, safeguards, limitations
- Fairness metrics (demographic parity, equalized odds) reported for production models

-----------|---------|----------|
| **Reproducibility as Afterthought** | Packaging code and artifacts AFTER paper acceptance leads to missing hyperparameters, broken dependencies, inaccessible data, and failed ACM Artifact Evaluation | Create reproducibility package during Phase 3 (gate-validation requirement). Test with archivist agent in fresh Docker. Assign DOIs (Zenodo, HuggingFace) before submission. Include reproducibility checklist in initial submission |
| **Ignoring Reviewer Comments** | Dismissing reviewer concerns or providing vague responses leads to paper rejection. Each comment represents a barrier to publication that MUST be addressed substantively | Create point-by-point response document addressing EVERY reviewer comment explicitly. Add requested experiments (even if Appendix), clarify confusing sections, acknowledge valid limitations. Use "We agree" for valid points, "We respectfully clarify" for misunderstandings |
| **Incomplete Anonymity (Blind Reviews)** | Self-citations, GitHub URLs, institutional affiliations in blind submissions violate anonymity and lead to desk rejection | Use "Our prior work [Anonymous, 2024]" instead of author names, host code on anonymous repositories (Anonymous GitHub), remove acknowledgments mentioning grants/institutions. Validate with venue-specific anonymity checklist |

---

## Conclusion

Research Publication is the culminating skill in Deep Research SOP Pipeline I, transforming 2-6 months of rigorous research (Phases 1-3) into peer-reviewed academic contributions with reproducibility artifacts meeting ACM Artifact Evaluation standards. By enforcing reproducibility checklists, statistical rigor, and ethics assessments, this skill ensures research meets publication standards for top-tier venues (NeurIPS, ICML, CVPR, ACL).

This skill is essential when Quality Gate 3 is APPROVED (production-ready model with validated artifacts) and research is ready for academic dissemination. The 2-4 week timeline includes paper writing (auto-generated sections from research artifacts), reproducibility checklist completion, supplementary materials preparation, ACM artifact submission, code release (GitHub with Zenodo DOI), and presentation slides (15-20 slides for conference talks).

Use this skill when preparing Deep Research SOP outputs for publication, responding to peer review (point-by-point reviewer responses), creating camera-ready versions (final formatting, acknowledgments, references), or submitting to artifact evaluation tracks (ACM badges: Available, Functional, Reproduced, Reusable). The result is a complete publication package: LaTeX paper draft, reproducibility checklist with ALL items addressed, supplementary materials (ablations, proofs, visualizations), ACM artifact submission (tested reproducibility package), public code release (GitHub + Zenodo DOI), and presentation slides. This comprehensive package maximizes publication success while advancing open science through reproducible, ethically sound research contributions.