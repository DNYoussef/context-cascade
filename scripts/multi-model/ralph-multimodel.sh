#!/bin/bash
# ralph-multimodel.sh - Ralph Wiggum persistence loop with multi-model routing
# Combines: Ralph's persistence + Gemini/Codex capabilities
# Part of Context Cascade Multi-Model Integration

set -e

# =============================================================================
# RALPH WIGGUM MULTI-MODEL PERSISTENCE LOOP
# =============================================================================
# This script extends the Ralph Wiggum pattern with intelligent model routing:
# - Uses Gemini for research phases (search, megacontext)
# - Uses Codex for autonomous iteration (yolo, full-auto)
# - Uses Claude for complex reasoning
# - Uses LLM Council for critical decisions
# =============================================================================

# Configuration
RALPH_STATE_DIR="$HOME/.claude/ralph-wiggum"
MULTIMODEL_STATE_DIR="$HOME/.claude/memory-mcp-data/multi-model"
MAX_ITERATIONS="${MAX_ITERATIONS:-30}"
COMPLETION_PROMISE="${COMPLETION_PROMISE:-DONE}"

mkdir -p "$RALPH_STATE_DIR"
mkdir -p "$MULTIMODEL_STATE_DIR"

# Parse arguments
TASK="$1"
LOOP_ID="${2:-ralph-$(date +%s)}"

if [ -z "$TASK" ]; then
    cat << 'EOF'
Usage: ralph-multimodel.sh <task> [loop_id]

RALPH WIGGUM MULTI-MODEL PERSISTENCE LOOP

This script iterates until completion using the optimal model for each phase:

PHASE ROUTING:
  - Research needed?     -> Gemini (search, megacontext)
  - Autonomous iteration -> Codex (yolo, full-auto, sandbox)
  - Complex reasoning    -> Claude (agents)
  - Critical decisions   -> LLM Council (consensus)

OPTIONS (via environment):
  MAX_ITERATIONS=30      Maximum loop iterations
  COMPLETION_PROMISE=DONE Text that signals completion
  USE_COUNCIL=false      Use LLM Council for decisions
  CODEX_MODE=full-auto   Codex mode: yolo, full-auto, sandbox

EXAMPLES:
  ralph-multimodel.sh "Build REST API, run tests, fix failures until all pass"

  MAX_ITERATIONS=50 ralph-multimodel.sh "Refactor auth system, verify with tests"

  CODEX_MODE=sandbox ralph-multimodel.sh "Experiment with risky refactoring"

EOF
    exit 1
fi

# =============================================================================
# MODEL ROUTING FUNCTIONS
# =============================================================================

detect_phase() {
    local task_lower=$(echo "$1" | tr '[:upper:]' '[:lower:]')

    # Research phase - use Gemini
    if echo "$task_lower" | grep -qE "research|search|find|latest|documentation|best practices|architecture overview|entire codebase"; then
        echo "research"
        return
    fi

    # Media generation - use Gemini
    if echo "$task_lower" | grep -qE "diagram|mockup|image|video|visualization|flowchart"; then
        echo "media"
        return
    fi

    # Autonomous iteration - use Codex
    if echo "$task_lower" | grep -qE "fix.*test|debug|iterate|autonomous|overnight|sandbox|prototype"; then
        echo "autonomous"
        return
    fi

    # Critical decision - use Council
    if echo "$task_lower" | grep -qE "decide|choose|architecture decision|critical|consensus"; then
        echo "decision"
        return
    fi

    # Default - use Claude
    echo "reasoning"
}

execute_phase() {
    local phase="$1"
    local task="$2"
    local iteration="$3"

    case "$phase" in
        "research")
            echo "[ralph] Phase: RESEARCH -> Using Gemini"
            if echo "$task" | grep -qiE "entire|full|all files|30k"; then
                bash scripts/multi-model/gemini-yolo.sh "$task" "ralph-$iteration" "yolo"
            else
                bash scripts/multi-model/gemini-research.sh "$task" "ralph-$iteration"
            fi
            ;;
        "media")
            echo "[ralph] Phase: MEDIA -> Using Gemini Media"
            bash scripts/multi-model/gemini-yolo.sh "Generate: $task" "ralph-$iteration" "yolo"
            ;;
        "autonomous")
            echo "[ralph] Phase: AUTONOMOUS -> Using Codex YOLO"
            local mode="${CODEX_MODE:-full-auto}"
            bash scripts/multi-model/codex-yolo.sh "$task" "ralph-$iteration" "." "10" "$mode"
            ;;
        "decision")
            echo "[ralph] Phase: DECISION -> Using LLM Council"
            if [ "${USE_COUNCIL:-false}" = "true" ]; then
                bash scripts/multi-model/llm-council.sh "$task"
            else
                echo "[ralph] Council disabled, using Claude reasoning"
                echo "CLAUDE_REASONING: $task"
            fi
            ;;
        "reasoning")
            echo "[ralph] Phase: REASONING -> Using Claude"
            echo "CLAUDE_TASK: $task"
            ;;
    esac
}

# =============================================================================
# MAIN LOOP
# =============================================================================

echo "=============================================="
echo "RALPH WIGGUM MULTI-MODEL PERSISTENCE LOOP"
echo "=============================================="
echo "Loop ID: $LOOP_ID"
echo "Task: $TASK"
echo "Max Iterations: $MAX_ITERATIONS"
echo "Completion Promise: $COMPLETION_PROMISE"
echo "=============================================="
echo ""

# Initialize state
ITERATION=0
COMPLETED=false

# Save initial state
cat << EOF > "$RALPH_STATE_DIR/loop-state.json"
{
    "loop_id": "$LOOP_ID",
    "task": $(echo "$TASK" | jq -Rs .),
    "max_iterations": $MAX_ITERATIONS,
    "completion_promise": "$COMPLETION_PROMISE",
    "started_at": "$(date -Iseconds)",
    "status": "running",
    "iterations": []
}
EOF

while [ $ITERATION -lt $MAX_ITERATIONS ] && [ "$COMPLETED" = "false" ]; do
    ITERATION=$((ITERATION + 1))
    echo ""
    echo "====== ITERATION $ITERATION / $MAX_ITERATIONS ======"

    # Detect optimal phase/model
    PHASE=$(detect_phase "$TASK")
    echo "[ralph] Detected phase: $PHASE"

    # Execute with appropriate model
    RESULT=$(execute_phase "$PHASE" "$TASK" "$ITERATION" 2>&1)

    # Check for completion promise
    if echo "$RESULT" | grep -q "$COMPLETION_PROMISE"; then
        COMPLETED=true
        echo ""
        echo "[ralph] COMPLETION PROMISE FOUND: $COMPLETION_PROMISE"
        echo "[ralph] Task completed in $ITERATION iterations"
    fi

    # Log iteration
    echo "{
        \"iteration\": $ITERATION,
        \"phase\": \"$PHASE\",
        \"timestamp\": \"$(date -Iseconds)\",
        \"completed\": $COMPLETED
    }" >> "$RALPH_STATE_DIR/loop-history.log"

    # Brief pause between iterations
    if [ "$COMPLETED" = "false" ]; then
        sleep 1
    fi
done

# Final status
if [ "$COMPLETED" = "true" ]; then
    echo ""
    echo "=============================================="
    echo "RALPH WIGGUM LOOP COMPLETED SUCCESSFULLY"
    echo "=============================================="
    echo "Iterations: $ITERATION"
    echo "Status: DONE"

    # Update state
    cat << EOF > "$RALPH_STATE_DIR/loop-state.json"
{
    "loop_id": "$LOOP_ID",
    "task": $(echo "$TASK" | jq -Rs .),
    "status": "completed",
    "iterations": $ITERATION,
    "completed_at": "$(date -Iseconds)"
}
EOF
else
    echo ""
    echo "=============================================="
    echo "RALPH WIGGUM LOOP REACHED MAX ITERATIONS"
    echo "=============================================="
    echo "Max iterations: $MAX_ITERATIONS"
    echo "Status: INCOMPLETE"
    echo "Consider increasing MAX_ITERATIONS or refining task"

    # Update state
    cat << EOF > "$RALPH_STATE_DIR/loop-state.json"
{
    "loop_id": "$LOOP_ID",
    "task": $(echo "$TASK" | jq -Rs .),
    "status": "max_iterations_reached",
    "iterations": $ITERATION,
    "stopped_at": "$(date -Iseconds)"
}
EOF
fi
