import Link from 'next/link';

export const metadata = {
  title: 'Tools | Meta-Calculus',
  description: 'Interactive simulators and source code for the meta-calculus framework.',
};

export default function ToolsPage() {
  return (
    <div className="section">
      <div className="mx-auto max-w-4xl">
        <div className="animate-fade-in">
          <p className="text-primary-400 font-mono text-sm mb-2">Interactive & Code</p>
          <h1 className="text-4xl font-bold mb-4">
            <span className="gradient-text">Tools</span>
          </h1>
          <p className="text-xl text-gray-300 mb-8">
            Explore the mathematics interactively and access the complete source code
          </p>
        </div>

        {/* Tool Cards */}
        <div className="grid gap-6 md:grid-cols-2 mb-12">
          <Link href="/tools/simulator" className="card hover:border-primary-500 transition-colors group">
            <div className="flex items-center mb-4">
              <div className="w-12 h-12 rounded-lg bg-primary-900/50 flex items-center justify-center mr-4">
                <svg className="w-6 h-6 text-primary-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9.75 17L9 20l-1 1h8l-1-1-.75-3M3 13h18M5 17h14a2 2 0 002-2V5a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                </svg>
              </div>
              <div>
                <h2 className="text-xl font-bold group-hover:text-primary-400 transition-colors">Simulator</h2>
                <p className="text-sm text-gray-500">Interactive visualizations</p>
              </div>
            </div>
            <p className="text-gray-400 text-sm mb-4">
              Explore Pareto frontiers, parameter spaces, quantum compatibility, and multi-calculus diffusion with interactive visualizers.
            </p>
            <div className="flex flex-wrap gap-2">
              <span className="text-xs bg-dark-bg text-gray-400 px-2 py-1 rounded">Pareto Explorer</span>
              <span className="text-xs bg-dark-bg text-gray-400 px-2 py-1 rounded">Parameter Space</span>
              <span className="text-xs bg-dark-bg text-gray-400 px-2 py-1 rounded">Quantum Tests</span>
            </div>
          </Link>

          <Link href="/tools/code" className="card hover:border-accent-500 transition-colors group">
            <div className="flex items-center mb-4">
              <div className="w-12 h-12 rounded-lg bg-accent-900/50 flex items-center justify-center mr-4">
                <svg className="w-6 h-6 text-accent-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4" />
                </svg>
              </div>
              <div>
                <h2 className="text-xl font-bold group-hover:text-accent-400 transition-colors">Source Code</h2>
                <p className="text-sm text-gray-500">Python implementation</p>
              </div>
            </div>
            <p className="text-gray-400 text-sm mb-4">
              Complete Python library for meta-calculus: generators, derivatives, scheme-robustness, FRW cosmology, and MOO integration.
            </p>
            <div className="flex flex-wrap gap-2">
              <span className="text-xs bg-dark-bg text-gray-400 px-2 py-1 rounded">meta_calculus/</span>
              <span className="text-xs bg-dark-bg text-gray-400 px-2 py-1 rounded">pymoo</span>
              <span className="text-xs bg-dark-bg text-gray-400 px-2 py-1 rounded">numpy</span>
            </div>
          </Link>
        </div>

        {/* Quick Links */}
        <div className="card bg-gradient-to-r from-primary-900/20 to-accent-900/20">
          <h2 className="text-xl font-bold mb-4">Quick Access</h2>
          <div className="grid md:grid-cols-2 gap-4">
            <a
              href="/moo_results.json"
              download
              className="flex items-center p-3 bg-dark-bg rounded-lg hover:bg-dark-border transition-colors"
            >
              <svg className="w-5 h-5 text-primary-400 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
              </svg>
              <div>
                <p className="font-medium text-sm">Download MOO Results</p>
                <p className="text-xs text-gray-500">JSON - 26 Pareto solutions</p>
              </div>
            </a>
            <a
              href="/quantum_results.json"
              download
              className="flex items-center p-3 bg-dark-bg rounded-lg hover:bg-dark-border transition-colors"
            >
              <svg className="w-5 h-5 text-accent-400 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
              </svg>
              <div>
                <p className="font-medium text-sm">Download Quantum Results</p>
                <p className="text-xs text-gray-500">JSON - 50 Pareto solutions</p>
              </div>
            </a>
          </div>
        </div>

        {/* Navigation */}
        <div className="flex justify-between items-center mt-12">
          <Link href="/" className="text-gray-400 hover:text-white transition-colors">
            &larr; Home
          </Link>
          <Link href="/tools/simulator" className="btn-primary">
            Open Simulator &rarr;
          </Link>
        </div>
      </div>
    </div>
  );
}
