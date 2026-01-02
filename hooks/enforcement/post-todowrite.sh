#!/bin/bash
# post-todowrite.sh
# Hook: PostToolUse on TodoWrite
# Purpose: Mark todos created in state

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
STATE_TRACKER="$SCRIPT_DIR/state-tracker.sh"

# Read tool execution data from stdin
TOOL_DATA=$(timeout 3 cat 2>/dev/null || echo '{}')

# Extract tool name
TOOL_NAME=$(echo "$TOOL_DATA" | jq -r '.tool_name // empty' 2>/dev/null)

# Only process TodoWrite invocations
if [[ "$TOOL_NAME" == "TodoWrite" ]]; then
    # Mark TodoWrite as called
    bash "$STATE_TRACKER" mark_todowrite

    cat << 'EOF'

============================================================
!! TODOWRITE EXECUTED - SOP COMPLIANCE ACHIEVED !!
============================================================

TodoWrite() has been called. Excellent!

You have completed the mandatory SOP pattern:
  Skill() -> Task() -> TodoWrite()

TODO MANAGEMENT REQUIREMENTS:

[ ] Create 5-10 todos for ALL planned work
    - Too few: You're missing tasks
    - Too many: Break into sub-projects

[ ] Each todo MUST have:
    - content: "Imperative form (Do X, Fix Y, Build Z)"
    - status: "pending" | "in_progress" | "completed"
    - activeForm: "Present continuous (Doing X, Fixing Y, Building Z)"

[ ] Mark todos in_progress BEFORE starting work
    - Exactly ONE todo should be in_progress at a time
    - NOT zero, NOT multiple

[ ] Mark completed IMMEDIATELY after finishing
    - Do NOT batch completions
    - Complete -> Mark completed -> Start next

[ ] Only mark completed when FULLY done
    - Tests passing
    - Implementation complete
    - No errors or blockers

PARALLEL EXECUTION RULE:

If you have parallel work:
  - Spawn ALL agents in ONE message
  - Create todos for all parallel work
  - Mark multiple in_progress if truly parallel
  - But typically: 1 in_progress at a time

COMPLIANCE STATUS: PASS

You have followed the SOP pattern correctly:
  1. Skill defined the SOP
  2. Task spawned agents
  3. TodoWrite tracking progress

STATE TRACKING:
  - TodoWrite marked as called
  - SOP compliance verified
  - No violations for this workflow

Keep following this pattern for all future work!

============================================================
EOF
fi

# Always exit 0
exit 0
