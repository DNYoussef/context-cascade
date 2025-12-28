#!/bin/bash
# codex-audit.sh - Execute Codex CLI in sandbox and store audit results
# Part of Context Cascade Multi-Model Integration

set -e

# Configuration
MEMORY_SCRIPT="C:/Users/17175/claude-code-plugins/ruv-sparc-three-loop-system/scripts/memory-store.sh"
MAX_ITERATIONS=5
SANDBOX=true

# Parse arguments
TASK="$1"
CONTEXT="$2"
TASK_ID="${3:-$(date +%s)-$(head -c 4 /dev/urandom | xxd -p)}"
MAX_ITER="${4:-$MAX_ITERATIONS}"

# Validate inputs
if [ -z "$TASK" ] || [ -z "$CONTEXT" ]; then
    echo "Usage: codex-audit.sh <task> <context> [task_id] [max_iterations]"
    echo "  task: Audit task description (required)"
    echo "  context: File or directory path (required)"
    echo "  task_id: Unique identifier (optional, auto-generated)"
    echo "  max_iterations: Max retry attempts (default: 5)"
    exit 1
fi

# Validate context exists
if [ ! -e "$CONTEXT" ]; then
    echo "[codex-audit] ERROR: Context path does not exist: $CONTEXT"
    exit 1
fi

# Function: Execute Codex in sandbox
execute_codex() {
    local result=""
    local temp_output="/tmp/codex-result-$TASK_ID.md"

    echo "[codex-audit] Executing in sandbox mode..."
    echo "[codex-audit] Task: $TASK"
    echo "[codex-audit] Context: $CONTEXT"
    echo "[codex-audit] Max iterations: $MAX_ITER"

    # Execute Codex with full-auto mode
    # Note: codex --full-auto is equivalent to codex -a on-failure -s workspace-write
    if codex --full-auto "$TASK" \
        --context "$CONTEXT" \
        --sandbox true \
        --max-iterations "$MAX_ITER" \
        > "$temp_output" 2>&1; then
        result=$(cat "$temp_output")
        rm -f "$temp_output"
        echo "$result"
    else
        echo "[codex-audit] Codex execution completed with findings"
        result=$(cat "$temp_output" 2>/dev/null || echo "No output captured")
        rm -f "$temp_output"
        echo "$result"
    fi
}

# Function: Parse audit results
parse_results() {
    local raw_output="$1"

    # Extract key metrics if possible
    local files_count=$(echo "$raw_output" | grep -c "File:" || echo "0")
    local findings_count=$(echo "$raw_output" | grep -ci "error\|warning\|issue\|bug" || echo "0")
    local fixes_count=$(echo "$raw_output" | grep -ci "fixed\|resolved\|corrected" || echo "0")

    cat <<EOF
{
    "raw_output": $(echo "$raw_output" | jq -Rs .),
    "metrics": {
        "files_analyzed": $files_count,
        "findings_count": $findings_count,
        "fixes_applied": $fixes_count
    },
    "context_path": "$CONTEXT",
    "sandbox_mode": $SANDBOX,
    "max_iterations": $MAX_ITER
}
EOF
}

# Function: Store to Memory-MCP
store_to_memory() {
    local parsed_result="$1"
    local memory_key="multi-model/codex/audit/$TASK_ID"

    # Create tagged payload
    local payload=$(cat <<EOF
{
    "content": $parsed_result,
    "metadata": {
        "WHO": "codex-cli:audit",
        "WHEN": "$(date -Iseconds)",
        "PROJECT": "context-cascade",
        "WHY": "audit",
        "MODEL": "gpt-5-codex",
        "TASK_ID": "$TASK_ID",
        "TASK": $(echo "$TASK" | jq -Rs .),
        "CONTEXT": "$CONTEXT"
    }
}
EOF
)

    # Store via Memory-MCP (if script exists)
    if [ -f "$MEMORY_SCRIPT" ]; then
        echo "$payload" | "$MEMORY_SCRIPT" store "$memory_key"
    else
        # Fallback: write to local file
        local output_dir="C:/Users/17175/.claude/memory-mcp-data/multi-model/codex/audit"
        mkdir -p "$output_dir"
        echo "$payload" > "$output_dir/$TASK_ID.json"
    fi

    echo "$memory_key"
}

# Main execution
echo "[codex-audit] Starting audit task: $TASK_ID"
echo "[codex-audit] Sandbox: $SANDBOX"

# Execute Codex
RAW_RESULT=$(execute_codex)

# Parse results
PARSED_RESULT=$(parse_results "$RAW_RESULT")

# Store to Memory-MCP
MEMORY_KEY=$(store_to_memory "$PARSED_RESULT")

# Output result
echo "[codex-audit] Result stored at: $MEMORY_KEY"
echo "---"
echo "$PARSED_RESULT" | jq .
