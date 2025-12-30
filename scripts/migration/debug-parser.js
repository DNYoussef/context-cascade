const fs = require('fs');
const path = require('path');

const testFile = path.join(__dirname, '../../skills/delivery/feature-dev-complete/SKILL.md');

console.log('Reading:', testFile);
const content = fs.readFileSync(testFile, 'utf-8');

console.log('File length:', content.length);
console.log('First 300 chars:');
console.log(content.slice(0, 300));
console.log('---');

// Try the regex
let cleanContent = content;

console.log('\nLooking for comment blocks...');
const commentMatch = cleanContent.match(/^\s*\/\*[\s\S]*?\*\/\s*/);
console.log('Comment match found:', !!commentMatch);

if (commentMatch) {
  console.log('Match length:', commentMatch[0].length);
  console.log('Match preview:', commentMatch[0].slice(0, 100));
}

// Remove leading comment blocks
let iterations = 0;
while (cleanContent.match(/^\s*\/\*[\s\S]*?\*\/\s*/) && iterations < 10) {
  cleanContent = cleanContent.replace(/^\s*\/\*[\s\S]*?\*\/\s*/, '');
  iterations++;
  console.log('Iteration', iterations, '- remaining length:', cleanContent.length);
}

console.log('\nClean content first 200:');
console.log(cleanContent.slice(0, 200));
console.log('---');

// Handle both LF and CRLF
const yamlMatch = cleanContent.match(/^---\r?\n([\s\S]*?)\r?\n---/);
console.log('\nYAML frontmatter found:', !!yamlMatch);

if (yamlMatch) {
  console.log('Frontmatter:');
  console.log(yamlMatch[1].slice(0, 500));
}
