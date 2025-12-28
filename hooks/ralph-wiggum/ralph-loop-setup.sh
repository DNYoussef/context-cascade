#!/bin/bash
# ralph-loop-setup.sh
# PURPOSE: Initialize a Ralph Wiggum persistence loop
# USAGE: bash ralph-loop-setup.sh "<prompt>" [--max-iterations N] [--completion-promise "<text>"]
#
# This creates the state file that the stop hook uses to maintain the loop.

set -e

# Parse arguments
PROMPT=""
MAX_ITERATIONS=50  # Default safety limit
COMPLETION_PROMISE=""

while [[ $# -gt 0 ]]; do
    case $1 in
        --max-iterations)
            MAX_ITERATIONS="$2"
            shift 2
            ;;
        --completion-promise)
            COMPLETION_PROMISE="$2"
            shift 2
            ;;
        *)
            if [[ -z "$PROMPT" ]]; then
                PROMPT="$1"
            else
                PROMPT="$PROMPT $1"
            fi
            shift
            ;;
    esac
done

# Validate
if [[ -z "$PROMPT" ]]; then
    echo "ERROR: No prompt provided"
    echo "Usage: ralph-loop-setup.sh \"<prompt>\" [--max-iterations N] [--completion-promise \"<text>\"]"
    exit 1
fi

# Create state directory
STATE_DIR="${HOME}/.claude/ralph-wiggum"
mkdir -p "$STATE_DIR"

STATE_FILE="${STATE_DIR}/loop-state.md"

# Generate session ID
SESSION_ID=$(date +%Y%m%d-%H%M%S)-$$

# Create state file with YAML frontmatter
cat > "$STATE_FILE" << EOF
---
session_id: ${SESSION_ID}
iteration: 0
max_iterations: ${MAX_ITERATIONS}
completion_promise: "${COMPLETION_PROMISE}"
started_at: $(date -Iseconds 2>/dev/null || date +%Y-%m-%dT%H:%M:%S)
active: true
---

${PROMPT}
EOF

echo ""
echo "=========================================="
echo "   RALPH WIGGUM LOOP ACTIVATED"
echo "=========================================="
echo ""
echo "Session ID: ${SESSION_ID}"
echo "Max Iterations: ${MAX_ITERATIONS}"
if [[ -n "$COMPLETION_PROMISE" ]]; then
    echo "Completion Promise: ${COMPLETION_PROMISE}"
    echo ""
    echo "To complete the loop, output exactly:"
    echo "  <promise>${COMPLETION_PROMISE}</promise>"
fi
echo ""
echo "To cancel: /cancel-ralph OR bash .claude/hooks/ralph-wiggum/cancel-ralph.sh"
echo ""
echo "Starting loop with prompt:"
echo "---"
echo "${PROMPT}"
echo "---"
echo ""

exit 0
