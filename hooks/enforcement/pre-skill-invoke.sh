#!/bin/bash
# pre-skill-invoke.sh
# Hook: PreToolUse on Skill
# Purpose: Log skill invocation and display SOP reminder

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
STATE_TRACKER="$SCRIPT_DIR/state-tracker.sh"

# Read tool data from stdin
TOOL_DATA=$(timeout 3 cat 2>/dev/null || echo '{}')

# Extract skill name from tool input
# NOTE: This tries to parse the skill parameter, but hooks have limited access
SKILL_NAME=$(echo "$TOOL_DATA" | jq -r '.tool_input.skill // "unknown"' 2>/dev/null)

# Log to state tracker
if [ "$SKILL_NAME" != "unknown" ]; then
    bash "$STATE_TRACKER" log_skill "$SKILL_NAME"
fi

# Display SOP reminder
cat << 'EOF'

============================================================
!! SKILL INVOCATION DETECTED !!
============================================================

Skills are SOPs (Standard Operating Procedures) that define
HOW to accomplish tasks. They are NOT direct execution tools.

MANDATORY PATTERN: Skill -> Task -> TodoWrite

After this skill completes, you MUST:

1. SPAWN AGENTS via Task()
   Pattern: Task("Agent Name", "Task description", "agent-type")

   Agent types MUST be from registry:
   - Registry: claude-code-plugins/ruv-sparc-three-loop-system/agents/
   - 206 agents in 10 categories
   - Fallbacks if unsure: coder, researcher, tester, reviewer

2. CREATE TODOS via TodoWrite()
   - Create 5-10 todos for planned work
   - Mark in_progress when starting
   - Mark completed immediately when done

3. SPAWN IN PARALLEL (Golden Rule)
   - 1 MESSAGE = ALL Task() calls for parallel work
   - Do NOT spawn agents sequentially

4. LOAD DOMAIN EXPERTISE (if available)
   - Check: .claude/expertise/{domain}.yaml
   - If exists: Load BEFORE spawning agents
   - If not: Agent discovers during execution

STATE TRACKING:
  - This skill invocation is being logged
  - Compliance will be checked after execution
  - Violations will be recorded

============================================================
EOF

# Always exit 0 (never block)
exit 0
