# Agent Identity & RBAC Generation Guide

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



**Version**: 1.0.0 (Agent Reality Map Compliance)
**Integration**: agent-creator v3.0+

This guide provides the complete process for generating Agent Reality Map compliant identities when creating new agents.

---

## Identity Components

Every agent MUST have these identity components in YAML frontmatter:

### 1. Agent ID (UUID)
```yaml
identity:
  agent_id: "550e8400-e29b-41d4-a716-446655440000"
```

**Generation**: Use `crypto.randomUUID()` or `uuidv4()` library
**Format**: UUIDv4 (36 characters with hyphens)
**Purpose**: Unique identifier for agent tracking, auditing, budget enforcement

---

### 2. Role Assignment

```yaml
identity:
  role: "developer"
  role_confidence: 0.9
```

**10 Available Roles**:
| Role | Use For | Confidence | Budget/Day |
|------|---------|------------|------------|
| `admin` | System design, infrastructure, full access | 0.95 | $100 |
| `developer` | Code implementation, general development | 0.9 | $30 |
| `reviewer` | Code review, quality analysis | 0.9 | $25 |
| `security` | Security audits, vulnerability scanning | 0.95 | $40 |
| `database` | Database design, schema, query optimization | 0.9 | $35 |
| `frontend` | UI/UX, React/Vue, CSS, accessibility | 0.85 | $25 |
| `backend` | API design, server logic, microservices | 0.85 | $30 |
| `tester` | Testing, QA, integration/e2e tests | 0.9 | $20 |
| `analyst` | Data analysis, reporting, metrics | 0.85 | $20 |
| `coordinator` | Orchestration, workflow management, planning | 0.9 | $50 |

**Role Assignment Algorithm**:

```javascript
// Step 1: Extract agent capabilities
const capabilities = ["coding", "api-design", "testing"];

// Step 2: Match to capability matrix
const roleRules = {
  "api-design": { role: "backend", confidence: 0.85 },
  "coding": { role: "developer", confidence: 0.9 },
  "security-audit": { role: "security", confidence: 0.95 },
  // ... see agent-capability-matrix.json for full list
};

// Step 3: Find highest confidence match
let bestMatch = { role: "developer", confidence: 0.7 }; // default
for (const capability of capabilities) {
  if (roleRules[capability] && roleRules[capability].confidence > bestMatch.confidence) {
    bestMatch = roleRules[capability];
  }
}

// Step 4: Validate against agent category
if (agentCategory === "security") {
  bestMatch.role = "security";
  bestMatch.confidence = 0.95;
}

// Step 5: Return assigned role
return bestMatch;
```

---

### 3. RBAC Permissions

```yaml
rbac:
  allowed_tools: [Read, Write, Edit, MultiEdit, Bash, Grep, Glob, Task, TodoWrite]
  path_scopes: ["src/**", "tests/**", "scripts/**", "config/**"]
  api_access: ["memory-mcp", "github"]
  requires_approval: false
  approval_threshold: 10.0
```

**Tool Permissions by Role**:

**Admin Role**:
```yaml
allowed_tools: [Read, Write, Edit, MultiEdit, Bash, Grep, Glob, Task, TodoWrite, WebSearch, WebFetch, KillShell, BashOutput, NotebookEdit]
denied_tools: []
path_scopes: ["**"]  # Full access
api_access: ["openai", "anthropic", "github", "memory-mcp", "connascence-analyzer", "flow-nexus", "ruv-swarm"]
```

**Developer Role**:
```yaml
allowed_tools: [Read, Write, Edit, MultiEdit, Bash, Grep, Glob, Task, TodoWrite]
denied_tools: [KillShell]
path_scopes: ["src/**", "tests/**", "scripts/**", "config/**"]
api_access: ["github", "memory-mcp"]
```

**Reviewer Role**:
```yaml
allowed_tools: [Read, Grep, Glob, Task, TodoWrite]
denied_tools: [Write, Edit, MultiEdit, Bash, KillShell]
path_scopes: ["**"]  # Read-only full access
api_access: ["memory-mcp", "connascence-analyzer"]
```

**Security Role**:
```yaml
allowed_tools: [Read, Grep, Glob, Bash, Task, TodoWrite, WebSearch]
denied_tools: [Write, Edit, KillShell]
path_scopes: ["**"]  # Read-only for audits
api_access: ["github", "memory-mcp", "connascence-analyzer"]
```

**Frontend/Backend Role**:
```yaml
allowed_tools: [Read, Write, Edit, Bash, Grep, Glob, Task, TodoWrite]
denied_tools: [KillShell, NotebookEdit]
path_scopes: ["frontend/**", "src/**", "components/**"]  # Frontend
# path_scopes: ["backend/**", "api/**", "src/**"]  # Backend
api_access: ["github", "memory-mcp"]
```

**Tester Role**:
```yaml
allowed_tools: [Read, Write, Edit, Bash, Grep, Glob, Task, TodoWrite]
denied_tools: [KillShell]
path_scopes: ["tests/**", "src/**", "scripts/**"]
api_access: ["memory-mcp"]
```

**Analyst Role**:
```yaml
allowed_tools: [Read, Grep, Glob, Task, TodoWrite, WebSearch, WebFetch]
denied_tools: [Write, Edit, Bash, KillShell]
path_scopes: ["**"]  # Read-only for analysis
api_access: ["memory-mcp"]
```

**Coordinator Role**:
```yaml
allowed_tools: [Read, Task, TodoWrite, Grep, Glob]
denied_tools: [Write, Edit, Bash, KillShell]
path_scopes: ["**"]  # Read-only for coordination
api_access: ["memory-mcp", "flow-nexus", "ruv-swarm"]
```

---

### 4. Budget Enforcement

```yaml
budget:
  max_tokens_per_session: 200000
  max_cost_per_day: 30
  currency: "USD"
```

**Budget by Role**:
| Role | Tokens/Session | Cost/Day | Rationale |
|------|----------------|----------|-----------|
| admin | 500,000 | $100 | High-level design, full system access |
| coordinator | 300,000 | $50 | Orchestration, multi-agent coordination |
| security | 250,000 | $40 | Comprehensive security audits |
| database | 200,000 | $35 | Complex schema, query optimization |
| developer | 200,000 | $30 | General code implementation |
| backend | 200,000 | $30 | API design, server logic |
| reviewer | 150,000 | $25 | Code review, analysis |
| frontend | 150,000 | $25 | UI components, styling |
| tester | 150,000 | $20 | Test writing, QA |
| analyst | 150,000 | $20 | Data analysis, reporting |

---

### 5. Metadata

```yaml
metadata:
  category: "delivery"
  specialist: true
  version: "1.0.0"
  tags: ["backend", "api", "development"]
```

**Categories**:
- `delivery` - Feature development, implementation
- `foundry` - Core agents, templates
- `operations` - DevOps, infrastructure, monitoring
- `orchestration` - Swarm coordination, consensus
- `platforms` - AI/ML, data, GraphQL, search
- `quality` - Testing, analysis, validation
- `research` - Analysis, literature, deep research
- `security` - Audits, compliance, penetration testing
- `specialists` - Domain-specific agents
- `tooling` - Automation, CLI, SDK, documentation

**Specialist Flag**:
- `true` - Narrow domain expertise (e.g., React specialist, SQL database specialist)
- `false` - General-purpose agent (e.g., coder, planner, reviewer)

---

## Complete Agent Template with Identity

```markdown
---
name: backend-api-specialist
description: Specialized backend API developer with expertise in REST, GraphQL, and microservices architecture

identity:
  agent_id: "62af40bf-feed-4249-9e71-759b938f530c"
  role: "backend"
  role_confidence: 0.85

rbac:
  allowed_tools: [Read, Write, Edit, Bash, Grep, Glob, Task, TodoWrite]
  denied_tools: [KillShell, NotebookEdit]
  path_scopes: ["backend/**", "api/**", "src/**", "tests/**"]
  api_access: ["github", "memory-mcp"]
  requires_approval: false
  approval_threshold: 10.0

budget:
  max_tokens_per_session: 200000
  max_cost_per_day: 30
  currency: "USD"

metadata:
  category: "specialists"
  specialist: true
  version: "1.0.0"
  tags: ["backend", "api", "rest", "graphql", "microservices"]
  created_at: "2025-01-17T00:00:00Z"

orchestration:
  primary_agent: backend-api-specialist
  support_agents: [database-specialist, security-manager, tester]
  coordination: sequential

capabilities:
  - api-design
  - backend-logic
  - microservices
  - database-integration
  - authentication
  - testing
---

# Backend API Specialist

You are a **Backend API Specialist** with comprehensive expertise in REST, GraphQL, and microservices architecture. Your role is to design and implement production-grade API endpoints with security, scalability, and maintainability.

## Core Identity

[Agent prompt content...]
```

---

## Identity Generation Workflow

### Step 1: Analyze Agent Specification

```javascript
// From Phase 1 (Specification)
const agentSpec = {
  name: "backend-api-specialist",
  description: "REST/GraphQL API development",
  domain: "Backend development",
  capabilities: ["api-design", "backend-logic", "microservices"],
  category: "specialists/backend"
};
```

### Step 2: Generate UUID

```javascript
const crypto = require('crypto');
const agentId = crypto.randomUUID();
// Result: "62af40bf-feed-4249-9e71-759b938f530c"
```

### Step 3: Assign Role

```javascript
const capabilityMatrix = {
  "api-design": { role: "backend", confidence: 0.85 },
  "backend-logic": { role: "backend", confidence: 0.85 },
  "microservices": { role: "backend", confidence: 0.85 }
};

// Find highest confidence
let role = "developer"; // default
let confidence = 0.7;

for (const cap of agentSpec.capabilities) {
  if (capabilityMatrix[cap] && capabilityMatrix[cap].confidence > confidence) {
    role = capabilityMatrix[cap].role;
    confidence = capabilityMatrix[cap].confidence;
  }
}

// Validate against category
if (agentSpec.category.includes("backend")) {
  role = "backend";
  confidence = 0.85;
}

// Result: { role: "backend", confidence: 0.85 }
```

### Step 4: Assign RBAC Permissions

```javascript
const rbacTemplates = {
  "backend": {
    allowed_tools: ["Read", "Write", "Edit", "Bash", "Grep", "Glob", "Task", "TodoWrite"],
    denied_tools: ["KillShell", "NotebookEdit"],
    path_scopes: ["backend/**", "api/**", "src/**", "tests/**"],
    api_access: ["github", "memory-mcp"],
    requires_approval: false,
    approval_threshold: 10.0
  },
  // ... other roles
};

const rbac = rbacTemplates[role];
```

### Step 5: Assign Budget

```javascript
const budgetTemplates = {
  "backend": {
    max_tokens_per_session: 200000,
    max_cost_per_day: 30,
    currency: "USD"
  },
  // ... other roles
};

const budget = budgetTemplates[role];
```

### Step 6: Generate Metadata

```javascript
const metadata = {
  category: agentSpec.category.split('/')[0], // "specialists"
  specialist: true, // based on category
  version: "1.0.0",
  tags: agentSpec.capabilities,
  created_at: new Date().toISOString()
};
```

### Step 7: Combine into Complete Identity

```yaml
identity:
  agent_id: "62af40bf-feed-4249-9e71-759b938f530c"
  role: "backend"
  role_confidence: 0.85

rbac:
  allowed_tools: [Read, Write, Edit, Bash, Grep, Glob, Task, TodoWrite]
  denied_tools: [KillShell, NotebookEdit]
  path_scopes: ["backend/**", "api/**", "src/**", "tests/**"]
  api_access: ["github", "memory-mcp"]
  requires_approval: false
  approval_threshold: 10.0

budget:
  max_tokens_per_session: 200000
  max_cost_per_day: 30
  currency: "USD"

metadata:
  category: "specialists"
  specialist: true
  version: "1.0.0"
  tags: ["api-design", "backend-logic", "microservices"]
  created_at: "2025-01-17T00:00:00Z"
```

---

## Validation Checklist

Before finalizing agent identity:

- [ ] UUID is valid UUIDv4 format
- [ ] Role is one of 10 defined roles
- [ ] Role confidence >= 0.7 (manual review if <0.7)
- [ ] All `allowed_tools` exist in tool registry
- [ ] `path_scopes` use valid glob patterns
- [ ] Budget limits are reasonable for role
- [ ] Category matches agent's purpose
- [ ] Tags accurately describe capabilities
- [ ] All required fields present

---

## Advanced: Custom Role Assignment

For agents with unique requirements, override automatic assignment:

```yaml
identity:
  agent_id: "custom-uuid"
  role: "admin"  # Override if agent needs elevated permissions
  role_confidence: 0.95
  role_justification: "Requires full system access for infrastructure automation"
```

**When to Override**:
- Agent needs broader permissions than capability-based assignment
- Security-critical agent requires elevated access
- Multi-domain agent (e.g., full-stack specialist)
- Coordinator managing multiple agent types

**Review Required**:
- All overrides must document justification
- Manual approval for `admin` role assignments
- Security review for custom `api_access` lists

---

## Integration with Migration Script

The `migrate-agent-identities.js` script uses this guide to automatically assign identities to existing agents. New agents created with agent-creator v3.0+ will have identities generated during creation.

**Manual Creation**:
```bash
# Generate UUID
node -e "console.log(require('crypto').randomUUID())"

# Use capability matrix
cat agents/identity/agent-capability-matrix.json

# Copy RBAC template
cat agents/identity/agent-rbac-rules.json
```

---

**Summary**: Every new agent MUST include identity, RBAC, budget, and metadata in YAML frontmatter. Use capability matrix for automatic role assignment, RBAC templates for permissions, and budget templates for resource limits. Validate all fields before finalizing agent.


---
*Promise: `<promise>AGENT_IDENTITY_GENERATION_GUIDE_VERIX_COMPLIANT</promise>`*
