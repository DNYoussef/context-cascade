---
name: ui-ux-excellence
description: Comprehensive UI/UX enhancement cascade that transforms generic websites into polished, accessible, brand-differentiated experiences. Combines constraint-based design, WCAG accessibility, micro-interactions, typography systems, and responsive refinements. Use when elevating landing pages, marketing sites, or any frontend that needs to stand out.
---

# UI/UX Excellence Cascade

Transform generic websites into polished, brand-differentiated experiences through a systematic 7-phase cascade.

## Purpose

This skill combines insights from multiple specialized skills into a single comprehensive workflow for elevating frontend experiences:

- **wcag-accessibility**: WCAG 2.1 AA compliance, ARIA, keyboard navigation
- **react-specialist**: Modern component patterns, performance optimization
- **style-audit**: Code quality, consistency, maintainability
- **pptx-generation/design-principles**: Constraint-based design philosophy
- **cascade-orchestrator**: Multi-phase workflow coordination

## When to Use This Skill

- Transforming MVP/prototype into production-ready frontend
- Elevating landing pages for premium brand positioning
- Adding micro-interactions and polish to existing sites
- Ensuring accessibility compliance before launch
- Creating differentiated experiences for different market segments
- Building design systems from scratch

## Prerequisites

**Required**: HTML/CSS, Tailwind CSS (optional), JavaScript basics
**Agents**: `coder`, `reviewer`, `frontend-dev`
**MCP**: None required (operates with Claude Code built-in tools)

## The 7-Phase Cascade

```
Phase 1: Brand Analysis & Design System Definition
    |
    v
Phase 2: Accessibility Foundation (WCAG)
    |
    v
Phase 3: Typography System Implementation
    |
    v
Phase 4: Micro-interactions & Motion Design
    |
    v
Phase 5: Component Enhancement & Polish
    |
    v
Phase 6: Responsive & Mobile Refinement
    |
    v
Phase 7: Style Audit & Validation
```



## Phase 2: Accessibility Foundation (WCAG)

### Purpose
Ensure WCAG 2.1 AA compliance for legal requirements and inclusive design.

### Key Activities

1. **Implement Skip Link**
   ```html
   <a href="#main-content" class="skip-link">Skip to main content</a>
   ```
   ```css
   .skip-link {
     position: absolute;
     top: -100%;
     left: 50%;
     transform: translateX(-50%);
     z-index: 9999;
     padding: 0.75rem 1.5rem;
     background: var(--color-primary);
     color: white;
     font-weight: 600;
     border-radius: 0.5rem;
     text-decoration: none;
     transition: top 150ms ease;
   }

   .skip-link:focus {
     top: 1rem;
     outline: 3px solid var(--color-accent);
     outline-offset: 2px;
   }
   ```

2. **Enhanced Focus States**
   ```css
   :focus-visible {
     outline: 3px solid var(--color-primary);
     outline-offset: 3px;
     border-radius: 0.25rem;
   }
   ```

3. **Color Contrast Validation**
   - Normal text: minimum 4.5:1 ratio
   - Large text (18pt+): minimum 3:1 ratio
   - Use tools: WebAIM Contrast Checker, axe DevTools

4. **Semantic HTML**
   - Use `<header>`, `<main>`, `<nav>`, `<footer>` landmarks
   - Proper heading hierarchy (h1 -> h2 -> h3)
   - Button vs link distinction

5. **Reduced Motion Support**
   ```css
   @media (prefers-reduced-motion: reduce) {
     *,
     *::before,
     *::after {
       animation-duration: 0.01ms !important;
       animation-iteration-count: 1 !important;
       transition-duration: 0.01ms !important;
     }
   }
   ```

### Output
- Skip link implementation
- Focus state styles
- Reduced motion media query
- Semantic HTML structure



## Phase 4: Micro-interactions & Motion Design

### Purpose
Add subtle animations that enhance user experience without overwhelming.

### Key Activities

1. **Scroll-triggered Animations**
   ```css
   .animate-on-scroll {
     opacity: 0;
     transform: translateY(30px);
     transition:
       opacity 0.7s cubic-bezier(0.16, 1, 0.3, 1),
       transform 0.7s cubic-bezier(0.16, 1, 0.3, 1);
     will-change: opacity, transform;
   }

   .animate-on-scroll.is-visible {
     opacity: 1;
     transform: translateY(0);
   }
   ```

2. **Intersection Observer Script**
   ```javascript
   const observer = new IntersectionObserver((entries) => {
     entries.forEach(entry => {
       if (entry.isIntersecting) {
         entry.target.classList.add('is-visible');
         observer.unobserve(entry.target);
       }
     });
   }, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });

   document.querySelectorAll('.animate-on-scroll')
     .forEach(el => observer.observe(el));
   ```

3. **Staggered Children Animation**
   ```css
   .stagger-children > * {
     opacity: 0;
     transform: translateY(20px);
     transition: opacity 0.5s, transform 0.5s;
   }

   .stagger-children > *:nth-child(1) { transition-delay: 0.1s; }
   .stagger-children > *:nth-child(2) { transition-delay: 0.2s; }
   .stagger-children > *:nth-child(3) { transition-delay: 0.3s; }
   /* ... continue pattern */

   .stagger-children.is-visible > * {
     opacity: 1;
     transform: translateY(0);
   }
   ```

4. **Hover Micro-interactions**

   **Lift Effect**:
   ```css
   .hover-lift {
     transition: transform 0.3s, box-shadow 0.3s;
   }
   .hover-lift:hover {
     transform: translateY(-6px);
     box-shadow: 0 20px 25px -5px rgb(0 0 0 / 0.1);
   }
   ```

   **Underline Reveal**:
   ```css
   .link-underline::after {
     content: '';
     position: absolute;
     bottom: -2px;
     left: 0;
     width: 0;
     height: 2px;
     background: var(--color-accent);
     transition: width 0.3s ease;
   }
   .link-underline:hover::after {
     width: 100%;
   }
   ```

   **Button Press**:
   ```css
   .btn-press:active {
     transform: scale(0.97);
   }
   ```

5. **Noise Texture Overlay** (Premium feel)
   ```css
   body::before {
     content: '';
     position: fixed;
     inset: 0;
     pointer-events: none;
     z-index: 9999;
     opacity: 0.025;
     background-image: url("data:image/svg+xml,..."); /* noise SVG */
   }
   ```

### Output
- Animation CSS classes
- Intersection Observer script
- Hover interaction patterns



## Phase 6: Responsive & Mobile Refinement

### Purpose
Ensure excellent experience across all device sizes.

### Key Activities

1. **Mobile-First Media Queries**
   ```css
   /* Base: Mobile */
   h1 { font-size: var(--text-3xl); }

   /* Tablet */
   @media (min-width: 640px) {
     h1 { font-size: var(--text-4xl); }
   }

   /* Desktop */
   @media (min-width: 1024px) {
     h1 { font-size: var(--text-5xl); }
   }
   ```

2. **Touch Target Sizes**
   - Minimum 44x44px for touch targets
   - Adequate spacing between interactive elements

3. **Container Width**
   ```css
   .container {
     max-width: 1200px;
     margin: 0 auto;
     padding: 0 var(--space-4);
   }

   @media (min-width: 640px) {
     .container { padding: 0 var(--space-6); }
   }

   @media (min-width: 1024px) {
     .container { padding: 0 var(--space-8); }
   }
   ```

4. **Mobile Stack Utilities**
   ```css
   @media (max-width: 640px) {
     .mobile-stack { flex-direction: column; }
     .mobile-full { width: 100%; }
   }
   ```

### Output
- Responsive typography
- Touch-friendly targets
- Mobile utility classes



## Usage Example

```markdown
# Invoke the UI/UX Excellence Cascade

User: "Make my landing page stand out - it looks too generic"
**Remember the pattern: Skill() -> Task() -> TodoWrite() - ALWAYS**

## Common Anti-Patterns

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| **Hardcoding colors/spacing in components** | Inconsistent design, difficult global changes, maintenance nightmare | Use CSS custom properties for ALL design tokens (--color-primary, --space-4) |
| **Skipping accessibility until the end** | Expensive retrofitting, missed WCAG requirements, legal risk | Build accessibility from Phase 2, test with keyboard navigation throughout development |
| **Over-animating the interface** | Motion sickness, distraction, poor performance, unprofessional feel | Limit animations to scroll-triggered and hover states, respect prefers-reduced-motion |
| **Ignoring responsive breakpoints** | Broken mobile experience, unusable on tablets, high bounce rate | Use mobile-first media queries, test at 375px, 768px, 1024px, 1440px breakpoints |
| **Not validating color contrast** | WCAG failures, unreadable text for users, accessibility lawsuits | Use WebAIM Contrast Checker or axe DevTools, enforce 4.5:1 minimum for normal text |

---

## Conclusion

UI/UX Excellence Cascade transforms generic websites into polished, brand-differentiated experiences through systematic application of design principles, accessibility standards, and micro-interactions. By following the 7-phase workflow - from brand analysis through typography implementation to final style audit - this skill ensures no aspect of user experience is overlooked.

The cascade's power lies in its integration of multiple disciplines: constraint-based design from presentation tools (pptx-generation), WCAG compliance from accessibility specialists, component patterns from React experts, and code quality validation from style auditors. This cross-functional approach produces interfaces that are not only beautiful but also accessible, performant, and maintainable.

Use this skill when elevating MVP prototypes to production quality, creating marketing sites that reflect premium brand positioning, or building design systems from scratch. The 7-phase structure provides clear checkpoints for stakeholder review, while the CSS custom properties approach ensures design changes propagate consistently across the entire application. The result is a user experience that stands out in crowded markets, converts visitors to customers, and maintains quality as the product evolves.