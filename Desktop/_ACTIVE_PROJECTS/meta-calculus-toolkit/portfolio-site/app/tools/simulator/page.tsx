import dynamicImport from 'next/dynamic';
import Link from 'next/link';

// Force dynamic rendering to prevent SSG issues with client components
export const dynamic = 'force-dynamic';

// Dynamic imports for heavy visualization components
const ParetoVisualizer = dynamicImport(() => import('@/components/ParetoVisualizer'), {
  ssr: false,
  loading: () => <div className="h-96 bg-dark-surface rounded-lg animate-pulse flex items-center justify-center text-gray-500">Loading Pareto Visualizer...</div>
});

const ParameterExplorer = dynamicImport(() => import('@/components/ParameterExplorer'), {
  ssr: false,
  loading: () => <div className="h-96 bg-dark-surface rounded-lg animate-pulse flex items-center justify-center text-gray-500">Loading Parameter Explorer...</div>
});

const SearchSpaceVisualizer = dynamicImport(() => import('@/components/SearchSpaceVisualizer'), {
  ssr: false,
  loading: () => <div className="h-96 bg-dark-surface rounded-lg animate-pulse flex items-center justify-center text-gray-500">Loading Search Space Visualizer...</div>
});

const QuantumCompatibilityVisualizer = dynamicImport(() => import('@/components/QuantumCompatibilityVisualizer'), {
  ssr: false,
  loading: () => <div className="h-96 bg-dark-surface rounded-lg animate-pulse flex items-center justify-center text-gray-500">Loading Quantum Compatibility Visualizer...</div>
});

const QuantumDiffusionVisualizer = dynamicImport(() => import('@/components/QuantumDiffusionVisualizer'), {
  ssr: false,
  loading: () => <div className="h-96 bg-dark-surface rounded-lg animate-pulse flex items-center justify-center text-gray-500">Loading Quantum Diffusion Visualizer...</div>
});

export default function SimulatorPage() {
  return (
    <div className="section">
      <div className="mx-auto max-w-7xl">
        <div className="animate-fade-in">
          <p className="text-primary-400 font-mono text-sm mb-2">Interactive Tools</p>
          <h1 className="text-4xl font-bold mb-4">
            <span className="gradient-text">Meta-Calculus Simulator</span>
          </h1>
          <p className="text-xl text-gray-300 mb-8">
            Explore the parameter space, visualize Pareto frontiers, and understand how different calculus configurations affect cosmological observables.
          </p>
        </div>

        {/* Quick Explanation */}
        <div className="card mb-8 border-l-4 border-primary-500">
          <h2 className="text-xl font-bold mb-3">How to Use These Simulators</h2>
          <div className="grid md:grid-cols-2 gap-4 text-sm text-gray-300">
            <div>
              <h3 className="text-primary-400 font-semibold mb-2">Parameters You Can Control:</h3>
              <ul className="space-y-1">
                <li><strong>n</strong> - Expansion exponent (how fast the universe expands)</li>
                <li><strong>s</strong> - Scale parameter (deviation from standard scaling)</li>
                <li><strong>k</strong> - Calculus index (0 = classical calculus)</li>
                <li><strong>w</strong> - Equation of state (type of cosmic fluid)</li>
              </ul>
            </div>
            <div>
              <h3 className="text-accent-400 font-semibold mb-2">What You Are Minimizing:</h3>
              <ul className="space-y-1">
                <li><strong>Chi-squared</strong> - How well config matches observations</li>
                <li><strong>Non-robustness</strong> - Sensitivity to calculus choice</li>
                <li><strong>Constraint tension</strong> - Proximity to BBN/CMB limits</li>
              </ul>
            </div>
          </div>
        </div>

        {/* Section 1: Pareto Frontier */}
        <section className="mb-12">
          <div className="flex items-center gap-3 mb-4">
            <span className="px-3 py-1 bg-primary-600/20 text-primary-400 text-sm rounded-full font-mono">01</span>
            <h2 className="text-2xl font-bold">Pareto Frontier Comparison</h2>
          </div>
          <p className="text-gray-400 mb-6">
            Compare solutions found by two independent optimizers: <span className="text-primary-400">pymoo (NSGA-II)</span> for
            fast local exploration and <span className="text-accent-400">Global MOO</span> for broader constraint-aware search.
            Rotate the 3D plot to see how solutions distribute across objective space.
          </p>
          <div className="card">
            <ParetoVisualizer />
          </div>
        </section>

        {/* Section 2: Parameter Explorer */}
        <section className="mb-12">
          <div className="flex items-center gap-3 mb-4">
            <span className="px-3 py-1 bg-accent-600/20 text-accent-400 text-sm rounded-full font-mono">02</span>
            <h2 className="text-2xl font-bold">Interactive Parameter Explorer</h2>
          </div>
          <p className="text-gray-400 mb-6">
            Drag the sliders to see how changing each parameter affects the objective landscape in real-time.
            The 3D surface shows the combined objective function. Lower values (darker blue) indicate better configurations.
            The diamond marker shows your current configuration.
          </p>
          <div className="card">
            <ParameterExplorer />
          </div>
        </section>

        {/* Section 3: Search Space Heatmap */}
        <section className="mb-12">
          <div className="flex items-center gap-3 mb-4">
            <span className="px-3 py-1 bg-green-600/20 text-green-400 text-sm rounded-full font-mono">03</span>
            <h2 className="text-2xl font-bold">Search Space Visualization</h2>
          </div>
          <p className="text-gray-400 mb-6">
            A 2D heatmap view of the (s, k) parameter space. Watch how the two optimizers explore
            the landscape differently. The dashed lines show physical constraints from Big Bang Nucleosynthesis (BBN)
            and Cosmic Microwave Background (CMB) observations.
          </p>
          <div className="card">
            <SearchSpaceVisualizer />
          </div>
        </section>

        {/* Section 4: Meta-Quantum Compatibility */}
        <section className="mb-12">
          <div className="flex items-center gap-3 mb-4">
            <span className="px-3 py-1 bg-purple-600/20 text-purple-400 text-sm rounded-full font-mono">04</span>
            <h2 className="text-2xl font-bold">Meta-Quantum Compatibility Explorer</h2>
          </div>
          <p className="text-gray-400 mb-6">
            Test how far meta-calculus can be pushed before quantum mechanics pushes back.
            We evolve a random finite-dimensional quantum state under the standard Schrodinger equation
            and various <span className="text-purple-400">meta-time derivative</span> variants, measuring
            unitarity (norm preservation) and deviation from the reference trajectory.
          </p>
          <div className="card mb-4 border-l-4 border-purple-500/50">
            <h3 className="text-lg font-semibold mb-2">The Experiment</h3>
            <ul className="text-sm text-gray-400 space-y-1">
              <li>Generate a random Hermitian Hamiltonian H and initial state |psi0&gt;</li>
              <li>Evolve under standard Schrodinger: i*hbar*d|psi&gt;/dt = H|psi&gt;</li>
              <li>Compare against meta-derivative variants: clock reparametrizations, global norm-dependent, componentwise</li>
              <li>Track ||psi(t)||^2 drift (should stay 1) and distance to standard trajectory</li>
            </ul>
          </div>
          <div className="card">
            <QuantumCompatibilityVisualizer />
          </div>
        </section>

        {/* Section 5: Multi-Calculus Quantum Diffusion */}
        <section className="mb-12">
          <div className="flex items-center gap-3 mb-4">
            <span className="px-3 py-1 bg-pink-600/20 text-pink-400 text-sm rounded-full font-mono">05</span>
            <h2 className="text-2xl font-bold">Multi-Calculus Quantum State Diffusion</h2>
          </div>
          <p className="text-gray-400 mb-6">
            A geometric view of quantum state space: we interpret points on the 2-simplex as
            <span className="text-pink-400"> diagonal qutrit density matrices</span> rho = diag(p0, p1, p2),
            then run multi-calculus diffusion to find structure that survives all geometric embeddings.
          </p>
          <div className="card mb-4 border-l-4 border-pink-500/50">
            <h3 className="text-lg font-semibold mb-2">Quantum Interpretation</h3>
            <div className="grid md:grid-cols-2 gap-4 text-sm text-gray-400">
              <div>
                <h4 className="text-pink-400 font-semibold mb-1">State Space Geometry</h4>
                <ul className="space-y-1">
                  <li>Vertices = pure states |0&gt;&lt;0|, |1&gt;&lt;1|, |2&gt;&lt;2|</li>
                  <li>Centroid = maximally mixed state I/3</li>
                  <li>Purity Tr(rho^2): 1/3 (mixed) to 1 (pure)</li>
                </ul>
              </div>
              <div>
                <h4 className="text-pink-400 font-semibold mb-1">Calculus Embeddings</h4>
                <ul className="space-y-1">
                  <li>Classical: phi(x) = x (Euclidean)</li>
                  <li>Log: phi(x) = log(x) (info-geometric)</li>
                  <li>Power: phi(x) = sqrt(x) (Hellinger)</li>
                  <li>Curvature: phi(x) = 2*arcsin(sqrt(x)) (Bures)</li>
                </ul>
              </div>
            </div>
          </div>
          <div className="card">
            <QuantumDiffusionVisualizer />
          </div>
        </section>

        {/* Key Insights */}
        <section className="mb-12">
          <h2 className="text-2xl font-bold mb-6">Key Insights from the Simulations</h2>
          <div className="grid md:grid-cols-3 gap-6">
            <div className="card bg-gradient-to-br from-primary-900/30 to-transparent border-primary-500/30">
              <div className="text-4xl font-bold text-primary-400 mb-2">k = 0</div>
              <h3 className="font-semibold text-white mb-2">Classical Calculus Preferred</h3>
              <p className="text-sm text-gray-400">
                Both optimizers converge toward k=0, suggesting that standard Newtonian calculus
                is observationally preferred. Non-classical calculi (k != 0) worsen chi-squared fit.
              </p>
            </div>
            <div className="card bg-gradient-to-br from-accent-900/30 to-transparent border-accent-500/30">
              <div className="text-4xl font-bold text-accent-400 mb-2">s = 0</div>
              <h3 className="font-semibold text-white mb-2">Scale Invariance</h3>
              <p className="text-sm text-gray-400">
                The optimal solutions cluster near s=0, indicating the meta-Friedmann equation
                reduces to standard Friedmann when scale modifications are minimal.
              </p>
            </div>
            <div className="card bg-gradient-to-br from-green-900/30 to-transparent border-green-500/30">
              <div className="text-4xl font-bold text-green-400 mb-2">100%</div>
              <h3 className="font-semibold text-white mb-2">Scheme Robustness</h3>
              <p className="text-sm text-gray-400">
                The classical limit (k=0, s=0) achieves perfect scheme robustness - the physical
                predictions are invariant across all calculus choices.
              </p>
            </div>
          </div>

          {/* Quantum insights */}
          <h3 className="text-xl font-semibold mt-8 mb-4">Quantum Extensions</h3>
          <div className="grid md:grid-cols-3 gap-6">
            <div className="card bg-gradient-to-br from-purple-900/30 to-transparent border-purple-500/30">
              <div className="text-4xl font-bold text-purple-400 mb-2">Q0-Q2</div>
              <h3 className="font-semibold text-white mb-2">Safe Meta-Derivatives</h3>
              <p className="text-sm text-gray-400">
                Clock reparametrizations (Q1) and global norm-dependent (Q2) families
                preserve unitarity. Componentwise (Q3) breaks norm conservation.
              </p>
            </div>
            <div className="card bg-gradient-to-br from-pink-900/30 to-transparent border-pink-500/30">
              <div className="text-4xl font-bold text-pink-400 mb-2">+15%</div>
              <h3 className="font-semibold text-white mb-2">Gap Amplification</h3>
              <p className="text-sm text-gray-400">
                Multi-calculus diffusion on qutrit state space achieves higher effective
                spectral gap than any single calculus embedding alone.
              </p>
            </div>
            <div className="card bg-gradient-to-br from-blue-900/30 to-transparent border-blue-500/30">
              <div className="text-3xl font-bold text-blue-400 mb-2">Unified</div>
              <h3 className="font-semibold text-white mb-2">Cross-Domain Pattern</h3>
              <p className="text-sm text-gray-400">
                The same principle applies: global/bulk modifications are safe,
                componentwise/local modifications break fundamental constraints.
              </p>
            </div>
          </div>
        </section>

        {/* Mathematical Note */}
        <div className="card mb-8 bg-dark-bg border-l-4 border-yellow-500">
          <h3 className="font-semibold text-yellow-400 mb-2">Technical Note</h3>
          <p className="text-sm text-gray-400 mb-2">
            <strong>Cosmology (01-03):</strong> These visualizations use synthetic data that mimics the behavior of the actual optimizers.
            The real pymoo and Global MOO runs were performed offline with the full meta-Friedmann solver.
            The patterns shown (convergence to k=0, constraint boundaries, Pareto structure) accurately
            represent the findings from the validation study.
          </p>
          <p className="text-sm text-gray-400">
            <strong>Quantum (04-05):</strong> The meta-quantum compatibility explorer runs simplified numerical
            experiments matching the Python module in <code className="text-purple-400">meta_calculus/quantum/</code>.
            The diffusion visualizer demonstrates the same spectral gap amplification effect seen in
            the full multi-calculus framework.
          </p>
        </div>

        {/* Navigation */}
        <div className="flex justify-between items-center mt-12">
          <Link href="/validation" className="text-gray-400 hover:text-white transition-colors">
            &larr; Back to Validation
          </Link>
          <Link href="/results" className="btn-primary">
            See Full Results &rarr;
          </Link>
        </div>
      </div>
    </div>
  );
}
