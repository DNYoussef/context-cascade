# Example 2: PDF Generation Discovery

## Scenario

User needs to generate PDF reports from application data.

## Discovery Process

### Step 1: Initial Query

```bash
./scripts/multi-model/delegate.sh gemini "Best PDF generation libraries for JavaScript 2024. Compare pdfkit, puppeteer, react-pdf, pdf-lib. Include performance benchmarks and use cases."
```

### Step 2: Gemini Response (Synthesized)

```yaml
discovered_libraries:
  - name: pdfkit
    type: "Programmatic"
    use_case: "Simple documents, invoices"
    bundle_size: "~200KB"
    pros: ["Lightweight", "No browser needed", "Fast"]
    cons: ["Manual layout", "No HTML support"]

  - name: puppeteer
    type: "Browser-based"
    use_case: "Complex layouts, HTML to PDF"
    bundle_size: "~50MB (Chromium)"
    pros: ["Perfect rendering", "CSS support", "Screenshots"]
    cons: ["Heavy", "Slower", "Server resources"]

  - name: react-pdf
    type: "React-based"
    use_case: "React apps, dynamic content"
    bundle_size: "~500KB"
    pros: ["React components", "Declarative", "Styling"]
    cons: ["React only", "Learning curve"]

  - name: pdf-lib
    type: "Manipulation"
    use_case: "Modify existing PDFs, forms"
    bundle_size: "~300KB"
    pros: ["Modify existing", "Form filling", "Merging"]
    cons: ["Not for creation from scratch"]

benchmarks:
  simple_invoice:
    pdfkit: "50ms"
    puppeteer: "800ms"
    react-pdf: "200ms"

  complex_report:
    pdfkit: "200ms"
    puppeteer: "1200ms"
    react-pdf: "500ms"
```

### Step 3: Decision Matrix

| Requirement | pdfkit | puppeteer | react-pdf |
|-------------|--------|-----------|-----------|
| Simple invoices | Best | Overkill | Good |
| Complex layouts | Hard | Best | Good |
| Performance | Best | Slow | Good |
| Bundle size | Small | Large | Medium |
| Existing HTML | No | Yes | No |

### Step 4: Contextual Decision

**Project context**:
- Need to generate monthly reports from data
- Reports have charts and tables
- Currently using React frontend
- Performance matters (batch generation)

**Decision**: Use **react-pdf** for:
- React integration
- Good performance for batch jobs
- Reasonable bundle size
- Declarative chart/table components

**Fallback**: For very complex layouts, consider puppeteer as secondary option.

### Step 5: Memory Storage

```json
{
  "key": "discovery/pdf/report-generation-2024",
  "value": {
    "chosen": "react-pdf",
    "alternatives": ["puppeteer for complex layouts"],
    "rejected": {
      "pdfkit": "Manual layout too tedious for complex reports",
      "pdf-lib": "For manipulation, not generation"
    },
    "context": "React app, batch report generation"
  },
  "tags": "WHO=multi-model-discovery,WHY=pdf-generation,PROJECT=dashboard"
}
```

## Outcome

- Avoided puppeteer's 50MB dependency for simple reports
- Chose library matching tech stack (React)
- Documented alternatives for future needs
