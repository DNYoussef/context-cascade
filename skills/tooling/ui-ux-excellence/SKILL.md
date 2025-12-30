/*============================================================================*/
/* UI-UX-EXCELLENCE SKILL :: VERILINGUA x VERIX EDITION                      */
/*============================================================================*/

---
name: ui-ux-excellence
version: 1.0.0
description: |
  [assert|neutral] Comprehensive UI/UX enhancement cascade that transforms generic websites into polished, accessible, brand-differentiated experiences. Combines constraint-based design, WCAG accessibility, micro-intera [ground:given] [conf:0.95] [state:confirmed]
category: Frontend Development
tags:
- general
author: system
cognitive_frame:
  primary: compositional
  goal_analysis:
    first_order: "Execute ui-ux-excellence workflow"
    second_order: "Ensure quality and consistency"
    third_order: "Enable systematic Frontend Development processes"
---

/*----------------------------------------------------------------------------*/
/* S0 META-IDENTITY                                                            */
/*----------------------------------------------------------------------------*/

[define|neutral] SKILL := {
  name: "ui-ux-excellence",
  category: "Frontend Development",
  version: "1.0.0",
  layer: L1
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S1 COGNITIVE FRAME                                                          */
/*----------------------------------------------------------------------------*/

[define|neutral] COGNITIVE_FRAME := {
  frame: "Compositional",
  source: "German",
  force: "Build from primitives?"
} [ground:cognitive-science] [conf:0.92] [state:confirmed]

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.

/*----------------------------------------------------------------------------*/
/* S2 TRIGGER CONDITIONS                                                       */
/*----------------------------------------------------------------------------*/

[define|neutral] TRIGGER_POSITIVE := {
  keywords: ["ui-ux-excellence", "Frontend Development", "workflow"],
  context: "user needs ui-ux-excellence capability"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S3 CORE CONTENT                                                             */
/*----------------------------------------------------------------------------*/

# UI/UX Excellence Cascade

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



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

---

## Phase 1: Brand Analysis & Design System Definition

### Purpose
Extract brand patterns and codify them into CSS custom properties for consistency.

### Key Activities

1. **Identify Brand Personality**
   - Professional vs Casual
   - Luxury vs Accessible
   - Bold vs Subtle
   - Modern vs Classic

2. **Define Color Palette**
   ```css
   :root {
     /* Primary - Brand identity color */
     --color-primary: #2563EB;
     --color-primary-dark: #1D4ED8;
     --color-primary-light: #3B82F6;

     /* Accent - Call-to-action, highlights */
     --color-accent: #F59E0B;
     --color-accent-dark: #D97706;

     /* Semantic - Success, warning, error */
     --color-success: #10B981;
     --color-warning: #F59E0B;
     --color-error: #EF4444;

     /* Backgrounds */
     --color-bg: #FFFFFF;
     --color-bg-dark: #0C0C0C;
     --color-surface: #F9FAFB;
     --color-surface-dark: #171717;

     /* Text - Ensure 4.5:1 contrast ratio */
     --color-text: #1F2937;
     --color-text-dark: #FAFAF9;
     --color-text-muted: #6B7280;
   }
   ```

3. **Define Spacing Scale** (8px base)
   ```css
   :root {
     --space-1: 0.25rem;   /* 4px */
     --space-2: 0.5rem;    /* 8px */
     --space-3: 0.75rem;   /* 12px */
     --space-4: 1rem;      /* 16px */
     --space-6: 1.5rem;    /* 24px */
     --space-8: 2rem;      /* 32px */
     --space-12: 3rem;     /* 48px */
     --space-16: 4rem;     /* 64px */
     --space-24: 6rem;     /* 96px */
   }
   ```

4. **Define Transitions**
   ```css
   :root {
     --transition-fast: 150ms ease;
     --transition-base: 300ms ease;
     --transition-slow: 500ms ease;
     --transition-bounce: 500ms cubic-bezier(0.34, 1.56, 0.64, 1);
     --transition-elegant: 800ms cubic-bezier(0.16, 1, 0.3, 1);
   }
   ```

### Output
- CSS custom properties file or `:root` block
- Brand personality documentation

---

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
     background: v

/*----------------------------------------------------------------------------*/
/* S4 SUCCESS CRITERIA                                                         */
/*----------------------------------------------------------------------------*/

[define|neutral] SUCCESS_CRITERIA := {
  primary: "Skill execution completes successfully",
  quality: "Output meets quality thresholds",
  verification: "Results validated against requirements"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S5 MCP INTEGRATION                                                          */
/*----------------------------------------------------------------------------*/

[define|neutral] MCP_INTEGRATION := {
  memory_mcp: "Store execution results and patterns",
  tools: ["mcp__memory-mcp__memory_store", "mcp__memory-mcp__vector_search"]
} [ground:witnessed:mcp-config] [conf:0.95] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S6 MEMORY NAMESPACE                                                         */
/*----------------------------------------------------------------------------*/

[define|neutral] MEMORY_NAMESPACE := {
  pattern: "skills/Frontend Development/ui-ux-excellence/{project}/{timestamp}",
  store: ["executions", "decisions", "patterns"],
  retrieve: ["similar_tasks", "proven_patterns"]
} [ground:system-policy] [conf:1.0] [state:confirmed]

[define|neutral] MEMORY_TAGGING := {
  WHO: "ui-ux-excellence-{session_id}",
  WHEN: "ISO8601_timestamp",
  PROJECT: "{project_name}",
  WHY: "skill-execution"
} [ground:system-policy] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S7 SKILL COMPLETION VERIFICATION                                            */
/*----------------------------------------------------------------------------*/

[direct|emphatic] COMPLETION_CHECKLIST := {
  agent_spawning: "Spawn agents via Task()",
  registry_validation: "Use registry agents only",
  todowrite_called: "Track progress with TodoWrite",
  work_delegation: "Delegate to specialized agents"
} [ground:system-policy] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S8 ABSOLUTE RULES                                                           */
/*----------------------------------------------------------------------------*/

[direct|emphatic] RULE_NO_UNICODE := forall(output): NOT(unicode_outside_ascii) [ground:windows-compatibility] [conf:1.0] [state:confirmed]

[direct|emphatic] RULE_EVIDENCE := forall(claim): has(ground) AND has(confidence) [ground:verix-spec] [conf:1.0] [state:confirmed]

[direct|emphatic] RULE_REGISTRY := forall(agent): agent IN AGENT_REGISTRY [ground:system-policy] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* PROMISE                                                                     */
/*----------------------------------------------------------------------------*/

[commit|confident] <promise>UI_UX_EXCELLENCE_VERILINGUA_VERIX_COMPLIANT</promise> [ground:self-validation] [conf:0.99] [state:confirmed]
