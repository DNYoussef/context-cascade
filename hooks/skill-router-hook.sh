#!/bin/bash
# skill-router-hook.sh
# PURPOSE: Smart skill routing via keyword matching with CASCADE DISCOVERY
# HOOK TYPE: UserPromptSubmit (runs before Claude processes user message)
# UPDATED: 2026-01-03 - Integrated COMMANDS_INDEX.yaml for explicit routing
#
# ROUTING PRIORITY:
#   1. COMMANDS_INDEX.yaml - Explicit trigger->skill mappings
#   2. skill-index.json - Fuzzy keyword matching (fallback)

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PLUGIN_DIR="${SCRIPT_DIR%/*}"
ROUTER="$PLUGIN_DIR/scripts/skill-index/route-skill.sh"
INDEX_FILE="$PLUGIN_DIR/scripts/skill-index/skill-index.json"
COMMANDS_INDEX="$HOME/.claude/commands/COMMANDS_INDEX.yaml"
SKILL_INDEX="$PLUGIN_DIR/discovery/SKILL-INDEX.md"
AGENT_REGISTRY="$PLUGIN_DIR/discovery/AGENT-REGISTRY.md"

# Read user message from stdin
USER_MESSAGE=$(timeout 5 cat 2>/dev/null || echo '{}')
MESSAGE_TEXT=$(echo "$USER_MESSAGE" | jq -r '.message // empty' 2>/dev/null || echo "$USER_MESSAGE")
MESSAGE_LOWER=$(echo "$MESSAGE_TEXT" | tr '[:upper:]' '[:lower:]')

# Skip trivial requests
TRIVIAL_PATTERNS="^(hi|hello|hey|thanks|ok|yes|no|bye|help|/help|continue|proceed)$"
if echo "$MESSAGE_TEXT" | grep -iqE "$TRIVIAL_PATTERNS"; then
    exit 0
fi

# === TIER 1: Check COMMANDS_INDEX.yaml for explicit matches ===
if [ -f "$COMMANDS_INDEX" ]; then
    TRIGGER=""
    while IFS= read -r line; do
        if [[ "$line" =~ trigger:.*\"(.+)\" ]]; then
            TRIGGER="${BASH_REMATCH[1]}"
        elif [[ "$line" =~ skill:.*\"(.+)\" ]] && [ -n "$TRIGGER" ]; then
            SKILL="${BASH_REMATCH[1]}"
            if echo "$MESSAGE_LOWER" | grep -qi "$TRIGGER"; then
                echo ""
                echo "!! CASCADE ROUTER (EXPLICIT) !!"
                echo "Trigger: \"$TRIGGER\" -> Skill: $SKILL"
                echo "Read: skills/packaged/${SKILL// /-}.skill"
                echo ""
                exit 0
            fi
            TRIGGER=""
        fi
    done < "$COMMANDS_INDEX"
fi

# === TIER 2: Fuzzy keyword matching ===
if [ ! -f "$ROUTER" ] || [ ! -f "$INDEX_FILE" ]; then
    exit 0
fi

ROUTER_OUTPUT=$(bash "$ROUTER" "$MESSAGE_TEXT" 2>/dev/null)

if [ -z "$ROUTER_OUTPUT" ] || echo "$ROUTER_OUTPUT" | grep -q "No matching"; then
    exit 0
fi

echo ""
echo "!! CASCADE SKILL ROUTER !!"
echo "================================================================"
echo "$ROUTER_OUTPUT"
echo "================================================================"
echo ""

exit 0
