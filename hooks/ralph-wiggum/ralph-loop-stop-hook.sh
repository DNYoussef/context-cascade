#!/bin/bash
# ralph-loop-stop-hook.sh
# PURPOSE: Stop hook for Ralph Wiggum persistence loop
# HOOK TYPE: Stop (runs when Claude tries to end session)
#
# This hook:
# 1. Checks if a Ralph loop is active
# 2. Validates completion promise if set
# 3. Blocks exit and re-injects prompt if loop should continue
# 4. Uses exit code 2 to block Claude from stopping

STATE_DIR="${HOME}/.claude/ralph-wiggum"
STATE_FILE="${STATE_DIR}/loop-state.md"
LOG_FILE="${STATE_DIR}/loop-history.log"

# Function to log
log_message() {
    echo "[$(date +%Y-%m-%d\ %H:%M:%S)] $1" >> "$LOG_FILE"
}

# Check if state file exists and loop is active
if [[ ! -f "$STATE_FILE" ]]; then
    # No active loop, allow normal exit
    exit 0
fi

# Check if loop is marked active
ACTIVE=$(grep -E "^active:" "$STATE_FILE" | head -1 | sed 's/active: *//' | tr -d '[:space:]')
if [[ "$ACTIVE" != "true" ]]; then
    exit 0
fi

# Extract state values using grep/sed (Windows-compatible, no yq dependency)
ITERATION=$(grep -E "^iteration:" "$STATE_FILE" | head -1 | sed 's/iteration: *//' | tr -d '[:space:]')
MAX_ITERATIONS=$(grep -E "^max_iterations:" "$STATE_FILE" | head -1 | sed 's/max_iterations: *//' | tr -d '[:space:]')
COMPLETION_PROMISE=$(grep -E "^completion_promise:" "$STATE_FILE" | head -1 | sed 's/completion_promise: *//' | tr -d '"')
SESSION_ID=$(grep -E "^session_id:" "$STATE_FILE" | head -1 | sed 's/session_id: *//' | tr -d '[:space:]')

# Validate numeric values
if ! [[ "$ITERATION" =~ ^[0-9]+$ ]]; then
    ITERATION=0
fi
if ! [[ "$MAX_ITERATIONS" =~ ^[0-9]+$ ]]; then
    MAX_ITERATIONS=50
fi

# Increment iteration
ITERATION=$((ITERATION + 1))

log_message "Ralph Loop iteration $ITERATION of $MAX_ITERATIONS (session: $SESSION_ID)"

# Check max iterations
if [[ $ITERATION -gt $MAX_ITERATIONS ]]; then
    log_message "Max iterations reached. Ending loop."

    # Deactivate loop
    if [[ "$(uname -s)" == "Darwin" ]]; then
        sed -i '' 's/^active: true/active: false/' "$STATE_FILE"
    else
        sed -i 's/^active: true/active: false/' "$STATE_FILE"
    fi

    echo ""
    echo "=========================================="
    echo "   RALPH LOOP: MAX ITERATIONS REACHED"
    echo "=========================================="
    echo "Completed $MAX_ITERATIONS iterations without completion promise."
    echo "Loop has been deactivated."
    echo ""

    exit 0
fi

# Check completion promise if set
if [[ -n "$COMPLETION_PROMISE" && "$COMPLETION_PROMISE" != '""' && "$COMPLETION_PROMISE" != "''" ]]; then
    # Read Claude's last response from stdin (piped by hook system)
    CLAUDE_OUTPUT=$(cat 2>/dev/null || echo "")

    # Look for <promise>TEXT</promise> pattern
    FOUND_PROMISE=$(echo "$CLAUDE_OUTPUT" | grep -oP '(?<=<promise>).*?(?=</promise>)' 2>/dev/null || echo "")

    if [[ "$FOUND_PROMISE" == "$COMPLETION_PROMISE" ]]; then
        log_message "Completion promise found: $FOUND_PROMISE. Ending loop successfully."

        # Deactivate loop
        if [[ "$(uname -s)" == "Darwin" ]]; then
            sed -i '' 's/^active: true/active: false/' "$STATE_FILE"
        else
            sed -i 's/^active: true/active: false/' "$STATE_FILE"
        fi

        echo ""
        echo "=========================================="
        echo "   RALPH LOOP: TASK COMPLETE!"
        echo "=========================================="
        echo "Completion promise verified: $FOUND_PROMISE"
        echo "Total iterations: $ITERATION"
        echo ""

        exit 0
    fi
fi

# Update iteration count in state file
if [[ "$(uname -s)" == "Darwin" ]]; then
    sed -i '' "s/^iteration: .*/iteration: $ITERATION/" "$STATE_FILE"
else
    sed -i "s/^iteration: .*/iteration: $ITERATION/" "$STATE_FILE"
fi

# Extract prompt (everything after the --- separator)
PROMPT=$(awk '/^---$/{if(++n==2){found=1;next}}found' "$STATE_FILE")

if [[ -z "$PROMPT" ]]; then
    log_message "ERROR: Could not extract prompt from state file"
    exit 0
fi

log_message "Re-injecting prompt for iteration $ITERATION"

# Output the blocking JSON to prevent exit and re-inject prompt
# Exit code 2 blocks the exit
cat << EOF

==========================================
   RALPH LOOP: ITERATION $ITERATION of $MAX_ITERATIONS
==========================================

The loop continues. Previous work persists in files.
Review your progress and continue working toward completion.

EOF

if [[ -n "$COMPLETION_PROMISE" && "$COMPLETION_PROMISE" != '""' ]]; then
    cat << EOF
To complete, output exactly: <promise>$COMPLETION_PROMISE</promise>

EOF
fi

cat << EOF
ORIGINAL TASK:
---
$PROMPT
---

Continue working on this task. Check files for your previous progress.
If tests exist, run them and fix any failures.
If blocked, document what's preventing progress.

EOF

# Exit with code 2 to block normal exit and trigger re-prompt
exit 2
