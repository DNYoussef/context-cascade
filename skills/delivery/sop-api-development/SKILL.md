---
name: sop-api-development
description: Complete REST API development workflow coordinating backend, database,
  testing, documentation, and DevOps agents. 2-week timeline with TDD approach.
version: 1.0.0
category: delivery
tags:
- delivery
- development
- workflow
author: ruv
---

# SOP: REST API Development


## When to Use This Skill

- **Domain-Specific Work**: Tasks requiring specialized domain knowledge
- **Complex Problems**: Multi-faceted challenges needing systematic approach
- **Best Practice Implementation**: Following industry-standard methodologies
- **Quality-Critical Work**: Production code requiring high standards
- **Team Collaboration**: Coordinated work following shared processes

## When NOT to Use This Skill

- **Outside Domain**: Tasks outside this skill specialty area
- **Incompatible Tech Stack**: Technologies not covered by this skill
- **Simple Tasks**: Trivial work not requiring specialized knowledge
- **Exploratory Work**: Experimental code without production requirements

## Success Criteria

- [ ] Implementation complete and functional
- [ ] Tests passing with adequate coverage
- [ ] Code reviewed and approved
- [ ] Documentation updated
- [ ] Performance benchmarks met
- [ ] Security considerations addressed
- [ ] Deployed or integrated successfully

## Edge Cases to Handle

- **Legacy Integration**: Working with older codebases or deprecated APIs
- **Missing Dependencies**: Unavailable libraries or external services
- **Version Conflicts**: Dependency version incompatibilities
- **Data Issues**: Malformed input or edge case data
- **Concurrency**: Race conditions or synchronization challenges
- **Error Handling**: Graceful degradation and recovery

## Guardrails

- **NEVER** skip testing to ship faster
- **ALWAYS** follow domain-specific best practices
- **NEVER** commit untested or broken code
- **ALWAYS** document complex logic and decisions
- **NEVER** hardcode sensitive data or credentials
- **ALWAYS** validate input and handle errors gracefully
- **NEVER** deploy without reviewing changes

## Evidence-Based Validation

- [ ] Automated tests passing
- [ ] Code linter/formatter passing
- [ ] Security scan completed
- [ ] Performance within acceptable range
- [ ] Manual testing completed
- [ ] Peer review approved
- [ ] Documentation reviewed

Complete REST API development using Test-Driven Development and multi-agent coordination.

## Timeline: 2 Weeks

**Phases**:
1. Planning & Design (Days 1-2)
2. Development (Days 3-8)
3. Testing & Documentation (Days 9-11)
4. Deployment (Days 12-14)

---

## Phase 1: Planning & Design (Days 1-2)

### Day 1: Requirements & Architecture

**Sequential Workflow**:

```javascript
// Step 1: Gather Requirements
await Task("Product Manager", `
Define API requirements:
- List all endpoints needed
- Define data models and relationships
- Specify authentication/authorization
- Define rate limiting and quotas
- Identify third-party integrations

Store requirements: api-dev/rest-api-v2/requirements
`, "planner");

// Step 2: API Design
await Task("System Architect", `
Using requirements: api-dev/rest-api-v2/requirements

Design:
- RESTful API structure (resources, HTTP methods)
- URL patterns and versioning strategy
- Request/response formats (JSON schemas)
- Error handling patterns
- API security architecture

Generate OpenAPI 3.0 specification
Store: api-dev/rest-api-v2/openapi-spec
`, "system-architect");

// Step 3: Database Design
await Task("Database Architect", `
Using API spec: api-dev/rest-api-v2/openapi-spec

Design database:
- Schema design (tables, columns, types)
- Relationships and foreign keys
- Indexes for performance
- Migration strategy
- Backup and recovery plan

Generate SQL schema
Store: api-dev/rest-api-v2/db-schema
`, "code-analyzer");
```

### Day 2: Test Planning

```javascript
// Step 4: Test Strategy
await Task("QA Engineer", `
Using:
- API spec: api-dev/rest-api-v2/openapi-spec
- DB schema: api-dev/rest-api-v2/db-schema

Create test plan:
- Unit test strategy (per endpoint)
- Integration test scenarios
- E2E test workflows
- Performance test targets
- Security test cases

Store test plan: api-dev/rest-api-v2/test-plan
`, "tester");

// Step 5: DevOps Planning
await Task("DevOps Engineer", `
Plan infrastructure:
- Environment setup (dev, staging, prod)
- CI/CD pipeline design
- Monitoring and logging strategy
- Deployment strategy (blue-green)
- Rollback procedures

Store DevOps plan: api-dev/rest-api-v2/devops-plan
`, "cicd-engineer");
```

**Deliverables**:
- API requirements document
- OpenAPI 3.0 specification
- Database schema
- Test plan
- DevOps plan

---

## Phase 2: Development (Days 3-8)

### Day 3-4: Setup & Foundation

**Parallel Workflow**:

```javascript
// Initialize development environment
await mcp__ruv-swarm__swarm_init({
  topology: 'hierarchical',
  maxAgents: 5,
  strategy: 'specialized'
});

// Parallel setup
const [projectSetup, dbSetup, ciSetup] = await Promise.all([
  Task("Backend Developer", `
Project setup:
- Initialize Node.js/Express project
- Configure TypeScript
- Set up ESLint + Prettier
- Configure environment variables
- Install dependencies (express, prisma, jest, etc.)

Store project structure: api-dev/rest-api-v2/project-setup
`, "backend-dev"),

  Task("Database Specialist", `
Database setup:
- Create PostgreSQL database
- Run initial migrations
- Seed test data
- Configure connection pooling
- Set up backup scripts

Store DB credentials (encrypted): api-dev/rest-api-v2/db-config
`, "code-analyzer"),

  Task("DevOps Engineer", `
CI/CD setup:
- Configure GitHub Actions workflow
- Set up Docker containers
- Configure environment secrets
- Set up code quality checks
- Configure automated testing

Store CI config: api-dev/rest-api-v2/ci-config
`, "cicd-engineer")
]);
```

### Day 5-6: Core Development (TDD)

**Sequential per Endpoint** (Example: User Authentication):

```javascript
// For each endpoint, follow TDD cycle:

// 1. Write Tests First
await Task("Test Engineer", `
Write tests for: POST /api/auth/register

Unit tests:
- Valid registration with email/password
- Duplicate email rejection
- Password strength validation
- Email format validation

Integration tests:
- Database record creation
- Email verification trigger
- Response format validation

Store tests: api-dev/rest-api-v2/tests/auth/register.test.ts
`, "tester");

// 2. Implement to Pass Tests
await Task("Backend Developer", `
Implement: POST /api/auth/register

Following tests at: api-dev/rest-api-v2/tests/auth/register.test.ts

Implementation:
- Request validation (email, password)
- Password hashing (bcrypt)
- User creation in database
- Send verification email
- Return JWT token

All tests must pass
Store implementation: api-dev/rest-api-v2/src/auth/register.ts
`, "backend-dev");

// 3. Refactor & Optimize
await Task("Code Reviewer", `
Review implementation: api-dev/rest-api-v2/src/auth/register.ts

Check:
- Code quality and style
- Security best practices
- Performance optimization
- Error handling completeness

Suggest improvements
Store review: api-dev/rest-api-v2/reviews/auth/register-review.md
`, "reviewer");

// Repeat for all endpoints (login, refresh, logout, etc.)
```

### Day 7-8: Advanced Features

**Parallel Development**:

```javascript
const [auth, crud, search, webhook] = await Promise.all([
  Task("Auth Specialist", `
Implement authentication middleware:
- JWT verification
- Token refresh logic
- Role-based access control (RBAC)
- API key authentication

Store: api-dev/rest-api-v2/src/middleware/auth.ts
`, "backend-dev"),

  Task("CRUD Developer", `
Implement CRUD operations for all resources:
- GET /api/resources (list with pagination, filtering, sorting)
- GET /api/resources/:id (single resource)
- POST /api/resources (create)
- PUT /api/resources/:id (update)
- DELETE /api/resources/:id (delete)

Store: api-dev/rest-api-v2/src/resources/
`, "backend-dev"),

  Task("Search Developer", `
Implement search functionality:
- Full-text search across resources
- Advanced filtering (operators: eq, gt, lt, contains)
- Faceted search with aggregations
- Search result ranking

Store: api-dev/rest-api-v2/src/search/
`, "backend-dev"),

  Task("Webhook Developer", `
Implement webhook system:
- Webhook registration endpoints
- Event triggering system
- Retry logic with exponential backoff
- Webhook signature verification

Store: api-dev/rest-api-v2/src/webhooks/
`, "backend-dev")
]);
```

**Deliverables**:
- Working API with all endpoints implemented
- All tests passing (unit + integration)
- Code reviewed and optimized

---

## Phase 3: Testing & Documentation (Days 9-11)

### Day 9: Comprehensive Testing

**Parallel Testing**:

```javascript
const [e2eTests, perfTests, securityTests] = await Promise.all([
  Task("E2E Test Engineer", `
End-to-end testing:
- Complete user workflows (register → login → CRUD → logout)
- Error scenarios (invalid input, unauthorized access)
- Edge cases (rate limiting, concurrent requests)

Run E2E test suite
Store results: api-dev/rest-api-v2/test-results/e2e
`, "tester"),

  Task("Performance Tester", `
Performance testing:
- Load testing (1000 req/sec target)
- Stress testing (find breaking point)
- Endurance testing (24-hour sustained load)
- API response time < 200ms (p95)

Run benchmarks
Store metrics: api-dev/rest-api-v2/test-results/performance
`, "perf-analyzer"),

  Task("Security Tester", `
Security testing:
- OWASP API Security Top 10 checks
- SQL injection testing
- XSS vulnerability testing
- Authentication/authorization bypass attempts
- Rate limiting validation

Run security scan
Store audit: api-dev/rest-api-v2/test-results/security
`, "security-manager")
]);
```

### Day 10-11: Documentation

**Parallel Documentation**:

```javascript
const [apiDocs, devDocs, runbook] = await Promise.all([
  Task("API Documentation Writer", `
Create API documentation:
- OpenAPI/Swagger interactive docs
- Authentication guide
- Endpoint reference (all endpoints)
- Code examples (cURL, JavaScript, Python)
- Rate limiting and quotas
- Error codes and handling

Host Swagger UI
Store: api-dev/rest-api-v2/docs/api-reference
`, "api-docs"),

  Task("Developer Documentation", `
Create developer guide:
- Getting started (setup, authentication)
- Tutorial (common workflows)
- Best practices
- SDKs and libraries
- Changelog and versioning

Store: api-dev/rest-api-v2/docs/developer-guide
`, "api-docs"),

  Task("Operations Runbook", `
Create operational docs:
- Deployment procedures
- Monitoring and alerting setup
- Troubleshooting guide
- Performance tuning
- Backup and recovery procedures
- Incident response plan

Store: api-dev/rest-api-v2/docs/operations
`, "cicd-engineer")
]);
```

**Deliverables**:
- All tests passing (unit, integration, E2E, performance, security)
- Complete API documentation
- Developer guide
- Operations runbook

---

## Phase 4: Deployment (Days 12-14)

### Day 12: Pre-Production Validation

**Sequential Workflow**:

```javascript
// Step 1: Final Validation
await Task("Production Validator", `
Pre-production checklist:
- All tests passing (100% of test suite)
- Code coverage > 90%
- Security audit passed
- Performance benchmarks met
- Documentation complete
- Monitoring configured
- Alerts configured
- Rollback plan ready

Generate go/no-go report
Store: api-dev/rest-api-v2/validation/final-check
`, "production-validator");

// Step 2: Staging Deployment
await Task("DevOps Engineer", `
Deploy to staging:
- Deploy API to staging environment
- Run smoke tests
- Validate monitoring and logging
- Test rollback procedure

Store staging deployment report: api-dev/rest-api-v2/deployment/staging
`, "cicd-engineer");

// Step 3: Staging Validation
await Task("QA Engineer", `
Validate staging environment:
- Run full test suite against staging
- Verify data persistence
- Check error handling
- Validate monitoring dashboards

Approve for production or identify issues
Store validation: api-dev/rest-api-v2/validation/staging
`, "tester");
```

### Day 13: Production Deployment

```javascript
// Step 4: Production Deployment (Blue-Green)
await Task("DevOps Engineer", `
Production deployment (blue-green):
- Deploy to green environment (alongside blue)
- Run smoke tests on green
- Switch traffic to green (gradual canary: 10% → 50% → 100%)
- Monitor error rates and performance
- Keep blue environment ready for rollback

Store production deployment: api-dev/rest-api-v2/deployment/production
`, "cicd-engineer");

// Step 5: Post-Deployment Validation
await Task("Production Monitor", `
Monitor production:
- Track API response times
- Monitor error rates
- Check resource utilization
- Validate data integrity
- Monitor user activity

Generate hourly reports for first 24 hours
Store: api-dev/rest-api-v2/monitoring/production
`, "performance-monitor");
```

### Day 14: Post-Launch

```javascript
// Step 6: Documentation Update
await Task("Documentation Specialist", `
Update all documentation:
- Add production API URLs
- Update authentication endpoints
- Add production monitoring dashboards
- Update support contact info

Publish final docs
Store: api-dev/rest-api-v2/docs/published
`, "api-docs");

// Step 7: Knowledge Transfer
await Task("Technical Writer", `
Create knowledge transfer materials:
- Developer onboarding guide
- Support team training
- Common issues and solutions
- Escalation procedures

Store: api-dev/rest-api-v2/knowledge-transfer
`, "api-docs");
```

**Deliverables**:
- Production API (live and stable)
- Complete documentation (published)
- Monitoring dashboards (active)
- Support team trained

---

## Success Metrics

### Technical Metrics
- **Test Coverage**: > 90%
- **API Response Time**: < 200ms (p95)
- **Uptime**: 99.9%+
- **Error Rate**: < 0.1%
- **Code Quality Score**: A rating

### Performance Metrics
- **Throughput**: > 1000 req/sec
- **Database Query Time**: < 50ms (p95)
- **Memory Usage**: < 512MB
- **CPU Usage**: < 70%

### Quality Metrics
- **Security Audit**: Passed
- **Documentation Coverage**: 100%
- **API Compliance**: OpenAPI 3.0 valid
- **Code Review Approval**: 100%

---

## Agent Coordination Summary

**Total Agents Used**: 8
**Execution Pattern**: Sequential + Parallel (TDD approach)
**Timeline**: 2 weeks (14 days)
**Memory Namespaces**: api-dev/rest-api-v2/*

**Key Agents**:
1. planner - Requirements gathering
2. system-architect - API design
3. code-analyzer - Database architecture
4. tester - Test planning and execution
5. cicd-engineer - DevOps and deployment
6. backend-dev - API implementation
7. reviewer - Code review
8. perf-analyzer - Performance testing
9. security-manager - Security testing
10. production-validator - Final validation
11. performance-monitor - Production monitoring
12. api-docs - Documentation

---

## Usage

```javascript
// Invoke this SOP skill
Skill("sop-api-development")

// Or execute with specific parameters
Task("API Development Orchestrator", `
Execute REST API development SOP for: User Management API
Requirements: {requirements}
Timeline: 2 weeks
`, "planner")
```

---

**Status**: Production-ready SOP
**Complexity**: Medium (8-12 agents, 2 weeks)
**Pattern**: Test-Driven Development with parallel optimization

---

## Core Principles

### 1. Test-Driven Development (TDD) as Non-Negotiable
Write tests BEFORE implementation, not after. TDD is not a productivity drag - it prevents rework:
- **Red-Green-Refactor Cycle**: Write failing test (red), implement minimal code to pass (green), refactor for clarity (refactor)
- **Regression Safety**: Tests prevent breaking existing functionality during refactoring or feature additions
- **Design Validation**: Tests force API design decisions before implementation locks them in
- **Documentation Through Tests**: Tests document expected behavior more accurately than comments

APIs developed without TDD accumulate technical debt through untested edge cases, brittle code, and breaking changes. The cost of writing tests after implementation is 3-5x higher than writing tests first due to refactoring required for testability.

### 2. API Contract-First Design
Define OpenAPI specification BEFORE writing code. API contracts are the interface between frontend and backend:
- **Frontend-Backend Parallelization**: Teams can work in parallel using mock servers from OpenAPI spec
- **Breaking Change Detection**: Schema validation detects breaking changes before deployment
- **Documentation Generation**: Interactive API docs (Swagger UI) generated automatically from spec
- **Client SDK Generation**: Client libraries generated automatically for multiple languages

Code-first API development leads to undocumented endpoints, inconsistent naming, and breaking changes discovered in production. Contract-first development treats the API as a product with versioned specifications and automated validation.

### 3. Progressive Deployment Through Canary Releases
Deploy new API versions incrementally to detect issues before full rollout:
- **Traffic Splitting**: Route 1-5% traffic to new version, monitor error rates and latency before full rollout
- **Rollback Capability**: Instant rollback to previous version if error rates exceed thresholds
- **Feature Flags**: Decouple deployment from feature activation, enable features per user cohort or API key
- **Blue-Green Strategy**: Run new version alongside old version, switch traffic atomically

Direct deployment to 100% of traffic converts minor bugs into major incidents. Canary releases limit blast radius - a bug affecting 5% of users is recoverable, the same bug affecting all users requires crisis management and customer notifications.

---

## Anti-Patterns

| Anti-Pattern | Why It Fails | Correct Approach |
|-------------|--------------|------------------|
| **Implementation Before Tests** | Writing code first, then adding tests as afterthought. Results in untested edge cases, brittle code that resists refactoring, and false confidence from passing tests that merely document existing behavior rather than validate requirements. | **Red-Green-Refactor TDD Cycle**: Write failing test first (red), implement minimal code to pass test (green), refactor for clarity (refactor). Tests drive API design and catch regressions. Aim for 90%+ test coverage measured by branches covered, not just lines executed. |
| **Implicit API Contracts Through Code** | Defining API through code without formal specification (OpenAPI/Swagger). Leads to undocumented endpoints, inconsistent naming conventions, and breaking changes discovered in production when clients fail. | **OpenAPI-First API Design**: Write OpenAPI 3.0 specification BEFORE implementing endpoints. Use specification to generate mock servers for frontend development, validate requests/responses in middleware, and auto-generate interactive documentation (Swagger UI). Version specifications alongside code. |
| **Direct Production Deployment** | Deploying new API version directly to 100% of production traffic without gradual rollout. Minor bugs become major incidents affecting all users. Rollback requires full redeployment under pressure. | **Canary Release with Progressive Rollout**: Deploy to 1-5% of traffic (canary), monitor error rates and latency for 1 hour. If metrics within thresholds, roll out to 25%, then 50%, then 100% with automated rollback on threshold violations. Use feature flags to decouple deployment from activation. |

---

## Common Anti-Patterns

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| **Code-First API Development** | Writing implementation before defining API specification. Results in inconsistent endpoints, undocumented breaking changes, and frontend-backend coordination failures. Changing API after implementation is 10x more expensive. | **Contract-First with OpenAPI**: Define OpenAPI 3.0 specification BEFORE implementation. Use spec to generate mock servers for parallel frontend dev, validate requests/responses in middleware, and auto-generate documentation. Implementation becomes spec fulfillment, not exploration. |
| **Testing After Implementation** | Writing tests after code is complete. Creates biased tests that document existing behavior rather than validate requirements. Misses edge cases discovered during implementation. Encourages untestable code architecture. | **Test-Driven Development**: Write failing test first (red), implement minimal code to pass (green), refactor (refactor). Tests drive API design decisions and catch regressions. Aim 90%+ branch coverage, not just line coverage. |
| **Direct Production Deployment** | Deploying API changes directly to 100% production traffic. Minor bugs become major incidents affecting all users. Rollback requires full redeployment under pressure. No validation against real traffic patterns. | **Canary Deployment with Progressive Rollout**: Deploy to 1-5% traffic canary first. Monitor error rates and latency for 1 hour. If metrics within thresholds, roll out to 25%, 50%, 100% with automated rollback on violations. Use feature flags to decouple deployment from activation. |

---

## Conclusion

REST API development requires systematic adherence to three core principles: Test-Driven Development for quality assurance, Contract-First Design for interface clarity, and Progressive Deployment for risk mitigation. This SOP coordinates 8-12 agents across a 2-week timeline to deliver production-ready APIs with comprehensive testing, documentation, and monitoring.

The TDD principle of writing tests before implementation is non-negotiable for production APIs. Tests written after code merely document existing behavior rather than validate requirements. The Red-Green-Refactor cycle forces API design decisions before implementation locks them in, provides regression safety during refactoring, and creates executable documentation that accurately reflects behavior. APIs developed without TDD accumulate technical debt through untested edge cases and brittle code that resists modification. The upfront investment in TDD pays dividends through faster feature development, fewer production bugs, and confident refactoring.

Contract-First API Design treats the API specification as a versioned product, not an afterthought. Defining OpenAPI specifications before writing code enables frontend-backend parallelization (mock servers from spec), breaking change detection (schema validation), automated documentation generation (Swagger UI), and client SDK generation. Implicit API contracts through code lead to undocumented endpoints, inconsistent naming, and breaking changes discovered in production. The OpenAPI specification becomes the source of truth that drives code generation, validation middleware, and interactive documentation.

Progressive Deployment through Canary Releases limits blast radius by incrementally rolling out new API versions to small traffic percentages before full production deployment. Direct deployment to 100% of traffic converts minor bugs into major incidents. Canary releases (1-5% traffic) with automated monitoring detect issues affecting a small user cohort before they impact the entire user base. Blue-green deployment provides instant rollback capability, while feature flags decouple deployment from feature activation. The incremental cost of progressive deployment is trivial compared to the cost of a production incident affecting all users.

This SOP provides a systematic 4-phase workflow (Planning & Design, Development, Testing & Documentation, Deployment) with clear agent assignments, memory namespace conventions, and success metrics. Use this as a template for API development projects, adapting timeline and agent allocation to project complexity. REST API mastery is not about memorizing HTTP status codes - it is about applying consistent principles that guarantee quality, maintainability, and reliability through systematic testing, contract-driven design, and progressive deployment.

---

## System Design Integration (Dr. Synthara Methodology)

### API Style Decision Tree

```
Who consumes it and what do they need?
|
+-- Public API, broad compatibility, caching & simplicity matter?
|   +-- REST (this skill's focus)
|
+-- Complex UI needing shaped responses, reducing round trips?
|   +-- GraphQL (control query cost + N+1)
|
+-- Internal service-to-service, performance + typed contracts?
    +-- gRPC (protobuf, streaming, strong typing)
```

**What I'm Thinking**: GraphQL trades "fewer requests" for "harder caching + expensive resolvers." Plan for that up front.

### Protocol Decision Tree

```
What interaction pattern do you need?
|
+-- Simple request/response?
|   +-- HTTPS (default for REST)
|
+-- Real-time push, bidirectional updates (chat, live presence)?
|   +-- WebSockets (plan for sticky connections & backpressure)
|
+-- Async work, decoupling, smoothing spikes (orders, emails)?
|   +-- Queue (AMQP/Kafka/etc.)
|
+-- Microservices needing speed/streaming contracts?
    +-- gRPC over HTTP/2
```

### REST API Checklist (Interview Gold)

- [ ] Resources are NOUNS: `/users`, `/orders/{id}`
- [ ] Proper verbs via HTTP methods (GET/POST/PATCH/DELETE)
- [ ] PAGINATION always for lists (limit/offset or cursor)
- [ ] IDEMPOTENCY where needed (especially POST for payments/orders)
- [ ] Correct status codes (201 Created, 204 No Content, 400/401/403/404/409/429, 5xx)
- [ ] Versioning strategy (URL or headers), deprecation plan

### GraphQL Checklist

- [ ] Schema mirrors domain, modular types
- [ ] Depth/complexity limits configured
- [ ] N+1 avoided (batching, dataloaders)
- [ ] Caching strategy defined (often app-level)
- [ ] Explicit error shape (don't hide failures behind 200-only)

### Phase 0 Constraint Extraction

Before designing ANY API, extract these constraints:

| Constraint | Questions |
|------------|-----------|
| **Users & Usage** | DAU/MAU? Peak QPS? Read/write ratio? Payload sizes? |
| **Latency Target** | p50/p95/p99? Mobile vs desktop? Global vs local? |
| **Consistency** | Strong vs eventual? Where does correctness matter? |
| **Security** | Auth model? Threat surface? Compliance? |

**What I'm Thinking**: "What are the non-negotiable invariants?"
- "No double-charging" (payments)
- "Messages never delivered out of order per conversation" (chat)
- "Inventory can't go negative" (e-commerce)

### The 90-Second Interview Narrative for API Design

1. **Clarify** requirements + scale + SLOs
2. **Choose** API style (REST/GraphQL/gRPC)
3. **Design** resources, methods, pagination
4. **Security** authn/authz + rate limiting
5. **Documentation** OpenAPI spec
6. **Testing** contract tests + integration
7. **Deployment** canary rollout
8. **Trade-offs** explain choices made
