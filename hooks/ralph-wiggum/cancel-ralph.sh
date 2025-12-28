#!/bin/bash
# cancel-ralph.sh
# PURPOSE: Cancel an active Ralph Wiggum loop
# USAGE: bash cancel-ralph.sh

STATE_DIR="${HOME}/.claude/ralph-wiggum"
STATE_FILE="${STATE_DIR}/loop-state.md"
LOG_FILE="${STATE_DIR}/loop-history.log"

if [[ ! -f "$STATE_FILE" ]]; then
    echo "No active Ralph loop found."
    exit 0
fi

# Get current iteration before canceling
ITERATION=$(grep -E "^iteration:" "$STATE_FILE" | head -1 | sed 's/iteration: *//' | tr -d '[:space:]')
SESSION_ID=$(grep -E "^session_id:" "$STATE_FILE" | head -1 | sed 's/session_id: *//' | tr -d '[:space:]')

# Deactivate loop
if [[ "$(uname -s)" == "Darwin" ]]; then
    sed -i '' 's/^active: true/active: false/' "$STATE_FILE"
else
    sed -i 's/^active: true/active: false/' "$STATE_FILE"
fi

echo "[$(date +%Y-%m-%d\ %H:%M:%S)] Ralph Loop CANCELLED at iteration $ITERATION (session: $SESSION_ID)" >> "$LOG_FILE"

echo ""
echo "=========================================="
echo "   RALPH LOOP CANCELLED"
echo "=========================================="
echo "Session ID: $SESSION_ID"
echo "Iterations completed: $ITERATION"
echo ""
echo "The loop has been deactivated."
echo "You can start a new loop with /ralph-loop"
echo ""

exit 0
