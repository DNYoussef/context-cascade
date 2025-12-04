# Meta-Calculus Portfolio Site

A Next.js 14 portfolio website documenting a 30-day journey exploring meta-calculus concepts using autonomous AI agents powered by GlobalMoo.

## Features

- **Modern Stack**: Next.js 14 with App Router, TypeScript, and Tailwind CSS
- **Mathematical Rendering**: KaTeX for beautiful equation display
- **Code Highlighting**: Prism for syntax-highlighted code blocks
- **Responsive Design**: Mobile-first physics/science themed aesthetic
- **Secure API**: Server-side GlobalMoo API integration (API key never exposed to client)
- **Railway Ready**: Configured for one-click deployment to Railway

## Project Structure

```
portfolio-site/
├── app/                      # Next.js 14 App Router
│   ├── api/                  # Server-side API routes
│   │   ├── agents/           # GlobalMoo agent orchestration
│   │   └── health/           # Health check endpoint
│   ├── exploration/          # Week 1: Exploration page
│   ├── ai-journey/           # Weeks 2-3: AI Journey page
│   ├── validation/           # Week 4: Validation page
│   ├── results/              # Final results page
│   ├── code/                 # Source code showcase
│   ├── layout.tsx            # Root layout with navigation
│   ├── page.tsx              # Landing page
│   └── globals.css           # Global styles
├── components/               # Reusable React components
│   ├── Navigation.tsx        # Site navigation
│   ├── CodeBlock.tsx         # Syntax-highlighted code
│   └── MathBlock.tsx         # KaTeX equation rendering
├── lib/                      # Utility libraries
│   └── api-client.ts         # Client-side API wrapper
├── public/                   # Static assets
├── next.config.js            # Next.js configuration
├── tailwind.config.js        # Tailwind CSS theme
├── tsconfig.json             # TypeScript configuration
├── railway.json              # Railway deployment config
└── package.json              # Dependencies
```

## Getting Started

### Prerequisites

- Node.js 18+ and npm
- GlobalMoo API key (for AI agent features)

### Installation

1. Clone the repository:
```bash
cd C:\Users\17175\Desktop\_ACTIVE_PROJECTS\meta-calculus-toolkit\portfolio-site
```

2. Install dependencies:
```bash
npm install
```

3. Create environment file:
```bash
cp .env.local.example .env.local
```

4. Add your GlobalMoo API key to `.env.local`:
```
GLOBALMOO_API_KEY=your_actual_api_key_here
```

5. Run development server:
```bash
npm run dev
```

6. Open [http://localhost:3000](http://localhost:3000)

## Environment Variables

### Server-Side Only (Secure)

- `GLOBALMOO_API_KEY`: GlobalMoo API key - **NEVER exposed to client**

### Public (Client-Accessible)

- `NEXT_PUBLIC_SITE_URL`: Site URL for metadata
- `NEXT_PUBLIC_SITE_NAME`: Site name for branding

## Security

The GlobalMoo API key is **ONLY accessible server-side** through:

1. API routes in `app/api/` directory
2. Server components (not client components)
3. Environment variable `process.env.GLOBALMOO_API_KEY`

**Client components CANNOT access the API key directly.** All agent orchestration happens through the `/api/agents` endpoint.

## Deployment

### Railway (Recommended)

1. Install Railway CLI:
```bash
npm install -g @railway/cli
```

2. Login to Railway:
```bash
railway login
```

3. Create new project:
```bash
railway init
```

4. Add environment variable in Railway dashboard:
   - `GLOBALMOO_API_KEY`: Your GlobalMoo API key

5. Deploy:
```bash
railway up
```

Railway will automatically detect `railway.json` and configure the deployment.

### Manual Build

```bash
npm run build
npm start
```

## Technology Stack

- **Framework**: Next.js 14 (App Router)
- **Language**: TypeScript
- **Styling**: Tailwind CSS
- **Math Rendering**: KaTeX via `react-katex`
- **Code Highlighting**: Prism via `prism-react-renderer`
- **Charts**: Recharts
- **Content**: MDX support for rich documentation
- **Fonts**: Inter (sans), JetBrains Mono (code)

## Development

### Adding New Pages

Create new route folders in `app/`:

```tsx
// app/new-page/page.tsx
export default function NewPage() {
  return <div>New Page Content</div>;
}
```

### Using Components

```tsx
import CodeBlock from '@/components/CodeBlock';
import MathBlock from '@/components/MathBlock';

// Math equation
<MathBlock equation="E = mc^2" displayMode={true} />

// Code block
<CodeBlock language="python" code="print('Hello')" />
```

### Calling AI Agents

```tsx
'use client';

import { triggerAgent } from '@/lib/api-client';

async function runExperiment() {
  const result = await triggerAgent({
    agentType: 'researcher',
    task: 'Analyze commutativity of meta-derivatives',
    parameters: { depth: 3 }
  });

  console.log(result);
}
```

## Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm start` - Start production server
- `npm run lint` - Run ESLint

## License

MIT License - See LICENSE file for details

## Contributing

This is a research project documenting a 30-day AI exploration journey. Contributions and feedback are welcome!

## Support

For questions or issues:
- Open an issue on GitHub
- Email: your-email@example.com
- GlobalMoo Documentation: https://docs.globalmoo.com
