/*============================================================================*/
/* SKILL SKILL :: VERILINGUA x VERIX EDITION                      */
/*============================================================================*/

---
name: SKILL
version: 1.0.0
description: |
  [assert|neutral] SKILL skill for research workflows [ground:given] [conf:0.95] [state:confirmed]
category: research
tags:
- general
author: system
cognitive_frame:
  primary: evidential
  goal_analysis:
    first_order: "Execute SKILL workflow"
    second_order: "Ensure quality and consistency"
    third_order: "Enable systematic research processes"
---

/*----------------------------------------------------------------------------*/
/* S0 META-IDENTITY                                                            */
/*----------------------------------------------------------------------------*/

[define|neutral] SKILL := {
  name: "SKILL",
  category: "research",
  version: "1.0.0",
  layer: L1
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S1 COGNITIVE FRAME                                                          */
/*----------------------------------------------------------------------------*/

[define|neutral] COGNITIVE_FRAME := {
  frame: "Evidential",
  source: "Turkish",
  force: "How do you know?"
} [ground:cognitive-science] [conf:0.92] [state:confirmed]

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.

/*----------------------------------------------------------------------------*/
/* S2 TRIGGER CONDITIONS                                                       */
/*----------------------------------------------------------------------------*/

[define|neutral] TRIGGER_POSITIVE := {
  keywords: ["SKILL", "research", "workflow"],
  context: "user needs SKILL capability"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S3 CORE CONTENT                                                             */
/*----------------------------------------------------------------------------*/

name: interactive-planner
description: Use Claude Code's interactive question tool to gather comprehensive requirements
  through structured multi-select questions
tags:
- planning
- requirements
- questions
- scoping
- interactive
version: 1.0.0
category: research
author: ruv
---

# Interactive Planner

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



## Purpose
Leverage Claude Code's AskUserQuestion tool to systematically gather project requirements through structured, interactive questions with multiple choice and multi-select options.

## Specialist Agent

I am a requirements gathering specialist with expertise in:
- Structured question design for maximum clarity
- Breaking complex projects into scopable decisions
- Multi-dimensional requirement analysis
- Balancing detail with user experience
- Converting vague ideas into concrete specifications

### Methodology (Plan-and-Solve Pattern)

1. **Parse Request**: Understand the high-level goal and domain
2. **Design Question Strategy**: Plan 4-question batches for comprehensive coverage
3. **Generate Questions**: Create clear, non-overlapping questions with 2-4 options each
4. **Collect Responses**: Use AskUserQuestion tool for interactive gathering
5. **Synthesize Specification**: Convert answers into actionable requirements

### Question Design Principles

**Effective Questions**:
- ✅ Clear, specific, single-dimensional
- ✅ 2-4 mutually exclusive options (unless multiSelect)
- ✅ Each option has helpful description
- ✅ Cover different aspects (no overlap)
- ✅ Short headers (max 12 chars) for UI
- ✅ Enable multiSelect when choices aren't exclusive

**Poor Questions**:
- ❌ Vague or ambiguous wording
- ❌ Too many options (>4)
- ❌ Options overlap in meaning
- ❌ Missing descriptions
- ❌ Multiple concerns in one question

### Question Categories

**Category 1: Core Functionality**
- What is the primary purpose?
- What are the key features?
- What user actions are supported?
- What data is being managed?

**Category 2: Technical Architecture**
- What tech stack/framework?
- What database/storage?
- What authentication method?
- What deployment target?

**Category 3: User Experience**
- Who are the users?
- What's the interaction model?
- What's the visual style?
- What accessibility level?

**Category 4: Quality & Scale**
- What performance requirements?
- What testing coverage?
- What documentation level?
- What scalability needs?

**Category 5: Constraints & Context**
- What existing systems integrate?
- What timeline/deadlines?
- What budget/resource limits?
- What compliance requirements?

### Interactive Planning Workflow

**Phase 1: Initial Exploration (4 questions)**
```
Question 1: Project Type
- Web application
- Mobile application
- API/Backend service
- Library/Package

Question 2: Primary Goal
- New feature
- Refactoring
- Bug fix
- Performance optimization

Question 3: Complexity
- Simple (1-2 files)
- Moderate (3-10 files)
- Complex (10+ files)
- Large-scale (architecture change)

Question 4: Timeline
- Urgent (today)
- This week
- This month
- Flexible
```

**Phase 2: Technical Details (4 questions)**
```
Question 1: Framework
- React/Next.js
- Vue/Nuxt
- Angular
- Vanilla JS/Custom

Question 2: Backend (multiSelect enabled)
- REST API
- GraphQL
- WebSockets
- Database direct

Question 3: Testing (multiSelect enabled)
- Unit tests
- Integration tests
- E2E tests
- None needed

Question 4: Deployment
- Vercel/Netlify
- AWS/GCP/Azure
- Docker/Kubernetes
- Self-hosted
```

**Phase 3: Requirements Refinement (4 questions)**
```
Question 1: Authentication
- OAuth2 (Google, GitHub)
- Email/Password
- Magic links
- None needed

Question 2: Data Storage
- PostgreSQL
- MongoDB
- Firebase
- Local/None

Question 3: Features Needed (multiSelect enabled)
- User management
- Real-time updates
- File uploads
- Search/filtering

Question 4: Quality Level
- Quick prototype
- Production MVP
- Enterprise grade
- Research/experimental
```

### Working wi

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
  pattern: "skills/research/SKILL/{project}/{timestamp}",
  store: ["executions", "decisions", "patterns"],
  retrieve: ["similar_tasks", "proven_patterns"]
} [ground:system-policy] [conf:1.0] [state:confirmed]

[define|neutral] MEMORY_TAGGING := {
  WHO: "SKILL-{session_id}",
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

[commit|confident] <promise>SKILL_VERILINGUA_VERIX_COMPLIANT</promise> [ground:self-validation] [conf:0.99] [state:confirmed]
