---
name: when-mapping-dependencies-use-dependency-mapper
description: Comprehensive dependency mapping, analysis, and visualization tool for software projects
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

## Core Principles

### 1. Comprehensive Multi-Dimensional Analysis
Dependency mapping is not just listing packages - it requires analyzing structure, security, licenses, and maintainability across all dimensions.

In practice:
- Extract both direct dependencies (package.json) and transitive dependencies (lock files)
- Build complete dependency graph with depth tracking (flag if depth > 5 levels)
- Detect circular dependencies using graph cycle detection algorithms
- Scan for security vulnerabilities by querying CVE databases (npm audit, pip-audit, cargo audit)
- Check license compliance against organizational policies (GPL, MIT, Apache compatibility)
- Identify duplicate dependencies (different versions of same package in tree)
- Analyze dependency health metrics (last update date, maintainer count, download statistics)

### 2. Multi-Language Unified Approach
Different package managers share common dependency patterns - extract abstractions that work across npm, pip, cargo, maven, go.mod.

In practice:
- Auto-detect package manager from manifest files (package.json, requirements.txt, Cargo.toml, pom.xml, go.mod)
- Use normalized dependency graph format across all languages (name, version, dependents, dependencies, depth, licenses, vulnerabilities)
- Run parallel analysis for multi-language projects (Node.js backend + Python ML service + Rust performance library)
- Aggregate results into unified report showing cross-language dependency relationships
- Handle package manager specifics (npm devDependencies, Python extras, Cargo features) with language adapters

### 3. Actionable Recommendations Over Raw Data
Dependency reports must guide decisions, not just present information - provide prioritized recommendations with clear remediation paths.

In practice:
- Rank vulnerabilities by severity (critical > high > medium > low) and exploitability (CVSS score, proof-of-concept exists)
- Identify circular dependencies with specific file paths causing cycles
- Highlight outdated packages with available updates, grouped by breaking changes (major, minor, patch)
- Detect duplicate dependencies with recommendations to deduplicate (use resolutions field in package.json, consolidate versions)
- Flag license conflicts with specific incompatible combinations (GPL dependency in proprietary project)
- Generate visual dependency graphs with problematic nodes highlighted (red = vulnerability, yellow = outdated, orange = circular)

## Anti-Patterns

| Anti-Pattern | Problem | Solution |
|-------------|---------|----------|
| Analyzing only direct dependencies | Misses 90% of actual dependencies (transitive) and vulnerabilities | Always analyze full dependency tree from lock files (package-lock.json, yarn.lock, Pipfile.lock). Direct dependencies are < 10% of total. Vulnerabilities hide in transitive deps. |
| Ignoring circular dependencies | Creates brittle coupling, prevents tree-shaking, causes runtime errors | Run cycle detection algorithms on dependency graph. Flag circular deps as critical issues. Visualize cycle paths. Refactor to break cycles through dependency inversion or abstraction layers. |
| No security vulnerability scanning | Ships known CVEs to production, exposes attack surface | Integrate security audits in CI/CD (npm audit, pip-audit, cargo audit, Snyk, Dependabot). Block builds on critical vulnerabilities. Auto-update security patches with automated testing. |
| Allowing unbounded dependency depth | Deep trees (> 5 levels) increase attack surface, slow installs, create conflicts | Set maximum dependency depth threshold (4-5 levels). Flag violations in CI/CD. Prefer libraries with flat dependency trees. Consider bundling/vendoring deep transitive deps. |
| Missing license compliance checks | Legal liability from incompatible license combinations (GPL + proprietary) | Scan all dependency licenses. Define allowed licenses policy (MIT, Apache, BSD). Block GPL dependencies in proprietary projects. Use SPDX identifiers for unambiguous license detection. |
| Stale dependency audits | Vulnerabilities discovered after last audit, false sense of security | Run dependency audits on every commit in CI/CD. Cache results for 1 hour maximum. Subscribe to security advisories for critical dependencies. Re-audit weekly minimum. |

## Conclusion

Dependency Mapper provides comprehensive visibility into the software supply chain by extracting, analyzing, and visualizing dependency trees across multiple package managers and languages. In modern software, direct dependencies are typically less than 10% of total dependencies - the remaining 90% are transitive dependencies pulled in automatically, creating hidden security vulnerabilities, license conflicts, and version conflicts that surface only in production.

This skill addresses the dependency analysis challenge through a five-phase workflow: Discovery (detect package managers and locate manifest files), Extraction (parse declarations and resolve transitive dependencies), Analysis (detect circular dependencies, duplicates, depth issues), Security (query vulnerability databases, check licenses, assess supply chain risks), and Visualization (generate interactive graphs with problematic nodes highlighted). Each phase builds on the previous, creating a complete picture from raw dependency declarations to actionable remediation recommendations.

The multi-language unified approach recognizes that modern applications often combine multiple ecosystems (Node.js frontend, Python ML service, Rust performance library, Go microservices). By abstracting common dependency patterns and using language-specific adapters for package manager nuances, the skill produces unified reports showing cross-language relationships and aggregated security posture. This holistic view prevents gaps where vulnerabilities hide at ecosystem boundaries.

Most critically, Dependency Mapper transforms raw dependency data into prioritized recommendations that guide decision-making. Instead of overwhelming developers with thousands of dependencies, the skill highlights critical issues: vulnerabilities ranked by severity and exploitability, circular dependencies with specific cycle paths, outdated packages grouped by breaking change risk, license conflicts with incompatible combinations, and duplicate dependencies with deduplication strategies. This actionable intelligence enables teams to systematically improve dependency health without getting lost in complexity. Integration with CI/CD pipelines ensures dependency audits run on every commit, catching issues before they reach production and maintaining continuous visibility into the evolving software supply chain.