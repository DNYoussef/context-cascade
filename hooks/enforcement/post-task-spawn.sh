#!/bin/bash
# post-task-spawn.sh
# Hook: PostToolUse on Task
# Purpose: Track agent spawn and remind about TodoWrite

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
STATE_TRACKER="$SCRIPT_DIR/state-tracker.sh"

# Read tool execution data from stdin
TOOL_DATA=$(timeout 3 cat 2>/dev/null || echo '{}')

# Extract tool name
TOOL_NAME=$(echo "$TOOL_DATA" | jq -r '.tool_name // empty' 2>/dev/null)

# Only process Task invocations
if [[ "$TOOL_NAME" == "Task" ]]; then
    # Try to extract agent info (limited by hook constraints)
    # NOTE: This may not work if hooks can't see tool input
    AGENT_TYPE=$(echo "$TOOL_DATA" | jq -r '.tool_input.agent_type // "unknown"' 2>/dev/null)
    AGENT_NAME=$(echo "$TOOL_DATA" | jq -r '.tool_input.name // "unknown"' 2>/dev/null)
    TASK_DESC=$(echo "$TOOL_DATA" | jq -r '.tool_input.task // "unknown"' 2>/dev/null)

    # Log agent spawn (even if unknown - will be validated later)
    if [ "$AGENT_TYPE" != "unknown" ]; then
        bash "$STATE_TRACKER" log_agent "$AGENT_TYPE" "$AGENT_NAME" "$TASK_DESC"
    fi

    cat << 'EOF'

============================================================
!! AGENT SPAWNED VIA TASK !!
============================================================

An agent has been spawned. Great!

NEXT MANDATORY STEPS:

[ ] STEP 1: Verify agent type is from registry
    - Registry: claude-code-plugins/ruv-sparc-three-loop-system/agents/
    - 206 agents in 10 categories
    - If you used a generic type: FIX IT NOW

[ ] STEP 2: If spawning multiple agents (parallel work):
    - Spawn ALL agents in THIS message
    - Do NOT spawn one, wait, spawn another
    - Golden Rule: 1 MESSAGE = ALL PARALLEL OPERATIONS

[ ] STEP 3: After ALL agents spawned, call TodoWrite()
    - Create 5-10 todos for all planned work
    - Format: {content: "Do X", status: "pending", activeForm: "Doing X"}
    - Mark in_progress when starting work
    - Mark completed IMMEDIATELY when done

[ ] STEP 4: Ensure domain expertise was loaded (if available)
    - Did you check .claude/expertise/{domain}.yaml?
    - If exists: Did you load it BEFORE spawning?
    - If not: Agent will create during execution

POST-SPAWN CHECKLIST:

Are ALL parallel agents spawned in THIS message?  [ ]
Did you call TodoWrite() with todos?              [ ]
Did todos include both content and activeForm?    [ ]
Did you load domain expertise before spawning?    [ ]

PATTERN REMINDER:

  Skill() -> Task() -> TodoWrite()
             ^^^^^
           (you are here)
                |
                v
          TodoWrite() <- REQUIRED NEXT

LIMITATION NOTE:
  This hook may not have access to your agent type parameter
  Validation will happen via transcript parsing
  Please ensure you used a registry agent type

STATE TRACKING:
  - Agent spawn logged (if parameters accessible)
  - Compliance check will run after TodoWrite
  - Violations recorded in state file

============================================================
EOF
fi

# Always exit 0 (never block)
exit 0
