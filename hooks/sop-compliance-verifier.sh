#!/bin/bash
# sop-compliance-verifier.sh
# PURPOSE: Verify that Skill SOPs are being followed correctly
# HOOK TYPE: PostToolUse (runs after Skill invocation)
#
# This hook checks if the AI is following the SOP pattern:
#   Skill -> Task (spawn agents) -> TodoWrite (track progress)

# Read tool execution data from stdin
TOOL_DATA=$(timeout 3 cat 2>/dev/null || echo '{}')

# Extract tool name and result
TOOL_NAME=$(echo "$TOOL_DATA" | jq -r '.tool_name // empty' 2>/dev/null)

# Only process Skill invocations
if [[ "$TOOL_NAME" == "Skill" ]]; then
    cat << 'EOF'

============================================================
!! SKILL SOP COMPLIANCE CHECK !!
============================================================

You just invoked a Skill. Skills are SOPs (Standard Operating Procedures)
that define HOW to accomplish tasks. They are NOT execution tools.

MANDATORY POST-SKILL REQUIREMENTS:

1. SPAWN AGENTS via Task()
   - Skills define the SOP
   - Task() spawns agents to EXECUTE the SOP
   - Pattern: Task("Agent Name", "Task description", "agent-type")
   - Agent types MUST be from registry (206 agents available)

2. AGENTS FROM REGISTRY ONLY
   - Registry: claude-code-plugins/context-cascade/agents/
   - Categories: delivery, foundry, operations, orchestration, platforms,
                 quality, research, security, specialists, tooling
   - If unsure: Use fallback types (coder, researcher, tester, reviewer)

3. TRACK WITH TodoWrite()
   - Create 5-10 todos for all planned work
   - Mark in_progress when starting a task
   - Mark completed when done (IMMEDIATELY, not batched)

4. SPAWN IN PARALLEL (Golden Rule)
   - 1 MESSAGE = ALL PARALLEL Task() calls
   - Don't spawn one agent, wait, spawn another
   - Spawn ALL independent agents in a SINGLE message

5. LOAD DOMAIN EXPERTISE
   - Check: .claude/expertise/{domain}.yaml
   - If exists: Load BEFORE spawning agents
   - If not: Agent should discover and create expertise

COMPLIANCE CHECK:
  [ ] Did you call Task() to spawn agents?
  [ ] Is agent type from the registry?
  [ ] Did you call TodoWrite() with todos?
  [ ] Are parallel tasks in ONE message?
  [ ] Did you load domain expertise if available?

If ANY checkbox is unchecked: DO IT NOW before proceeding.

============================================================
EOF
fi

exit 0
