---
name: template-extractor
description: Reverse-engineer document templates to extract exact design specifications and generate reusable AI prompts for pixel-perfect document recreation
---

# Template Extractor

## Overview

Template Extractor is a systematic reverse-engineering tool that extracts precise design specifications from existing documents (DOCX, PPTX, XLSX, PDF) to enable pixel-perfect recreation. Unlike visual inspection which leads to "close enough" approximations, this skill unpacks document file structures and parses their underlying XML to extract exact font sizes, color hex codes, spacing values, and layout configurations.

The skill generates two critical outputs: (1) a code-level technical specification with exact measurements and values, and (2) an AI-ready prompt that enables any language model to recreate documents in that exact style. This dual-output approach ensures both machine precision and human comprehension.

By validating extracted templates through test recreation and visual comparison, Template Extractor guarantees that generated specifications are accurate and actionable, eliminating the guesswork and iteration cycles typical of manual document formatting.

## When to Use

**Use When**:
- User provides a sample document (DOCX, PPTX, XLSX, or PDF) and wants to replicate its formatting exactly
- User needs to create a reusable document style guide from an existing file without manual measurement
- User wants to generate an AI prompt that enables consistent document generation across multiple files
- User needs to standardize document formatting across a team by extracting a reference template
- User is migrating from one document system to another and needs precise format specifications
- User wants to create a branded document generator that matches corporate style guides
- User needs to audit existing documents to document their design specifications
- User wants to ensure document formatting consistency without manually measuring fonts and spacing

**Do Not Use**:
- User wants to create a document from scratch without a reference template (use doc-generator or pptx-generation instead)
- User only needs to convert document formats without preserving exact styling (use standard conversion tools)
- User wants to improve or modify existing formatting rather than replicate it exactly
- User is working with handwritten documents or non-digital formats (no structured data to extract)
- User needs real-time document editing rather than specification extraction
- User's priority is content extraction rather than format specification

## Core Principles

### Principle 1: Systematic Extraction Over Visual Guessing

Human visual inspection of documents leads to approximations: "that looks like 14pt" or "probably Arial". Template Extractor treats documents as ZIP archives containing structured XML, unpacking them to access authoritative sources like `styles.xml`, `theme1.xml`, and `document.xml`. This approach extracts definitive values rather than best guesses.

**Why This Matters**: A "close enough" color (#333333 vs #1F1F1F) creates subtle inconsistency that compounds across documents. A 1pt font size difference (11pt vs 12pt) changes readability and layout flow. Manual inspection cannot reliably detect these differences, but XML parsing provides ground truth.

**In Practice**:
- Unpack DOCX/PPTX/XLSX files as ZIP archives to access internal XML structure
- Parse `word/styles.xml` for exact heading and body text specifications
- Extract `word/theme/theme1.xml` for color scheme definitions (hex values, not visual approximations)
- Read `word/document.xml` for page layout settings (margins, orientation, dimensions)
- Convert OOXML units (half-points, twips, EMUs) to standard measurements using precise formulas
- Extract embedded media files (logos, images) from `word/media/` directories
- For PDFs, use metadata extraction and text analysis to identify fonts and spacing patterns

### Principle 2: Dual Output (Specification + Prompt)

Template Extractor generates two complementary artifacts: a technical specification for developers/designers who need exact measurements, and an AI replication prompt for language models that will generate documents in this style. This separation serves distinct audiences while ensuring both receive accurate, actionable information.

**Why This Matters**: Developers need machine-readable values ("font: Calibri 11pt, line-height: 1.15, margin-top: 0pt, margin-bottom: 8pt") while AI systems need natural language instructions with embedded precision ("Use Calibri 11pt for body text with 1.15 line spacing. Add 8pt spacing after each paragraph."). A single output cannot optimize for both use cases.

**In Practice**:
- **Output 1 (TEMPLATE_SPEC.md)**: Structured technical reference
  - Markdown tables for heading hierarchy (H1/H2/H3 with exact fonts, sizes, weights, colors)
  - Color palette with hex codes, RGB values, and usage descriptions
  - Page configuration with exact margin measurements in inches
  - Table formatting rules (borders, padding, header/body styling)
  - List formatting (bullet styles, indentation, spacing)
  - Implementation notes for edge cases and quirks

- **Output 2 (AI_PROMPT.md)**: Natural language generation instructions
  - Imperative directives ("Create documents with these exact settings:")
  - Critical warnings ("CRITICAL: Use these exact fonts and sizes - no substitutions")
  - Usage context for each design element ("Primary color: #0078D4 for headings and accents")
  - Quality checklist to validate output ("Verify all colors use exact hex values")
  - Common mistake warnings ("Do NOT approximate colors - use exact hex codes")

### Principle 3: Verification Through Recreation

Extraction accuracy is validated by using the generated specification to recreate a test document, then comparing it visually and structurally to the original. This closes the loop and ensures specifications are not just theoretically correct but practically actionable.

**Why This Matters**: Specifications can be technically accurate but incomplete, omitting critical details that only become apparent during recreation. A color scheme might be extracted perfectly, but if table border rules are missing, the recreated document will differ visibly. Verification through recreation catches these gaps before specifications are used in production.

**In Practice**:
- Generate a test document using the AI_PROMPT.md instructions
- Compare side-by-side with the original using visual diff tools
- Check font rendering, color matching, spacing consistency, and layout alignment
- Validate that embedded assets (logos, images) are correctly positioned and sized
- Test with multiple content samples to ensure template generalizes beyond the original
- Document any discrepancies in TEMPLATE_SPEC.md implementation notes
- Iterate on specifications until recreation achieves >95% visual fidelity

## Workflow

### Phase 1: Document Analysis

**Objective**: Identify document type and unpack file structure to access underlying XML and assets.

**Actions**:
1. **Detect Document Type**
   - Check file extension: `.docx` (Word), `.pptx` (PowerPoint), `.xlsx` (Excel), `.pdf` (PDF)
   - Map to handler: DOCX Handler, PPTX Handler, XLSX Handler, PDF Handler
   - Verify file is valid Office Open XML format (DOCX/PPTX/XLSX are ZIP archives)

2. **Unpack Document Structure**
   - For DOCX/PPTX/XLSX: Extract ZIP contents to `unpacked/` directory
     ```bash
     unzip document.docx -d unpacked/
     ```
   - Key directories created:
     - `word/` (DOCX), `ppt/` (PPTX), or `xl/` (XLSX) - main content
     - `[type]/theme/` - theme colors and fonts
     - `[type]/media/` - embedded images and logos
     - `_rels/` - relationships and references
   - For PDF: Extract metadata and analyze text structure

3. **Identify Key Files**
   - **DOCX**: `word/document.xml`, `word/styles.xml`, `word/theme/theme1.xml`
   - **PPTX**: `ppt/presentation.xml`, `ppt/slideLayouts/`, `ppt/theme/theme1.xml`
   - **XLSX**: `xl/workbook.xml`, `xl/styles.xml`, `xl/theme/theme1.xml`
   - **PDF**: Metadata fields, font definitions, embedded color profiles

4. **Catalog Media Assets**
   - List all files in `word/media/`, `ppt/media/`, or `xl/media/`
   - Note filenames (e.g., `image1.png`, `logo.svg`) and formats
   - Record dimensions and file sizes for reference

**Output**: Unpacked directory structure with cataloged XML files and media assets

### Phase 2: Systematic Extraction

**Objective**: Parse XML files and extract all design elements using the comprehensive extraction checklist.

**Actions**:
1. **Extract Theme Data** (from `theme1.xml`)
   - **Colors**: Parse `<a:clrScheme>` for primary, secondary, accent colors
     - Convert `<a:srgbClr val="0078D4">` to `#0078D4`
     - Map semantic names: `dk1` (dark1), `lt1` (light1), `accent1-6`
   - **Fonts**: Parse `<a:fontScheme>` for major (headings) and minor (body) fonts
     - Extract `<a:majorFont><a:latin typeface="Calibri Light">`
     - Extract `<a:minorFont><a:latin typeface="Calibri">`

2. **Extract Style Definitions** (from `styles.xml`)
   - **Heading Styles**: For each heading level (H1-H6)
     - Font family: `<w:rFonts w:ascii="Calibri Light">`
     - Font size: `<w:sz w:val="32">` (32 half-points = 16pt)
     - Font weight: `<w:b/>` (bold) or absence (regular)
     - Color: `<w:color w:val="2E74B5">` = `#2E74B5`
     - Spacing: `<w:spacing w:before="0" w:after="200">` (200 twips = 10pt)
   - **Body Text Style**: Same extraction for Normal/paragraph style
   - **Special Styles**: Links, captions, footnotes, code blocks

3. **Extract Page Settings** (from `document.xml`)
   - **Page Size**: `<w:pgSz w:w="12240" w:h="15840">` (12240 twips = 8.5", 15840 twips = 11")
   - **Orientation**: `<w:pgSz w:orient="portrait">` or `landscape`
   - **Margins**: `<w:pgMar w:top="1440" w:right="1440" w:bottom="1440" w:left="1440">` (1440 twips = 1")
   - **Header/Footer Heights**: `w:header="720"` (720 twips = 0.5")

4. **Extract Structural Elements**
   - **Tables**: Border styles, cell padding, header formatting, alternating row colors
   - **Lists**: Bullet characters, numbering formats, indentation levels
   - **Dividers**: Line styles, colors, widths, spacing

5. **Apply Extraction Checklist** (see references/extraction-checklist.md)
   - Typography: All heading levels, body text, special text
   - Colors: Core palette, functional colors
   - Page Layout: Dimensions, orientation, margins, headers/footers
   - Structure: Section organization, content blocks
   - Tables: Structure, borders, content formatting
   - Lists: Bullet/numbered styles, indentation
   - Branding: Logo placement, brand colors
   - Special Elements: Callouts, dividers, code blocks

6. **Convert Units**
   - Half-points to points: divide by 2
   - Twips to points: divide by 20
   - EMUs to inches: divide by 914400
   - Points to pixels (96 DPI): multiply by 1.333

**Output**: JSON data structure with all extracted specifications (`extraction_results.json`)

### Phase 3: Asset Handling

**Objective**: Copy all embedded media files to an organized assets directory for reference and reuse.

**Actions**:
1. **Locate Media Files**
   - Scan `word/media/`, `ppt/media/`, `xl/media/` directories
   - Identify file types: `.png`, `.jpg`, `.svg`, `.emf`, `.wmf`

2. **Copy Assets**
   - Create `assets/` directory in output location
   - Copy all media files preserving filenames
   - Document original paths for reference

3. **Catalog Asset Usage**
   - For each asset, note:
     - Filename and format
     - Dimensions (extract from image metadata)
     - Usage context (logo in header, chart in section 3, etc.)
     - Positioning rules (left-aligned, centered, 0.5" margin)

4. **Generate Asset Reference**
   - Create `ASSETS.md` with table of all media files
   - Include thumbnails or descriptions
   - Document required placement and sizing

**Output**: `assets/` directory with all media files and `ASSETS.md` reference

### Phase 4: Output Generation

**Objective**: Generate both technical specification and AI replication prompt using the extracted data.

**Actions**:
1. **Generate TEMPLATE_SPEC.md** (Code-Level Specification)
   - Use template from `references/output-template.md` (Output 1 section)
   - Fill in extracted values:
     - Document Setup: Page size, orientation, margins
     - Typography System: Font stack, heading styles table, body text specs
     - Color System: Primary/neutral palettes with hex codes and usage
     - Structural Elements: Tables, lists with exact formatting rules
     - Branding Assets: Logo specifications and placement
     - Special Components: Callouts, dividers, code blocks
     - Implementation Notes: Edge cases, quirks, important details
   - Format as structured Markdown with tables and code blocks
   - Include measurement conversion reference

2. **Generate AI_PROMPT.md** (AI Replication Prompt)
   - Use template from `references/output-template.md` (Output 2 section)
   - Convert technical specs to imperative instructions:
     - "Create documents with these exact settings:"
     - "CRITICAL: Use these exact fonts and sizes."
     - "Use ONLY these colors:" (table with purpose, hex, usage)
     - "Follow this document structure:" (example template)
     - "When creating tables:" (specific rules)
     - "Quality Checklist" (validation steps)
     - "Common Mistakes to Avoid" (anti-patterns)
   - Emphasize precision with warnings and bold text
   - Include success criteria and quality gates

3. **Package Assets**
   - Ensure `assets/` directory is referenced in both outputs
   - Document how to use extracted media files
   - Provide file paths and placement instructions

4. **Create README**
   - Document extraction metadata (source file, date, tool version)
   - Provide usage instructions for both outputs
   - Include verification steps and known limitations

**Output**:
- `TEMPLATE_SPEC.md` (technical specification)
- `AI_PROMPT.md` (AI replication prompt)
- `ASSETS.md` (media reference)
- `README.md` (usage guide)

### Phase 5: Quality Verification

**Objective**: Validate extraction accuracy by recreating a test document and comparing to the original.

**Actions**:
1. **Generate Test Document**
   - Use AI_PROMPT.md to create a new document
   - Apply same content structure as original (headings, paragraphs, tables, lists)
   - Include all branding elements (logo, colors, formatting)

2. **Visual Comparison**
   - Open original and test documents side-by-side
   - Check font rendering: Do fonts, sizes, and weights match exactly?
   - Check colors: Are hex codes visually identical?
   - Check spacing: Do margins, line heights, and paragraph spacing match?
   - Check layout: Are headers, footers, and page structure identical?
   - Check assets: Are logos and images correctly positioned and sized?

3. **Structural Validation**
   - Unpack test document and compare XML structure
   - Verify style definitions match extracted specifications
   - Check theme colors and fonts are correctly applied
   - Validate table and list formatting rules

4. **Discrepancy Analysis**
   - Document any differences between original and recreation
   - Identify missing specifications or ambiguous instructions
   - Update TEMPLATE_SPEC.md and AI_PROMPT.md to address gaps
   - Add implementation notes for edge cases

5. **Iteration**
   - Repeat verification until >95% visual fidelity achieved
   - Test with multiple content samples to ensure generalization
   - Finalize specifications once validation passes

**Output**: Verified specifications with documented accuracy and known limitations

## File Type Handlers

### DOCX Handler

**Purpose**: Extract specifications from Microsoft Word documents (.docx)

**Key Files**:
- `word/document.xml`: Document content and section properties
- `word/styles.xml`: Style definitions (headings, body, tables, lists)
- `word/theme/theme1.xml`: Theme colors and fonts
- `word/media/`: Embedded images and logos

**Extraction Commands**:
```bash
# Unpack document
unzip document.docx -d unpacked/

# Extract theme colors
grep -A 3 "<a:clrScheme>" unpacked/word/theme/theme1.xml

# Extract heading styles
grep -A 10 "w:styleId=\"Heading1\"" unpacked/word/styles.xml

# List media assets
ls -lh unpacked/word/media/
```

**Key Conversions**:
- Font size: `<w:sz w:val="24">` = 24 half-points = 12pt
- Spacing: `<w:spacing w:after="200">` = 200 twips = 10pt
- Margins: `<w:pgMar w:top="1440">` = 1440 twips = 1 inch
- Colors: `<w:color w:val="1F4E78">` = #1F4E78

**Special Considerations**:
- Different styles for first page headers/footers
- Section breaks may have different page settings
- Linked styles (character + paragraph combined)
- Table styles may override document styles

### PPTX Handler

**Purpose**: Extract specifications from Microsoft PowerPoint presentations (.pptx)

**Key Files**:
- `ppt/presentation.xml`: Presentation-level settings
- `ppt/slideLayouts/`: Slide layout definitions
- `ppt/slideMasters/`: Master slide formatting
- `ppt/theme/theme1.xml`: Theme colors and fonts
- `ppt/media/`: Embedded images and graphics

**Extraction Commands**:
```bash
# Unpack presentation
unzip presentation.pptx -d unpacked/

# Extract theme colors
grep -A 3 "<a:clrScheme>" unpacked/ppt/theme/theme1.xml

# List slide layouts
ls -1 unpacked/ppt/slideLayouts/

# Extract master slide settings
cat unpacked/ppt/slideMasters/slideMaster1.xml
```

**Key Conversions**:
- Font size: Same as DOCX (half-points)
- Slide dimensions: `<p:sldSz cx="9144000" cy="6858000">` (EMUs)
  - 9144000 EMUs = 10 inches (standard width)
  - 6858000 EMUs = 7.5 inches (standard height)
- Positioning: All coordinates in EMUs

**Special Considerations**:
- Slide layouts override master formatting
- Placeholder positioning critical for consistency
- Animation settings not extracted (focus on static design)
- Speaker notes may have separate formatting

### XLSX Handler

**Purpose**: Extract specifications from Microsoft Excel spreadsheets (.xlsx)

**Key Files**:
- `xl/workbook.xml`: Workbook-level settings
- `xl/styles.xml`: Cell styles, fonts, colors, number formats
- `xl/theme/theme1.xml`: Theme colors and fonts
- `xl/media/`: Embedded charts and images

**Extraction Commands**:
```bash
# Unpack workbook
unzip workbook.xlsx -d unpacked/

# Extract theme colors
grep -A 3 "<a:clrScheme>" unpacked/xl/theme/theme1.xml

# Extract cell styles
grep -A 5 "<cellXfs>" unpacked/xl/styles.xml

# Extract fonts
grep -A 3 "<fonts>" unpacked/xl/styles.xml
```

**Key Conversions**:
- Font size: `<sz val="11">` = 11pt (direct, not half-points)
- Column width: `<col min="1" max="1" width="12.5">` (character units)
- Row height: `<row r="1" ht="15">` (points)
- Colors: Same RGB/hex format as DOCX/PPTX

**Special Considerations**:
- Conditional formatting rules affect cell styling
- Merged cells have special layout implications
- Print settings critical for page-based output
- Chart styles separate from cell styles

### PDF Handler

**Purpose**: Extract specifications from PDF documents (limited extraction)

**Key Limitations**:
- PDFs are rendered output, not source documents
- No XML structure to parse (unless PDF/A with XMP metadata)
- Font and color extraction requires specialized tools
- Layout analysis is heuristic, not definitive

**Extraction Approach**:
```bash
# Extract metadata
pdfinfo document.pdf

# Extract fonts
pdffonts document.pdf

# Extract text with layout
pdftotext -layout document.pdf

# Extract images
pdfimages document.pdf extracted_images/
```

**Extraction Strategy**:
1. Use `pdffonts` to identify font families used
2. Use `pdftotext -layout` to analyze spacing and structure
3. Use color sampling tools to estimate palette
4. Manual verification required for accuracy
5. Recommend converting to DOCX if source unavailable

**Special Considerations**:
- Font embedding may hide actual font names
- Colors may be in CMYK rather than RGB
- Layout reconstruction is approximate
- Best used as reference, not source of truth

## Extraction Checklist

Use this comprehensive checklist to ensure no design element is missed. Check off each item as extracted.

### Typography

#### Headings
- [ ] **H1**: Font family, size (pt), weight, color (hex), case (title/upper/sentence)
- [ ] **H2**: Font family, size (pt), weight, color (hex), case
- [ ] **H3**: Font family, size (pt), weight, color (hex), case
- [ ] **H4+**: Font family, size (pt), weight, color (hex), case (if present)
- [ ] **Heading spacing**: Space before (pt), space after (pt)

#### Body Text
- [ ] **Primary body**: Font family, size (pt), weight, color (hex)
- [ ] **Line height**: Exact value or multiplier (e.g., 1.5 or 18pt)
- [ ] **Paragraph spacing**: Space after paragraphs (pt)
- [ ] **First line indent**: Yes/no, amount if yes

#### Special Text
- [ ] **Emphasized text**: Bold weight, italic style
- [ ] **Links**: Color (hex), underline style
- [ ] **Captions**: Font, size, color, alignment
- [ ] **Footnotes**: Font, size, placement

### Colors

#### Core Palette
- [ ] **Primary color**: Hex code, RGB, usage (headings, accents, etc.)
- [ ] **Secondary color**: Hex code, RGB, usage
- [ ] **Accent color(s)**: Hex codes, RGB, usage contexts
- [ ] **Background**: Hex code (usually #FFFFFF)
- [ ] **Body text**: Hex code (usually #000000 or dark gray)

#### Functional Colors
- [ ] **Border/line color**: Hex code, RGB
- [ ] **Table header background**: Hex code, RGB
- [ ] **Table alternating rows**: Hex code, RGB (if applicable)
- [ ] **Highlight/callout background**: Hex code, RGB

### Page Layout

#### Dimensions
- [ ] **Page size**: Letter (8.5x11"), A4, or custom dimensions
- [ ] **Orientation**: Portrait or landscape
- [ ] **Margins**: Top, bottom, left, right (inches or cm)

#### Headers & Footers
- [ ] **Header content**: Text, logo, page numbers
- [ ] **Header height**: Distance from top (inches)
- [ ] **Footer content**: Text, page numbers, date
- [ ] **Footer height**: Distance from bottom (inches)
- [ ] **Different first page**: Yes/no

### Structure

#### Section Organization
- [ ] **Number of main sections**: Typical structure
- [ ] **Section dividers**: Lines, spacing, page breaks
- [ ] **Numbering scheme**: 1.0, 1.1, 1.1.1 or I, A, 1, a

#### Content Blocks
- [ ] **Introduction/overview placement**
- [ ] **Conclusion/summary placement**
- [ ] **Sidebar/callout box styling**

### Tables

#### Structure
- [ ] **Header row**: Background color, text color, font weight
- [ ] **Border style**: Solid, none, partial (which sides)
- [ ] **Border color**: Hex code
- [ ] **Border width**: Pixels or points
- [ ] **Cell padding**: Top, right, bottom, left

#### Content
- [ ] **Header text**: Font, size, alignment
- [ ] **Cell text**: Font, size, alignment
- [ ] **Alternating row colors**: Yes/no, colors if yes

### Lists

#### Bullet Lists
- [ ] **Bullet style**: Disc, circle, square, custom character
- [ ] **Bullet color**: Same as text or different hex code
- [ ] **Indentation**: First level, nested levels
- [ ] **Spacing**: Between items (pt)

#### Numbered Lists
- [ ] **Number style**: 1, a, i, roman numerals
- [ ] **Number formatting**: Period, parenthesis, none
- [ ] **Indentation**: First level, nested levels

### Branding Elements

#### Logo
- [ ] **Filename and format extracted**: e.g., logo.png, logo.svg
- [ ] **Dimensions**: Width x height (px or inches)
- [ ] **Position**: Page location (header, title page, footer, etc.)
- [ ] **Margins**: Space around logo (inches)
- [ ] **Placement on**: Every page, first page only, specific pages

#### Brand Colors
- [ ] **Match to palette**: Ensure brand colors documented in color system
- [ ] **Specific usage rules**: Logo colors vs accent colors vs functional colors

### Special Elements

#### Callout/Info Boxes
- [ ] **Background color**: Hex code
- [ ] **Border**: Style (solid/dashed), color (hex), width (px), radius (px)
- [ ] **Padding**: Internal spacing (pt)
- [ ] **Icon**: Type, color, position (if applicable)

#### Dividers/Lines
- [ ] **Style**: Solid, dashed, dotted
- [ ] **Color**: Hex code
- [ ] **Width**: Points or pixels
- [ ] **Spacing**: Above and below (pt)

#### Code/Technical Blocks (if applicable)
- [ ] **Font family**: Monospace choice (e.g., Consolas, Courier New)
- [ ] **Background color**: Hex code
- [ ] **Border styling**: Style, color, width
- [ ] **Syntax highlighting scheme**: Colors for keywords, strings, comments

### Document Metadata

- [ ] **Document title styling**: Font, size, color, position
- [ ] **Author/date placement and styling**
- [ ] **Version/revision styling**
- [ ] **Confidentiality markings**: If present, font, color, position

### Measurement Conversion Reference

```
OOXML half-points to points: divide by 2
  Example: <w:sz w:val="24"/> = 12pt

OOXML twips to points: divide by 20
  Example: <w:spacing w:after="200"/> = 10pt

OOXML EMUs to inches: divide by 914400
  Example: 914400 EMUs = 1 inch

Points to pixels (at 96 DPI): multiply by 1.333
  Example: 12pt = 16px
```

## Common Anti-Patterns

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| **Visual Estimation** | Guessing colors/fonts from appearance leads to inaccuracy. "That looks like 14pt Arial" may actually be 13pt Calibri, causing subtle but compounding inconsistency. | Always extract from XML source files. Use `styles.xml` for fonts, `theme1.xml` for colors. Convert OOXML units precisely. |
| **Skipping Verification** | Generated templates may drift from original due to missing specifications or ambiguous instructions. Without testing, errors only surface in production. | Always verify by recreation and visual comparison. Generate test document using AI_PROMPT.md, compare side-by-side, iterate until >95% fidelity. |
| **Missing Assets** | Forgetting to extract logos/images breaks branding and layout. Even if specifications are perfect, missing media ruins output. | Check `word/media/`, `ppt/media/`, `xl/media/` directories in all unpacked documents. Copy all files to `assets/` and document in ASSETS.md. |
| **Unit Conversion Errors** | OOXML uses half-points, twips, and EMUs. Forgetting conversions leads to 2x font sizes, incorrect margins. | Use conversion formulas: half-points ÷ 2, twips ÷ 20, EMUs ÷ 914400. Validate converted values against visual inspection. |
| **Ignoring Edge Cases** | First page headers, section breaks, and linked styles have special behavior. Assuming uniform formatting causes inconsistency. | Document all variations in TEMPLATE_SPEC.md implementation notes. Test recreation with multi-page, multi-section documents. |
| **Incomplete Color Extraction** | Extracting only theme colors misses table borders, callout backgrounds, and special element styling. | Use extraction checklist to systematically capture core palette AND functional colors. Check every visual element. |
| **Approximating Measurements** | Rounding margins to "about 1 inch" or spacing to "roughly 10pt" compounds across pages. | Extract and document exact values. Use original OOXML values, not rounded approximations. |
| **Single-Sample Testing** | Verifying with only the original content hides template generalization issues. New content may break layout. | Test recreation with multiple content samples: different lengths, varied structure, additional tables/lists. Ensure template generalizes. |
| **Forgetting Fallback Fonts** | Primary font may not be available on all systems. No fallback causes browser/OS substitution, ruining design. | Document font stack with fallbacks: "Calibri, Arial, Helvetica, sans-serif". Test on systems without primary font. |
| **Mixing RGB and Hex** | Inconsistent color notation causes confusion. Hex in some places, RGB in others leads to translation errors. | Standardize on hex for all color specifications. Include RGB as reference in tables, but use hex as primary. |

## Automation Script

The `scripts/extract_template.py` Python helper automates the extraction workflow for Office documents:

**Usage**:
```bash
python scripts/extract_template.py <document_path> <output_dir>

# Example
python scripts/extract_template.py company_report.docx ./extracted_template
```

**What It Does**:
1. Detects document type (DOCX/PPTX/XLSX)
2. Unpacks ZIP structure to `output_dir/unpacked/`
3. Extracts theme colors from `theme1.xml`
4. Extracts theme fonts (major/minor)
5. Extracts style definitions from `styles.xml` (DOCX)
6. Extracts page settings from `document.xml` (DOCX)
7. Copies media assets to `output_dir/assets/`
8. Generates `extraction_results.json` with all extracted data
9. Prints summary with key findings

**Output Structure**:
```
extracted_template/
├── unpacked/              # Full ZIP contents
├── assets/                # Copied media files
├── extraction_results.json   # Raw extraction data
└── [manual step: create TEMPLATE_SPEC.md and AI_PROMPT.md]
```

**Next Steps After Script**:
1. Review `extraction_results.json` for raw data
2. Inspect `unpacked/` directory for detailed XML
3. Check `assets/` for logos and images
4. Use extraction data to complete `TEMPLATE_SPEC.md` using Output 1 template
5. Generate `AI_PROMPT.md` using Output 2 template
6. Run Phase 5 verification

**Limitations**:
- Does not generate final Markdown outputs (manual step required)
- PDF support limited to metadata extraction
- Complex table styles may need manual review
- Conditional formatting (Excel) not fully captured

## Conclusion

Template Extractor transforms document reverse-engineering from a manual, error-prone guessing process into a systematic, verifiable workflow. By unpacking file structures and parsing XML directly, it provides ground-truth specifications that enable pixel-perfect recreation without iteration cycles.

The dual-output approach (technical specification + AI prompt) ensures both developers and AI systems have actionable, precise instructions tailored to their needs. The verification phase closes the loop, validating that specifications are not just theoretically correct but practically usable.

This skill is essential for teams needing document consistency across multiple files, for migrating formatting between systems, and for creating reusable branded document generators. By eliminating guesswork and manual measurement, it accelerates document production while guaranteeing visual fidelity.

Use this skill whenever precision matters more than approximation - when "close enough" is not acceptable and exact replication is required.

## Related Skills

- **doc-generator**: Generates documents from scratch using specifications (complementary - uses Template Extractor output)
- **pptx-generation**: Creates PowerPoint presentations programmatically (complementary - uses Template Extractor output)
- **documentation**: Generates technical documentation with consistent formatting (uses templates from Template Extractor)
- **code-review-assistant**: May reference document style guides extracted by Template Extractor

## MCP Requirements

```yaml
mcp_servers:
  required: []
  optional: [memory-mcp]
  auto_enable: false
```

**Optional MCP Usage**:
- **memory-mcp**: Can store extracted templates for reuse across sessions
  - Namespace: `templates/{document_type}/{organization}`
  - Tags: `who: template-extractor, project: document-templates, intent: specification`
  - Enables template library building and organizational style guide management