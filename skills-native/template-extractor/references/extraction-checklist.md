# Extraction Checklist

Systematically extract every element below. Missing any item results in imperfect template recreation.

## Typography

### Headings
- [ ] H1: Font family, size (pt), weight, color, case (title/upper/sentence)
- [ ] H2: Font family, size (pt), weight, color, case
- [ ] H3: Font family, size (pt), weight, color, case
- [ ] H4+: Font family, size (pt), weight, color, case
- [ ] Heading spacing: Space before (pt), space after (pt)

### Body Text
- [ ] Primary body: Font family, size (pt), weight, color
- [ ] Line height: Exact value or multiplier (e.g., 1.5 or 18pt)
- [ ] Paragraph spacing: Space after paragraphs (pt)
- [ ] First line indent: Yes/no, amount if yes

### Special Text
- [ ] Emphasized text: Bold weight, italic style
- [ ] Links: Color, underline style
- [ ] Captions: Font, size, color, alignment
- [ ] Footnotes: Font, size, placement

## Colors

### Core Palette
- [ ] Primary color: Hex code, usage (headings, accents, etc.)
- [ ] Secondary color: Hex code, usage
- [ ] Accent color(s): Hex codes, usage contexts
- [ ] Background: Hex code (usually #FFFFFF)
- [ ] Body text: Hex code (usually #000000 or dark gray)

### Functional Colors
- [ ] Border/line color: Hex code
- [ ] Table header background: Hex code
- [ ] Table alternating rows: Hex code (if applicable)
- [ ] Highlight/callout background: Hex code

## Page Layout

### Dimensions
- [ ] Page size: Letter (8.5x11"), A4, or custom
- [ ] Orientation: Portrait or landscape
- [ ] Margins: Top, bottom, left, right (inches or cm)

### Headers & Footers
- [ ] Header content: Text, logo, page numbers
- [ ] Header height: Distance from top
- [ ] Footer content: Text, page numbers, date
- [ ] Footer height: Distance from bottom
- [ ] Different first page: Yes/no

## Structure

### Section Organization
- [ ] Number of main sections typical
- [ ] Section dividers: Lines, spacing, page breaks
- [ ] Numbering scheme: 1.0, 1.1, 1.1.1 or I, A, 1, a

### Content Blocks
- [ ] Introduction/overview placement
- [ ] Conclusion/summary placement
- [ ] Sidebar/callout box styling

## Tables

### Structure
- [ ] Header row: Background color, text color, font weight
- [ ] Border style: Solid, none, partial (which sides)
- [ ] Border color: Hex code
- [ ] Border width: Pixels or points
- [ ] Cell padding: Top, right, bottom, left

### Content
- [ ] Header text: Font, size, alignment
- [ ] Cell text: Font, size, alignment
- [ ] Alternating row colors: Yes/no, colors if yes

## Lists

### Bullet Lists
- [ ] Bullet style: Disc, circle, square, custom character
- [ ] Bullet color: Same as text or different
- [ ] Indentation: First level, nested levels
- [ ] Spacing: Between items

### Numbered Lists
- [ ] Number style: 1, a, i, roman numerals
- [ ] Number formatting: Period, parenthesis, none
- [ ] Indentation: First level, nested levels

## Branding Elements

### Logo
- [ ] Filename and format extracted
- [ ] Dimensions: Width x height (px or inches)
- [ ] Position: Page location (header, title page, etc.)
- [ ] Margins: Space around logo
- [ ] Placement on: Every page, first page only, specific pages

### Brand Colors
- [ ] Match to palette above
- [ ] Specific usage rules (logo colors vs accent colors)

## Special Elements

### Callout/Info Boxes
- [ ] Background color
- [ ] Border: Style, color, width, radius
- [ ] Padding: Internal spacing
- [ ] Icon: Type, color, position (if applicable)

### Dividers/Lines
- [ ] Style: Solid, dashed, dotted
- [ ] Color: Hex code
- [ ] Width: Points or pixels
- [ ] Spacing: Above and below

### Code/Technical Blocks (if applicable)
- [ ] Font family: Monospace choice
- [ ] Background color
- [ ] Border styling
- [ ] Syntax highlighting scheme

## Document Metadata

- [ ] Document title styling
- [ ] Author/date placement and styling
- [ ] Version/revision styling
- [ ] Confidentiality markings (if present)

## Measurement Conversion Reference

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
