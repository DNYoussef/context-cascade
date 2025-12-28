---
name: language-specialists
description: Unified language specialists for Python and TypeScript development, providing expert guidance for modern backend APIs, type-safe development, async optimization, and framework integration (Django/Flask/FastAPI for Python, Express/Nest.js for TypeScript). Includes comprehensive resources, testing tools, and production-ready examples.
---

# Language Specialists - Gold Tier


## When to Use This Skill

- **Language-Specific Features**: Leveraging unique language capabilities
- **Idiomatic Code**: Writing language-specific best practices
- **Performance Optimization**: Using language-specific optimization techniques
- **Type System**: Advanced TypeScript, Rust, or type system features
- **Concurrency**: Language-specific async/parallel programming patterns
- **Ecosystem Tools**: Language-specific linters, formatters, build tools

## When NOT to Use This Skill

- **Cross-Language Work**: Polyglot projects requiring multiple languages
- **Framework-Specific**: React, Django, Rails (use framework specialist instead)
- **Algorithm Design**: Language-agnostic algorithmic work
- **Generic Patterns**: Design patterns applicable across languages

## Success Criteria

- [ ] Code follows language-specific style guide (PEP 8, Effective Go, etc.)
- [ ] Language-specific linter passing (eslint, pylint, clippy)
- [ ] Idiomatic patterns used (decorators, context managers, traits)
- [ ] Type safety enforced (TypeScript strict mode, mypy, etc.)
- [ ] Language-specific tests passing (pytest, jest, cargo test)
- [ ] Performance benchmarks met
- [ ] Documentation follows language conventions (JSDoc, docstrings, rustdoc)

## Edge Cases to Handle

- **Version Differences**: Language version compatibility (Python 2 vs 3, ES5 vs ES6)
- **Platform Differences**: OS-specific behavior (Windows vs Linux paths)
- **Encoding Issues**: Unicode, character sets, binary data
- **Dependency Hell**: Version conflicts or missing dependencies
- **Memory Management**: GC tuning, manual memory management (Rust, C++)
- **Concurrency Models**: GIL limitations, async runtime differences

## Guardrails

- **NEVER** ignore language-specific warnings or deprecations
- **ALWAYS** use language version managers (nvm, pyenv, rustup)
- **NEVER** reinvent standard library functionality
- **ALWAYS** follow language security best practices
- **NEVER** disable type checking to make code compile
- **ALWAYS** use language-native package managers
- **NEVER** commit language-specific artifacts (node_modules, __pycache__)

## Evidence-Based Validation

- [ ] Language-specific linter passes with zero warnings
- [ ] Type checker passes (tsc --strict, mypy --strict)
- [ ] Tests pass on target language version
- [ ] Benchmarks show performance within acceptable range
- [ ] Code review by language expert
- [ ] Security scanner passes (npm audit, safety, cargo audit)
- [ ] Documentation generated successfully

Expert multi-language development suite for Python and TypeScript backend systems with comprehensive tooling, testing, and examples.

## Purpose

This Gold tier skill provides unified access to Python and TypeScript specialists with production-ready resources, automated linting/validation scripts, configuration templates, comprehensive test suites, and real-world examples for multi-language repository development.

## When to Use This Skill

Activate this skill when:
- Building multi-language backend services (Python + TypeScript)
- Setting up monorepo with Python and Node.js components
- Migrating between Python and TypeScript
- Requiring language-specific best practices and tooling
- Setting up CI/CD for polyglot projects
- Implementing type-safe APIs across languages

## Nested Specialist Skills

This parent skill orchestrates two specialized sub-skills:

1. **Python Specialist** (`python-specialist/`)
   - FastAPI, Django, Flask backend development
   - Async/await optimization with asyncio
   - Type hints and mypy validation
   - Performance profiling with cProfile
   - pytest testing and coverage

2. **TypeScript Specialist** (`typescript-specialist/`)
   - Nest.js and Express API development
   - Advanced TypeScript types (generics, mapped types, conditional types)
   - npm package creation and monorepo management
   - Jest/Vitest testing
   - Build optimization with tsup/esbuild

## Structure

```
language-specialists/
├── skill.md                    # This parent skill file
├── README.md                   # Quick start guide
├── python-specialist/          # Python-specific skill
│   └── skill.md
├── typescript-specialist/      # TypeScript-specific skill
│   └── skill.md
├── resources/                  # Shared tooling and configs ⭐ NEW
│   ├── scripts/
│   │   ├── python-linter.py
│   │   ├── typescript-validator.js
│   │   ├── code-formatter.sh
│   │   └── language-analyzer.py
│   └── templates/
│       ├── python-config.yaml
│       ├── typescript-config.json
│       └── linting-rules.yaml
├── tests/                      # Validation test suites ⭐ NEW
│   ├── test-python-specialist.py
│   ├── test-typescript-specialist.ts
│   └── test-multi-language-integration.sh
└── examples/                   # Production examples ⭐ NEW
    ├── python-development/
    │   └── fastapi-postgresql-api/ (150-200 lines)
    ├── typescript-project/
    │   └── nestjs-typeorm-api/ (200-250 lines)
    └── multi-language-repo/
        └── polyglot-microservices/ (250-300 lines)
```

## Core Workflows

### Workflow 1: Initialize Multi-Language Project

**Step 1: Run Language Analyzer**

Analyze existing codebase to determine language distribution and recommend tooling:

```bash
python C:\Users\17175\claude-code-plugins\ruv-sparc-three-loop-system\skills\language-specialists\resources\scripts\language-analyzer.py --path /path/to/project
```

**Step 2: Apply Language-Specific Configs**

Copy templates to project based on analysis:

```bash
# For Python projects
cp resources/templates/python-config.yaml project/pyproject.toml

# For TypeScript projects
cp resources/templates/typescript-config.json project/tsconfig.json

# For linting
cp resources/templates/linting-rules.yaml project/.linting-rules.yaml
```

**Step 3: Setup Development Environment**

```bash
# Python environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# TypeScript environment
pnpm install
pnpm build
```

### Workflow 2: Code Quality Validation

**Step 1: Run Python Linter**

```bash
python resources/scripts/python-linter.py --dir src/ --strict
```

**Step 2: Run TypeScript Validator**

```bash
node resources/scripts/typescript-validator.js --dir src/ --strict
```

**Step 3: Format All Code**

```bash
bash resources/scripts/code-formatter.sh --all
```

### Workflow 3: Multi-Language Testing

**Step 1: Run Specialist Tests**

```bash
# Test Python specialist
pytest tests/test-python-specialist.py -v

# Test TypeScript specialist
pnpm test tests/test-typescript-specialist.ts

# Integration tests
bash tests/test-multi-language-integration.sh
```

**Step 2: Coverage Analysis**

```bash
# Python coverage
pytest --cov=src --cov-report=html

# TypeScript coverage
pnpm test --coverage
```

## Resources Overview

### Scripts (`resources/scripts/`)

1. **python-linter.py** (80-100 lines)
   - Runs black, flake8/ruff, mypy
   - Checks import ordering with isort
   - Validates docstrings
   - Reports cyclomatic complexity

2. **typescript-validator.js** (90-110 lines)
   - Runs tsc --noEmit for type checking
   - ESLint validation
   - Prettier formatting check
   - Detects unused exports

3. **code-formatter.sh** (60-80 lines)
   - Auto-formats Python with black
   - Auto-formats TypeScript with Prettier
   - Organizes imports
   - Generates formatting report

4. **language-analyzer.py** (100-120 lines)
   - Scans directory for file types
   - Calculates language distribution
   - Recommends tooling based on stack
   - Generates dependency graph

### Templates (`resources/templates/`)

1. **python-config.yaml**
   - pyproject.toml template with black, mypy, pytest configs
   - ruff configuration
   - Tool-specific settings

2. **typescript-config.json**
   - Strict tsconfig.json with modern settings
   - ESLint + Prettier integration
   - Build optimization flags

3. **linting-rules.yaml**
   - Shared linting rules for both languages
   - Code style enforcement
   - Complexity thresholds

## Testing Suite

### Test Files (`tests/`)

1. **test-python-specialist.py** (150-180 lines)
   - Unit tests for Python linter
   - FastAPI route validation
   - Async function testing
   - Type hint coverage checks

2. **test-typescript-specialist.ts** (160-190 lines)
   - TypeScript validator tests
   - Nest.js controller validation
   - Generic type constraint tests
   - Build output verification

3. **test-multi-language-integration.sh** (120-140 lines)
   - End-to-end workflow tests
   - Cross-language API contract validation
   - Performance benchmarks
   - CI/CD simulation

## Examples Overview

### 1. Python Development (`examples/python-development/`)

**fastapi-postgresql-api/** (150-200 lines total)
- Complete FastAPI + PostgreSQL CRUD API
- SQLAlchemy async models
- Pydantic validation
- pytest test suite
- Docker configuration

**Key Features**:
- JWT authentication
- Database migrations with Alembic
- API documentation with OpenAPI
- Health check endpoints

### 2. TypeScript Project (`examples/typescript-project/`)

**nestjs-typeorm-api/** (200-250 lines total)
- Nest.js + TypeORM REST API
- PostgreSQL integration
- Class-validator DTOs
- Jest testing
- Docker setup

**Key Features**:
- Dependency injection
- Swagger documentation
- Database seeding
- E2E tests

### 3. Multi-Language Repo (`examples/multi-language-repo/`)

**polyglot-microservices/** (250-300 lines total)
- FastAPI service (Python)
- Nest.js service (TypeScript)
- Shared API contracts
- Inter-service communication
- Docker Compose orchestration

**Key Features**:
- gRPC communication
- Shared TypeScript types + Python dataclasses
- Centralized logging
- Distributed tracing

## Best Practices

**1. Language Selection Guidelines**

- **Use Python for**:
  - Data processing pipelines
  - Machine learning APIs
  - Scientific computing
  - Quick prototyping

- **Use TypeScript for**:
  - Complex business logic requiring strict types
  - Frontend + Backend consistency
  - npm ecosystem integration
  - High-performance APIs

**2. Code Organization**

```
monorepo/
├── services/
│   ├── python-api/       # FastAPI service
│   └── typescript-api/   # Nest.js service
├── shared/
│   ├── types/            # Shared TypeScript types
│   └── schemas/          # Shared Pydantic models
├── tools/
│   ├── scripts/          # Language-specific tooling
│   └── configs/          # Shared configurations
└── tests/
    ├── python/
    └── typescript/
```

**3. Dependency Management**

- **Python**: Use `poetry` or `pip-tools` for deterministic builds
- **TypeScript**: Use `pnpm` with workspace protocol for monorepos
- **Shared**: Lock files committed to version control

**4. CI/CD Integration**

```yaml
# .github/workflows/multi-language.yml
jobs:
  python-quality:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/setup-python@v4
      - run: python resources/scripts/python-linter.py --strict
      - run: pytest tests/test-python-specialist.py

  typescript-quality:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/setup-node@v3
      - run: node resources/scripts/typescript-validator.js --strict
      - run: pnpm test tests/test-typescript-specialist.ts

  integration:
    needs: [python-quality, typescript-quality]
    runs-on: ubuntu-latest
    steps:
      - run: bash tests/test-multi-language-integration.sh
```

## Quality Criteria

**Code Quality**:
- ✅ Python: mypy strict mode passes, black formatted, ruff linting clean
- ✅ TypeScript: tsc --noEmit passes, ESLint clean, Prettier formatted
- ✅ Test coverage ≥85% for both languages
- ✅ All scripts executable and documented

**Resource Completeness**:
- ✅ 4 scripts in `resources/scripts/` (80-120 lines each)
- ✅ 3 templates in `resources/templates/`
- ✅ 3 test files in `tests/` (120-190 lines each)
- ✅ 3 example projects in `examples/` (150-300 lines each)

**Documentation**:
- ✅ Parent skill.md complete
- ✅ README.md quick start guide
- ✅ Inline comments in all scripts
- ✅ Example project READMEs

## Agent Coordination

**Specialized Agents**:
- `python-specialist` → Python development, async optimization, type hints
- `typescript-specialist` → TypeScript development, type safety, build optimization
- `backend-dev` → General backend architecture
- `tester` → Test suite creation and validation
- `code-analyzer` → Code quality analysis across languages

**Workflow**:
```bash
# Pre-task: Initialize environment
npx claude-flow@alpha hooks pre-task --description "Multi-language project setup"

# During: Track changes across languages
npx claude-flow@alpha hooks post-edit --file "src/api.py" --memory-key "language-specialists/python-api"
npx claude-flow@alpha hooks post-edit --file "src/api.ts" --memory-key "language-specialists/typescript-api"

# Post-task: Run comprehensive validation
bash resources/scripts/code-formatter.sh --all
python resources/scripts/python-linter.py --strict
node resources/scripts/typescript-validator.js --strict
bash tests/test-multi-language-integration.sh

npx claude-flow@alpha hooks post-task --task-id "language-specialists-validation"
```

## Common Patterns

**Pattern 1: Shared API Contracts**

```python
# Python (Pydantic)
from pydantic import BaseModel

class UserSchema(BaseModel):
    id: int
    email: str
    username: str
```

```typescript
// TypeScript (interface)
export interface User {
  id: number;
  email: string;
  username: string;
}
```

**Pattern 2: Error Handling Consistency**

```python
# Python
from fastapi import HTTPException

if not user:
    raise HTTPException(status_code=404, detail="User not found")
```

```typescript
// TypeScript
import { NotFoundException } from '@nestjs/common';

if (!user) {
  throw new NotFoundException('User not found');
}
```

## Troubleshooting

**Issue**: Import conflicts between Python and TypeScript in monorepo
**Solution**: Use separate `node_modules/` and `.venv/` directories, configure `.gitignore` properly

**Issue**: Type validation inconsistencies across languages
**Solution**: Use shared schema definitions (e.g., JSON Schema) and generate types for both languages

**Issue**: Performance differences between Python/TypeScript for same workload
**Solution**: Run language-analyzer.py to identify bottlenecks, consider moving CPU-bound tasks to Rust/Go

## Related Skills

- `python-specialist`: Deep Python expertise
- `typescript-specialist`: Deep TypeScript expertise
- `backend-dev`: Backend architecture
- `docker-containerization`: Multi-service Docker setup
- `testing-quality`: Advanced testing strategies

## Tools and Resources

**Python**:
- black: Code formatter
- ruff: Fast linter (replaces flake8, isort, etc.)
- mypy: Static type checker
- pytest: Testing framework

**TypeScript**:
- Prettier: Code formatter
- ESLint: Linter with TypeScript support
- tsc: TypeScript compiler
- Jest/Vitest: Testing frameworks

**Multi-Language**:
- Docker Compose: Service orchestration
- Turborepo/nx: Monorepo management
- OpenAPI: API contract sharing

## MCP Tools

- `mcp__flow-nexus__sandbox_create`: Create isolated testing environments
- `mcp__connascence-analyzer__analyze_workspace`: Analyze code quality across languages
- `mcp__memory-mcp__memory_store`: Store language-specific patterns and decisions

## Success Metrics

**Development Speed**:
- New Python API endpoint: 15-30 minutes
- New TypeScript API endpoint: 10-20 minutes
- Multi-language feature: 2-3 hours

**Code Quality**:
- Python type coverage (mypy): 100%
- TypeScript type coverage: 100%
- Combined test coverage: ≥85%
- Linting errors: 0

**Resource Quality**:
- Script execution time: <5 seconds each
- Template adoption rate: ≥90%
- Example project boot time: <2 minutes

## Core Principles

1. **Language Idioms Over Generic Patterns**: Always prioritize language-specific idioms and conventions over generic cross-language patterns. Python's decorators, context managers, and duck typing should be leveraged fully rather than forcing Java-style interfaces. TypeScript's structural typing and advanced type features like mapped types and conditional types should be used to create type-safe abstractions rather than runtime checks. The goal is to write code that feels native to the language ecosystem, not code that could be translated from any other language.

2. **Type Safety as a Foundation, Not an Afterthought**: Type systems are not optional features to be added later but foundational components that guide architecture. In TypeScript, strict mode should be enabled from day one with no `any` escapes. In Python, type hints should be comprehensive enough that mypy in strict mode passes cleanly. Type-driven development catches entire classes of bugs at compile time, enables confident refactoring, and serves as living documentation that stays in sync with implementation.

3. **Polyglot Projects Require Shared Contracts, Not Duplicated Logic**: When building multi-language systems, the interface boundaries must be precisely defined through shared schemas (JSON Schema, Protocol Buffers, OpenAPI). Business logic should never be duplicated across languages - instead, each language handles what it does best with clear API contracts at the boundaries. Python processes data pipelines, TypeScript handles type-safe business logic, and they communicate through well-defined interfaces with automated contract testing to prevent drift.

## Anti-Patterns

| Anti-Pattern | Why It Fails | Better Approach |
|-------------|--------------|-----------------|
| **Ignoring Language Version Managers** | Leads to "works on my machine" issues where code runs in development but fails in CI/CD due to version mismatches. Python 3.8 vs 3.11 have significant differences (typing features, asyncio improvements), and Node 16 vs 20 affect import resolution and performance. | Use pyenv/nvm consistently across all environments. Pin exact versions in .python-version and .nvmrc files. Document required versions in README with setup scripts. CI/CD should match production versions exactly. |
| **Disabling Type Checkers to Ship Faster** | Using `@ts-ignore`, `# type: ignore`, or disabling strict mode trades short-term velocity for long-term technical debt. These suppressions hide bugs that will surface in production, make refactoring dangerous, and erode confidence in the type system. | Fix the root cause of type errors by refactoring interfaces, adding proper type definitions, or using type guards. If third-party libraries lack types, contribute them to DefinitelyTyped or create local declaration files. Treat type errors as seriously as runtime errors. |
| **Mixing Language Conventions in Polyglot Codebases** | Using camelCase in Python because "it's consistent with TypeScript" or snake_case in TypeScript breaks ecosystem tooling, confuses developers, and makes code harder to maintain. Each language has conventions for good reasons - Python's PEP 8 reflects the community's decades of experience, as does TypeScript's alignment with JavaScript standards. | Follow each language's native conventions strictly. Use automated formatters (black for Python, Prettier for TypeScript) to enforce style. Create adapter layers at API boundaries to translate between naming conventions rather than forcing one language's style onto another. |

## Conclusion

The Language Specialists skill provides comprehensive multi-language development capabilities with production-ready tooling, automated validation, and real-world examples. By combining Python and TypeScript specialists with shared scripts, templates, and testing frameworks, this skill enables teams to build polyglot backend systems with confidence and consistency.

Success with this skill depends on embracing each language's unique strengths while maintaining rigorous standards across both. The provided linting scripts, validation tools, and example projects demonstrate that multi-language development doesn't require compromising on code quality, type safety, or maintainability. Whether building a pure Python FastAPI service, a TypeScript Nest.js application, or a hybrid microservices architecture with both, this skill provides the expertise, automation, and guidance needed to deliver production-quality software.

The Gold tier designation reflects not just the comprehensive resources provided, but the battle-tested patterns and tools that emerge from real-world polyglot development. Use this skill when language-specific expertise matters, when type safety is non-negotiable, and when you need proven patterns for building maintainable multi-language systems at scale.