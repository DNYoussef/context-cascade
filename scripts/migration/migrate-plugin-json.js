#!/usr/bin/env node
/**
 * migrate-plugin-json.js
 * Transforms plugin.json from custom schema to Anthropic official format
 *
 * Usage:
 *   node migrate-plugin-json.js [--dry-run]
 */

const fs = require('fs');
const path = require('path');

const PLUGIN_DIR = path.resolve(__dirname, '../../.claude-plugin');
const PLUGIN_JSON_PATH = path.join(PLUGIN_DIR, 'plugin.json');
const BACKUP_PATH = path.join(PLUGIN_DIR, 'plugin.json.backup');

const DRY_RUN = process.argv.includes('--dry-run');

function log(msg) {
  console.log(`[migrate-plugin-json] ${msg}`);
}

function readPluginJson() {
  const content = fs.readFileSync(PLUGIN_JSON_PATH, 'utf-8');
  return JSON.parse(content);
}

function transformPluginJson(original) {
  // Extract required fields
  const transformed = {
    name: original.name,
    description: original.description || 'Context-saving nested plugin architecture for Claude Code',
    version: original.version,
    author: original.author || { name: 'DNYoussef' }
  };

  // Add official path fields
  transformed.commands = './commands/';
  transformed.agents = './agents/';
  transformed.skills = './skills/';
  transformed.hooks = './hooks/hooks.json';
  transformed.mcpServers = './.mcp.json';

  // Preserve custom fields with x- prefix
  if (original.license) {
    transformed['x-license'] = original.license;
  }
  if (original.repository) {
    transformed['x-repository'] = original.repository;
  }
  if (original.homepage) {
    transformed['x-homepage'] = original.homepage;
  }
  if (original.keywords) {
    transformed['x-keywords'] = original.keywords;
  }
  if (original.claudeCode) {
    transformed['x-claudeCode'] = original.claudeCode;
  }
  if (original.contents) {
    transformed['x-contents'] = original.contents;
  }
  if (original.features) {
    transformed['x-features'] = original.features;
  }
  if (original.installation) {
    transformed['x-installation'] = original.installation;
  }
  if (original.documentation) {
    transformed['x-documentation'] = original.documentation;
  }
  if (original.maintainers) {
    transformed['x-maintainers'] = original.maintainers;
  }

  return transformed;
}

function validateTransformed(transformed) {
  const required = ['name', 'description', 'version', 'author'];
  const missing = required.filter(f => !transformed[f]);

  if (missing.length > 0) {
    throw new Error(`Missing required fields: ${missing.join(', ')}`);
  }

  const officialPaths = ['commands', 'agents', 'skills'];
  const missingPaths = officialPaths.filter(f => !transformed[f]);

  if (missingPaths.length > 0) {
    throw new Error(`Missing path fields: ${missingPaths.join(', ')}`);
  }

  return true;
}

function main() {
  log('Starting plugin.json migration...');

  if (DRY_RUN) {
    log('DRY RUN MODE - no files will be modified');
  }

  // Read original
  log(`Reading ${PLUGIN_JSON_PATH}`);
  const original = readPluginJson();
  log(`Original has ${Object.keys(original).length} top-level keys`);

  // Transform
  log('Transforming to official format...');
  const transformed = transformPluginJson(original);
  log(`Transformed has ${Object.keys(transformed).length} top-level keys`);

  // Validate
  log('Validating transformed structure...');
  validateTransformed(transformed);
  log('Validation PASSED');

  // Show diff
  log('\n--- TRANSFORMATION SUMMARY ---');
  log('ADDED official fields:');
  log('  - commands: "./commands/"');
  log('  - agents: "./agents/"');
  log('  - skills: "./skills/"');
  log('  - hooks: "./hooks/hooks.json"');
  log('  - mcpServers: "./.mcp.json"');
  log('\nPRESERVED with x- prefix:');
  Object.keys(transformed)
    .filter(k => k.startsWith('x-'))
    .forEach(k => log(`  - ${k}`));
  log('--- END SUMMARY ---\n');

  if (DRY_RUN) {
    log('DRY RUN - would write:');
    console.log(JSON.stringify(transformed, null, 2));
    return;
  }

  // Backup original
  log(`Creating backup at ${BACKUP_PATH}`);
  fs.copyFileSync(PLUGIN_JSON_PATH, BACKUP_PATH);

  // Write transformed
  log(`Writing transformed plugin.json`);
  fs.writeFileSync(
    PLUGIN_JSON_PATH,
    JSON.stringify(transformed, null, 2) + '\n',
    'utf-8'
  );

  log('Migration COMPLETE');
  log(`Backup saved to: ${BACKUP_PATH}`);
}

try {
  main();
  process.exit(0);
} catch (err) {
  console.error(`[migrate-plugin-json] ERROR: ${err.message}`);
  process.exit(1);
}
