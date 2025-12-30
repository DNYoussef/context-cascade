#!/usr/bin/env node
/**
 * migrate-agents.js
 * Transforms all agent .md files to Anthropic official format
 *
 * Usage:
 *   node migrate-agents.js [--dry-run] [--verbose]
 */

const fs = require('fs');
const path = require('path');

const AGENTS_DIR = path.resolve(__dirname, '../../agents');
const DRY_RUN = process.argv.includes('--dry-run');
const VERBOSE = process.argv.includes('--verbose');

let stats = {
  total: 0,
  transformed: 0,
  skipped: 0,
  errors: 0
};

function log(msg) {
  console.log(`[migrate-agents] ${msg}`);
}

function verbose(msg) {
  if (VERBOSE) console.log(`  ${msg}`);
}

function findAgentFiles(dir) {
  const results = [];
  const excludeFiles = ['README.md', 'index.md'];
  const excludeDirs = ['.backup', 'node_modules', '.git'];

  function walk(currentDir) {
    const items = fs.readdirSync(currentDir);
    for (const item of items) {
      const fullPath = path.join(currentDir, item);
      const stat = fs.statSync(fullPath);
      if (stat.isDirectory()) {
        // Skip excluded directories
        if (!excludeDirs.includes(item)) {
          walk(fullPath);
        }
      } else if (item.endsWith('.md') && !excludeFiles.includes(item)) {
        // Check if it looks like an agent file (has YAML frontmatter)
        const content = fs.readFileSync(fullPath, 'utf-8');
        if (content.startsWith('---') || content.match(/^\s*\/\*/)) {
          results.push(fullPath);
        }
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

  // Parse YAML (simplified for our structure)
  const frontmatter = {};
  let currentKey = null;
  let currentObject = null;
  let indent = 0;

  // Normalize line endings (remove \r)
  const lines = frontmatterRaw.split('\n').map(l => l.replace(/\r$/, ''));

  for (const line of lines) {
    if (line.trim() === '') continue;

    // Detect indentation
    const lineIndent = line.match(/^(\s*)/)[1].length;

    // Handle array items
    if (line.match(/^\s*- /)) {
      const value = line.replace(/^\s*- /, '').trim();
      if (currentKey && Array.isArray(frontmatter[currentKey])) {
        frontmatter[currentKey].push(value);
      } else if (currentObject && currentKey) {
        if (!frontmatter[currentObject]) frontmatter[currentObject] = {};
        if (!frontmatter[currentObject][currentKey]) frontmatter[currentObject][currentKey] = [];
        frontmatter[currentObject][currentKey].push(value);
      }
      continue;
    }

    // Handle key: value pairs
    const kvMatch = line.match(/^(\s*)([a-z_]+):\s*(.*)$/i);
    if (kvMatch) {
      const [, spaces, key, value] = kvMatch;
      const keyIndent = spaces.length;

      if (keyIndent === 0) {
        // Top-level key
        currentObject = null;
        currentKey = key;

        if (value === '' || value === '|') {
          frontmatter[key] = '';
        } else if (value.startsWith('[') && value.endsWith(']')) {
          // Inline array
          frontmatter[key] = value.slice(1, -1).split(',').map(s => s.trim());
        } else if (value.startsWith('{')) {
          // Inline object - skip for now
          frontmatter[key] = value;
        } else {
          frontmatter[key] = value.replace(/^["']|["']$/g, '');
        }
      } else if (keyIndent > 0) {
        // Nested key
        if (!currentObject && currentKey) {
          // This is the start of an object
          currentObject = currentKey;
          frontmatter[currentObject] = frontmatter[currentObject] || {};
        }

        if (currentObject) {
          if (value === '' || value === '|') {
            frontmatter[currentObject][key] = '';
            currentKey = key;
          } else if (value.startsWith('[') && value.endsWith(']')) {
            frontmatter[currentObject][key] = value.slice(1, -1).split(',').map(s => s.trim());
          } else {
            frontmatter[currentObject][key] = value.replace(/^["']|["']$/g, '');
          }
        }
      }
      continue;
    }

    // Handle multiline continuation
    if (currentKey && line.startsWith('  ') && !line.match(/^\s+[a-z_]+:/i)) {
      if (currentObject && frontmatter[currentObject] && typeof frontmatter[currentObject][currentKey] === 'string') {
        frontmatter[currentObject][currentKey] += '\n' + line.trim();
      } else if (typeof frontmatter[currentKey] === 'string') {
        frontmatter[currentKey] += '\n' + line.trim();
      }
    }
  }

  return { frontmatter, body };
}

function extractPlainDescription(verixDescription) {
  if (!verixDescription) return '';

  // Remove VERIX notation
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

function extractTools(frontmatter) {
  // Try to get tools from rbac.allowed_tools
  if (frontmatter.rbac && frontmatter.rbac.allowed_tools) {
    const tools = frontmatter.rbac.allowed_tools;
    if (Array.isArray(tools)) {
      return tools.join(', ');
    }
    return tools;
  }

  // Default tools
  return 'Read, Write, Edit, Bash, Glob, Grep';
}

function transformAgent(content, filePath) {
  const { frontmatter, body } = parseYamlFrontmatter(content);

  if (!frontmatter) {
    return { transformed: false, reason: 'No frontmatter found' };
  }

  if (!frontmatter.name) {
    return { transformed: false, reason: 'No name field' };
  }

  // Build new frontmatter with official fields first
  const newFrontmatter = {
    name: frontmatter.name.replace(/^["']|["']$/g, ''),
    description: extractPlainDescription(frontmatter.description) || frontmatter.name,
    tools: extractTools(frontmatter),
    model: 'sonnet'  // Default model
  };

  // Preserve custom fields with x- prefix
  if (frontmatter.type) {
    newFrontmatter['x-type'] = frontmatter.type;
  }
  if (frontmatter.color) {
    newFrontmatter['x-color'] = frontmatter.color;
  }
  if (frontmatter.capabilities) {
    newFrontmatter['x-capabilities'] = frontmatter.capabilities;
  }
  if (frontmatter.priority) {
    newFrontmatter['x-priority'] = frontmatter.priority;
  }
  if (frontmatter.identity) {
    newFrontmatter['x-identity'] = frontmatter.identity;
  }
  if (frontmatter.rbac) {
    // Keep rbac but remove allowed_tools (now in 'tools')
    const rbacCopy = { ...frontmatter.rbac };
    delete rbacCopy.allowed_tools;
    if (Object.keys(rbacCopy).length > 0) {
      newFrontmatter['x-rbac'] = rbacCopy;
    }
  }
  if (frontmatter.budget) {
    newFrontmatter['x-budget'] = frontmatter.budget;
  }
  if (frontmatter.metadata) {
    newFrontmatter['x-metadata'] = frontmatter.metadata;
  }

  // Preserve original VERIX description
  if (frontmatter.description && frontmatter.description.includes('[')) {
    newFrontmatter['x-verix-description'] = frontmatter.description;
  }

  // Build new YAML
  let yaml = '---\n';
  yaml += `name: ${newFrontmatter.name}\n`;
  yaml += `description: ${newFrontmatter.description}\n`;
  yaml += `tools: ${newFrontmatter.tools}\n`;
  yaml += `model: ${newFrontmatter.model}\n`;

  // Add x- fields
  for (const [key, value] of Object.entries(newFrontmatter)) {
    if (key.startsWith('x-')) {
      if (Array.isArray(value)) {
        yaml += `${key}:\n`;
        value.forEach(v => yaml += `  - ${v}\n`);
      } else if (typeof value === 'object' && value !== null) {
        yaml += `${key}:\n`;
        for (const [k, v] of Object.entries(value)) {
          if (Array.isArray(v)) {
            yaml += `  ${k}:\n`;
            v.forEach(item => yaml += `    - ${item}\n`);
          } else if (typeof v === 'object' && v !== null) {
            yaml += `  ${k}:\n`;
            for (const [k2, v2] of Object.entries(v)) {
              yaml += `    ${k2}: ${JSON.stringify(v2)}\n`;
            }
          } else {
            yaml += `  ${k}: ${v}\n`;
          }
        }
      } else {
        // Escape multiline strings
        if (typeof value === 'string' && value.includes('\n')) {
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
    .trim();

  return {
    transformed: true,
    content: yaml + newBody
  };
}

function main() {
  log('Starting agents migration...');

  if (DRY_RUN) {
    log('DRY RUN MODE - no files will be modified');
  }

  // Find all agent files
  log(`Scanning ${AGENTS_DIR}...`);
  const agentFiles = findAgentFiles(AGENTS_DIR);
  stats.total = agentFiles.length;
  log(`Found ${stats.total} agent files`);

  for (const filePath of agentFiles) {
    const relativePath = path.relative(AGENTS_DIR, filePath);
    verbose(`Processing: ${relativePath}`);

    try {
      const content = fs.readFileSync(filePath, 'utf-8');
      const result = transformAgent(content, filePath);

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
      console.error(`  ERROR processing ${relativePath}: ${err.message}`);
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
  console.error(`[migrate-agents] FATAL: ${err.message}`);
  process.exit(1);
}
