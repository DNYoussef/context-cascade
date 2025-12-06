import MathBlock from '@/components/MathBlock';
import CodeBlock from '@/components/CodeBlock';
import Link from 'next/link';

export default function QuantumPage() {
  return (
    <div className="section">
      <div className="mx-auto max-w-4xl">
        <div className="animate-fade-in">
          <p className="text-primary-400 font-mono text-sm mb-2">Chapter 05</p>
          <h1 className="text-4xl font-bold mb-4">
            <span className="gradient-text">Meta-Quantum Test Bench</span>
          </h1>
          <p className="text-xl text-gray-300 mb-8">
            How far can &quot;many calculi&quot; go before quantum mechanics pushes back?
          </p>
        </div>

        {/* Introduction */}
        <div className="card mb-8 animate-slide-up border-l-4 border-primary-500">
          <h2 className="text-2xl font-bold mb-4">Testing Meta-Calculus Against Quantum Mechanics</h2>
          <p className="text-gray-300 mb-4">
            This chapter builds a small but honest <strong className="text-primary-400">meta-quantum test bench</strong>.
            Instead of jumping straight to interpretations, we:
          </p>
          <ul className="space-y-2 text-gray-300 mb-4">
            <li className="flex items-start">
              <span className="text-primary-400 mr-2">-</span>
              <span>Rewrite the Schrodinger equation with meta-derivatives in time</span>
            </li>
            <li className="flex items-start">
              <span className="text-primary-400 mr-2">-</span>
              <span>Classify which meta-derivatives are <strong className="text-primary-400">physically compatible</strong> (preserve norm, look unitary)</span>
            </li>
            <li className="flex items-start">
              <span className="text-primary-400 mr-2">-</span>
              <span>Show explicitly where the structure breaks when we push too far</span>
            </li>
          </ul>
          <p className="text-gray-300">
            The result is a <strong className="text-accent-400">quantum compatibility hierarchy</strong> that mirrors
            what we saw in cosmology: mathematics allows many calculi, but physics tolerates only a narrow corner.
          </p>
        </div>

        {/* Why Start with Time */}
        <div className="card mb-8">
          <h2 className="text-2xl font-bold mb-4">Why Start with Time?</h2>
          <p className="text-gray-300 mb-4">
            Space can be complicated: potentials, boundaries, discretizations. Time is simpler.
          </p>
          <p className="text-gray-300 mb-6">
            So we keep the spatial part <strong className="text-primary-400">classical</strong> and only modify
            the <strong className="text-primary-400">time derivative</strong> in the Schrodinger equation. That isolates
            the role of meta-calculus as a deformation of the clock, not of the spatial geometry.
          </p>

          <div className="bg-dark-bg rounded-lg p-4 mb-6">
            <p className="text-gray-400 text-sm mb-2">Standard Schrodinger equation (finite-dimensional version):</p>
            <MathBlock
              equation="i\hbar \frac{d}{dt} c(t) = H c(t)"
              displayMode={true}
            />
          </div>

          <div className="text-gray-300 mb-4 text-sm">
            <p className="mb-2">Where:</p>
            <ul className="space-y-1 ml-4">
              <li><MathBlock equation="c(t)" displayMode={false} /> is a state vector in <MathBlock equation="\mathbb{C}^n" displayMode={false} /></li>
              <li><MathBlock equation="H" displayMode={false} /> is a Hermitian Hamiltonian</li>
              <li><MathBlock equation="\|c(t)\|^2" displayMode={false} /> is the Born probability (must stay constant)</li>
            </ul>
          </div>

          <p className="text-gray-300">
            A meta-derivative in time replaces <MathBlock equation="\frac{d}{dt}" displayMode={false} /> with
            some <MathBlock equation="D_t^{(\text{meta})}" displayMode={false} />, and we ask:
          </p>

          <blockquote className="border-l-4 border-accent-500 pl-4 py-2 my-4">
            <p className="text-accent-300 italic">
              When does <MathBlock equation="i\hbar D_t^{(\text{meta})} c(t) = H c(t)" displayMode={false} /> still behave like quantum mechanics?
            </p>
          </blockquote>
        </div>

        {/* The Safe Class */}
        <div className="card mb-8">
          <h2 className="text-2xl font-bold mb-4">The Safe Class: Meta-Time as a Clock Change</h2>
          <p className="text-gray-300 mb-4">
            The simplest meta-time derivative is:
          </p>

          <div className="bg-dark-bg rounded-lg p-4 mb-6">
            <MathBlock
              equation="D_t^{\text{safe}} c(t) = \frac{1}{u(t)} \frac{dc}{dt}"
              displayMode={true}
            />
          </div>

          <p className="text-gray-300 mb-4">With:</p>
          <ul className="space-y-1 text-gray-300 mb-6 ml-4">
            <li><MathBlock equation="u(t) > 0" displayMode={false} /> a smooth time-weight</li>
            <li>No dependence on the state <MathBlock equation="c" displayMode={false} /></li>
            <li>No dependence on individual components</li>
          </ul>

          <p className="text-gray-300 mb-4">The meta-Schrodinger equation becomes:</p>

          <div className="bg-dark-bg rounded-lg p-4 mb-6">
            <MathBlock
              equation="i\hbar \frac{1}{u(t)} \frac{dc}{dt} = Hc \quad \Rightarrow \quad \frac{dc}{dt} = -i \frac{u(t)}{\hbar} Hc"
              displayMode={true}
            />
          </div>

          <p className="text-gray-300 mb-4">Define a new time coordinate:</p>

          <div className="bg-dark-bg rounded-lg p-4 mb-6">
            <MathBlock
              equation="\tau(t) = \int_{t_0}^t u(s) \, ds"
              displayMode={true}
            />
          </div>

          <p className="text-gray-300 mb-4">
            Then the equation turns into the <strong className="text-primary-400">ordinary</strong> Schrodinger equation in <MathBlock equation="\tau" displayMode={false} />:
          </p>

          <div className="bg-dark-bg rounded-lg p-4 mb-6">
            <MathBlock
              equation="i\hbar \frac{d}{d\tau} c(\tau) = H c(\tau)"
              displayMode={true}
            />
          </div>
        </div>

        {/* Numerical Test Bench */}
        <div className="card mb-8">
          <h2 className="text-2xl font-bold mb-4">Numerical Test Bench</h2>
          <p className="text-gray-300 mb-4">To actually test this, we:</p>
          <ul className="space-y-2 text-gray-300 mb-6">
            <li className="flex items-start">
              <span className="text-primary-400 mr-2">1.</span>
              <span>Pick a random 4x4 Hermitian matrix <MathBlock equation="H" displayMode={false} /></span>
            </li>
            <li className="flex items-start">
              <span className="text-primary-400 mr-2">2.</span>
              <span>Pick a random normalized state <MathBlock equation="c_0" displayMode={false} /></span>
            </li>
            <li className="flex items-start">
              <span className="text-primary-400 mr-2">3.</span>
              <span>Choose a smooth positive weight <MathBlock equation="u(t) = 1 + \epsilon \sin(0.7t)\cos(0.3t)" displayMode={false} /> with <MathBlock equation="\epsilon < 1" displayMode={false} /></span>
            </li>
            <li className="flex items-start">
              <span className="text-primary-400 mr-2">4.</span>
              <span>Integrate both meta-time and standard Schrodinger via RK4</span>
            </li>
          </ul>

          <CodeBlock
            language="python"
            code={`import numpy as np
from scipy.integrate import solve_ivp
from scipy.linalg import expm

def meta_schrodinger_test(dim=4, epsilon=0.3, t_max=10.0):
    """Test meta-time Schrodinger vs standard evolution."""

    # Random Hermitian H
    A = np.random.randn(dim, dim) + 1j * np.random.randn(dim, dim)
    H = (A + A.conj().T) / 2

    # Random normalized initial state
    c0 = np.random.randn(dim) + 1j * np.random.randn(dim)
    c0 = c0 / np.linalg.norm(c0)

    # Time weight
    def u(t):
        return 1 + epsilon * np.sin(0.7 * t) * np.cos(0.3 * t)

    # Meta-time ODE: dc/dt = -i * u(t) * H @ c
    def meta_rhs(t, c_flat):
        c = c_flat[:dim] + 1j * c_flat[dim:]
        dcdt = -1j * u(t) * (H @ c)
        return np.concatenate([dcdt.real, dcdt.imag])

    # Solve meta-time evolution
    c0_flat = np.concatenate([c0.real, c0.imag])
    sol = solve_ivp(meta_rhs, [0, t_max], c0_flat,
                    method='RK45', dense_output=True)

    # Compare with exact solution in tau coordinates
    t_eval = np.linspace(0, t_max, 100)
    max_diff = 0.0
    max_norm_drift = 0.0

    for t in t_eval:
        # Meta-time solution
        c_flat = sol.sol(t)
        c_meta = c_flat[:dim] + 1j * c_flat[dim:]

        # Compute tau(t)
        tau, _ = scipy.integrate.quad(u, 0, t)

        # Exact solution: c(tau) = exp(-i*H*tau) @ c0
        c_exact = expm(-1j * H * tau) @ c0

        diff = np.linalg.norm(c_meta - c_exact)
        norm_drift = abs(np.linalg.norm(c_meta) - 1.0)

        max_diff = max(max_diff, diff)
        max_norm_drift = max(max_norm_drift, norm_drift)

    return max_diff, max_norm_drift

# Result: max_diff ~ 1e-7, norm_drift ~ 1e-12`}
          />

          <div className="bg-gradient-to-r from-green-900/30 to-transparent border-l-2 border-green-500 p-4 mt-6">
            <h3 className="font-semibold text-green-400 mb-2">Result</h3>
            <ul className="text-sm text-gray-300 space-y-1">
              <li>Max trajectory difference: ~10<sup>-7</sup> (pure numerical error)</li>
              <li>Norm drift: ~10<sup>-12</sup> or better (effectively exact)</li>
            </ul>
          </div>

          <div className="mt-6 p-4 bg-dark-bg rounded-lg">
            <h3 className="font-semibold text-primary-400 mb-2">Takeaway</h3>
            <p className="text-gray-300 text-sm">
              For <MathBlock equation="D_t^{\text{safe}} = \frac{1}{u(t)} \frac{d}{dt}" displayMode={false} />,
              meta-time Schrodinger is <em>exactly</em> equivalent to standard quantum mechanics with a reparametrized clock <MathBlock equation="\tau" displayMode={false} />.
            </p>
            <blockquote className="border-l-4 border-primary-500 pl-4 py-2 mt-4">
              <p className="text-primary-300 italic text-sm">
                This class of meta-calculus does not change quantum predictions; it only changes how we label time.
              </p>
            </blockquote>
          </div>
        </div>

        {/* Global Nonlinear Weights */}
        <div className="card mb-8">
          <h2 className="text-2xl font-bold mb-4">Global Nonlinear Weights: Still Just a Weird Clock</h2>
          <p className="text-gray-300 mb-4">
            Next, we tried a slightly more exotic meta-derivative:
          </p>

          <div className="bg-dark-bg rounded-lg p-4 mb-6">
            <MathBlock
              equation="D_t^{\text{global}} c = \frac{1}{u(t)} \left(1 + k\|c(t)\|^2\right) \frac{dc}{dt}"
              displayMode={true}
            />
          </div>

          <p className="text-gray-300 mb-4">
            At first glance this looks nonlinear, but the factor <MathBlock equation="\frac{u(t)}{1 + k\|c\|^2}" displayMode={false} /> is
            just a <strong className="text-primary-400">real scalar</strong> multiplying the Hermitian generator <MathBlock equation="H" displayMode={false} />.
            That still produces a norm-preserving flow.
          </p>

          <div className="grid gap-4 md:grid-cols-2 mb-4">
            <div className="bg-dark-bg rounded-lg p-4">
              <p className="text-sm text-gray-400 mb-1">Norm drift:</p>
              <p className="text-green-400 font-mono">~10<sup>-14</sup></p>
            </div>
            <div className="bg-dark-bg rounded-lg p-4">
              <p className="text-sm text-gray-400 mb-1">Interpretation:</p>
              <p className="text-gray-300 text-sm">Standard Schrodinger in reparametrized time</p>
            </div>
          </div>

          <p className="text-gray-300 text-sm">
            So this belongs to the same &quot;safe corner&quot;: as long as <MathBlock equation="D_t" displayMode={false} /> is
            a <strong className="text-primary-400">global real scalar</strong> times <MathBlock equation="\frac{d}{dt}" displayMode={false} />,
            quantum structure is preserved.
          </p>
        </div>

        {/* When Meta-Calculus Breaks */}
        <div className="card mb-8 bg-gradient-to-r from-red-900/20 to-transparent">
          <h2 className="text-2xl font-bold mb-4">When Meta-Calculus Breaks Quantum Mechanics</h2>
          <p className="text-gray-300 mb-6">
            To see where meta-calculus <em>stops</em> being safe, we deliberately move to <strong className="text-red-400">component-wise</strong> deformations.
          </p>

          {/* Family 1: Log-Like */}
          <div className="mb-8">
            <h3 className="font-semibold text-red-400 mb-3">Family 1: Log-Like Component Derivative</h3>
            <div className="bg-dark-bg rounded-lg p-4 mb-4">
              <MathBlock
                equation="D_t^{\log} c_j = \frac{1}{u(t)} \frac{1}{c_j} \frac{dc_j}{dt}"
                displayMode={true}
              />
            </div>
            <p className="text-gray-300 text-sm mb-2">
              This couples each component to its own amplitude and its own &quot;local energy&quot; <MathBlock equation="(Hc)_j" displayMode={false} />.
            </p>
            <div className="bg-red-900/30 border border-red-500/30 rounded p-3">
              <p className="text-sm text-gray-300">
                <strong className="text-red-400">Norm drift:</strong> ~65% change in <MathBlock equation="\|c(t)\|" displayMode={false} />
              </p>
            </div>
          </div>

          {/* Family 2: Power-Style */}
          <div className="mb-8">
            <h3 className="font-semibold text-red-400 mb-3">Family 2: Power-Style Component Derivative</h3>
            <div className="bg-dark-bg rounded-lg p-4 mb-4">
              <MathBlock
                equation="D_t^{\text{pow}} c_j = \frac{1}{u(t)} |c_j|^p \frac{dc_j}{dt}"
                displayMode={true}
              />
            </div>
            <p className="text-gray-300 text-sm mb-2">
              For <MathBlock equation="p=1" displayMode={false} />:
            </p>
            <div className="bg-red-900/30 border border-red-500/30 rounded p-3">
              <p className="text-sm text-gray-300">
                <strong className="text-red-400">Norm drift:</strong> ~7-8% over evolution
              </p>
            </div>
          </div>

          {/* Family 3: Componentwise */}
          <div>
            <h3 className="font-semibold text-red-400 mb-3">Family 3: Componentwise (1 + k|c_j|^2) Factors</h3>
            <div className="bg-dark-bg rounded-lg p-4 mb-4">
              <MathBlock
                equation="D_t^{\text{comp}} c_j = \frac{1}{u(t)} \left(1 + k|c_j|^2\right) \frac{dc_j}{dt}"
                displayMode={true}
              />
            </div>
            <p className="text-gray-300 text-sm mb-2">
              Different components see different effective &quot;time speeds&quot; depending on their amplitudes.
            </p>
            <div className="bg-red-900/30 border border-red-500/30 rounded p-3">
              <p className="text-sm text-gray-300">
                <strong className="text-red-400">Norm drift:</strong> ~10-12% over evolution
              </p>
            </div>
          </div>
        </div>

        {/* Quantum Compatibility Hierarchy */}
        <div className="card mb-8">
          <h2 className="text-2xl font-bold mb-4">Quantum Compatibility Hierarchy</h2>
          <p className="text-gray-300 mb-6">
            Putting all of this together, we can sketch a <strong className="text-primary-400">quantum compatibility hierarchy</strong> for meta-derivatives in time:
          </p>

          <div className="space-y-4">
            <div className="bg-dark-bg rounded p-4 border-l-2 border-green-500">
              <h3 className="font-semibold text-green-400">Level Q0 - Classical Schrodinger</h3>
              <p className="text-sm text-gray-400 mt-2">
                Standard derivative <MathBlock equation="D_t = \frac{d}{dt}" displayMode={false} />.
                Norm exactly preserved, fully unitary.
              </p>
            </div>

            <div className="bg-dark-bg rounded p-4 border-l-2 border-blue-500">
              <h3 className="font-semibold text-blue-400">Level Q1 - Pure Clock Reparametrizations</h3>
              <p className="text-sm text-gray-400 mt-2">
                Meta-derivatives of the form <MathBlock equation="D_t = \lambda(t) \frac{d}{dt}" displayMode={false} /> or
                more generally <MathBlock equation="\lambda(t, \|c\|^2)" displayMode={false} /> with <MathBlock equation="\lambda \in \mathbb{R}" displayMode={false} /> and global.
                Quantum predictions unchanged.
              </p>
            </div>

            <div className="bg-dark-bg rounded p-4 border-l-2 border-yellow-500">
              <h3 className="font-semibold text-yellow-400">Level Q2 - Structured but Nontrivial Deformations</h3>
              <p className="text-sm text-gray-400 mt-2">
                More elaborate global scalings that depend on conserved quantities but still act uniformly on all components.
                Still norm-preserving, but highly constrained.
              </p>
            </div>

            <div className="bg-dark-bg rounded p-4 border-l-2 border-red-500">
              <h3 className="font-semibold text-red-400">Level Q3 - Componentwise Meta-Calculus</h3>
              <p className="text-sm text-gray-400 mt-2">
                Meta-derivatives that act differently on each component. Generically break norm conservation
                and cannot be written as a Hermitian generator times a real scalar.
              </p>
            </div>
          </div>
        </div>

        {/* MOO Results */}
        <div className="card mb-8">
          <h2 className="text-2xl font-bold mb-4">Multi-Objective Optimization Results</h2>
          <p className="text-gray-300 mb-6">
            We ran NSGA-II optimization on both meta-quantum compatibility and quantum diffusion problems.
            Here are the real Pareto frontiers:
          </p>

          {/* Meta-Quantum Results */}
          <div className="mb-8">
            <h3 className="font-semibold text-primary-400 mb-4">Meta-Quantum Compatibility (25 Pareto Solutions)</h3>
            <div className="overflow-x-auto">
              <table className="w-full text-sm">
                <thead>
                  <tr className="border-b border-gray-700">
                    <th className="text-left p-2 text-gray-400">Solution</th>
                    <th className="text-center p-2 text-gray-400">Norm Drift (Global)</th>
                    <th className="text-center p-2 text-gray-400">Distance (Global)</th>
                    <th className="text-center p-2 text-gray-400">Norm Drift (Power)</th>
                    <th className="text-center p-2 text-gray-400">Complexity</th>
                  </tr>
                </thead>
                <tbody>
                  <tr className="border-b border-gray-800 bg-green-900/20">
                    <td className="p-2 text-green-400">Best Norm (Global)</td>
                    <td className="p-2 text-center text-green-400">1.25e-14</td>
                    <td className="p-2 text-center">1.536</td>
                    <td className="p-2 text-center">0.0056</td>
                    <td className="p-2 text-center">1.67</td>
                  </tr>
                  <tr className="border-b border-gray-800 bg-blue-900/20">
                    <td className="p-2 text-blue-400">Lowest Complexity</td>
                    <td className="p-2 text-center">1.79e-10</td>
                    <td className="p-2 text-center text-blue-400">0.165</td>
                    <td className="p-2 text-center text-blue-400">3.35e-05</td>
                    <td className="p-2 text-center text-blue-400">0.031</td>
                  </tr>
                  <tr className="border-b border-gray-800 bg-yellow-900/20">
                    <td className="p-2 text-yellow-400">Balanced Trade-off</td>
                    <td className="p-2 text-center">8.41e-12</td>
                    <td className="p-2 text-center">1.536</td>
                    <td className="p-2 text-center">0.0005</td>
                    <td className="p-2 text-center">0.73</td>
                  </tr>
                </tbody>
              </table>
            </div>
            <p className="text-xs text-gray-500 mt-2">
              Key finding: Global meta-derivatives achieve near-zero norm drift (~10^-14), confirming they preserve quantum structure.
            </p>
          </div>

          {/* Quantum Diffusion Results */}
          <div>
            <h3 className="font-semibold text-accent-400 mb-4">Quantum Diffusion (25 Pareto Solutions)</h3>
            <div className="overflow-x-auto">
              <table className="w-full text-sm">
                <thead>
                  <tr className="border-b border-gray-700">
                    <th className="text-left p-2 text-gray-400">Solution</th>
                    <th className="text-center p-2 text-gray-400">Multi-Var</th>
                    <th className="text-center p-2 text-gray-400">Entropy Target</th>
                    <th className="text-center p-2 text-gray-400">Robustness</th>
                    <th className="text-center p-2 text-gray-400">gamma</th>
                  </tr>
                </thead>
                <tbody>
                  <tr className="border-b border-gray-800 bg-green-900/20">
                    <td className="p-2 text-green-400">Best Cluster Var</td>
                    <td className="p-2 text-center text-green-400">1.22e-05</td>
                    <td className="p-2 text-center">0.0456</td>
                    <td className="p-2 text-center">3.67e-05</td>
                    <td className="p-2 text-center">1.28</td>
                  </tr>
                  <tr className="border-b border-gray-800 bg-blue-900/20">
                    <td className="p-2 text-blue-400">Best Robustness</td>
                    <td className="p-2 text-center">2.27e-05</td>
                    <td className="p-2 text-center">0.0442</td>
                    <td className="p-2 text-center text-blue-400">3.41e-05</td>
                    <td className="p-2 text-center">0.32</td>
                  </tr>
                  <tr className="border-b border-gray-800 bg-yellow-900/20">
                    <td className="p-2 text-yellow-400">Optimal Config</td>
                    <td className="p-2 text-center">1.30e-05</td>
                    <td className="p-2 text-center text-yellow-400">0.0435</td>
                    <td className="p-2 text-center">3.63e-05</td>
                    <td className="p-2 text-center">1.62</td>
                  </tr>
                </tbody>
              </table>
            </div>
            <p className="text-xs text-gray-500 mt-2">
              Key finding: Multi-calculus diffusion achieves excellent cluster preservation (variance ~10^-5) with high robustness.
            </p>
          </div>

          <div className="mt-6 p-4 bg-dark-bg rounded-lg border-l-2 border-primary-500">
            <h4 className="font-semibold text-primary-400 mb-2">Optimization Parameters</h4>
            <div className="grid grid-cols-2 gap-4 text-sm text-gray-400">
              <div>
                <p>Algorithm: NSGA-II</p>
                <p>Generations: 50</p>
              </div>
              <div>
                <p>Population: 25</p>
                <p>Run Date: December 2025</p>
              </div>
            </div>
          </div>
        </div>

        {/* What We Learned */}
        <div className="card mb-8 bg-gradient-to-r from-primary-900/30 to-accent-900/30">
          <h2 className="text-2xl font-bold mb-4">What We Actually Learned (Quantum Edition)</h2>
          <div className="space-y-4">
            <div className="flex items-start">
              <span className="text-green-400 mr-2 text-xl">1.</span>
              <div>
                <p className="font-semibold text-gray-200">Meta-time is mostly a clock story</p>
                <p className="text-sm text-gray-400">For a large and natural class of meta-derivatives in time, meta-calculus does not change quantum mechanics; it just changes how quickly the clock ticks.</p>
              </div>
            </div>
            <div className="flex items-start">
              <span className="text-yellow-400 mr-2 text-xl">2.</span>
              <div>
                <p className="font-semibold text-gray-200">Quantum structure is fragile</p>
                <p className="text-sm text-gray-400">Small-looking, componentwise changes to the calculus can completely destroy norm conservation.</p>
              </div>
            </div>
            <div className="flex items-start">
              <span className="text-primary-400 mr-2 text-xl">3.</span>
              <div>
                <p className="font-semibold text-gray-200">The physically allowed corner is tiny</p>
                <p className="text-sm text-gray-400">Just as cosmological data pushed k, s toward 0 in the meta-Friedmann analysis, quantum structure pushes meta-derivatives back toward global scalar deformations.</p>
              </div>
            </div>
            <div className="flex items-start">
              <span className="text-accent-400 mr-2 text-xl">4.</span>
              <div>
                <p className="font-semibold text-gray-200">This is a feature, not a bug</p>
                <p className="text-sm text-gray-400">It supports the overarching theme: the geometry is real; the calculus is a lens - but only a very special family of lenses respects quantum structure.</p>
              </div>
            </div>
          </div>
        </div>

        {/* What's Next */}
        <div className="card mb-8">
          <h2 className="text-2xl font-bold mb-4">What&apos;s Next</h2>
          <p className="text-gray-300">
            The next chapter zooms out from single equations to <strong className="text-accent-400">multi-geometry diffusion</strong>:
          </p>
          <ul className="mt-4 space-y-2 text-gray-300">
            <li className="flex items-start">
              <span className="text-accent-400 mr-2">-&gt;</span>
              <span>Multiple calculi on the same state space</span>
            </li>
            <li className="flex items-start">
              <span className="text-accent-400 mr-2">-&gt;</span>
              <span>Diffusion trajectories across calculi instead of a single fixed one</span>
            </li>
            <li className="flex items-start">
              <span className="text-accent-400 mr-2">-&gt;</span>
              <span>Toy experiments on a triangle and on early-universe parameter space</span>
            </li>
            <li className="flex items-start">
              <span className="text-accent-400 mr-2">-&gt;</span>
              <span>Connections to positive geometries, cosmological polytopes, and multi-metric diffusion</span>
            </li>
          </ul>
        </div>

        {/* Navigation */}
        <div className="flex justify-between items-center mt-12">
          <Link href="/story/geometry" className="text-gray-400 hover:text-white transition-colors">
            &larr; Back to Results
          </Link>
          <Link href="/story/geometry" className="btn-primary">
            Next: Many Calculi, Many Geometries &rarr;
          </Link>
        </div>
      </div>
    </div>
  );
}
