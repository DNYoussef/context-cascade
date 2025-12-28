#!/bin/bash
# codex-yolo.sh - Fully autonomous Codex execution with YOLO/Full-Auto mode
# Uses: codex --yolo or codex --full-auto for unattended operation
# Part of Context Cascade Multi-Model Integration

set -e

# Configuration
TASK_ID="${2:-$(date +%s)-$(head -c 4 /dev/urandom | xxd -p)}"
MAX_ITERATIONS="${4:-10}"

# Parse arguments
TASK="$1"
CONTEXT="${3:-.}"  # Default to current directory
MODE="${5:-yolo}"  # yolo, full-auto, sandbox, zdr

if [ -z "$TASK" ]; then
    echo "Usage: codex-yolo.sh <task> [task_id] [context] [max_iterations] [mode]"
    echo ""
    echo "Modes:"
    echo "  yolo      - Auto-accept all actions (default)"
    echo "  full-auto - Equivalent to -a on-failure -s workspace-write"
    echo "  sandbox   - Full isolation with network disabled"
    echo "  zdr       - Zero Data Retention for sensitive code"
    echo ""
    echo "Examples:"
    echo "  codex-yolo.sh 'Build REST API with tests'"
    echo "  codex-yolo.sh 'Fix all failing tests' task-123 tests/ 15 full-auto"
    echo "  codex-yolo.sh 'Audit sensitive code' task-456 src/ 5 zdr"
    exit 1
fi

echo "[codex-yolo] Starting task: $TASK_ID"
echo "[codex-yolo] Mode: $MODE"
echo "[codex-yolo] Context: $CONTEXT"
echo "[codex-yolo] Max iterations: $MAX_ITERATIONS"
echo "[codex-yolo] Task: $TASK"
echo ""

# Build command based on mode
case "$MODE" in
    "yolo")
        # YOLO mode - auto-accept everything
        CMD="codex --yolo"
        ;;
    "full-auto")
        # Full-auto mode - autonomous with workspace write
        CMD="codex --full-auto"
        ;;
    "sandbox")
        # Sandbox mode - full isolation
        CMD="codex --full-auto --sandbox true --network disabled"
        ;;
    "zdr")
        # Zero Data Retention - for sensitive/proprietary code
        CMD="codex --full-auto --zdr"
        ;;
    *)
        CMD="codex --full-auto"
        ;;
esac

# Add common options
CMD="$CMD --max-iterations $MAX_ITERATIONS --context \"$CONTEXT\""

# Execute Codex
echo "[codex-yolo] Executing: $CMD \"$TASK\""
echo "---"

# Create temp file for output
TEMP_OUTPUT="/tmp/codex-yolo-$TASK_ID.log"

# Run Codex (note: actual codex command would be used here)
# For now, simulate the call structure
eval "$CMD \"$TASK\"" > "$TEMP_OUTPUT" 2>&1 || {
    echo "[codex-yolo] Execution completed (check output for details)"
}

RESULT=$(cat "$TEMP_OUTPUT" 2>/dev/null || echo "Execution completed")
rm -f "$TEMP_OUTPUT"

# Store result in Memory-MCP
MEMORY_KEY="multi-model/codex/yolo/$TASK_ID"

PAYLOAD=$(cat <<EOF
{
    "content": $(echo "$RESULT" | jq -Rs .),
    "metadata": {
        "WHO": "codex-cli:yolo",
        "WHEN": "$(date -Iseconds)",
        "PROJECT": "context-cascade",
        "WHY": "yolo-execution",
        "MODE": "$MODE",
        "MAX_ITERATIONS": $MAX_ITERATIONS,
        "CONTEXT": "$CONTEXT",
        "TASK_ID": "$TASK_ID",
        "TASK": $(echo "$TASK" | jq -Rs .)
    }
}
EOF
)

# Store to Memory-MCP
OUTPUT_DIR="$HOME/.claude/memory-mcp-data/multi-model/codex/yolo"
mkdir -p "$OUTPUT_DIR"
echo "$PAYLOAD" > "$OUTPUT_DIR/$TASK_ID.json"

echo ""
echo "[codex-yolo] Result stored at: $MEMORY_KEY"
echo "---"
echo "$RESULT"
