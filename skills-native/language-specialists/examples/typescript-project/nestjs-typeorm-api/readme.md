# Nest.js + TypeORM API Example


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

Complete production-ready REST API with PostgreSQL, dependency injection, Swagger documentation, and E2E tests.

## Features

- ✅ Nest.js for scalable architecture
- ✅ TypeORM for type-safe database operations
- ✅ class-validator for DTO validation
- ✅ Swagger/OpenAPI documentation
- ✅ Jest for unit and E2E testing
- ✅ PostgreSQL with TypeORM migrations

## Quick Start

### 1. Install Dependencies

```bash
pnpm install
```

### 2. Setup PostgreSQL

```bash
# Using Docker
docker run --name nestjs-postgres -e POSTGRES_PASSWORD=postgres -p 5432:5432 -d postgres

# Or install PostgreSQL locally
createdb nestjs_db
```

### 3. Run the API

```bash
# Development
pnpm start:dev

# Production
pnpm build
pnpm start:prod
```

API will be available at:
- http://localhost:3000
- http://localhost:3000/api (Swagger UI)

## API Endpoints

### Create User
```bash
POST /users
Content-Type: application/json

{
  "email": "user@example.com",
  "username": "johndoe",
  "password": "securepassword123"
}
```

### Get All Users
```bash
GET /users
```

### Get User by ID
```bash
GET /users/1
```

### Delete User
```bash
DELETE /users/1
```

## Testing

```bash
# Unit tests
pnpm test

# E2E tests
pnpm test:e2e

# Test coverage
pnpm test:cov
```

## Project Structure

```
nestjs-typeorm-api/
├── src/
│   ├── users/
│   │   ├── dto/
│   │   │   └── create-user.dto.ts
│   │   ├── user.entity.ts
│   │   ├── users.controller.ts
│   │   ├── users.service.ts
│   │   └── users.module.ts
│   ├── app.module.ts
│   └── main.ts
├── test/
├── package.json
└── README.md
```

## Key Patterns

- **Dependency Injection**: Services injected via constructor
- **DTOs with Validation**: class-validator decorators
- **Type-Safe Database**: TypeORM with TypeScript
- **Swagger Decorators**: Auto-generated API docs
- **Exception Filters**: Proper error handling

## Production Considerations

1. **Environment Variables**: Use @nestjs/config
2. **Database Migrations**: Use TypeORM migrations instead of synchronize
3. **Authentication**: Add JWT auth with @nestjs/passport
4. **Rate Limiting**: Add @nestjs/throttler
5. **Logging**: Use built-in Logger service
6. **CORS**: Configure CORS for frontend

---

**Lines**: ~220 (all files combined)
**Language**: TypeScript 5.0+
**Framework**: Nest.js 10+
**Database**: PostgreSQL with TypeORM
