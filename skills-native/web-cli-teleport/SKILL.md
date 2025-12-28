---
name: web-cli-teleport
description: Guide users on when to use Claude Code Web vs CLI and seamlessly teleport sessions between environments
---

## When to Use This Skill

- **Tool Usage**: When you need to execute specific tools, lookup reference materials, or run automation pipelines
- **Reference Lookup**: When you need to access documented patterns, best practices, or technical specifications
- **Automation Needs**: When you need to run standardized workflows or pipeline processes

## When NOT to Use This Skill

- **Manual Processes**: Avoid when manual intervention is more appropriate than automated tools
- **Non-Standard Tools**: Do not use when tools are deprecated, unsupported, or outside standard toolkit

## Success Criteria

- **Tool Executed Correctly**: Verify tool runs without errors and produces expected output
- **Reference Accurate**: Confirm reference material is current and applicable
- **Pipeline Complete**: Ensure automation pipeline completes all stages successfully

## Edge Cases

- **Tool Unavailable**: Handle scenarios where required tool is not installed or accessible
- **Outdated References**: Detect when reference material is obsolete or superseded
- **Pipeline Failures**: Recover gracefully from mid-pipeline failures with clear error messages

## Guardrails

- **NEVER use deprecated tools**: Always verify tool versions and support status before execution
- **ALWAYS verify outputs**: Validate tool outputs match expected format and content
- **ALWAYS check health**: Run tool health checks before critical operations

## Evidence-Based Validation

- **Tool Health Checks**: Execute diagnostic commands to verify tool functionality before use
- **Output Validation**: Compare actual outputs against expected schemas or patterns
- **Pipeline Monitoring**: Track pipeline execution metrics and success rates

# Web-CLI Teleport Guide

## Purpose
Help users choose the optimal Claude Code interface (Web vs CLI) and seamlessly teleport sessions between environments for maximum productivity.

## Specialist Agent

I am a workflow optimization specialist with expertise in:
- Claude Code Web and CLI capabilities and limitations
- Session state management and teleportation
- Task complexity analysis and interface selection
- Context window optimization for different interfaces
- Mobile and desktop workflow integration

### Methodology (Program-of-Thought Pattern)

1. **Analyze Task Characteristics**: Determine complexity, iteration needs, back-and-forth
2. **Recommend Interface**: Choose Web, CLI, or hybrid approach
3. **Set Up Session**: Initialize in optimal environment
4. **Monitor Progress**: Track if interface switch needed
5. **Facilitate Teleport**: Guide seamless session handoff when beneficial

### Decision Matrix: Web vs CLI

**Use Claude Code Web When**:
- ✅ Well-defined, one-off tasks (1-3 interactions expected)
- ✅ Simple changes: translations, styling, config updates
- ✅ Away from development machine (mobile, other computer)
- ✅ Want to review/approve before applying locally
- ✅ Collaborative review needed before merging
- ✅ Quick fixes during meetings or on-the-go
- ✅ Creating PRs without local checkout

**Use Claude Code CLI When**:
- ✅ Complex, iterative development (5+ interactions)
- ✅ Debugging requiring multiple attempts
- ✅ Large refactoring across multiple files
- ✅ Need inline diffs and VS Code integration
- ✅ Local testing and running required
- ✅ Working with local databases or services
- ✅ Need full file tree visibility and exploration

**Hybrid Approach (Start Web, Teleport to CLI)**:
- ✅ Initial exploration and planning on mobile
- ✅ Review progress on web, continue implementation locally
- ✅ Quick start on web, complex debugging on CLI
- ✅ Collaborative approval on web, local refinement on CLI

### Web Capabilities

**Strengths**:
- No local setup required
- Works on iOS app (not Android yet)
- GitHub integration for PRs
- Notifications when tasks complete
- Sandboxed cloud execution
- Quick context switching between repositories

**Limitations**:
- Cannot see inline diffs (only final PR diffs)
- Less interactive file exploration
- Limited terminal access
- No local service integration
- Fixed network isolation policies

### CLI Capabilities

**Strengths**:
- Full file system access and exploration
- Inline diffs for every change
- VS Code integration
- Local testing and debugging
- Custom sandbox configuration
- Background task monitoring
- Full terminal control

**Limitations**:
- Requires local setup
- Desktop/laptop only
- More permission prompts without sandbox
- Context switches cost more

### Teleport Protocol

**From Web to CLI**:
1. Complete task on web or reach handoff point
2. Click "Open in CLI" button
3. Copy teleport command: `claude --teleport <session-id>`
4. Ensure clean git working directory locally
5. Run teleport command in local terminal
6. Full session history loaded (~50% context window)
7. Continue work with full CLI capabilities

**Benefits of Teleporting**:
- Preserves entire conversation history
- Maintains context and decisions
- No need to repeat requirements
- Seamless continuation of work
- Can switch back to web for final PR review

**Best Practices**:
- Start small tasks on web for quick wins
- Teleport when complexity increases
- Use web for final PR review and approval
- Clean git state before teleporting
- Verify context loaded correctly (check context %)

### Workflow Patterns

**Pattern 1: Mobile Planning → Desktop Implementation**:
```
[Mobile/Web] Define requirements and initial approach
[Mobile/Web] Let Claude Code explore and plan
[Teleport] Continue on desktop CLI
[CLI] Implement with full tooling
[CLI] Test and debug locally
[Web] Create PR and review
```

**Pattern 2: Quick Fix Anywhere**:
```
[Web] Make simple change (translation, config, style)
[Web] Review diff in PR
[Web] Merge if good OR teleport if issues found
```

**Pattern 3: Complex Feature with Reviews**:
```
[CLI] Initial implementation and testing
[CLI] Create PR when ready
[Web/Mobile] Review PR on the go
[Teleport if needed] Make revisions on desktop
[Web] Final approval and merge
```

## Input Contract

```yaml
task_description: string
task_complexity: simple | moderate | complex
iteration_expected: low | medium | high
current_location: desktop | mobile | away
has_local_environment: boolean
needs_testing: boolean
needs_debugging: boolean
```

## Output Contract

```yaml
recommendation:
  interface: web | cli | hybrid
  reasoning: string
  workflow: array[steps]
  teleport_points: array[string] (when to switch interfaces)

setup_instructions:
  web_url: string (if web recommended)
  cli_commands: array[string] (if CLI recommended)
  teleport_command: string (if hybrid)

optimization_tips:
  time_savings: string
  context_preservation: string
  best_practices: array[string]
```

## Integration Points

- **Cascades**: Pre-step for task planning workflows
- **Commands**: `/web-or-cli`, `/teleport-session`
- **Other Skills**: Works with interactive-planner, task-orchestrator

## Usage Examples

**Quick Decision**:
```
I need to translate the landing page to Japanese. Should I use web or CLI?
```

**Complex Task Planning**:
```
Use web-cli-teleport skill to plan approach for implementing new authentication system with OAuth2
```

**Mid-Task Switch**:
```
I started this on Claude Code Web but it's getting complex. Help me teleport to CLI and continue.
```

## Common Scenarios

**Scenario 1: On Mobile, Need Quick Fix**:
- Recommendation: Use Web
- Create PR directly from web
- Review and merge on mobile

**Scenario 2: Complex Refactoring**:
- Recommendation: Use CLI
- Need inline diffs and local testing
- Multiple iterations expected

**Scenario 3: Started Simple, Got Complex**:
- Started on Web for "simple" task
- Discovered complexity during implementation
- Teleport to CLI with full context
- Complete complex parts locally
- Return to web for PR review

**Scenario 4: Team Collaboration**:
- Use Web for initial work
- Create PR for team review
- Teammates review on web
- Teleport to CLI if changes needed
- Push updates to PR

## Failure Modes & Mitigations

- **Dirty git state blocks teleport**: Stash or commit local changes first
- **Context too large to teleport**: Start fresh, reference PR for context
- **Web limitations discovered mid-task**: Teleport immediately, don't struggle
- **Mobile notifications not working**: Enable in iOS app settings
- **PR diffs not showing**: Refresh page or open PR directly on GitHub

## Validation Checklist

- [ ] Task complexity accurately assessed
- [ ] Interface recommendation matches task needs
- [ ] Teleport points clearly identified
- [ ] User knows how to switch interfaces
- [ ] Git state prepared for teleporting
- [ ] Notifications configured if needed
- [ ] Context preservation verified

## Neural Training Integration

```yaml
training:
  pattern: adaptive
  feedback_collection: true
  success_metrics:
    - task_completion_time
    - interface_switches_needed
    - user_satisfaction
    - context_preservation_quality
```

## Core Principles

### 1. Context Preservation Over Interface Consistency
The teleport system prioritizes maintaining conversation history and decision context over forcing users to stay in one interface. A 50% context window load during teleportation is vastly superior to starting fresh with 0% context. This principle recognizes that continuity of thought matters more than tool familiarity, especially when complexity escalates mid-task.

### 2. Mobile-First Planning, Desktop-First Execution
Effective development workflows separate thinking from doing. Mobile devices excel at async planning, requirement gathering, and progress review due to notification systems and portability. Desktop environments with full IDE integration excel at iterative implementation, debugging, and local testing. The skill treats these as complementary rather than competitive, optimizing for the strengths of each environment.

### 3. Complexity-Triggered Interface Switching
Static interface recommendations fail because task complexity reveals itself during execution, not planning. The skill designs for mid-stream transitions, providing clear signals for when to teleport and ensuring the teleportation mechanism is friction-free. This accepts that initial assessments are probabilistic and builds in escape hatches when predictions fail.

----------|--------------|------------------|
| **Forcing CLI for all "serious" work** | Dismisses valid web use cases like quick fixes, mobile access, and collaborative PR review. Creates unnecessary friction for tasks that don't need full local tooling. | Use decision matrix: complexity, iteration count, local testing needs, current location. Web handles 1-3 interaction tasks efficiently. |
| **Starting fresh instead of teleporting** | Loses 50% context window worth of decisions, requirements, and exploratory work. Forces re-explanation of nuances already established. Wastes time rebuilding shared understanding. | Always use teleport command when switching. Verify context % loaded. Continue conversation rather than restart. |
| **Teleporting with dirty git state** | Blocks teleport operation, requires cleanup, causes confusion about what changes belong to current task vs previous work. Risks accidental commits of unrelated changes. | Verify git status shows clean working directory before teleport. Stash or commit local changes first. Use branch per feature to isolate work. |

---

## Conclusion

The Web-CLI Teleport skill addresses a fundamental tension in modern development: the need for both mobility and power. Traditional tooling forces binary choices between environments, losing context during transitions and creating artificial barriers based on location rather than task requirements.

This skill's innovation lies in treating interface selection as a continuous optimization problem rather than an upfront commitment. By providing seamless teleportation with context preservation, it enables developers to start work anywhere, recognize complexity shifts in real-time, and transition to appropriate tooling without penalty. The decision matrix reduces cognitive load by encoding environment-specific tradeoffs into clear criteria, while the teleport protocol ensures conversations remain continuous across physical and virtual boundaries.

The result is a workflow that respects both human mobility patterns and technical complexity curves, allowing planning on mobile during commute, exploratory work on web during meetings, and focused implementation on desktop with full tooling, all within a single conversational thread that accumulates rather than resets context.