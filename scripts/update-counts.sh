#!/bin/bash
# update-counts.sh - Updates skill and agent counts in registry and CLAUDE.md
# Updated: 2026-01-02 - Excludes temp merge dirs, counts packaged .skill files
set -euo pipefail

PLUGIN_DIR="C:/Users/17175/claude-code-plugins/context-cascade"

# Portable sed in-place function (works on Windows/macOS/Linux)
sed_inplace() {
    local pattern="$1"
    local file="$2"
    local temp_file="${file}.tmp.$$"
    sed "$pattern" "$file" > "$temp_file" && mv "$temp_file" "$file"
}

# Count directory-based skills (SKILL.md files, excluding temp merge dirs)
SKILL_DIR_COUNT=$(find "$PLUGIN_DIR/skills" -name "SKILL.md" -type f 2>/dev/null | grep -v "_merged" | grep -v "packaged" | wc -l | tr -d ' ')

# Count packaged skills (.skill files)
SKILL_PKG_COUNT=$(find "$PLUGIN_DIR/skills/packaged" -name "*.skill" -type f 2>/dev/null | wc -l | tr -d ' ')

# Total skills (use directory count as canonical - packaged are just exports)
SKILL_COUNT=$SKILL_DIR_COUNT

# Count agents (.md files excluding READMEs and reports)
AGENT_COUNT=$(find "$PLUGIN_DIR/agents" -name "*.md" \
  -not -name "README*" \
  -not -name "*SUMMARY*" \
  -not -name "*REPORT*" \
  -not -name "*INDEX*" \
  -not -name "*MIGRATION*" \
  2>/dev/null | wc -l | tr -d ' ')

# Count commands
COMMAND_COUNT=$(find "$PLUGIN_DIR/commands" -name "*.md" 2>/dev/null | wc -l | tr -d ' ')

# Count playbooks
PLAYBOOK_COUNT=$(find "$PLUGIN_DIR/playbooks" -name "*.md" 2>/dev/null | wc -l | tr -d ' ')

echo "=== Context Cascade Component Counts ==="
echo "Skills (directory-based): $SKILL_DIR_COUNT"
echo "Skills (packaged .skill): $SKILL_PKG_COUNT"
echo "Agents:                   $AGENT_COUNT"
echo "Commands:                 $COMMAND_COUNT"
echo "Playbooks:                $PLAYBOOK_COUNT"
echo "Total:                    $((SKILL_COUNT + AGENT_COUNT + COMMAND_COUNT + PLAYBOOK_COUNT))"
echo ""

# Update registry.json
REGISTRY="$PLUGIN_DIR/agents/foundry/registry/registry.json"
if [ -f "$REGISTRY" ]; then
  sed_inplace "s/\"total_agents\": [0-9]*/\"total_agents\": $AGENT_COUNT/" "$REGISTRY"
  echo "Updated registry.json: total_agents = $AGENT_COUNT"
fi

# Update CLAUDE.md in plugin
CLAUDE_MD="$PLUGIN_DIR/CLAUDE.md"
if [ -f "$CLAUDE_MD" ]; then
  sed_inplace "s/Skills | [0-9]*/Skills | $SKILL_COUNT/" "$CLAUDE_MD"
  sed_inplace "s/Agents | [0-9]*/Agents | $AGENT_COUNT/" "$CLAUDE_MD"
  echo "Updated plugin CLAUDE.md"
fi

# Update user's global CLAUDE.md
USER_CLAUDE="C:/Users/17175/.claude/CLAUDE.md"
if [ -f "$USER_CLAUDE" ]; then
  sed_inplace "s/Skills | [0-9]*/Skills | $SKILL_COUNT/" "$USER_CLAUDE"
  sed_inplace "s/Agents | [0-9]*/Agents | $AGENT_COUNT/" "$USER_CLAUDE"
  echo "Updated user CLAUDE.md"
fi

echo ""
echo "Done!"
