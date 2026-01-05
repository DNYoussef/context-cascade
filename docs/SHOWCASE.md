# Context Cascade - Complete AI Development System

## The Vibe Coding Showcase

This repository showcases a complete AI-assisted development system combining **three interconnected projects** that work together to create an intelligent, memory-persistent, quality-aware coding assistant.

```
+---------------------+     +----------------------+     +-------------------+
|  CONTEXT CASCADE    |<--->|  MEMORY-MCP TRIPLE   |<--->|    OBSIDIAN       |
|  (Claude Plugin)    |     |  (Persistent Memory) |     |    (Knowledge)    |
|  660 Components     |     |  Triple-Layer Store  |     |    Vault Sync     |
+---------------------+     +----------------------+     +-------------------+
         |                           |
         |                           |
         v                           v
+---------------------+     +----------------------+
| CONNASCENCE         |     |  AGENT COORDINATION  |
| ANALYZER (MCP)      |     |  WHO/WHEN/PROJECT/   |
| 7 Code Analyzers    |     |  WHY Tagging         |
+---------------------+     +----------------------+
```

---

## The Three Parts

### 1. Context Cascade Plugin (This Repository)

**What it is:** A Claude Code plugin with 660 integrated components for AI-assisted development.

| Component | Count | Purpose |
|-----------|-------|---------|
| Skills | 196 | Specialized capabilities (SKILL.md files) |
| Agents | 211 | AI agent definitions with roles |
| Commands | 223 | Slash commands for workflows |
| Playbooks | 30 | End-to-end workflow orchestration |

**Key Features:**
- 5-Phase Workflow System (intent -> prompt -> plan -> route -> execute)
- Three-Loop Development (Research + Swarm + CI/CD Recovery)
- SPARC Methodology
- Agent Registry with 10 categories
- Hook Enforcement for pattern compliance

### 2. Memory-MCP Triple System

**Repository:** [github.com/DNYoussef/memory-mcp-triple-system](https://github.com/DNYoussef/memory-mcp-triple-system)

**What it is:** An MCP server providing persistent, multi-layered memory for AI assistants.

**Architecture:**
- **Short-term** (24h): Conversation context
- **Mid-term** (7d): Project context, decisions
- **Long-term** (30d): Documentation, best practices

**Storage:**
- ChromaDB: Vector embeddings (384-dim)
- NetworkX: Knowledge graphs
- SQLite: Event logs, KV store

**Key Feature:** WHO/WHEN/PROJECT/WHY tagging protocol for agent coordination

### 3. Connascence Safety Analyzer

**Repository:** [github.com/DNYoussef/connascence-safety-analyzer](https://github.com/DNYoussef/connascence-safety-analyzer)

**What it is:** An MCP server for static code analysis detecting coupling issues.

**7 Analyzers:**
1. Connascence Analyzer (9 types)
2. NASA Safety Analyzer (Power of 10)
3. MECE Analyzer (logical organization)
4. Duplication Analyzer (code clones)
5. Clarity Linter (readability)
6. Safety Violation Detector
7. Six Sigma Quality Metrics

**Detects:**
- God Objects (>15 methods)
- Parameter Bombs (>6 params)
- Deep Nesting (>4 levels)
- Magic Literals
- Cyclomatic Complexity

---

## Quick Start Installation

### Prerequisites

- Node.js >= 18.0.0
- Python >= 3.10
- Git
- Claude Code or Claude Desktop

### Step 1: Clone All Repositories

```bash
# Create projects directory
mkdir -p ~/Projects && cd ~/Projects

# Clone Context Cascade
git clone https://github.com/DNYoussef/context-cascade.git
cd context-cascade

# Clone Memory-MCP
git clone https://github.com/DNYoussef/memory-mcp-triple-system.git ../memory-mcp-triple-system

# Clone Connascence Analyzer
git clone https://github.com/DNYoussef/connascence-safety-analyzer.git ../connascence-analyzer
```

### Step 2: Install Memory-MCP

```bash
cd ../memory-mcp-triple-system

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create data directories
mkdir -p chroma_data data logs

# Verify installation
python -c "from src.mcp.stdio_server import main; print('Memory-MCP ready!')"
```

### Step 3: Install Connascence Analyzer

```bash
cd ../connascence-analyzer

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install with MCP support
pip install -e ".[mcp]"

# Verify installation
connascence --help
```

### Step 4: Configure Claude Code

Add to `~/.claude/settings.json` (or `%APPDATA%\Claude\claude_desktop_config.json` for Claude Desktop):

```json
{
  "mcpServers": {
    "memory-mcp": {
      "command": "python",
      "args": ["-m", "src.mcp.stdio_server"],
      "cwd": "/path/to/memory-mcp-triple-system",
      "env": {
        "PYTHONPATH": "/path/to/memory-mcp-triple-system",
        "PYTHONIOENCODING": "utf-8"
      }
    },
    "connascence-analyzer": {
      "command": "python",
      "args": ["-m", "mcp.cli", "mcp-server"],
      "cwd": "/path/to/connascence-analyzer",
      "env": {
        "PYTHONPATH": "/path/to/connascence-analyzer",
        "PYTHONIOENCODING": "utf-8"
      }
    }
  },
  "enabledPlugins": {
    "context-cascade": true
  }
}
```

### Step 5: Install Context Cascade Plugin

```bash
cd ../context-cascade

# Verify npm package
npm install

# Or install as Claude Code plugin
claude plugins add ./
```

---

## How the Systems Work Together

### Agent Memory Coordination

Agents share memory via the Memory-MCP tagging protocol:

```javascript
// Code analyzer stores finding
kv.set_json("findings:code-analyzer:high:SEC-001", {
  WHO: "code-analyzer:601c545c",
  WHEN: "2025-12-28T15:00:00Z",
  PROJECT: "my-project",
  WHY: "analysis",
  finding: "SQL injection vulnerability in auth.py:42"
});

// Coder reads finding and applies fix
const finding = kv.get_json("findings:code-analyzer:high:SEC-001");
// ... applies fix ...
kv.set_json("fixes:coder:SEC-001", {
  WHO: "coder:abc123",
  WHEN: "2025-12-28T15:30:00Z",
  PROJECT: "my-project",
  WHY: "bugfix",
  fix: "Parameterized query implementation"
});

// Graph tracks relationship
graph.add_relationship("fix:SEC-001", "resolves", "finding:SEC-001");
```

### Quality Gates

The Connascence Analyzer enforces code quality:

```bash
# Analyze workspace before commit
mcp__connascence-analyzer__analyze_workspace({
  workspace_path: "./src",
  analysis_type: "full"
})

# Response includes:
{
  "violations": [...],
  "summary": {
    "critical": 0,
    "high": 2,
    "medium": 5
  }
}
```

### 5-Phase Workflow

Every request goes through:

1. **Intent Analysis** - Understand what user wants
2. **Prompt Optimization** - Structure the request
3. **Planning** - Break down into tasks
4. **Routing** - Select skills/playbooks
5. **Execution** - Spawn agents, track progress

---

## Obsidian Integration

The Memory-MCP syncs with Obsidian vaults:

### Configure Vault

In `memory-mcp-triple-system/config/memory-mcp.yaml`:

```yaml
storage:
  obsidian_vault: ~/Documents/AI-Memory-Vault
```

### Sync Commands

```python
# Sync vault to memory
client.sync_vault(file_extensions=[".md"])

# Export memories to vault
client.export_to_vault(chunks, "exported_memories.md")

# Watch for changes
client.watch_changes(callback=on_change)
```

### Vault Structure

```
AI-Memory-Vault/
  agents/
    findings/     # Issues found by agents
    fixes/        # Applied fixes
    decisions/    # Design decisions
  expertise/
    domains/      # Domain knowledge
    patterns/     # Code patterns
  projects/
    project-1/    # Project-specific memories
```

---

## Showcase Demos

### Demo 1: Smart Bug Fix with Memory

```
User: "Fix the authentication bug in auth.py"

5-Phase Flow:
1. Intent: Bug fix request, auth domain
2. Prompt: "Fix authentication vulnerability with root cause analysis"
3. Plan: Analyze -> Find root cause -> Fix -> Test -> Verify
4. Route: smart-bug-fix skill -> coder agent
5. Execute:
   - Check memory for prior findings
   - Analyze with Connascence
   - Apply fix with reasoning
   - Store fix in memory
   - Verify with tests
```

### Demo 2: Feature Development

```
User: "Add user profile editing"

5-Phase Flow:
1. Intent: New feature, user management
2. Prompt: "Implement user profile editing with validation"
3. Plan: Research -> Design -> Implement (parallel) -> Test -> Deploy
4. Route: feature-dev-complete skill
5. Execute:
   - Load domain expertise
   - Spawn 3 parallel agents (backend, frontend, tests)
   - Track progress via TodoWrite
   - Store decisions in memory
   - Run quality gates
```

---

## Component Statistics

| System | Files | Lines | Components |
|--------|-------|-------|------------|
| Context Cascade | 800+ | 100k+ | 660 |
| Memory-MCP | 150+ | 25k+ | 6 MCP tools |
| Connascence | 200+ | 30k+ | 7 analyzers |
| **Total** | 1150+ | 155k+ | 673+ |

---

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines.

## License

- Context Cascade: Apache-2.0 / MIT
- Memory-MCP: MIT
- Connascence Analyzer: MIT

---

## Links

- **Context Cascade**: [github.com/DNYoussef/context-cascade](https://github.com/DNYoussef/context-cascade)
- **Memory-MCP**: [github.com/DNYoussef/memory-mcp-triple-system](https://github.com/DNYoussef/memory-mcp-triple-system)
- **Connascence Analyzer**: [github.com/DNYoussef/connascence-safety-analyzer](https://github.com/DNYoussef/connascence-safety-analyzer)

---

*Built with Claude Code, powered by vibe coding.*
