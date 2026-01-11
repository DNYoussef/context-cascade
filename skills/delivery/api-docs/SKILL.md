/*============================================================================*/
/* API-DOCS SKILL :: VERILINGUA x VERIX EDITION                      */
/*============================================================================*/

---
name: api-docs
version: 1.0.0
description: |
  [assert|neutral] Generate and maintain comprehensive API documentation using OpenAPI 3.0, Swagger UI, and GraphQL Playground. Use when documenting REST APIs, GraphQL services, or creating API reference materials. Ensu [ground:given] [conf:0.95] [state:confirmed]
category: delivery
tags:
- delivery
- development
- workflow
author: ruv
cognitive_frame:
  primary: aspectual
  goal_analysis:
    first_order: "Execute api-docs workflow"
    second_order: "Ensure quality and consistency"
    third_order: "Enable systematic delivery processes"
---

/*----------------------------------------------------------------------------*/
/* S0 META-IDENTITY                                                            */
/*----------------------------------------------------------------------------*/

[define|neutral] SKILL := {
  name: "api-docs",
  category: "delivery",
  version: "1.0.0",
  layer: L1
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S1 COGNITIVE FRAME                                                          */
/*----------------------------------------------------------------------------*/

[define|neutral] COGNITIVE_FRAME := {
  frame: "Aspectual",
  source: "Russian",
  force: "Complete or ongoing?"
} [ground:cognitive-science] [conf:0.92] [state:confirmed]

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.

/*----------------------------------------------------------------------------*/
/* S2 TRIGGER CONDITIONS                                                       */
/*----------------------------------------------------------------------------*/

[define|neutral] TRIGGER_POSITIVE := {
  keywords: ["api-docs", "delivery", "workflow"],
  context: "user needs api-docs capability"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S3 CORE CONTENT                                                             */
/*----------------------------------------------------------------------------*/

# API Documentation Generator (Gold Tier)

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.




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
   - Enable "Try It Out" fu

/*----------------------------------------------------------------------------*/
/* S4 SUCCESS CRITERIA                                                         */
/*----------------------------------------------------------------------------*/

[define|neutral] SUCCESS_CRITERIA := {
  primary: "Skill execution completes successfully",
  quality: "Output meets quality thresholds",
  verification: "Results validated against requirements"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S5 MCP INTEGRATION                                                          */
/*----------------------------------------------------------------------------*/

[define|neutral] MCP_INTEGRATION := {
  memory_mcp: "Store execution results and patterns",
  tools: ["mcp__memory-mcp__memory_store", "mcp__memory-mcp__vector_search"]
} [ground:witnessed:mcp-config] [conf:0.95] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S6 MEMORY NAMESPACE                                                         */
/*----------------------------------------------------------------------------*/

[define|neutral] MEMORY_NAMESPACE := {
  pattern: "skills/delivery/api-docs/{project}/{timestamp}",
  store: ["executions", "decisions", "patterns"],
  retrieve: ["similar_tasks", "proven_patterns"]
} [ground:system-policy] [conf:1.0] [state:confirmed]

[define|neutral] MEMORY_TAGGING := {
  WHO: "api-docs-{session_id}",
  WHEN: "ISO8601_timestamp",
  PROJECT: "{project_name}",
  WHY: "skill-execution"
} [ground:system-policy] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S7 SKILL COMPLETION VERIFICATION                                            */
/*----------------------------------------------------------------------------*/

[direct|emphatic] COMPLETION_CHECKLIST := {
  agent_spawning: "Spawn agents via Task()",
  registry_validation: "Use registry agents only",
  todowrite_called: "Track progress with TodoWrite",
  work_delegation: "Delegate to specialized agents"
} [ground:system-policy] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S8 ABSOLUTE RULES                                                           */
/*----------------------------------------------------------------------------*/

[direct|emphatic] RULE_NO_UNICODE := forall(output): NOT(unicode_outside_ascii) [ground:windows-compatibility] [conf:1.0] [state:confirmed]

[direct|emphatic] RULE_EVIDENCE := forall(claim): has(ground) AND has(confidence) [ground:verix-spec] [conf:1.0] [state:confirmed]

[direct|emphatic] RULE_REGISTRY := forall(agent): agent IN AGENT_REGISTRY [ground:system-policy] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* PROMISE                                                                     */
/*----------------------------------------------------------------------------*/

[commit|confident] <promise>API_DOCS_VERILINGUA_VERIX_COMPLIANT</promise> [ground:self-validation] [conf:0.99] [state:confirmed]
