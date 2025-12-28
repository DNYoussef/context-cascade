---
name: agent-creator
description: Creates specialized AI agents with optimized system prompts using the official 5-phase SOP methodology (v3.0 adds Phase 0.5 cognitive frame selection), combined with evidence-based prompting techniques and Claude Agent SDK implementation. Use this skill when creating production-ready agents for specific domains, workflows, or tasks requiring consistent high-quality performance with deeply embedded domain knowledge and cognitive frame optimization. Integrates with recursive improvement loop. --- # Agent Creator - Enhanced with 5-Phase SOP Methodology (v3.0) This skill provides the **official comprehensive framework** for creating specialized AI agents, integrating the proven 5-phase methodology (v3.0 adds Phase 0.5 cognitive frame selection) from Desktop .claude-flow with Claude Agent SDK implementation and evidence-based prompting techniques. ## Trigger Keywords **USE WHEN user mentions:** - "create agent", "build agent", "new agent", "design agent" - "agent for [domain]", "specialist agent", "domain exper...
---

# Agent Creator - Enhanced with 5-Phase SOP Methodology (v3.0)

This skill provides the **official comprehensive framework** for creating specialized AI agents, integrating the proven 5-phase methodology (v3.0 adds Phase 0.5 cognitive frame selection) from Desktop .claude-flow with Claude Agent SDK implementation and evidence-based prompting techniques.

## Trigger Keywords

**USE WHEN user mentions:**
- "create agent", "build agent", "new agent", "design agent"
- "agent for [domain]", "specialist agent", "domain expert agent"
- "rewrite agent", "optimize agent", "improve agent"
- "agent with [capability]", "agent that does [task]"
- "multi-agent workflow", "coordinating agents"
- "production-ready agent", "agent system prompt"

**DO NOT USE when:**
- User wants a simple SKILL (not agent) - use skill-creator-agent or micro-skill-creator
- User wants to improve a PROMPT (not system prompt) - use prompt-architect
- User wants to improve THIS skill itself - use skill-forge
- User wants quick automation without agent architecture - use micro-skill-creator

**Instead use:**
- skill-creator-agent when creating skills that spawn agents (higher-level)
- micro-skill-creator when creating atomic, focused skills
- prompt-architect when optimizing user prompts (not system prompts)
- skill-forge when improving agent-creator itself

## When to Use This Skill

Use agent-creator for:
- Creating project-specialized agents with deeply embedded domain knowledge
- Building agents for recurring tasks requiring consistent behavior
- Rewriting existing agents to optimize performance
- Creating multi-agent workflows with sequential or parallel coordination
- Agents that will integrate with MCP servers and Claude Flow

## MCP Requirements

This skill requires the following MCP servers for optimal functionality:

### memory-mcp (6.0k tokens)

**Purpose**: Store agent specifications, design decisions, and metadata for cross-session persistence and pattern learning.

**Tools Used**:
- `mcp__memory-mcp__memory_store`: Store agent specs, cognitive frameworks, and design patterns
- `mcp__memory-mcp__vector_search`: Retrieve similar agent patterns for reuse

**Activation** (PowerShell):
```powershell
# Check if already active
claude mcp list

# Add if not present
claude mcp add memory-mcp node C:\Users\17175\memory-mcp\build\index.js
```

**Usage Example**:
```javascript
// Store agent specification
await mcp__memory-mcp__memory_store({
  text: `Agent: ${agentName}. Role: ${roleTitle}. Domains: ${expertiseDomains}. Capabilities: ${coreCapabilities}. Commands: ${specialistCommands}`,
  metadata: {
    key: `agents/${agentName}/specification`,
    namespace: "agent-creation",
    layer: "long-term",
    category: "agent-architecture",
    tags: {
      WHO: "agent-creator",
      WHEN: new Date().toISOString(),
      PROJECT: agentName,
      WHY: "agent-specification"
    }
  }
});

// Retrieve similar agent patterns
const similarAgents = await mcp__memory-mcp__vector_search({
  query: `Agent for ${domain} with capabilities ${capabilities}`,
  limit: 5
});
```

**Token Cost**: 6.0k tokens (3.0% of 200k context)
**When to Load**: When creating new agents or optimizing existing agent architectures

## The 5-Phase Agent Creation Methodology (v3.0)

**Source**: Desktop `.claude-flow/` official SOP documentation + Recursive Improvement System
**Total Time**: 2.5-4 hours per agent (first-time), 1.5-2 hours (speed-run)

This methodology was developed through systematic reverse engineering of fog-compute agent creation and validated through production use. **v3.0 adds Phase 0.5 for cognitive frame selection with multi-lingual embedding.**

### Phase 0: Expertise Loading (5-10 minutes) [NEW]

**Objective**: Load domain expertise before beginning agent creation.

**Activities**:
1. **Detect Domain**
   - What domain does this agent operate in?
   - Examples: authentication, payments, ML, frontend, etc.

2. **Check for Expertise File**
   ```bash
   # Check if expertise exists
   ls .claude/expertise/{domain}.yaml
   ```

3. **Load If Available**
   ```yaml
   if expertise_exists:
     - Run: /expertise-validate {domain}
     - Load: file_locations, patterns, known_issues
     - Context: Agent inherits domain knowledge
   else:
     - Flag: Discovery mode - agent will learn
     - After: Generate expertise from agent creation
   ```

4. **Apply to Agent Design**
   - Use expertise.file_locations for code references
   - Use expertise.patterns for conventions
   - Use expertise.known_issues to prevent bugs

**Validation Gate**:
- [ ] Checked for domain expertise
- [ ] Loaded expertise if available
- [ ] Flagged for discovery if not

**Outputs**:
- Domain expertise context (if available)
- Discovery mode flag (if not)

-------|-------------------|
   | Is completion tracking critical? | Aspectual (Russian) |
   | Is source verification critical? | Evidential (Turkish) |
   | Is audience calibration critical? | Hierarchical (Japanese) |
   | Is semantic analysis needed? | Morphological (Arabic) |
   | Is object comparison needed? | Classifier (Mandarin) |

3. **Frame Embedding**
   Embed frame activation phrase in agent system prompt:

   For Evidential Frame:
   ```
   ## Kanitsal Cerceve (Evidential Mode)
   Bu agent her iddia icin kaynak belirtir:
   - DOGRUDAN: "I tested this directly"
   - CIKARIM: "Evidence suggests..."
   - BILDIRILEN: "Documentation states..."
   ```

   For Aspectual Frame:
   ```
   ## Aspektual'naya Ramka (Aspectual Mode)
   Etot agent otslezhivaet zavershenie:
   - [SV] Polnost'yu zaversheno - COMPLETED
   - [NSV] V protsesse - IN_PROGRESS
   - [BLOCKED] Ozhidaet - WAITING
   ```

4. **Multi-Lingual Section**
   Include 3-5 lines in target language within agent template.

**Validation Gate**:
- [ ] Goal analysis completed (all 3 orders)
- [ ] Frame selection checklist run
- [ ] Frame activation phrase prepared
- [ ] Multi-lingual section ready

**Outputs**:
- Selected cognitive frame
- Frame activation phrase
- Multi-lingual embedding for system prompt

### Phase 2: Meta-Cognitive Extraction (30-45 minutes)

**Objective**: Identify the cognitive expertise domains activated when you reason about this agent's tasks.

**Activities**:
1. **Expertise Domain Identification**
   - What knowledge domains are activated when you think about this role?
   - What heuristics, patterns, rules-of-thumb?
   - What decision-making frameworks?
   - What quality standards?

2. **Agent Specification Creation**
   ```markdown
   # Agent Specification: [Name]

   ## Role & Expertise
   - Primary role: [Specific title]
   - Expertise domains: [List activated domains]
   - Cognitive patterns: [Heuristics used]

   ## Cognitive Frame (NEW in v3.0)
   ```yaml
   cognitive_frame:
     primary: evidential|aspectual|hierarchical|morphological|classifier
     goal_analysis:
       first_order: "..."
       second_order: "..."
       third_order: "..."
     frame_embedding: |
       [Multi-lingual activation phrase]
   ```

   ## Core Capabilities
   1. [Capability with specific examples]
   2. [Capability with specific examples]
   ...

   ## Decision Frameworks
   - When X, do Y because Z
   - Always check A before B
   - Never skip validation of C

   ## Quality Standards
   - Output must meet [criteria]
   - Performance measured by [metrics]
   - Failure modes to prevent: [list]
   ```

3. **Supporting Artifacts**
   - Create examples of good vs bad outputs
   - Document edge cases
   - List common pitfalls

**Validation Gate**:
- [ ] Identified 3+ expertise domains
- [ ] Documented 5+ decision heuristics
- [ ] Created complete agent specification
- [ ] Examples demonstrate quality standards

**Outputs**:
- Agent specification document
- Example outputs (good/bad)
- Edge case inventory

### Phase 4: Deep Technical Enhancement (60-90 minutes)

**Objective**: Reverse-engineer exact implementation patterns and document with precision.

**Activities**:
1. **Code Pattern Extraction**

   For technical agents, extract EXACT patterns from codebase:
   ```markdown
   ## Code Patterns I Recognize

   ### Pattern: [Name]
   **File**: `path/to/file.py:123-156`

   ```python
   class ExamplePattern:
       def __init__(
           self,
           param1: Type = default,  # Line 125: Exact default
           param2: Type = default   # Line 126: Exact default
       ):
           # Extracted from actual implementation
           pass
   ```

   **When I see this pattern, I know**:
   - [Specific insight about architecture]
   - [Specific constraint or requirement]
   - [Common mistake to avoid]
   ```

2. **Critical Failure Mode Documentation**

   From experience and domain knowledge:
   ```markdown
   ## Critical Failure Modes

   ### Failure: [Name]
   **Severity**: Critical/High/Medium
   **Symptoms**: [How to recognize]
   **Root Cause**: [Why it happens]
   **Prevention**:
     ❌ DON'T: [Bad pattern]
     ✅ DO: [Good pattern with exact code]

   **Detection**:
     ```bash
     # Exact command to detect this failure
     [command]
     ```
   ```

3. **Integration Patterns**

   Document exact MCP tool usage:
   ```markdown
   ## MCP Integration Patterns

   ### Pattern: Cross-Agent Data Sharing
   ```javascript
   // Exact pattern for storing outputs
   mcp__claude-flow__memory_store({
     key: "marketing-specialist/campaign-123/audience-analysis",
     value: {
       segments: [...],
       targeting: {...},
       confidence: 0.89
     },
     ttl: 86400
   })
   ```

   **Namespace Convention**:
   - Format: `{agent-role}/{task-id}/{data-type}`
   - Example: `backend-dev/api-v2/schema-design`
   ```

4. **Performance Metrics**

   Define what to track:
   ```markdown
   ## Performance Metrics I Track

   ```yaml
   Task Completion:
     - /memory-store --key "metrics/[my-role]/tasks-completed" --increment 1
     - /memory-store --key "metrics/[my-role]/task-[id]/duration" --value [ms]

   Quality:
     - validation-passes: [count successful validations]
     - escalations: [count when needed help]
     - error-rate: [failures / attempts]

   Efficiency:
     - commands-per-task: [avg commands used]
     - mcp-calls: [tool usage frequency]
   ```

   These metrics enable continuous improvement.
   ```

**Validation Gate**:
- [ ] Code patterns include file/line references
- [ ] Failure modes have detection + prevention
- [ ] MCP patterns show exact syntax
- [ ] Performance metrics defined
- [ ] Agent can self-improve through metrics

**Outputs**:
- Enhanced system prompt (v2.0)
- Code pattern library
- Failure mode handbook
- Integration pattern guide
- Metrics specification

## Claude Agent SDK Implementation

Once system prompt is finalized, implement with SDK:

### TypeScript Implementation

```typescript
import { query, tool } from '@anthropic-ai/claude-agent-sdk';
import { z } from 'zod';

// Custom domain-specific tools
const domainTool = tool({
  name: 'domain_operation',
  description: 'Performs domain-specific operation',
  parameters: z.object({
    param: z.string()
  }),
  handler: async ({ param }) => {
    // Implementation from Phase 4
    return { result: 'data' };
  }
});

// Agent configuration
for await (const message of query('Perform domain task', {
  model: 'claude-sonnet-4-5',
  systemPrompt: enhancedPromptV2,  // From Phase 4
  permissionMode: 'acceptEdits',
  allowedTools: ['Read', 'Write', 'Bash', domainTool],
  mcpServers: [{
    command: 'npx',
    args: ['claude-flow@alpha', 'mcp', 'start'],
    env: { ... }
  }],
  settingSources: ['user', 'project']
})) {
  console.log(message);
}
```

### Python Implementation

```python
from claude_agent_sdk import query, tool, ClaudeAgentOptions
import asyncio

@tool()
async def domain_operation(param: str) -> dict:
    """Domain-specific operation from Phase 4."""
    # Implementation
    return {"result": "data"}

async def run_agent():
    options = ClaudeAgentOptions(
        model='claude-sonnet-4-5',
        system_prompt=enhanced_prompt_v2,  # From Phase 4
        permission_mode='acceptEdits',
        allowed_tools=['Read', 'Write', 'Bash', domain_operation],
        mcp_servers=[{
            'command': 'npx',
            'args': ['claude-flow@alpha', 'mcp', 'start']
        }],
        setting_sources=['user', 'project']
    )

    async for message in query('Perform domain task', **options):
        print(message)

asyncio.run(run_agent())
```

## Testing & Validation

From existing framework + SOP enhancements:

### Test Suite Creation

1. **Typical Cases** - Expected behavior on common tasks
2. **Edge Cases** - Boundary conditions and unusual inputs
3. **Error Cases** - Graceful handling and escalation
4. **Integration Cases** - End-to-end workflow with other agents
5. **Performance Cases** - Speed, efficiency, resource usage

### Validation Checklist

- [ ] **Identity**: Agent maintains consistent role
- [ ] **Commands**: Uses universal commands correctly
- [ ] **Specialist Skills**: Demonstrates domain expertise
- [ ] **MCP Integration**: Coordinates via memory and tools
- [ ] **Guardrails**: Prevents identified failure modes
- [ ] **Workflows**: Executes examples successfully
- [ ] **Metrics**: Tracks performance data
- [ ] **Code Patterns**: Applies exact patterns from Phase 4
- [ ] **Error Handling**: Escalates appropriately
- [ ] **Consistency**: Produces stable outputs on repeat

## Examples from Production

### Example: Marketing Specialist Agent

See: `docs/agent-architecture/agents-rewritten/MARKETING-SPECIALIST-AGENT.md`

**Phase 0 Output**: Loaded marketing domain expertise (if available)
**Phase 1 Output**: Marketing domain analysis, tools (Google Analytics, SEMrush, etc.)
**Phase 2 Output**: Marketing expertise (CAC, LTV, funnel optimization, attribution)
**Phase 3 Output**: Base prompt with 9 specialist commands
**Phase 4 Output**: Campaign workflow patterns, A/B test validation, ROI calculations

**Result**: Production-ready agent with deeply embedded marketing expertise

## Summary

This enhanced agent-creator skill combines:
- Phase 0: Expertise Loading (NEW in v2.0)
- Phase 1-4: Official SOP methodology (Desktop .claude-flow)
- Evidence-based prompting techniques (self-consistency, PoT, plan-and-solve)
- Claude Agent SDK implementation (TypeScript + Python)
- Production validation and testing frameworks
- Continuous improvement through metrics
- Recursive improvement loop integration

Use this methodology to create agents with:
- Deeply embedded domain knowledge
- Exact command and MCP tool specifications
- Production-ready failure prevention
- Measurable performance tracking

## Cross-Skill Coordination

Agent Creator works with:
- **cognitive-lensing**: Select optimal cognitive frames for agents (Phase 0.5 integration)
- **skill-forge**: Improve agent-creator itself through meta-prompting
- **prompt-forge**: Optimize agent system prompts using evidence-based techniques
- **eval-harness**: Validate created agents against benchmarks

**Integration Points**:
- **cognitive-lensing** provides frame selection during agent creation (goal-based analysis)
- **prompt-forge** optimizes agent prompts after Phase 3 architecture design
- **skill-forge** uses meta-loop to improve the agent creation process itself
- **eval-harness** validates agent quality through regression and benchmark tests

See: `.claude/skills/META-SKILLS-COORDINATION.md` for full coordination matrix.

## GraphViz Diagram

Create `agent-creator-process.dot` to visualize the 5-phase workflow:

```dot
digraph AgentCreator {
    rankdir=TB;
    compound=true;
    node [shape=box, style=filled, fontname="Arial"];

    start [shape=ellipse, label="Start:\nAgent Request", fillcolor=lightgreen];
    end [shape=ellipse, label="Complete:\nProduction Agent", fillcolor=green, fontcolor=white];

    subgraph cluster_phase0 {
        label="Phase 0: Expertise Loading";
        fillcolor=lightyellow;
        style=filled;
        p0 [label="Load Domain\nExpertise"];
    }

    subgraph cluster_phase1 {
        label="Phase 1: Analysis";
        fillcolor=lightblue;
        style=filled;
        p1 [label="Domain\nBreakdown"];
    }

    subgraph cluster_phase2 {
        label="Phase 2: Extraction";
        fillcolor=lightblue;
        style=filled;
        p2 [label="Meta-Cognitive\nExtraction"];
    }

    subgraph cluster_phase3 {
        label="Phase 3: Architecture";
        fillcolor=lightblue;
        style=filled;
        p3 [label="System Prompt\nDesign"];
    }

    subgraph cluster_phase4 {
        label="Phase 4: Enhancement";
        fillcolor=lightblue;
        style=filled;
        p4 [label="Technical\nPatterns"];
    }

    eval [shape=octagon, label="Eval Harness\nGate", fillcolor=orange];

    start -> p0;
    p0 -> p1;
    p1 -> p2;
    p2 -> p3;
    p3 -> p4;
    p4 -> eval;
    eval -> end [label="pass", color=green];
    eval -> p1 [label="fail", color=red, style=dashed];

    labelloc="t";
    label="Agent Creator: 5-Phase Workflow (v2.0)";
    fontsize=16;
}
```

**Next**: Begin agent creation using this enhanced methodology.

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
| **Generic Instructions Without Domain Context** | Agent lacks critical domain knowledge, makes avoidable mistakes, reinvents wheels | Complete Phase 0 expertise loading and Phase 1 domain analysis before designing agent prompts |
| **Skipping Phase 2 Meta-Cognitive Extraction** | Agent follows instructions mechanically without understanding expert reasoning patterns | Identify expertise domains and decision heuristics that experts naturally apply |
| **Vague Command Specifications** | Agent receives "Process data" or "Handle errors" without concrete patterns | Provide exact command syntax, MCP tool usage patterns, and specific workflow examples |
| **Missing Failure Mode Documentation** | Agent encounters known edge cases without documented handling strategies | Document Phase 4 critical failure modes with detection scripts and prevention patterns |
| **No Performance Tracking** | Agent cannot self-improve because success/failure data is never captured | Add metrics tracking to agent prompts, store via memory-mcp, review weekly |

## Conclusion

Agent Creator transforms agent development from ad-hoc prompt writing into systematic knowledge engineering. By progressing through 5 phases - expertise loading, domain analysis, meta-cognitive extraction, architecture design, and technical enhancement - you create agents with deeply embedded domain knowledge rather than shallow instruction-following.

The investment in systematic agent creation compounds over time. Agents built with this methodology handle edge cases gracefully, avoid documented failure modes, and improve continuously through metrics tracking. When integrated with expertise files and recursive improvement loops, agents become institutional knowledge repositories that preserve and enhance organizational capabilities.

Use Agent Creator when building production-ready agents for domains requiring consistent high-quality performance. The 2.5-4 hour first-time investment becomes 1.5-2 hours for speed-runs, yielding agents that reliably execute complex workflows without constant supervision.

---

## Version History

### v3.0.1 (2025-12-19)
- Fixed typo: "n## Trigger Keywords" -> "## Trigger Keywords"
- Enhanced cross-skill coordination section with all four foundry skills
- Added integration points for cognitive-lensing, skill-forge, prompt-forge, eval-harness
- Clarified how skills integrate at different phases of agent creation

### v3.0.0 (2025-12-18)
- Added Phase 0.5: Cognitive Frame Selection with multi-lingual embedding
- Integrated goal analysis framework (1st, 2nd, 3rd order goals)
- Added frame selection checklist (Aspectual, Evidential, Hierarchical, Morphological, Classifier)
- Added frame activation phrases for Evidential (Turkish) and Aspectual (Russian) modes
- Extended Agent Specification template with cognitive_frame YAML section
- Added multi-lingual embedding requirements for agent system prompts

### v2.2.0 (2025-11-08)
- Added Phase 0: Expertise Loading
- Integrated expertise system for domain knowledge inheritance
- Added discovery mode for agents without pre-existing expertise
- Updated 5-phase workflow to 6 phases (Phase 0 + Phases 1-4)
- Added expertise validation gates
- Updated speed-run timelines to account for expertise loading

### v2.1.0 (2025-10-15)
- Enhanced Meta-Cognitive Extraction with decision framework templates
- Added quality standards documentation
- Improved agent specification structure
- Added supporting artifacts guidelines

### v2.0.0 (2025-09-20)
- Official 5-phase SOP methodology integration from Desktop .claude-flow
- Added systematic domain analysis (Phase 1)
- Added meta-cognitive extraction (Phase 2)
- Added architecture design phase (Phase 3)
- Added technical enhancement phase (Phase 4)
- Integrated evidence-based prompting techniques
- Added production validation frameworks

### v1.0.0 (2025-08-01)
- Initial agent-creator skill
- Basic agent creation workflow
- Claude Agent SDK implementation
- Evidence-based prompting techniques (self-consistency, PoT, plan-and-solve)