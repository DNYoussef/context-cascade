---
name: documentation
description: Documentation generation hub for code documentation, API docs, READMEs, and inline comments. Routes to doc-generator and related documentation tools. Use when generating or improving project documentation.
---

# Documentation

Central hub for generating and maintaining project documentation.

## Phase 0: Expertise Loading & Cognitive Frame Activation

```yaml
expertise_check:
  domain: documentation
  file: .claude/expertise/documentation.yaml

  if_exists:
    - Load documentation standards
    - Load project conventions
    - Apply style guides

  if_not_exists:
    - Flag discovery mode
    - Document patterns learned

cognitive_activation:
  - Activate hierarchical documentation framework (Keigo Wakugumi)
  - Activate morphological concept extraction (Al-Itar al-Sarfi)
  - Map codebase to audience levels
  - Extract documentation concepts from code structure
```

## Cognitive Frame 1: Keigo Wakugumi (Hierarchical Documentation)

Documentation organized by **audience level** and **scope hierarchy** - from executive summaries to implementation details.

### Rejisutaa Shurui (Audience Register Levels)

**SONKEIGO (Executive/Respectful)** - High-level overview, business value:
- **Purpose**: Explain "why this exists" for executives, product managers
- **Content**: Business value, ROI, strategic alignment, high-level architecture
- **Format**: Executive summary, one-page overviews, architecture diagrams
- **Example**: "This authentication system reduces security incidents by 40% and enables SSO integration"

**TEINEIGO (Developer/Polite)** - Technical details, API reference:
- **Purpose**: Enable developers to integrate and use the system
- **Content**: API reference, function signatures, parameters, return values, examples
- **Format**: OpenAPI specs, JSDoc, function-level documentation
- **Example**: "POST /api/auth/login - Accepts email/password, returns JWT token (200) or error (401)"

**CASUAL (Internal/Plain)** - Implementation notes, quick reference:
- **Purpose**: Help maintainers understand internal workings
- **Content**: Code comments, implementation notes, architectural decisions (ADRs)
- **Format**: Inline comments, ADRs, internal wikis
- **Example**: "// Uses bcrypt with cost factor 12 - balances security vs performance"

### Hierarchy Structure (Multi-Level Documentation)

```
LEVEL 1 (SYSTEM) - Architecture Overview
├── What: System purpose and scope
├── Why: Business drivers and constraints
├── How: High-level architecture
└── Who: Stakeholders and users
    |
    ├── LEVEL 2 (COMPONENT) - Module Documentation
    |   ├── Component responsibility
    |   ├── Dependencies and interfaces
    |   ├── Data flow diagrams
    |   └── Configuration options
    |       |
    |       ├── LEVEL 3 (INTERFACE) - API/Function Docs
    |       |   ├── Function signatures
    |       |   ├── Parameters and types
    |       |   ├── Return values and errors
    |       |   └── Usage examples
    |       |       |
    |       |       └── LEVEL 4 (IMPLEMENTATION) - Code Comments
    |       |           ├── Algorithm explanations
    |       |           ├── Edge case handling
    |       |           ├── Performance considerations
    |       |           └── TODO/FIXME notes
```

### Documentation Routing by Audience

| Audience | Register | Level | Example |
|----------|----------|-------|---------|
| CTO, Product Manager | SONKEIGO | L1 System | "Reduces auth latency by 60%" |
| External Developer | TEINEIGO | L3 Interface | "auth.login(email, password) -> Promise<Token>" |
| Team Developer | TEINEIGO | L2 Component | "Auth module handles JWT, OAuth, SAML" |
| Maintainer | CASUAL | L4 Implementation | "// Edge case: token refresh race condition" |
| New Hire | TEINEIGO | L2-L3 | "Architecture + API quick start" |

## Cognitive Frame 2: Al-Itar al-Sarfi lil-Tawthiq (Morphological Documentation)

Documentation sections **derived from code structure** - extract concepts from patterns, root words, and compositions.

### Concept Extraction Process

**ROOT (Jidhir)** - Core concept identified from codebase:
- Extracted from: Class names, module names, core functions
- Example: "Authentication" (from `AuthService`, `authenticateUser`, `auth/`)

**DERIVED (Mushtaq)** - Related concepts from same semantic root:
- Extracted from: Related functions, sub-modules, patterns
- Example from "Authentication" root:
  - Token validation (`validateToken`)
  - Session management (`createSession`, `revokeSession`)
  - Password operations (`hashPassword`, `verifyPassword`)
  - Authorization checks (`hasPermission`, `checkRole`)

**COMPOSED (Murakkab)** - Synthesized explanations combining multiple concepts:
- Extracted from: Code flow analysis, integration points
- Example: "Security Flow" = Authentication + Authorization + Session Management

### Morphological Documentation Pattern

```yaml
root_concept: Authentication
  derived_concepts:
    - token_validation:
        code_pattern: "*.validateToken(), *.verifyJWT()"
        documentation: "Token Validation - Verifies JWT signatures and expiration"

    - session_management:
        code_pattern: "session.*, *Session()"
        documentation: "Session Management - Maintains user state across requests"

    - password_security:
        code_pattern: "*.hash*, *.bcrypt*, *.salt*"
        documentation: "Password Security - Hashing and verification strategies"

  composed_explanations:
    - security_flow:
        combines: [authentication, authorization, session_management]
        documentation: |
          Security Flow:
          1. User submits credentials -> Authentication validates identity
          2. System checks permissions -> Authorization grants access
          3. Session created -> Session Management maintains state

    - auth_architecture:
        combines: [token_validation, password_security, session_management]
        documentation: |
          Authentication Architecture:
          - Password Security: bcrypt hashing (cost 12)
          - Token Validation: JWT with RS256 signing
          - Session Management: Redis-backed sessions (30min TTL)
```

### Auto-Generation Strategy

**Step 1: Extract ROOT concepts** from code structure:
```bash
# Identify root concepts from directory names
ls src/ -> "auth", "users", "payments", "notifications"

# Extract from class/module names
grep "class " src/**/*.js -> "AuthService", "UserRepository", "PaymentProcessor"
```

**Step 2: Derive RELATED concepts** using pattern matching:
```bash
# Find derived functions for "auth" root
grep -r "auth" src/ -> "authenticate()", "validateToken()", "hashPassword()"

# Group by semantic similarity
- auth.* -> Authentication operations
- *Token* -> Token management
- *Password* -> Password operations
```

**Step 3: Synthesize COMPOSED explanations** from flow analysis:
```bash
# Trace code flow through modules
AuthService.login() -> UserRepository.findByEmail() -> Session.create()

# Generate flow documentation
"Login Flow: AuthService validates credentials, UserRepository retrieves user, Session creates session token"
```

## When to Use This Skill

Use documentation when:
- Generating README files
- Creating API documentation
- Adding inline code comments
- Building documentation sites
- Documenting architecture

## Sub-Skills

| Skill | Use Case |
|-------|----------|
| doc-generator | Generate documentation |
| doc-readme | README generation |
| doc-api | API documentation |
| doc-inline | Inline comments |

## Documentation Types

### Hierarchical Documentation Template (Cognitive-Enhanced)

```yaml
documentation_output:
  # LEVEL 1 - SONKEIGO (Executive)
  executive_summary:
    target_audience: [CTO, Product Manager, Stakeholders]
    register: SONKEIGO
    sections:
      - what: "System purpose in one sentence"
      - why: "Business value and ROI"
      - impact: "Key metrics (40% faster, 60% reduction, etc.)"
      - architecture_diagram: "High-level system overview"

  # LEVEL 2 - TEINEIGO (Developer - Component)
  component_documentation:
    target_audience: [Team Developers, Contributors]
    register: TEINEIGO
    sections:
      - component_overview:
          extracted_from: "Directory structure (src/auth/, src/users/)"
          root_concepts: ["Authentication", "User Management"]
      - responsibilities: "What each component does"
      - dependencies: "Component interaction diagram"
      - configuration: "Environment variables, config options"

  # LEVEL 3 - TEINEIGO (Developer - Interface)
  api_documentation:
    target_audience: [External Developers, Integration Teams]
    register: TEINEIGO
    sections:
      - api_reference:
          format: openapi|jsdoc|sphinx
          output: html|markdown|json
          extracted_from: "Function signatures, JSDoc comments"
          includes:
            - endpoints: "Derived from route definitions"
            - parameters: "Extracted from function params"
            - responses: "Composed from return types + error handling"
            - examples: "Generated from test cases"

  # LEVEL 4 - CASUAL (Internal - Implementation)
  inline_comments:
    target_audience: [Maintainers, Future Self]
    register: CASUAL
    sections:
      - implementation_notes:
          style: jsdoc|docstring|rustdoc
          coverage:
            - functions: "Algorithm explanations"
            - classes: "Design pattern rationale"
            - complex_logic: "Edge cases and why"
          extracted_from: "Code analysis + complexity detection"

# Morphological Extraction Applied
concept_mapping:
  root_concepts:
    - extracted_from: ["Class names", "Module names", "Directory structure"]
    - example: "Authentication from AuthService, auth/, authenticateUser()"

  derived_concepts:
    - extracted_from: ["Related functions", "Pattern matching"]
    - example: "Token validation from *.validateToken(), *.verifyJWT()"

  composed_explanations:
    - extracted_from: ["Code flow tracing", "Integration points"]
    - example: "Security Flow = Authentication + Authorization + Session"
```

### README Generation
```yaml
type: readme
register: TEINEIGO (Developer audience)
hierarchy_level: L2-L3 (Component + Interface)
sections:
  - title_and_badges
  - description: "Extracted from package.json, root comment"
  - installation: "Derived from package.json scripts"
  - usage: "Composed from examples/ directory"
  - api_reference: "Links to L3 API docs"
  - contributing: "CASUAL register for maintainers"
  - license
```

### API Documentation
```yaml
type: api
register: TEINEIGO
hierarchy_level: L3 (Interface)
format: openapi|jsdoc|sphinx
output: html|markdown|json
morphological_extraction:
  - root: "Extract from route definitions"
  - derived: "Extract from middleware, validators"
  - composed: "Synthesize request/response flows"
includes:
  - endpoints
  - parameters
  - responses
  - examples
```

### Inline Comments
```yaml
type: inline
register: CASUAL
hierarchy_level: L4 (Implementation)
style: jsdoc|docstring|rustdoc
morphological_extraction:
  - root: "Core algorithm concept"
  - derived: "Helper functions, edge cases"
  - composed: "Overall flow explanation"
coverage:
  - functions
  - classes
  - complex_logic
```

## MCP Requirements

- **claude-flow**: For orchestration
- **Read/Write**: For file operations

## Recursive Improvement Integration (v2.1)

### Eval Harness Integration

```yaml
benchmark: documentation-benchmark-v1
  tests:
    - doc-001: README completeness
    - doc-002: API doc accuracy
  minimum_scores:
    completeness: 0.85
    accuracy: 0.90
```

### Memory Namespace

```yaml
namespaces:
  - documentation/generated/{id}: Generated docs
  - documentation/templates: Doc templates
  - improvement/audits/documentation: Skill audits
```

### Uncertainty Handling

```yaml
confidence_check:
  if confidence >= 0.8:
    - Generate documentation
  if confidence 0.5-0.8:
    - Show preview, ask confirmation
  if confidence < 0.5:
    - Ask for style preferences
```

### Cross-Skill Coordination

Works with: **code-review-assistant**, **api-development**, **feature-dev-complete**



## Core Principles

### 1. Documentation as Code Synchronization, Not Artifact Generation
Documentation becomes stale the moment it diverges from code. Treating documentation as a separate artifact that must be manually updated creates guaranteed drift. Instead, documentation should be generated from code structure, type signatures, and inline comments, ensuring synchronization by design. README sections describe usage patterns, but API references should derive from source truth in the codebase itself.

### 2. Audience-Specific Documentation Layers
Documentation serves multiple audiences with conflicting needs: quick-start users need minimal viable knowledge, API consumers need comprehensive references, and contributors need architectural context. A single documentation artifact that tries to serve all audiences creates cognitive overload for beginners and insufficient depth for experts. Layered documentation with clear navigation between levels optimizes for each audience's distinct goals.

### 3. Completeness Metrics Over Coverage Metrics
High code coverage (90% of functions documented) does not guarantee useful documentation. A function with a docstring saying "handles user data" provides zero additional information beyond the function name. Completeness metrics (parameters explained, return values specified, edge cases documented, examples provided) measure documentation utility rather than documentation existence, preventing theater that satisfies linters without serving readers.

----------|--------------|------------------|
| **Manually writing API documentation** | Diverges from code immediately. Parameters change, functions added/removed, return types evolve. Manual docs lag reality, misleading users and wasting maintainer time on sync. | Generate API docs from code: JSDoc -> html, Python docstrings -> Sphinx, Rust comments -> rustdoc. Source of truth is code, docs are derived artifact. |
| **README everything at once** | Overwhelms new users with 50-page READMEs covering every edge case. Buries essential quick-start information. Intimidates contributors. Reduces engagement with critical sections. | Layered docs: README (quick-start + links), /docs/api (reference), /docs/architecture (deep dive), /docs/contributing (process). Progressive disclosure based on user journey. |
| **Documenting without examples** | Abstract descriptions of parameters and return values require users to infer usage. Increases cognitive load. Leads to misuse and support burden. Examples communicate intent faster than prose. | Every public API function needs working example. Show common use case, edge case handling, and integration pattern. Runnable code > paragraphs of explanation. |



## Changelog

### v2.2.0 (2025-12-19) - Cognitive Lensing Enhancement

**Added: Cognitive Frame System**
- Primary frame: Hierarchical (Japanese Keigo Wakugumi) for multi-level audience organization
- Secondary frame: Morphological (Arabic Al-Itar al-Sarfi) for concept extraction from code
- Cognitive activation in Phase 0 before documentation generation

**Hierarchical Documentation (Keigo Wakugumi)**:
- SONKEIGO register: Executive-level documentation (business value, ROI, architecture)
- TEINEIGO register: Developer-level documentation (API reference, technical details)
- CASUAL register: Internal documentation (code comments, implementation notes)
- 4-level hierarchy: L1 System -> L2 Component -> L3 Interface -> L4 Implementation
- Audience routing table mapping stakeholders to appropriate documentation levels

**Morphological Concept Extraction (Al-Itar al-Sarfi)**:
- ROOT extraction: Core concepts from class/module names and directory structure
- DERIVED extraction: Related concepts via pattern matching and semantic similarity
- COMPOSED synthesis: Combined explanations from code flow tracing
- Auto-generation strategy for extracting documentation from code patterns
- Example: "Authentication" root -> Token validation, Session management, Password security (derived) -> Security flow (composed)

**Enhanced Documentation Templates**:
- Hierarchical output template showing all 4 levels with audience mapping
- README generation mapped to L2-L3 (Component + Interface) with TEINEIGO register
- API documentation at L3 with morphological extraction patterns
- Inline comments at L4 with CASUAL register for maintainers
- Concept mapping workflow: root -> derived -> composed explanations

**Integration**:
- Cognitive frame activation in Phase 0 expertise loading
- Multi-level documentation hierarchy enforced in output templates
- Pattern-based concept extraction from codebase structure
- Audience-aware documentation routing based on register levels

**Rationale**: Documentation requires serving multiple audiences (executives to maintainers) with different information needs, while extracting concepts systematically from code structure rather than manual writing.

### v2.1.0 (Previous)
- Added Recursive Improvement Integration
- Added Eval Harness benchmarks
- Added Memory namespace configuration
- Added Uncertainty handling



## Anti-Patterns

| Anti-Pattern | Why It Fails | Correct Approach |
|-------------|--------------|------------------|
| **Documentation Separate from Code** | Documentation in wikis, Google Docs, or Confluence becomes stale because it is not version-controlled or reviewed with code changes. API changes break documentation silently, creating documentation-code drift that misleads users. | Store documentation in `/docs` directory within code repository. Version control docs alongside code using Git. Require documentation updates in code review for any public API or architecture change. Auto-generate API docs from code annotations (JSDoc, docstrings). |
| **No Working Examples** | API reference without runnable examples forces users to guess how to use the API. Example-free docs result in support tickets asking "how do I actually use this?" for basic use cases. | Include working code examples for common use cases in documentation. Provide copy-paste starter code in README. Create `/examples` directory with runnable sample applications. Validate examples in CI/CD to ensure they stay functional. |
| **Waiting for Perfect Documentation** | Delaying documentation until it is "comprehensive" and "polished" results in zero documentation. Perfectionism blocks creation, leaving new developers with no guidance. Undocumented systems have high onboarding friction and knowledge silos. | Start with essential documentation: README (what, why, how to run), CONTRIBUTING (how to contribute), API reference (public interfaces). Incrementally add docs based on user questions. Accept imperfect docs and iterate based on feedback. Documentation improves through use, not upfront planning. |

---

## Conclusion

Documentation generation transforms knowledge silos into accessible, version-controlled resources that enable onboarding, contribution, and long-term maintainability. This skill provides automated documentation workflows for READMEs, API docs, inline comments, and architecture guides, treating documentation as first-class code artifacts subject to review and validation.

Use this skill to generate essential documentation (README, API reference, deployment guides) from templates, auto-generate API docs from code annotations (JSDoc, docstrings, Rustdoc), and validate documentation in CI/CD (broken links, outdated examples). The expertise loading system (Phase 0) enables domain-aware documentation that follows project conventions and style guides.

The key insight is that documentation-code drift occurs when documentation is not version-controlled and reviewed alongside code changes. Storing docs in wikis or Google Docs guarantees staleness - public API changes break docs silently, misleading users. Version-controlling documentation in `/docs` directory ensures synchronization, enabling documentation updates to be required in code review.

Documentation written for current experts is useless - the people who need docs are those unfamiliar with the system (new hires, contributors, future self after 6 months). Including working examples, "Getting Started" sections, and architecture decision records (ADRs) documenting WHY decisions were made reduces onboarding friction and prevents knowledge loss when team members leave.

Success requires accepting that incomplete documentation is better than none. Perfectionism blocks documentation creation - teams delay writing docs until they are "comprehensive," resulting in zero documentation. Starting with essential docs (README with installation, CONTRIBUTING, API reference) provides 80% of value with 20% of effort, enabling incremental improvement based on user questions and feedback. Documentation is a continuous discipline, not a one-time artifact.