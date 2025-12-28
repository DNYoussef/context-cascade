# Changelog - cascade-orchestrator

## [2.1.0] - 2025-12-19

### Added - Cognitive Lensing Enhancement

**Aspectual Cognitive Frame (Russian linguistic influence)**:
- State tracking for workflow stages: SV:COMPLETED, NSV:IN_PROGRESS, BLOCKED, PARALLEL, FAILED, PENDING
- Agent state monitoring: IDLE, WORKING, WAITING, DONE, ERROR
- State transition rules and visualization
- Aspectual state report template with transition history

**Hierarchical Cognitive Frame (Japanese linguistic influence)**:
- 5-level hierarchy: WORKFLOW > PHASE > STAGE > TASK > SUBTASK
- Hierarchical dependency visualization with state annotations
- Japanese terminology integration (最上位, 重要段階, 小段階, 作業, 細分)
- Hierarchical dependency report template

**Enhanced Cascade Definition Format**:
- `state_tracking: aspectual` configuration option
- `hierarchy_tracking: enabled` configuration option
- Stage-level state tracking (`state: PENDING | IN_PROGRESS | COMPLETED | FAILED | BLOCKED | PARALLEL`)
- Stage-level hierarchy annotation (`hierarchy_level: phase | stage | task | subtask`)
- State transition configuration (`state_transitions` block)
- Agent state tracking within stages
- State history persistence (`store_state_history: true`)

**Output Templates**:
- Aspectual State Report Template (workflow state summary with transition history)
- Hierarchical Dependency Report Template (5-level hierarchy visualization)
- Combined Aspectual-Hierarchical View (integrated status dashboard)

**Documentation Updates**:
- Updated version from 2.0.0 to 2.1.0
- Added cognitive_frame YAML frontmatter with rationale
- Updated Success Criteria to reference state tracking ([SV:COMPLETED])
- Updated Edge Cases to reference state transitions ([FAILED])
- Updated Guardrails to reference aspectual tracking
- Updated Evidence-Based Validation to reference hierarchy levels

### Rationale

Workflow orchestration inherently deals with two critical concerns:

1. **State Progression** (Aspectual): Tracking whether work is complete (perfective aspect) vs ongoing (imperfective aspect) vs blocked
2. **Hierarchical Organization**: Managing nested dependencies across workflow > phase > stage > task > subtask levels

The aspectual cognitive frame (inspired by Russian verb aspects distinguishing completed vs ongoing actions) maps perfectly to workflow state management. The hierarchical cognitive frame (inspired by Japanese honorific levels) maps perfectly to nested task organization with dependency tracking.

This enhancement makes implicit state tracking and hierarchy management **explicit and systematic**, reducing cognitive load when orchestrating complex multi-stage workflows.

### Migration Notes

**Backward Compatibility**: All v2.0.0 cascade definitions remain valid. New fields are optional.

**To Adopt Cognitive Frames**:
1. Add `state_tracking: aspectual` and `hierarchy_tracking: enabled` to cascade config
2. Annotate stages with `state:` and `hierarchy_level:` fields
3. Add `state_transitions:` block to stages for explicit transition rules
4. Enable `store_state_history: true` in memory config for state audit trail
5. Use new output templates for state reporting

**Example Minimal Migration**:
```yaml
# v2.0.0 (still works)
cascade:
  name: my-workflow
  stages:
    - stage_id: stage-1
      name: Build

# v2.1.0 (enhanced)
cascade:
  name: my-workflow
  config:
    state_tracking: aspectual
    hierarchy_tracking: enabled
  stages:
    - stage_id: stage-1
      name: Build
      state: PENDING
      hierarchy_level: phase
      state_transitions:
        on_start: PENDING -> IN_PROGRESS
        on_complete: IN_PROGRESS -> COMPLETED
```

---

## [2.0.0] - 2025-11-XX

### Added
- Codex sandbox iteration pattern for auto-fix loops
- Multi-model intelligent routing (Gemini/Codex/Claude)
- Ruv-swarm MCP integration for parallel coordination
- Memory persistence across cascade stages
- GitHub workflow automation (PR creation, issue reporting)
- Enhanced error recovery with multiple strategies

### Changed
- Expanded stage types to include codex-sandbox, multi-model, swarm-parallel
- Enhanced data flow with multi-model context and sandbox state
- Advanced error handling with auto-fix and model switching

---

## [1.0.0] - Initial Release

- Sequential, parallel, and conditional cascade execution
- Micro-skill composition and coordination
- Basic data flow and error handling
- Cascade definition format
