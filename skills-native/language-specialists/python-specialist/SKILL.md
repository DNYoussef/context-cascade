---
name: python-specialist
description: Expert Python development specialist for backend APIs, async/await optimization, Django/Flask/FastAPI frameworks, type hints, packaging, and performance profiling. Use when building Python backend services, optimizing async code, implementing REST/GraphQL APIs, or requiring Python-specific best practices. Handles dependency management, virtual environments, testing with pytest, and deployment patterns.
category: Language Specialists
complexity: Medium
triggers: ["python", "django", "fastapi", "flask", "async python", "python api", "python backend", "type hints", "pytest", "python optimization"]
---

# Python Specialist

Expert Python development for modern backend systems, API development, and high-performance applications.

## Purpose

This skill provides comprehensive Python expertise across frameworks, async patterns, type safety, and production deployment. It ensures Python code follows best practices, leverages modern features (Python 3.10+), and achieves optimal performance.

## When to Use This Skill

Activate this skill when:
- Building backend APIs with Django REST Framework, FastAPI, or Flask
- Implementing async/await patterns with asyncio or trio
- Optimizing Python performance (cProfile, memory_profiler, line_profiler)
- Setting up Python projects with proper dependency management
- Writing type-safe code with type hints and mypy validation
- Creating Python packages with setuptools or poetry
- Debugging production Python issues
- Migrating from Python 2 to Python 3 or upgrading to modern Python

## Prerequisites

**Required Knowledge**:
- Python 3.10+ syntax and standard library
- Virtual environment concepts (venv, virtualenv, conda)
- Basic understanding of HTTP and REST principles

**Required Tools**:
- Python 3.10+ installed
- pip and venv available
- Code editor with Python support

**Agent Assignments**:
- `backend-dev`: Primary Python implementation
- `coder`: General coding and refactoring
- `tester`: pytest test suite creation
- `code-analyzer`: Code quality and connascence analysis
- `perf-analyzer`: Performance optimization

## Core Workflows

### Workflow 1: FastAPI REST API Development

**Step 1: Initialize Project Structure**

Create a production-ready FastAPI project with proper organization:

```bash
# Create project structure
mkdir -p my_api/{app,tests,alembic}
cd my_api

# Initialize virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install dependencies
pip install fastapi uvicorn[standard] pydantic pydantic-settings sqlalchemy alembic pytest pytest-asyncio httpx
```

**Step 2: Define Data Models with Pydantic**

Create type-safe models with validation:

```python
# app/models.py
from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    email: str = Field(..., description="User email address")
    username: str = Field(..., min_length=3, max_length=50)

class UserCreate(UserBase):
    password: str = Field(..., min_length=8)

class UserResponse(UserBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
```

**Step 3: Implement API Routes with Dependency Injection**

```python
# app/main.py
from fastapi import FastAPI, Depends, HTTPException, status
from typing import Annotated
from .models import UserCreate, UserResponse
from .dependencies import get_db, get_current_user

app = FastAPI(title="My API", version="1.0.0")

@app.post("/users", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(
    user: UserCreate,
    db: Annotated[AsyncSession, Depends(get_db)]
) -> UserResponse:
    """Create a new user with email validation."""
    # Implementation
    return user_response

@app.get("/users/me", response_model=UserResponse)
async def read_current_user(
    current_user: Annotated[User, Depends(get_current_user)]
) -> UserResponse:
    """Get current authenticated user."""
    return current_user
```

**Step 4: Add Database Integration with SQLAlchemy**

```python
# app/database.py
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

SQLALCHEMY_DATABASE_URL = "postgresql+asyncpg://user:pass@localhost/dbname"

engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

class Base(DeclarativeBase):
    pass

async def get_db():
    async with async_session_maker() as session:
        yield session
```

**Step 5: Write Comprehensive Tests**

```python
# tests/test_users.py
import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_create_user():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post("/users", json={
            "email": "test@example.com",
            "username": "testuser",
            "password": "securepass123"
        })
    assert response.status_code == 201
    assert response.json()["email"] == "test@example.com"
```

### Workflow 2: Async/Await Optimization

**Step 1: Identify Blocking Operations**

Analyze code for blocking I/O that should be async:

```python
# ❌ BLOCKING (avoid)
import requests
def fetch_data(url: str) -> dict:
    response = requests.get(url)
    return response.json()

# ✅ ASYNC (preferred)
import httpx
async def fetch_data(url: str) -> dict:
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()
```

**Step 2: Use asyncio.gather for Concurrent Operations**

```python
import asyncio
from typing import List

async def fetch_multiple(urls: List[str]) -> List[dict]:
    """Fetch multiple URLs concurrently."""
    tasks = [fetch_data(url) for url in urls]
    results = await asyncio.gather(*tasks, return_exceptions=True)
    return [r for r in results if not isinstance(r, Exception)]
```

**Step 3: Handle CPU-Bound Tasks Properly**

For CPU-intensive work, use ProcessPoolExecutor to avoid blocking the event loop:

```python
import asyncio
from concurrent.futures import ProcessPoolExecutor
from typing import Any

async def cpu_intensive_task(data: Any) -> Any:
    """Run CPU-bound task in separate process."""
    loop = asyncio.get_event_loop()
    with ProcessPoolExecutor() as executor:
        result = await loop.run_in_executor(executor, blocking_cpu_function, data)
    return result
```

### Workflow 3: Type Safety with mypy

**Step 1: Add Type Hints to Functions**

```python
from typing import List, Dict, Optional, Union, TypeVar, Generic

T = TypeVar('T')

def process_items(
    items: List[Dict[str, Any]],
    filter_key: str,
    default: Optional[T] = None
) -> List[T]:
    """Process items with type-safe filtering."""
    results: List[T] = []
    for item in items:
        value = item.get(filter_key, default)
        if value is not None:
            results.append(value)
    return results
```

**Step 2: Configure mypy Strict Mode**

```ini
# mypy.ini
[mypy]
python_version = 3.10
warn_return_any = True
warn_unused_configs = True
disallow_untyped_defs = True
disallow_any_generics = True
strict_optional = True
warn_redundant_casts = True
warn_unused_ignores = True
warn_no_return = True
check_untyped_defs = True
```

**Step 3: Run Type Checking**

```bash
mypy app/ tests/
```

### Workflow 4: Performance Profiling and Optimization

**Step 1: Profile with cProfile**

```python
import cProfile
import pstats
from pstats import SortKey

def profile_function(func, *args, **kwargs):
    """Profile function execution."""
    profiler = cProfile.Profile()
    profiler.enable()
    result = func(*args, **kwargs)
    profiler.disable()

    stats = pstats.Stats(profiler)
    stats.sort_stats(SortKey.CUMULATIVE)
    stats.print_stats(20)  # Top 20 functions
    return result
```

**Step 2: Memory Profiling**

```python
from memory_profiler import profile

@profile
def memory_intensive_function():
    """Function to profile memory usage."""
    large_list = [i for i in range(1000000)]
    return sum(large_list)
```

**Step 3: Optimize with Numba for Numerical Code**

```python
from numba import jit
import numpy as np

@jit(nopython=True)
def fast_computation(array: np.ndarray) -> float:
    """JIT-compiled numerical computation."""
    total = 0.0
    for i in range(array.size):
        total += array[i] ** 2
    return total
```

## Best Practices

**1. Use Virtual Environments Always**
- Never install packages globally
- Use `venv` for simple projects, `poetry` for complex ones
- Pin all dependencies in requirements.txt or pyproject.toml

**2. Follow PEP 8 Style Guide**
- Use `black` for automatic formatting
- Use `flake8` or `ruff` for linting
- Maximum line length: 88 characters (black default)

**3. Write Docstrings**
- Use Google or NumPy style docstrings
- Document all public functions, classes, and modules
- Include type information and examples

**4. Handle Errors Explicitly**
```python
# ✅ GOOD: Specific exception handling
try:
    result = risky_operation()
except ValueError as e:
    logger.error(f"Invalid value: {e}")
    raise HTTPException(status_code=400, detail=str(e))
except DatabaseError as e:
    logger.error(f"Database error: {e}")
    raise HTTPException(status_code=500, detail="Internal server error")

# ❌ BAD: Bare except
try:
    result = risky_operation()
except:
    pass  # Silently fails
```

**5. Use Context Managers for Resources**
```python
# ✅ GOOD: Automatic cleanup
async with httpx.AsyncClient() as client:
    response = await client.get(url)

# ❌ BAD: Manual cleanup (error-prone)
client = httpx.AsyncClient()
response = await client.get(url)
client.close()  # Might not execute if error occurs
```

## Quality Criteria

**Code Quality**:
- ✅ All functions have type hints
- ✅ mypy passes with strict mode
- ✅ black formatting applied
- ✅ flake8 or ruff linting passes
- ✅ Test coverage ≥ 90%

**Performance**:
- ✅ No blocking I/O in async functions
- ✅ Database queries use connection pooling
- ✅ Expensive operations are cached
- ✅ API response time < 200ms for simple endpoints

**Security**:
- ✅ Input validation with Pydantic
- ✅ SQL injection prevented (use parameterized queries)
- ✅ Passwords hashed with bcrypt or argon2
- ✅ Environment variables for secrets (never hardcoded)

## Agent Coordination

**backend-dev Agent**:
```bash
# Pre-task: Setup Python environment
npx claude-flow@alpha hooks pre-task --description "Python FastAPI implementation"
python -m venv .venv && source .venv/bin/activate

# During: Track file changes
npx claude-flow@alpha hooks post-edit --file "app/main.py" --memory-key "python-api/fastapi-routes"

# Post-task: Run tests
pytest tests/ --cov=app --cov-report=html
npx claude-flow@alpha hooks post-task --task-id "python-api-implementation"
```

**tester Agent**:
```bash
# Pre-task: Prepare test environment
npx claude-flow@alpha hooks pre-task --description "Python test suite creation"

# Execute: Run comprehensive tests
pytest tests/ -v --cov=app --cov-report=term-missing --cov-fail-under=90

# Post-task: Report coverage
npx claude-flow@alpha hooks post-task --task-id "python-testing"
```

## Common Patterns

**Pattern 1: Dependency Injection with FastAPI**
```python
from typing import Annotated
from fastapi import Depends

async def get_service() -> MyService:
    return MyService()

@app.get("/items")
async def get_items(
    service: Annotated[MyService, Depends(get_service)]
):
    return await service.get_all()
```

**Pattern 2: Background Tasks**
```python
from fastapi import BackgroundTasks

async def send_email(email: str):
    # Send email asynchronously
    pass

@app.post("/register")
async def register(user: UserCreate, background_tasks: BackgroundTasks):
    # Create user
    background_tasks.add_task(send_email, user.email)
    return {"status": "registered"}
```

**Pattern 3: Middleware for Logging**
```python
from fastapi import Request
import time

@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    duration = time.time() - start_time
    logger.info(f"{request.method} {request.url.path} - {duration:.2f}s")
    return response
```

## Troubleshooting

**Issue**: Import errors with relative imports
**Solution**: Ensure `__init__.py` files exist in all package directories and use absolute imports from package root

**Issue**: asyncio.run() RuntimeError "Event loop is already running"
**Solution**: Use `await` inside async functions, not `asyncio.run()` which creates a new event loop

**Issue**: SQLAlchemy "greenlet_spawn has not been called" error
**Solution**: Ensure using `asyncpg` driver for PostgreSQL and `AsyncSession` for all database operations

**Issue**: mypy errors with third-party libraries
**Solution**: Install type stubs (`pip install types-requests`) or ignore with `# type: ignore` comment

## Related Skills

- `backend-dev`: General backend development patterns
- `sql-database-specialist`: Database optimization
- `testing-quality`: Advanced testing strategies
- `docker-containerization`: Containerizing Python apps
- `opentelemetry-observability`: Adding tracing to Python services

## Tools and Resources

**Development**:
- FastAPI: https://fastapi.tiangolo.com/
- Pydantic: https://docs.pydantic.dev/
- SQLAlchemy: https://docs.sqlalchemy.org/
- pytest: https://docs.pytest.org/

**Code Quality**:
- black: Code formatter
- ruff: Fast linter (replaces flake8, isort, etc.)
- mypy: Static type checker
- bandit: Security linter

**Performance**:
- uvloop: Fast event loop implementation
- orjson: Fast JSON library
- httpx: Async HTTP client

## MCP Tools

- `mcp__flow-nexus__sandbox_create` with `template: "python"` for isolated testing
- `mcp__flow-nexus__sandbox_execute` for running Python code
- `mcp__connascence-analyzer__analyze_file` for detecting code quality issues
- `mcp__memory-mcp__memory_store` for persisting API patterns and decisions

## Success Metrics

**Development Speed**:
- New API endpoint: 15-30 minutes
- Database model + CRUD: 30-45 minutes
- Full feature with tests: 2-3 hours

**Code Quality**:
- Test coverage: ≥90%
- Type coverage (mypy): 100%
- Linting: 0 errors

**Performance**:
- API latency p95: <200ms
- Throughput: 1000+ req/s (simple endpoints)
- Memory usage: <100MB for simple APIs

---

**Skill Version**: 1.0.0
**Last Updated**: 2025-11-02
**Maintained By**: python-specialist agent

## Core Principles

### 1. Async/Await for I/O - Never Block the Event Loop
Modern Python backends must handle concurrent requests efficiently. Async/await enables thousands of concurrent connections without thread overhead.

**In practice**:
- Use async def for all I/O operations (database queries, HTTP requests, file operations)
- Use httpx instead of requests for async HTTP clients
- Employ asyncio.gather for concurrent operations
- Example: FastAPI endpoint fetching data from 3 services concurrently reduces latency from 600ms (sequential) to 200ms (parallel)

### 2. Type Hints Everywhere - Catch Errors at Compile Time
Type hints combined with mypy provide static type checking that prevents runtime errors and improves code maintainability.

**In practice**:
- Add type hints to all function signatures (arguments and return types)
- Enable mypy strict mode in CI/CD pipelines
- Use Pydantic models for data validation at runtime
- Example: Type hint prevents passing string to function expecting int, caught by mypy before deployment

### 3. Virtual Environments Always - Isolate Dependencies
Global Python package installations create conflicts between projects and make deployment unpredictable.

**In practice**:
- Create venv for every project (python -m venv .venv)
- Pin exact versions in requirements.txt or pyproject.toml
- Use Poetry or PDM for advanced dependency management
- Example: Two projects using different Django versions coexist without conflicts through isolated virtual environments

## Anti-Patterns

| Anti-Pattern | Problem | Solution |
|-------------|---------|----------|
| **Blocking I/O in Async Functions** | Using requests.get() in async functions blocks event loop, preventing concurrency and reducing throughput | Use async libraries (httpx, asyncpg, motor) and await all I/O operations |
| **Bare Exception Handling** | Catching all exceptions with bare except silently swallows errors, making debugging impossible | Catch specific exceptions (ValueError, DatabaseError), log errors, and let unexpected exceptions propagate |
| **No Type Hints** | Missing type hints prevent static analysis, break IDE autocomplete, and hide bugs until runtime | Add type hints to all function signatures, enable mypy strict mode |
| **Global Package Installation** | Installing packages globally with pip causes version conflicts and non-reproducible deployments | Always use virtual environments (venv, virtualenv, conda) and pin dependencies |
| **Manual Resource Cleanup** | Forgetting to close files, database connections, or HTTP clients leaks resources and causes crashes | Use context managers (async with, with statements) for automatic resource cleanup |

## Conclusion

Modern Python development for backend systems centers on FastAPI for API development, async/await for concurrency, and type hints for safety. FastAPI's automatic OpenAPI documentation, Pydantic integration for validation, and dependency injection system create a powerful foundation for production APIs. Combined with async/await patterns using asyncio, Python achieves performance comparable to Node.js while maintaining Python's readability and ecosystem.

Type safety through type hints and mypy transforms Python from a dynamically typed language into a statically verified one at development time. This catches entire categories of bugs before code runs, while preserving Python's flexibility for rapid development. Pydantic bridges the gap between static types and runtime validation, ensuring data from external sources (API requests, database queries) matches expected schemas.

Performance optimization in Python requires understanding when to use async for I/O-bound work and when to use ProcessPoolExecutor for CPU-bound tasks. Profiling with cProfile and memory_profiler identifies bottlenecks, while tools like Numba provide JIT compilation for numerical code. For production deployments, uvicorn with uvloop provides the fastest ASGI server, while connection pooling for databases and caching for expensive operations ensure scalability. This comprehensive approach produces Python applications that are type-safe, performant, and maintainable at scale.
