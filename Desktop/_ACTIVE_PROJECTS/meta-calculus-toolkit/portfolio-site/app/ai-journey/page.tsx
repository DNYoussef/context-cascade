import Link from 'next/link';
import MathBlock from '@/components/MathBlock';
import CodeBlock from '@/components/CodeBlock';

export default function AIJourneyPage() {
  return (
    <div className="section">
      <div className="mx-auto max-w-4xl">
        <div className="animate-fade-in">
          <p className="text-accent-400 font-mono text-sm mb-2">Chapter 02</p>
          <h1 className="text-4xl font-bold mb-4">
            <span className="gradient-text">AI Hype & Audits</span>
          </h1>
          <p className="text-xl text-gray-300 mb-8">
            From over-promising to publishable methodology: how falsification saved the project
          </p>
        </div>

        {/* The Original Hunch */}
        <div className="card mb-8 animate-slide-up border-l-4 border-accent-500">
          <h2 className="text-2xl font-bold mb-4">The Original Hunch</h2>
          <p className="text-gray-300 mb-4">
            The starting hypothesis was simple and bold: <strong className="text-accent-400">
            maybe some of the weirdness in modern physics - infinities, singularities,
            dark energy - are artifacts of using the wrong calculus system.</strong>
          </p>
          <p className="text-gray-300">
            After all, we use classical (Newtonian) calculus everywhere in physics.
            But there are infinitely many other valid calculi - geometric, bigeometric,
            anageometric. What if switching to a different mathematical language would
            make some problems disappear?
          </p>
        </div>

        {/* The AI Hype Phase */}
        <div className="card mb-8">
          <h2 className="text-2xl font-bold mb-4">The AI Hype Phase</h2>
          <p className="text-gray-300 mb-4">
            When AI tools were brought in to explore this idea, things got exciting fast.
            The AI confidently suggested that <strong className="text-primary-400">
            bigeometric calculus could solve everything</strong>:
          </p>

          <div className="bg-dark-bg rounded-lg p-4 mb-4 border-l-2 border-yellow-500">
            <p className="text-gray-300 italic">
              &quot;The bigeometric derivative of the Ricci scalar is bounded even at r=0,
              suggesting singularities are purely coordinate artifacts...&quot;
            </p>
            <p className="text-sm text-gray-500 mt-2">- AI-generated claim (unverified)</p>
          </div>

          <p className="text-gray-300 mb-4">
            This sounded revolutionary. The AI produced equations, made connections to
            known physics, and generated code that looked plausible. It felt like we
            were onto something big.
          </p>

          <p className="text-gray-300">
            <strong className="text-red-400">The problem:</strong> Most of it was wrong.
          </p>
        </div>

        {/* The Scientific Instinct */}
        <div className="card mb-8 bg-gradient-to-r from-red-900/20 to-accent-900/20">
          <h2 className="text-2xl font-bold mb-4">The Scientific Reality Check</h2>
          <blockquote className="border-l-4 border-red-500 pl-4 py-2 my-4">
            <p className="text-xl text-red-300 italic">
              If it is not falsifiable and you do not run simulations, it is BS.
            </p>
          </blockquote>
          <p className="text-gray-300 mb-4">
            Having just enough background in science to know this, we stopped
            celebrating and started testing. The approach:
          </p>
          <ul className="space-y-2 text-gray-300">
            <li className="flex items-start">
              <span className="text-accent-400 mr-2">1.</span>
              <span>Build toy models with actual numbers, not just symbols</span>
            </li>
            <li className="flex items-start">
              <span className="text-accent-400 mr-2">2.</span>
              <span>Run simulations that could falsify the claims</span>
            </li>
            <li className="flex items-start">
              <span className="text-accent-400 mr-2">3.</span>
              <span>Check against observational constraints (BBN, CMB)</span>
            </li>
            <li className="flex items-start">
              <span className="text-accent-400 mr-2">4.</span>
              <span>Use multi-objective optimization to scan parameter space</span>
            </li>
          </ul>
        </div>

        {/* What We Falsified */}
        <div className="card mb-8">
          <h2 className="text-2xl font-bold mb-4">What Got Falsified</h2>
          <p className="text-gray-300 mb-6">
            When we actually ran the simulations, several AI-hyped claims failed:
          </p>

          <div className="space-y-4">
            <div className="bg-dark-bg rounded-lg p-4 border-l-2 border-red-500">
              <h3 className="font-semibold text-red-400 mb-2">Claim: Bigeometric calculus removes all singularities</h3>
              <p className="text-sm text-gray-400">
                <strong>Reality:</strong> Bigeometric derivative D_BG[constant] = 1, not 0.
                This breaks the linear structure Einstein equations require. Minkowski
                space stops looking flat. The 4D FRW curvature actually blows up WORSE.
              </p>
            </div>

            <div className="bg-dark-bg rounded-lg p-4 border-l-2 border-red-500">
              <h3 className="font-semibold text-red-400 mb-2">Claim: k = -0.7 explains dark energy</h3>
              <p className="text-sm text-gray-400">
                <strong>Reality:</strong> k = -0.7 violates BBN constraints by a factor of 20+.
                The chi-squared fit was terrible. Observationally ruled out immediately.
              </p>
            </div>

            <div className="bg-dark-bg rounded-lg p-4 border-l-2 border-red-500">
              <h3 className="font-semibold text-red-400 mb-2">Claim: Alternative calculus = new physics</h3>
              <p className="text-sm text-gray-400">
                <strong>Reality:</strong> GUC with nontrivial weights is just a coordinate
                change + measure modification. The t^(2k) factor in L_meta IS the Jacobian
                from tau = t^(1-k)/(1-k). Not new physics - just different coordinates.
              </p>
            </div>
          </div>
        </div>

        {/* The Breakthrough */}
        <div className="card mb-8 bg-gradient-to-r from-primary-900/30 to-accent-900/30">
          <h2 className="text-2xl font-bold mb-4">The Actual Discovery</h2>
          <p className="text-gray-300 mb-4">
            But here is where it gets interesting. While falsifying the hype, we discovered
            something genuinely useful: <strong className="text-primary-400">a methodology
            for testing which features of physics are real vs artifacts.</strong>
          </p>

          <p className="text-gray-300 mb-4">
            By scanning the space of calculus configurations with multi-objective optimization,
            we found:
          </p>

          <div className="grid gap-4 md:grid-cols-2 mb-6">
            <div className="bg-dark-bg rounded-lg p-4 border-l-2 border-green-500">
              <h3 className="font-semibold text-green-400 mb-2">Some infinities DISAPPEAR</h3>
              <p className="text-sm text-gray-400">
                In certain calculi, quantities like R ~ t^(-2) become bounded.
                The bigeometric derivative gives D_BG[R] = e^(-2) - finite!
              </p>
            </div>

            <div className="bg-dark-bg rounded-lg p-4 border-l-2 border-yellow-500">
              <h3 className="font-semibold text-yellow-400 mb-2">Some infinities PERSIST</h3>
              <p className="text-sm text-gray-400">
                Other singularities appear in ALL calculi we tested. No coordinate
                change makes them go away. These are scheme-robust.
              </p>
            </div>
          </div>

          <p className="text-gray-300">
            <strong className="text-accent-400">The key insight:</strong> Infinities that
            disappear in some calculi are likely <em>mathematical artifacts</em>. Infinities
            that persist across ALL calculi are likely <em>real physics</em>.
          </p>
        </div>

        {/* The Publishable Methodology */}
        <div className="card mb-8">
          <h2 className="text-2xl font-bold mb-4">Publishable Methodology: Calculus Ensemble Analysis</h2>
          <p className="text-gray-300 mb-4">
            This approach - using families of calculi to test which features are
            scheme-robust - is actually a novel contribution:
          </p>

          <div className="bg-dark-bg rounded-lg p-4 mb-6">
            <MathBlock
              equation="\text{Physical} = \text{Scheme-Robust} = \text{Cross-Calculus Invariant}"
              displayMode={true}
            />
          </div>

          <div className="overflow-x-auto mb-6">
            <table className="w-full text-sm">
              <thead>
                <tr className="border-b border-gray-700">
                  <th className="text-left p-3 text-gray-400">Feature</th>
                  <th className="text-center p-3 text-gray-400">Scheme-Dependent</th>
                  <th className="text-center p-3 text-gray-400">Scheme-Robust</th>
                  <th className="text-left p-3 text-gray-400">Interpretation</th>
                </tr>
              </thead>
              <tbody>
                <tr className="border-b border-gray-800">
                  <td className="p-3 text-gray-300">Some curvature singularities</td>
                  <td className="p-3 text-center text-green-400">Yes</td>
                  <td className="p-3 text-center text-gray-500">-</td>
                  <td className="p-3 text-gray-400">Coordinate artifact</td>
                </tr>
                <tr className="border-b border-gray-800">
                  <td className="p-3 text-gray-300">Geodesic incompleteness</td>
                  <td className="p-3 text-center text-gray-500">-</td>
                  <td className="p-3 text-center text-yellow-400">Yes</td>
                  <td className="p-3 text-gray-400">Real physics</td>
                </tr>
                <tr className="border-b border-gray-800">
                  <td className="p-3 text-gray-300">Metric distances</td>
                  <td className="p-3 text-center text-green-400">Yes</td>
                  <td className="p-3 text-center text-gray-500">-</td>
                  <td className="p-3 text-gray-400">Coordinate-dependent</td>
                </tr>
                <tr className="border-b border-gray-800">
                  <td className="p-3 text-gray-300">Topological features</td>
                  <td className="p-3 text-center text-gray-500">-</td>
                  <td className="p-3 text-center text-yellow-400">Yes</td>
                  <td className="p-3 text-gray-400">Real structure</td>
                </tr>
              </tbody>
            </table>
          </div>

          <CodeBlock
            language="python"
            code={`class CalculusEnsemble:
    """Test scheme-robustness across calculus families."""

    def __init__(self, calculi):
        # Collection: Classical, GUC, Bigeometric, Curvature-weighted
        self.calculi = calculi

    def is_scheme_robust(self, feature, X):
        """
        Returns True if feature survives all calculi.
        Features that disappear in ANY calculus = artifacts.
        Features that persist in ALL calculi = real physics.
        """
        results = []
        for calc in self.calculi:
            # Does this feature exist in this calculus?
            exists = calc.feature_exists(feature, X)
            results.append(exists)

        # Scheme-robust = present in ALL calculi
        return all(results)

    def classify_singularity(self, singularity, X):
        if self.is_scheme_robust(singularity, X):
            return "REAL PHYSICS - persists across all calculi"
        else:
            return "ARTIFACT - disappears in some calculus"`}
          />
        </div>

        {/* Key Takeaways */}
        <div className="card mb-8">
          <h2 className="text-2xl font-bold mb-4">What We Actually Learned</h2>
          <div className="space-y-4">
            <div className="flex items-start">
              <span className="text-green-400 mr-2 text-xl">1.</span>
              <div>
                <p className="font-semibold text-gray-200">AI hype without falsification is dangerous</p>
                <p className="text-sm text-gray-400">Enthusiasm is not evidence. Run the simulations.</p>
              </div>
            </div>
            <div className="flex items-start">
              <span className="text-green-400 mr-2 text-xl">2.</span>
              <div>
                <p className="font-semibold text-gray-200">Falsification led to real discovery</p>
                <p className="text-sm text-gray-400">By proving claims wrong, we found what was actually right.</p>
              </div>
            </div>
            <div className="flex items-start">
              <span className="text-green-400 mr-2 text-xl">3.</span>
              <div>
                <p className="font-semibold text-gray-200">The methodology is the contribution</p>
                <p className="text-sm text-gray-400">Calculus ensemble analysis as a reality test for singularities.</p>
              </div>
            </div>
            <div className="flex items-start">
              <span className="text-green-400 mr-2 text-xl">4.</span>
              <div>
                <p className="font-semibold text-gray-200">k -&gt; 0 is the answer</p>
                <p className="text-sm text-gray-400">Observations prefer classical calculus, but the TEST is valuable.</p>
              </div>
            </div>
          </div>
        </div>

        {/* The Paradox */}
        <div className="card mb-8 bg-gradient-to-r from-accent-900/30 to-primary-900/30">
          <h2 className="text-2xl font-bold mb-4">The Productive Paradox</h2>
          <p className="text-gray-300 mb-4">
            The original hunch was partially wrong: alternative calculi do not solve
            physics problems by magic. But by rigorously testing that hunch, we developed
            something useful:
          </p>
          <blockquote className="border-l-4 border-primary-500 pl-4 py-2">
            <p className="text-xl text-primary-300 italic">
              A principled way to distinguish real physics from mathematical artifacts.
            </p>
          </blockquote>
          <p className="text-gray-300 mt-4">
            The journey from hype to honesty was the real discovery.
          </p>
        </div>

        {/* Navigation */}
        <div className="flex justify-between items-center mt-12">
          <Link href="/exploration" className="text-gray-400 hover:text-white transition-colors">
            &larr; Back to The Hunch
          </Link>
          <Link href="/validation" className="btn-primary">
            Next: Rigorous Validation &rarr;
          </Link>
        </div>
      </div>
    </div>
  );
}
