---
name: code-formatter
description: Automatically format code files using the appropriate formatter based
  on file type, providing clear feedback on changes made
author: pilot-test
version: 1.0.0
created: 2025-11-06
category: foundry
tags:
- foundry
- creation
- meta-tools
---

<!-- SKILL SOP IMPROVEMENT v1.0 -->
## Skill Execution Criteria

### When to Use This Skill
- [AUTO-EXTRACTED from skill description and content]
- [Task patterns this skill is optimized for]
- [Workflow contexts where this skill excels]

### When NOT to Use This Skill
- [Situations where alternative skills are better suited]
- [Anti-patterns that indicate wrong skill choice]
- [Edge cases this skill doesn't handle well]

### Success Criteria
- primary_outcome: "[SKILL-SPECIFIC measurable result based on skill purpose]"
- quality_threshold: 0.85
- verification_method: "[How to validate skill executed correctly and produced expected outcome]"

### Edge Cases
- case: "Ambiguous or incomplete input"
  handling: "Request clarification, document assumptions, proceed with explicit constraints"
- case: "Conflicting requirements or constraints"
  handling: "Surface conflict to user, propose resolution options, document trade-offs"
- case: "Insufficient context for quality execution"
  handling: "Flag missing information, provide template for needed context, proceed with documented limitations"

### Skill Guardrails
NEVER:
  - "[SKILL-SPECIFIC anti-pattern that breaks methodology]"
  - "[Common mistake that degrades output quality]"
  - "[Shortcut that compromises skill effectiveness]"
ALWAYS:
  - "[SKILL-SPECIFIC requirement for successful execution]"
  - "[Critical step that must not be skipped]"
  - "[Quality check that ensures reliable output]"

### Evidence-Based Execution
self_consistency: "After completing this skill, verify output quality by [SKILL-SPECIFIC validation approach]"
program_of_thought: "Decompose this skill execution into: [SKILL-SPECIFIC sequential steps]"
plan_and_solve: "Plan: [SKILL-SPECIFIC planning phase] -> Execute: [SKILL-SPECIFIC execution phase] -> Verify: [SKILL-SPECIFIC verification phase]"
<!-- END SKILL SOP IMPROVEMENT -->

# Code Formatter

Automatically format code files using language-specific formatters with comprehensive error handling.

## Overview

This skill formats code files by detecting the programming language and applying the appropriate formatter (Prettier for JS/TS, Black for Python, rustfmt for Rust). It provides clear feedback on changes and handles edge cases systematically.

## When to Use This Skill

Use when you need to format code before commits, ensure consistent style across projects, or apply language-specific formatting standards automatically.

## Instructions for Claude

When this skill is activated, follow these steps to format code files.

### Step 1: Validate Input File

**Action**: Verify that the specified file exists and is accessible.

**Implementation**:
```bash
# Check file exists
if [ ! -f "$FILE_PATH" ]; then
    echo "Error: File '$FILE_PATH' not found. Check path and try again."
    exit 1
fi

# Verify file is readable
if [ ! -r "$FILE_PATH" ]; then
    echo "Error: Cannot read '$FILE_PATH'. Fix with: chmod +r '$FILE_PATH'"
    exit 2
fi

# Check file size (max 10MB)
file_size=$(stat -c%s "$FILE_PATH" 2>/dev/null || stat -f%z "$FILE_PATH")
if [ $file_size -gt 10485760 ]; then
    echo "Warning: File is $(($file_size / 1024 / 1024))MB (max: 10MB). Continue? (y/n)"
    read -r response
    if [[ "$response" != "y" ]]; then
        exit 0
    fi
fi
```

**Success Criteria**:
- ✓ File exists at specified path
- ✓ File is readable (not a permissions error)
- ✓ File size ≤ 10MB or user confirms proceed

**Error Handling**:
- If file not found (exit 1) → Display error with path, abort
- If permissions denied (exit 2) → Display error with chmod fix, abort
- If file too large → Warn user, allow proceed or abort

---

### Step 2: Detect File Language and Formatter

**Action**: Determine programming language from file extension and select appropriate formatter.

**Implementation**:
```bash
# Detect language by extension
case "$FILE_PATH" in
    *.js|*.jsx|*.ts|*.tsx|*.json)
        FORMATTER="prettier"
        FORMATTER_CMD="prettier --write"
        CHECK_CMD="prettier --check"
        ;;
    *.py)
        FORMATTER="black"
        FORMATTER_CMD="black"
        CHECK_CMD="black --check"
        ;;
    *.rs)
        FORMATTER="rustfmt"
        FORMATTER_CMD="rustfmt"
        CHECK_CMD="rustfmt --check"
        ;;
    *)
        echo "Error: Unsupported file type '${FILE_PATH##*.}'"
        echo "Supported: .js, .jsx, .ts, .tsx, .json (Prettier), .py (Black), .rs (rustfmt)"
        exit 3
        ;;
esac

echo "Detected language: ${FILE_PATH##*.} → Using $FORMATTER"
```

**Success Criteria**:
- ✓ File extension recognized
- ✓ Appropriate formatter selected
- ✓ Formatter choice logged

**Error Handling**:
- If unsupported extension (exit 3) → Display error with supported types, abort

---

### Step 3: Check Formatter Installation

**Action**: Verify the required formatter is installed before attempting to run.

**Implementation**:
```bash
# Check if formatter exists
if ! command -v $FORMATTER &> /dev/null; then
    echo "Error: $FORMATTER is not installed."

    # Provide installation instructions
    case "$FORMATTER" in
        prettier)
            echo "Install with: npm install -g prettier"
            ;;
        black)
            echo "Install with: pip install black"
            ;;
        rustfmt)
            echo "Install with: rustup component add rustfmt"
            ;;
    esac

    echo "Install now and retry? (y/n)"
    read -r response
    if [[ "$response" == "y" ]]; then
        # User can install manually, then we retry
        exit 4
    else
        exit 4
    fi
fi
```

**Success Criteria**:
- ✓ Formatter found in PATH
- ✓ Formatter version logged (optional)

**Error Handling**:
- If formatter not found (exit 4) → Display installation instructions, offer retry

---

### Step 4: Check for Syntax Errors

**Action**: Run formatter in check mode to detect syntax errors before modifying file.

**Implementation**:
```bash
# Create backup before checking
cp "$FILE_PATH" "${FILE_PATH}.backup"

# Check for syntax errors
$CHECK_CMD "$FILE_PATH" > /tmp/format-check.txt 2>&1
check_exit=$?

if [ $check_exit -ne 0 ]; then
    echo "Syntax errors detected:"
    cat /tmp/format-check.txt
    echo ""
    echo "Fix syntax errors first? (y/n)"
    read -r response
    if [[ "$response" != "y" ]]; then
        rm "${FILE_PATH}.backup"
        exit 0
    else
        # User will fix manually
        rm "${FILE_PATH}.backup"
        exit 5
    fi
fi
```

**Success Criteria**:
- ✓ Formatter check completes without errors
- ✓ Backup created successfully

**Error Handling**:
- If syntax errors (exit 5) → Display errors with line numbers, ask user to fix first

---

### Step 5: Run Formatter and Report Changes

**Action**: Execute formatter with timeout and report what changed.

**Implementation**:
```bash
# Run formatter with 60s timeout
timeout 60s $FORMATTER_CMD "$FILE_PATH" > /tmp/format-output.txt 2>&1
exit_code=$?

if [ $exit_code -eq 124 ]; then
    echo "Error: Formatter timed out after 60 seconds."
    mv "${FILE_PATH}.backup" "$FILE_PATH"  # Restore backup
    exit 6
elif [ $exit_code -ne 0 ]; then
    echo "Error: Formatter failed with exit code $exit_code"
    cat /tmp/format-output.txt
    mv "${FILE_PATH}.backup" "$FILE_PATH"  # Restore backup
    exit 7
fi

# Calculate changes
changes=$(diff -u "${FILE_PATH}.backup" "$FILE_PATH" | wc -l)

# Report results
if [ $changes -eq 0 ]; then
    echo "✓ No formatting changes needed for $FILE_PATH"
else
    echo "✓ Formatted $FILE_PATH with $FORMATTER"
    echo "  Changes: $(($changes / 2)) lines modified"
    echo "  Backup: ${FILE_PATH}.backup"
fi

# Cleanup
rm -f /tmp/format-check.txt /tmp/format-output.txt

exit 0
```

**Success Criteria**:
- ✓ Formatter completes within 60 seconds
- ✓ Formatter exits with code 0 (success)
- ✓ User receives clear feedback (X lines changed)
- ✓ Backup preserved for rollback

**Error Handling**:
- If timeout (exit 6) → Restore backup, display timeout message
- If formatter error (exit 7) → Restore backup, display formatter output

---

## Edge Cases & Special Handling

### Edge Case 1: File Has Mixed Line Endings

**When**: File contains both CRLF (Windows) and LF (Unix) line endings

**Handling**:
```bash
# Detect and normalize line endings before formatting
file "$FILE_PATH" | grep -q "CRLF"
if [ $? -eq 0 ]; then
    echo "Info: Normalizing line endings to LF (Unix style)"
    dos2unix "$FILE_PATH" 2>/dev/null || sed -i 's/\r$//' "$FILE_PATH"
fi
```

**Success Criteria**:
- ✓ Line endings detected and normalized
- ✓ User informed of normalization

---

### Edge Case 2: Multiple Formatters Available

**When**: Multiple formatter versions installed (e.g., prettier in node_modules and global)

**Handling**:
```bash
# Use project-local formatter if available
if [ -f "./node_modules/.bin/$FORMATTER" ]; then
    FORMATTER_CMD="./node_modules/.bin/$FORMATTER --write"
    echo "Info: Using project-local $FORMATTER"
else
    echo "Info: Using global $FORMATTER"
fi
```

**Success Criteria**:
- ✓ Local formatter prioritized over global
- ✓ User informed which formatter used

---

### Edge Case 3: Formatter Config File Present

**When**: .prettierrc, pyproject.toml, or rustfmt.toml exists

**Handling**:
```bash
# Formatters automatically detect config files, just inform user
if [ -f ".prettierrc" ] || [ -f "pyproject.toml" ] || [ -f "rustfmt.toml" ]; then
    echo "Info: Using custom formatter configuration"
fi
```

**Success Criteria**:
- ✓ Config file detected and used by formatter
- ✓ User informed of custom config

---

## Error Codes & Recovery

| Code | Error | User Message | Recovery Strategy |
|------|-------|--------------|-------------------|
| 1 | File not found | "Error: File '[PATH]' not found." | Check path, try again |
| 2 | Permissions denied | "Error: Cannot read '[PATH]'. Fix with: chmod +r" | Fix permissions, try again |
| 3 | Unsupported file type | "Error: Unsupported file type '.ext'. Supported: .js, .py, .rs" | Use supported file type |
| 4 | Formatter not installed | "Error: [FORMATTER] not installed. Install with: [CMD]" | Install formatter, try again |
| 5 | Syntax error | "Syntax errors detected: [ERRORS]" | Fix syntax, try again |
| 6 | Formatter timeout | "Error: Formatter timed out after 60s" | Use smaller file or fix infinite loop |
| 7 | Formatter failure | "Error: Formatter failed: [OUTPUT]" | Check formatter logs, fix issue |

---

## Success Verification Checklist

After execution, verify:
- ✓ File formatted according to language style guide
- ✓ Original file backed up before modification
- ✓ User received clear feedback on changes (X lines modified)
- ✓ No data loss or file corruption
- ✓ Exit code indicates success (0) or failure (1-7)

---

## Performance Expectations

| Metric | Target | Measurement |
|--------|--------|-------------|
| **Execution Time** | <5 seconds for typical file | Actual runtime |
| **Max File Size** | 10MB | File size check |
| **Timeout** | 60 seconds max | Timeout mechanism |
| **Memory Usage** | <100MB | Not measured (formatter-dependent) |
---

## Core Principles

Code Formatter operates on 3 fundamental principles that ensure reliable automated formatting with comprehensive error handling:

### Principle 1: Validation Before Modification

Always verify file existence, permissions, syntax, and create backups before making any changes. Never modify files without safety nets.

In practice:
- Check file exists and is readable before attempting any formatting operations, providing clear error messages with fix suggestions
- Verify file size is within limits (10MB default) with user confirmation for larger files to prevent timeout issues
- Run formatter in check mode first to detect syntax errors before modifying the file, avoiding corruption of malformed code
- Create timestamped backups (.backup suffix) automatically before every formatting run, enabling instant rollback if needed

### Principle 2: Language-Specific Formatter Selection

Detect programming language from file extension and select the appropriate industry-standard formatter, prioritizing project-local over global installations.

In practice:
- Map file extensions to formatters - .js/.jsx/.ts/.tsx/.json to Prettier, .py to Black, .rs to rustfmt
- Prioritize project-local formatters in ./node_modules/.bin/ over globally installed versions for consistency with project conventions
- Automatically detect and respect formatter configuration files (.prettierrc, pyproject.toml, rustfmt.toml) when present
- Provide clear installation instructions with package manager commands when required formatters are missing

### Principle 3: Graceful Failure with Actionable Recovery

Handle all error conditions with clear messages, restoration of original state, and specific recovery instructions. Never leave files corrupted.

In practice:
- Implement timeout mechanism (60s default) to prevent infinite loops in formatter bugs, restoring backup on timeout
- Restore backup automatically on any formatter failure (syntax error, crash, timeout) before exiting
- Provide error codes (1-7) mapped to specific recovery strategies documented in error code table
- Normalize line endings (CRLF to LF) automatically when detected to prevent cross-platform formatting conflicts

---

## Common Anti-Patterns

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| **Formatting Without Backup** | Running formatter directly on files without creating backups risks data loss if formatter crashes, has bugs, or encounters syntax errors | Always create .backup files before any modification (Step 4.1) and restore automatically on any failure (Step 5 error handling) |
| **Ignoring Syntax Errors** | Attempting to format files with syntax errors can corrupt code or produce unpredictable results depending on formatter behavior | Run formatter in check mode first (Step 4) to detect syntax errors, display them with line numbers, and ask user to fix before formatting |
| **Missing Timeout Protection** | Formatters with bugs can hang indefinitely on malformed code, blocking automation pipelines and requiring manual intervention | Wrap formatter execution in timeout mechanism (60s default in Step 5) with automatic backup restoration on timeout |

---

## Conclusion

Code Formatter provides a production-ready automated formatting system with comprehensive error handling and safety mechanisms. By validating before modification, selecting language-specific formatters intelligently, and handling failures gracefully, it enables reliable code formatting in automation pipelines.

This skill excels at pre-commit formatting hooks, CI/CD style enforcement, and codebase-wide style consistency. Use this when you need automated formatting that won't corrupt files, respects project conventions, and provides clear feedback on changes. The comprehensive error code system (1-7) ensures every failure mode has a documented recovery path.

The key differentiator is the safety-first approach - backup before modification, syntax check before formatting, timeout protection during execution, and automatic restoration on failure. This makes it suitable for production environments where file corruption is unacceptable and manual intervention should be minimized.
