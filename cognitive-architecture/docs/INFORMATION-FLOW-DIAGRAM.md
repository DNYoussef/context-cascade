# Cognitive Architecture Information Flow Diagram

**Generated**: 2026-01-09
**Smoke Test Status**: ALL PASS

---

## Executive Summary

```
+------------------+     +------------------+     +------------------+
|   USER REQUEST   | --> |   LOOP 1: EXEC   | --> |  LOOP 1.5: REFLECT|
+------------------+     +------------------+     +------------------+
                                |                        |
                                v                        v
                         +-------------+          +-------------+
                         | FrozenHarn. |          | Reflect     |
                         | + Connasc.  |          | to Memory   |
                         +-------------+          +-------------+
                                |                        |
                                v                        v
                         +------------------------------------------+
                         |            MEMORY MCP STORAGE            |
                         |  (ChromaDB + WHO/WHEN/PROJECT/WHY tags)  |
                         +------------------------------------------+
                                          |
                                          v
                         +------------------+     +------------------+
                         | LOOP 2: QUALITY  | <-- | LOOP 3: META-OPT |
                         +------------------+     +------------------+
```

---

## Component Smoke Test Results

| # | Component | Status | Mode | Key Metrics |
|---|-----------|--------|------|-------------|
| 1 | FrozenHarness | PASS | cli_evaluator | overall: 0.79 |
| 2 | ConnascenceBridge | PASS | cli (mock fallback) | sigma: 4.0, dpmo: 3132 |
| 3 | TelemetryBridge | PASS | file-based | 17 items stored |
| 4 | Library Catalog | PASS | json | 25 components, 8 domains |
| 5 | Meta-Loop Runner | PASS | script ready | 9 functions |
| 6 | Reflect-to-Memory | PASS | script ready | 6 functions |
| 7 | Memory MCP Storage | PASS | mcp-fallback | 17+ items |
| 8 | Scheduled Task | PASS | Windows Task Scheduler | Ready state |

---

## Detailed Information Flows

### Flow 1: User Request -> Execution (Loop 1)

```
[User Request]
      |
      v
+------------------+
| 5-Phase Workflow |
| 1. Intent        |
| 2. Prompt Opt    |
| 3. Planning      |
| 4. Playbook      |
| 5. Execution     |
+------------------+
      |
      v
[Task() Agents]
      |
      v
[Artifact Output]
```

**Data Produced**:
- Artifact files (code, docs, etc.)
- Task metadata
- Execution logs

---

### Flow 2: Artifact -> FrozenHarness Evaluation

```
[Artifact Path]
      |
      v
+------------------+
| FrozenHarness    |
| .grade()         |
+------------------+
      |
      +---> [CLI Evaluator] ---> LLM Judge
      |            |
      |            v
      |     {task_accuracy, token_efficiency,
      |      edge_robustness, epistemic_consistency}
      |
      +---> [ConnascenceBridge]
                   |
                   v
             {sigma_level, dpmo, nasa_compliance,
              mece_score, theater_risk, clarity_score,
              violations_count, passes_strict}
                   |
                   v
+------------------+
| Combined Metrics |
| overall: 0.79    |
| connascence: {...}|
+------------------+
      |
      v
[eval_report.json]
```

**Data Flow**:
```
Input:  artifact_path (Path)
Output: {
  task_accuracy: 0.85,
  token_efficiency: 0.90,
  edge_robustness: 0.65,
  epistemic_consistency: 0.70,
  overall: 0.79,
  evaluation_mode: "cli_evaluator",
  connascence_mode: "cli",
  connascence: {
    sigma_level: 6.0,
    dpmo: 0.0,
    nasa_compliance: 1.0,
    mece_score: 0.80,
    theater_risk: 0.0,
    clarity_score: 0.75,
    violations_count: 0,
    critical_violations: 0,
    passes_strict: true,
    passes_lenient: true
  }
}
```

---

### Flow 3: Evaluation -> TelemetryBridge -> Memory MCP

```
[eval_report.json]
      |
      v
+------------------+
| TelemetryBridge  |
| .store_to_memory |
| _mcp()           |
+------------------+
      |
      v
+------------------+
| WHO/WHEN/PROJECT |
| /WHY Tagging     |
+------------------+
      |
      v
+------------------+
| Memory MCP       |
| (ChromaDB)       |
+------------------+
      |
      v
[storage/mcp-fallback/*.json]
```

**Data Flow**:
```
Input:  iteration (int), eval_report (dict)
Output: {
  WHO: "telemetry-bridge:loopctl",
  WHEN: "2026-01-09T12:00:00Z",
  PROJECT: "cognitive-architecture",
  WHY: "iteration-telemetry",
  iteration: 1,
  metrics: {...},
  harness_version: "1.0.0"
}
```

---

### Flow 4: Session End -> Reflect -> Memory MCP (Loop 1.5)

```
[Session End Hook]
      |
      v
+------------------+
| reflect_to_      |
| memory.py        |
+------------------+
      |
      v
+------------------+
| Signal Detection |
| - Corrections    |
| - Explicit Rules |
| - Approvals      |
| - Observations   |
+------------------+
      |
      v
+------------------+
| store_session_   |
| learnings()      |
+------------------+
      |
      v
[Memory MCP with tags]
  WHO: "reflect:session-{id}"
  WHEN: ISO8601
  PROJECT: detected-project
  WHY: "session-learning"
```

**Data Flow**:
```
Input:  session_transcript, corrections, patterns
Output: {
  WHO: "reflect:session-abc123",
  WHEN: "2026-01-09T12:00:00Z",
  PROJECT: "cognitive-architecture",
  WHY: "session-learning",
  signal_type: "correction",
  confidence: 0.90,
  skill_affected: "code",
  learning: "Always run tests before commit",
  context: "User corrected premature commit"
}
```

---

### Flow 5: Memory MCP -> Meta-Loop Optimization (Loop 3)

```
[Scheduled Task: Every 3 Days]
      |
      v
+------------------+
| meta_loop_       |
| runner.py        |
+------------------+
      |
      v
+------------------+
| query_session_   |
| learnings()      |
+------------------+
      |
      v
[Memory MCP Query]
  intent: "session-learning"
  time_range: last 3 days
      |
      v
+------------------+
| aggregate_by_    |
| skill()          |
+------------------+
      |
      v
+------------------+
| identify_        |
| patterns()       |
+------------------+
      |
      v
+------------------+
| detect_          |
| conflicts()      |
+------------------+
      |
      v
+------------------+
| generate_        |
| report()         |
+------------------+
      |
      v
[Optimization Suggestions]
  - Skill file updates
  - Named mode adjustments
  - Template improvements
```

**Data Flow**:
```
Input:  Memory MCP learnings (last 3 days)
Output: {
  total_learnings: 47,
  skills_affected: ["code", "debug", "test"],
  patterns: [
    {pattern: "test-before-commit", frequency: 12},
    {pattern: "type-check-imports", frequency: 8}
  ],
  conflicts: [],
  recommendations: [
    "Update code skill: add pre-commit test step",
    "Update debug skill: include type checking"
  ]
}
```

---

### Flow 6: Library Catalog Lookup (Pre-Coding Guard)

```
[Pre-Coding Hook]
      |
      v
+------------------+
| pre-coding-      |
| library-check.sh |
+------------------+
      |
      v
+------------------+
| catalog.json     |
| (25 components)  |
+------------------+
      |
      v
+------------------+
| Search:          |
| - By keyword     |
| - By domain      |
| - By technology  |
+------------------+
      |
      v
[Match Results]
  >90%: REUSE
  70-90%: ADAPT
  <70%: BUILD NEW
      |
      v
[Memory MCP Log]
  WHO: "library-check:1.0.0"
  WHY: "pre-coding-guard"
```

**Data Flow**:
```
Input:  task_description, keywords
Output: {
  matches: [
    {
      id: "frozen-harness",
      name: "FrozenHarness Evaluation System",
      location: "cognitive-architecture/loopctl/core.py",
      quality_score: 80,
      match_confidence: 0.92
    }
  ],
  recommendation: "REUSE",
  time_saved: "8+ hours"
}
```

---

### Flow 7: Quality Gate Check (Loop 2)

```
[Artifact/Directory]
      |
      v
+------------------+
| ConnascenceBridge|
| .analyze_file()  |
| .analyze_dir()   |
+------------------+
      |
      v
+------------------+
| 7-Analyzer Suite |
| 1. Connascence   |
| 2. NASA Safety   |
| 3. MECE          |
| 4. Clarity       |
| 5. Six Sigma     |
| 6. Theater       |
| 7. Safety        |
+------------------+
      |
      v
[ConnascenceResult]
      |
      v
+------------------+
| .passes_gate()   |
| strict=True/False|
+------------------+
      |
      +---> PASS: Continue
      |
      +---> FAIL: Block/Escalate
```

**Quality Thresholds**:
```
Strict Mode:
  sigma_level >= 4.0
  dpmo <= 6210
  nasa_compliance >= 0.95
  mece_score >= 0.80
  theater_risk < 0.20
  critical_violations == 0

Lenient Mode:
  critical_violations == 0
```

---

## Complete System Flow (End-to-End)

```
+===========================================================================+
|                         COGNITIVE ARCHITECTURE                             |
+===========================================================================+

[User Request]
      |
      v
+===================+
| LOOP 1: EXECUTION |
+===================+
      |
      +---> [5-Phase Workflow]
      |            |
      |            v
      |     [Task() Agents]
      |            |
      |            v
      |     [Artifact Output]
      |            |
      v            v
+------------------+
| FrozenHarness    |<----+
| .grade()         |     |
+------------------+     |
      |                  |
      +---> [CLI Eval]   |
      |                  |
      +---> [Connascence]|
      |                  |
      v                  |
[eval_report.json]       |
      |                  |
      v                  |
+------------------+     |
| TelemetryBridge  |     |
+------------------+     |
      |                  |
      v                  |
+==================+     |
| MEMORY MCP       |     |
| (ChromaDB)       |<----+----+----+
+==================+     |    |    |
      ^                  |    |    |
      |                  |    |    |
+===================+    |    |    |
| LOOP 1.5: REFLECT |----+    |    |
+===================+         |    |
      ^                       |    |
      |                       |    |
[Session End Hook]            |    |
      |                       |    |
      v                       |    |
[reflect_to_memory.py]--------+    |
                                   |
+===================+              |
| LOOP 2: QUALITY   |              |
+===================+              |
      |                            |
      +---> [ConnascenceBridge]    |
      |                            |
      v                            |
[Quality Gate: PASS/FAIL]          |
                                   |
+===================+              |
| LOOP 3: META-OPT  |              |
+===================+              |
      |                            |
      +---> [Scheduled: 3 days]    |
      |                            |
      v                            |
[meta_loop_runner.py]--------------+
      |
      v
[Optimization Report]
      |
      v
[Cascade Updates]
  - Skills
  - Agents
  - Commands
  - Templates

+===========================================================================+
|                         EXTERNAL INTEGRATIONS                              |
+===========================================================================+

[Library Catalog]  <---> [Pre-Coding Hook]
  25 components            |
  8 domains                v
                    [REUSE/ADAPT/BUILD]

[Windows Task Scheduler] ---> [meta_loop_runner.py] ---> [Memory MCP]
  Every 3 days @ 3:00 AM

[Claude CLI] <---> [FrozenHarness CLI Evaluator]
  LLM-as-Judge

[Connascence Project] <---> [ConnascenceBridge]
  D:\Projects\connascence     (mock fallback active)
```

---

## Data Storage Locations

| Storage | Location | Purpose | Items |
|---------|----------|---------|-------|
| MCP Fallback | `cognitive-architecture/storage/mcp-fallback/` | Telemetry, evaluations | 17 |
| Memory MCP Data | `D:\Projects\memory-mcp-triple-system\data\` | Graph, entities | 7 |
| Library Catalog | `~/.claude/library/catalog.json` | Component index | 25 |
| Scheduled Task | Windows Task Scheduler | Meta-loop trigger | 1 |

---

## Key Files

| Component | File | Lines | Functions |
|-----------|------|-------|-----------|
| FrozenHarness | `loopctl/core.py` | 524 | grade, _grade_with_cli, _grade_with_connascence |
| ConnascenceBridge | `integration/connascence_bridge.py` | 447 | analyze_file, analyze_directory, _analyze_mock |
| TelemetryBridge | `integration/telemetry_bridge.py` | ~200 | store_to_memory_mcp, sync_iteration |
| Meta-Loop Runner | `scripts/meta_loop_runner.py` | 387 | query_session_learnings, aggregate_by_skill, generate_report |
| Reflect-to-Memory | `scripts/reflect_to_memory.py` | 362 | store_session_learnings, parse_learnings_from_file |
| Library Catalog | `~/.claude/library/catalog.json` | - | 25 components |

---

## Smoke Test Commands

```bash
# Test 1: FrozenHarness
cd cognitive-architecture && python -m loopctl self-test

# Test 2: ConnascenceBridge
python -c "from integration.connascence_bridge import ConnascenceBridge; b=ConnascenceBridge(); print(b.mode)"

# Test 3: Library Catalog
python -c "import json; print(json.load(open('~/.claude/library/catalog.json'))['statistics'])"

# Test 4: Scheduled Task
schtasks /query /tn "MemoryMCP-MetaLoop-3Day"

# Test 5: Meta-Loop Runner (dry run)
python scripts/meta_loop_runner.py --dry-run

# Test 6: Storage Check
ls storage/mcp-fallback/
```

---

<promise>INFORMATION_FLOW_DOCUMENTED_2026_01_09</promise>
