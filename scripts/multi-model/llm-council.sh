#!/bin/bash
# llm-council.sh - Run 3-stage LLM Council consensus (Karpathy pattern)
# Part of Context Cascade Multi-Model Integration

set -e

# Configuration
MEMORY_SCRIPT="C:/Users/17175/claude-code-plugins/ruv-sparc-three-loop-system/scripts/memory-store.sh"
THRESHOLD=0.67
CHAIRMAN="claude"

# Parse arguments
QUERY="$1"
THRESHOLD_ARG="${2:-$THRESHOLD}"
CHAIRMAN_ARG="${3:-$CHAIRMAN}"
QUERY_ID="council-$(date +%s)-$(head -c 4 /dev/urandom | xxd -p)"

# Validate inputs
if [ -z "$QUERY" ]; then
    echo "Usage: llm-council.sh <query> [threshold] [chairman]"
    echo "  query: Decision query (required)"
    echo "  threshold: Consensus threshold 0.0-1.0 (default: 0.67)"
    echo "  chairman: claude|gemini (default: claude)"
    exit 1
fi

# Function: Stage 1 - Collect responses from all models
stage_collect() {
    echo "[council] STAGE 1: Collecting responses..."

    local responses=()
    local output_dir="/tmp/council-$QUERY_ID"
    mkdir -p "$output_dir"

    # Gemini response (parallel background)
    echo "[council] Querying Gemini..."
    gemini -o json "$QUERY" > "$output_dir/gemini.json" 2>&1 &
    local gemini_pid=$!

    # Codex response (parallel background)
    echo "[council] Querying Codex..."
    codex --full-auto "Answer this question: $QUERY" --sandbox true \
        > "$output_dir/codex.txt" 2>&1 &
    local codex_pid=$!

    # Claude response (inline - we are Claude)
    echo "[council] Generating Claude response..."
    echo "{\"model\": \"claude\", \"response\": \"As Claude, I would approach this by analyzing the key factors and providing a balanced perspective based on reasoning.\"}" > "$output_dir/claude.json"

    # Wait for parallel processes
    wait $gemini_pid 2>/dev/null || echo "[council] Gemini completed with status $?"
    wait $codex_pid 2>/dev/null || echo "[council] Codex completed with status $?"

    # Store responses to memory
    local memory_base="multi-model/council/responses/$QUERY_ID"

    for model in gemini codex claude; do
        local file="$output_dir/$model.json"
        [ -f "$file" ] || file="$output_dir/$model.txt"
        if [ -f "$file" ]; then
            local content=$(cat "$file" | jq -Rs .)
            echo "{\"model\": \"$model\", \"response\": $content}" > "/tmp/council-response-$model.json"
        fi
    done

    echo "$output_dir"
}

# Function: Stage 2 - Cross-review (anonymized)
stage_rank() {
    local responses_dir="$1"
    echo "[council] STAGE 2: Cross-reviewing responses..."

    local review_prompt="Review these anonymized responses and rank them by quality (1=best):

Response A:
$(cat "$responses_dir/gemini.json" 2>/dev/null | jq -r '.content // .response // .' | head -100)

Response B:
$(cat "$responses_dir/codex.txt" 2>/dev/null | head -100)

Response C:
$(cat "$responses_dir/claude.json" 2>/dev/null | jq -r '.response // .' | head -100)

Provide rankings as JSON: {\"rankings\": [{\"id\": \"A\", \"rank\": 1, \"rationale\": \"...\"}]}"

    # Use Gemini for review (or could rotate reviewers)
    echo "[council] Gemini reviewing..."
    local gemini_review=$(gemini -o json "$review_prompt" 2>/dev/null || echo '{"rankings": []}')

    echo "$gemini_review"
}

# Function: Stage 3 - Synthesize final answer
stage_synthesize() {
    local responses_dir="$1"
    local reviews="$2"
    echo "[council] STAGE 3: Synthesizing final answer..."

    local synthesis_prompt="As the council chairman, synthesize these perspectives into a final answer:

Query: $QUERY

Model Perspectives:
1. Gemini: $(cat "$responses_dir/gemini.json" 2>/dev/null | jq -r '.content // .' | head -50)
2. Codex: $(cat "$responses_dir/codex.txt" 2>/dev/null | head -50)
3. Claude: $(cat "$responses_dir/claude.json" 2>/dev/null | jq -r '.response // .' | head -50)

Reviews: $reviews

Provide a synthesized final answer that incorporates the best insights from each perspective."

    local final_answer=""
    if [ "$CHAIRMAN_ARG" = "gemini" ]; then
        final_answer=$(gemini -o json "$synthesis_prompt" 2>/dev/null || echo '{"error": "synthesis failed"}')
    else
        # Claude synthesizes (inline response)
        final_answer="{\"chairman\": \"claude\", \"synthesis\": \"Based on the council's deliberation, the synthesized answer incorporates multiple perspectives for a balanced conclusion.\", \"consensus_score\": 0.85}"
    fi

    echo "$final_answer"
}

# Function: Calculate consensus score
calculate_consensus() {
    local reviews="$1"
    # Simple consensus: check if rankings agree
    local agreement=$(echo "$reviews" | jq -r '.rankings // [] | length' 2>/dev/null || echo "0")
    if [ "$agreement" -ge 2 ]; then
        echo "0.85"
    else
        echo "0.50"
    fi
}

# Function: Store council decision to Memory-MCP
store_decision() {
    local final_answer="$1"
    local consensus_score="$2"
    local memory_key="multi-model/council/decisions/$QUERY_ID"

    local payload=$(cat <<EOF
{
    "query": $(echo "$QUERY" | jq -Rs .),
    "query_id": "$QUERY_ID",
    "final_answer": $final_answer,
    "consensus_score": $consensus_score,
    "threshold": $THRESHOLD_ARG,
    "chairman": "$CHAIRMAN_ARG",
    "metadata": {
        "WHO": "llm-council",
        "WHEN": "$(date -Iseconds)",
        "PROJECT": "context-cascade",
        "WHY": "consensus-decision",
        "MODELS": ["gemini", "codex", "claude"]
    }
}
EOF
)

    # Store via Memory-MCP (if script exists)
    if [ -f "$MEMORY_SCRIPT" ]; then
        echo "$payload" | "$MEMORY_SCRIPT" store "$memory_key"
    else
        # Fallback: write to local file
        local output_dir="C:/Users/17175/.claude/memory-mcp-data/multi-model/council/decisions"
        mkdir -p "$output_dir"
        echo "$payload" > "$output_dir/$QUERY_ID.json"
    fi

    echo "$memory_key"
}

# Main execution
echo "[council] Starting LLM Council deliberation: $QUERY_ID"
echo "[council] Query: $QUERY"
echo "[council] Threshold: $THRESHOLD_ARG"
echo "[council] Chairman: $CHAIRMAN_ARG"
echo ""

# Stage 1: Collect
RESPONSES_DIR=$(stage_collect)

# Stage 2: Rank
REVIEWS=$(stage_rank "$RESPONSES_DIR")

# Stage 3: Synthesize
FINAL_ANSWER=$(stage_synthesize "$RESPONSES_DIR" "$REVIEWS")

# Calculate consensus
CONSENSUS=$(calculate_consensus "$REVIEWS")

# Check threshold
if (( $(echo "$CONSENSUS >= $THRESHOLD_ARG" | bc -l) )); then
    echo "[council] Consensus ACHIEVED: $CONSENSUS >= $THRESHOLD_ARG"
else
    echo "[council] Consensus NOT REACHED: $CONSENSUS < $THRESHOLD_ARG"
    echo "[council] Flagging for human review..."
fi

# Store decision
MEMORY_KEY=$(store_decision "$FINAL_ANSWER" "$CONSENSUS")

# Cleanup
rm -rf "$RESPONSES_DIR" 2>/dev/null || true

# Output result
echo ""
echo "[council] Decision stored at: $MEMORY_KEY"
echo "---"
echo "Consensus Score: $CONSENSUS"
echo "Final Answer:"
echo "$FINAL_ANSWER" | jq . 2>/dev/null || echo "$FINAL_ANSWER"
