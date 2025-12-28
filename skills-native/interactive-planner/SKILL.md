---
name: interactive-planner
description: Use Claude Code's interactive question tool to gather comprehensive requirements through structured multi-select questions
---

through structured multi-select questions
- planning
- requirements
- questions
- scoping
- interactive


**Quick Reference**:
- Max 4 questions per batch
- Use multiSelect for non-exclusive choices
- "Other" option always available
- Plan 5-8 batches for complex projects

**Pro Tips**:
- Better to ask more questions upfront than iterate later
- Use in Planning Mode for automatic activation
- Combine with open discussion for best results
- Save complex projects for CLI, simple tasks for Web
## Core Principles

Interactive Planning operates on 3 fundamental principles:

### Principle 1: Question-Driven Requirements Elicitation
Every project begins with structured, multi-dimensional questions that systematically explore scope, architecture, features, quality, and constraints. This prevents assumption-driven planning and ensures user preferences are captured explicitly.

In practice:
- 5-10 multi-select questions covering critical decision points (framework, database, auth, deployment, testing)
- Questions designed to be clear, non-overlapping, with 2-4 mutually exclusive options
- Multi-batch strategy for complex projects (20-30 questions across 5-8 batches)

### Principle 2: Progressive Refinement Through Batches
Requirements gathering proceeds in waves from broad to specific, with each batch building on previous answers. This balances comprehensiveness with user experience, avoiding overwhelming users while ensuring complete coverage.

In practice:
- Batch 1: Project type, goal, complexity (high-level scope)
- Batch 2: Tech stack, architecture (technical foundations)
- Batch 3: Core features, priorities (functionality)
- Batch 4: Quality, testing, documentation (non-functional requirements)
- Batch 5+: Domain-specific details (context-dependent refinement)

### Principle 3: Synthesis Into Actionable Specifications
Gathered answers are transformed into concrete, validated specifications that directly inform downstream planning and execution. This ensures interactive questions produce tangible value rather than surface-level data collection.

In practice:
- Requirements document exports all selections with explanations
- Conflicts and gaps are identified and resolved before proceeding
- User confirmation required before moving to execution phase
- Specifications include explicit technical decisions (no lingering ambiguities)

## Common Anti-Patterns

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| **Assumption-Driven Planning** | Proceeding with technical choices (framework, database, cloud provider) without explicit user input leads to misaligned implementations and rework | Use interactive questions to gather ALL critical decisions upfront - NEVER assume user preferences |
| **Question Overload** | Asking >15 questions in a single batch or poorly organized questions overwhelms users and reduces response quality | Limit to 4 questions per batch, use 5-8 batches for complex projects, group related questions into coherent phases |
| **Overlapping Options** | Question options that aren't mutually exclusive or cover the same concept confuse users and produce ambiguous requirements | Design orthogonal question dimensions - each option must be distinct, use multiSelect when choices aren't exclusive |

## Conclusion

Interactive Planner provides a structured framework for gathering comprehensive requirements through multi-select questions that systematically explore all critical project dimensions. By enforcing question-driven elicitation, progressive refinement through batches, and synthesis into actionable specifications, this skill ensures projects begin with clear, validated requirements rather than assumptions.

Use this skill when starting new projects with vague or underspecified requirements, when technical stack decisions need user input, or when planning complex features where preferences are unknown. The multi-batch workflow (4 questions per batch across 5-8 batches) balances thoroughness with user experience, while the guardrails prevent common pitfalls like assumption-driven planning, question overload, and ambiguous options. The result is a complete requirements document with explicit technical decisions ready for downstream planning and execution.

## Anti-Patterns

| Anti-Pattern | Why It Fails | Correct Approach |
|--------------|--------------|------------------|
| **Asking too few questions (<10 total)** | Insufficient coverage leaves critical decisions unstated. Common gaps: testing strategy, deployment target, authentication method, scalability requirements. Under-specified requirements lead to rework when user reveals missing constraints mid-implementation. | Plan 20-30 questions across 5-7 batches for complex projects. Cover all decision dimensions: functionality, architecture, UX, quality, constraints. Better to gather comprehensive requirements upfront than iterate on wrong assumptions. Use multi-select to capture nuanced choices efficiently. |
| **Non-orthogonal options that overlap** | Options like "REST API" and "Backend Service" aren't mutually exclusive - confusion about which to choose. Overlapping options signal unclear question design and produce ambiguous responses that don't clarify actual intent. | Design questions with distinct, non-overlapping options. Each option should be clearly different from others. Good: "REST API", "GraphQL", "WebSockets", "Database Direct". Bad: "API Service", "Backend API", "RESTful Service" (all mean similar things). Test: can user pick multiple without contradiction? |
| **Overwhelming users with 40+ questions in one batch** | Tool constraint is 4 questions per call, but even 8-10 batches (32-40 questions) causes fatigue. Users rush through later questions, provide low-quality responses, or abandon the process. Diminishing returns after 30 questions. | Cap at 20-30 questions (5-7 batches) for complex projects, 12-16 (3-4 batches) for moderate scope. Prioritize highest-impact questions. For extremely complex projects, split into multi-session gathering or supplement with open discussion. Quality over exhaustive coverage. |

---

## Conclusion

Interactive Planner transforms requirement gathering from unstructured conversation into systematic multi-dimensional scoping through Claude Code's AskUserQuestion tool. This structured approach converts vague project ideas into concrete specifications by making technical choices explicit through strategic multi-select questions organized into coherent decision categories. The skill's value lies in preventing assumption debt - eliminating hidden technical choices that cause rework when user expectations diverge from agent decisions.

The power emerges from three integrated patterns: structured multi-select questions eliminate implicit assumptions by forcing explicit technical choices; categorical batching (scope, architecture, features, quality, constraints) creates cognitive flow that helps users think systematically; and progressive refinement from broad to specific enables adaptive question paths where early answers guide later technical specificity. Together, these patterns enable comprehensive requirement gathering in 20-30 well-designed questions spanning 5-7 batches.

Successful implementation requires balancing thoroughness with user experience. Too few questions leave critical gaps; too many cause fatigue. The sweet spot: 20-30 questions for complex projects, 12-16 for moderate scope, organized into decision categories that minimize context switching. Master question design (clear, specific, non-overlapping options with helpful descriptions), leverage multiSelect for non-exclusive choices, and maintain progressive refinement from project scope to technical details. This systematic approach transforms ambiguous project requests into actionable specifications that align agent implementation with user intent from the start.