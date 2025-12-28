---
name: frontend-specialists
description: Comprehensive frontend development system with specialist agents for React, Vue, UI components, CSS styling, accessibility, and performance optimization. Use when building modern web applications, component libraries, or optimizing frontend performance. Includes production-ready scripts, templates, and testing utilities.
---

# Frontend Specialists


## When to Use This Skill

- **React/Vue/Angular Development**: Building modern frontend applications
- **Component Development**: Creating reusable UI components
- **State Management**: Implementing Redux, Zustand, Pinia, or other state solutions
- **Performance Optimization**: Improving render performance or bundle size
- **Accessibility**: Implementing WCAG-compliant interfaces
- **Responsive Design**: Building mobile-first or adaptive layouts

## When NOT to Use This Skill

- **Backend APIs**: Server-side logic or database operations
- **Static Sites**: Simple HTML/CSS without framework complexity
- **Native Mobile**: React Native, Flutter, Swift, Kotlin (use mobile specialist)
- **Design Work**: Visual design or UI/UX research (use designer)

## Success Criteria

- [ ] Components render correctly across browsers (Chrome, Firefox, Safari, Edge)
- [ ] Responsive design works on mobile, tablet, desktop
- [ ] Accessibility score >90 (axe-core, Lighthouse)
- [ ] Performance budget met (FCP <2s, LCP <2.5s, CLS <0.1)
- [ ] Unit tests passing for components
- [ ] E2E tests passing for user flows
- [ ] TypeScript types accurate with no any types
- [ ] Bundle size within limits

## Edge Cases to Handle

- **Hydration Mismatches**: SSR/SSG content differing from client render
- **Browser Differences**: Vendor prefixes, polyfills, or feature detection
- **Offline Support**: Service workers or offline-first functionality
- **Memory Leaks**: Event listeners, subscriptions, or timers not cleaned up
- **Large Lists**: Virtualization for rendering 1000+ items
- **Form Validation**: Complex multi-step forms with async validation

## Guardrails

- **NEVER** mutate state directly (use immutable updates)
- **ALWAYS** clean up effects (removeEventListener, unsubscribe)
- **NEVER** store sensitive data in localStorage
- **ALWAYS** sanitize user input before rendering (prevent XSS)
- **NEVER** skip key prop on list items
- **ALWAYS** use semantic HTML and ARIA labels
- **NEVER** block main thread with heavy computation (use Web Workers)

## Evidence-Based Validation

- [ ] Lighthouse audit score >90 in all categories
- [ ] React DevTools Profiler shows no unnecessary re-renders
- [ ] Bundle analyzer shows no duplicate dependencies
- [ ] axe-core accessibility scan passes
- [ ] Visual regression tests pass (Percy, Chromatic)
- [ ] Cross-browser testing (BrowserStack, Playwright)
- [ ] Console shows no errors or warnings

A comprehensive frontend development system combining specialized agents, production scripts, and reusable templates for modern web application development.

## Purpose

Provide complete frontend development capabilities through specialized agents and tools. Each specialist focuses on a specific domain (React, Vue, UI components, CSS, accessibility, performance) while sharing common scripts and templates for rapid development.

## System Architecture

```
frontend-specialists/
├── skill.md (this file)
├── react-specialist/      # React 18+ specialist
├── vue-specialist/        # Vue 3 specialist (future)
├── ui-component-builder/  # Component library specialist (future)
├── resources/
│   ├── scripts/           # Production automation scripts
│   │   ├── component-generator.js
│   │   ├── bundle-analyzer.js
│   │   ├── a11y-checker.js
│   │   └── performance-profiler.js
│   └── templates/         # Reusable component templates
│       ├── react-component.tsx
│       ├── vue-component.vue
│       └── component.config.json
└── tests/                 # Comprehensive test suites
    ├── component-generator.test.js
    ├── bundle-analyzer.test.js
    └── a11y-checker.test.js
```

## Available Specialists

### 1. React Specialist (`react-specialist`)
**Triggers**: "React", "React 18", "Next.js", "hooks", "server components"

**Capabilities**:
- React 18+ with concurrent rendering
- Next.js 13+ App Router with Server Components
- State management (Zustand, Redux Toolkit, Jotai)
- Performance optimization (memoization, code splitting)
- Testing with React Testing Library

**Agent**: `react-developer`

### 2. Vue Specialist (Planned)
**Triggers**: "Vue", "Vue 3", "Composition API", "Nuxt"

**Capabilities**:
- Vue 3 Composition API
- Nuxt 3 with server-side rendering
- Pinia state management
- Vue testing utilities

**Agent**: `vue-developer`

### 3. UI Component Builder (Planned)
**Triggers**: "component library", "design system", "UI components"

**Capabilities**:
- Component library architecture
- Storybook integration
- Theming and customization
- Component documentation

**Agent**: `ui-component-builder`

### 4. CSS Styling Specialist (Planned)
**Triggers**: "CSS", "Tailwind", "styled-components", "CSS-in-JS"

**Capabilities**:
- Modern CSS (Grid, Flexbox, Container Queries)
- Tailwind CSS utility-first design
- CSS-in-JS (styled-components, Emotion)
- Responsive design patterns

**Agent**: `css-styling-specialist`

### 5. Accessibility Specialist (Planned)
**Triggers**: "accessibility", "a11y", "WCAG", "ARIA"

**Capabilities**:
- WCAG 2.1 AA/AAA compliance
- ARIA patterns and semantics
- Keyboard navigation
- Screen reader testing

**Agent**: `accessibility-specialist`

### 6. Performance Optimizer (Planned)
**Triggers**: "performance", "optimization", "bundle size", "lighthouse"

**Capabilities**:
- Bundle size optimization
- Code splitting strategies
- Image optimization
- Performance monitoring

**Agent**: `frontend-performance-optimizer`

## Shared Scripts

### 1. Component Generator (`component-generator.js`)
**Purpose**: Scaffold new components with best practices

```bash
# Generate React component
node resources/scripts/component-generator.js --framework react --name Button --type functional

# Generate Vue component
node resources/scripts/component-generator.js --framework vue --name Card --type composition
```

**Features**:
- TypeScript support
- Test file generation
- Storybook story creation
- Accessibility defaults (ARIA, semantic HTML)

### 2. Bundle Analyzer (`bundle-analyzer.js`)
**Purpose**: Analyze and optimize bundle sizes

```bash
# Analyze bundle
node resources/scripts/bundle-analyzer.js --project ./my-app --threshold 200

# Output: Bundle report with recommendations
```

**Features**:
- Webpack/Vite/Rollup support
- Tree-shaking analysis
- Dependency visualization
- Size recommendations

### 3. Accessibility Checker (`a11y-checker.js`)
**Purpose**: Automated accessibility audits

```bash
# Check accessibility
node resources/scripts/a11y-checker.js --url http://localhost:3000 --level AA

# Output: WCAG violations with fixes
```

**Features**:
- axe-core integration
- WCAG 2.1 AA/AAA validation
- Color contrast checking
- Keyboard navigation testing

### 4. Performance Profiler (`performance-profiler.js`)
**Purpose**: Performance metrics and optimization suggestions

```bash
# Profile performance
node resources/scripts/performance-profiler.js --url http://localhost:3000

# Output: Lighthouse scores, Web Vitals, optimization tips
```

**Features**:
- Lighthouse integration
- Core Web Vitals (LCP, FID, CLS)
- Performance budget validation
- Optimization recommendations

## Shared Templates

### 1. React Component Template (`react-component.tsx`)
- Functional component with TypeScript
- Props interface
- Accessibility attributes
- CSS module import
- Test file structure

### 2. Vue Component Template (`vue-component.vue`)
- Composition API structure
- TypeScript support
- Scoped styles
- Accessibility setup

### 3. Component Config (`component.config.json`)
- Component metadata
- Variant definitions
- Theming variables
- Documentation links

## Quality Criteria

All frontend specialists adhere to:

- ✅ **TypeScript**: Strict mode enabled
- ✅ **Accessibility**: WCAG 2.1 AA minimum
- ✅ **Performance**: Lighthouse score ≥90
- ✅ **Testing**: Coverage ≥80%
- ✅ **Bundle Size**: <200KB initial load (gzipped)
- ✅ **Browser Support**: Last 2 versions, >0.5% market share

## Testing Strategy

### Unit Tests (Jest/Vitest)
```javascript
// Component logic, hooks, utilities
describe('Button', () => {
  it('renders with correct variant', () => {
    // Test implementation
  });
});
```

### Integration Tests (React Testing Library)
```javascript
// User interactions, form submissions
test('submits form on button click', async () => {
  // Test implementation
});
```

### E2E Tests (Playwright)
```javascript
// Full user workflows
test('complete checkout flow', async ({ page }) => {
  // Test implementation
});
```

### Visual Regression (Chromatic/Percy)
```javascript
// UI consistency checks
test('button snapshot', () => {
  // Snapshot comparison
});
```

## Best Practices

**1. Component Architecture**
- Single Responsibility Principle
- Composition over inheritance
- Props validation with TypeScript
- Controlled vs uncontrolled components

**2. State Management**
- Local state for UI (useState)
- Global state for app-wide data (Zustand/Redux)
- Server state for API data (TanStack Query)
- URL state for navigation (Next.js router)

**3. Performance Optimization**
- Code splitting with lazy loading
- Memoization (React.memo, useMemo, useCallback)
- Virtual scrolling for large lists
- Image optimization (next/image, WebP)

**4. Accessibility**
- Semantic HTML elements
- ARIA attributes when needed
- Keyboard navigation support
- Focus management
- Color contrast ratios

**5. Testing**
- Test user behavior, not implementation
- Accessibility testing in all tests
- Mock external dependencies
- Integration tests over unit tests

## Integration with Other Skills

- `typescript-specialist`: TypeScript patterns and advanced types
- `wcag-accessibility`: Deep accessibility compliance
- `testing-quality`: Advanced testing strategies
- `docker-containerization`: Containerizing frontend apps
- `cicd-intelligent-recovery`: CI/CD pipeline integration

## MCP Tools

### Sandbox Testing
```javascript
// Create isolated frontend sandbox
mcp__flow-nexus__sandbox_create({
  template: "react", // or "nextjs", "vanilla"
  env_vars: { NODE_ENV: "development" }
})
```

### Browser Automation
```javascript
// Visual testing with Playwright
mcp__playwright__browser_snapshot()
mcp__playwright__browser_take_screenshot({ fullPage: true })
```

### Memory Persistence
```javascript
// Store component patterns
mcp__memory-mcp__memory_store({
  key: "frontend/react-patterns",
  value: { pattern: "compound-components", usage: "..." }
})
```

## Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Component Creation | 10-15 min | Time to scaffold + test |
| Feature Development | 1-2 hours | Implementation + tests |
| Lighthouse Score | ≥90 | Performance audit |
| Test Coverage | ≥80% | Jest/Vitest reports |
| Bundle Size | <200KB | Webpack/Vite analysis |
| Accessibility | WCAG 2.1 AA | axe-core validation |

## Troubleshooting

### Issue: Hydration Mismatch (Next.js)
**Solution**: Ensure server/client HTML match. Use `suppressHydrationWarning` for time-dependent content.

### Issue: Slow Performance with Large Lists
**Solution**: Implement virtualization (react-window, react-virtual).

### Issue: Bundle Size Too Large
**Solution**: Use bundle analyzer, code splitting, tree-shaking, dynamic imports.

### Issue: Accessibility Violations
**Solution**: Run axe-core, add ARIA labels, semantic HTML, keyboard support.

## Workflow: Complete Feature Development

**Step 1: Initialize with Specialist**
```bash
# Trigger appropriate specialist
"I need to build a React dashboard with charts"
→ Activates react-specialist
```

**Step 2: Generate Component Scaffolding**
```bash
node resources/scripts/component-generator.js \
  --framework react \
  --name Dashboard \
  --type functional
```

**Step 3: Implement with Best Practices**
- Use shared templates
- Follow TypeScript patterns
- Implement accessibility defaults

**Step 4: Test Comprehensively**
- Unit tests for logic
- Integration tests for interactions
- Accessibility tests with axe-core

**Step 5: Optimize Performance**
```bash
node resources/scripts/bundle-analyzer.js --project ./my-app
node resources/scripts/performance-profiler.js --url http://localhost:3000
```

**Step 6: Validate Quality**
```bash
node resources/scripts/a11y-checker.js --url http://localhost:3000 --level AA
npm run test -- --coverage
```

## Related Documentation

- [React Specialist Skill](./react-specialist/skill.md)
- [Component Generator Script](./resources/scripts/component-generator.js)
- [Bundle Analyzer Script](./resources/scripts/bundle-analyzer.js)
- [Accessibility Checker Script](./resources/scripts/a11y-checker.js)
- [Performance Profiler Script](./resources/scripts/performance-profiler.js)

## Core Principles

1. **Accessibility is Not Optional, It's Foundational**: Building accessible interfaces isn't a feature to add later or a compliance checkbox - it's a fundamental architectural requirement that shapes component design from the start. Every interactive element must be keyboard navigable, every state change must be announced to screen readers, and every visual distinction must work without color alone. This means using semantic HTML as the foundation (button, nav, main, article), adding ARIA attributes only when semantic HTML is insufficient, and testing with keyboard navigation and screen readers during development, not after. Accessibility failures aren't minor issues - they exclude users and expose organizations to legal liability. WCAG 2.1 AA compliance should be the minimum bar, with automated testing (axe-core) integrated into CI/CD and manual testing with assistive technologies as part of the definition of done.

2. **Performance is a Feature, Not an Afterthought**: Frontend performance directly impacts user experience, conversion rates, and SEO rankings. Core Web Vitals (LCP < 2.5s, FID < 100ms, CLS < 0.1) are measurable business metrics, not abstract technical ideals. This requires performance budgets enforced in CI/CD, lazy loading for routes and heavy components, image optimization with modern formats (WebP, AVIF) and responsive images, code splitting to minimize initial bundle size, and React-specific optimizations like memoization (React.memo, useMemo, useCallback) to prevent unnecessary re-renders. Performance optimization isn't premature if it's built into the development workflow - using Lighthouse in CI/CD, profiling with React DevTools, and testing on real devices with throttled connections ensures performance issues are caught before they reach production.

3. **Component Architecture Follows Composition Over Inheritance**: Modern frontend development favors composition patterns where complex UIs are built from small, focused components rather than inheritance hierarchies. Each component should have a single responsibility, accept props for configuration, and compose smaller components rather than implementing monolithic functionality. This means designing component APIs thoughtfully (what should be props vs children vs render props), using TypeScript to enforce prop contracts, implementing controlled vs uncontrolled patterns appropriately, and creating reusable primitives (Button, Input, Card) that compose into domain-specific components (LoginForm, ProductCard). Composition enables reusability, testability, and maintainability - a well-designed component library becomes a shared language across the team with components that can be recombined to solve new problems without modification.

## Anti-Patterns

| Anti-Pattern | Why It Fails | Better Approach |
|-------------|--------------|-----------------|
| **Mutating State Directly** | Directly modifying state objects (state.user.name = 'new') breaks React's reconciliation algorithm, causing components to not re-render or re-rendering inconsistently. React compares previous and next state by reference, so in-place mutations make state appear unchanged. This leads to subtle bugs where UI doesn't update when it should, or updates at unexpected times. | Use immutable update patterns: spread operators for objects ({...state, user: {...state.user, name: 'new'}}), array methods that return new arrays (map, filter, concat instead of push/splice), or state management libraries like Immer that provide immutable-friendly APIs. For complex state, use useReducer with immutable updates or Zustand/Redux with Immer integration. |
| **Skipping Cleanup in useEffect** | Effects that add event listeners, create subscriptions, or start timers without cleanup cause memory leaks and duplicate handlers. Each time the component re-renders, a new effect runs without removing the previous one, accumulating listeners/subscriptions/timers until the browser slows down or crashes. | Always return a cleanup function from useEffect that removes listeners, cancels subscriptions, and clears timers: useEffect(() => { const handler = () => {}; window.addEventListener('resize', handler); return () => window.removeEventListener('resize', handler); }, []). Test cleanup by forcing re-renders and checking that handlers aren't duplicated. |
| **Overusing Context for Frequently Changing State** | React Context was designed for infrequent updates (theme, user auth) not frequent changes (form inputs, animation states). When context value changes, all consumers re-render, even if they only use a small part of the context. This causes performance issues where unrelated components re-render on every keystroke or animation frame. | Use context for truly global, infrequent state. For frequent updates, use local component state, or specialized state management (Zustand, Redux) with selector-based subscriptions that only re-render when relevant data changes. For form state, use React Hook Form or similar libraries that minimize re-renders. Split large contexts into smaller, focused contexts to reduce re-render scope. |

## Conclusion

The Frontend Specialists skill provides comprehensive capabilities for building modern, accessible, and performant web applications. By combining specialized agents for React, Vue, UI components, CSS, accessibility, and performance with production-ready scripts and templates, this skill enables teams to deliver high-quality frontend experiences that meet both user needs and technical requirements.

Success with this skill requires balancing user experience, accessibility, performance, and maintainability. The tooling provided - component generators, bundle analyzers, accessibility checkers, and performance profilers - ensures that best practices are enforced throughout development rather than retrofitted before launch. The multi-specialist architecture recognizes that frontend development spans multiple domains, each requiring deep expertise, from framework-specific patterns to accessibility compliance to performance optimization.

Whether building a React dashboard with real-time updates, implementing a design system with comprehensive component libraries, or optimizing a sluggish application with bundle splitting and lazy loading, this skill provides the expertise, automation, and quality standards needed to ship production-grade frontend applications. The Gold tier designation reflects the comprehensive coverage, production-ready tooling, and battle-tested patterns that enable teams to build frontend systems with confidence and consistency.