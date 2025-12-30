const fs = require('fs');
const path = require('path');

const testFile = path.join(__dirname, '../../agents/delivery/sparc/specification.md');

console.log('Reading:', testFile);
const content = fs.readFileSync(testFile, 'utf-8');

// Try the YAML parser from migrate-agents.js
let cleanContent = content;
while (cleanContent.match(/^\s*\/\*[\s\S]*?\*\/\s*/)) {
  cleanContent = cleanContent.replace(/^\s*\/\*[\s\S]*?\*\/\s*/, '');
}

const match = cleanContent.match(/^---\r?\n([\s\S]*?)\r?\n---/);
if (!match) {
  console.log('No YAML match found');
  process.exit(1);
}

const frontmatterRaw = match[1];
console.log('Frontmatter raw first 500 chars:');
console.log(frontmatterRaw.slice(0, 500));
console.log('\n--- Parsing lines ---');

const frontmatter = {};
let currentKey = null;
let currentObject = null;

const lines = frontmatterRaw.split('\n');
for (let i = 0; i < Math.min(10, lines.length); i++) {
  const line = lines[i];
  if (line.trim() === '') continue;

  // Show raw line
  console.log(`\nLine ${i}: ${JSON.stringify(line)}`);

  // Handle key: value pairs - note the regex pattern
  const kvMatch = line.match(/^(\s*)([a-z_]+):\s*(.*)$/i);
  console.log('  kvMatch:', kvMatch ? 'YES' : 'NO');

  if (kvMatch) {
    const [, spaces, key, value] = kvMatch;
    console.log(`  -> key="${key}", value="${value}", indent=${spaces.length}`);
  }
}

console.log('\n--- Testing name regex specifically ---');
const nameLine = lines.find(l => l.includes('name'));
console.log('Name line:', JSON.stringify(nameLine));
const nameMatch = nameLine ? nameLine.match(/^(\s*)([a-z_]+):\s*(.*)$/i) : null;
console.log('Name match:', nameMatch);
