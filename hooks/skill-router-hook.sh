#!/bin/bash
# skill-router-hook.sh
# PURPOSE: Smart skill routing via keyword matching
# HOOK TYPE: UserPromptSubmit (runs before Claude processes user message)
#
# Replaces brute-force skill listing with intelligent routing:
# 1. Tokenizes user request
# 2. Queries skill-index.json
# 3. Returns ONLY top 5 matching skills
# 4. Includes match confidence and file paths

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PLUGIN_DIR="${SCRIPT_DIR%/*}"
ROUTER="$PLUGIN_DIR/scripts/skill-index/route-skill.sh"
INDEX_FILE="$PLUGIN_DIR/scripts/skill-index/skill-index.json"

# Read the user's message from stdin
USER_MESSAGE=$(timeout 5 cat 2>/dev/null || echo '{}')

# Extract the actual message text
MESSAGE_TEXT=$(echo "$USER_MESSAGE" | jq -r '.message // empty' 2>/dev/null || echo "$USER_MESSAGE")

# Trivial patterns (skip routing entirely)
TRIVIAL_PATTERNS=(
    "^(hi|hello|hey|thanks|thank you|ok|okay|yes|no|bye)$"
    "^(help|/help|/clear|/status|/tasks)"
    "^(git status|git log|ls|pwd)"
    "^what time"
    "^continue"
)

IS_TRIVIAL=false
for pattern in "${TRIVIAL_PATTERNS[@]}"; do
    if echo "$MESSAGE_TEXT" | grep -iqE "$pattern"; then
        IS_TRIVIAL=true
        break
    fi
done

# Skip for trivial requests
if [ "$IS_TRIVIAL" = true ]; then
    exit 0
fi

# Check if router and index exist
if [ ! -f "$ROUTER" ] || [ ! -f "$INDEX_FILE" ]; then
    echo "!! SKILL ROUTER NOT READY - Using fallback !!" >&2
    exit 0
fi

# Run the skill router
ROUTER_OUTPUT=$(bash "$ROUTER" "$MESSAGE_TEXT" 2>/dev/null)

# Check if we got matches
if [ -z "$ROUTER_OUTPUT" ] || echo "$ROUTER_OUTPUT" | grep -q "No matching skills"; then
    # No matches - fallback to standard 5-phase without skill suggestions
    cat << 'EOF'

!! 5-PHASE WORKFLOW ACTIVE !!

Execute the standard 5-phase workflow:
1. Intent Analysis (intent-analyzer)
2. Prompt Optimization (prompt-architect)
3. Strategic Planning (research-driven-planning)
4. Playbook Routing (match tasks to skills)
5. Execution (Skill -> Task -> TodoWrite)

No specific skills matched - use general workflow.

EOF
    exit 0
fi

# Output the smart routing result
cat << EOF

!! SKILL ROUTER RESULTS !!
================================================================

Based on your request, these skills are MOST RELEVANT:

$ROUTER_OUTPUT

================================================================

INSTRUCTIONS:
1. LOAD the top-matching skill(s) - Read SKILL.md from the path shown
2. Also read ANTI-PATTERNS.md and examples/ if they exist
3. Use the skill's SOP to guide your approach
4. Follow 5-phase workflow with these specific skills

EXECUTION PATTERN:
  Skill("matched-skill-name")  // Load the SOP
       |
       v
  Task("Agent", "...", "type")  // Execute via registry agent
       |
       v
  TodoWrite({ todos: [...] })   // Track progress

DO NOT use generic implementations when matched skills exist.
================================================================

EOF

exit 0
