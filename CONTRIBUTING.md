# Contributing to Context Cascade

Thank you for your interest in contributing to Context Cascade! This document provides guidelines and instructions for contributing.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Project Structure](#project-structure)
- [Making Changes](#making-changes)
- [Pull Request Process](#pull-request-process)
- [Style Guidelines](#style-guidelines)

## Code of Conduct

By participating in this project, you agree to maintain a respectful and inclusive environment. Be kind, constructive, and professional in all interactions.

## Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/YOUR-USERNAME/context-cascade.git
   cd context-cascade
   ```
3. **Add upstream remote**:
   ```bash
   git remote add upstream https://github.com/DNYoussef/context-cascade.git
   ```

## Development Setup

### Prerequisites

- Node.js >= 18.0.0
- npm >= 9.0.0
- Git
- Claude Code CLI (for testing plugins)

### Installation

```bash
# Install dependencies
npm install

# Install claude-flow (required MCP server)
npm install -g claude-flow@alpha

# Verify installation
npm run verify
```

### Testing Your Changes

```bash
# List available agents
npm run list-agents

# List available skills
npm run list-skills

# Test in Claude Code
claude mcp add claude-flow npx claude-flow@alpha mcp start
```

## Project Structure

```
context-cascade/
|-- agents/           # 203 agent definitions (by category)
|-- skills/           # 122 skill definitions (by category)
|-- commands/         # 130+ command definitions
|-- plugins/          # 5 installable plugin packages
|-- hooks/            # Lifecycle hooks (12fa compliant)
|-- docs/             # Documentation
|-- .claude-plugin/   # Plugin manifest and marketplace config
|-- index.js          # Package entry point
```

### Key Directories

- **agents/**: Agent definitions organized by category (delivery, foundry, operations, etc.)
- **skills/**: Skill definitions with SKILL.md files
- **commands/**: Slash command definitions
- **plugins/**: Modular plugin packages (12fa-core, 12fa-three-loop, etc.)

## Making Changes

### Branch Naming

- `feature/description` - New features
- `fix/description` - Bug fixes
- `docs/description` - Documentation updates
- `refactor/description` - Code refactoring

### Commit Messages

Use clear, descriptive commit messages:

```
type: short description

Longer description if needed.
```

Types: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`

### Adding a New Agent

1. Create the agent file in the appropriate category:
   ```
   agents/[category]/[subcategory]/agent-name.md
   ```
2. Follow the agent template format (see existing agents)
3. Update `agents/README.md` with the new agent
4. Test the agent with Claude Code

### Adding a New Skill

1. Create a directory under the appropriate category:
   ```
   skills/[category]/skill-name/SKILL.md
   ```
2. Follow the skill template format
3. Update `skills/README.md`
4. Test the skill invocation

## Pull Request Process

1. **Update your fork**:
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

2. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature
   ```

3. **Make your changes** and commit

4. **Push to your fork**:
   ```bash
   git push origin feature/your-feature
   ```

5. **Open a Pull Request** on GitHub

### PR Requirements

- [ ] Clear description of changes
- [ ] Tests pass (if applicable)
- [ ] Documentation updated (if applicable)
- [ ] No breaking changes (or clearly documented)
- [ ] Follows style guidelines

## Style Guidelines

### Markdown Files

- Use ATX-style headers (`#`, `##`, `###`)
- Include a table of contents for long documents
- Use fenced code blocks with language identifiers
- Keep lines under 100 characters when possible

### Agent/Skill Definitions

- Include clear descriptions
- Document all parameters
- Provide usage examples
- List dependencies and requirements

### Code (JavaScript/Python)

- Use consistent indentation (2 spaces for JS, 4 for Python)
- Add JSDoc/docstrings for functions
- Keep functions focused and small
- Handle errors gracefully

## Questions?

- Open an issue for bugs or feature requests
- Start a discussion for questions or ideas
- Check existing issues before creating new ones

---

Thank you for contributing to Context Cascade!
