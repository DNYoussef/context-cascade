---
name: ai-dev-orchestration
description: Meta-orchestrator for AI-assisted app development with behavioral guardrails and prompt templates. 5-phase SOP - Product Framing (planner) -> Setup & Foundations (system-architect) -> Feature Development Loop (coder + tester + reviewer) -> Testing & Refactors (tester + coder) -> Deployment (cicd-engineer). Wraps three-loop system with AI-specific safety patterns.
---

# AI-Assisted App Development Orchestration

## Phase 0: Expertise Loading

Before orchestrating AI development:

1. **Detect Domain**: Identify app type and tech stack
2. **Check Expertise**: Look for `.claude/expertise/ai-dev-${stack}.yaml`
3. **Load Context**: If exists, load guardrail patterns and successful prompts
4. **Apply Configuration**: Use expertise for development orchestration

**Purpose**: Ship reliable apps with AI coding tools while minimizing bugs, rework, and chaos

**Core Principle**: Treat AI as a junior dev with superpowers inside a structured pipeline. Real leverage comes from tight specs, clean context, and strong foundations.

**Timeline**: Varies by complexity (Product Framing 30-60min, Foundations 1-2hrs, Per-Feature 1-3hrs, Testing 30-90min, Deployment 15-30min)

**Integration**: Wraps feature-dev-complete, sparc-methodology, cicd-intelligent-recovery with AI-specific guardrails



## When to Use This Skill

Activate this skill when:
- Building apps with AI coding tools (Cursor, Claude Code, Lovable, Bolt)
- Need to prevent AI coding chaos and "theater implementations"
- Want systematic approach to AI-assisted development
- Building greenfield projects (web, mobile, internal tools)
- Small teams or solo builders using AI agents
- Need AI-safe guardrails (scope limiting, context management, testing gates)

**DO NOT** use this skill for:
- Traditional development without AI assistance (use feature-dev-complete)
- Quick scripts or throwaway code (too much process)
- Well-understood repetitive tasks (use existing patterns)
- Emergency hotfixes (skip structured workflow)



## Input Contract

```yaml
input:
  product:
    name: string (required)
    description: string (required)  # 1-2 sentence "who + what outcome"
    target_user: string (optional)  # Narrow customer segment
    differentiators: array[string] (optional)  # How you differ from competitors

  requirements:
    must_have_features: array[string] (1-2 core features for MVP)
    nice_to_have: array[string]
    constraints:
      technical: array[string]  # Required stack, frameworks
      timeline: string
      budget: string

  options:
    run_product_framing: boolean (default: true)  # Skip if already validated
    auto_test: boolean (default: true)  # Run tests after each feature
    manual_review: boolean (default: true)  # Human approval gates
    deployment_target: enum[staging, production] (default: staging)
```

## Output Contract

```yaml
output:
  product_frame:  # Phase 0 output
    app_one_pager: path  # docs/app-one-pager.md
    persona_snapshot: object
    validation_summary: string
    monetization_hypothesis: string

  foundations:  # Phase 1 output
    tech_stack: object
      frontend: string
      backend: string
      database: string
      auth: string
      payments: string (if applicable)
      deployment: string
    mvp_checklist: array[object]
      task: string
      status: enum[pending, in_progress, completed]
    repo_url: string
    base_app_running: boolean

  features:  # Phase 2 output (per feature)
    feature_specs: array[path]  # docs/features/*.md
    implementations: array[object]
      feature_id: string
      files_changed: array[string]
      test_coverage: number (percentage)
      status: enum[accepted, rejected, rolled_back]
    total_features_completed: number

  quality:  # Phase 3 output
    bugs_fixed: number
    refactorings_applied: number
    test_coverage_overall: number

  deployment:  # Phase 4 output
    deployment_url: string
    monitoring_dashboard: string
    health_check_url: string

  integration:
    memory_namespace: string  # ai-dev/{project-name}
    compliance_rate: number  # % of features following framework
```



## SOP Phase 1: Setup & Foundations (1-2 hrs)

**Objective**: Choose stack, create repo, define MVP, implement foundations BEFORE feature chaos

**Agent**: `system-architect`

**Prompt for Tech Stack Selection**:
```javascript
await Task("Tech Stack Architect", `
Choose technology stack for AI-assisted app development.

Product Context: <app-one-pager-summary>
Requirements: <functional + non-functional>
Constraints: <technical-constraints>

Decision Criteria:
1. **AI Tool Compatibility**: Works well with Cursor/Claude Code (export capability, ownership)
2. **Stack you can own**: Prefer stacks you can export (Lovable/Bolt with GitHub export)
3. **Proven patterns**: Battle-tested combinations
4. **Team expertise**: Match team skills or learning goals

Stack Decisions (with justification):

### Frontend
- **Framework**: <Next.js/React, Expo React Native, Vue, etc.>
- **Rationale**: <why this choice>

### Backend
- **Platform**: <Next API routes, Supabase, Convex, Express, FastAPI, etc.>
- **Rationale**: <why this choice>

### Database
- **Choice**: <Supabase Postgres, Convex KV, MongoDB, etc.>
- **Rationale**: <why this choice>

### Auth
- **Provider**: <Supabase Auth, Clerk, Auth0, platform-built, etc.>
- **Rationale**: <why this choice>

### Payments (if applicable)
- **Provider**: <Stripe, RevenueCat, etc.>
- **Rationale**: <why this choice>

### Deployment
- **Platform**: <Vercel, Netlify, Render, app stores, etc.>
- **Rationale**: <why this choice>

Save to: docs/tech-stack-decision.md

Generate MVP Checklist:
1. Setup app + basic layout
2. DB + auth (only if needed for MVP)
3. Core feature A (must-have)
4. Core feature B (must-have, if applicable)
5. Payments / subscription (only if revenue-critical)
6. Basic deployment

Save to: docs/mvp-checklist.md
`, "system-architect");
```

**Prompt for Repository & Base App Setup**:
```javascript
await Task("Repository Scaffolder", `
Initialize repository and create base app.

Tech Stack: <from tech-stack-decision.md>

Steps:
1. Initialize git repo
   git init
   git remote add origin <repo-url>

2. Scaffold base app (using CLI or AI coding agent with SINGLE, CLEAR prompt):
   Prompt: "Create a barebones [framework] app with a simple home screen and a health check route."

   Example for Next.js:
   npx create-next-app@latest <app-name> --typescript --tailwind --app --no-src-dir

3. Verify can run locally:
   - npm install
   - npm run dev
   - Open http://localhost:3000
   - See simple landing page
   - Hit test API route (/api/health)

4. Create .gitignore with:
   - node_modules/
   - .env*
   - .next/
   - build/
   - dist/

5. Create initial commit:
   git add .
   git commit -m "Initial commit: Barebones [framework] app

   - Simple home screen
   - Health check route /api/health
   - Basic project structure

   🤖 Generated with [Claude Code](https://claude.com/claude-code)

   Co-Authored-By: Claude <noreply@anthropic.com>"

Report:
- [ ] Repo initialized
- [ ] Base app created
- [ ] Runs locally
- [ ] Landing page visible
- [ ] Health check route works
- [ ] Initial commit created
`, "system-architect");
```

**Prompt for Foundations Implementation**:
```javascript
await Task("Foundations Implementer", `
Implement core infrastructure BEFORE adding features.

Use Foundation Prompt Template (.claude/skills/ai-dev-orchestration/.artifacts/Foundation-Prompt-Template.md)

Foundations to implement:
1. Frontend shell (basic layout, navigation)
2. Backend scaffold (routes, handlers)
3. Database schema (only tables needed for MVP)
4. Auth (signup/login/logout) - ONLY if needed for MVP
5. Payments (if revenue-critical for MVP)
6. External APIs (if needed)

For EACH foundation item:
1. Open a FRESH AI chat (Cursor/Claude Code)
2. Use Foundation Prompt Template:



3. Apply code changes via tool's review mechanism (diff/preview)
4. MANUALLY TEST:
   - DB migrations and basic CRUD
   - Auth flows (signup, login, logout)
   - Payment sandbox flow (if integrated)

Report per foundation:
- [ ] Plan reviewed and approved
- [ ] Implementation complete
- [ ] Manual tests passing
- [ ] Committed with clear message

Store decisions in Memory-MCP:
- Database schema rationale
- Auth flow design
- Payment integration approach
`, "system-architect");
```

**MCP Tools Used**:
- `mcp__memory-mcp__memory_store`

**Success Criteria**:
- Tech stack chosen with justification
- MVP checklist defined (1-2 must-have features)
- Repo created and base app running
- Foundations implemented (DB, auth, payments if needed)
- All foundations manually tested
- Decisions stored in Memory-MCP



## SOP Phase 3: Testing, Bugs, & Refactors (30-90 min)

**Objective**: Keep code healthy while moving fast

**Agents**: `tester` + `coder`

**Bug Hygiene Rule**: Never let more than 5 bugs linger per feature

**Prompt for Bug Fixes**:
```javascript
await Task("Bug Fixer", `
Fix bug with AI coding tool in FRESH chat.

Bug Description: <error-messages / failing-behavior>
Relevant Code: <snippets>

Instructions:
1. Open FRESH AI chat
2. Provide:
   - Error messages / failing behavior
   - Relevant code snippets
   - Clear constraint: "Fix only what is necessary to resolve this bug. Do not touch <X, Y, Z>."
3. Apply fix
4. Test again

If bug cascades into new bugs:
- Consider rolling back
- Re-implement more cleanly

Report:
- [ ] Bug fixed
- [ ] Tests passing
- [ ] No new bugs introduced
- [ ] Committed with message: "fix: <bug-description>"
`, "coder");
```

**Prompt for Refactors**:
```javascript
await Task("Refactorer", `
Apply refactoring with AI coding tool.

Refactor Type: <renaming / extraction / simplification>
Scope: <files/components affected>

Use AI for:
- Renaming components/functions across codebase
- Extracting shared components/hooks
- Simplifying complex logic

ALWAYS:
- Scope the refactor clearly
- Prevent database schema or auth changes unless explicitly requested
- Test after refactoring

Report:
- [ ] Refactor applied
- [ ] Tests passing
- [ ] No unintended changes
- [ ] Committed with message: "refactor: <what-changed>"
`, "coder");
```

**Success Criteria**:
- Bugs fixed promptly (within 1-2 feature cycles)
- Refactorings scoped and tested
- No accumulation of technical debt
- Code quality maintained



## Operational Rules of Thumb (Behavioral)

These encode "unintuitive" insights into simple rules:

### Rule 1: Never ask AI to "build my whole app"
**Always scope to**: one foundation piece OR one feature

### Rule 2: No feature without a user journey
**If you can't write**: "User does A → B → C → sees D", you're not ready

### Rule 3: Every major feature prompt must include a "do not touch" list
**Protect by default**: DB schema, auth, payments

### Rule 4: One chat = one feature/foundation
**When done**: reset context, start fresh for next task

### Rule 5: Architecture choices are sticky
**Don't pick casually**: DB/auth/stack decisions are long-term

### Rule 6: Manual testing is non-optional, especially early
**You can add automated tests later**: first understand how things fail

### Rule 7: AI is a factory, you are the orchestrator
**Your main job**: design good specs, run the pipeline, decide pass/fail



## Integration with Three-Loop System

**AI Dev Orchestration** wraps the three-loop system:

```
[AI Dev Orchestration]
    │
    ├─ Phase 0: Product Framing → planner
    │
    ├─ Phase 1: Foundations → system-architect
    │   └─ Uses: sparc-methodology (architecture phase)
    │
    ├─ Phase 2: Feature Loop → coder + tester + reviewer
    │   └─ Uses: feature-dev-complete (wrapped with AI guardrails)
    │   └─ Uses: parallel-swarm-implementation (Loop 2)
    │
    ├─ Phase 3: Testing & Refactors → tester + coder
    │   └─ Uses: smart-bug-fix (intelligent debugging)
    │   └─ Uses: functionality-audit (sandbox validation)
    │
    └─ Phase 4: Deployment → cicd-engineer
        └─ Uses: cicd-intelligent-recovery (Loop 3)
```

**Unique Value of AI Dev Orchestration**:
- **Prompt Templates**: Feature Prompt Framework, Foundation Prompt Template
- **Behavioral Rules**: Fresh context, do not touch lists, manual testing gates
- **Context Management**: Ephemeral chat history, persistent memory in code/docs
- **Scope Limiting**: One feature per chat, guardrails against feature creep

----|-------------|----------------|
| Phase 0: Product Framing | 30-60 min | App One-Pager complete |
| Phase 1: Foundations | 1-2 hrs | Base app running + foundations tested |
| Phase 2: Per-Feature | 1-3 hrs | Feature ACCEPTED with tests passing |
| Phase 3: Testing | 30-90 min | Bugs fixed, refactors scoped |
| Phase 4: Deployment | 15-30 min | Deployed + monitoring active |

**Quality Targets**:
- Bug accumulation: ≤5 bugs per feature
- Test coverage: ≥80% (manual initially, automated later)
- Rollback rate: ≤20% (80% features accepted first try)
- Deployment success: 100% (no broken deploys)



## Artifacts Reference

1. **Feature-Prompt-Framework.md**: Reusable template for feature specs
2. **Foundation-Prompt-Template.md**: Reusable template for foundations (DB, auth, etc.)
3. **Compliance-Checklist.md**: Per-feature validation checklist
4. **Do-Not-Touch-Template.md**: Template for constraint lists



**END OF AI-DEV-ORCHESTRATION SKILL SOP**



## !! SKILL COMPLETION VERIFICATION (MANDATORY) !!

**After invoking this skill, you MUST complete ALL items below before proceeding:**

### Completion Checklist

- [ ] **Agent Spawning**: Did you spawn at least 1 agent via Task()?
  - Example: `Task("Agent Name", "Task description", "agent-type-from-registry")`

- [ ] **Agent Registry Validation**: Is your agent from the registry?
  - Registry location: `claude-code-plugins/ruv-sparc-three-loop-system/agents/`
  - Valid categories: delivery, foundry, operations, orchestration, platforms, quality, research, security, specialists, tooling
  - NOT valid: Made-up agent names

- [ ] **TodoWrite Called**: Did you call TodoWrite with 5+ todos?
  - Example: `TodoWrite({ todos: [8-10 items covering all work] })`

- [ ] **Work Delegation**: Did you delegate to agents (not do work yourself)?
  - CORRECT: Agents do the implementation via Task()
  - WRONG: You write the code directly after reading skill

### Correct Pattern After Skill Invocation

```javascript
// After Skill("<skill-name>") is invoked:
[Single Message - ALL in parallel]:
  Task("Agent 1", "Description of task 1...", "agent-type-1")
  Task("Agent 2", "Description of task 2...", "agent-type-2")
  Task("Agent 3", "Description of task 3...", "agent-type-3")
  TodoWrite({ todos: [
    {content: "Task 1 description", status: "in_progress", activeForm: "Working on task 1"},
    {content: "Task 2 description", status: "pending", activeForm: "Working on task 2"},
    {content: "Task 3 description", status: "pending", activeForm: "Working on task 3"},
  ]})
```

### Wrong Pattern (DO NOT DO THIS)

```javascript
// WRONG - Reading skill and then doing work yourself:
Skill("<skill-name>")
// Then you write all the code yourself without Task() calls
// This defeats the purpose of the skill system!
```

**The skill is NOT complete until all checklist items are checked.**

-----------|---------|----------|
| **"Build my whole app" prompts** | AI attempts to implement everything in one massive change, resulting in scope creep, missed requirements, and untested code. | Break into Phase 1 (foundations) and Phase 2 (per-feature loops). One feature per chat, 1-3 hours max per iteration. |
| **Reusing AI chat context across features** | Context pollution causes AI to make assumptions from previous work, touching files outside current scope. | Open fresh AI chat for every feature or foundation. No exceptions. Reset context to reset AI assumptions. |
| **Skipping manual testing gates** | Theater implementations (code that looks correct but doesn't work) reach production because automated tests pass but functionality fails. | Manual test EVERY feature against user journey spec before accepting. No "Accept" without human verification. |
| **Vague "do not touch" lists** | AI breaks auth, modifies DB schema, or changes payment logic because constraints weren't explicit. | Include exhaustive "DO NOT TOUCH" list in every prompt: specific tables, routes, components, flows. Default to restrictive. |
| **Feature creep in single chat** | AI starts with "implement login" and ends with "redesigned entire auth system + password reset + 2FA". | Feature Prompt Framework defines EXACT user journey (7-10 steps). Reject ANY changes beyond that scope. |

## Conclusion

AI-Assisted App Development Orchestration bridges the gap between AI coding tools' raw power and production-quality software delivery. By treating AI as a constrained factory inside a structured 5-phase pipeline (Product Framing, Foundations, Feature Loop, Testing, Deployment), teams ship reliable apps 3-5x faster than traditional development while maintaining quality through behavioral guardrails.

The skill's unique value lies not in the technical stack decisions or coding speed, but in the orchestration patterns: fresh context per feature, "do not touch" lists, manual testing gates, and ephemeral chat history combined with persistent architectural memory. These patterns prevent the chaos typical of AI-assisted development (scope creep, theater implementations, context pollution) while preserving the leverage (rapid prototyping, automation of repetitive tasks).

Use this skill when building greenfield applications with AI coding tools (Cursor, Claude Code, Lovable), especially for small teams or solo builders who need systematic quality controls without heavyweight processes. The 5-phase structure scales from MVP (1-2 must-have features) to production (iterative feature additions with deployment monitoring), making it ideal for both product validation and sustained development. The key takeaway: AI accelerates execution, but humans must orchestrate strategy, enforce boundaries, and validate outcomes.