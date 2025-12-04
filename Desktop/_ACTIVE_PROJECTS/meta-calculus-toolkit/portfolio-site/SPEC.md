# Meta-Calculus Portfolio Website Specification

## Overview

An engaging, narrative-driven portfolio website documenting the meta-calculus research journey - from initial theoretical exploration through AI-assisted over-promising to rigorous computational validation. The site serves as both a technical showcase and an honest documentation of the research process.

## Requirements

### Functional Requirements

1. **Multi-Page Narrative Structure**
   - Landing page with project overview and visual hook
   - "The Punch" - Initial exploration and theoretical framework
   - "AI Psychosis" - Honest documentation of over-promising and course correction
   - "Rigorous Validation" - Simulation-based verification with interactive demos
   - "Results" - Optimization findings and Pareto frontiers
   - "Code & Methods" - Technical implementation details

2. **Interactive Demonstrations**
   - Run meta-calculus calculations in-browser (Pyodide/WebAssembly)
   - Visualize Pareto frontiers from optimization results
   - Parameter exploration widgets for physics simulations
   - Code snippets with syntax highlighting

3. **Visual Elements**
   - Mathematical equations (LaTeX/KaTeX rendering)
   - Data visualizations (charts, 3D plots)
   - Code blocks with copy functionality
   - Responsive images and diagrams

4. **Technical Showcase**
   - Embedded code samples from actual codebase
   - API integration examples (pymoo, Global MOO)
   - Architecture diagrams
   - Results data visualization

### Non-Functional Requirements

- **Performance**: First contentful paint < 1.5s
- **Accessibility**: WCAG 2.1 AA compliance
- **Responsive**: Mobile-first design, works on all devices
- **SEO**: Meta tags, Open Graph, structured data

## Constraints

### Technical
- Framework: Next.js 14 (App Router) for SSR/SSG
- Styling: Tailwind CSS for rapid development
- Hosting: Railway (free tier compatible)
- Python demos: Pyodide for in-browser execution
- Charts: Recharts or D3.js
- Math: KaTeX for equation rendering

### Security
- Global MOO API key in environment variable (GLOBALMOO_API_KEY)
- No secrets in client-side code
- Private GitHub repository

### Timeline
- MVP: Core pages with static content
- V1: Interactive demos working
- V2: Full polish and deployment

## Page Structure

### 1. Landing Page (/)
- Hero section with compelling visual
- One-sentence hook about meta-calculus
- Navigation to story sections
- Quick stats/results teaser

### 2. The Punch (/exploration)
- Initial theoretical framework
- "The geometry is real; the calculus is a lens"
- Core equations with explanations
- What problem we're solving

### 3. AI Psychosis (/ai-journey)
- Honest documentation of AI assistance
- Over-promising moments and corrections
- What we learned about AI limitations
- The value of rigorous validation

### 4. Rigorous Validation (/validation)
- Simulation methodology
- Interactive parameter explorer
- Multi-calculus diffusion demos
- Scheme-robustness visualizations

### 5. Results (/results)
- Pareto frontier visualizations
- Optimal configurations found
- pymoo vs Global MOO comparison
- Key findings summary

### 6. Code & Methods (/code)
- Architecture overview
- Key code snippets
- How to use the library
- Links to documentation

## Success Criteria

1. Tells a compelling story that engages both physicists and developers
2. Demonstrates technical competence through working demos
3. Shows intellectual honesty about AI limitations
4. Deploys successfully on Railway
5. Loads fast and works on mobile
6. Code samples are accurate and runnable

## Out of Scope

- User authentication/accounts
- Database backend
- Real-time collaboration
- Payment processing
- Full documentation site (separate project)
