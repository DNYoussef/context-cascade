/**
 * Context Cascade - Nested Plugin Architecture for Claude Code
 *
 * This module exports the plugin configuration and utility functions
 * for the Context Cascade system.
 *
 * @module context-cascade
 * @version 3.0.0
 * @license MIT
 */

import { readFileSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';

const __dirname = dirname(fileURLToPath(import.meta.url));

/**
 * Load and parse the plugin manifest
 * @returns {Object} Plugin manifest configuration
 */
export function getPluginManifest() {
  const manifestPath = join(__dirname, '.claude-plugin', 'plugin.json');
  return JSON.parse(readFileSync(manifestPath, 'utf-8'));
}

/**
 * Load and parse the marketplace configuration
 * @returns {Object} Marketplace configuration
 */
export function getMarketplaceConfig() {
  const marketplacePath = join(__dirname, '.claude-plugin', 'marketplace.json');
  return JSON.parse(readFileSync(marketplacePath, 'utf-8'));
}

/**
 * Get the base directory for plugin resources
 * @returns {string} Absolute path to plugin root
 */
export function getPluginRoot() {
  return __dirname;
}

/**
 * Get paths to core plugin directories
 * @returns {Object} Object containing paths to agents, skills, commands, docs
 */
export function getPluginPaths() {
  return {
    agents: join(__dirname, 'agents'),
    skills: join(__dirname, 'skills'),
    commands: join(__dirname, 'commands'),
    docs: join(__dirname, 'docs'),
    hooks: join(__dirname, 'hooks'),
    plugins: join(__dirname, 'plugins')
  };
}

// Default export for convenience
export default {
  getPluginManifest,
  getMarketplaceConfig,
  getPluginRoot,
  getPluginPaths
};
