# Output Template Formats

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



Use these templates to structure the two required outputs.

## Output 1: Code-Level Template Specification

```markdown
# [Document Type] Template Specification
Generated from: [original filename]
Extraction date: [date]

## Document Setup

### Page Configuration
- **Page size**: [Letter 8.5" x 11" / A4 / Custom]
- **Orientation**: [Portrait / Landscape]
- **Margins**: Top [X]", Right [X]", Bottom [X]", Left [X]"

### Header Configuration
- **Height**: [X]" from top
- **Content**: [Description of header elements]
- **First page different**: [Yes/No]

### Footer Configuration
- **Height**: [X]" from bottom
- **Content**: [Description, e.g., "Page X of Y, centered"]

---

## Typography System

### Font Stack
```
Primary (Headings): [Font Name], [Fallback 1], [Fallback 2], sans-serif
Secondary (Body): [Font Name], [Fallback 1], [Fallback 2], serif
Monospace (Code): [Font Name], monospace
```

### Heading Styles

| Level | Font | Size | Weight | Color | Case | Space Before | Space After |
|-------|------|------|--------|-------|------|--------------|-------------|
| H1 | [Font] | [X]pt | [Weight] | [#HEX] | [Case] | [X]pt | [X]pt |
| H2 | [Font] | [X]pt | [Weight] | [#HEX] | [Case] | [X]pt | [X]pt |
| H3 | [Font] | [X]pt | [Weight] | [#HEX] | [Case] | [X]pt | [X]pt |

### Body Text
- **Font**: [Font Name]
- **Size**: [X]pt
- **Weight**: [Regular/400]
- **Color**: [#HEX]
- **Line height**: [X] or [X]pt
- **Paragraph spacing**: [X]pt after

---

## Color System

### Primary Palette
| Name | Hex | RGB | Usage |
|------|-----|-----|-------|
| Primary | #[XXXXXX] | rgb(X,X,X) | [Headings, primary accents] |
| Secondary | #[XXXXXX] | rgb(X,X,X) | [Secondary elements] |
| Accent | #[XXXXXX] | rgb(X,X,X) | [Highlights, CTAs] |

### Neutral Palette
| Name | Hex | Usage |
|------|-----|-------|
| Text Primary | #[XXXXXX] | Body text |
| Text Secondary | #[XXXXXX] | Captions, secondary text |
| Background | #[XXXXXX] | Page background |
| Border | #[XXXXXX] | Lines, table borders |

---

## Structural Elements

### Tables
```
Header Row:
  - Background: #[XXXXXX]
  - Text: #[XXXXXX], [Font], [X]pt, [Weight]
  - Alignment: [Left/Center]

Body Rows:
  - Background: #[XXXXXX] (alternating: #[XXXXXX])
  - Text: #[XXXXXX], [Font], [X]pt
  - Alignment: [Left/Center]

Borders:
  - Style: [solid/none]
  - Color: #[XXXXXX]
  - Width: [X]px
  - Applied to: [all/horizontal only/header bottom only]

Cell Padding: [X]pt
```

### Lists
```
Bullet Lists:
  - Style: [disc/circle/square/custom]
  - Color: [#HEX or "inherit"]
  - Indent: [X]pt per level
  - Item spacing: [X]pt

Numbered Lists:
  - Format: [1. / 1) / a. / i.]
  - Indent: [X]pt per level
  - Item spacing: [X]pt
```

---

## Branding Assets

### Logo
- **File**: [filename.png/svg]
- **Dimensions**: [W]" x [H]" ([W]px x [H]px at 96 DPI)
- **Position**: [Header left / Title page center / etc.]
- **Margin**: [X]" from edges
- **Pages**: [All pages / First page only / Title page only]

---

## Special Components

### Callout/Info Box
```
Background: #[XXXXXX]
Border: [X]px [solid/dashed] #[XXXXXX]
Border radius: [X]px
Padding: [X]pt
Text: [Font], [X]pt, #[XXXXXX]
```

### Horizontal Divider
```
Style: [solid/dashed/dotted]
Color: #[XXXXXX]
Width: [X]px
Margin: [X]pt above, [X]pt below
```

---

## Implementation Notes

[Any specific quirks, exceptions, or important details about recreating this template]
```

---

## Output 2: AI Replication Prompt

```markdown
# [Document Type] Document Generator

You are a document formatting expert. Your task is to create [document type] files that EXACTLY match the following specification. Precision is critical—every font, color, and spacing value must match exactly.

## Document Configuration

Create documents with these exact settings:
- Page size: [size]
- Orientation: [orientation]
- Margins: [specific values]

## Typography Rules

**CRITICAL: Use these exact fonts and sizes.**

### Headings
- **Title/H1**: [Font] [Size]pt [Weight] in [#HEX]
  - Space before: [X]pt, Space after: [X]pt
  - Case: [UPPERCASE / Title Case / Sentence case]

- **H2**: [Font] [Size]pt [Weight] in [#HEX]
  - Space before: [X]pt, Space after: [X]pt

- **H3**: [Font] [Size]pt [Weight] in [#HEX]
  - Space before: [X]pt, Space after: [X]pt

### Body Text
- Font: [Font] [Size]pt [Weight]
- Color: [#HEX]
- Line height: [value]
- Paragraph spacing: [X]pt after each paragraph

## Color Palette

**Use ONLY these colors:**

| Purpose | Hex Code | When to Use |
|---------|----------|-------------|
| Primary | [#HEX] | [Usage description] |
| Secondary | [#HEX] | [Usage description] |
| Accent | [#HEX] | [Usage description] |
| Body text | [#HEX] | All body copy |
| Background | [#HEX] | Page background |
| Borders | [#HEX] | Table borders, dividers |

## Structure Template

Follow this document structure:

```
[Header with logo positioned at X]

[TITLE - H1 style]

[Introduction paragraph - body style]

[SECTION HEADING - H2 style]
[Content...]

[SUBSECTION - H3 style]
[Content...]

[Footer with page numbers]
```

## Table Formatting

When creating tables:
- Header row: Background [#HEX], text [#HEX] [Font] [Size]pt [Weight]
- Body rows: Background [#HEX], text [#HEX]
- Borders: [X]px [style] [#HEX] on [which sides]
- Cell padding: [X]pt

## List Formatting

Bullet lists:
- Use [bullet style] bullets
- Indent [X]pt per level
- [X]pt spacing between items

Numbered lists:
- Format: [style]
- Indent [X]pt per level

## Branding Requirements

[Logo instructions if applicable]:
- Place [logo filename] in [position]
- Size: [dimensions]
- Maintain [X]" margin around logo

## Quality Checklist

Before finalizing, verify:
- [ ] All fonts match specification exactly
- [ ] All colors use exact hex values (not "close enough")
- [ ] Heading hierarchy is correct (H1 > H2 > H3)
- [ ] Spacing matches specification
- [ ] Tables follow formatting rules
- [ ] Logo (if applicable) is correctly positioned
- [ ] Headers/footers match specification
- [ ] Page margins are exact

## Common Mistakes to Avoid

1. Do NOT substitute similar fonts—use exact font names
2. Do NOT approximate colors—use exact hex codes
3. Do NOT guess at spacing—use specified values
4. Do NOT add decorative elements not in the specification
5. Do NOT change the heading hierarchy

---

When asked to create a document using this template, produce a [.docx/.pptx/etc.] file that a human reviewer could not distinguish from the original template.
```

---

## Packaging Instructions

Save outputs as:
1. `TEMPLATE_SPEC.md` - The code-level specification
2. `AI_PROMPT.md` - The replication prompt
3. Copy any extracted assets to `assets/` folder
4. Optionally generate a test document to verify accuracy


---
*Promise: `<promise>OUTPUT_TEMPLATE_VERIX_COMPLIANT</promise>`*
