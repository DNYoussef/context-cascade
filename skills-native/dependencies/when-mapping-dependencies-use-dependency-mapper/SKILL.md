---
name: when-mapping-dependencies-use-dependency-mapper
version: 1.0.0
description: Comprehensive dependency mapping, analysis, and visualization tool for software projects
author: Claude Code
category: analysis
complexity: MEDIUM
tags: [dependencies, graph-analysis, security, visualization, mece]
agents:
  - code-analyzer
  - researcher
  - security-manager
components:
  - subagent
  - slash-command
  - mcp-tool
dependencies:
  - claude-flow@alpha
  - graphviz (optional)
  - npm/pip/cargo (auto-detected)
---

# Dependency Mapper Skill

## Overview

**When mapping dependencies, use dependency-mapper** to extract, analyze, visualize, and audit dependency trees across multiple package managers (npm, pip, cargo, maven, go.mod).

## MECE Breakdown

### Mutually Exclusive Components:
1. **Extraction Phase**: Parse lock files and manifests
2. **Analysis Phase**: Build dependency graph and detect issues
3. **Security Phase**: Audit for vulnerabilities
4. **Visualization Phase**: Generate interactive dependency graphs
5. **Reporting Phase**: Create actionable recommendations

### Collectively Exhaustive Coverage:
- All major package managers (npm, pip, cargo, maven, go)
- Direct and transitive dependencies
- Circular dependency detection
- License compliance checking
- Security vulnerability scanning
- Outdated package detection
- Duplicate dependency identification

## Features

### Core Capabilities:
- Multi-language dependency extraction
- Dependency graph construction
- Circular dependency detection
- Security vulnerability scanning
- License compliance auditing
- Outdated package detection
- Interactive visualization generation
- Dependency optimization recommendations

### Supported Package Managers:
- **JavaScript/Node**: npm, yarn, pnpm
- **Python**: pip, poetry, pipenv
- **Rust**: cargo
- **Java**: maven, gradle
- **Go**: go.mod
- **Ruby**: bundler
- **PHP**: composer
- **C#**: nuget

## Usage

### Slash Command:
```bash
/dep-map [path] [--format json|html|svg] [--security] [--circular] [--outdated]
```

### Subagent Invocation:
```javascript
Task("Dependency Mapper", "Analyze dependencies for ./project with security audit", "code-analyzer")
```

### MCP Tool:
```javascript
mcp__dependency-mapper__analyze({
  project_path: "./project",
  include_security: true,
  detect_circular: true,
  visualization_format: "html"
})
```

## Architecture

### Phase 1: Discovery
1. Detect project type and package manager
2. Locate manifest and lock files
3. Parse dependency declarations

### Phase 2: Extraction
1. Extract direct dependencies
2. Resolve transitive dependencies
3. Build dependency tree structure

### Phase 3: Analysis
1. Detect circular dependencies
2. Identify duplicate dependencies
3. Check for outdated packages
4. Analyze dependency depth

### Phase 4: Security
1. Query vulnerability databases
2. Check license compliance
3. Identify supply chain risks
4. Generate security scores

### Phase 5: Visualization
1. Generate graph data structure
2. Create interactive HTML visualization
3. Export SVG/PNG diagrams
4. Generate dependency reports

## Output Formats

### JSON Report:
```json
{
  "project": "my-app",
  "package_manager": "npm",
  "total_dependencies": 847,
  "direct_dependencies": 23,
  "vulnerabilities": {
    "critical": 0,
    "high": 2,
    "medium": 5,
    "low": 12
  },
  "circular_dependencies": [],
  "outdated_packages": 15,
  "license_issues": 0,
  "dependency_tree": {...}
}
```

### HTML Visualization:
Interactive D3.js graph with:
- Zoomable dependency tree
- Vulnerability highlighting
- Circular dependency paths
- Click-to-expand nodes
- Search and filter capabilities

### SVG/PNG Export:
Static GraphViz-generated diagrams

## Examples

### Example 1: Basic Analysis
```bash
/dep-map ./my-project
```

### Example 2: Security-Focused Audit
```bash
/dep-map ./my-project --security --format json
```

### Example 3: Circular Dependency Detection
```bash
/dep-map ./my-project --circular --visualization svg
```

### Example 4: Full Comprehensive Analysis
```bash
/dep-map ./my-project --security --circular --outdated --format html
```

## Integration with Claude-Flow

### Coordination Pattern:
```javascript
// Step 1: Initialize swarm for complex analysis
mcp__claude-flow__swarm_init({ topology: "hierarchical", maxAgents: 4 })

// Step 2: Spawn agents via Claude Code Task tool
[Parallel Execution]:
  Task("Dependency Extractor", "Extract all dependencies from package.json and package-lock.json", "code-analyzer")
  Task("Security Auditor", "Run npm audit and cross-reference CVE databases", "security-manager")
  Task("Graph Builder", "Construct dependency graph and detect circular deps", "code-analyzer")
  Task("Visualization Generator", "Create interactive HTML dependency graph", "coder")
```

## Configuration

### Default Settings:
```json
{
  "max_depth": 10,
  "include_dev_dependencies": true,
  "security_scan_enabled": true,
  "circular_detection_enabled": true,
  "license_check_enabled": true,
  "outdated_check_enabled": true,
  "visualization_default_format": "html",
  "cache_results": true,
  "cache_ttl": 3600
}
```

## Performance Considerations

- **Caching**: Results cached for 1 hour by default
- **Parallel Processing**: Multiple package managers analyzed concurrently
- **Incremental Analysis**: Only re-analyze changed dependencies
- **Lazy Loading**: Visualization loads nodes on-demand for large graphs

## Error Handling

- Graceful degradation if package manager unavailable
- Fallback to partial analysis if network issues
- Clear error messages for invalid project structures
- Retry logic for transient failures

## Best Practices

1. Run dependency mapping before major releases
2. Integrate into CI/CD pipelines for automated auditing
3. Set up alerts for critical vulnerabilities
4. Review circular dependencies regularly
5. Keep dependency depth shallow (< 5 levels)
6. Audit licenses for compliance requirements
7. Update outdated packages incrementally

## Troubleshooting

### Issue: No dependencies found
**Solution**: Ensure lock files are present (package-lock.json, yarn.lock, etc.)

### Issue: Visualization too large to render
**Solution**: Use `--max-depth 5` to limit tree depth

### Issue: Security scan taking too long
**Solution**: Use cached results or run offline mode

## MCP Requirements

This skill requires the following MCP servers for optimal functionality:

### Filesystem MCP (18k tokens)

**Purpose**: Read package manifests and lock files across multiple languages

**Tools Used**:
- `mcp__filesystem__read_text_file`: Read package.json, requirements.txt, Cargo.toml, etc.
- `mcp__filesystem__read_multiple_files`: Batch read multiple dependency files
- `mcp__filesystem__list_directory`: Discover package manager files

**Activation** (PowerShell):
```powershell
# Check if already active
claude mcp list

# Add if not present
claude mcp add filesystem npx @modelcontextprotocol/server-filesystem start
```

**Usage Example**:
```javascript
// Read multiple package files
mcp__filesystem__read_multiple_files({
  paths: [
    "C:/Users/17175/project/package.json",
    "C:/Users/17175/project/package-lock.json",
    "C:/Users/17175/project/requirements.txt"
  ]
})

// Discover dependency files
mcp__filesystem__list_directory({ path: "C:/Users/17175/project" })

// Read specific lock file
mcp__filesystem__read_text_file({ path: "C:/Users/17175/project/yarn.lock" })
```

**Token Cost**: 18k tokens (9% of 200k context)
**When to Load**: Always (core functionality for reading dependency files)

### Memory MCP (8.5k tokens)

**Purpose**: Store dependency analysis results and vulnerability patterns

**Tools Used**:
- `mcp__memory-mcp__memory_store`: Store dependency graphs and security findings
- `mcp__memory-mcp__vector_search`: Find similar dependency patterns

**Activation** (PowerShell):
```powershell
# Already configured
claude mcp list
```

**Usage Example**:
```javascript
// Store dependency analysis
const { taggedMemoryStore } = require('./hooks/12fa/memory-mcp-tagging-protocol.js');
taggedMemoryStore('code-analyzer', JSON.stringify(dependency_graph), {
  project: 'my-app',
  total_deps: 847,
  vulnerabilities: 19
});

// Search for similar patterns
mcp__memory-mcp__vector_search({ query: "circular dependency npm packages", limit: 5 })
```

**Token Cost**: 8.5k tokens (4.25% of 200k context)
**When to Load**: Optional (for caching results)

## See Also

- PROCESS.md - Detailed step-by-step workflow
- README.md - Quick start guide
- subagent-dependency-mapper.md - Agent implementation details
- slash-command-dep-map.sh - Command-line interface
- mcp-dependency-mapper.json - MCP tool schema

---

## Core Principles

### 1. Dependency Graphs are Multi-Dimensional
Dependencies are not just a tree of packages. They encompass security vulnerabilities, license compliance, circular references, version conflicts, and supply chain risks.

**In practice:**
- Extract direct AND transitive dependencies from lock files
- Build dependency graph with depth tracking (max 10 levels)
- Detect circular dependencies using graph cycle detection algorithms
- Query vulnerability databases (npm audit, Snyk, CVE feeds)
- Check license compliance (GPL vs MIT vs proprietary)
- Identify duplicate dependencies at different versions
- Analyze dependency depth distribution (shallow vs deep trees)

### 2. Visualization Enables Comprehension
Dependency trees with 500+ packages are incomprehensible as JSON. Interactive visualizations transform data into actionable insights.

**In practice:**
- Generate interactive D3.js HTML graphs (zoomable, searchable, filterable)
- Color-code nodes by severity (red for critical vulnerabilities, yellow for outdated)
- Highlight circular dependency paths with distinct styling
- Enable click-to-expand nodes for on-demand exploration
- Export static SVG/PNG diagrams for documentation
- Provide search functionality to locate specific packages
- Show dependency depth visually (tree levels, concentric circles)

### 3. Analysis Must Be Actionable
Reports should prioritize fixes by impact and effort, not just list violations. Provide clear next steps.

**In practice:**
- Sort vulnerabilities by severity (critical > high > medium > low)
- Identify "dependency bombs" (packages pulling in 50+ transitive deps)
- Recommend specific version upgrades for outdated packages
- Suggest license-compatible alternatives for compliance issues
- Provide fix commands: "npm update package@version"
- Calculate risk scores combining vulnerability count, depth, and usage
- Generate TODO lists: "Update 15 packages", "Remove 3 circular deps", "Fix 2 critical CVEs"

---

## Anti-Patterns

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| **Only analyzing direct dependencies** | Misses 90% of supply chain risk in transitive dependencies, vulnerable packages hidden 5 levels deep | Analyze full dependency tree. Use lock files (package-lock.json, yarn.lock). Scan all transitive dependencies for vulnerabilities. |
| **Ignoring circular dependencies** | Causes build failures, infinite loops, unpredictable behavior, module initialization order issues | Detect circular dependencies using graph cycle detection. Visualize circular paths. Refactor to break cycles. |
| **No license compliance checking** | Legal risk from GPL contamination in proprietary code, license incompatibilities in combined software | Check all package licenses. Flag GPL, AGPL, copyleft licenses. Provide license-compatible alternatives. Audit before releases. |
| **Treating all vulnerabilities equally** | Wastes time on low-severity issues, misses critical remote code execution (RCE) vulnerabilities | Prioritize by severity (CVSS score). Fix critical/high first. Filter low-severity for large projects. Focus on exploitable paths. |
| **Manual dependency tracking** | Cannot scale to 500+ packages, prone to human error, misses updates, no historical tracking | Automate with dependency-mapper. Integrate into CI/CD pipelines. Set up automated alerts for new CVEs. Cache results. |
| **No visualization for large graphs** | JSON reports with 500 packages are unreadable, cannot identify patterns, misses structural issues | Generate interactive HTML visualizations. Use D3.js for zoomable graphs. Export SVG for documentation. Enable search/filter. |

---

## Conclusion

The Dependency Mapper skill transforms dependency management from a reactive firefighting exercise into a proactive engineering discipline. By treating dependencies as a multi-dimensional problem - spanning security, licensing, architecture, and supply chain risk - this skill provides comprehensive visibility into the often-hidden complexity of modern software projects.

The five-phase workflow (discovery, extraction, analysis, security, visualization) ensures that dependency mapping is thorough, automated, and actionable. Whether analyzing a small Python project with 20 packages or a large Node.js monorepo with 800+ dependencies, this skill scales from quick audits to comprehensive security reviews.

By integrating interactive visualizations (D3.js graphs), multi-language support (npm, pip, cargo, maven, go.mod), and actionable recommendations (prioritized fix lists), the Dependency Mapper makes complex dependency trees comprehensible and manageable. The result is reduced supply chain risk, faster vulnerability remediation, and better architectural decisions based on dependency health metrics.
