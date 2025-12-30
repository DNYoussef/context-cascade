#!/usr/bin/env node
/**
 * run-migration.js
 * Master migration script - runs all phases in order
 *
 * Usage:
 *   node run-migration.js [--dry-run] [--skip-backup] [--verbose]
 */

const { execSync, spawnSync } = require('child_process');
const fs = require('fs');
const path = require('path');

const ROOT_DIR = path.resolve(__dirname, '../..');
const SCRIPTS_DIR = __dirname;

const DRY_RUN = process.argv.includes('--dry-run');
const SKIP_BACKUP = process.argv.includes('--skip-backup');
const VERBOSE = process.argv.includes('--verbose');

function log(msg) {
  console.log(`\n${'='.repeat(60)}`);
  console.log(`[MIGRATION] ${msg}`);
  console.log('='.repeat(60));
}

function runScript(scriptName, args = []) {
  const scriptPath = path.join(SCRIPTS_DIR, scriptName);
  const fullArgs = [...args];
  if (DRY_RUN) fullArgs.push('--dry-run');
  if (VERBOSE) fullArgs.push('--verbose');

  console.log(`\nRunning: node ${scriptName} ${fullArgs.join(' ')}`);

  const result = spawnSync('node', [scriptPath, ...fullArgs], {
    cwd: SCRIPTS_DIR,
    stdio: 'inherit',
    shell: true
  });

  if (result.status !== 0) {
    throw new Error(`Script ${scriptName} failed with exit code ${result.status}`);
  }

  return result;
}

function createGitBackup() {
  log('PHASE 0: Creating Git Backup');

  if (SKIP_BACKUP) {
    console.log('Skipping backup (--skip-backup flag)');
    return;
  }

  try {
    // Check if in git repo
    execSync('git rev-parse --is-inside-work-tree', { cwd: ROOT_DIR, stdio: 'pipe' });

    // Check for uncommitted changes
    const status = execSync('git status --porcelain', { cwd: ROOT_DIR, encoding: 'utf-8' });

    if (status.trim()) {
      console.log('Uncommitted changes detected. Creating checkpoint commit...');
      if (!DRY_RUN) {
        execSync('git add -A', { cwd: ROOT_DIR, stdio: 'inherit' });
        execSync('git commit -m "chore: pre-migration checkpoint"', { cwd: ROOT_DIR, stdio: 'inherit' });
      } else {
        console.log('[DRY RUN] Would commit current changes');
      }
    }

    // Create tag
    console.log('Creating pre-migration tag...');
    if (!DRY_RUN) {
      try {
        execSync('git tag -d pre-migration-backup 2>nul', { cwd: ROOT_DIR, stdio: 'pipe' });
      } catch (e) { /* Tag might not exist */ }
      execSync('git tag pre-migration-backup', { cwd: ROOT_DIR, stdio: 'inherit' });
    } else {
      console.log('[DRY RUN] Would create tag: pre-migration-backup');
    }

    console.log('Git backup complete. To rollback: git reset --hard pre-migration-backup');

  } catch (err) {
    console.log('Not a git repository or git not available. Skipping git backup.');
  }
}

function main() {
  console.log(`
${'#'.repeat(60)}
#                                                          #
#          ANTHROPIC FORMAT COMPLIANCE MIGRATION           #
#                                                          #
#  This will transform your plugin to official format      #
#  All original data will be preserved with x- prefix      #
#                                                          #
${'#'.repeat(60)}
`);

  if (DRY_RUN) {
    console.log('*** DRY RUN MODE - No files will be modified ***\n');
  }

  // Phase 0: Backup
  createGitBackup();

  // Phase 1: Plugin.json
  log('PHASE 1: Migrating plugin.json');
  runScript('migrate-plugin-json.js');

  // Phase 2: Skills
  log('PHASE 2: Migrating Skills (196 files)');
  runScript('migrate-skills.js');

  // Phase 3: Agents
  log('PHASE 3: Migrating Agents (211 files)');
  runScript('migrate-agents.js');

  // Phase 4: Validation
  log('PHASE 4: Validating Results');
  try {
    runScript('validate-all.js');
  } catch (err) {
    console.log('\nValidation found some issues. Review the report above.');
    console.log('You can rollback with: node rollback.js --phase all');
  }

  // Summary
  log('MIGRATION COMPLETE');

  console.log(`
Next steps:
1. Review the validation report above
2. Test the plugin with Claude Code
3. If issues: node rollback.js --phase all
4. If success: git add -A && git commit -m "feat: migrate to Anthropic format"
`);
}

try {
  main();
} catch (err) {
  console.error(`\n[MIGRATION FAILED] ${err.message}`);
  console.log('\nTo rollback:');
  console.log('  git reset --hard pre-migration-backup');
  console.log('  OR');
  console.log('  node rollback.js --phase all');
  process.exit(1);
}
