#!/bin/bash
# gemini-research.sh - Execute Gemini CLI and store results in Memory-MCP
# Part of Context Cascade Multi-Model Integration

set -e

# Configuration
MEMORY_SCRIPT="C:/Users/17175/claude-code-plugins/ruv-sparc-three-loop-system/scripts/memory-store.sh"
MAX_RETRIES=3
RETRY_DELAY=5

# Parse arguments
QUERY="$1"
TASK_ID="${2:-$(date +%s)-$(head -c 4 /dev/urandom | xxd -p)}"
OUTPUT_FORMAT="${3:-json}"

# Validate inputs
if [ -z "$QUERY" ]; then
    echo "Usage: gemini-research.sh <query> [task_id] [output_format]"
    echo "  query: Research query (required)"
    echo "  task_id: Unique identifier (optional, auto-generated)"
    echo "  output_format: json|text (default: json)"
    exit 1
fi

# Function: Execute Gemini with retries
execute_gemini() {
    local attempt=1
    local result=""

    while [ $attempt -le $MAX_RETRIES ]; do
        echo "[gemini-research] Attempt $attempt of $MAX_RETRIES..."

        if [ "$OUTPUT_FORMAT" = "json" ]; then
            result=$(gemini -o json "$QUERY" 2>&1) && break
        else
            result=$(gemini "$QUERY" 2>&1) && break
        fi

        echo "[gemini-research] Attempt $attempt failed, retrying in ${RETRY_DELAY}s..."
        sleep $RETRY_DELAY
        attempt=$((attempt + 1))
    done

    if [ $attempt -gt $MAX_RETRIES ]; then
        echo "[gemini-research] ERROR: All $MAX_RETRIES attempts failed"
        echo "{\"error\": \"gemini_unavailable\", \"fallback\": \"claude\"}"
        exit 1
    fi

    echo "$result"
}

# Function: Store to Memory-MCP
store_to_memory() {
    local content="$1"
    local memory_key="multi-model/gemini/research/$TASK_ID"

    # Create tagged payload
    local payload=$(cat <<EOF
{
    "content": $(echo "$content" | jq -Rs .),
    "metadata": {
        "WHO": "gemini-cli:research",
        "WHEN": "$(date -Iseconds)",
        "PROJECT": "context-cascade",
        "WHY": "research",
        "MODEL": "gemini-2.5-pro",
        "TASK_ID": "$TASK_ID",
        "QUERY": $(echo "$QUERY" | jq -Rs .)
    }
}
EOF
)

    # Store via Memory-MCP (if script exists)
    if [ -f "$MEMORY_SCRIPT" ]; then
        echo "$payload" | "$MEMORY_SCRIPT" store "$memory_key"
    else
        # Fallback: write to local file
        local output_dir="C:/Users/17175/.claude/memory-mcp-data/multi-model/gemini/research"
        mkdir -p "$output_dir"
        echo "$payload" > "$output_dir/$TASK_ID.json"
    fi

    echo "$memory_key"
}

# Main execution
echo "[gemini-research] Starting research task: $TASK_ID"
echo "[gemini-research] Query: $QUERY"

# Execute Gemini
RESULT=$(execute_gemini)

# Store to Memory-MCP
MEMORY_KEY=$(store_to_memory "$RESULT")

# Output result
echo "[gemini-research] Result stored at: $MEMORY_KEY"
echo "---"
echo "$RESULT"
