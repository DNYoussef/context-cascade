# Installation Guide

## Complete Setup for Context Cascade + Memory-MCP + Connascence Analyzer

This guide covers setting up the complete 3-part AI development system.

---

## System Requirements

| Requirement | Minimum | Recommended |
|-------------|---------|-------------|
| Node.js | 18.0.0 | 20.x LTS |
| Python | 3.10 | 3.11/3.12 |
| RAM | 4GB | 8GB+ |
| Disk | 2GB | 5GB+ |
| OS | Windows 10, macOS 12, Ubuntu 20.04 | Latest |

---

## Quick Install (One Command)

### Windows (PowerShell)

```powershell
# Run as Administrator
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Clone and setup all systems
$ProjectDir = "$env:USERPROFILE\Projects"
New-Item -ItemType Directory -Force -Path $ProjectDir
Set-Location $ProjectDir

# Clone repositories
git clone https://github.com/DNYoussef/context-cascade.git
git clone https://github.com/DNYoussef/memory-mcp-triple-system.git
git clone https://github.com/DNYoussef/connascence-safety-analyzer.git

# Setup Memory-MCP
Set-Location memory-mcp-triple-system
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
New-Item -ItemType Directory -Force -Path chroma_data,data,logs
deactivate

# Setup Connascence Analyzer
Set-Location ..\connascence-safety-analyzer
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -e ".[mcp]"
deactivate

# Return to Context Cascade
Set-Location ..\context-cascade
npm install

Write-Host "Installation complete! Configure Claude Code settings next."
```

### macOS/Linux (Bash)

```bash
#!/bin/bash

PROJECT_DIR="${HOME}/Projects"
mkdir -p "$PROJECT_DIR" && cd "$PROJECT_DIR"

# Clone repositories
git clone https://github.com/DNYoussef/context-cascade.git
git clone https://github.com/DNYoussef/memory-mcp-triple-system.git
git clone https://github.com/DNYoussef/connascence-safety-analyzer.git

# Setup Memory-MCP
cd memory-mcp-triple-system
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
mkdir -p chroma_data data logs
deactivate

# Setup Connascence Analyzer
cd ../connascence-safety-analyzer
python3 -m venv venv
source venv/bin/activate
pip install -e ".[mcp]"
deactivate

# Setup Context Cascade
cd ../context-cascade
npm install

echo "Installation complete! Configure Claude Code settings next."
```

---

## Step-by-Step Installation

### Part 1: Memory-MCP Triple System

```bash
cd ~/Projects/memory-mcp-triple-system

# Create Python environment
python -m venv venv
source venv/bin/activate  # Windows: .\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Create data directories
mkdir -p chroma_data data logs

# Verify installation
python -c "from src.mcp.stdio_server import main; print('OK')"
```

**Configuration** (`config/memory-mcp.yaml`):

```yaml
storage:
  data_dir: ./data
  obsidian_vault: ~/Documents/AI-Memory-Vault  # Optional
  vector_db:
    type: chromadb
    persist_directory: ./chroma_data
```

### Part 2: Connascence Safety Analyzer

```bash
cd ~/Projects/connascence-safety-analyzer

# Create Python environment
python -m venv venv
source venv/bin/activate

# Install with MCP support
pip install -e ".[mcp]"

# Verify CLI
connascence --help

# Verify MCP server
python -m mcp.cli health-check
```

### Part 3: Context Cascade Plugin

```bash
cd ~/Projects/context-cascade

# Install npm dependencies
npm install

# Verify plugin structure
ls -la .claude-plugin/
```

---

## Claude Code Configuration

### Option A: Claude Code CLI

Edit `~/.claude/settings.json`:

```json
{
  "enabledMcpjsonServers": [
    "memory-mcp",
    "connascence-analyzer",
    "claude-flow"
  ],
  "extraKnownMarketplaces": {
    "context-cascade": {
      "source": {
        "source": "directory",
        "path": "/path/to/context-cascade"
      }
    }
  },
  "enabledPlugins": {
    "context-cascade": true
  }
}
```

### Option B: Claude Desktop

Edit the config file:
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Linux**: `~/.config/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "memory-mcp": {
      "command": "/path/to/memory-mcp-triple-system/venv/bin/python",
      "args": ["-m", "src.mcp.stdio_server"],
      "cwd": "/path/to/memory-mcp-triple-system",
      "env": {
        "PYTHONPATH": "/path/to/memory-mcp-triple-system",
        "PYTHONIOENCODING": "utf-8"
      }
    },
    "connascence-analyzer": {
      "command": "/path/to/connascence-safety-analyzer/venv/bin/python",
      "args": ["-m", "mcp.cli", "mcp-server"],
      "cwd": "/path/to/connascence-safety-analyzer",
      "env": {
        "PYTHONPATH": "/path/to/connascence-safety-analyzer",
        "PYTHONIOENCODING": "utf-8"
      }
    }
  }
}
```

### Windows-Specific Paths

```json
{
  "mcpServers": {
    "memory-mcp": {
      "command": "C:\\Users\\USERNAME\\Projects\\memory-mcp-triple-system\\venv\\Scripts\\python.exe",
      "args": ["-X", "utf8", "-m", "src.mcp.stdio_server"],
      "cwd": "C:\\Users\\USERNAME\\Projects\\memory-mcp-triple-system",
      "env": {
        "PYTHONIOENCODING": "utf-8",
        "CHROMA_PERSIST_DIR": "C:\\Users\\USERNAME\\Projects\\memory-mcp-triple-system\\chroma_data"
      }
    },
    "connascence-analyzer": {
      "command": "C:\\Users\\USERNAME\\Projects\\connascence-safety-analyzer\\venv\\Scripts\\python.exe",
      "args": ["-m", "mcp.cli", "mcp-server"],
      "cwd": "C:\\Users\\USERNAME\\Projects\\connascence-safety-analyzer",
      "env": {
        "PYTHONIOENCODING": "utf-8"
      }
    }
  }
}
```

---

## Verification

### Test Memory-MCP

```bash
cd ~/Projects/memory-mcp-triple-system
source venv/bin/activate

# Start server (will listen on stdin/stdout)
python -m src.mcp.stdio_server

# In another terminal, test with:
echo '{"jsonrpc":"2.0","id":1,"method":"tools/list","params":{}}' | python -m src.mcp.stdio_server
```

### Test Connascence Analyzer

```bash
cd ~/Projects/connascence-safety-analyzer
source venv/bin/activate

# Test CLI
connascence . --format=json

# Test MCP
python -m mcp.cli health-check
```

### Test Context Cascade

In Claude Code:

```
> What plugins do I have installed?
> Skill("intent-analyzer")
> /sparc
```

---

## Obsidian Integration (Optional)

### Create Memory Vault

```bash
mkdir -p ~/Documents/AI-Memory-Vault/{agents,expertise,projects}

# Create structure
cd ~/Documents/AI-Memory-Vault
mkdir -p agents/{findings,fixes,decisions}
mkdir -p expertise/{domains,patterns}
mkdir -p projects
```

### Configure in Memory-MCP

Edit `memory-mcp-triple-system/config/memory-mcp.yaml`:

```yaml
storage:
  obsidian_vault: ~/Documents/AI-Memory-Vault
```

### Sync Commands

```python
from src.mcp.obsidian_client import ObsidianMCPClient

client = ObsidianMCPClient(vault_path="~/Documents/AI-Memory-Vault")
client.sync_vault()  # Index all markdown files
```

---

## Troubleshooting

### MCP Server Won't Start

1. Check Python path is correct
2. Verify virtual environment is activated
3. Check PYTHONIOENCODING is set to utf-8
4. Look at logs in respective project's logs/ directory

### Memory-MCP: ChromaDB Issues

```bash
# Reinstall chromadb
pip uninstall chromadb
pip install chromadb==1.3.0

# Clear data and restart
rm -rf chroma_data/*
```

### Connascence: Import Errors

```bash
# Reinstall with all dependencies
pip install -e ".[dev,mcp]"
```

### Context Cascade: Plugin Not Loading

1. Check `~/.claude/settings.json` syntax
2. Verify path to plugin directory
3. Restart Claude Code

---

## Uninstallation

```bash
# Remove repositories
rm -rf ~/Projects/context-cascade
rm -rf ~/Projects/memory-mcp-triple-system
rm -rf ~/Projects/connascence-safety-analyzer

# Remove Obsidian vault (if created)
rm -rf ~/Documents/AI-Memory-Vault

# Remove from Claude settings
# Edit ~/.claude/settings.json and remove the entries
```

---

## Next Steps

1. Read [SHOWCASE.md](./SHOWCASE.md) for system overview
2. Try the demo workflows
3. Explore the 196 skills and 211 agents
4. Set up your Obsidian vault for persistent memory

---

*Need help? Open an issue on GitHub.*
