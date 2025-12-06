import Link from 'next/link';
import MathBlock from '@/components/MathBlock';
import CodeBlock from '@/components/CodeBlock';

export default function FailuresPage() {
  return (
    <div className="section">
      <div className="mx-auto max-w-4xl">
        <div className="animate-fade-in">
          <p className="text-red-400 font-mono text-sm mb-2">Mathematical History</p>
          <h1 className="text-4xl font-bold mb-4">
            <span className="gradient-text">Failures & Pivots</span>
          </h1>
          <p className="text-xl text-gray-300 mb-8">
            Detailed documentation of claims that failed and the lessons learned
          </p>
        </div>

        {/* Introduction */}
        <div className="card mb-8 animate-slide-up border-l-4 border-red-500">
          <h2 className="text-2xl font-bold mb-4">Why Document Failures?</h2>
          <p className="text-gray-300 mb-4">
            Scientific progress depends on knowing what does NOT work. Publishing only
            successes creates survivorship bias and wastes resources as others repeat
            the same failed experiments. Here we document every significant failure
            in this project.
          </p>
          <blockquote className="border-l-4 border-red-500 pl-4 py-2 my-4">
            <p className="text-lg text-red-300 italic">
              &quot;If it is not falsifiable and you do not run simulations, it is BS.&quot;
            </p>
            <p className="text-sm text-gray-500 mt-2">- The principle that saved this project</p>
          </blockquote>
        </div>

        {/* Failure 1: Bigeometric Singularity Removal */}
        <div className="card mb-8 bg-gradient-to-r from-red-900/10 to-transparent">
          <div className="flex items-center mb-4">
            <span className="text-red-500 text-3xl mr-4">&#x2717;</span>
            <h2 className="text-2xl font-bold">Failure #1: Bigeometric Singularity Removal</h2>
          </div>

          <div className="bg-dark-bg rounded-lg p-4 mb-6 border-l-2 border-yellow-500">
            <h3 className="font-semibold text-yellow-400 mb-2">The Claim (AI-generated)</h3>
            <p className="text-gray-300 italic">
              &quot;The bigeometric derivative of the Ricci scalar is bounded even at r=0,
              suggesting singularities are purely coordinate artifacts. In bigeometric
              calculus, the troublesome infinities of black hole singularities become finite.&quot;
            </p>
          </div>

          <div className="space-y-4 mb-6">
            <h3 className="font-semibold text-gray-300">The Test:</h3>
            <p className="text-sm text-gray-400">
              We computed the bigeometric derivative of a constant function to test basic properties:
            </p>
            <CodeBlock
              language="python"
              code={`# Test: D_BG[constant] should equal 0 for any sensible derivative
def bigeometric_derivative(f, x, h=1e-7):
    """D_BG f(x) = exp(x * f'(x) / f(x))"""
    f_prime = (f(x + h) - f(x - h)) / (2 * h)
    return np.exp(x * f_prime / f(x))

# Test with constant function
constant = lambda x: 5.0
result = bigeometric_derivative(constant, x=2.0)
print(f"D_BG[5] = {result}")  # Expected: 0, Actual: exp(0) = 1.0`}
            />
          </div>

          <div className="bg-dark-bg rounded-lg p-4 mb-6 border-l-2 border-red-500">
            <h3 className="font-semibold text-red-400 mb-2">The Result:</h3>
            <MathBlock
              equation="D_{BG}[c] = \exp\left(\frac{x \cdot 0}{c}\right) = \exp(0) = 1 \neq 0"
              displayMode={true}
            />
            <p className="text-sm text-gray-400 mt-2">
              The bigeometric derivative of any constant is 1, not 0.
            </p>
          </div>

          <div className="bg-dark-bg rounded-lg p-4 mb-6">
            <h3 className="font-semibold text-gray-300 mb-2">Why This Matters:</h3>
            <ul className="text-sm text-gray-400 space-y-2">
              <li>
                <strong className="text-red-400">Breaks linearity:</strong> D_BG[af + bg] is not
                a*D_BG[f] + b*D_BG[g]. The derivative operator is no longer linear.
              </li>
              <li>
                <strong className="text-red-400">Breaks Einstein equations:</strong> GR requires
                linear differential operators. Minkowski space (constant metric) would have
                nonzero &quot;curvature&quot; in bigeometric calculus.
              </li>
              <li>
                <strong className="text-red-400">FRW curvature blows up worse:</strong> The 4D
                Riemann tensor actually has MORE severe behavior, not less.
              </li>
            </ul>
          </div>

          <div className="bg-dark-bg rounded-lg p-4 border border-green-800">
            <h3 className="font-semibold text-green-400 mb-2">Lesson Learned:</h3>
            <p className="text-sm text-gray-300">
              Always test basic properties (linearity, limits, edge cases) before making
              grand claims. The failure of a simple constant-function test invalidated
              the entire &quot;singularity removal&quot; narrative.
            </p>
          </div>
        </div>

        {/* Failure 2: k = -0.7 Dark Energy */}
        <div className="card mb-8 bg-gradient-to-r from-red-900/10 to-transparent">
          <div className="flex items-center mb-4">
            <span className="text-red-500 text-3xl mr-4">&#x2717;</span>
            <h2 className="text-2xl font-bold">Failure #2: k = -0.7 Dark Energy Explanation</h2>
          </div>

          <div className="bg-dark-bg rounded-lg p-4 mb-6 border-l-2 border-yellow-500">
            <h3 className="font-semibold text-yellow-400 mb-2">The Claim (AI-generated)</h3>
            <p className="text-gray-300 italic">
              &quot;Setting the meta-weight k = -0.7 produces an effective equation of state
              that matches dark energy observations. The accelerating expansion could be
              a meta-calculus effect rather than requiring exotic dark energy.&quot;
            </p>
          </div>

          <div className="space-y-4 mb-6">
            <h3 className="font-semibold text-gray-300">The Test:</h3>
            <p className="text-sm text-gray-400">
              We checked k = -0.7 against Big Bang Nucleosynthesis (BBN) constraints:
            </p>
            <CodeBlock
              language="python"
              code={`# BBN constraint: expansion rate during nucleosynthesis
# must match observed light element abundances
# This requires |k| < 0.03 (conservative) or |k| < 0.05 (liberal)

k_proposed = -0.7
k_max_allowed = 0.03  # From BBN analysis

violation_factor = abs(k_proposed) / k_max_allowed
print(f"Violation factor: {violation_factor:.1f}x")  # 23.3x!

# Chi-squared fit to expansion history
# k = -0.7 gives chi2 >> 100 (catastrophic)`}
            />
          </div>

          <div className="bg-dark-bg rounded-lg p-4 mb-6 border-l-2 border-red-500">
            <h3 className="font-semibold text-red-400 mb-2">The Result:</h3>
            <div className="space-y-2">
              <p className="text-sm text-gray-300">
                <strong>BBN violation:</strong> k = -0.7 exceeds allowed bounds by a factor of 23x
              </p>
              <p className="text-sm text-gray-300">
                <strong>Chi-squared:</strong> Fit to supernova data gives chi^2 &gt;&gt; 100 (unacceptable)
              </p>
              <p className="text-sm text-gray-300">
                <strong>Light element abundances:</strong> Would predict wrong helium-4 and deuterium ratios
              </p>
            </div>
          </div>

          <div className="bg-dark-bg rounded-lg p-4 mb-6">
            <h3 className="font-semibold text-gray-300 mb-2">The Physics:</h3>
            <p className="text-sm text-gray-400 mb-2">
              During BBN (~3 minutes after Big Bang), the expansion rate determines how
              much time neutrons have to combine into helium before decaying. A modified
              expansion rate changes the final helium abundance:
            </p>
            <MathBlock
              equation="Y_p \propto \exp\left(-\frac{t_{BBN}}{t_n}\right) \cdot f(H(t))"
              displayMode={true}
            />
            <p className="text-sm text-gray-400">
              where Y_p is the primordial helium mass fraction, t_n is neutron lifetime,
              and H(t) is the Hubble rate modified by k.
            </p>
          </div>

          <div className="bg-dark-bg rounded-lg p-4 border border-green-800">
            <h3 className="font-semibold text-green-400 mb-2">Lesson Learned:</h3>
            <p className="text-sm text-gray-300">
              Any modification to cosmology must satisfy ALL observational constraints,
              not just the one you are trying to explain. BBN constraints are among the
              most stringent and immediately ruled out k = -0.7.
            </p>
          </div>
        </div>

        {/* Failure 3: New Physics Claim */}
        <div className="card mb-8 bg-gradient-to-r from-red-900/10 to-transparent">
          <div className="flex items-center mb-4">
            <span className="text-red-500 text-3xl mr-4">&#x2717;</span>
            <h2 className="text-2xl font-bold">Failure #3: &quot;Alternative Calculus = New Physics&quot;</h2>
          </div>

          <div className="bg-dark-bg rounded-lg p-4 mb-6 border-l-2 border-yellow-500">
            <h3 className="font-semibold text-yellow-400 mb-2">The Claim (AI-generated)</h3>
            <p className="text-gray-300 italic">
              &quot;Using GUC (Generalized Uncertainty Calculus) instead of classical calculus
              provides genuinely new physics. The meta-Lagrangian with t^{'{2k}'} factor represents
              a physical modification, not just a mathematical rewriting.&quot;
            </p>
          </div>

          <div className="space-y-4 mb-6">
            <h3 className="font-semibold text-gray-300">The Analysis:</h3>
            <p className="text-sm text-gray-400 mb-2">
              We examined what the t^{'{2k}'} modification actually means geometrically:
            </p>
            <MathBlock
              equation="\mathcal{L}_{meta} = -\frac{3}{8\pi G} a \cdot t^{2k} \cdot \dot{a}^2 - a^3 \rho(a)"
              displayMode={true}
            />
          </div>

          <div className="bg-dark-bg rounded-lg p-4 mb-6 border-l-2 border-red-500">
            <h3 className="font-semibold text-red-400 mb-2">The Realization:</h3>
            <p className="text-sm text-gray-400 mb-2">
              Consider the coordinate transformation:
            </p>
            <MathBlock
              equation="\tau = \frac{t^{1-k}}{1-k} \quad \Rightarrow \quad dt = t^k \, d\tau"
              displayMode={true}
            />
            <p className="text-sm text-gray-400 mb-2">
              Under this transformation:
            </p>
            <MathBlock
              equation="\dot{a}^2 = \left(\frac{da}{dt}\right)^2 = t^{-2k}\left(\frac{da}{d\tau}\right)^2"
              displayMode={true}
            />
            <p className="text-sm text-gray-400 mb-2">
              So the &quot;modified&quot; Lagrangian becomes:
            </p>
            <MathBlock
              equation="\mathcal{L}_{meta} = -\frac{3}{8\pi G} a \cdot t^{2k} \cdot t^{-2k}\left(\frac{da}{d\tau}\right)^2 = \mathcal{L}_{classical}(\tau)"
              displayMode={true}
            />
          </div>

          <div className="bg-dark-bg rounded-lg p-4 mb-6">
            <h3 className="font-semibold text-gray-300 mb-2">What This Means:</h3>
            <p className="text-sm text-gray-400">
              The t^{'{2k}'} factor is exactly the Jacobian of the coordinate transformation
              tau = t^{'{1-k}'}/(1-k). The &quot;meta-calculus modification&quot; is mathematically
              equivalent to using a different time coordinate. This is not new physics -
              it is the same physics written in different coordinates.
            </p>
          </div>

          <div className="bg-dark-bg rounded-lg p-4 border border-green-800">
            <h3 className="font-semibold text-green-400 mb-2">Lesson Learned:</h3>
            <p className="text-sm text-gray-300">
              Be extremely careful about claiming &quot;new physics&quot; from mathematical
              reformulations. General covariance means physics should not depend on
              coordinate choice. If your &quot;new effect&quot; can be removed by coordinate
              transformation, it is not physical.
            </p>
          </div>
        </div>

        {/* Failure 4: Q3 Quantum Compatibility */}
        <div className="card mb-8 bg-gradient-to-r from-red-900/10 to-transparent">
          <div className="flex items-center mb-4">
            <span className="text-red-500 text-3xl mr-4">&#x2717;</span>
            <h2 className="text-2xl font-bold">Failure #4: Componentwise Meta-Derivatives (Q3)</h2>
          </div>

          <div className="bg-dark-bg rounded-lg p-4 mb-6 border-l-2 border-yellow-500">
            <h3 className="font-semibold text-yellow-400 mb-2">The Hypothesis</h3>
            <p className="text-gray-300 italic">
              &quot;If global meta-time reparametrization (Q1, Q2) preserves unitarity, perhaps
              we can apply meta-calculus componentwise to wave function components,
              giving each quantum amplitude its own effective time evolution.&quot;
            </p>
          </div>

          <div className="space-y-4 mb-6">
            <h3 className="font-semibold text-gray-300">The Test:</h3>
            <CodeBlock
              language="python"
              code={`# Q3: Componentwise meta-derivative on Schrodinger equation
# Each psi_i evolves with its own generator alpha_i

def test_q3_unitarity(H, psi0, num_steps=100, dt=0.01):
    """
    Test if componentwise meta-derivatives preserve norm.
    """
    psi = psi0.copy()
    norms = [np.linalg.norm(psi)]

    for step in range(num_steps):
        # Each component gets different effective dt
        effective_dt = np.array([
            dt * alpha_derivative(i, step * dt)
            for i in range(len(psi))
        ])

        # RK4 step with component-dependent time
        dpsi = -1j * H @ psi
        for i in range(len(psi)):
            psi[i] += effective_dt[i] * dpsi[i]

        norms.append(np.linalg.norm(psi))

    return norms

# Result: norm drifts by ~65% over 100 steps`}
            />
          </div>

          <div className="bg-dark-bg rounded-lg p-4 mb-6 border-l-2 border-red-500">
            <h3 className="font-semibold text-red-400 mb-2">The Result:</h3>
            <div className="grid gap-4 md:grid-cols-2">
              <div className="bg-dark-bg rounded-lg p-3 border border-green-700">
                <p className="text-sm text-green-400 font-semibold">Q0-Q2 (Global)</p>
                <p className="text-xs text-gray-400">Norm drift: &lt; 1%</p>
                <p className="text-xs text-gray-400">Status: SAFE</p>
              </div>
              <div className="bg-dark-bg rounded-lg p-3 border border-red-700">
                <p className="text-sm text-red-400 font-semibold">Q3 (Componentwise)</p>
                <p className="text-xs text-gray-400">Norm drift: ~65%</p>
                <p className="text-xs text-gray-400">Status: BREAKS UNITARITY</p>
              </div>
            </div>
          </div>

          <div className="bg-dark-bg rounded-lg p-4 mb-6">
            <h3 className="font-semibold text-gray-300 mb-2">Why It Fails:</h3>
            <p className="text-sm text-gray-400 mb-2">
              Unitarity requires:
            </p>
            <MathBlock
              equation="\frac{d}{dt}\langle\psi|\psi\rangle = 0"
              displayMode={true}
            />
            <p className="text-sm text-gray-400 mb-2">
              When each component has different effective time, the evolution operator
              is no longer unitary:
            </p>
            <MathBlock
              equation="U_{Q3}^\dagger U_{Q3} \neq I"
              displayMode={true}
            />
          </div>

          <div className="bg-dark-bg rounded-lg p-4 border border-green-800">
            <h3 className="font-semibold text-green-400 mb-2">Lesson Learned:</h3>
            <p className="text-sm text-gray-300">
              Quantum mechanics has rigid structural requirements. You can reparametrize
              time globally (Q1-Q2) but not locally on individual components (Q3).
              The Q0-Q2 hierarchy identifies the boundary of safe modifications.
            </p>
          </div>
        </div>

        {/* The Pivots Section */}
        <div className="card mb-8 bg-gradient-to-r from-yellow-900/20 to-accent-900/20">
          <h2 className="text-2xl font-bold mb-4">The Pivots</h2>
          <p className="text-gray-300 mb-6">
            Each failure forced a pivot in the research direction. Here are the key turning points:
          </p>

          <div className="space-y-6">
            <div className="border-l-4 border-yellow-500 pl-4">
              <h3 className="font-semibold text-yellow-400 mb-2">Pivot #1: From &quot;Right Calculus&quot; to &quot;Calculus Ensemble&quot;</h3>
              <p className="text-sm text-gray-400 mb-2">
                <strong>Before:</strong> Looking for the &quot;correct&quot; calculus that makes problems disappear.
              </p>
              <p className="text-sm text-gray-400">
                <strong>After:</strong> Using families of calculi to test which features are real vs artifacts.
              </p>
            </div>

            <div className="border-l-4 border-yellow-500 pl-4">
              <h3 className="font-semibold text-yellow-400 mb-2">Pivot #2: From &quot;New Physics&quot; to &quot;Scheme-Robustness Test&quot;</h3>
              <p className="text-sm text-gray-400 mb-2">
                <strong>Before:</strong> Alternative calculi provide genuinely new physics.
              </p>
              <p className="text-sm text-gray-400">
                <strong>After:</strong> Alternative calculi are a diagnostic tool - if something survives
                ALL calculi, it is likely real physics.
              </p>
            </div>

            <div className="border-l-4 border-yellow-500 pl-4">
              <h3 className="font-semibold text-yellow-400 mb-2">Pivot #3: From &quot;Parameter Fitting&quot; to &quot;Classical Limit&quot;</h3>
              <p className="text-sm text-gray-400 mb-2">
                <strong>Before:</strong> Searching for k, s values that explain dark energy.
              </p>
              <p className="text-sm text-gray-400">
                <strong>After:</strong> Accepting that k -&gt; 0, s -&gt; 0 (classical calculus) is
                observationally preferred, but the methodology is the contribution.
              </p>
            </div>

            <div className="border-l-4 border-yellow-500 pl-4">
              <h3 className="font-semibold text-yellow-400 mb-2">Pivot #4: From &quot;Local&quot; to &quot;Global&quot; Modifications</h3>
              <p className="text-sm text-gray-400 mb-2">
                <strong>Before:</strong> Componentwise meta-derivatives might be interesting.
              </p>
              <p className="text-sm text-gray-400">
                <strong>After:</strong> Only global/bulk modifications are compatible with quantum mechanics.
                Q3 is a hard boundary.
              </p>
            </div>
          </div>
        </div>

        {/* Meta-Lessons */}
        <div className="card mb-8">
          <h2 className="text-2xl font-bold mb-4">Meta-Lessons for Research</h2>

          <div className="space-y-4">
            <div className="flex items-start">
              <span className="text-primary-400 mr-3 text-xl">1.</span>
              <div>
                <p className="font-semibold text-gray-200">AI enthusiasm requires falsification</p>
                <p className="text-sm text-gray-400">
                  AI can generate plausible-sounding claims very quickly. Each claim must be
                  tested against simple sanity checks before investing time in development.
                </p>
              </div>
            </div>

            <div className="flex items-start">
              <span className="text-primary-400 mr-3 text-xl">2.</span>
              <div>
                <p className="font-semibold text-gray-200">Basic tests first</p>
                <p className="text-sm text-gray-400">
                  The bigeometric failure was caught by testing D_BG[constant]. Always test
                  edge cases (constants, limits, simple functions) before complex applications.
                </p>
              </div>
            </div>

            <div className="flex items-start">
              <span className="text-primary-400 mr-3 text-xl">3.</span>
              <div>
                <p className="font-semibold text-gray-200">All constraints matter</p>
                <p className="text-sm text-gray-400">
                  k = -0.7 might explain dark energy but violates BBN. Any new theory must
                  satisfy ALL observational constraints simultaneously.
                </p>
              </div>
            </div>

            <div className="flex items-start">
              <span className="text-primary-400 mr-3 text-xl">4.</span>
              <div>
                <p className="font-semibold text-gray-200">Coordinate artifacts are real dangers</p>
                <p className="text-sm text-gray-400">
                  Many &quot;new physics&quot; claims are coordinate artifacts in disguise. Always check
                  if your effect can be removed by change of variables.
                </p>
              </div>
            </div>

            <div className="flex items-start">
              <span className="text-primary-400 mr-3 text-xl">5.</span>
              <div>
                <p className="font-semibold text-gray-200">Failures are information</p>
                <p className="text-sm text-gray-400">
                  Each failure narrowed the search space. By proving what does NOT work, we
                  identified what might. The methodology emerged from the wreckage.
                </p>
              </div>
            </div>
          </div>
        </div>

        {/* Navigation */}
        <div className="flex justify-between items-center mt-12">
          <Link href="/math-history/derivations" className="text-gray-400 hover:text-white transition-colors">
            &larr; Back to Derivations
          </Link>
          <Link href="/math-history/experiments" className="btn-primary">
            Next: Experiments &rarr;
          </Link>
        </div>
      </div>
    </div>
  );
}
