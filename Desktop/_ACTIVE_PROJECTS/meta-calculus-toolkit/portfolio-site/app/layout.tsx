import type { Metadata } from 'next';
import { Inter, JetBrains_Mono } from 'next/font/google';
import './globals.css';
import Navigation from '@/components/Navigation';

const inter = Inter({
  subsets: ['latin'],
  variable: '--font-inter',
  display: 'swap',
});

const jetbrainsMono = JetBrains_Mono({
  subsets: ['latin'],
  variable: '--font-jetbrains-mono',
  display: 'swap',
});

export const metadata: Metadata = {
  title: 'Meta-Calculus Toolkit | AI-Driven Mathematical Discovery',
  description: 'A 30-day journey exploring foundational mathematics through autonomous AI agents, validation frameworks, and computational experiments.',
  keywords: ['meta-calculus', 'AI', 'mathematics', 'autonomous agents', 'mathematical discovery'],
  authors: [{ name: 'Meta-Calculus Research' }],
  openGraph: {
    title: 'Meta-Calculus Toolkit',
    description: 'AI-Driven Mathematical Discovery Journey',
    type: 'website',
  },
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" className={`${inter.variable} ${jetbrainsMono.variable}`}>
      <body className="min-h-screen bg-dark-bg text-dark-text antialiased">
        <div className="relative flex min-h-screen flex-col">
          {/* Background gradient */}
          <div className="fixed inset-0 -z-10 overflow-hidden">
            <div className="absolute -top-1/2 left-1/4 h-96 w-96 rounded-full bg-primary-600/20 blur-3xl" />
            <div className="absolute top-1/3 right-1/4 h-96 w-96 rounded-full bg-accent-600/20 blur-3xl" />
          </div>

          <Navigation />

          <main className="flex-1">
            {children}
          </main>

          <footer className="border-t border-dark-border py-8">
            <div className="section">
              <div className="flex flex-col items-center justify-between gap-4 md:flex-row">
                <p className="text-sm text-gray-400">
                  Meta-Calculus Toolkit - A 30-Day AI Research Journey
                </p>
                <div className="flex gap-6 text-sm text-gray-400">
                  <a
                    href="https://github.com/your-repo"
                    target="_blank"
                    rel="noopener noreferrer"
                    className="link"
                  >
                    GitHub
                  </a>
                  <a href="/code" className="link">
                    Source Code
                  </a>
                  <a href="/results" className="link">
                    Results
                  </a>
                </div>
              </div>
            </div>
          </footer>
        </div>
      </body>
    </html>
  );
}
