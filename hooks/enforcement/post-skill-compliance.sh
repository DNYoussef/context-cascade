#!/bin/bash
# post-skill-compliance.sh
# Hook: PostToolUse on Skill
# Purpose: Verify SOP compliance after skill invocation

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
STATE_TRACKER="$SCRIPT_DIR/state-tracker.sh"

# Read tool execution data from stdin
TOOL_DATA=$(timeout 3 cat 2>/dev/null || echo '{}')

# Extract tool name
TOOL_NAME=$(echo "$TOOL_DATA" | jq -r '.tool_name // empty' 2>/dev/null)

# Only process Skill invocations
if [[ "$TOOL_NAME" == "Skill" ]]; then
    cat << 'EOF'

============================================================
!! SKILL EXECUTION COMPLETED - COMPLIANCE CHECK !!
============================================================

You just invoked a Skill. The skill defines the SOP for a task.
Now you MUST follow the SOP compliance pattern.

MANDATORY NEXT STEPS:

[ ] STEP 1: Spawn agents via Task()
    - Pattern: Task("Agent Name", "Task description", "agent-type")
    - Agent type MUST be from registry (206 agents available)
    - If parallel work: Spawn ALL agents in ONE message

[ ] STEP 2: Track progress via TodoWrite()
    - Create 5-10 todos for all planned work
    - Include both content and activeForm for each todo
    - Mark in_progress when starting work
    - Mark completed IMMEDIATELY when done (not batched)

[ ] STEP 3: Load domain expertise (if available)
    - Check: .claude/expertise/{domain}.yaml
    - If exists: Load patterns BEFORE spawning agents
    - If not: Agent will create during execution

COMPLIANCE CHECKLIST:

Did you call Task() to spawn agents?           [ ]
Are agent types from the registry?             [ ]
Did you spawn parallel agents in ONE message?  [ ]
Did you call TodoWrite() with todos?           [ ]
Did you check for domain expertise?            [ ]

If ANY checkbox is UNCHECKED: Complete it NOW before proceeding.

PATTERN REMINDER:

  Skill() defines the SOP
      |
      | (you are here - skill just completed)
      |
      v
  Task() spawns registry agents to execute SOP
      |
      v
  TodoWrite() tracks progress with todos

VIOLATION TRACKING:
  - If you skip Task(): VIOLATION logged (missing_agents)
  - If you skip TodoWrite(): VIOLATION logged (missing_todowrite)
  - If you use generic agent: VIOLATION logged (generic_agent)

Your compliance is being tracked. Follow the pattern.

============================================================
EOF

    # Check compliance (will log violations)
    bash "$STATE_TRACKER" check_compliance
fi

# Always exit 0 (never block)
exit 0
