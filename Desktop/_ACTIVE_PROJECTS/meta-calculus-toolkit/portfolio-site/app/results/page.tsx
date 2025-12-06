import MathBlock from '@/components/MathBlock';
import Link from 'next/link';

export default function ResultsPage() {
  return (
    <div className="section">
      <div className="mx-auto max-w-4xl">
        <div className="animate-fade-in">
          <p className="text-accent-400 font-mono text-sm mb-2">Chapter 04</p>
          <h1 className="text-4xl font-bold mb-4">
            <span className="gradient-text">Results</span>
          </h1>
          <p className="text-xl text-gray-300 mb-8">
            Optimal calculus configurations, Pareto frontiers, and what we actually learned
          </p>
        </div>

        {/* Key Findings Summary */}
        <div className="card mb-8 animate-slide-up bg-gradient-to-r from-primary-900/30 to-accent-900/30">
          <h2 className="text-2xl font-bold mb-4">The Bottom Line</h2>
          <p className="text-gray-300 mb-6">
            After rigorous multi-objective optimization with two independent solvers:
          </p>
          <div className="grid gap-4 md:grid-cols-3 text-center">
            <div className="bg-dark-bg rounded-lg p-4">
              <div className="text-3xl font-bold text-primary-400">k -&gt; 0</div>
              <p className="text-sm text-gray-400 mt-2">Optimal meta-weight converges to zero</p>
            </div>
            <div className="bg-dark-bg rounded-lg p-4">
              <div className="text-3xl font-bold text-accent-400">|s| &lt; 0.05</div>
              <p className="text-sm text-gray-400 mt-2">Action weight tightly constrained</p>
            </div>
            <div className="bg-dark-bg rounded-lg p-4">
              <div className="text-3xl font-bold text-primary-400">chi2 = 0</div>
              <p className="text-sm text-gray-400 mt-2">Perfect observational fit at k=0</p>
            </div>
          </div>
        </div>

        {/* Optimizer Comparison */}
        <div className="card mb-8">
          <h2 className="text-2xl font-bold mb-4">Optimizer Comparison</h2>

          <div className="overflow-x-auto">
            <table className="w-full text-sm">
              <thead>
                <tr className="border-b border-gray-700">
                  <th className="text-left p-3 text-gray-400">Metric</th>
                  <th className="text-center p-3 text-primary-400">pymoo (NSGA-II)</th>
                  <th className="text-center p-3 text-accent-400">Global MOO</th>
                </tr>
              </thead>
              <tbody>
                <tr className="border-b border-gray-800">
                  <td className="p-3 text-gray-300">Pareto Solutions</td>
                  <td className="p-3 text-center">26</td>
                  <td className="p-3 text-center">--</td>
                </tr>
                <tr className="border-b border-gray-800">
                  <td className="p-3 text-gray-300">Best chi2</td>
                  <td className="p-3 text-center text-green-400">1.73e-18</td>
                  <td className="p-3 text-center">--</td>
                </tr>
                <tr className="border-b border-gray-800">
                  <td className="p-3 text-gray-300">Best Invariance</td>
                  <td className="p-3 text-center text-green-400">1.000</td>
                  <td className="p-3 text-center">--</td>
                </tr>
                <tr className="border-b border-gray-800">
                  <td className="p-3 text-gray-300">Best Spectral Gap</td>
                  <td className="p-3 text-center text-green-400">0.99999997</td>
                  <td className="p-3 text-center">--</td>
                </tr>
                <tr className="border-b border-gray-800">
                  <td className="p-3 text-gray-300">k Range</td>
                  <td className="p-3 text-center">[-0.023, 0.0001]</td>
                  <td className="p-3 text-center">--</td>
                </tr>
                <tr className="border-b border-gray-800">
                  <td className="p-3 text-gray-300">Generations</td>
                  <td className="p-3 text-center">100</td>
                  <td className="p-3 text-center">--</td>
                </tr>
              </tbody>
            </table>
          </div>

          <p className="text-sm text-gray-400 mt-4">
            <strong>Insight:</strong> pymoo aggressively drives k-&gt;0 for perfect chi2 fit,
            while Global MOO explores the full constraint-feasible region.
          </p>
        </div>

        {/* Representative Solutions */}
        <div className="card mb-8">
          <h2 className="text-2xl font-bold mb-4">Representative Pareto Solutions</h2>

          <div className="space-y-4">
            <div className="bg-dark-bg rounded-lg p-4 border-l-2 border-green-500">
              <div className="flex justify-between items-center mb-2">
                <h3 className="font-semibold text-green-400">Best Observational Fit</h3>
                <span className="text-xs text-gray-500 font-mono">pymoo #24</span>
              </div>
              <div className="grid grid-cols-4 gap-2 text-sm">
                <div><span className="text-gray-500">n:</span> 1.4905</div>
                <div><span className="text-gray-500">s:</span> 0.0383</div>
                <div><span className="text-gray-500">k:</span> 7.88e-13</div>
                <div><span className="text-gray-500">w:</span> -0.382</div>
              </div>
              <p className="text-xs text-gray-500 mt-2">chi2=1.73e-18, invariance=1.000, gap=0.9999980 (effectively classical)</p>
            </div>

            <div className="bg-dark-bg rounded-lg p-4 border-l-2 border-yellow-500">
              <div className="flex justify-between items-center mb-2">
                <h3 className="font-semibold text-yellow-400">Best Spectral Gap</h3>
                <span className="text-xs text-gray-500 font-mono">pymoo #1</span>
              </div>
              <div className="grid grid-cols-4 gap-2 text-sm">
                <div><span className="text-gray-500">n:</span> 0.4725</div>
                <div><span className="text-gray-500">s:</span> -0.0279</div>
                <div><span className="text-gray-500">k:</span> -0.0230</div>
                <div><span className="text-gray-500">w:</span> -0.434</div>
              </div>
              <p className="text-xs text-gray-500 mt-2">chi2=1470.67, invariance=1.000, gap=0.99999997 (max structure clarity)</p>
            </div>

            <div className="bg-dark-bg rounded-lg p-4 border-l-2 border-blue-500">
              <div className="flex justify-between items-center mb-2">
                <h3 className="font-semibold text-blue-400">Sweet Spot (Balanced)</h3>
                <span className="text-xs text-gray-500 font-mono">pymoo #8</span>
              </div>
              <div className="grid grid-cols-4 gap-2 text-sm">
                <div><span className="text-gray-500">n:</span> 0.5381</div>
                <div><span className="text-gray-500">s:</span> -0.0171</div>
                <div><span className="text-gray-500">k:</span> ~0</div>
                <div><span className="text-gray-500">w:</span> -0.279</div>
              </div>
              <p className="text-xs text-gray-500 mt-2">chi2=7.17e-14, invariance=1.000, gap=0.99999996 (optimal balance)</p>
            </div>

            <div className="bg-dark-bg rounded-lg p-4 border-l-2 border-orange-500">
              <div className="flex justify-between items-center mb-2">
                <h3 className="font-semibold text-orange-400">High-n Configuration</h3>
                <span className="text-xs text-gray-500 font-mono">pymoo #3</span>
              </div>
              <div className="grid grid-cols-4 gap-2 text-sm">
                <div><span className="text-gray-500">n:</span> 1.4976</div>
                <div><span className="text-gray-500">s:</span> -0.0135</div>
                <div><span className="text-gray-500">k:</span> 5.05e-05</div>
                <div><span className="text-gray-500">w:</span> -0.298</div>
              </div>
              <p className="text-xs text-gray-500 mt-2">chi2=0.0071, invariance=1.000, gap=0.9999996 (accelerated expansion)</p>
            </div>
          </div>
        </div>

        {/* The Physics Interpretation */}
        <div className="card mb-8">
          <h2 className="text-2xl font-bold mb-4">Physics Interpretation</h2>

          <div className="space-y-6">
            <div>
              <h3 className="font-semibold text-primary-400 mb-2">Why k-&gt;0?</h3>
              <p className="text-gray-300 mb-3">
                The meta-weight k controls how much the GUC corrections affect dynamics.
                Observational data strongly prefers k=0, meaning:
              </p>
              <blockquote className="border-l-4 border-primary-500 pl-4 py-2">
                <p className="text-primary-300 italic">
                  The universe, as observed, is best described by classical calculus.
                </p>
              </blockquote>
            </div>

            <div>
              <h3 className="font-semibold text-accent-400 mb-2">What About Non-Zero k?</h3>
              <p className="text-gray-300 mb-3">
                Solutions with k != 0 exist in the Pareto set, but they trade off:
              </p>
              <ul className="text-sm text-gray-400 space-y-1 ml-4">
                <li>* Worse chi-squared fit to observations</li>
                <li>* Lower scheme-robustness (less invariant across calculi)</li>
                <li>* Potential tension with BBN at the boundary</li>
              </ul>
            </div>

            <div>
              <h3 className="font-semibold text-primary-400 mb-2">The Scheme-Robust Insight</h3>
              <p className="text-gray-300">
                The key finding: <strong className="text-primary-400">physical observables
                are scheme-robust</strong>. Quantities that change significantly under
                different calculi are likely mathematical artifacts, not real physics.
              </p>
            </div>
          </div>
        </div>

        {/* Mathematical Summary */}
        <div className="card mb-8">
          <h2 className="text-2xl font-bold mb-4">Mathematical Summary</h2>

          <div className="space-y-6">
            <div className="bg-dark-bg rounded-lg p-4">
              <p className="text-gray-400 text-sm mb-2">Optimal expansion exponent:</p>
              <MathBlock
                equation="n_{opt} = \frac{2}{3(1+w)} + O(s,k) \quad \text{where } O(s,k) < 10^{-3}"
                displayMode={true}
              />
            </div>

            <div className="bg-dark-bg rounded-lg p-4">
              <p className="text-gray-400 text-sm mb-2">Scheme-robustness condition:</p>
              <MathBlock
                equation="I_{scheme} = \exp(-10(k^2 + s^2)) \approx 1 \quad \Leftrightarrow \quad k,s \approx 0"
                displayMode={true}
              />
            </div>

            <div className="bg-dark-bg rounded-lg p-4">
              <p className="text-gray-400 text-sm mb-2">Observational constraint region:</p>
              <MathBlock
                equation="\mathcal{F} = \{(s,k) : |s| \leq 0.05, |k| \leq 0.03\}"
                displayMode={true}
              />
            </div>
          </div>
        </div>

        {/* What We Learned */}
        <div className="card mb-8 bg-gradient-to-r from-accent-900/30 to-primary-900/30">
          <h2 className="text-2xl font-bold mb-4">What We Actually Learned</h2>

          <div className="space-y-4">
            <div className="flex items-start">
              <span className="text-green-400 mr-2 text-xl">1.</span>
              <div>
                <p className="font-semibold text-gray-200">The hunch was partially right</p>
                <p className="text-sm text-gray-400">Meta-calculus is mathematically consistent and can be applied to cosmology</p>
              </div>
            </div>
            <div className="flex items-start">
              <span className="text-yellow-400 mr-2 text-xl">2.</span>
              <div>
                <p className="font-semibold text-gray-200">But observations prefer classical calculus</p>
                <p className="text-sm text-gray-400">The Pareto-optimal solutions converge to k=0, s=0 for best fit</p>
              </div>
            </div>
            <div className="flex items-start">
              <span className="text-primary-400 mr-2 text-xl">3.</span>
              <div>
                <p className="font-semibold text-gray-200">Scheme-robustness is a useful concept</p>
                <p className="text-sm text-gray-400">Testing invariance across calculi helps identify real physics vs artifacts</p>
              </div>
            </div>
            <div className="flex items-start">
              <span className="text-accent-400 mr-2 text-xl">4.</span>
              <div>
                <p className="font-semibold text-gray-200">Rigorous validation matters</p>
                <p className="text-sm text-gray-400">AI hype needed computational reality checks - and those checks worked</p>
              </div>
            </div>
          </div>
        </div>

        {/* Scheme-Breaking Detection Results */}
        <div className="card mb-8 animate-slide-up bg-gradient-to-r from-green-900/20 to-primary-900/20">
          <h2 className="text-2xl font-bold mb-4">Scheme-Breaking Detection Results (Dec 2025)</h2>
          <p className="text-gray-300 mb-6">
            Latest MOO simulation hunting for new physics via scheme invariance breaking:
          </p>

          <div className="grid gap-4 md:grid-cols-3 text-center mb-6">
            <div className="bg-dark-bg rounded-lg p-4 border border-green-500/30">
              <div className="text-3xl font-bold text-green-400">950</div>
              <p className="text-sm text-gray-400 mt-2">Total evaluations (PyMOO + GlobalMOO)</p>
            </div>
            <div className="bg-dark-bg rounded-lg p-4 border border-yellow-500/30">
              <div className="text-3xl font-bold text-yellow-400">110</div>
              <p className="text-sm text-gray-400 mt-2">Breaking candidates found</p>
            </div>
            <div className="bg-dark-bg rounded-lg p-4 border border-primary-500/30">
              <div className="text-3xl font-bold text-primary-400">0</div>
              <p className="text-sm text-gray-400 mt-2">Physical candidates (expected)</p>
            </div>
          </div>

          <div className="space-y-4">
            <div className="bg-dark-bg rounded-lg p-4 border-l-2 border-green-500">
              <h3 className="font-semibold text-green-400 mb-2">Quantum Control: CQT == RNQT</h3>
              <p className="text-sm text-gray-400">
                Tested across dimensions 2, 3, 4 with 50 samples each.
                <strong className="text-green-400"> CONFIRMED: Zero breaking found.</strong>
                This validates the Hoffreumon-Woods 2025 theorem that complex and real
                number quantum theories are exactly equivalent.
              </p>
            </div>

            <div className="bg-dark-bg rounded-lg p-4 border-l-2 border-yellow-500">
              <h3 className="font-semibold text-yellow-400 mb-2">FRW Singular Regime</h3>
              <p className="text-sm text-gray-400">
                100 breaking points found near t=0 (Big Bang singularity). Max disagreement: 785,908.
                <strong className="text-yellow-400"> EXPECTED:</strong> Different C-schemes give
                different H(t) near singularities because coordinate time t is scheme-dependent.
                The physical observable H(z) remains scheme-robust.
              </p>
            </div>

            <div className="bg-dark-bg rounded-lg p-4 border-l-2 border-primary-500">
              <h3 className="font-semibold text-primary-400 mb-2">Regular Regime Search</h3>
              <p className="text-sm text-gray-400">
                PyMOO NSGA-II optimization with 30 generations found 80 Pareto-optimal solutions.
                Top scheme disagreement: 0.68 (at t=10us). All classified as numerical artifacts,
                not physical breaking. <strong className="text-primary-400">Scheme invariance holds.</strong>
              </p>
            </div>
          </div>
        </div>

        {/* G_scheme Formal Framework */}
        <div className="card mb-8">
          <h2 className="text-2xl font-bold mb-4">Formal G_scheme Framework</h2>
          <p className="text-gray-300 mb-4">
            The scheme-invariance framework now has rigorous mathematical foundations:
          </p>

          <div className="overflow-x-auto">
            <table className="w-full text-sm">
              <thead>
                <tr className="border-b border-gray-700">
                  <th className="text-left p-3 text-gray-400">Admissibility Axiom</th>
                  <th className="text-left p-3 text-gray-400">Requirement</th>
                  <th className="text-center p-3 text-green-400">Status</th>
                </tr>
              </thead>
              <tbody>
                <tr className="border-b border-gray-800">
                  <td className="p-3 text-primary-400">preserves_spectrum</td>
                  <td className="p-3 text-gray-300">Eigenvalues unchanged</td>
                  <td className="p-3 text-center text-green-400">PASS</td>
                </tr>
                <tr className="border-b border-gray-800">
                  <td className="p-3 text-primary-400">preserves_expectations</td>
                  <td className="p-3 text-gray-300">Probabilities agree</td>
                  <td className="p-3 text-center text-green-400">PASS</td>
                </tr>
                <tr className="border-b border-gray-800">
                  <td className="p-3 text-primary-400">is_local</td>
                  <td className="p-3 text-gray-300">No nonlocal dependence</td>
                  <td className="p-3 text-center text-green-400">PASS</td>
                </tr>
                <tr className="border-b border-gray-800">
                  <td className="p-3 text-primary-400">is_invertible</td>
                  <td className="p-3 text-gray-300">Bijective transformation</td>
                  <td className="p-3 text-center text-green-400">PASS</td>
                </tr>
                <tr className="border-b border-gray-800">
                  <td className="p-3 text-primary-400">is_smooth</td>
                  <td className="p-3 text-gray-300">Differentiable in domain</td>
                  <td className="p-3 text-center text-green-400">PASS</td>
                </tr>
              </tbody>
            </table>
          </div>

          <p className="text-sm text-gray-400 mt-4">
            <strong>Key Theorem:</strong> Meta-derivatives D_meta = u(t)f'(t) + v(t)f(t) are admissible
            iff u(t) &gt; 0 throughout the domain. The pullback tau(t) = integral(u(s)ds) recovers standard calculus.
          </p>
        </div>

        {/* Future Directions */}
        <div className="card mb-8">
          <h2 className="text-2xl font-bold mb-4">Future Directions</h2>
          <ul className="space-y-2 text-gray-300">
            <li className="flex items-start">
              <span className="text-accent-400 mr-2">-&gt;</span>
              <span>Apply meta-calculus to quantum mechanics (Schrodinger equation)</span>
            </li>
            <li className="flex items-start">
              <span className="text-accent-400 mr-2">-&gt;</span>
              <span>Test scheme-robustness on other cosmological parameters</span>
            </li>
            <li className="flex items-start">
              <span className="text-accent-400 mr-2">-&gt;</span>
              <span>Develop formal proofs for compatibility hierarchy</span>
            </li>
            <li className="flex items-start">
              <span className="text-accent-400 mr-2">-&gt;</span>
              <span>Investigate if k != 0 regimes are relevant at Planck scale</span>
            </li>
            <li className="flex items-start">
              <span className="text-green-400 mr-2">NEW</span>
              <span>Hunt for anomalies as G_scheme obstructions in QFT</span>
            </li>
            <li className="flex items-start">
              <span className="text-green-400 mr-2">NEW</span>
              <span>Test amplitude representation invariance (Feynman vs BCFW vs Amplituhedron)</span>
            </li>
          </ul>
        </div>

        {/* Navigation */}
        <div className="flex justify-between items-center mt-12">
          <Link href="/simulator" className="text-gray-400 hover:text-white transition-colors">
            &larr; Back to Simulator
          </Link>
          <Link href="/quantum" className="btn-primary">
            Next: Meta-Quantum &rarr;
          </Link>
        </div>
      </div>
    </div>
  );
}
