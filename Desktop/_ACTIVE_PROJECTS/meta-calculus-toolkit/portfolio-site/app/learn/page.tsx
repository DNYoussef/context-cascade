import Link from 'next/link';

export const metadata = {
  title: 'Learn | Meta-Calculus',
  description: 'Educational resources, textbook, proofs, and lessons learned.',
};

export default function LearnPage() {
  return (
    <div className="section">
      <div className="mx-auto max-w-4xl">
        <div className="animate-fade-in">
          <p className="text-primary-400 font-mono text-sm mb-2">Educational Resources</p>
          <h1 className="text-4xl font-bold mb-4">
            <span className="gradient-text">Learn</span>
          </h1>
          <p className="text-xl text-gray-300 mb-8">
            Comprehensive textbook, rigorous proofs, and documented lessons from failures
          </p>
        </div>

        {/* Resource Cards */}
        <div className="space-y-6 mb-12">
          <Link href="/learn/textbook" className="card hover:border-primary-500 transition-colors group block">
            <div className="flex items-start justify-between">
              <div>
                <div className="flex items-center mb-2">
                  <svg className="w-6 h-6 text-primary-400 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" />
                  </svg>
                  <h2 className="text-xl font-bold group-hover:text-primary-400 transition-colors">Complete Textbook</h2>
                </div>
                <p className="text-gray-400 text-sm mb-3">
                  9 chapters covering foundations, meta-calculus framework, physics applications, validation, and use cases. Includes downloadable markdown.
                </p>
                <div className="flex flex-wrap gap-2">
                  <span className="text-xs bg-primary-900/50 text-primary-400 px-2 py-1 rounded">900+ lines</span>
                  <span className="text-xs bg-primary-900/50 text-primary-400 px-2 py-1 rounded">Full proofs</span>
                  <span className="text-xs bg-primary-900/50 text-primary-400 px-2 py-1 rounded">Code examples</span>
                </div>
              </div>
              <svg className="w-6 h-6 text-gray-500 group-hover:text-primary-400 transition-colors" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
              </svg>
            </div>
          </Link>

          <Link href="/learn/proofs" className="card hover:border-accent-500 transition-colors group block">
            <div className="flex items-start justify-between">
              <div>
                <div className="flex items-center mb-2">
                  <svg className="w-6 h-6 text-accent-400 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 7h6m0 10v-3m-3 3h.01M9 17h.01M9 14h.01M12 14h.01M15 11h.01M12 11h.01M9 11h.01M7 21h10a2 2 0 002-2V5a2 2 0 00-2-2H7a2 2 0 00-2 2v14a2 2 0 002 2z" />
                  </svg>
                  <h2 className="text-xl font-bold group-hover:text-accent-400 transition-colors">Rigorous Proofs</h2>
                </div>
                <p className="text-gray-400 text-sm mb-3">
                  Step-by-step mathematical derivations with no skipped steps. Power Law Theorem, meta-Friedmann equations, spectral gap amplification.
                </p>
                <div className="flex flex-wrap gap-2">
                  <span className="text-xs bg-accent-900/50 text-accent-400 px-2 py-1 rounded">Full algebra</span>
                  <span className="text-xs bg-accent-900/50 text-accent-400 px-2 py-1 rounded">Numerical checks</span>
                </div>
              </div>
              <svg className="w-6 h-6 text-gray-500 group-hover:text-accent-400 transition-colors" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
              </svg>
            </div>
          </Link>

          <Link href="/learn/lessons" className="card hover:border-red-500 transition-colors group block bg-gradient-to-r from-red-900/10 to-transparent">
            <div className="flex items-start justify-between">
              <div>
                <div className="flex items-center mb-2">
                  <svg className="w-6 h-6 text-red-400 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" />
                  </svg>
                  <h2 className="text-xl font-bold group-hover:text-red-400 transition-colors">Lessons from Failures</h2>
                </div>
                <p className="text-gray-400 text-sm mb-3">
                  Documented failures and pivots. What we tried that didn't work, and why. Essential reading for avoiding the same mistakes.
                </p>
                <div className="flex flex-wrap gap-2">
                  <span className="text-xs bg-red-900/50 text-red-400 px-2 py-1 rounded">Bigeometric GR failure</span>
                  <span className="text-xs bg-red-900/50 text-red-400 px-2 py-1 rounded">QM violations</span>
                </div>
              </div>
              <svg className="w-6 h-6 text-gray-500 group-hover:text-red-400 transition-colors" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
              </svg>
            </div>
          </Link>
        </div>

        {/* Quick Facts */}
        <div className="card">
          <h2 className="text-xl font-bold mb-4">Quick Reference</h2>
          <div className="grid md:grid-cols-3 gap-4 text-center">
            <div className="bg-dark-bg rounded-lg p-4">
              <div className="text-2xl font-bold text-primary-400 mb-1">D_BG[x^n] = e^n</div>
              <p className="text-xs text-gray-500">Power Law Theorem</p>
            </div>
            <div className="bg-dark-bg rounded-lg p-4">
              <div className="text-2xl font-bold text-accent-400 mb-1">k -&gt; 0</div>
              <p className="text-xs text-gray-500">Classical calculus preferred</p>
            </div>
            <div className="bg-dark-bg rounded-lg p-4">
              <div className="text-2xl font-bold text-green-400 mb-1">~10^-14</div>
              <p className="text-xs text-gray-500">Safe meta-derivative norm drift</p>
            </div>
          </div>
        </div>

        {/* Navigation */}
        <div className="flex justify-between items-center mt-12">
          <Link href="/" className="text-gray-400 hover:text-white transition-colors">
            &larr; Home
          </Link>
          <Link href="/learn/textbook" className="btn-primary">
            Read Textbook &rarr;
          </Link>
        </div>
      </div>
    </div>
  );
}
