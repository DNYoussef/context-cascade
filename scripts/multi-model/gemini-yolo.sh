#!/bin/bash
# gemini-yolo.sh - Semi-autonomous Gemini execution with YOLO mode
# Uses: gemini --yolo for auto-accepting all actions
# Part of Context Cascade Multi-Model Integration

set -e

# Configuration
MEMORY_SCRIPT="C:/Users/17175/claude-code-plugins/ruv-sparc-three-loop-system/scripts/memory-store.sh"
TASK_ID="${2:-$(date +%s)-$(head -c 4 /dev/urandom | xxd -p)}"

# Parse arguments
TASK="$1"
MODE="${3:-yolo}"  # yolo, interactive, sandbox

if [ -z "$TASK" ]; then
    echo "Usage: gemini-yolo.sh <task> [task_id] [mode]"
    echo ""
    echo "Modes:"
    echo "  yolo        - Auto-accept all actions (default)"
    echo "  interactive - Prompt for each action"
    echo "  sandbox     - Run in sandbox mode"
    echo ""
    echo "Examples:"
    echo "  gemini-yolo.sh 'Analyze entire codebase architecture'"
    echo "  gemini-yolo.sh 'Generate dashboard mockup' task-123 yolo"
    echo "  gemini-yolo.sh 'Search for latest React 19 features'"
    exit 1
fi

echo "[gemini-yolo] Starting task: $TASK_ID"
echo "[gemini-yolo] Mode: $MODE"
echo "[gemini-yolo] Task: $TASK"
echo ""

# Build command based on mode
case "$MODE" in
    "yolo")
        # YOLO mode - auto-accept all actions
        CMD="gemini --yolo"
        ;;
    "sandbox")
        # Sandbox mode - isolated execution
        CMD="gemini -s"
        ;;
    *)
        # Interactive mode
        CMD="gemini"
        ;;
esac

# Execute Gemini
echo "[gemini-yolo] Executing: $CMD \"$TASK\""
echo "---"

RESULT=$($CMD "$TASK" 2>&1) || {
    echo "[gemini-yolo] Execution completed with warnings"
}

# Store result in Memory-MCP
MEMORY_KEY="multi-model/gemini/yolo/$TASK_ID"

PAYLOAD=$(cat <<EOF
{
    "content": $(echo "$RESULT" | jq -Rs .),
    "metadata": {
        "WHO": "gemini-cli:yolo",
        "WHEN": "$(date -Iseconds)",
        "PROJECT": "context-cascade",
        "WHY": "yolo-execution",
        "MODE": "$MODE",
        "TASK_ID": "$TASK_ID",
        "TASK": $(echo "$TASK" | jq -Rs .)
    }
}
EOF
)

# Store to Memory-MCP
OUTPUT_DIR="$HOME/.claude/memory-mcp-data/multi-model/gemini/yolo"
mkdir -p "$OUTPUT_DIR"
echo "$PAYLOAD" > "$OUTPUT_DIR/$TASK_ID.json"

echo ""
echo "[gemini-yolo] Result stored at: $MEMORY_KEY"
echo "---"
echo "$RESULT"
