#!/bin/bash
# user-prompt-submit.sh
# Hook: UserPromptSubmit
# Purpose: Initialize workflow state, match skills, and inject context
#
# INTEGRATED SKILL ROUTER - Matches user request to relevant skills

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PLUGIN_DIR="${SCRIPT_DIR%/hooks/enforcement}"
STATE_TRACKER="$SCRIPT_DIR/state-tracker.sh"
SKILL_ROUTER="$PLUGIN_DIR/scripts/skill-index/route-skill.sh"
SKILL_INDEX="$PLUGIN_DIR/scripts/skill-index/skill-index.json"

# Read user message from stdin
USER_MESSAGE=$(timeout 5 cat 2>/dev/null || echo '{}')

# Extract message text
MESSAGE_TEXT=$(echo "$USER_MESSAGE" | jq -r '.message // empty' 2>/dev/null || echo "$USER_MESSAGE")

# Classify request as trivial or non-trivial
IS_TRIVIAL=false

# Trivial patterns (skip enforcement)
TRIVIAL_PATTERNS=(
    "^(hi|hello|hey|thanks|thank you|ok|okay|yes|no|bye)$"
    "^what (is|are|does|do) "
    "^(can you|could you) explain"
    "^(help|/help|/clear|/status)"
    "^show me"
    "^list "
    "^read "
    "^(git status|git log|ls|pwd)"
    "^search "
    "^find "
    "^grep "
)

for pattern in "${TRIVIAL_PATTERNS[@]}"; do
    if echo "$MESSAGE_TEXT" | grep -iqE "$pattern"; then
        IS_TRIVIAL=true
        break
    fi
done

# Non-trivial patterns (REQUIRE 5-phase)
NONTRIVIAL_PATTERNS=(
    "(build|create|implement|develop|add|make)"
    "(fix|debug|repair|resolve|solve)"
    "(refactor|optimize|improve|enhance)"
    "(analyze|audit|review|check|validate)"
    "(deploy|release|ship|publish)"
    "(test|spec|coverage)"
    "(design|architect|plan|strategy)"
)

for pattern in "${NONTRIVIAL_PATTERNS[@]}"; do
    if echo "$MESSAGE_TEXT" | grep -iqE "$pattern"; then
        IS_TRIVIAL=false
        break
    fi
done

# For non-trivial requests, initialize state and run skill router
if [ "$IS_TRIVIAL" = false ]; then
    # Initialize workflow state
    if [ -f "$STATE_TRACKER" ]; then
        bash "$STATE_TRACKER" init_state 2>/dev/null
    fi

    # Run skill router if available
    SKILL_MATCHES=""
    if [ -f "$SKILL_ROUTER" ] && [ -f "$SKILL_INDEX" ]; then
        SKILL_MATCHES=$(bash "$SKILL_ROUTER" "$MESSAGE_TEXT" 2>/dev/null)
    fi

    # Check if we got skill matches
    if [ -n "$SKILL_MATCHES" ] && ! echo "$SKILL_MATCHES" | grep -q "No matching skills"; then
        # Display matched skills with routing info
        cat << EOF

================================================================
!! SKILL ROUTER + 5-PHASE WORKFLOW ACTIVE !!
================================================================

MATCHED SKILLS FOR YOUR REQUEST:

$SKILL_MATCHES

================================================================
WORKFLOW INSTRUCTIONS:
================================================================

1. LOAD TOP SKILL(S) - Read the SKILL.md from path shown above
   Also read: ANTI-PATTERNS.md, README.md, examples/ if they exist

2. FOLLOW THE SKILL'S SOP - Each skill defines HOW to accomplish the task

3. SPAWN AGENTS via Task() - Use agents from registry only:
   Registry: claude-code-plugins/context-cascade/agents/
   Categories: delivery, foundry, operations, orchestration,
               platforms, quality, research, security, specialists, tooling
   Fallbacks if unsure: coder, researcher, tester, reviewer

4. TRACK PROGRESS via TodoWrite() - Create 5-10 todos for the work

EXECUTION PATTERN:
  Read(skill_path + "SKILL.md")   // Load the SOP
       |
       v
  Task("Agent", "...", "type")    // Execute via registry agent
       |
       v
  TodoWrite({ todos: [...] })     // Track progress

GOLDEN RULE: 1 MESSAGE = ALL PARALLEL Task() CALLS
================================================================

EOF
    else
        # No skill matches - show generic 5-phase
        cat << 'EOF'

================================================================
!! 5-PHASE WORKFLOW ACTIVE !!
================================================================

No specific skills matched. Use general 5-phase workflow:

1. INTENT ANALYSIS - Understand what user wants
2. PLANNING - Break down into tasks
3. SKILL ROUTING - Find relevant skills in:
   skills/delivery/     - Feature implementation
   skills/quality/      - Testing, auditing
   skills/security/     - Security tasks
   skills/research/     - Research tasks
   skills/orchestration/ - Multi-agent coordination
   skills/operations/   - DevOps, deployment
   skills/platforms/    - Platform-specific
   skills/foundry/      - Creating new skills/agents
   skills/specialists/  - Domain experts
   skills/tooling/      - Tool integrations

4. EXECUTION - Skill -> Task -> TodoWrite pattern
5. VERIFICATION - Check outputs against requirements

Agent Registry: claude-code-plugins/context-cascade/agents/
Fallbacks: coder, researcher, tester, reviewer
================================================================

EOF
    fi
fi

# Always exit 0 (never block)
exit 0
