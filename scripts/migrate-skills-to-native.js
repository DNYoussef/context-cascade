#!/usr/bin/env node
/**
 * Migrate Context Cascade Skills to Claude Code Native Format
 *
 * This script:
 * 1. Flattens nested skills/{category}/{skill-name}/ to skills-native/{skill-name}/
 * 2. Fixes YAML frontmatter to put name/description at the top
 * 3. Preserves all other content
 */

const fs = require('fs');
const path = require('path');

const SKILLS_SOURCE = path.join(__dirname, '..', 'skills');
const SKILLS_TARGET = path.join(__dirname, '..', 'skills-native');

// Categories to scan (subdirectories of skills/)
const CATEGORIES = [
  'delivery', 'foundry', 'operations', 'orchestration',
  'platforms', 'quality', 'research', 'security',
  'specialists', 'tooling'
];

function extractFrontmatter(content) {
  let name = null;
  let description = null;

  // Extract name from anywhere in the content
  const nameMatch = content.match(/^name:\s*(.+)$/m);
  if (nameMatch) {
    name = nameMatch[1].trim();
  }

  // Extract description (can be multiline with indentation)
  // Match until we hit another YAML key (word at start of line followed by colon)
  const descMatch = content.match(/^description:\s*([\s\S]*?)(?=\n[a-z][a-z0-9_-]*:\s)/m);
  if (descMatch) {
    description = descMatch[1]
      .split('\n')
      .map(line => line.trim())
      .filter(line => line.length > 0)
      .join(' ')
      .trim();
  }

  // Remove ALL YAML blocks (between --- markers)
  let markdownContent = content.replace(/^---[\s\S]*?---\n*/gm, '');

  // Remove free-floating YAML fields that might be outside blocks
  markdownContent = markdownContent.replace(/^name:\s*[^\n]*\n?/gm, '');
  markdownContent = markdownContent.replace(/^description:\s*[\s\S]*?(?=\n[a-z_]+:|\n\n|\n#|$)/m, '');
  markdownContent = markdownContent.replace(/^version:\s*[^\n]*\n?/gm, '');
  markdownContent = markdownContent.replace(/^category:\s*[^\n]*\n?/gm, '');
  markdownContent = markdownContent.replace(/^tags:\s*\n?/gm, '');
  markdownContent = markdownContent.replace(/^author:\s*[^\n]*\n?/gm, '');
  markdownContent = markdownContent.replace(/^license:\s*[^\n]*\n?/gm, '');
  markdownContent = markdownContent.replace(/^- [a-z]+\n/gm, ''); // Remove tag list items

  // Clean up leading whitespace/newlines
  markdownContent = markdownContent.replace(/^\s*\n+/, '').trim();

  return { name, description, markdownContent };
}

function createNativeSkillMd(name, description, markdownContent) {
  // Truncate description to 1024 chars if needed
  const truncatedDesc = description && description.length > 1024
    ? description.substring(0, 1021) + '...'
    : description;

  return `---
name: ${name}
description: ${truncatedDesc || 'No description provided'}
---

${markdownContent}`;
}

function migrateSkill(sourcePath, targetDir) {
  const skillMdPath = path.join(sourcePath, 'SKILL.md');

  if (!fs.existsSync(skillMdPath)) {
    return { success: false, error: 'No SKILL.md found' };
  }

  const content = fs.readFileSync(skillMdPath, 'utf8');
  const { name, description, markdownContent } = extractFrontmatter(content);

  // Check if name is missing or is a placeholder template
  const isPlaceholder = !name || name.includes('{') || name.includes('}') || name.includes('"') || name.includes('<');
  if (isPlaceholder) {
    // Try to infer name from directory
    const inferredName = path.basename(sourcePath);
    return migrateSkillWithInferredName(sourcePath, targetDir, inferredName, content);
  }

  const newContent = createNativeSkillMd(name, description, markdownContent);

  // Create target directory
  const skillTargetDir = path.join(targetDir, name);
  if (!fs.existsSync(skillTargetDir)) {
    fs.mkdirSync(skillTargetDir, { recursive: true });
  }

  // Write new SKILL.md
  fs.writeFileSync(path.join(skillTargetDir, 'SKILL.md'), newContent);

  // Copy any other files (scripts, examples, etc.)
  const files = fs.readdirSync(sourcePath);
  for (const file of files) {
    if (file !== 'SKILL.md') {
      const srcFile = path.join(sourcePath, file);
      const destFile = path.join(skillTargetDir, file);
      const stat = fs.statSync(srcFile);
      if (stat.isDirectory()) {
        copyDirRecursive(srcFile, destFile);
      } else {
        fs.copyFileSync(srcFile, destFile);
      }
    }
  }

  return { success: true, name, description: description?.substring(0, 50) + '...' };
}

function migrateSkillWithInferredName(sourcePath, targetDir, inferredName, content) {
  // Clean up content - just use the markdown part
  let markdownContent = content;

  // Remove any existing frontmatter blocks
  markdownContent = markdownContent.replace(/^---[\s\S]*?---\n*/gm, '');
  markdownContent = markdownContent.trim();

  // Extract first paragraph as description
  const firstParagraph = markdownContent.match(/^#.*?\n\n(.*?)(?:\n\n|$)/s);
  const description = firstParagraph
    ? firstParagraph[1].replace(/\n/g, ' ').substring(0, 200)
    : `Skill for ${inferredName}`;

  const newContent = createNativeSkillMd(inferredName, description, markdownContent);

  const skillTargetDir = path.join(targetDir, inferredName);
  if (!fs.existsSync(skillTargetDir)) {
    fs.mkdirSync(skillTargetDir, { recursive: true });
  }

  fs.writeFileSync(path.join(skillTargetDir, 'SKILL.md'), newContent);

  return { success: true, name: inferredName, description: description.substring(0, 50) + '...' };
}

function copyDirRecursive(src, dest) {
  if (!fs.existsSync(dest)) {
    fs.mkdirSync(dest, { recursive: true });
  }
  const entries = fs.readdirSync(src, { withFileTypes: true });
  for (const entry of entries) {
    const srcPath = path.join(src, entry.name);
    const destPath = path.join(dest, entry.name);
    if (entry.isDirectory()) {
      copyDirRecursive(srcPath, destPath);
    } else {
      fs.copyFileSync(srcPath, destPath);
    }
  }
}

function main() {
  console.log('=== Context Cascade Skill Migration ===\n');

  // Create target directory
  if (!fs.existsSync(SKILLS_TARGET)) {
    fs.mkdirSync(SKILLS_TARGET, { recursive: true });
  }

  let totalMigrated = 0;
  let totalFailed = 0;
  const results = [];

  for (const category of CATEGORIES) {
    const categoryPath = path.join(SKILLS_SOURCE, category);

    if (!fs.existsSync(categoryPath)) {
      console.log(`Category ${category}/ not found, skipping...`);
      continue;
    }

    const skills = fs.readdirSync(categoryPath, { withFileTypes: true })
      .filter(d => d.isDirectory())
      .map(d => d.name);

    console.log(`\nProcessing ${category}/ (${skills.length} skills):`);

    for (const skill of skills) {
      const skillPath = path.join(categoryPath, skill);
      const result = migrateSkill(skillPath, SKILLS_TARGET);

      if (result.success) {
        console.log(`  [OK] ${skill} -> ${result.name}`);
        totalMigrated++;
        results.push({ category, skill, status: 'migrated', name: result.name });
      } else {
        console.log(`  [FAIL] ${skill}: ${result.error}`);
        totalFailed++;
        results.push({ category, skill, status: 'failed', error: result.error });
      }
    }
  }

  console.log('\n=== Migration Summary ===');
  console.log(`Total migrated: ${totalMigrated}`);
  console.log(`Total failed: ${totalFailed}`);
  console.log(`Output directory: ${SKILLS_TARGET}`);

  // Write results to JSON
  fs.writeFileSync(
    path.join(SKILLS_TARGET, 'migration-results.json'),
    JSON.stringify(results, null, 2)
  );

  return { migrated: totalMigrated, failed: totalFailed };
}

// Run if called directly
if (require.main === module) {
  main();
}

module.exports = { main, migrateSkill, extractFrontmatter };
