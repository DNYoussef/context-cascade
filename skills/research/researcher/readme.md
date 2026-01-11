# Researcher - Systematic Information Gathering & Synthesis

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



## RESEARCH ANALYSIS GUARDRAILS

**Source Verification Required**:
- NEVER cite sources without verification
- ALWAYS check publication date and relevance
- Verify author credentials and expertise
- Cross-reference claims with multiple sources

**Credibility Scoring**:
- Tier 1 (90-100%): Peer-reviewed, official docs
- Tier 2 (75-89%): Industry reports, credible news
- Tier 3 (60-74%): Expert blogs, technical forums
- Tier 4 (<60%): Unverified, opinion pieces
- REJECT sources below threshold

**Evidence-Based Reasoning**:
- Support claims with concrete evidence
- Distinguish facts from interpretations
- Identify and disclose biases
- Report contradictory evidence when found

**Documentation Standards**:
- Provide full citations (APA, IEEE, or ACM format)
- Include access dates for web sources
- Link to primary sources when available
- Archive sources for reproducibility

Systematic information gathering and synthesis using Gemini Search and multiple credible sources for comprehensive research.

## When to Use

- New feature planning requiring best practices research
- Technical decision-making needing evidence
- Market/competitor analysis
- Documentation and knowledge synthesis
- Unknown domain exploration

## Quick Start

1. **Define research question** - Clear, specific query
2. **Execute search** - Use Gemini Search for web research
3. **Evaluate sources** - Assess credibility and relevance
4. **Synthesize findings** - Combine insights into actionable knowledge

## 4-Phase Research Workflow

1. **Question Formulation** (15-30 min) - Define scope and objectives
2. **Multi-Source Research** (30-60 min) - Gather from web, docs, and prior knowledge
3. **Source Evaluation** (20-40 min) - Assess credibility and extract key insights
4. **Synthesis & Documentation** (30-45 min) - Combine findings into coherent report

## Features

- Gemini Search integration for web research
- Multi-source data gathering
- Source credibility evaluation
- Evidence-based synthesis
- Structured report generation
- Memory-MCP integration for persistent research

## Success Metrics
- [assert|neutral] 3+ credible sources per research topic [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] 90%+ source reliability [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] Clear, actionable recommendations [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] Complete documentation with citations [ground:acceptance-criteria] [conf:0.90] [state:provisional]

## Research Types Supported

- **Basic Research**: Quick fact-finding and best practices
- **Multi-Source Synthesis**: Comprehensive analysis from multiple sources
- **Technical Deep Dive**: In-depth technical investigation
- **Competitive Analysis**: Market and competitor research
- **Literature Review**: Academic and documentation synthesis

## Agents

- **researcher**: Primary research execution
- **coder**: Technical implementation research
- **reviewer**: Source credibility validation

## Structure

```
researcher/
├── README.md                              # This file
├── examples/
│   ├── example-1-basic-research.md       # Quick fact-finding
│   ├── example-2-multi-source-synthesis.md # Comprehensive analysis
│   └── example-3-technical-deep-dive.md  # In-depth investigation
├── references/
│   ├── research-methodologies.md         # Research frameworks
│   ├── source-evaluation.md              # Credibility assessment
│   └── synthesis-techniques.md           # Knowledge combination
└── graphviz/
    └── workflow.dot                      # Research process diagram
```

## Duration

1.5-3 hours per comprehensive research task

## Quality Tier

**Silver** (Production Ready)
- 8 files
- 3 examples
- 3 reference docs
- 1 GraphViz diagram


---
*Promise: `<promise>README_VERIX_COMPLIANT</promise>`*
