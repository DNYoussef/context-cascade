# HOFSTADTER AXIOM IMPROVEMENTS - SPECIFICATION

[assert|neutral] This SPEC.md defines requirements for implementing Hofstadter axiom improvements [ground:improvement-spec] [conf:0.95] [state:confirmed]

---

## Overview

Apply insights from Hofstadter's Metamagical Themas to improve the cognitive architecture:
- VERILINGUA (7 cognitive frames)
- VERIX (epistemic notation)
- GlobalMOO/PyMOO (multi-objective optimization)
- DSPy (signature optimization)

**Source**: METAMAGICAL_AXIOM_SYNTHESIS.yaml (9 files, 3 models, 55 axioms)

---

## Requirements

### Functional Requirements

#### FR1: VERILINGUA Improvements

1. **FR1.1**: Add `meta_instruction()` method to all 7 frames for self-reference mode
   - Enable frames to discuss themselves (mention mode vs use mode)
   - Markers: `[mentioning:frame]` vs `[using:frame]`

2. **FR1.2**: Add recursion depth limits to frame nesting
   - `max_frame_depth: 3` (configurable)
   - `frame_step_policy: "simpler"` - nested frames must be "lighter"
   - Add `validate_nesting()` method to FrameworkConfig

3. **FR1.3**: Add thrashing prevention heuristics
   - `get_active_fast()` method using keyword triggers (first 500 chars)
   - Fallback to evidential frame if no triggers match
   - Avoid O(n) frame evaluation on every prompt

4. **FR1.4**: Document two-tier architecture explicitly
   - TIER 1: IMMUTABLE (7 frame definitions)
   - TIER 2: MUTABLE (activation weights, scoring)

#### FR2: VERIX Improvements

1. **FR2.1**: Add optional `[agent:X]` prefix to VERIX grammar
   - Values: model, user, system, doc, process
   - Disambiguate "who" makes each claim

2. **FR2.2**: Add recursive claim validation
   - `validate_nested_claim()` function
   - MAX_DEPTH = 3
   - Confidence must decrease toward base case

3. **FR2.3**: Add meta-level markers
   - Level 1: (no prefix) - claims about world
   - Level 2: `[meta]` - claims about claims
   - Level 3: `[meta:verix]` - claims about VERIX itself

#### FR3: GlobalMOO/PyMOO Improvements

1. **FR3.1**: Add two-tier optimization bounds
   - IMMUTABLE_BOUNDS: evidential >= 0.3, require_ground >= 0.5
   - MUTABLE_BOUNDS: other parameters 0.0-1.0
   - Add `constrain_suggestion()` method

2. **FR3.2**: Add self-modification objective
   - New objective: `self_modification_potential`
   - Weight: 20% of total objectives

3. **FR3.3**: Add thrashing detection and recovery
   - `detect_optimization_thrashing()` function
   - `handle_thrashing()` with population diversification

#### FR4: DSPy Improvements

1. **FR4.1**: Add self-referential signatures
   - `MetaVerilinguaSignature` with introspect mode
   - Signatures can describe themselves

2. **FR4.2**: Add Hofstadter-aware optimizer
   - `HofstadterOptimizer` with base case detection
   - Step-toward-simpler logic

3. **FR4.3**: Add homoiconic signature manipulation
   - `signature_to_dict()` and `dict_to_signature()`
   - `mutate_signature()` for runtime modification

---

### Non-Functional Requirements

#### NFR1: Performance
- Thrashing prevention must reduce frame selection time by >= 50%
- New validation functions must complete in < 10ms
- No regression in existing optimization performance

#### NFR2: Compatibility
- All changes must be backwards-compatible
- Existing VERILINGUA/VERIX usage must continue to work
- No breaking changes to GlobalMOO API integration

#### NFR3: Testability
- All new functions must have unit tests
- Coverage >= 80% for new code
- Integration tests for cross-system changes

#### NFR4: Documentation
- All new markers/methods documented in guides
- Examples for each new capability
- Architecture diagrams updated

---

## Constraints

### Technical Constraints
- **Language**: Python 3.10+
- **Framework**: Existing cognitive-architecture structure
- **Dependencies**: No new external dependencies for core features
- **DSPy**: Requires dspy-ai >= 2.0

### Timeline Constraints
- P0 improvements: Within current sprint
- P1 improvements: Within 2 sprints
- P2/P3 improvements: Backlog

### Resource Constraints
- Single developer implementation
- No cloud infrastructure changes required
- Existing GlobalMOO subscription limits apply

---

## Success Criteria

### SC1: Functionality
- [x] All 7 frames have `meta_instruction()` method
- [x] Frame nesting validated with depth limits
- [x] VERIX agent markers functional
- [x] Optimization bounds enforced
- [x] Thrashing detection operational

### SC2: Quality
- [x] All tests pass (existing + new)
- [x] No critical/high severity issues in code review
- [x] Documentation complete for all features

### SC3: Performance
- [x] Frame selection time reduced by >= 50%
- [x] No performance regression in optimization
- [x] Validation overhead < 10ms per call

### SC4: Integration
- [x] Three-Loop system continues functioning
- [x] Memory-MCP integration preserved
- [x] Existing skills/agents unaffected

---

## Out of Scope

- Changing the 7 frame definitions (IMMUTABLE tier)
- Modifying VERIX core grammar (only adding optional prefix)
- Cloud infrastructure changes
- New external API integrations
- UI/frontend changes

---

## Risk Summary (Pre-Analysis)

| Risk | Severity | Probability | Notes |
|------|----------|-------------|-------|
| Breaking existing VERILINGUA usage | High | Medium | Backwards-compat required |
| DSPy version incompatibility | Medium | Medium | Homoiconic may need 2.0+ |
| Optimization performance regression | High | Low | Thrashing detection adds overhead |
| Complexity creep in VERIX | Medium | Medium | Agent markers add complexity |
| Windows compatibility issues | Medium | Low | No new native deps |

---

## Implementation Priority

| Priority | Item | Target | Complexity | Impact |
|----------|------|--------|------------|--------|
| P0 | Agent identity markers | VERIX | Low | High |
| P0 | Frame self-reference mode | VERILINGUA | Low | Medium |
| P1 | Thrashing prevention | VERILINGUA | Medium | High |
| P1 | Two-tier bounds | GlobalMOO | Low | Medium |
| P1 | Recursion limits | VERIX | Medium | Medium |
| P2 | Meta-VERIX levels | VERIX | Medium | Medium |
| P2 | Self-mod objective | PyMOO | Medium | High |
| P2 | Thrashing detection | PyMOO | Medium | Medium |
| P3 | Self-ref signatures | DSPy | High | Medium |
| P3 | Homoiconic sigs | DSPy | High | High |
| P3 | Hofstadter optimizer | DSPy | High | High |

---

*[commit|neutral] This specification captures all Hofstadter axiom improvements [ground:improvement-spec] [conf:0.95] [state:confirmed]*
