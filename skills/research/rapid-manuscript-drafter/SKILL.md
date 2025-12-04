---
name: rapid-manuscript-drafter
description: Generate structured research manuscript drafts in 10-15 minutes with
  proper academic sections (Abstract, Introduction, Methods, Results, Discussion).
  Creates scaffolded drafts with placeholders for data, not fabricated content. Use
  for quickly producing first drafts from research ideas, speeding up the writing
  process while maintaining academic integrity.
version: 1.0.0
category: research
tags:
- research
- writing
- manuscript
- academic
- drafting
- rapid
author: ruv
mcp_servers:
  required: [memory-mcp]
  optional: [sequential-thinking]
  auto_enable: true
---

# Rapid Manuscript Drafter

## Purpose

Generate structured, scaffolded research manuscript drafts in 10-15 minutes that provide a solid foundation for academic writing. Unlike tools that fabricate content, this skill creates honest drafts with clear placeholders for user-provided data and findings.

## Critical Ethical Stance

**This skill NEVER fabricates research results or data.**

What we DO:
- Generate document structure and section scaffolding
- Write introduction and background based on known literature
- Create methodology templates based on described approach
- Provide results section structure with [YOUR_DATA] placeholders
- Draft discussion frameworks with logical argument structure

What we DON'T DO:
- Invent experimental results
- Fabricate statistical findings
- Create fake tables or figures with made-up numbers
- Generate citations to non-existent papers

## When to Use This Skill

Activate this skill when:
- Have a research idea ready to write up
- Need to quickly produce a first draft
- Want to overcome blank page syndrome
- Preparing a manuscript outline for collaborators
- Writing conference paper with tight deadline
- Need structured template for thesis chapter

**DO NOT** use this skill for:
- Final polished manuscripts (this is a first draft tool)
- Generating fake research (we don't do that)
- Replacing actual research work

## Manuscript Types Supported

1. **Research Article** (IMRaD format)
2. **Conference Paper** (shorter, focused)
3. **Review Article** (literature synthesis)
4. **Technical Report**
5. **Thesis Chapter**
6. **Grant Proposal Section**

## Input Contract

```yaml
input:
  manuscript_type: enum[research_article, conference_paper, review, technical_report, thesis_chapter, grant_section] (required)

  research_content:
    title: string (required)
    abstract_points: array[string] (optional)
    research_question: string (required)
    hypotheses: array[string] (optional)
    methodology_description: string (required)
    key_findings_summary: string (optional, will use placeholders if empty)
    contribution_claims: array[string] (required)

  literature_context:
    key_papers: array[object] (optional)
      title: string
      authors: string
      year: number
      relevance: string
    research_gap: string (required)

  target_venue:
    name: string (optional)
    word_limit: number (optional)
    style: enum[ieee, acm, nature, apa, chicago] (default: apa)

  output_preferences:
    include_placeholders: boolean (default: true)
    include_writing_tips: boolean (default: true)
    generate_outline_first: boolean (default: true)
```

## Output Contract

```yaml
output:
  manuscript:
    title: string
    sections: array[object]
      name: string
      content: string
      word_count: number
      completeness: percentage
      placeholders: array[string]

  outline:
    structure: object (hierarchical outline)

  metadata:
    total_words: number
    total_placeholders: number
    sections_complete: number
    sections_scaffolded: number
    generation_time: number

  next_steps:
    required_additions: array[string]
    recommended_revisions: array[string]
```

## SOP Phase 1: Outline Generation

Create hierarchical document structure:

```markdown
## Manuscript Outline: [TITLE]

### 1. Abstract (~250 words)
- Background context (1-2 sentences)
- Research gap/problem (1 sentence)
- Methodology summary (1-2 sentences)
- Key findings (2-3 sentences)
- Implications (1 sentence)

### 2. Introduction (~800-1000 words)
- 2.1 Opening hook and context
- 2.2 Background and related work
- 2.3 Research gap identification
- 2.4 Research questions/hypotheses
- 2.5 Contribution statement
- 2.6 Paper organization

### 3. Related Work (~600-800 words)
- 3.1 [Theme 1 from literature]
- 3.2 [Theme 2 from literature]
- 3.3 Gap analysis and positioning

### 4. Methodology (~800-1200 words)
- 4.1 Research design overview
- 4.2 Data collection
- 4.3 Analysis approach
- 4.4 Validation strategy

### 5. Results (~600-1000 words)
- 5.1 [Finding 1 - placeholder]
- 5.2 [Finding 2 - placeholder]
- 5.3 Summary of findings

### 6. Discussion (~800-1000 words)
- 6.1 Interpretation of results
- 6.2 Comparison with prior work
- 6.3 Implications
- 6.4 Limitations
- 6.5 Future work

### 7. Conclusion (~200-300 words)
- Summary
- Key contributions
- Call to action

### References
- [Placeholder for bibliography]
```

## SOP Phase 2: Section Drafting

### Abstract Template

```markdown
## Abstract

[BACKGROUND CONTEXT - 1-2 sentences about the field and why it matters]

[RESEARCH GAP - 1 sentence identifying the specific problem addressed]

In this work, we [METHODOLOGY SUMMARY - brief description of approach].

[KEY FINDINGS - use provided findings or placeholder]:
- [FINDING 1: YOUR_RESULT_HERE]
- [FINDING 2: YOUR_RESULT_HERE]

Our results demonstrate [IMPLICATION - how this advances the field].

**Keywords**: [keyword1], [keyword2], [keyword3], [keyword4], [keyword5]
```

### Introduction Template

```markdown
## 1. Introduction

[HOOK - Opening sentence that captures attention and establishes importance]

### Background and Context

[BACKGROUND PARAGRAPH 1 - Establish the broader research area]
The field of [DOMAIN] has seen significant advances in recent years,
particularly in [SPECIFIC AREA] (Author1 et al., YEAR; Author2 et al., YEAR).

[BACKGROUND PARAGRAPH 2 - Narrow to specific topic]
Within this context, [SPECIFIC TOPIC] has emerged as a critical challenge
because [REASON FOR IMPORTANCE].

### Research Gap

Despite these advances, [RESEARCH GAP STATEMENT]. Current approaches
[LIMITATION 1] and [LIMITATION 2]. This limitation is significant because
[WHY IT MATTERS].

### Research Questions

This work addresses the following research questions:
- RQ1: [RESEARCH QUESTION 1]
- RQ2: [RESEARCH QUESTION 2]

### Contributions

The main contributions of this paper are:
1. [CONTRIBUTION 1]
2. [CONTRIBUTION 2]
3. [CONTRIBUTION 3]

### Paper Organization

The remainder of this paper is organized as follows. Section 2 reviews
related work. Section 3 describes our methodology. Section 4 presents
results. Section 5 discusses implications, and Section 6 concludes.
```

### Methodology Template

```markdown
## 3. Methodology

### 3.1 Research Design Overview

[METHODOLOGY DESCRIPTION - from user input]

Figure 1 illustrates our overall approach.

[FIGURE 1 PLACEHOLDER: Insert methodology flowchart here]

### 3.2 Data Collection

**Dataset/Participants**: [YOUR_DATA_DESCRIPTION_HERE]
- Sample size: [N = YOUR_NUMBER]
- Collection period: [YOUR_DATES]
- Selection criteria: [YOUR_CRITERIA]

**Data Sources**:
- Source 1: [DESCRIPTION]
- Source 2: [DESCRIPTION]

### 3.3 Analysis Approach

[ANALYSIS DESCRIPTION]

The key steps in our analysis are:
1. [STEP 1]
2. [STEP 2]
3. [STEP 3]

### 3.4 Validation Strategy

To ensure validity, we [VALIDATION APPROACH].

- Internal validity: [YOUR_APPROACH]
- External validity: [YOUR_APPROACH]
- Reliability: [YOUR_APPROACH]
```

### Results Template

```markdown
## 4. Results

### 4.1 [Finding Category 1]

[YOUR RESULTS PARAGRAPH HERE]

Table 1 summarizes [WHAT TABLE SHOWS].

**[TABLE 1 PLACEHOLDER]**
| Metric | Baseline | Proposed | Improvement |
|--------|----------|----------|-------------|
| [Metric 1] | [YOUR_DATA] | [YOUR_DATA] | [YOUR_DATA] |
| [Metric 2] | [YOUR_DATA] | [YOUR_DATA] | [YOUR_DATA] |

### 4.2 [Finding Category 2]

[YOUR RESULTS PARAGRAPH HERE]

Figure 2 illustrates [WHAT FIGURE SHOWS].

**[FIGURE 2 PLACEHOLDER]**: [Description of figure to insert]

### 4.3 Summary of Findings

In summary, our results show:
1. [FINDING SUMMARY 1 - YOUR_TEXT]
2. [FINDING SUMMARY 2 - YOUR_TEXT]
3. [FINDING SUMMARY 3 - YOUR_TEXT]
```

### Discussion Template

```markdown
## 5. Discussion

### 5.1 Interpretation of Results

Our findings demonstrate [MAIN INTERPRETATION]. This is significant
because [SIGNIFICANCE].

The result that [SPECIFIC FINDING] suggests [INTERPRETATION]. This
aligns with / contradicts [PRIOR WORK] who found [PRIOR FINDING].

### 5.2 Comparison with Prior Work

Compared to [RELATED WORK 1], our approach [COMPARISON]. Unlike
[RELATED WORK 2], we [DIFFERENTIATION].

Table X compares our results with prior work.

**[TABLE X PLACEHOLDER: Comparison with prior work]**

### 5.3 Implications

**Theoretical Implications**: [YOUR_THEORETICAL_IMPLICATIONS]

**Practical Implications**: [YOUR_PRACTICAL_IMPLICATIONS]

### 5.4 Limitations

This work has several limitations:
1. [LIMITATION 1] - [MITIGATION OR FUTURE WORK]
2. [LIMITATION 2] - [MITIGATION OR FUTURE WORK]
3. [LIMITATION 3] - [MITIGATION OR FUTURE WORK]

### 5.5 Future Work

Future research directions include:
- [FUTURE DIRECTION 1]
- [FUTURE DIRECTION 2]
- [FUTURE DIRECTION 3]
```

### Conclusion Template

```markdown
## 6. Conclusion

This paper addressed [RESEARCH PROBLEM] by [APPROACH SUMMARY].

Our key contributions include:
1. [CONTRIBUTION 1]
2. [CONTRIBUTION 2]
3. [CONTRIBUTION 3]

The results demonstrate [MAIN FINDING SUMMARY]. This work advances
[FIELD] by [HOW IT ADVANCES].

Future work will explore [FUTURE DIRECTION].

[OPTIONAL: Call to action or broader impact statement]
```

## SOP Phase 3: Writing Tips Insertion

Add contextual writing guidance:

```markdown
<!-- WRITING TIP: Introduction Hook -->
Start with a compelling fact, statistic, or scenario that immediately
demonstrates why this research matters. Avoid generic openings like
"In recent years..." when possible.

<!-- WRITING TIP: Results Section -->
Lead with your most important finding. Use topic sentences that state
the finding, then provide evidence. Don't interpret here - save that
for Discussion.

<!-- WRITING TIP: Placeholder Completion -->
Replace [YOUR_DATA] placeholders with actual values. Ensure all claims
are supported by your actual results.
```

## SOP Phase 4: Quality Checklist

Generate completion checklist:

```markdown
## Manuscript Completion Checklist

### Structure
- [ ] All sections present and in correct order
- [ ] Logical flow between sections
- [ ] Appropriate section lengths for venue

### Content
- [ ] Abstract accurately summarizes paper
- [ ] Introduction clearly states gap and contributions
- [ ] Methodology reproducible from description
- [ ] Results support claims made
- [ ] Discussion interprets (not repeats) results
- [ ] Limitations honestly acknowledged
- [ ] Conclusion doesn't introduce new material

### Placeholders to Complete
- [ ] [YOUR_DATA] - X occurrences
- [ ] [FIGURE] - X occurrences
- [ ] [TABLE] - X occurrences
- [ ] [CITATION] - X occurrences

### Final Polish
- [ ] Check word count against venue limit
- [ ] Verify citation format matches venue
- [ ] Proofread for clarity and grammar
- [ ] Get feedback from collaborators
```

## Example Execution

**Input**:
```yaml
manuscript_type: research_article
research_content:
  title: "Improving Drug Discovery with Graph Neural Networks"
  research_question: "Can graph neural networks improve molecular property
    prediction compared to traditional fingerprint-based methods?"
  methodology_description: "We train GNN models on molecular graphs and
    compare against random forest baselines on three benchmark datasets"
  contribution_claims:
    - "Novel GNN architecture for molecular property prediction"
    - "Comprehensive benchmark on 3 public datasets"
    - "Interpretability analysis of learned representations"
literature_context:
  research_gap: "Existing GNN approaches lack interpretability for
    domain experts in pharmaceutical settings"
target_venue:
  name: "Journal of Chemical Information and Modeling"
  word_limit: 8000
  style: acs
```

**Output** (abbreviated):
```markdown
# Improving Drug Discovery with Graph Neural Networks

## Abstract
Drug discovery remains a costly and time-consuming process, with
molecular property prediction serving as a critical bottleneck...

[KEY FINDINGS PLACEHOLDER: YOUR_ACCURACY_IMPROVEMENT_HERE]

## 1. Introduction
The pharmaceutical industry faces unprecedented challenges...

[Full scaffolded manuscript with placeholders]

## Completion Status
- Sections drafted: 7/7
- Placeholders remaining: 12
- Estimated completion: 60%
- Next steps: Add experimental results, figures, citations
```

## Integration Points

### Receives From
- **rapid-idea-generator**: Research ideas to write up
- **research-gap-visualizer**: Gap evidence for introduction
- **literature-synthesis**: Related work content
- **visual-asset-generator**: Figures and tables

### Feeds Into
- **research-publication**: Final manuscript preparation
- **gate-validation**: Quality gate for publication readiness

## Feature Comparison

| Feature | Basic Tools | This Skill |
|---------|--------|------------|
| Speed | 5 min | 10-15 min |
| Data fabrication | YES (problematic) | NO (placeholders) |
| Section structure | Yes | Yes (IMRaD) |
| Writing tips | No | Yes |
| Completion checklist | No | Yes |
| Venue customization | No | Yes |
| Citation placeholders | Fake citations | [CITATION NEEDED] markers |
| Figures/tables | Fabricated | Placeholders with descriptions |

## Success Criteria

- [ ] All sections generated with appropriate structure
- [ ] No fabricated data or results
- [ ] Placeholders clearly marked
- [ ] Writing tips contextually relevant
- [ ] Completion checklist accurate
- [ ] Word count appropriate for venue
- [ ] Logical argument flow maintained

## Ethical Guidelines

1. **Placeholders over fabrication** - Always use [YOUR_DATA] instead of making up numbers
2. **Honest scaffolding** - Structure guides writing, doesn't replace research
3. **Clear marking** - All placeholders clearly identifiable
4. **Academic integrity** - Draft is a tool, not a substitute for research

---

**Version**: 1.0.0
**Category**: Research / Writing
**Time**: 10-15 minutes for full draft
**Output**: Scaffolded manuscript with placeholders
**Design**: Ethical scaffolding with placeholder-based content
