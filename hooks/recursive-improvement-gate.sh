#!/bin/bash
# recursive-improvement-gate.sh
# PURPOSE: Gate all self-improvement changes through eval harness
# HOOK TYPE: PreToolUse (runs before Write/Edit on improvement targets)
#
# This hook ensures that changes to meta-skills (prompt-forge, skill-forge,
# agent-creator, eval-harness) go through proper evaluation.

# Read tool input from stdin
TOOL_INPUT=$(timeout 5 cat 2>/dev/null || echo '{}')

# Extract file path
FILE_PATH=$(echo "$TOOL_INPUT" | jq -r '.tool_input.file_path // .tool_input.path // empty' 2>/dev/null)

# Check if this is a recursive improvement target
IMPROVEMENT_TARGETS=(
    "prompt-forge"
    "skill-forge"
    "agent-creator"
    "eval-harness"
    "bootstrap-loop"
    "improvement-pipeline"
    "prompt-auditor"
    "skill-auditor"
    "expertise-auditor"
    "output-auditor"
)

IS_IMPROVEMENT_TARGET=false

for target in "${IMPROVEMENT_TARGETS[@]}"; do
    if echo "$FILE_PATH" | grep -q "$target"; then
        IS_IMPROVEMENT_TARGET=true
        break
    fi
done

# If modifying an improvement target, warn about eval gate
if [ "$IS_IMPROVEMENT_TARGET" = true ]; then
    cat << 'EOF'

================================================================
!! RECURSIVE IMPROVEMENT GATE !!
================================================================

You are modifying a META-SKILL that powers the recursive improvement system.

TARGET DETECTED: This file is part of the self-improvement loop.

MANDATORY REQUIREMENTS:

1. EVAL HARNESS GATE
   - ALL changes to meta-skills MUST pass eval-harness
   - Run: Skill("eval-harness") after changes
   - Benchmarks + Regressions must pass

2. ARCHIVE BEFORE MODIFY
   - Current version MUST be archived first
   - Path: .archive/SKILL-v{current}.md
   - Enables rollback if regression detected

3. FORBIDDEN CHANGES
   - NEVER remove safeguards
   - NEVER bypass eval harness
   - NEVER modify frozen benchmarks
   - NEVER weaken contract requirements

4. SPECIAL RULES FOR EVAL-HARNESS
   - eval-harness does NOT self-improve
   - Changes to eval-harness require MANUAL human approval
   - Only expansion allowed (never reduction)

5. SELF-REBUILD SAFETY
   - skill-forge rebuilding itself uses PREVIOUS version
   - Never use current version to rebuild current version

PROCEED ONLY IF:
  [ ] Change improves the system (not just different)
  [ ] Eval harness will be run after
  [ ] Archive exists for rollback
  [ ] No forbidden changes included

================================================================
EOF
fi

exit 0
