#!/usr/bin/env node
/**
 * Post-Hook Template (Observational)
 *
 * Template for creating non-blocking hooks that run after operations.
 * Supports: PostToolUse, Notification, Stop, SubagentStop, SessionEnd
 *
 * Features:
 * - Async-safe logging
 * - Metric collection
 * - Non-blocking execution
 * - Error isolation
 *
 * Usage:
 *   1. Copy this template to your hook location
 *   2. Implement the processHook() function
 *   3. Configure LOG_FILE for audit trail
 *   4. Add to settings.json hooks configuration
 *
 * @module hooks/templates/post-hook-template
 * @version 1.0.0
 */

const fs = require('fs');
const path = require('path');

// Configuration
const HOOK_NAME = 'my-post-hook';  // Change this
const LOG_FILE = null;             // Set to file path for audit logging
const LOG_PERFORMANCE = true;      // Log execution time to stderr
const COLLECT_METRICS = true;      // Collect execution metrics

/**
 * Main hook processing function
 * @param {Object} input - Hook input from Claude Code
 * @param {string} input.session_id - Current session ID
 * @param {string} input.tool_name - Tool that was invoked
 * @param {Object} input.tool_input - Tool input parameters
 * @param {Object} input.tool_response - Tool execution result
 * @returns {Object} Hook output
 */
function processHook(input) {
  // ===========================================
  // IMPLEMENT YOUR LOGIC HERE
  // ===========================================

  // Example: Audit logging
  if (LOG_FILE) {
    const auditEntry = {
      timestamp: new Date().toISOString(),
      session_id: input.session_id,
      tool_name: input.tool_name,
      success: isSuccess(input.tool_response),
      // Add WHO/WHEN/PROJECT/WHY tags for Memory MCP integration
      WHO: `${HOOK_NAME}-observer`,
      WHEN: new Date().toISOString(),
      PROJECT: 'claude-code-hooks',
      WHY: 'audit-trail'
    };

    try {
      fs.appendFileSync(LOG_FILE, JSON.stringify(auditEntry) + '\n');
    } catch (error) {
      console.error(`[${HOOK_NAME}] Failed to write audit log: ${error.message}`);
    }
  }

  // Example: Metric collection
  if (COLLECT_METRICS) {
    const metrics = {
      tool_name: input.tool_name,
      success: isSuccess(input.tool_response),
      timestamp: Date.now()
    };
    // In real implementation, send to metrics service
    console.error(`[METRIC] ${JSON.stringify(metrics)}`);
  }

  // Example: Error detection and alerting
  if (input.tool_response && input.tool_response.stderr) {
    const stderr = input.tool_response.stderr;
    if (stderr.includes('error') || stderr.includes('failed')) {
      console.error(`[ALERT] Tool ${input.tool_name} produced errors: ${stderr.substring(0, 100)}`);
    }
  }

  // ===========================================
  // Return non-blocking output
  // ===========================================
  return {
    suppressOutput: false
  };
}

/**
 * Check if tool execution was successful
 * @param {Object} response - Tool response
 * @returns {boolean} True if successful
 */
function isSuccess(response) {
  if (!response) return false;

  // Check exit code for Bash
  if (response.exit_code !== undefined) {
    return response.exit_code === 0;
  }

  // Check success flag
  if (response.success !== undefined) {
    return response.success;
  }

  // Check for error field
  if (response.error) {
    return false;
  }

  // Default to success
  return true;
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
      console.log(JSON.stringify({ suppressOutput: false }));
      process.exit(1);
    }

    // Process hook (non-blocking, errors are isolated)
    let result;
    try {
      result = processHook(input);
    } catch (processError) {
      console.error(`[${HOOK_NAME}] Processing error: ${processError.message}`);
      result = { suppressOutput: false };
    }

    // Ensure required fields
    if (result.suppressOutput === undefined) {
      result.suppressOutput = false;
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
    // Error handling - never block for post hooks
    console.error(`[${HOOK_NAME}] Error: ${error.message}`);
    console.log(JSON.stringify({ suppressOutput: false }));
    process.exit(1);
  }
}

// Execute
main();
