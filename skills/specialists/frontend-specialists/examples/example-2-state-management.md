# Example 2: State Management Decision

## Context
Choose a state strategy for a React dashboard with real-time data and offline tolerance.

## Constraints (HARD/SOFT/INFERRED)
- HARD: React + WebSocket feed; offline read cache; error budget p95 <200ms.
- SOFT: Minimal bundle growth; DX-friendly tooling.
- INFERRED: Need query caching + mutation retries.

## Decision Flow
1. Evaluate options (React Query vs Redux Toolkit vs Context-only) against constraints.
2. Select React Query + lightweight context for UI state; enable cache persistence for offline.
3. Define mutation/optimistic update rules and error boundaries.
4. Validate with perf/a11y tests, bundle size check, and failure simulation.

## Output
- Decision rationale, API boundaries, and migration steps.
- Confidence: 0.72 (ceiling: inference 0.70) - Based on scenario scoring and validation steps.
