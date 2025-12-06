import Link from 'next/link';
import MathBlock from '@/components/MathBlock';

export const metadata = {
  title: 'Textbook | Meta-Calculus',
  description: 'Complete learning path and textbook for the Meta-Calculus framework with proofs and applications.',
};

export default function TextbookPage() {
  return (
    <div className="section">
      {/* Hero Section */}
      <div className="mx-auto max-w-4xl text-center mb-12 animate-fade-in">
        <p className="text-primary-400 font-mono text-sm mb-4">Complete Learning Resource</p>
        <h1 className="text-4xl font-bold tracking-tight sm:text-5xl mb-6">
          <span className="gradient-text">Meta-Calculus Textbook</span>
        </h1>
        <p className="text-xl text-gray-300 mb-6">
          A comprehensive guide from discovery through rigorous validation
        </p>
        <div className="flex flex-wrap justify-center gap-4">
          <a
            href="/META_CALCULUS_TEXTBOOK.md"
            download="META_CALCULUS_TEXTBOOK.md"
            className="btn-primary inline-flex items-center gap-2"
          >
            <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
            </svg>
            Download Textbook (Markdown)
          </a>
        </div>
      </div>

      {/* Table of Contents */}
      <div className="mx-auto max-w-4xl mb-12">
        <div className="card">
          <h2 className="text-2xl font-bold mb-6">Table of Contents</h2>
          <div className="grid md:grid-cols-2 gap-6">
            <div>
              <h3 className="text-lg font-semibold text-primary-400 mb-3">Part I: Learning Path</h3>
              <ul className="space-y-2 text-gray-300">
                <li className="flex items-start gap-2">
                  <span className="text-primary-500">1.</span>
                  <span>Discovery and Initial Exploration</span>
                </li>
                <li className="flex items-start gap-2">
                  <span className="text-primary-500">2.</span>
                  <span>Physics Singularity Analysis</span>
                </li>
                <li className="flex items-start gap-2">
                  <span className="text-primary-500">3.</span>
                  <span>Implementation and Simulation</span>
                </li>
                <li className="flex items-start gap-2">
                  <span className="text-primary-500">4.</span>
                  <span>Critical Audit and Course Correction</span>
                </li>
                <li className="flex items-start gap-2">
                  <span className="text-primary-500">5.</span>
                  <span>The Paradigm Shift (v2.0)</span>
                </li>
                <li className="flex items-start gap-2">
                  <span className="text-primary-500">6.</span>
                  <span>Multi-Objective Optimization</span>
                </li>
                <li className="flex items-start gap-2">
                  <span className="text-primary-500">7.</span>
                  <span>Quantum Mechanics Testing</span>
                </li>
                <li className="flex items-start gap-2">
                  <span className="text-primary-500">8.</span>
                  <span>Final Synthesis</span>
                </li>
              </ul>
            </div>
            <div>
              <h3 className="text-lg font-semibold text-accent-400 mb-3">Part III: Textbook Chapters</h3>
              <ul className="space-y-2 text-gray-300">
                <li className="flex items-start gap-2">
                  <span className="text-accent-500">1.</span>
                  <span>Foundations of Non-Newtonian Calculus</span>
                </li>
                <li className="flex items-start gap-2">
                  <span className="text-accent-500">2.</span>
                  <span>Meta-Calculus Framework</span>
                </li>
                <li className="flex items-start gap-2">
                  <span className="text-accent-500">3.</span>
                  <span>Multi-Calculus Framework (v2.0)</span>
                </li>
                <li className="flex items-start gap-2">
                  <span className="text-accent-500">4.</span>
                  <span>Applications to Physics</span>
                </li>
                <li className="flex items-start gap-2">
                  <span className="text-accent-500">5.</span>
                  <span>Validation and Constraints</span>
                </li>
                <li className="flex items-start gap-2">
                  <span className="text-accent-500">6.</span>
                  <span>The Hierarchy of Approaches</span>
                </li>
                <li className="flex items-start gap-2">
                  <span className="text-accent-500">7.</span>
                  <span>Use Cases and Applications</span>
                </li>
                <li className="flex items-start gap-2">
                  <span className="text-accent-500">8-9.</span>
                  <span>Open Problems & Conclusions</span>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>

      {/* Key Theorems Preview */}
      <div className="mx-auto max-w-4xl mb-12">
        <h2 className="text-2xl font-bold mb-6 text-center">Key Theorems & Proofs</h2>
        <div className="space-y-6">
          {/* Theorem 1 */}
          <div className="card border-l-4 border-primary-500">
            <h3 className="text-lg font-semibold text-primary-400 mb-3">Theorem 1.1: Power Law Theorem</h3>
            <p className="text-gray-300 mb-4">
              For f(x) = x^n where n is any real number:
            </p>
            <MathBlock
              equation="D_{BG}[x^n] = e^n"
              displayMode={true}
            />
            <div className="mt-4 bg-dark-bg rounded-lg p-4">
              <p className="text-sm text-gray-400 mb-2">Proof:</p>
              <div className="space-y-2 font-mono text-sm text-gray-300">
                <p>D_BG[x^n] = exp(x * d/dx[x^n] / x^n)</p>
                <p className="pl-8">= exp(x * n*x^(n-1) / x^n)</p>
                <p className="pl-8">= exp(x * n*x^(-1))</p>
                <p className="pl-8">= exp(n) QED</p>
              </div>
            </div>
          </div>

          {/* Theorem 2 */}
          <div className="card border-l-4 border-accent-500">
            <h3 className="text-lg font-semibold text-accent-400 mb-3">Theorem 3.1: Spectral Gap Amplification</h3>
            <p className="text-gray-300 mb-4">
              The spectral gap of the mixed operator P_mix is typically larger than any individual operator:
            </p>
            <MathBlock
              equation="gap(P_{mix}) > \max\{gap(P_A), gap(P_B), gap(P_C)\}"
              displayMode={true}
            />
            <div className="mt-4 bg-dark-bg rounded-lg p-4">
              <p className="text-sm text-gray-400 mb-2">Experimental Result:</p>
              <div className="grid grid-cols-2 gap-4 text-sm">
                <div>
                  <p className="text-gray-500">gap(P_A):</p>
                  <p className="text-gray-300 font-mono">~0.03</p>
                </div>
                <div>
                  <p className="text-gray-500">gap(P_B):</p>
                  <p className="text-gray-300 font-mono">~0.01</p>
                </div>
                <div>
                  <p className="text-gray-500">gap(P_C):</p>
                  <p className="text-gray-300 font-mono">~0.00002</p>
                </div>
                <div>
                  <p className="text-gray-500">gap(P_mix):</p>
                  <p className="text-primary-400 font-mono font-bold">~0.11 (4x improvement!)</p>
                </div>
              </div>
            </div>
          </div>

          {/* Theorem 3 */}
          <div className="card border-l-4 border-blue-500">
            <h3 className="text-lg font-semibold text-blue-400 mb-3">Theorem 5.1: Observational Preference</h3>
            <p className="text-gray-300 mb-4">
              Multi-objective optimization finds that the meta-weight parameter k converges to zero for best observational fit.
            </p>
            <MathBlock
              equation="k \to 0 \text{ (classical calculus preferred)}"
              displayMode={true}
            />
            <p className="text-gray-400 text-sm mt-4">
              This is a NEGATIVE result for strong meta-calculus claims, but a POSITIVE result for the validation methodology.
            </p>
          </div>
        </div>
      </div>

      {/* The Hierarchy */}
      <div className="mx-auto max-w-4xl mb-12">
        <h2 className="text-2xl font-bold mb-6 text-center">The Correct Hierarchy</h2>
        <div className="grid md:grid-cols-3 gap-6">
          <div className="card text-center border-t-4 border-green-500">
            <div className="text-4xl mb-4">1</div>
            <h3 className="text-lg font-semibold text-green-400 mb-2">Meta-Calculus</h3>
            <p className="text-gray-400 text-sm">For modified field equations. Preserves tensor linearity.</p>
            <p className="text-green-500 font-mono text-xs mt-2">USE FOR: Modifying dynamics</p>
          </div>
          <div className="card text-center border-t-4 border-yellow-500">
            <div className="text-4xl mb-4">2</div>
            <h3 className="text-lg font-semibold text-yellow-400 mb-2">Bigeometric</h3>
            <p className="text-gray-400 text-sm">For diagnostic analysis. Power law exponents become constants.</p>
            <p className="text-yellow-500 font-mono text-xs mt-2">USE FOR: Understanding</p>
          </div>
          <div className="card text-center border-t-4 border-blue-500">
            <div className="text-4xl mb-4">3</div>
            <h3 className="text-lg font-semibold text-blue-400 mb-2">Multi-Calculus</h3>
            <p className="text-gray-400 text-sm">For invariant extraction. Physical = scheme-robust.</p>
            <p className="text-blue-500 font-mono text-xs mt-2">USE FOR: Identifying physics</p>
          </div>
        </div>
      </div>

      {/* What Does NOT Work */}
      <div className="mx-auto max-w-4xl mb-12">
        <div className="card bg-red-900/20 border-red-500/50">
          <h2 className="text-2xl font-bold mb-4 text-red-400">What Does NOT Work</h2>
          <ul className="space-y-3 text-gray-300">
            <li className="flex items-start gap-3">
              <span className="text-red-500 text-xl">X</span>
              <div>
                <strong>Full bigeometric GR</strong>
                <p className="text-gray-500 text-sm">D_BG[const] = 1, breaks tensor calculus</p>
              </div>
            </li>
            <li className="flex items-start gap-3">
              <span className="text-red-500 text-xl">X</span>
              <div>
                <strong>L_BG-Christoffel substitution</strong>
                <p className="text-gray-500 text-sm">Falsified in 4D, static metrics untouched</p>
              </div>
            </li>
            <li className="flex items-start gap-3">
              <span className="text-red-500 text-xl">X</span>
              <div>
                <strong>Component-wise quantum modifications</strong>
                <p className="text-gray-500 text-sm">Breaks unitarity (65% norm drift for log-derivative)</p>
              </div>
            </li>
          </ul>
        </div>
      </div>

      {/* Key Insight Quote */}
      <div className="mx-auto max-w-3xl mb-12">
        <blockquote className="card border-l-4 border-primary-500 text-center py-8">
          <p className="text-2xl text-gray-200 italic mb-4">
            "Physical = Scheme-Robust = Cross-Calculus Invariant"
          </p>
          <p className="text-gray-400">
            Features that survive analysis under multiple calculi are candidates for genuine physics;
            features that appear only in one calculus may be mathematical artifacts.
          </p>
        </blockquote>
      </div>

      {/* Download CTA */}
      <div className="mx-auto max-w-3xl text-center">
        <div className="card bg-gradient-to-r from-primary-900/50 to-accent-900/50 border-primary-600/50">
          <h2 className="text-2xl font-bold mb-4">Download the Complete Textbook</h2>
          <p className="text-gray-300 mb-6">
            900+ lines of comprehensive content including 9 chapters, 3 appendices,
            complete proofs, formulas, code examples, and honest reporting of findings.
          </p>
          <div className="flex flex-wrap justify-center gap-4">
            <a
              href="/META_CALCULUS_TEXTBOOK.md"
              download="META_CALCULUS_TEXTBOOK.md"
              className="btn-primary inline-flex items-center gap-2"
            >
              <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
              </svg>
              Download Markdown
            </a>
            <Link href="/tools/code" className="btn-secondary">
              View Source Code
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
}
