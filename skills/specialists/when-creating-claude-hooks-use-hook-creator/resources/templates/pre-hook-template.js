#!/usr/bin/env node
/**
 * Pre-Hook Template (Blocking)
 *
 * Template for creating blocking hooks that run before operations.
 * Supports: PreToolUse, UserPromptSubmit, SessionStart, PermissionRequest
 *
 * Features:
 * - Input validation
 * - Error handling with configurable fail mode
 * - Performance timing
 * - RBAC integration point
 *
 * Usage:
 *   1. Copy this template to your hook location
 *   2. Implement the processHook() function
 *   3. Configure FAIL_OPEN based on security requirements
 *   4. Add to settings.json hooks configuration
 *
 * @module hooks/templates/pre-hook-template
 * @version 1.0.0
 */

const fs = require('fs');
const path = require('path');

// Configuration
const HOOK_NAME = 'my-pre-hook';  // Change this
const FAIL_OPEN = true;           // Set to false for security-critical hooks
const LOG_PERFORMANCE = true;     // Log execution time to stderr

/**
 * Main hook processing function
 * @param {Object} input - Hook input from Claude Code
 * @param {string} input.session_id - Current session ID
 * @param {string} input.tool_name - Tool being invoked (for PreToolUse)
 * @param {Object} input.tool_input - Tool input parameters
 * @returns {Object} Hook output
 */
function processHook(input) {
  // ===========================================
  // IMPLEMENT YOUR LOGIC HERE
  // ===========================================

  // Example: Block dangerous commands
  if (input.tool_name === 'Bash') {
    const command = input.tool_input.command || '';

    // Block rm -rf commands
    if (command.match(/rm\s+(-[a-zA-Z]*r[a-zA-Z]*f|--recursive.*--force)/)) {
      return {
        continue: false,
        decision: 'block',
        reason: 'Dangerous command: recursive force delete is blocked'
      };
    }

    // Block sudo commands
    if (command.match(/\bsudo\b/)) {
      return {
        continue: false,
        decision: 'block',
        reason: 'Sudo commands require manual approval'
      };
    }
  }

  // Example: Block writes to system directories
  if (input.tool_name === 'Write' || input.tool_name === 'Edit') {
    const filePath = input.tool_input.file_path || '';

    if (filePath.startsWith('/etc/') || filePath.startsWith('C:\\Windows\\')) {
      return {
        continue: false,
        decision: 'block',
        reason: 'Cannot modify system files'
      };
    }
  }

  // ===========================================
  // DEFAULT: Approve operation
  // ===========================================
  return {
    continue: true,
    decision: 'approve'
  };
}

/**
 * Validate hook input structure
 * @param {Object} input - Raw input
 * @returns {boolean} True if valid
 */
function validateInput(input) {
  if (!input || typeof input !== 'object') {
    return false;
  }
  if (!input.session_id) {
    return false;
  }
  return true;
}

/**
 * Main execution
 */
function main() {
  const startTime = process.hrtime.bigint();

  try {
    // Read input from stdin
    const rawInput = fs.readFileSync(0, 'utf-8');
    const input = JSON.parse(rawInput);

    // Validate input
    if (!validateInput(input)) {
      console.error(`[${HOOK_NAME}] Invalid input structure`);
      console.log(JSON.stringify({ continue: FAIL_OPEN, decision: FAIL_OPEN ? 'approve' : 'block' }));
      process.exit(1);
    }

    // Process hook
    const result = processHook(input);

    // Ensure required fields
    if (result.continue === undefined) {
      result.continue = true;
    }
    if (!result.decision) {
      result.decision = result.continue ? 'approve' : 'block';
    }
    if (!result.continue && !result.reason) {
      result.reason = 'Blocked by hook';
    }

    // Output result
    console.log(JSON.stringify(result));

    // Log performance
    if (LOG_PERFORMANCE) {
      const endTime = process.hrtime.bigint();
      const durationMs = Number(endTime - startTime) / 1_000_000;
      console.error(`[PERF] ${HOOK_NAME} completed in ${durationMs.toFixed(2)}ms`);
    }

  } catch (error) {
    // Error handling
    console.error(`[${HOOK_NAME}] Error: ${error.message}`);

    // Fail open or closed based on configuration
    console.log(JSON.stringify({
      continue: FAIL_OPEN,
      decision: FAIL_OPEN ? 'approve' : 'block',
      reason: FAIL_OPEN ? undefined : `Hook error: ${error.message}`
    }));

    process.exit(1);
  }
}

// Execute
main();
