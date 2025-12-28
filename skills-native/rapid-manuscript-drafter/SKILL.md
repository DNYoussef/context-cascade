---
name: rapid-manuscript-drafter
description: Generate structured research manuscript drafts in 10-15 minutes with proper academic sections (Abstract, Introduction, Methods, Results, Discussion). Creates scaffolded drafts with placeholders for data, not fabricated content. Use for quickly producing first drafts from research ideas, speeding up the writing process while maintaining academic integrity.
---

proper academic sections (Abstract, Introduction, Methods, Results, Discussion).
  Creates scaffolded drafts with placeholders for data, not fabricated content. Use
  for quickly producing first drafts from research ideas, speeding up the writing
  process while maintaining academic integrity.
- research
- writing
- manuscript
- academic
- drafting
- rapid
mcp_servers:
  required: [memory-mcp]
  optional: [sequential-thinking]
  auto_enable: true
-----|----------|----------|-------------|
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

## Core Principles

### 1. Scaffolding Over Fabrication
Academic writing tools must never cross the line from assistance to deception. This skill creates structural frameworks that guide authentic research communication.

**In practice:**
- Generate document outlines with proper academic section hierarchy (Abstract, IMRaD)
- Create writing prompts that help articulate genuine research contributions
- Provide templates that organize thoughts without replacing original thinking
- Use placeholders like [YOUR_DATA] to mark where real content must be inserted
- Flag sections requiring user input with specific guidance on what information belongs

### 2. Speed Without Sacrifice of Integrity
Rapid drafting should accelerate the mechanical aspects of writing while preserving the essential human elements of research communication - original thought, data interpretation, and scholarly argumentation.

**In practice:**
- Reduce time on boilerplate structure (paper organization, section transitions)
- Automate citation placeholder insertion ([Author, Year] markers)
- Generate section templates based on venue requirements (page limits, formatting)
- Preserve researcher control over all substantive claims and findings
- Maintain clear separation between auto-generated structure and required user content

### 3. Transparency in Assistance
Users must always know what is generated versus what requires their expertise. The boundary between tool-assisted and human-created content must be unmistakable.

**In practice:**
- Mark all generated content with clear indicators (<!-- AI-GENERATED TEMPLATE -->)
- Use distinctive placeholder syntax that cannot be mistaken for real content
- Include metadata showing what sections are complete vs scaffolded
- Generate completion checklists highlighting all areas needing user input
- Provide "generation time" metrics so users understand the tool's contribution

-----------|---------|----------|
| Fabricating experimental results | Violates research integrity; creates fake data that appears legitimate but has no basis in actual experiments | Use explicit placeholders like [YOUR_RESULT: Mean accuracy = ?] instead of generating plausible-looking numbers. Add warnings that placeholders must be replaced before submission. |
| Generic template overload | Produces formulaic writing that lacks domain-specific depth; all papers sound identical regardless of field or contribution | Customize templates based on research type (experimental, theoretical, review). Include field-specific writing tips. Generate domain-appropriate example text that researchers can adapt. |
| Hiding AI contribution | Creates ethical ambiguity about authorship; users may unknowingly submit AI-generated text as their own work | Add metadata footer to drafts: "Generated with rapid-manuscript-drafter v1.0.0". Mark all AI-generated sections. Include ethics statement template about tool use. |

---

## Conclusion

The rapid-manuscript-drafter skill addresses a critical bottleneck in academic publishing: the time-consuming process of transforming completed research into properly structured manuscripts. By automating the mechanical aspects of academic writing while preserving the essential human elements of scholarship, this skill enables researchers to focus on what matters most - articulating genuine insights and contributions.

The ethical foundation of this skill rests on an unwavering commitment to transparency and integrity. Unlike tools that fabricate plausible-sounding content, rapid-manuscript-drafter creates honest scaffolds that make the writing process more efficient without compromising authenticity. Every placeholder is clearly marked, every template is customizable, and every generated structure serves to guide rather than replace human expertise. This approach respects both the researcher's intellectual contribution and the academic community's standards for scholarly communication.

As research demands accelerate while publication standards remain rigorous, tools that accelerate legitimate scholarship become increasingly valuable. The rapid-manuscript-drafter skill demonstrates that speed and integrity are not opposing forces - when properly designed, automation can enhance both the efficiency and the quality of academic writing. By reducing the friction of manuscript preparation, this skill allows researchers to spend more time on the substance of their work and less time wrestling with formatting, structure, and organization.