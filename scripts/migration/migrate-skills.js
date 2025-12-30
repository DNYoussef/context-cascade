#!/usr/bin/env node
/**
 * migrate-skills.js
 * Transforms all SKILL.md files to Anthropic official format
 *
 * Usage:
 *   node migrate-skills.js [--dry-run] [--verbose]
 */

const fs = require('fs');
const path = require('path');

const SKILLS_DIR = path.resolve(__dirname, '../../skills');
const DRY_RUN = process.argv.includes('--dry-run');
const VERBOSE = process.argv.includes('--verbose');

let stats = {
  total: 0,
  transformed: 0,
  skipped: 0,
  errors: 0
};

function log(msg) {
  console.log(`[migrate-skills] ${msg}`);
}

function verbose(msg) {
  if (VERBOSE) console.log(`  ${msg}`);
}

function findSkillFiles(dir) {
  const results = [];

  function walk(currentDir) {
    const items = fs.readdirSync(currentDir);
    for (const item of items) {
      const fullPath = path.join(currentDir, item);
      const stat = fs.statSync(fullPath);
      if (stat.isDirectory()) {
        walk(fullPath);
      } else if (item === 'SKILL.md') {
        results.push(fullPath);
      }
    }
  }

  walk(dir);
  return results;
}

function parseYamlFrontmatter(content) {
  // Skip any leading /* */ comment blocks before frontmatter
  let cleanContent = content;

  // Remove leading comment blocks (/* ... */)
  while (cleanContent.match(/^\s*\/\*[\s\S]*?\*\/\s*/)) {
    cleanContent = cleanContent.replace(/^\s*\/\*[\s\S]*?\*\/\s*/, '');
  }

  // Handle both LF and CRLF line endings
  const match = cleanContent.match(/^---\r?\n([\s\S]*?)\r?\n---/);
  if (!match) return { frontmatter: null, body: content };

  const frontmatterRaw = match[1];
  // Calculate where body starts in original content
  const frontmatterEndInClean = match[0].length;
  const prefixLength = content.length - cleanContent.length;
  const body = content.slice(prefixLength + frontmatterEndInClean).trim();

  // Simple YAML parser for our known structure
  const frontmatter = {};
  let currentKey = null;

  let currentValue = [];
  let inMultiline = false;
  let inArray = false;
  let inObject = false;
  let objectKey = null;
  let objectData = {};

  // Normalize line endings (remove \r)
  const lines = frontmatterRaw.split('\n').map(l => l.replace(/\r$/, ''));

  for (const line of lines) {
    // Handle array items
    if (line.match(/^- /)) {
      if (currentKey && !frontmatter[currentKey]) {
        frontmatter[currentKey] = [];
      }
      if (currentKey) {
        frontmatter[currentKey].push(line.replace(/^- /, '').trim());
      }
      continue;
    }

    // Handle key: value
    const kvMatch = line.match(/^([a-z_]+):\s*(.*)$/i);
    if (kvMatch) {
      const [, key, value] = kvMatch;

      if (value === '' || value === '|') {
        // Multiline or empty - will collect on next lines
        currentKey = key;
        inMultiline = value === '|';
        frontmatter[key] = '';
      } else if (value.startsWith('[') && value.endsWith(']')) {
        // Inline array
        frontmatter[key] = value.slice(1, -1).split(',').map(s => s.trim());
      } else {
        frontmatter[key] = value.replace(/^["']|["']$/g, '');
      }
      continue;
    }

    // Handle multiline content
    if (currentKey && inMultiline && line.startsWith('  ')) {
      frontmatter[currentKey] += (frontmatter[currentKey] ? '\n' : '') + line.trim();
    }
  }

  return { frontmatter, body };
}

function extractPlainDescription(verixDescription) {
  if (!verixDescription) return '';

  // Remove VERIX notation: [assert|neutral], [ground:...], [conf:...], [state:...]
  let plain = verixDescription
    .replace(/\[assert\|[^\]]+\]\s*/g, '')
    .replace(/\[ground:[^\]]+\]\s*/g, '')
    .replace(/\[conf:[^\]]+\]\s*/g, '')
    .replace(/\[state:[^\]]+\]\s*/g, '')
    .replace(/\[define\|[^\]]+\]\s*/g, '')
    .replace(/\[direct\|[^\]]+\]\s*/g, '')
    .trim();

  return plain;
}

function transformSkill(content, filePath) {
  const { frontmatter, body } = parseYamlFrontmatter(content);

  if (!frontmatter) {
    return { transformed: false, reason: 'No frontmatter found' };
  }

  // Build new frontmatter with official fields first
  const newFrontmatter = {
    name: frontmatter.name,
    description: extractPlainDescription(frontmatter.description) || frontmatter.name
  };

  // Add allowed-tools if we can derive them
  // Default to common tools if not specified
  newFrontmatter['allowed-tools'] = 'Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite';

  // Preserve custom fields with x- prefix
  if (frontmatter.version) {
    newFrontmatter['x-version'] = frontmatter.version;
  }
  if (frontmatter.category) {
    newFrontmatter['x-category'] = frontmatter.category;
  }
  if (frontmatter.tags) {
    newFrontmatter['x-tags'] = frontmatter.tags;
  }
  if (frontmatter.author) {
    newFrontmatter['x-author'] = frontmatter.author;
  }
  if (frontmatter.cognitive_frame) {
    newFrontmatter['x-cognitive-frame'] = frontmatter.cognitive_frame;
  }

  // Preserve original VERIX description
  if (frontmatter.description && frontmatter.description.includes('[')) {
    newFrontmatter['x-verix-description'] = frontmatter.description;
  }

  // Build new YAML
  let yaml = '---\n';
  yaml += `name: ${newFrontmatter.name}\n`;
  yaml += `description: ${newFrontmatter.description}\n`;
  yaml += `allowed-tools: ${newFrontmatter['allowed-tools']}\n`;

  // Add x- fields
  for (const [key, value] of Object.entries(newFrontmatter)) {
    if (key.startsWith('x-')) {
      if (Array.isArray(value)) {
        yaml += `${key}:\n`;
        value.forEach(v => yaml += `  - ${v}\n`);
      } else if (typeof value === 'object') {
        yaml += `${key}:\n`;
        for (const [k, v] of Object.entries(value)) {
          yaml += `  ${k}: ${JSON.stringify(v)}\n`;
        }
      } else {
        // Escape multiline strings
        if (value.includes('\n')) {
          yaml += `${key}: |\n`;
          value.split('\n').forEach(line => yaml += `  ${line}\n`);
        } else {
          yaml += `${key}: ${value}\n`;
        }
      }
    }
  }
  yaml += '---\n\n';

  // Transform body: convert /* */ to markdown
  let newBody = body
    .replace(/\/\*={70,}\*\//g, '') // Remove separator lines
    .replace(/\/\*-{70,}\*\//g, '---') // Convert to markdown hr
    .replace(/\/\*\s*([^*]+)\s*\*\//g, '<!-- $1 -->') // Convert inline comments
    .replace(/^\/\*\n/gm, '<!--\n') // Convert block comment start
    .replace(/^\*\/$/gm, '-->') // Convert block comment end
    .trim();

  return {
    transformed: true,
    content: yaml + newBody
  };
}

function main() {
  log('Starting skills migration...');

  if (DRY_RUN) {
    log('DRY RUN MODE - no files will be modified');
  }

  // Find all SKILL.md files
  log(`Scanning ${SKILLS_DIR}...`);
  const skillFiles = findSkillFiles(SKILLS_DIR);
  stats.total = skillFiles.length;
  log(`Found ${stats.total} SKILL.md files`);

  for (const filePath of skillFiles) {
    const relativePath = path.relative(SKILLS_DIR, filePath);
    verbose(`Processing: ${relativePath}`);

    try {
      const content = fs.readFileSync(filePath, 'utf-8');
      const result = transformSkill(content, filePath);

      if (!result.transformed) {
        verbose(`  SKIPPED: ${result.reason}`);
        stats.skipped++;
        continue;
      }

      if (DRY_RUN) {
        verbose(`  Would transform (${result.content.length} bytes)`);
      } else {
        // Create backup
        fs.copyFileSync(filePath, filePath + '.backup');
        // Write transformed
        fs.writeFileSync(filePath, result.content, 'utf-8');
        verbose(`  TRANSFORMED`);
      }

      stats.transformed++;

    } catch (err) {
      console.error(`  ERROR: ${err.message}`);
      stats.errors++;
    }
  }

  log('\n--- MIGRATION SUMMARY ---');
  log(`Total files:    ${stats.total}`);
  log(`Transformed:    ${stats.transformed}`);
  log(`Skipped:        ${stats.skipped}`);
  log(`Errors:         ${stats.errors}`);
  log('--- END SUMMARY ---');
}

try {
  main();
  process.exit(stats.errors > 0 ? 1 : 0);
} catch (err) {
  console.error(`[migrate-skills] FATAL: ${err.message}`);
  process.exit(1);
}
