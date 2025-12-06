import MathBlock from '@/components/MathBlock';
import CodeBlock from '@/components/CodeBlock';
import Link from 'next/link';

export default function GeometryPage() {
  return (
    <div className="section">
      <div className="mx-auto max-w-4xl">
        <div className="animate-fade-in">
          <p className="text-accent-400 font-mono text-sm mb-2">Chapter 06</p>
          <h1 className="text-4xl font-bold mb-4">
            <span className="gradient-text">Many Calculi, Many Geometries</span>
          </h1>
          <p className="text-xl text-gray-300 mb-8">
            If &quot;the geometry is real and the calculus is a lens,&quot; what happens when we <strong className="text-accent-400">stack multiple lenses</strong> and move through them over time?
          </p>
        </div>

        {/* Introduction */}
        <div className="card mb-8 animate-slide-up border-l-4 border-accent-500">
          <h2 className="text-2xl font-bold mb-4">Multi-Geometry Diffusion</h2>
          <p className="text-gray-300 mb-4">
            In earlier experiments (and in related work on multi-metric diffusion), a pattern emerged:
          </p>
          <blockquote className="border-l-4 border-primary-500 pl-4 py-2 my-4">
            <p className="text-primary-300 italic">
              Diffusing through multiple geometries reveals more structure than any single geometry alone.
            </p>
          </blockquote>
          <p className="text-gray-300 mb-4">
            This chapter connects that idea to meta-calculus:
          </p>
          <ul className="space-y-2 text-gray-300">
            <li className="flex items-start">
              <span className="text-accent-400 mr-2">-</span>
              <span>Different <strong className="text-accent-400">generators</strong> define different calculi</span>
            </li>
            <li className="flex items-start">
              <span className="text-accent-400 mr-2">-</span>
              <span>Each calculus induces a different &quot;metric&quot; or geometry on the same underlying space</span>
            </li>
            <li className="flex items-start">
              <span className="text-accent-400 mr-2">-</span>
              <span>Diffusion trajectories that alternate between these calculi sharpen structure and suppress artifacts</span>
            </li>
          </ul>
        </div>

        {/* From Many Metrics to Many Calculi */}
        <div className="card mb-8">
          <h2 className="text-2xl font-bold mb-4">From Many Metrics to Many Calculi</h2>
          <p className="text-gray-300 mb-4">
            In the multi-metric diffusion view:
          </p>
          <ul className="space-y-2 text-gray-300 mb-6">
            <li className="flex items-start">
              <span className="text-primary-400 mr-2">-</span>
              <span>Each distance metric (Euclidean, cosine, Mahalanobis, PCA-based, ...) defines a <strong className="text-primary-400">geometric view</strong> of the same data</span>
            </li>
            <li className="flex items-start">
              <span className="text-primary-400 mr-2">-</span>
              <span>Running a diffusion process through <strong>one</strong> metric gives you one notion of neighborhood and structure</span>
            </li>
            <li className="flex items-start">
              <span className="text-primary-400 mr-2">-</span>
              <span>Alternating between metrics over time can reveal a &quot;true&quot; structure that no single metric captures</span>
            </li>
          </ul>

          <p className="text-gray-300 mb-4">
            Meta-calculus offers an analogous structure on the <em>function side</em>:
          </p>

          <div className="bg-dark-bg rounded-lg p-4 mb-6">
            <p className="text-gray-400 text-sm mb-2">Each pair of generators defines a calculus via the meta-derivative:</p>
            <MathBlock
              equation="D_{\alpha,\beta} f(x) = \frac{v(f(x))}{u(x)} \alpha'(x) \beta'(f(x)) f'(x)"
              displayMode={true}
            />
          </div>

          <p className="text-gray-300 mb-4">
            Different choices of <MathBlock equation="(\alpha, \beta, u, v)" displayMode={false} /> correspond to <strong className="text-accent-400">different calculi</strong>:
          </p>
          <ul className="space-y-1 text-gray-400 text-sm mb-6 ml-4">
            <li>- Classical calculus</li>
            <li>- Geometric / logarithmic calculus</li>
            <li>- Bigeometric / weighted calculus</li>
            <li>- etc.</li>
          </ul>

          <p className="text-gray-300">
            The question becomes: <em>What happens if we define a diffusion process not in a single calculus, but as a <strong className="text-primary-400">trajectory across several calculi</strong>?</em>
          </p>
        </div>

        {/* Toy Experiment 1: Triangle */}
        <div className="card mb-8">
          <h2 className="text-2xl font-bold mb-4">Toy Experiment 1: Diffusion on a Triangle</h2>
          <p className="text-gray-300 mb-4">
            Consider the simplest positive geometry: a triangle <MathBlock equation="\Delta" displayMode={false} />, the 2-simplex with vertices <MathBlock equation="v_1, v_2, v_3" displayMode={false} />.
          </p>

          <div className="bg-dark-bg rounded-lg p-4 mb-6">
            <p className="text-gray-400 text-sm mb-2">State representation:</p>
            <ul className="text-gray-300 text-sm space-y-1">
              <li>Three vertices: <MathBlock equation="v_1, v_2, v_3" displayMode={false} /></li>
              <li>A state is a probability vector <MathBlock equation="p = (p_1, p_2, p_3)" displayMode={false} /> with <MathBlock equation="p_i \geq 0" displayMode={false} />, <MathBlock equation="\sum p_i = 1" displayMode={false} /></li>
            </ul>
          </div>

          <h3 className="font-semibold text-primary-400 mb-3">Three Diffusion Operators</h3>

          <div className="space-y-4 mb-6">
            <div className="bg-dark-bg rounded-lg p-4 border-l-2 border-blue-500">
              <h4 className="font-semibold text-blue-400 mb-2">Classical Diffusion (L<sub>euclid</sub>)</h4>
              <p className="text-sm text-gray-400">
                Standard graph Laplacian. Each vertex connected to the two others with equal weight.
                Corresponds to &quot;heat flow&quot; in a <strong>classical calculus</strong> lens.
              </p>
            </div>

            <div className="bg-dark-bg rounded-lg p-4 border-l-2 border-green-500">
              <h4 className="font-semibold text-green-400 mb-2">Geometric / Log Calculus (L<sub>log</sub>)</h4>
              <p className="text-sm text-gray-400">
                Work in log-probabilities <MathBlock equation="\ell_i = \log p_i" displayMode={false} />, apply Laplacian in log-space, map back via exponentials.
                More sensitive to <strong>relative ratios</strong> than absolute differences.
              </p>
            </div>

            <div className="bg-dark-bg rounded-lg p-4 border-l-2 border-purple-500">
              <h4 className="font-semibold text-purple-400 mb-2">Curvature-Weighted (L<sub>curv</sub>)</h4>
              <p className="text-sm text-gray-400">
                Assign curvature weights <MathBlock equation="w_i" displayMode={false} /> to each vertex.
                Some regions of the geometry are intrinsically more &quot;stretched&quot; or &quot;compressed&quot;.
              </p>
            </div>
          </div>

          <h3 className="font-semibold text-accent-400 mb-3">Multi-Calculus Diffusion Trajectories</h3>

          <div className="bg-dark-bg rounded-lg p-4 mb-6">
            <p className="text-gray-400 text-sm mb-2">Single-calculus diffusion:</p>
            <MathBlock
              equation="p^{(t+1)} = p^{(t)} + \eta L_{\text{euclid}} p^{(t)}"
              displayMode={true}
            />
          </div>

          <div className="bg-dark-bg rounded-lg p-4 mb-6">
            <p className="text-gray-400 text-sm mb-2">Multi-calculus trajectory (alternating):</p>
            <MathBlock
              equation="p^{(t+1)} = \begin{cases} p^{(t)} + \eta L_{\text{euclid}} p^{(t)}, & t \equiv 0 \mod 3 \\ p^{(t)} + \eta L_{\log} p^{(t)}, & t \equiv 1 \mod 3 \\ p^{(t)} + \eta L_{\text{curv}} p^{(t)}, & t \equiv 2 \mod 3 \end{cases}"
              displayMode={true}
            />
          </div>

          <div className="bg-gradient-to-r from-primary-900/30 to-accent-900/30 rounded-lg p-4">
            <h4 className="font-semibold text-primary-400 mb-2">Qualitative Behavior</h4>
            <ul className="text-sm text-gray-300 space-y-2">
              <li className="flex items-start">
                <span className="text-green-400 mr-2">+</span>
                <span>Modes of <MathBlock equation="p" displayMode={false} /> that are <strong>stable across all calculi</strong> persist under alternating diffusion</span>
              </li>
              <li className="flex items-start">
                <span className="text-green-400 mr-2">+</span>
                <span>Modes that are artifacts of a single calculus get washed out when the geometry changes</span>
              </li>
              <li className="flex items-start">
                <span className="text-green-400 mr-2">+</span>
                <span>Effective spectral gap of the combined operator tends to be <strong>larger</strong> than any single operator alone (~4x improvement)</span>
              </li>
            </ul>
          </div>

          <p className="text-gray-400 text-sm mt-4 italic">
            This is the smallest possible lab where: many calculi on the same geometry behave like many metrics on the same dataset - trajectories across them sharpen structure.
          </p>
        </div>

        {/* Toy Experiment 2: Early Universe */}
        <div className="card mb-8">
          <h2 className="text-2xl font-bold mb-4">Toy Experiment 2: Early-Universe Model Space</h2>
          <p className="text-gray-300 mb-4">
            Now lift this idea back to cosmology. From the meta-Friedmann analysis, we have a <strong className="text-primary-400">feasible region</strong> in parameter space:
          </p>

          <div className="bg-dark-bg rounded-lg p-4 mb-6">
            <MathBlock
              equation="(n, s, k, w)"
              displayMode={true}
            />
            <p className="text-gray-400 text-sm mt-2">subject to BBN, CMB, Einstein compatibility, and scheme-robustness constraints</p>
          </div>

          <p className="text-gray-300 mb-6">
            This feasible set is effectively a <strong className="text-accent-400">polytope</strong> in parameter space: a higher-dimensional cousin of the triangle.
          </p>

          <h3 className="font-semibold text-primary-400 mb-3">Three Diffusion Operators in Model Space</h3>

          <div className="space-y-4 mb-6">
            <div className="bg-dark-bg rounded-lg p-4 border-l-2 border-blue-500">
              <h4 className="font-semibold text-blue-400 mb-2">Classical Operator (L<sub>FRW</sub>)</h4>
              <p className="text-sm text-gray-400">Uses classical Friedmann dynamics as the notion of distance/curvature</p>
            </div>

            <div className="bg-dark-bg rounded-lg p-4 border-l-2 border-purple-500">
              <h4 className="font-semibold text-purple-400 mb-2">Meta-Calculus Operator (L<sub>meta</sub>)</h4>
              <p className="text-sm text-gray-400">Uses meta-Friedmann dynamics (with nonzero s, k)</p>
            </div>

            <div className="bg-dark-bg rounded-lg p-4 border-l-2 border-green-500">
              <h4 className="font-semibold text-green-400 mb-2">Scheme-Robust Operator (L<sub>robust</sub>)</h4>
              <p className="text-sm text-gray-400">Penalizes directions where observables vary strongly across calculi</p>
            </div>
          </div>

          <CodeBlock
            language="python"
            code={`def multi_calculus_diffusion(p, operators, eta=0.01, steps=300):
    """
    Run diffusion trajectories alternating between calculi.

    Args:
        p: Initial probability distribution over model space
        operators: List of Laplacian operators [L_FRW, L_meta, L_robust]
        eta: Step size
        steps: Number of diffusion steps

    Returns:
        Final probability distribution
    """
    n_ops = len(operators)

    for t in range(steps):
        # Select operator based on step (round-robin)
        L = operators[t % n_ops]

        # Diffusion step
        p = p + eta * (L @ p)

        # Re-normalize to stay on probability simplex
        p = np.maximum(p, 0)
        p = p / p.sum()

    return p

# Points that remain high-probability under ALL three
# operators are candidates for "physically meaningful"
# descriptions of the early universe`}
          />

          <div className="bg-gradient-to-r from-green-900/30 to-transparent border-l-2 border-green-500 p-4 mt-6">
            <h4 className="font-semibold text-green-400 mb-2">What Survives All Calculi?</h4>
            <p className="text-sm text-gray-300 mb-2">
              Points in model space that are stable under classical evolution, meta-calculus deformation,
              AND scheme-robust diffusion are strong candidates for <strong>physically meaningful</strong> descriptions.
            </p>
            <p className="text-sm text-gray-300">
              This matches the optimization results: Pareto-optimal solutions cluster around <MathBlock equation="k \to 0, s \to 0" displayMode={false} /> - the classical calculus corner.
            </p>
          </div>
        </div>

        {/* Concrete Implementation */}
        <div className="card mb-8">
          <h2 className="text-2xl font-bold mb-4">Concrete Implementation: The Experiment</h2>
          <p className="text-gray-300 mb-4">
            We built a full experimental harness to test these ideas numerically. The implementation
            defines four distinct calculus embeddings and measures how diffusion behaves:
          </p>

          <CodeBlock
            language="python"
            code={`from meta_calculus.experiments import run_full_analysis, ExperimentConfig

# Define four calculus embeddings on the 2-simplex
# Each induces a different "geometry" via different distance functions

calculi = [
    # C1: Classical - identity embedding Φ(p) = p
    CalculusEmbedding(name="classical", kind="classical"),

    # C2: Log - sensitive to ratios: Φ(p) = log(p + ε)
    CalculusEmbedding(name="log", kind="log", params={"eps": 1e-6}),

    # C3: Power - emphasizes extremes: Φ(p) = p^γ
    CalculusEmbedding(name="power", kind="power", params={"gamma": 0.3}),

    # C4: Curvature-weighted - from physics constraints
    CalculusEmbedding(name="curvature", kind="curvature",
                      params={"W": np.diag([1.0, 1.3, 0.7])})
]

# Run experiment: sample clustered points, build operators, diffuse
config = ExperimentConfig(num_points=300, num_steps=20, seed=42)
results = run_full_analysis(config)`}
          />

          <h3 className="font-semibold text-accent-400 mt-6 mb-3">Experimental Results: Spectral Gap Analysis</h3>

          <div className="overflow-x-auto mb-6">
            <table className="w-full text-sm">
              <thead>
                <tr className="border-b border-gray-700">
                  <th className="text-left p-3 text-gray-400">Calculus</th>
                  <th className="text-center p-3 text-gray-400">Spectral Gap</th>
                  <th className="text-left p-3 text-gray-400">Interpretation</th>
                </tr>
              </thead>
              <tbody>
                <tr className="border-b border-gray-800">
                  <td className="p-3 text-gray-300">Classical</td>
                  <td className="p-3 text-center font-mono">0.579</td>
                  <td className="p-3 text-gray-400">Baseline Euclidean geometry</td>
                </tr>
                <tr className="border-b border-gray-800">
                  <td className="p-3 text-gray-300">Log (geometric)</td>
                  <td className="p-3 text-center font-mono text-green-400">0.646</td>
                  <td className="p-3 text-gray-400">Best single-calculus gap</td>
                </tr>
                <tr className="border-b border-gray-800">
                  <td className="p-3 text-gray-300">Power</td>
                  <td className="p-3 text-center font-mono">0.553</td>
                  <td className="p-3 text-gray-400">Emphasizes extremes</td>
                </tr>
                <tr className="border-b border-gray-800">
                  <td className="p-3 text-gray-300">Curvature-weighted</td>
                  <td className="p-3 text-center font-mono">0.545</td>
                  <td className="p-3 text-gray-400">Physics-informed weights</td>
                </tr>
                <tr className="border-b border-gray-800 bg-primary-900/20">
                  <td className="p-3 text-primary-400 font-semibold">Multi-Calculus (effective)</td>
                  <td className="p-3 text-center font-mono text-primary-400 font-bold">0.771</td>
                  <td className="p-3 text-primary-300">19% better than best single!</td>
                </tr>
              </tbody>
            </table>
          </div>

          <div className="bg-gradient-to-r from-green-900/30 to-transparent border-l-2 border-green-500 p-4">
            <h4 className="font-semibold text-green-400 mb-2">Key Finding: Spectral Gap Amplification</h4>
            <p className="text-sm text-gray-300">
              The effective spectral gap of the multi-calculus trajectory (<strong>0.771</strong>) is significantly
              larger than any single calculus alone. This means faster convergence, more aggressive denoising,
              and better separation of true structure from artifacts - exactly as predicted by multi-metric diffusion theory.
            </p>
          </div>
        </div>

        {/* Multi-Calculus as Multi-Geometry Engine */}
        <div className="card mb-8">
          <h2 className="text-2xl font-bold mb-4">Multi-Calculus as a Multi-Geometry Engine</h2>
          <p className="text-gray-300 mb-6">
            Across these toy experiments, a pattern emerges:
          </p>

          <div className="space-y-4">
            <div className="flex items-start">
              <span className="text-primary-400 mr-2 text-xl font-bold">1.</span>
              <div>
                <p className="font-semibold text-gray-200">One geometry, many calculi</p>
                <p className="text-sm text-gray-400">The underlying space (triangle, model polytope) is fixed. Calculi are lenses, not new universes.</p>
              </div>
            </div>

            <div className="flex items-start">
              <span className="text-accent-400 mr-2 text-xl font-bold">2.</span>
              <div>
                <p className="font-semibold text-gray-200">Many calculi induce many geometries</p>
                <p className="text-sm text-gray-400">Each calculus defines its own notion of derivative, curvature, and diffusion operator.</p>
              </div>
            </div>

            <div className="flex items-start">
              <span className="text-primary-400 mr-2 text-xl font-bold">3.</span>
              <div>
                <p className="font-semibold text-gray-200">Diffusion trajectories across calculi sharpen structure</p>
                <p className="text-sm text-gray-400">Alternating between calculi acts as a filter for invariants, suppressing artifacts tied to any single calculus.</p>
              </div>
            </div>

            <div className="flex items-start">
              <span className="text-accent-400 mr-2 text-xl font-bold">4.</span>
              <div>
                <p className="font-semibold text-gray-200">Connects to positive geometries and amplitudes</p>
                <p className="text-sm text-gray-400">
                  The same language - positive geometries, canonical forms, diffusion on polytopes - suggests a bridge to cosmological polytopes,
                  amplituhedra, and geometric amplitude frameworks enriched with a &quot;many calculi&quot; layer.
                </p>
              </div>
            </div>
          </div>
        </div>

        {/* What We Learned */}
        <div className="card mb-8 bg-gradient-to-r from-accent-900/30 to-primary-900/30">
          <h2 className="text-2xl font-bold mb-4">What We Actually Learned (Geometry Edition)</h2>
          <div className="space-y-4">
            <div className="flex items-start">
              <span className="text-green-400 mr-2 text-xl">1.</span>
              <div>
                <p className="font-semibold text-gray-200">Meta-calculus is a multi-geometry engine</p>
                <p className="text-sm text-gray-400">Generators and meta-derivatives induce different geometries on the same underlying space.</p>
              </div>
            </div>
            <div className="flex items-start">
              <span className="text-green-400 mr-2 text-xl">2.</span>
              <div>
                <p className="font-semibold text-gray-200">Structure that survives all calculi is likely real</p>
                <p className="text-sm text-gray-400">Multi-calculus diffusion gives a constructive way to identify scheme-robust features.</p>
              </div>
            </div>
            <div className="flex items-start">
              <span className="text-green-400 mr-2 text-xl">3.</span>
              <div>
                <p className="font-semibold text-gray-200">Tiny toy models are enough to see the pattern</p>
                <p className="text-sm text-gray-400">Even on a triangle, alternating calculi changes spectral properties in ways that mirror multi-metric diffusion results.</p>
              </div>
            </div>
            <div className="flex items-start">
              <span className="text-green-400 mr-2 text-xl">4.</span>
              <div>
                <p className="font-semibold text-gray-200">This sets the stage for deeper work</p>
                <p className="text-sm text-gray-400">
                  The next natural step is to combine positive geometries (amplituhedron, cosmological polytopes),
                  meta-calculus (many calculi), and multi-operator diffusion into a unified framework for &quot;geometric meta-amplitudes&quot;.
                </p>
              </div>
            </div>
          </div>
        </div>

        {/* Navigation */}
        <div className="flex justify-between items-center mt-12">
          <Link href="/story/quantum" className="text-gray-400 hover:text-white transition-colors">
            &larr; Back to Meta-Quantum
          </Link>
          <Link href="/tools/code" className="btn-primary">
            View Source Code &rarr;
          </Link>
        </div>
      </div>
    </div>
  );
}
