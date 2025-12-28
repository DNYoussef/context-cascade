---
name: api-docs
description: Generate and maintain comprehensive API documentation using OpenAPI 3.0, Swagger UI, and GraphQL Playground. Use when documenting REST APIs, GraphQL services, or creating API reference materials. Ensures consistent, machine-readable, and developer-friendly documentation.
---

# API Documentation Generator (Gold Tier)


## When to Use This Skill

- **API Development**: Building or documenting REST APIs, GraphQL APIs, or other web services
- **API Versioning**: Managing multiple API versions or migration strategies
- **Developer Experience**: Creating interactive documentation for API consumers
- **OpenAPI/Swagger**: Generating or maintaining OpenAPI specifications
- **Integration Work**: Helping external teams understand and use your APIs

## When NOT to Use This Skill

- **Non-API Documentation**: General code documentation, user manuals, or internal wikis
- **No API Surface**: Pure frontend apps, CLI tools, or embedded systems without APIs
- **Legacy Systems**: APIs without code access or with undocumented proprietary protocols
- **Incompatible Stacks**: Non-HTTP protocols (MQTT, gRPC) requiring specialized tooling

## Success Criteria

- [ ] API endpoints fully documented with request/response schemas
- [ ] Authentication and authorization flows clearly explained
- [ ] Interactive API explorer (Swagger UI/GraphQL Playground) functional
- [ ] Error codes and handling strategies documented
- [ ] Rate limiting and usage guidelines specified
- [ ] Code examples provided for common use cases
- [ ] Versioning strategy documented if applicable

## Edge Cases to Handle

- **Missing Type Annotations**: Infer schemas from runtime behavior or database models
- **Dynamic Routes**: Document parameterized endpoints and path variables
- **Nested Resources**: Handle complex resource hierarchies and relationships
- **File Uploads**: Document multipart/form-data and binary payloads
- **Webhooks**: Document callback URLs and event payloads
- **Deprecated Endpoints**: Mark sunset dates and migration paths

## Guardrails

- **NEVER** expose internal implementation details or security vulnerabilities in public docs
- **ALWAYS** validate generated specs against OpenAPI/GraphQL schema validators
- **NEVER** ship documentation without testing example requests
- **ALWAYS** include authentication requirements for protected endpoints
- **NEVER** assume default values - explicitly document all parameters
- **ALWAYS** document error responses, not just success cases

## Evidence-Based Validation

- [ ] Run generated OpenAPI spec through swagger-cli validate
- [ ] Test all documented endpoints with actual HTTP requests
- [ ] Verify GraphQL schema with graphql-schema-linter
- [ ] Check accessibility of interactive docs with axe-core
- [ ] Validate examples compile and execute successfully
- [ ] Review documentation with API consumers for clarity

Generate production-quality API documentation with OpenAPI 3.0, automated validation, and interactive documentation formats.

## When to Use This Skill

Use when documenting new or existing APIs, creating REST API specifications, maintaining GraphQL schema documentation, or generating interactive API explorers with Swagger UI/GraphQL Playground. Ideal for API-first development, maintaining accurate documentation, and ensuring OpenAPI 3.0 compliance.

## API Documentation Types

### REST API Documentation
- OpenAPI 3.0 specifications
- Endpoint descriptions and parameters
- Request/response examples
- Authentication schemes
- Error codes and handling

### GraphQL Documentation
- Schema definitions
- Query and mutation documentation
- Type system reference
- Resolver documentation

## Process

1. **Analyze API structure**
   - Identify all endpoints/operations
   - Document request/response schemas
   - Define authentication requirements
   - Catalog error responses

2. **Generate OpenAPI/GraphQL spec**
   - Write structured YAML/SDL definitions
   - Include comprehensive examples
   - Document edge cases
   - Add usage guidelines

3. **Create interactive documentation**
   - Configure Swagger UI for REST APIs
   - Set up GraphQL Playground
   - Add authentication testing support
   - Enable "Try It Out" functionality

4. **Add versioning and deprecation notices**
   - Document API version compatibility
   - Mark deprecated endpoints
   - Provide migration guides
   - Include changelog

5. **Generate code examples**
   - Client SDK examples (curl, JavaScript, Python)
   - Authentication flows
   - Common use case scenarios
   - Error handling patterns

## Gold Tier Features

### Automated Specification Generation
- **Framework Support**: Flask, FastAPI, Express.js, Django REST Framework
- **Auto-Detection**: Automatically identifies web framework from source code
- **Route Extraction**: Parses decorators, docstrings, and JSDoc comments
- **Parameter Inference**: Extracts path/query/body parameters from function signatures
- **Schema Generation**: Creates reusable component schemas from type hints

### Multi-Tool Validation
- **Syntax Validation**: YAML/JSON syntax checking with yamllint/jq
- **OpenAPI Compliance**: swagger-cli and openapi-generator-cli validation
- **Strict Mode**: Treat warnings as errors for production specs
- **Validation Reports**: Detailed error/warning reports with timestamps
- **Field Checks**: Required fields, best practices, security schemes

### Interactive Documentation
- **Swagger UI**: Interactive API explorer with "Try it out" functionality
- **ReDoc**: Clean three-panel documentation with search
- **Markdown**: Human-readable documentation with tables
- **HTML**: Custom templates with styling

### Code Examples
- **Multi-Language**: cURL, JavaScript, Python, Go examples
- **Authentication**: Automatic header injection (Bearer, API Key)
- **Request/Response**: Complete examples with realistic data

## Available Resources

### Scripts (resources/scripts/)
1. **generate_openapi.py**
   - Generate OpenAPI 3.0 specs from source code
   - Framework auto-detection (Flask, FastAPI, Express, Django)
   - Route extraction with docstrings/JSDoc
   - Component schema generation
   - YAML/JSON output formats

2. **validate_spec.sh**
   - Multi-tool validation pipeline
   - YAML/JSON syntax checking
   - OpenAPI 3.0 compliance validation
   - Best practices enforcement
   - Validation report generation

3. **create_docs.py**
   - Markdown documentation generation
   - Swagger UI setup
   - ReDoc setup
   - Custom HTML templates
   - Schema-to-example conversion

### Templates (resources/templates/)
1. **openapi-3.0.yaml** - Complete OpenAPI 3.0 specification template
2. **endpoint-template.json** - Reusable endpoint definition with examples
3. **schema-template.json** - Comprehensive schema patterns

### Tests (tests/)
1. **test-1-openapi-generation.md** - 12 test cases for spec generation
2. **test-2-spec-validation.md** - 12 test cases for validation
3. **test-3-documentation.md** - 12 test cases for documentation

## Usage Examples

### Generate OpenAPI Spec from Source Code
```bash
# Auto-detect framework and generate spec
python resources/scripts/generate_openapi.py \
  --source ./src \
  --output openapi.yaml \
  --framework auto

# Explicit framework with custom info
python resources/scripts/generate_openapi.py \
  --source ./app \
  --output api-spec.json \
  --framework fastapi \
  --format json \
  --title "My API" \
  --version "2.0.0"
```

### Validate OpenAPI Specification
```bash
# Standard validation
./resources/scripts/validate_spec.sh openapi.yaml

# Strict mode (warnings as errors)
./resources/scripts/validate_spec.sh openapi.yaml --strict

# Save validation report
./resources/scripts/validate_spec.sh openapi.yaml \
  --output validation-report.txt \
  --verbose
```

### Generate Documentation
```bash
# Swagger UI (interactive)
python resources/scripts/create_docs.py \
  --spec openapi.yaml \
  --output docs/ \
  --format html \
  --swagger-ui

# ReDoc (clean layout)
python resources/scripts/create_docs.py \
  --spec openapi.yaml \
  --output docs/ \
  --format html \
  --redoc

# Markdown documentation
python resources/scripts/create_docs.py \
  --spec openapi.yaml \
  --output docs/ \
  --format markdown

# Both formats
python resources/scripts/create_docs.py \
  --spec openapi.yaml \
  --output docs/ \
  --format both \
  --swagger-ui
```

## Best Practices

- **Completeness**: Document all endpoints, parameters, responses
- **Accuracy**: Keep docs synchronized with implementation
- **Clarity**: Use clear descriptions and examples
- **Consistency**: Follow OpenAPI 3.0 or GraphQL standards
- **Usability**: Enable interactive testing
- **Automation**: Integrate generation/validation into CI/CD
- **Versioning**: Track API versions and deprecations
- **Testing**: Use validation before deployment

## Integration with CI/CD

```yaml
# .github/workflows/api-docs.yml

on: [push, pull_request]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Generate OpenAPI Spec
        run: |
          python skills/api-docs/resources/scripts/generate_openapi.py \
            --source ./src --output openapi.yaml

      - name: Validate Specification
        run: |
          bash skills/api-docs/resources/scripts/validate_spec.sh \
            openapi.yaml --strict

      - name: Generate Documentation
        run: |
          python skills/api-docs/resources/scripts/create_docs.py \
            --spec openapi.yaml --output docs/ --format both --swagger-ui

      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./docs
```

## Performance Metrics

| Operation | Small API | Medium API | Large API |
|-----------|-----------|------------|-----------|
| Generation | < 1s | < 3s | < 10s |
| Validation | < 1s | < 2s | < 5s |
| Documentation | < 2s | < 5s | < 15s |

**Specifications:**
- Small: 5-20 endpoints
- Medium: 20-100 endpoints
- Large: 100+ endpoints

## Core Principles

API Documentation operates on 3 fundamental principles:

### Principle 1: Documentation as Code

API specifications should be machine-readable, version-controlled, and generated from source code rather than maintained manually.

In practice:
- OpenAPI specs live in version control alongside code (docs/openapi.yaml)
- Automated generation from code annotations prevents drift between implementation and documentation
- CI/CD validates specs on every commit using swagger-cli and openapi-generator-cli
- Breaking changes detected automatically through spec comparison tools

### Principle 2: Interactive Over Static

Developers learn APIs by trying them, not just reading about them. Interactive documentation enables exploration and experimentation.

In practice:
- Swagger UI provides "Try it out" functionality for every endpoint
- Authentication is pre-configured so developers can test with real credentials
- Response examples show actual JSON/XML structures, not just schema definitions
- Error cases documented with real error payloads developers will encounter

### Principle 3: Completeness Through Automation

Comprehensive documentation requires documenting every parameter, response, and error code. Manual documentation always has gaps.

In practice:
- Framework auto-detection extracts routes from Flask/FastAPI/Express/Django automatically
- Type hints and JSDoc comments become parameter schemas without duplication
- Validation rules (required fields, enum values, constraints) flow from code to spec
- Missing documentation triggers validation warnings, not silent gaps

## Common Anti-Patterns

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| **Manual Specification Maintenance** | Hand-writing OpenAPI specs separate from code causes documentation drift as code evolves | Generate specs from code annotations (docstrings, JSDoc, decorators) using framework-specific tools; treat specs as build artifacts |
| **Example-Free Documentation** | Schema-only docs without concrete request/response examples force developers to construct examples mentally | Include realistic examples for every endpoint; show full request bodies and response payloads with actual data |
| **Missing Error Documentation** | Documenting only success cases (200 OK) while omitting error responses (4xx, 5xx) leaves developers unprepared for failures | Document all error codes with example payloads; explain what triggers each error; show error response schemas |
| **Static-Only Documentation** | PDF or Markdown docs without interactive API explorer require developers to use separate tools (Postman, curl) for testing | Deploy Swagger UI or ReDoc with "Try it out" functionality; enable authentication testing in browser; provide runnable examples |
| **Versioning Neglect** | Single documentation version for multiple API versions confuses developers about which features are available | Document each API version separately; mark deprecated endpoints with sunset dates; provide migration guides between versions |
| **Validation-Free Publishing** | Deploying documentation without validating OpenAPI compliance results in broken specs that tools cannot parse | Run swagger-cli validate and openapi-generator-cli validate in CI/CD; treat validation failures as build breaks; enforce strict mode |

## Conclusion

API Documentation Generator transforms API specification from a manual, error-prone chore into an automated, reliable artifact generated directly from source code. By extracting documentation from Flask decorators, FastAPI type hints, Express JSDoc comments, and Django REST Framework serializers, it ensures documentation stays synchronized with implementation through continuous validation in CI/CD pipelines.

The skill's three-phase workflow - generation from code, multi-tool validation (swagger-cli, openapi-generator-cli, yamllint), and interactive documentation deployment (Swagger UI, ReDoc) - creates a comprehensive documentation pipeline that catches errors early and delivers developer-friendly exploration tools. The framework auto-detection intelligently identifies your web framework and applies appropriate extraction strategies, while the validation pipeline enforces OpenAPI 3.0 compliance with strict mode treating warnings as errors for production specs.

Use this skill when building new APIs that need documentation from day one, when refactoring existing APIs where documentation has drifted from reality, or when onboarding external developers who need clear API references. The automated generation prevents documentation debt from accumulating, while interactive Swagger UI enables developers to understand and test endpoints without leaving the browser. The result is API documentation that developers actually trust and use rather than outdated PDFs gathering dust in wikis.