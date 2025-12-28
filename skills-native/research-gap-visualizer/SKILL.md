---
name: research-gap-visualizer
description: Create visual maps of research gaps from literature analysis, showing what has been studied, what is missing, and where opportunities exist. Generates gap matrices, research landscape diagrams, and opportunity maps. Use after literature synthesis to visualize the state of research and identify promising directions.
---

what has been studied, what is missing, and where opportunities exist. Generates
  gap matrices, research landscape diagrams, and opportunity maps. Use after literature
  synthesis to visualize the state of research and identify promising directions.
- research
- gaps
- visualization
- literature
- analysis
mcp_servers:
  required: [memory-mcp]
  optional: [sequential-thinking]
  auto_enable: true
--------|-------|------------|
| [Method 1] | [N] | [%] |
| [Method 2] | [N] | [%] |
```

## SOP Phase 2: Gap Matrix Generation

Create the gap matrix visualization:

### Gap Matrix Template (Markdown)

```markdown
## Research Gap Matrix: [X-Axis] vs [Y-Axis]

|           | [Y1] | [Y2] | [Y3] | [Y4] | [Y5] |
|-----------|------|------|------|------|------|
| **[X1]**  | [N]  | [N]  | GAP  | [N]  | GAP  |
| **[X2]**  | GAP  | [N]  | [N]  | GAP  | GAP  |
| **[X3]**  | [N]  | GAP  | [N]  | [N]  | GAP  |
| **[X4]**  | GAP  | GAP  | GAP  | [N]  | [N]  |

**Legend**:
- [N] = Number of papers
- GAP = No papers found (research opportunity)
- Shading: Darker = more studied

**Gap Statistics**:
- Total cells: [N]
- Studied cells: [N] ([%])
- Gap cells: [N] ([%])
```

### Gap Matrix Template (Mermaid Heatmap)

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': '#ff6b6b'}}}%%
quadrantChart
    title Research Gap Analysis
    x-axis Low Method Complexity --> High Method Complexity
    y-axis Low Application Novelty --> High Application Novelty
    quadrant-1 High opportunity
    quadrant-2 Competitive space
    quadrant-3 Low priority
    quadrant-4 Niche opportunities
    Topic A: [0.3, 0.6]
    Topic B: [0.45, 0.23]
    Topic C: [0.57, 0.69]
    Topic D: [0.78, 0.34]
    Gap Area 1: [0.15, 0.85]
    Gap Area 2: [0.85, 0.75]
```

## SOP Phase 3: Research Landscape Diagram

Visualize research density:

```mermaid
flowchart TB
    subgraph HighlyStudied["Highly Studied Areas"]
        A[Deep Learning + NLP<br/>150 papers]
        B[CNN + Image Classification<br/>200 papers]
    end

    subgraph ModeratelyStudied["Moderately Studied"]
        C[Transformers + Vision<br/>45 papers]
        D[GNN + Molecules<br/>30 papers]
    end

    subgraph UnderStudied["Under-Studied (GAPS)"]
        E[Neuro-symbolic + Robotics<br/>3 papers]
        F[Federated + Medical<br/>5 papers]
    end

    subgraph Unexplored["Unexplored (OPPORTUNITIES)"]
        G[Quantum ML + Drug Discovery<br/>0 papers]
        H[Causal + Time Series<br/>0 papers]
    end

    style HighlyStudied fill:#ff6b6b
    style ModeratelyStudied fill:#ffd93d
    style UnderStudied fill:#6bcb77
    style Unexplored fill:#4d96ff
```

## SOP Phase 4: Temporal Gap Analysis

Show research trends over time:

```markdown
## Temporal Research Landscape

### Publication Trend by Topic

```
Year    | Topic A | Topic B | Topic C | Topic D |
--|---------|---------|---------|---------|
2019    |  ***    |  **     |  *      |         |
2020    |  ****   |  ***    |  *      |         |
2021    |  *****  |  ****   |  **     |  *      |
2022    |  ****   |  *****  |  ***    |  **     |
2023    |  ***    |  ****   |  ****   |  ***    |
2024    |  **     |  ***    |  *****  |  ****   |
```

**Trend Analysis**:
- **Rising**: Topic C, Topic D (opportunity areas)
- **Stable**: Topic B (competitive but active)
- **Declining**: Topic A (may be saturated)
- **Stale**: [Topics not updated since 2021]
```

## SOP Phase 5: Opportunity Quadrant

Generate prioritized opportunity map:

```mermaid
quadrantChart
    title Research Opportunity Analysis
    x-axis Low Feasibility --> High Feasibility
    y-axis Low Impact --> High Impact
    quadrant-1 Pursue Aggressively
    quadrant-2 Strategic Investment
    quadrant-3 Deprioritize
    quadrant-4 Quick Wins
    Gap 1: [0.8, 0.9]
    Gap 2: [0.3, 0.85]
    Gap 3: [0.7, 0.4]
    Gap 4: [0.2, 0.3]
    Gap 5: [0.9, 0.6]
```

## SOP Phase 6: Gap Prioritization

Rank identified gaps by research potential:

```markdown
## Prioritized Research Gaps

### High Priority (Pursue)
1. **[Gap Description]**
   - Evidence: [Why this is a gap]
   - Opportunity Score: [0-1]
   - Feasibility: [high/medium/low]
   - Impact: [high/medium/low]
   - Suggested Approach: [Brief methodology]

### Medium Priority (Consider)
2. **[Gap Description]**
   ...

### Low Priority (Monitor)
3. **[Gap Description]**
   ...
```

## Example Execution

**Input** (from literature-synthesis output):
```yaml
literature_data:
  papers:
    - title: "Deep Learning for Drug Discovery"
      year: 2023
      methods: ["CNN", "GNN"]
      domains: ["drug_discovery", "molecular"]
    - title: "Transformers in Medical Imaging"
      year: 2024
      methods: ["Transformer", "Attention"]
      domains: ["medical_imaging", "diagnosis"]
    # ... more papers

analysis_type: gap_matrix
dimensions:
  x_axis: methods
  y_axis: domains
```

**Output**:

```markdown
## Research Gap Matrix: Methods vs Application Domains

|                | Drug Discovery | Medical Imaging | Genomics | Clinical NLP |
|----------------|----------------|-----------------|----------|--------------|
| **CNN**        | 23             | 45              | 12       | 8            |
| **GNN**        | 15             | 3               | 8        | **GAP**      |
| **Transformer**| 5              | 18              | **GAP**  | 22           |
| **Diffusion**  | **GAP**        | 7               | **GAP**  | **GAP**      |

## Identified Gaps (Ranked)

### High Priority
1. **Diffusion Models for Drug Discovery**
   - Evidence: 0 papers found; diffusion excels at generation
   - Opportunity Score: 0.92
   - Rationale: Diffusion models successful in images, untapped in molecules

2. **Graph Neural Networks for Clinical NLP**
   - Evidence: 0 papers; GNNs model document relationships
   - Opportunity Score: 0.78

### Medium Priority
3. **Transformers for Genomics**
   - Evidence: 0 papers in our corpus (may exist elsewhere)
   - Opportunity Score: 0.65
```

## Integration Points

### Receives From
- **literature-synthesis**: Paper data for gap analysis
- **baseline-replication**: Validation of gap existence

### Feeds Into
- **rapid-idea-generator**: Gap-informed ideation
- **rapid-manuscript-drafter**: Visual evidence for motivation
- **research-driven-planning**: Strategic direction

### Memory Storage

```bash
# Store gap analysis for future reference
npx claude-flow@alpha memory store \
  "gap_analysis_[topic]" \
  "[gap_data_json]" \
  --namespace "research/gaps"
```

## Success Criteria

- [ ] All dimensions extracted from literature data
- [ ] Gap matrix accurately reflects paper coverage
- [ ] Gaps prioritized by opportunity score
- [ ] Visual outputs render correctly
- [ ] Recommendations actionable and evidence-based
- [ ] Integration with manuscript writing enabled

## Feature Comparison

| Feature | Basic Tools | This Skill |
|---------|--------|------------|
| Gap identification | Basic | Multi-dimensional |
| Evidence for gaps | None | Paper counts, citations |
| Visualization | Basic diagrams | Matrix, landscape, temporal, quadrant |
| Prioritization | None | Opportunity scoring |
| Integration | Standalone | Feeds into manuscript, planning |
| Transparency | Black box | Full methodology shown |

## Core Principles

### 1. Multi-Dimensional Gap Analysis Over Linear Enumeration
Research gaps exist at the intersection of multiple dimensions (methods, domains, datasets, time). Single-axis analysis misses the combinatorial opportunities where established methods meet unexplored application areas.

**In practice:**
- Generate gap matrices with at least 2 dimensions (method x domain, technique x dataset)
- Use quadrant analysis to classify gaps by feasibility vs impact (pursue high-high areas first)
- Apply temporal filtering to identify stale research areas (not updated in 2+ years)
- Create bubble charts showing research density to reveal saturated vs unexplored regions
- Combine multiple visualizations (matrix + landscape + temporal) for comprehensive coverage

### 2. Evidence-Based Gap Identification With Quantitative Metrics
Claiming a gap exists requires proof. This skill quantifies gaps using paper counts, citation analysis, and coverage metrics rather than subjective assessments.

**In practice:**
- Calculate gap percentage (unstudied cells / total cells in matrix)
- Report exact paper counts per intersection (e.g., "GNN + Clinical NLP: 0 papers")
- Use minimum threshold filters (e.g., >5 papers = studied, <3 = gap, 0 = opportunity)
- Track confidence scores based on corpus size (1000+ papers = high confidence gaps)
- Provide source data in CSV/JSON for independent validation and reproducibility

### 3. Opportunity Scoring Beyond Gap Existence
A gap is not inherently valuable. This skill prioritizes gaps by research potential, combining novelty with feasibility and impact to guide strategic direction.

**In practice:**
- Score each gap on 3 axes: novelty (0-1), feasibility (0-1), impact (0-1)
- Calculate opportunity score as weighted combination (e.g., 0.4 * novelty + 0.3 * impact + 0.3 * feasibility)
- Rank gaps by opportunity score to create actionable priority list
- Classify as high/medium/low priority with explicit thresholds (>0.7 = high, 0.4-0.7 = medium, <0.4 = low)
- Justify prioritization with evidence (why is this gap feasible? what makes it impactful?)

-----------|---------|----------|
| Cherry-picking visualization to emphasize desired gaps | Selective axis choice or dimension filtering can make any area appear understudied; creates misleading visual "evidence" for pre-determined research direction | Use systematic dimension selection based on literature data (most common methods/domains). Generate multiple visualizations with different axes. Report both studied AND unstudied areas transparently. |
| Ignoring corpus limitations in gap claims | A gap in your analyzed papers may not be a gap in the broader literature; limited corpus leads to false gap identification | Report corpus size prominently (e.g., "Analysis based on 150 papers from 2020-2024"). Add caveat: "Gaps may exist outside analyzed corpus". Use confidence scoring based on coverage (>1000 papers = high confidence). |
| Treating all gaps as equal opportunities | Some gaps exist because they are uninteresting, infeasible, or already attempted and failed; visualization alone doesn't distinguish valuable from valueless gaps | Add feasibility and impact dimensions to opportunity scoring. Research why gap exists (technical barrier? lack of interest? ethical concerns?). Provide rationale for each high-priority gap recommendation. |

---

## Conclusion

Research gap visualization transforms the abstract concept of "what's missing" into concrete, actionable visual evidence. By mapping the research landscape across multiple dimensions, this skill reveals not only where gaps exist but also where the most promising opportunities lie. The combination of gap matrices, landscape diagrams, temporal analysis, and opportunity scoring provides researchers with a comprehensive view of the strategic research terrain.

The power of this skill lies in its ability to make gap identification systematic and evidence-based. Rather than relying on intuition or anecdotal observations about what's been studied, researchers can point to specific visualizations showing exact paper counts, coverage percentages, and prioritized recommendations. This visual evidence is particularly valuable in grant proposals and manuscript motivation sections, where demonstrating research novelty is critical for funding and publication success.

As research fields become increasingly specialized and literature volumes grow exponentially, manual gap identification becomes impractical. Systematic visualization of research coverage allows scholars to identify novel contribution opportunities efficiently, avoid redundant work, and make strategic decisions about research direction. The research gap visualizer skill represents an essential tool for modern evidence-based research planning, transforming literature synthesis from descriptive summaries into strategic roadmaps.