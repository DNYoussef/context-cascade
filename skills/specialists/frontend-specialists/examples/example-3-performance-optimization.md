# Example 3: Performance Optimization

## Context
Next.js storefront with slow product grid; CWV targets failing (LCP 4.5s → goal <2.5s).

## Plan (Skill-Forge Validation)
1. Measure baseline (Lighthouse/Profiler) and capture constraints (hosting, cache/CDN, bundle budget).
2. Interventions:
   - Code-splitting and lazy loading for non-critical widgets.
   - Image optimization (next/image, proper sizes, preconnect for CDN).
   - Data fetching: incremental static regeneration + stale-while-revalidate.
   - Reduce hydration cost: memoization, virtualization for grids, remove unnecessary client JS.
3. Validation:
   - Re-run CWV metrics; profile render timings and bundle size.
   - Regression tests + a11y checks to ensure no UX regressions.

## Outputs
- Optimization diff list with before/after metrics.
- Rollout/rollback notes and monitoring hooks.
- Confidence: 0.73 (ceiling: observation 0.95) - Improvements verified on staging metrics.
