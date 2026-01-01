# VVV RECURSIVE IMPROVEMENT PLAN
## VERILINGUA x VCL x VERIX Meta-Loop Architecture

**Created**: 2026-01-01
**Author**: Claude Opus 4.5 + User
**Status**: PLANNING
**Scope**: Three Foundry Skills + Full Context Cascade Propagation

---

## EXECUTIVE SUMMARY

This plan implements a Hofstadter strange loop at the skill level:
1. **Bootstrap Phase**: VVV-optimize the three foundry skills (prompt-architect, agent-creator, skill-forge)
2. **Dogfooding Phase**: Each skill improves itself recursively until diminishing returns
3. **Cross-Pollination Phase**: Skills improve each other in a meta-loop
4. **Propagation Phase**: Apply optimized skills to rewrite all 660+ Context Cascade components
5. **Data Collection**: Gather telemetry for two optimization levels:
   - **Low-level**: DSPy prompt optimization (14D parameter space)
   - **High-level**: VVV language creolization (evolving the language structure itself)

---

## ARCHITECTURE: THE STRANGE LOOP

```
                    +---------------------------+
                    |    VVV LANGUAGE LEVEL     |
                    |   (Creolization Data)     |
                    +-------------+-------------+
                                  |
                    +-------------v-------------+
                    |   SKILL-FORGE (v3.2.0)    |<----+
                    |   Meta-skill for skills   |     |
                    +-------------+-------------+     |
                                  |                   |
          +-----------------------+-----------------------+
          |                                               |
+---------v---------+                         +-----------v---------+
| PROMPT-ARCHITECT  |<----------------------->|    AGENT-CREATOR    |
|   (v3.1.1)        |   Cross-Improvement     |      (v3.2.0)       |
+---------+---------+                         +-----------+---------+
          |                                               |
          +-------------------+---------------------------+
                              |
                    +---------v---------+
                    |    DSPy LEVEL     |
                    | (Prompt Telemetry)|
                    +-------------------+
```

---

## PHASE 0: EVALUATION FRAMEWORK (FREE TOOLS)

### 0.1 Primary Eval Stack (Zero Cost)

| Tool | Purpose | Setup |
|------|---------|-------|
| **DeepEval** | Pytest-like LLM unit testing | pip install deepeval |
| **Promptfoo** | Security + RAG eval | npm install -g promptfoo |
| **Claude-as-Judge** | LLM grading (self-eval) | Use existing Anthropic API |
| **GitHub Actions** | CI/CD eval pipeline | Already configured |
| **LangSmith Free** | 5K traces/month | Free tier |

### 0.2 Evaluation Metrics

```python
EVAL_DIMENSIONS = {
    # Prompt-Architect specific
    "intent_extraction_accuracy": "Did PA correctly identify user intent?",
    "constraint_identification": "Were all constraints captured?",
    "optimization_quality": "Did the optimized prompt perform better?",

    # Agent-Creator specific
    "registry_compliance": "Is agent in AGENT_REGISTRY?",
    "yaml_validity": "Does frontmatter parse correctly?",
    "vcl_7slot_coverage": "Are all 7 VCL slots documented?",

    # Skill-Forge specific
    "structure_completeness": "All required dirs present?",
    "adversarial_resistance": "Survives edge case testing?",
    "cov_validation_pass": "Passes Chain-of-Verification?",

    # Cross-cutting VVV metrics
    "verix_grounding_ratio": "% claims with [ground:*]",
    "confidence_ceiling_compliance": "No conf > EVD ceiling?",
    "l2_output_purity": "No VCL markers in user output?",
    "epistemic_cosplay_detection": "Caught overconfident claims?"
}
```

### 0.3 Task Corpus Design

**Prompt-Architect Corpus (50 tasks)**
- PA-001 to PA-010: Intent extraction (easy)
- PA-011 to PA-030: Prompt optimization (medium)
- PA-031 to PA-050: Anti-pattern detection (hard)

**Agent-Creator Corpus (50 tasks)**
- AC-001 to AC-015: Agent definition (easy)
- AC-016 to AC-035: Registry validation (medium)
- AC-036 to AC-050: VCL 7-slot compliance (hard)

**Skill-Forge Corpus (50 tasks)**
- SF-001 to SF-015: Skill structure (easy)
- SF-016 to SF-035: Adversarial testing (medium)
- SF-036 to SF-050: COV protocol validation (hard)

---

## PHASE 1: PROMPT-ARCHITECT VVV OPTIMIZATION

### 1.1 Current State

| Metric | Current | Target |
|--------|---------|--------|
| VCL 7-Slot Coverage | 100% | 100% |
| VERIX Grounding | ~80% | 95% |
| L2 Output Purity | 95% | 100% |
| Turkish/Russian Creole | Present | Enhanced |

### 1.2 Dogfooding Loop

```
LOOP until diminishing_returns:
    1. prompt_architect.optimize(prompt_architect.SKILL.md)
    2. Run eval corpus (PA-001 to PA-050)
    3. Collect DSPy telemetry
    4. Collect creolization telemetry
    5. Apply improvements
    6. Check delta < 2%? -> break
```

### 1.3 Telemetry Collection Points

- Frame activation frequency
- Strictness level effectiveness
- Token efficiency per task type
- Missing Turkish/Russian markers

---

## PHASE 2: AGENT-CREATOR VVV OPTIMIZATION

### 2.1 Apply VVV Prompt-Architect

Use the now-optimized prompt-architect to improve agent-creator.

### 2.2 Cross-Improvement Loop

```
LOOP until diminishing_returns:
    1. agent_creator.improve(agent_creator)
    2. agent_creator.improve_agents_in(prompt_architect)
    3. prompt_architect.optimize(agent_creator)
    4. Check delta < 2%? -> break
```

---

## PHASE 3: SKILL-FORGE VVV OPTIMIZATION

### 3.1 Triple Skill Loop

```
LOOP until diminishing_returns:
    1. skill_forge.improve(skill_forge)
    2. skill_forge.improve(prompt_architect)
    3. skill_forge.improve(agent_creator)
    4. prompt_architect.optimize(skill_forge)
    5. agent_creator.improve_agents(skill_forge)
    6. Check all deltas < 2%? -> break
```

### 3.2 Data Collection Checkpoint

At this point collect:
- DSPy Level: Optimal frame configurations
- Creolization Level: Language gaps identified

---

## PHASE 4: PROPAGATION TO CONTEXT CASCADE

### 4.1 Order of Operations

1. **Commands** (245): prompt_architect.optimize(each)
2. **Agents** (217): prompt_architect + agent_creator(each)
3. **Skills** (226): prompt_architect + skill_forge(each)
4. **Playbooks** (7): skill_forge.optimize_high_level(each)

### 4.2 Batch Processing

Process in batches of 20-50 components with eval checkpoints.

---

## PHASE 5: OPTIMIZATION APPLICATION

### 5.1 DSPy Level Updates

Apply collected telemetry to:
- CALIBRATION.md coefficients
- two_stage_optimizer.py parameters
- Named mode configurations

### 5.2 Creolization Protocol Updates

Based on gaps identified:
- New Turkish evidential markers
- Russian aspect refinements
- Arabic root expansions
- Chinese classifier additions

---

## SUCCESS CRITERIA

| Phase | Criteria | Threshold |
|-------|----------|-----------|
| Phase 1 | PA eval score | >= 0.90 |
| Phase 2 | AC eval score | >= 0.90 |
| Phase 3 | Cross-improvement delta | < 2% |
| Phase 4 | All components VVV-compliant | 100% |
| Phase 5 | DSPy calibration with real data | Done |

---

## FREE EVALUATION TOOLS DETAIL

### DeepEval (Primary)

```bash
pip install deepeval
```

Features:
- Pytest-like syntax for LLM tests
- Built-in LLM-as-judge scoring
- Hallucination detection
- Custom metrics support

### Promptfoo (Security)

```bash
npm install -g promptfoo
```

Features:
- Red team testing
- OWASP compliance
- RAG evaluation

### GitHub Actions CI

Already configured in .github/workflows/cognitive-tests.yml
Add vvv-eval.yml for recursive improvement eval.

### LangSmith Free Tier

- 5,000 traces/month
- Automatic LLM call tracing
- Dataset-based evaluation

---

## TELEMETRY SCHEMA

```json
{
  "execution_id": "uuid",
  "timestamp": "ISO8601",
  "skill": "prompt-architect|agent-creator|skill-forge",
  "phase": "dogfood|cross-improve|propagate",
  "dspy_telemetry": {
    "frames_activated": ["evidential", "aspectual"],
    "strictness_level": 0.8,
    "token_count": 1234,
    "accuracy_score": 0.91,
    "efficiency_score": 0.87
  },
  "creolization_telemetry": {
    "markers_used": ["EVD:-DI", "ASP:sov."],
    "missing_markers": [],
    "l2_purity_score": 1.0,
    "cosplay_detected": false
  },
  "improvement_delta": 0.03
}
```

---

## PREREQUISITE INFRASTRUCTURE (From REMEDIATION-PLAN)

These items from the cognitive architecture remediation must be completed
before or during the VVV loop to provide proper infrastructure.

### High Priority (Blocking VVV Loop)

| ID | Item | Status | Integrated Into |
|----|------|--------|-----------------|
| 4.1 | Real Evaluator | PENDING | Phase 0 (task corpus IS the real evaluator) |

### Medium Priority (Improves Quality)

| ID | Item | Status | Integrated Into |
|----|------|--------|-----------------|
| 3.2 | Agent template YAML anchor | PENDING | Phase 2 (agent-creator optimization) |
| 3.3 | Storage deduplication | PENDING | Phase 5 (cleanup after propagation) |
| 5.4 | Error handling tests | PENDING | Phase 0 (eval framework) |

### Low Priority (Final Polish)

| ID | Item | Status | Integrated Into |
|----|------|--------|-----------------|
| 6 | Final audit | PENDING | After Phase 5 complete |

### HOFSTADTER-SPEC P2-P3 (DSPy/PyMOO Advanced)

These advanced Hofstadter features can be implemented during or after the VVV loop.

| Priority | Item | Target | Integrated Into |
|----------|------|--------|-----------------|
| P2 | Self-mod objective | PyMOO | Phase 5 (optimization application) |
| P2 | Thrashing detection | PyMOO | Phase 5 (detect optimization loops) |
| P3 | Self-ref signatures | DSPy | Phase 3 (skill-forge meta-skill) |
| P3 | Homoiconic sigs | DSPy | Phase 3 (signature manipulation) |
| P3 | Hofstadter optimizer | DSPy | Phase 5 (base case detection) |

### Integration Notes

1. **Real Evaluator (4.1)**: The 150-task corpus in Phase 0 IS the real evaluator.
   No separate implementation needed - the VVV loop uses real LLM execution.

2. **Agent Template (3.2)**: Implement during Phase 2 when optimizing agent-creator.
   The YAML anchor template reduces redundancy across 217 agents.

3. **Storage Deduplication (3.3)**: Implement in Phase 5 after propagation.
   Delta-based storage for cascade results.

4. **Self-mod Objective (P2)**: Add to PyMOO during Phase 5.
   Weight: 20% of optimization objectives.

5. **Hofstadter Optimizer (P3)**: Implement base case detection for DSPy.
   Prevents infinite recursion in skill self-improvement.

---

## NEXT STEPS

### Immediate (Before VVV Loop)
1. [ ] Create task corpus files (150 total tasks) - BECOMES Real Evaluator
2. [ ] Set up DeepEval test structure
3. [ ] Create vvv-eval.yml GitHub Action
4. [ ] Add error handling tests (5.4)

### Phase 1-3 (During VVV Loop)
5. [ ] Begin Phase 1: prompt-architect dogfooding
6. [ ] Implement agent template YAML anchor (3.2) in Phase 2
7. [ ] Implement self-ref signatures (P3) in Phase 3
8. [ ] Document creolization gaps as they arise

### Phase 5 (After VVV Loop)
9. [ ] Add self-mod objective to PyMOO (P2)
10. [ ] Add thrashing detection (P2)
11. [ ] Implement Hofstadter optimizer (P3)
12. [ ] Implement storage deduplication (3.3)
13. [ ] Run final audit (Phase 6)

---

## CONSOLIDATED CHECKLIST

All items from REMEDIATION-PLAN + HOFSTADTER-SPEC + VVV-PLAN:

### Infrastructure
- [x] CALIBRATION.md (commit 95ad023)
- [x] CI workflow (commit 460fe0d)
- [x] CI fix: Add PyYAML dependency (missing `yaml` module)
- [ ] Task corpus (150 tasks)
- [ ] DeepEval setup
- [ ] Error handling tests

### VVV Optimization
- [ ] Phase 1: prompt-architect
- [ ] Phase 2: agent-creator + YAML anchor
- [ ] Phase 3: skill-forge + cross-improvement
- [ ] Phase 4: propagate to 660+ components
- [ ] Phase 5: apply optimizations

### Advanced Hofstadter
- [ ] P2: Self-mod objective
- [ ] P2: Thrashing detection
- [ ] P3: Self-ref signatures
- [ ] P3: Homoiconic sigs
- [ ] P3: Hofstadter optimizer

### Final
- [ ] Storage deduplication
- [ ] Final audit

---

*Plan Version: 1.1*
*Last Updated: 2026-01-01*
*Incorporates: REMEDIATION-PLAN.md, HOFSTADTER-SPEC.md*
