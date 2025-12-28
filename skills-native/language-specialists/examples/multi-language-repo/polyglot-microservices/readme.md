# Polyglot Microservices Example


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

Multi-language microservices architecture with FastAPI (Python) and Nest.js (TypeScript) services communicating via gRPC, with shared type definitions and Docker Compose orchestration.

## Architecture

```
┌─────────────────┐         gRPC         ┌─────────────────┐
│  FastAPI        │◄────────────────────►│  Nest.js        │
│  Service        │                       │  Service        │
│  (Python)       │                       │  (TypeScript)   │
└────────┬────────┘                       └────────┬────────┘
         │                                         │
         └──────────────┬──────────────────────────┘
                        │
                   PostgreSQL
```

## Features

- ✅ FastAPI service (Python) for data processing
- ✅ Nest.js service (TypeScript) for business logic
- ✅ gRPC for inter-service communication
- ✅ Shared Protocol Buffer definitions
- ✅ Docker Compose orchestration
- ✅ Centralized logging with Loki/Grafana
- ✅ Distributed tracing with Jaeger

## Project Structure

```
polyglot-microservices/
├── services/
│   ├── python-service/
│   │   ├── main.py              # FastAPI service
│   │   ├── grpc_client.py       # gRPC client
│   │   └── requirements.txt
│   └── typescript-service/
│       ├── src/
│       │   ├── main.ts          # Nest.js service
│       │   └── grpc.service.ts  # gRPC server
│       └── package.json
├── shared/
│   └── proto/
│       └── user.proto           # Shared Protocol Buffer
├── docker-compose.yml           # Service orchestration
└── README.md
```

## Quick Start

### 1. Start All Services

```bash
docker-compose up -d
```

Services will be available at:
- Python service: http://localhost:8000
- TypeScript service: http://localhost:3000
- PostgreSQL: localhost:5432
- Jaeger UI: http://localhost:16686

### 2. Test Inter-Service Communication

```bash
# Call TypeScript service (which calls Python service via gRPC)
curl http://localhost:3000/api/users/process/1
```

## Services

### Python Service (FastAPI)

**Port**: 8000

Endpoints:
- `GET /health` - Health check
- `POST /process` - Process data
- gRPC server on port 50051

### TypeScript Service (Nest.js)

**Port**: 3000

Endpoints:
- `GET /health` - Health check
- `GET /api/users/:id` - Get user
- `GET /api/users/process/:id` - Process user (calls Python service via gRPC)

## Development

### Python Service

```bash
cd services/python-service
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

### TypeScript Service

```bash
cd services/typescript-service
pnpm install
pnpm start:dev
```

## Shared Types

Protocol Buffer definition (`shared/proto/user.proto`):

```protobuf
syntax = "proto3";

package user;

message User {
  int32 id = 1;
  string email = 2;
  string username = 3;
}

message ProcessRequest {
  int32 user_id = 1;
}

message ProcessResponse {
  User user = 1;
  string processed_data = 2;
}

service UserService {
  rpc ProcessUser(ProcessRequest) returns (ProcessResponse);
}
```

## Monitoring

### Distributed Tracing (Jaeger)

View traces at: http://localhost:16686

### Logging

Centralized logging with Grafana Loki

### Metrics

Prometheus metrics exposed on:
- Python service: http://localhost:8000/metrics
- TypeScript service: http://localhost:3000/metrics

## Production Deployment

### 1. Build Images

```bash
docker-compose build
```

### 2. Push to Registry

```bash
docker tag polyglot-python:latest registry.example.com/polyglot-python:latest
docker tag polyglot-typescript:latest registry.example.com/polyglot-typescript:latest

docker push registry.example.com/polyglot-python:latest
docker push registry.example.com/polyglot-typescript:latest
```

### 3. Deploy to Kubernetes

```bash
kubectl apply -f k8s/
```

## Key Patterns

- **gRPC Communication**: Type-safe inter-service calls
- **Shared Proto Definitions**: Single source of truth
- **Service Discovery**: Docker DNS within compose network
- **Health Checks**: Standardized health endpoints
- **Graceful Shutdown**: Proper signal handling

## Testing

```bash
# Python tests
cd services/python-service
pytest

# TypeScript tests
cd services/typescript-service
pnpm test

# Integration tests
bash test-integration.sh
```

---

**Lines**: ~280 (all services combined)
**Languages**: Python + TypeScript
**Frameworks**: FastAPI + Nest.js
**Communication**: gRPC
**Orchestration**: Docker Compose
