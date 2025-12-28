---
name: template-extractor
description: Reverse-engineer document templates to extract exact design specifications and generate reusable AI prompts for pixel-perfect document recreation
category: tooling
version: 1.1.0
triggers:
  - "extract template"
  - "reverse engineer format"
  - "document style guide"
  - "replicate formatting"
  - "template from document"
  - "document specification"
  - "format analysis"
mcp_servers:
  required: []
  optional: [memory-mcp]
  auto_enable: false
input_contract:
  required:
    document_path:
      type: string
      description: Absolute path to source document
    output_directory:
      type: string
      description: Where to save extracted specifications
output_contract:
  guaranteed:
    - TEMPLATE_SPEC.md
    - AI_PROMPT.md
    - assets/
    - ASSETS.md
    - README.md
  conditional:
    - extraction_results.json
    - unpacked/
    - verification_report.md
---
