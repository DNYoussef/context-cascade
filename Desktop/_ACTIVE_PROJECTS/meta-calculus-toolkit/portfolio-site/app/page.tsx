import Link from 'next/link';
import MathBlock from '@/components/MathBlock';

export default function HomePage() {
  return (
    <div className="section">
      {/* Hero Section */}
      <div className="mx-auto max-w-4xl text-center animate-fade-in">
        <p className="text-primary-400 font-mono text-sm mb-4">A Physics Research Portfolio</p>
        <h1 className="text-5xl font-bold tracking-tight sm:text-6xl mb-6">
          <span className="gradient-text">Meta-Calculus</span>
        </h1>
        <p className="text-2xl text-gray-200 mb-4 font-light">
          The geometry is real; the calculus is a lens.
        </p>
        <p className="text-lg text-gray-400 mb-8 max-w-2xl mx-auto">
          A journey from theoretical physics through AI-assisted exploration to
          rigorous computational validation. This is the honest story of finding
          scheme-robust observables in cosmology.
        </p>
        <div className="flex flex-wrap justify-center gap-4 mb-12">
          <Link href="/exploration" className="btn-primary">
            Start the Journey
          </Link>
          <Link href="/results" className="btn-secondary">
            See the Results
          </Link>
        </div>
      </div>

      {/* The Core Insight */}
      <div className="mx-auto max-w-3xl my-16 animate-slide-up">
        <div className="card border-l-4 border-primary-500">
          <h2 className="text-2xl font-bold mb-4">The Core Insight</h2>
          <p className="text-gray-300 mb-6">
            Instead of searching for the correct calculus (classical, GUC, bigeometric),
            we use <strong className="text-primary-400">families of calculi</strong> to extract
            what is intrinsic to the underlying geometry. Cross-calculus invariants are the
            candidates for physically meaningful structure.
          </p>
          <div className="bg-dark-bg rounded-lg p-4 mb-4">
            <p className="text-center text-xl font-mono text-primary-300">
              Physical = Scheme-Robust = Cross-Calculus Invariant
            </p>
          </div>
          <p className="text-gray-400 text-sm">
            This reframing emerged from experiments showing that mixed diffusion operators
            have 4x larger spectral gaps, and that structure surviving all calculi represents
            real physics.
          </p>
        </div>
      </div>

      {/* Key Equations */}
      <div className="mx-auto max-w-3xl my-16">
        <div className="card">
          <h2 className="text-2xl font-bold mb-6">The Mathematics</h2>
          <div className="space-y-6">
            <div>
              <p className="text-gray-400 text-sm mb-2">Meta-Friedmann equations with GUC corrections:</p>
              <MathBlock
                equation="n_{act}(s,w) = \frac{-(3ws + 2s - 2) + \sqrt{\Delta}}{6(1+w)}"
                displayMode={true}
              />
            </div>
            <div>
              <p className="text-gray-400 text-sm mb-2">Where the discriminant ensures real solutions:</p>
              <MathBlock
                equation="\Delta(s,w) = 9s^2w^2 - 8s^2 + 4s + 4"
                displayMode={true}
              />
            </div>
            <div>
              <p className="text-gray-400 text-sm mb-2">Observable constraints from BBN and CMB:</p>
              <MathBlock
                equation="|s| \leq 0.05, \quad |k| \leq 0.03"
                displayMode={true}
              />
            </div>
          </div>
        </div>
      </div>

      {/* Journey Sections */}
      <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-4 my-16">
        <Link href="/exploration" className="card group hover:border-primary-500 transition-colors">
          <div className="text-primary-400 mb-4 text-3xl font-bold">01</div>
          <h3 className="text-xl font-semibold mb-2 group-hover:text-primary-400 transition-colors">
            The Hunch
          </h3>
          <p className="text-gray-400 text-sm">
            What if the weirdness of modern physics is partly an artifact of using
            the wrong calculus? Time series geometry and non-Newtonian calculus.
          </p>
        </Link>

        <Link href="/ai-journey" className="card group hover:border-accent-500 transition-colors">
          <div className="text-accent-400 mb-4 text-3xl font-bold">02</div>
          <h3 className="text-xl font-semibold mb-2 group-hover:text-accent-400 transition-colors">
            AI Hype & Audits
          </h3>
          <p className="text-gray-400 text-sm">
            The honest story of AI over-promising, the need for rigorous audits,
            and learning what AI can and cannot do for physics research.
          </p>
        </Link>

        <Link href="/validation" className="card group hover:border-primary-500 transition-colors">
          <div className="text-primary-400 mb-4 text-3xl font-bold">03</div>
          <h3 className="text-xl font-semibold mb-2 group-hover:text-primary-400 transition-colors">
            Rigorous Validation
          </h3>
          <p className="text-gray-400 text-sm">
            Multi-objective optimization, Pareto frontiers, and computational
            verification of scheme-robust observables.
          </p>
        </Link>

        <Link href="/results" className="card group hover:border-accent-500 transition-colors">
          <div className="text-accent-400 mb-4 text-3xl font-bold">04</div>
          <h3 className="text-xl font-semibold mb-2 group-hover:text-accent-400 transition-colors">
            Results
          </h3>
          <p className="text-gray-400 text-sm">
            Optimal calculus configurations, Pareto frontiers, and what we
            actually learned about physics.
          </p>
        </Link>
      </div>

      {/* Key Results Preview */}
      <div className="mx-auto max-w-4xl my-16">
        <h2 className="text-3xl font-bold text-center mb-8">Key Findings</h2>
        <div className="grid gap-6 md:grid-cols-3">
          <div className="card text-center">
            <div className="text-4xl font-bold text-primary-400 mb-2">12</div>
            <h3 className="font-semibold text-lg mb-2">Pareto Solutions</h3>
            <p className="text-gray-400 text-sm">
              Optimal configurations found via NSGA-II optimization
            </p>
          </div>
          <div className="card text-center">
            <div className="text-4xl font-bold text-accent-400 mb-2">1.0</div>
            <h3 className="font-semibold text-lg mb-2">Invariance Score</h3>
            <p className="text-gray-400 text-sm">
              Perfect scheme-robustness across all calculi
            </p>
          </div>
          <div className="card text-center">
            <div className="text-4xl font-bold text-primary-400 mb-2">k=0</div>
            <h3 className="font-semibold text-lg mb-2">Meta-Weight</h3>
            <p className="text-gray-400 text-sm">
              Converges to zero for observational fit
            </p>
          </div>
        </div>
      </div>

      {/* Tech Stack */}
      <div className="mx-auto max-w-4xl my-16">
        <h2 className="text-3xl font-bold text-center mb-8">Built With</h2>
        <div className="grid gap-4 md:grid-cols-4 text-center">
          <div className="card py-4">
            <h3 className="font-semibold">Python + NumPy</h3>
            <p className="text-gray-500 text-xs mt-1">Physics simulations</p>
          </div>
          <div className="card py-4">
            <h3 className="font-semibold">pymoo</h3>
            <p className="text-gray-500 text-xs mt-1">Multi-objective optimization</p>
          </div>
          <div className="card py-4">
            <h3 className="font-semibold">Global MOO</h3>
            <p className="text-gray-500 text-xs mt-1">Agent-based optimization</p>
          </div>
          <div className="card py-4">
            <h3 className="font-semibold">Claude Code</h3>
            <p className="text-gray-500 text-xs mt-1">AI-assisted development</p>
          </div>
        </div>
      </div>

      {/* CTA */}
      <div className="mx-auto max-w-3xl my-16 text-center">
        <div className="card bg-gradient-to-r from-primary-900/50 to-accent-900/50 border-primary-600/50">
          <h2 className="text-2xl font-bold mb-4">Explore the Code</h2>
          <p className="text-gray-300 mb-6">
            All the Python modules, optimization scripts, and analysis tools
            are available. See how we went from theory to validation.
          </p>
          <Link href="/code" className="btn-primary">
            View Source Code
          </Link>
        </div>
      </div>
    </div>
  );
}
