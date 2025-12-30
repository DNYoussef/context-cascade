#!/usr/bin/env node
/**
 * rollback.js
 * Rollback migration by restoring from .backup files
 *
 * Usage:
 *   node rollback.js [--phase plugin|skills|agents|all] [--dry-run]
 */

const fs = require('fs');
const path = require('path');

const ROOT_DIR = path.resolve(__dirname, '../..');
const DRY_RUN = process.argv.includes('--dry-run');

// Parse phase argument
let phase = 'all';
const phaseIdx = process.argv.indexOf('--phase');
if (phaseIdx !== -1 && process.argv[phaseIdx + 1]) {
  phase = process.argv[phaseIdx + 1];
}

let stats = {
  restored: 0,
  notFound: 0,
  errors: 0
};

function log(msg) {
  console.log(`[rollback] ${msg}`);
}

function findBackupFiles(dir, pattern) {
  const results = [];

  function walk(currentDir) {
    if (!fs.existsSync(currentDir)) return;
    const items = fs.readdirSync(currentDir);
    for (const item of items) {
      const fullPath = path.join(currentDir, item);
      const stat = fs.statSync(fullPath);
      if (stat.isDirectory()) {
        walk(fullPath);
      } else if (pattern.test(item)) {
        results.push(fullPath);
      }
    }
  }

  walk(dir);
  return results;
}

function restoreFromBackup(backupPath) {
  const originalPath = backupPath.replace(/\.backup$/, '');

  if (!fs.existsSync(backupPath)) {
    log(`  NOT FOUND: ${backupPath}`);
    stats.notFound++;
    return false;
  }

  try {
    if (DRY_RUN) {
      log(`  Would restore: ${originalPath}`);
    } else {
      fs.copyFileSync(backupPath, originalPath);
      fs.unlinkSync(backupPath);
      log(`  RESTORED: ${originalPath}`);
    }
    stats.restored++;
    return true;
  } catch (err) {
    log(`  ERROR: ${err.message}`);
    stats.errors++;
    return false;
  }
}

function rollbackPlugin() {
  log('Rolling back plugin.json...');
  const backupPath = path.join(ROOT_DIR, '.claude-plugin', 'plugin.json.backup');
  restoreFromBackup(backupPath);
}

function rollbackSkills() {
  log('Rolling back skills...');
  const skillsDir = path.join(ROOT_DIR, 'skills');
  const backups = findBackupFiles(skillsDir, /SKILL\.md\.backup$/);
  log(`Found ${backups.length} skill backups`);

  for (const backup of backups) {
    restoreFromBackup(backup);
  }
}

function rollbackAgents() {
  log('Rolling back agents...');
  const agentsDir = path.join(ROOT_DIR, 'agents');
  const backups = findBackupFiles(agentsDir, /\.md\.backup$/);
  log(`Found ${backups.length} agent backups`);

  for (const backup of backups) {
    restoreFromBackup(backup);
  }
}

function main() {
  log(`Starting rollback (phase: ${phase})...`);

  if (DRY_RUN) {
    log('DRY RUN MODE - no files will be modified');
  }

  switch (phase) {
    case 'plugin':
      rollbackPlugin();
      break;
    case 'skills':
      rollbackSkills();
      break;
    case 'agents':
      rollbackAgents();
      break;
    case 'all':
      rollbackPlugin();
      rollbackSkills();
      rollbackAgents();
      break;
    default:
      log(`Unknown phase: ${phase}`);
      log('Valid phases: plugin, skills, agents, all');
      process.exit(1);
  }

  log('\n--- ROLLBACK SUMMARY ---');
  log(`Restored:   ${stats.restored}`);
  log(`Not found:  ${stats.notFound}`);
  log(`Errors:     ${stats.errors}`);
  log('--- END SUMMARY ---');
}

try {
  main();
  process.exit(stats.errors > 0 ? 1 : 0);
} catch (err) {
  console.error(`[rollback] FATAL: ${err.message}`);
  process.exit(1);
}
