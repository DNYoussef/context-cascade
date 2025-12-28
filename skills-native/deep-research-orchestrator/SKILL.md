---
name: deep-research-orchestrator
description: Meta-orchestrator for complete Deep Research SOP lifecycle managing 3 phases, 9 pipelines (A-I), and 3 quality gates. Use when starting new research projects, conducting systematic ML research, or ensuring rigorous scientific methodology from literature review through production deployment. Coordinates all SOP skills and agents for end-to-end research execution.
---

## SKILL-SPECIFIC GUIDANCE

### When to Use This Skill
- Complete research lifecycle from literature review to production (Pipelines A-I)
- Multi-month academic projects requiring 3 quality gates
- NeurIPS/ICML/CVPR submissions with reproducibility requirements
- Research requiring systematic methodology (PRISMA, ACM badging)
- Coordinating 9 pipelines with 15+ specialized agents

### When NOT to Use This Skill
- Quick investigations (<1 week, use researcher skill)
- Single-pipeline workflows (use specific skills)
- Industry projects without academic rigor
- Prototyping without publication goals

### Success Criteria
- All 3 Quality Gates passed (Foundations, Development, Production)
- Minimum 50 papers reviewed (Pipeline A)
- Baseline replicated within +/- 1% (Pipeline D)
- Novel method validated (p < 0.05, d >= 0.5)
- Holistic evaluation across 6+ dimensions
- Reproducibility package tested in fresh environments
- Ethics review completed (data bias audit, fairness metrics)

### Edge Cases & Limitations
- Gate 1 failure: incomplete literature review, missing SOTA benchmarks
- Gate 2 failure: insufficient ablations, statistical power too low
- Gate 3 failure: production infrastructure not validated, monitoring gaps
- Multi-modal data: expand holistic evaluation to modality-specific metrics
- Limited compute: prioritize smaller ablation sets, document constraints

### Critical Guardrails
- NEVER skip Quality Gates (use gate-validation for rigorous checks)
- ALWAYS document full pipeline execution (A through I, no shortcuts)
- NEVER claim production readiness without Gate 3 validation
- ALWAYS coordinate ethics review (ethics-agent) before Gate 1
- NEVER bypass reproducibility requirements (archivist agent mandatory)

### Evidence-Based Validation
- Validate Gate 1: verify 50+ papers, SOTA benchmarks, research gaps
- Validate Gate 2: confirm 5+ ablations, p < 0.05, effect size d >= 0.5
- Validate Gate 3: test production deployment, monitoring, rollback strategies
- Cross-validate pipelines: ensure Pipeline D baseline feeds into Pipeline E
- Verify agent coordination: check memory-mcp state, confirm handoffs logged



# Deep Research Orchestrator

Master orchestration skill for the complete Deep Research Standard Operating Procedure (SOP), managing the entire research lifecycle from ideation through production deployment with rigorous quality gates.

## Kanitsal Cerceve Aktivasyonu (Evidential Frame)

Bu arastirma gorevi icin her iddia kaynaklandirilmalidir:

**Kaynak Turleri:**
- **DOGRUDAN (-DI)**: Birincil kaynak, dogrudan inceleme
- **CIKARIM (-mIs)**: Ikincil analiz, cikarim yapildi
- **BILDIRILEN (-mIs)**: Ucuncu taraf bildirimi

**English Application:**
- **[DIRECT]**: Primary source, directly examined
- **[INFERRED]**: Secondary analysis, derived conclusion
- **[REPORTED]**: Third-party report or citation

**Usage in Research Pipelines:**
Every deliverable must include evidential markers indicating the source type and confidence level.

Example:
```
Literature Review Finding [DIRECT, confidence: 95%]:
- Baseline accuracy: 94.2% (source: original paper Table 3, directly replicated)

Hypothesis [INFERRED, confidence: 78%]:
- Multi-scale attention may improve performance (derived from 5 papers showing similar patterns)

Related Work [REPORTED, confidence: 90%]:
- Vision Transformers achieve SOTA (cited from Dosovitskiy et al. 2021, not replicated)
```

## Al-Itar al-Sarfi (Morphological Frame)

Hadhihi al-mahimma tatatallab tahlil al-judur:

**Concept Decomposition:**
- **ROOT**: Core research question (undivisible atomic concept)
- **DERIVED**: Sub-questions from decomposition (morphological transformations)
- **COMPOSED**: Synthesized findings from multiple roots (compound concepts)

**English Application:**

Research questions follow morphological decomposition:

**ROOT**: "How does multi-scale attention improve vision transformers?"

**DERIVED** (decomposition):
1. What is multi-scale attention? (definition root)
2. How do vision transformers work? (mechanism root)
3. What metrics define improvement? (evaluation root)
4. What baselines exist? (comparison root)

**COMPOSED** (synthesis):
- Multi-scale attention + vision transformers + evaluation metrics = testable hypothesis
- Baseline performance + novel method + statistical validation = publishable contribution

**Usage in Pipelines:**
- **Pipeline A (Literature)**: Decompose research question into ROOT concepts
- **Pipeline D (Baseline)**: Verify ROOT assumptions with [DIRECT] evidence
- **Pipeline E (Holistic Eval)**: Synthesize COMPOSED metrics across dimensions

## Overview

**Purpose**: Orchestrate complete research lifecycle following Deep Research SOP methodology

**When to Use**:
- Starting new machine learning research projects
- Conducting systematic scientific research with reproducibility requirements
- Academic paper submission with artifact evaluation
- Production ML deployment requiring ethics, fairness, and safety validation
- Research requiring regulatory compliance (FDA, EU AI Act)
- Multi-month research projects with team coordination

**Quality Gates**: Manages ALL 3 quality gates (Data & Methods, Model & Evaluation, Production & Artifacts)

**Prerequisites**:
- Research question formulated
- Resources allocated (compute, datasets, team)
- Institutional approvals (IRB if needed)
- Memory MCP configured for cross-session persistence

**Outputs**:
- Complete research artifact package
- Published paper with reproducibility artifacts
- Production-ready model with ethics validation
- All quality gate checklists (3 gates APPROVED)
- Comprehensive documentation (datasheets, model cards, method cards)
- DOI-assigned artifacts (Zenodo, HuggingFace)

**Time Estimate**: 2-6 months (full research lifecycle)
- Phase 1 (Foundations): 2-4 weeks
- Phase 2 (Development): 6-12 weeks
- Phase 3 (Production): 2-4 weeks

**Skills Orchestrated**: baseline-replication, method-development, holistic-evaluation, literature-synthesis, reproducibility-audit, deployment-readiness, research-publication, gate-validation

**Agents Used**: ALL 4 P0 agents (data-steward, ethics-agent, archivist, evaluator) + system-architect, coder, tester, reviewer, researcher



## Detailed Instructions

### PHASE 1: FOUNDATIONS (2-4 weeks)

#### Pipeline A: Literature Synthesis
**Objective**: Systematic literature review identifying SOTA methods, gaps, opportunities

**Execution**:
```bash
claude-code invoke-skill literature-synthesis \
  --query "vision transformers attention mechanisms" \
  --databases "arxiv,semantic-scholar,papers-with-code" \
  --output phase1-foundations/literature/
```

**Deliverables**:
- Literature review document (50-100 papers) **[REPORTED, confidence: varies per paper]**
- SOTA performance benchmarks **[DIRECT if replicated, REPORTED if cited]**
- Research gap analysis **[INFERRED from literature patterns]**
- Hypothesis formulation **[COMPOSED from ROOT + DERIVED concepts]**

**Evidential Requirements**:
- Each paper tagged with [DIRECT|REPORTED] based on whether code/results were verified
- Confidence levels for each claim (90%+ for DIRECT, 70-90% for REPORTED, 60-80% for INFERRED)

**Morphological Decomposition**:
- ROOT question decomposed into 3-5 atomic sub-questions
- DERIVED concepts mapped to literature sources
- COMPOSED hypothesis shows clear lineage from decomposition

**Agent**: researcher



#### Pipeline C: PRISMA Protocol (if systematic review)
**Objective**: PRISMA-compliant systematic literature review

**Execution**:
```bash
npx claude-flow@alpha sparc run researcher \
  "/prisma-init --topic 'attention mechanisms in vision transformers'"
```

**Deliverables**:
- PRISMA protocol document
- Search strategy
- Inclusion/exclusion criteria
- Quality assessment framework

**Agent**: researcher



#### Quality Gate 1 Validation
**Objective**: GO/NO-GO decision for method development

**Execution**:
```bash
claude-code invoke-skill gate-validation --gate 1
```

**Gate 1 Requirements** (with Evidential Markers):
- [ ] Literature review complete (≥50 papers) **[REPORTED, avg confidence: ≥80%]**
- [ ] Datasheet complete (Form F-P1, ≥90% filled) **[DIRECT, confidence: 100%]**
- [ ] Ethics review APPROVED (data-steward + ethics-agent) **[INFERRED risk assessment ≥85% confidence]**
- [ ] Baseline replication ±1% tolerance **[DIRECT, confidence: ≥95%]**
- [ ] Reproducibility package tested (3/3 runs successful) **[DIRECT, confidence: 100%]**
- [ ] Dataset validated (bias audit complete) **[DIRECT, confidence: ≥90%]**

**Evidence Chain for Gate Decision**:
1. Collect all [DIRECT] measurements from Phase 1 pipelines
2. Aggregate [REPORTED] confidence from literature (weighted by paper quality)
3. Synthesize [INFERRED] risk assessments from ethics review
4. Compute overall confidence: weighted average of 6 requirements
5. **Gate 1 approval threshold**: ≥90% overall confidence

**Decision Criteria**:
- **APPROVED** (≥90% confidence): Proceed to Phase 2 (Method Development)
- **CONDITIONAL** (80-89% confidence): Minor fixes required, proceed with restrictions
- **REJECTED** (<80% confidence): Critical issues, return to Phase 1

**Confidence Decomposition**:
- ROOT requirements: Datasheet, baseline, reproducibility (must be [DIRECT] ≥95%)
- DERIVED requirements: Literature, bias audit (can be [REPORTED] ≥80%)
- COMPOSED decision: Overall confidence synthesis

**Agent**: evaluator



#### Pipeline E: Holistic Evaluation
**Objective**: Comprehensive evaluation across 6+ dimensions

**Execution**:
```bash
claude-code invoke-skill holistic-evaluation \
  --model phase2-development/novel-method/checkpoint.pth \
  --dimensions "accuracy,fairness,robustness,efficiency,interpretability,safety"
```

**Deliverables**:
- Holistic evaluation report **[COMPOSED from 6 DIRECT measurement pipelines]**
- Fairness metrics (demographic parity, equalized odds) **[DIRECT, confidence: 90%]**
- Robustness analysis (adversarial, OOD) **[DIRECT, confidence: 85%]**
- Efficiency profiling (latency, memory, energy) **[DIRECT, confidence: 95%]**
- Interpretability analysis (SHAP, attention viz) **[INFERRED from model internals, confidence: 75%]**
- Safety evaluation (harmful outputs, bias, privacy) **[DIRECT measurements + INFERRED risk assessment]**

**Evidence Chain for Each Dimension**:
1. **Accuracy** [DIRECT]: Test set performance, error bars
2. **Fairness** [DIRECT]: Measured across demographic groups
3. **Robustness** [DIRECT]: Adversarial attack success rate, OOD performance
4. **Efficiency** [DIRECT]: Profiled latency/memory/energy
5. **Interpretability** [INFERRED]: Feature importance, attention patterns (cannot directly measure understanding)
6. **Safety** [COMPOSED]: Bias audit [DIRECT] + risk assessment [INFERRED]

**Confidence Aggregation**:
- Overall holistic evaluation confidence = weighted average of 6 dimensions
- Minimum 80% confidence required for Gate 2 approval

**Agents**: tester, ethics-agent



#### Quality Gate 2 Validation
**Objective**: GO/NO-GO decision for production deployment

**Execution**:
```bash
claude-code invoke-skill gate-validation --gate 2
```

**Gate 2 Requirements** (with Evidential Markers):
- [ ] Novel method outperforms baseline (statistically significant) **[DIRECT, p < 0.05, d ≥ 0.5, confidence: ≥95%]**
- [ ] Ablation studies complete (≥5 components) **[DIRECT, each with error bars, confidence: ≥90%]**
- [ ] Holistic evaluation complete (6+ dimensions) **[COMPOSED from 6 DIRECT pipelines, avg confidence: ≥85%]**
- [ ] Ethics review APPROVED (ethics-agent) **[INFERRED risk assessment, confidence: ≥85%]**
- [ ] Method card complete (≥90% filled) **[COMPOSED documentation, confidence: 100%]**
- [ ] Reproducibility tested (3/3 runs successful) **[DIRECT, confidence: 100%]**

**Evidence Chain for Gate 2**:
1. Performance improvement [DIRECT]: t-test p-value < 0.05, Cohen's d ≥ 0.5
2. Ablation validity [DIRECT]: Each component tested with 3+ runs, error bars computed
3. Holistic evaluation [COMPOSED]: 6 dimensions measured → weighted average confidence
4. Ethics approval [INFERRED]: Risk assessment based on fairness metrics [DIRECT] + safety evaluation [INFERRED]
5. Reproducibility [DIRECT]: 3/3 fresh runs within ±1% variance

**Decision Criteria**:
- **APPROVED** (≥90% confidence): Proceed to Phase 3 (Production)
- **CONDITIONAL** (80-89% confidence): Mitigation plan required (e.g., fairness gaps, robustness issues)
- **REJECTED** (<80% confidence): Critical issues (performance regression, safety risks)

**Confidence Requirements by Type**:
- [DIRECT] measurements: ≥90% required (performance, ablations, reproducibility)
- [INFERRED] assessments: ≥80% required (ethics, safety)
- [COMPOSED] synthesis: ≥85% required (holistic evaluation, method card)

**Agent**: evaluator



#### Pipeline H: Deployment Readiness
**Objective**: Production deployment validation

**Execution**:
```bash
claude-code invoke-skill deployment-readiness \
  --model phase3-production/final-checkpoint.pth \
  --environment production
```

**Deliverables**:
- Deployment checklist
- Infrastructure requirements
- Monitoring plan
- Incident response plan
- Rollback strategy
- Performance benchmarks (production environment)

**Agents**: tester, archivist



#### Quality Gate 3 Validation
**Objective**: Final GO/NO-GO for production deployment and publication

**Execution**:
```bash
claude-code invoke-skill gate-validation --gate 3
```

**Gate 3 Requirements** (with Evidential Markers):
- [ ] Model card complete (≥90% filled) **[COMPOSED from Phases 1-3, confidence: 100%]**
- [ ] Reproducibility package tested (3/3 runs) **[DIRECT, confidence: 100%]**
- [ ] DOIs assigned (dataset, model, code) **[DIRECT, verified URLs, confidence: 100%]**
- [ ] Code public (GitHub release) **[DIRECT, accessible, confidence: 100%]**
- [ ] Ethics review APPROVED (deployment) **[INFERRED deployment risks, confidence: ≥85%]**
- [ ] Deployment plan validated **[DIRECT infrastructure tests, confidence: ≥90%]**
- [ ] Publication artifacts ready **[COMPOSED from all phases, confidence: 100%]**

**Evidence Chain for Gate 3**:
1. Artifact completeness [DIRECT]: All checklist items (100% verifiable)
2. Reproducibility [DIRECT]: 3/3 fresh environments, <1% variance
3. Public accessibility [DIRECT]: DOIs resolve, code clones successfully
4. Deployment readiness [DIRECT]: Infrastructure validated, monitoring tested
5. Ethics clearance [INFERRED]: Production risk assessment based on Phase 2 safety evaluation [DIRECT]
6. Publication package [COMPOSED]: All prior evidence chains synthesized

**Decision Criteria**:
- **APPROVED** (≥95% confidence): Deploy to production, submit publication
  - All [DIRECT] requirements: 100% (reproducibility, DOIs, code, deployment tests)
  - [INFERRED] ethics: ≥85%
  - [COMPOSED] artifacts: 100% completeness
- **CONDITIONAL** (90-94% confidence): Minor documentation fixes
- **REJECTED** (<90% confidence): Critical reproducibility or ethics issues

**Final Evidence Preservation**:
- Model card documents full evidence chain: ROOT question → DERIVED hypotheses → COMPOSED findings
- All [DIRECT] measurements archived with provenance (who, when, how)
- All [INFERRED] conclusions documented with reasoning + confidence
- All [REPORTED] claims linked to sources (DOIs, paper references)

**Publication Readiness Checklist**:
- [ ] Evidence chain complete (ROOT → DERIVED → COMPOSED)
- [ ] All claims tagged ([DIRECT] | [INFERRED] | [REPORTED])
- [ ] Confidence levels reported (mean ± std dev for all measurements)
- [ ] Reproducibility verified (3/3 independent runs)
- [ ] Ethics approved (≥85% confidence on deployment risks)

**Agent**: evaluator



## Agent Coordination Matrix

| Phase | Pipeline | Lead Agent | Supporting Agents |
|-------|----------|------------|-------------------|
| 1 | A (Literature) | researcher | - |
| 1 | B (Data & Ethics) | data-steward | ethics-agent |
| 1 | C (PRISMA) | researcher | - |
| 1 | D (Baseline) | coder | researcher, tester, archivist |
| 1 | Gate 1 | evaluator | ALL agents review |
| 2 | D (Method Dev) | system-architect | coder, tester, reviewer |
| 2 | E (Holistic Eval) | tester | ethics-agent |
| 2 | F (Ethics) | ethics-agent | - |
| 2 | Gate 2 | evaluator | ethics-agent reviews |
| 3 | G (Archival) | archivist | - |
| 3 | H (Deployment) | tester | archivist |
| 3 | I (Publication) | researcher | archivist |
| 3 | Gate 3 | evaluator | archivist reviews |



## Troubleshooting

### Issue: Quality Gate 1 rejected
**Symptoms**: evaluator returns REJECTED status for Gate 1
**Common Causes**:
- Baseline replication outside ±1% tolerance
- Incomplete datasheet (<90% filled)
- Ethics review flagged critical data risks
- Reproducibility tests failed

**Solutions**:
```bash
# Check Gate 1 requirements
claude-code invoke-skill gate-validation --gate 1 --verbose

# Re-run baseline replication with debugging
claude-code invoke-skill baseline-replication --debug

# Complete datasheet gaps
npx claude-flow@alpha sparc run data-steward \
  "/init-datasheet --fill-missing-sections"
```

### Issue: Quality Gate 2 rejected
**Symptoms**: Novel method fails holistic evaluation or ethics review
**Solutions**:
```bash
# Review holistic evaluation failures
claude-code invoke-skill holistic-evaluation --dimensions "fairness,safety" --verbose

# Address ethics concerns
npx claude-flow@alpha sparc run ethics-agent \
  "/assess-risks --component model --gate 2 --mitigation-plan"

# Re-run method development with improvements
claude-code invoke-skill method-development --incorporate-feedback
```

### Issue: Quality Gate 3 rejected
**Symptoms**: Reproducibility package fails or deployment validation issues
**Solutions**:
```bash
# Audit reproducibility package
claude-code invoke-skill reproducibility-audit --strict

# Fix deployment issues
claude-code invoke-skill deployment-readiness --fix-issues

# Complete model card
npx claude-flow@alpha sparc run archivist \
  "/init-model-card --complete-missing-sections"
```

### Issue: Phase transitions blocked
**Symptoms**: Cannot proceed to next phase due to pending validations
**Solutions**:
```bash
# Check all gate requirements
npx claude-flow@alpha memory retrieve --key "sop/gates/status"

# Identify blocking agents
npx claude-flow@alpha memory retrieve --key "sop/coordination/*/status"

# Resolve blocking tasks
# (Address specific agent requirements)
```



## Related Skills and Commands

### Phase 1 Skills
- `literature-synthesis` - Systematic literature review
- `baseline-replication` - Reproduce published baselines

### Phase 2 Skills
- `method-development` - Develop novel methods
- `holistic-evaluation` - Comprehensive evaluation

### Phase 3 Skills
- `reproducibility-audit` - Audit reproducibility
- `deployment-readiness` - Production deployment validation
- `research-publication` - Academic publication

### Cross-Phase Skills
- `gate-validation` - Quality gate validation (all 3 gates)

### Related Commands
- `/init-datasheet` - Create dataset documentation
- `/prisma-init` - Initialize systematic review
- `/assess-risks` - Ethics and safety assessment
- `/init-model-card` - Create model card
- `/validate-gate-{1,2,3}` - Gate validation



## Appendix

### Example Deep Research SOP Timeline

```
Week 1-2: Phase 1 Start
  - Literature synthesis (50+ papers)
  - Datasheet creation
  - Bias audit

Week 3-4: Phase 1 Complete
  - Baseline replication
  - Ethics review (Gate 1)
  - Gate 1 validation → APPROVED

Week 5-8: Phase 2 Development
  - Novel method implementation
  - Ablation studies
  - Hyperparameter optimization

Week 9-12: Phase 2 Evaluation
  - Holistic evaluation (6 dimensions)
  - Ethics review (Gate 2)
  - Gate 2 validation → APPROVED

Week 13-14: Phase 3 Archival
  - Reproducibility package creation
  - Model card, DOI assignment
  - Registry publishing

Week 15-16: Phase 3 Deployment & Publication
  - Deployment readiness validation
  - Paper writing
  - Gate 3 validation → APPROVED → DEPLOY

Total: 16 weeks (4 months) for complete research lifecycle
```

### Quality Gate Decision Matrix

| Gate | APPROVED | CONDITIONAL | REJECTED |
|------|----------|-------------|----------|
| Gate 1 | All requirements met, proceed to Phase 2 | Minor datasheet gaps, proceed with restrictions | Baseline >±1% or critical ethics issues |
| Gate 2 | All requirements met, proceed to Phase 3 | Mitigation plan for fairness/robustness gaps | Performance regression or critical safety risks |
| Gate 3 | All requirements met, DEPLOY to production | Minor documentation fixes required | Reproducibility failures or ethics violations |


## Common Anti-Patterns

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| **Gate Skipping** | Proceeding to Phase 2 without Gate 1 APPROVED leads to invalid foundations (incomplete literature review, unvalidated datasets, failed baseline replication) | NEVER bypass gate-validation skill. If Gate 1 returns CONDITIONAL/REJECTED, address deficiencies before Phase 2. Use gate-validation --verbose to identify specific gaps |
| **Single-Run Validation** | Testing reproducibility once (1/1 runs) masks non-deterministic behavior, framework bugs, or environment-specific issues | ALWAYS run 3+ reproductions in fresh Docker containers. Calculate variance (must be near-zero). Use different random seeds to validate determinism |
| **Ethics Review as Checkbox** | Treating ethics-agent as formality rather than substantive risk assessment leads to Gate 2/3 rejection for bias, fairness, or safety violations | Integrate ethics-agent at EVERY gate (data bias in Gate 1, model fairness in Gate 2, deployment safety in Gate 3). Address flagged risks with mitigation plans, not dismissals |

---

## Conclusion

The Deep Research Orchestrator is the definitive workflow for conducting rigorous, reproducible, and ethically sound machine learning research from ideation to production deployment. By enforcing 3 quality gates across 9 pipelines (A-I), this orchestrator ensures that research meets the standards required for top-tier academic publication (NeurIPS, ICML, CVPR) and production deployment.

**Cognitive Lensing Enhancement**:

This skill now integrates **evidential reasoning** (Turkish linguistic frame) and **morphological decomposition** (Arabic linguistic frame) to ensure:

1. **Evidential Tracking**: Every claim is tagged with source type ([DIRECT] | [INFERRED] | [REPORTED]) and confidence level (60-100%)
2. **Morphological Analysis**: Research questions decompose into ROOT (atomic concepts) → DERIVED (sub-questions) → COMPOSED (synthesized findings)
3. **Evidence Chains**: Full traceability from raw measurements to final conclusions
4. **Confidence Thresholds**: Gate approval requires ≥90% overall confidence from aggregated evidence

**When to Use**:

This skill is essential when research quality cannot be compromised: systematic literature reviews with 50+ papers **[REPORTED, avg confidence ≥80%]**, baseline replication within ±1% tolerance **[DIRECT, confidence ≥95%]**, holistic evaluation across 6+ dimensions **[COMPOSED from DIRECT measurements]**, and reproducibility packages tested in independent environments **[DIRECT, 3/3 runs]**. The 2-6 month timeline reflects the complexity of comprehensive research, but the result is publication-ready artifacts with ACM Artifact Evaluation badges and permanent DOIs.

Use this orchestrator when starting new ML research projects, preparing academic submissions with artifact tracks, or ensuring regulatory compliance (FDA, EU AI Act). The coordinated multi-agent approach (researcher, data-steward, ethics-agent, archivist, coder, tester, evaluator) ensures no dimension is overlooked, and the quality gate system prevents premature progression. The investment in systematic methodology yields research that not only passes peer review but advances the state of the art with **verifiable confidence** in its validity and reproducibility.

**Evidence-Based Guarantee**:
- All [DIRECT] measurements: ≥95% confidence
- All [INFERRED] conclusions: ≥80% confidence, documented reasoning
- All [REPORTED] claims: Linked to sources (DOIs), ≥70% confidence
- Overall research validity: ≥90% confidence threshold for publication approval