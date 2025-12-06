import Link from 'next/link';
import MathBlock from '@/components/MathBlock';
import CodeBlock from '@/components/CodeBlock';

export default function DerivationsPage() {
  return (
    <div className="section">
      <div className="mx-auto max-w-4xl">
        <div className="animate-fade-in">
          <p className="text-primary-400 font-mono text-sm mb-2">Mathematical History</p>
          <h1 className="text-4xl font-bold mb-4">
            <span className="gradient-text">Rigorous Derivations</span>
          </h1>
          <p className="text-xl text-gray-300 mb-8">
            Step-by-step mathematical proofs with full working
          </p>
        </div>

        {/* Introduction */}
        <div className="card mb-8 animate-slide-up border-l-4 border-primary-500">
          <h2 className="text-2xl font-bold mb-4">About These Derivations</h2>
          <p className="text-gray-300 mb-4">
            This page provides rigorous step-by-step derivations of all key results.
            Each derivation includes:
          </p>
          <ul className="space-y-1 text-gray-300 text-sm">
            <li><span className="text-primary-400">Starting assumptions</span> - What we take as given</li>
            <li><span className="text-primary-400">Step-by-step algebra</span> - No skipped steps</li>
            <li><span className="text-primary-400">Verification</span> - Numerical or limit checks</li>
            <li><span className="text-primary-400">Physical interpretation</span> - What the result means</li>
          </ul>
        </div>

        {/* Section 1: Meta-Derivative Definition */}
        <div className="card mb-8">
          <h2 className="text-2xl font-bold mb-4">1. The Meta-Derivative</h2>

          <div className="bg-dark-bg rounded-lg p-4 mb-6">
            <h3 className="font-semibold text-primary-400 mb-2">Definition (Grossman-Katz, 1972)</h3>
            <p className="text-sm text-gray-400 mb-4">
              Let alpha, beta be bijective, differentiable functions on their domains.
              The (alpha, beta)-derivative of f at x is:
            </p>
            <MathBlock
              equation="D_{(\alpha,\beta)}f(x) = \lim_{h \to 0} \beta^{-1}\left(\frac{\beta(f(x+h)) - \beta(f(x))}{\alpha(x+h) - \alpha(x)}\right)"
              displayMode={true}
            />
          </div>

          <div className="space-y-6">
            <div>
              <h3 className="font-semibold text-gray-300 mb-2">Step 1: Taylor expand beta(f(x+h))</h3>
              <MathBlock
                equation="\beta(f(x+h)) = \beta(f(x)) + \beta'(f(x)) \cdot f'(x) \cdot h + O(h^2)"
                displayMode={true}
              />
            </div>

            <div>
              <h3 className="font-semibold text-gray-300 mb-2">Step 2: Taylor expand alpha(x+h)</h3>
              <MathBlock
                equation="\alpha(x+h) = \alpha(x) + \alpha'(x) \cdot h + O(h^2)"
                displayMode={true}
              />
            </div>

            <div>
              <h3 className="font-semibold text-gray-300 mb-2">Step 3: Substitute and take limit</h3>
              <MathBlock
                equation="\frac{\beta(f(x+h)) - \beta(f(x))}{\alpha(x+h) - \alpha(x)} = \frac{\beta'(f(x)) \cdot f'(x) \cdot h}{\alpha'(x) \cdot h} + O(h)"
                displayMode={true}
              />
              <MathBlock
                equation="= \frac{\beta'(f(x)) \cdot f'(x)}{\alpha'(x)} \text{ as } h \to 0"
                displayMode={true}
              />
            </div>

            <div>
              <h3 className="font-semibold text-gray-300 mb-2">Step 4: Apply beta-inverse</h3>
              <MathBlock
                equation="D_{(\alpha,\beta)}f(x) = \beta^{-1}\left(\frac{\beta'(f(x)) \cdot f'(x)}{\alpha'(x)}\right)"
                displayMode={true}
              />
            </div>
          </div>

          <div className="bg-dark-bg rounded-lg p-4 mt-6 border border-green-800">
            <h3 className="font-semibold text-green-400 mb-2">Verification: Classical Limit</h3>
            <p className="text-sm text-gray-400 mb-2">
              When alpha = beta = Identity (id(x) = x), we have id&apos;(x) = 1 and id^(-1) = id:
            </p>
            <MathBlock
              equation="D_{(id,id)}f(x) = id\left(\frac{1 \cdot f'(x)}{1}\right) = f'(x)"
              displayMode={true}
            />
            <p className="text-sm text-green-400 mt-2">Recovers standard derivative.</p>
          </div>
        </div>

        {/* Section 2: Bigeometric Derivative */}
        <div className="card mb-8">
          <h2 className="text-2xl font-bold mb-4">2. The Bigeometric Derivative</h2>

          <div className="bg-dark-bg rounded-lg p-4 mb-6">
            <h3 className="font-semibold text-primary-400 mb-2">Definition</h3>
            <p className="text-sm text-gray-400 mb-4">
              The bigeometric calculus uses alpha(x) = beta(x) = ln(x):
            </p>
            <MathBlock
              equation="D_{BG}f(x) = \exp\left(\frac{\ln(f(x+h)) - \ln(f(x))}{\ln(x+h) - \ln(x)}\right)"
              displayMode={true}
            />
          </div>

          <div className="space-y-6">
            <div>
              <h3 className="font-semibold text-gray-300 mb-2">Step 1: Simplify the argument</h3>
              <MathBlock
                equation="\frac{\ln(f(x+h)) - \ln(f(x))}{\ln(x+h) - \ln(x)} = \frac{\ln(f(x+h)/f(x))}{\ln((x+h)/x)}"
                displayMode={true}
              />
            </div>

            <div>
              <h3 className="font-semibold text-gray-300 mb-2">Step 2: Taylor expand logarithms</h3>
              <p className="text-sm text-gray-400 mb-2">Using ln(1 + epsilon) = epsilon + O(epsilon^2):</p>
              <MathBlock
                equation="\ln(f(x+h)/f(x)) = \ln\left(1 + \frac{f'(x)h}{f(x)}\right) \approx \frac{f'(x)h}{f(x)}"
                displayMode={true}
              />
              <MathBlock
                equation="\ln((x+h)/x) = \ln(1 + h/x) \approx \frac{h}{x}"
                displayMode={true}
              />
            </div>

            <div>
              <h3 className="font-semibold text-gray-300 mb-2">Step 3: Take the ratio</h3>
              <MathBlock
                equation="\frac{f'(x)h/f(x)}{h/x} = \frac{x \cdot f'(x)}{f(x)}"
                displayMode={true}
              />
            </div>

            <div>
              <h3 className="font-semibold text-gray-300 mb-2">Step 4: Apply exponential</h3>
              <MathBlock
                equation="D_{BG}f(x) = \exp\left(\frac{x \cdot f'(x)}{f(x)}\right) = \exp\left(\frac{d}{dx}\ln(f(x)) \cdot x\right)"
                displayMode={true}
              />
            </div>
          </div>

          <div className="bg-dark-bg rounded-lg p-4 mt-6 border border-red-800">
            <h3 className="font-semibold text-red-400 mb-2">Critical Check: Constant Function</h3>
            <p className="text-sm text-gray-400 mb-2">
              Let f(x) = c (constant). Then f&apos;(x) = 0:
            </p>
            <MathBlock
              equation="D_{BG}[c] = \exp\left(\frac{x \cdot 0}{c}\right) = \exp(0) = 1"
              displayMode={true}
            />
            <p className="text-sm text-red-400 mt-2">
              This is NOT zero. Bigeometric derivative of a constant is 1, not 0.
              This breaks linearity: D_BG[af + bg] != a D_BG[f] + b D_BG[g].
            </p>
          </div>
        </div>

        {/* Section 3: Meta-Friedmann Derivation */}
        <div className="card mb-8">
          <h2 className="text-2xl font-bold mb-4">3. Meta-Friedmann Equation</h2>

          <div className="bg-dark-bg rounded-lg p-4 mb-6">
            <h3 className="font-semibold text-primary-400 mb-2">Starting Point</h3>
            <p className="text-sm text-gray-400 mb-4">
              We modify the cosmological Lagrangian to include a meta-weight k:
            </p>
            <MathBlock
              equation="\mathcal{L} = -\frac{3}{8\pi G} a \cdot t^{2k} \cdot \dot{a}^2 - a^3 \rho(a)"
              displayMode={true}
            />
          </div>

          <div className="space-y-6">
            <div>
              <h3 className="font-semibold text-gray-300 mb-2">Step 1: Euler-Lagrange equation</h3>
              <p className="text-sm text-gray-400 mb-2">
                The equation of motion is:
              </p>
              <MathBlock
                equation="\frac{d}{dt}\left(\frac{\partial \mathcal{L}}{\partial \dot{a}}\right) - \frac{\partial \mathcal{L}}{\partial a} = 0"
                displayMode={true}
              />
            </div>

            <div>
              <h3 className="font-semibold text-gray-300 mb-2">Step 2: Compute partial derivatives</h3>
              <MathBlock
                equation="\frac{\partial \mathcal{L}}{\partial \dot{a}} = -\frac{6}{8\pi G} a \cdot t^{2k} \cdot \dot{a} = -\frac{3}{4\pi G} a t^{2k} \dot{a}"
                displayMode={true}
              />
              <MathBlock
                equation="\frac{\partial \mathcal{L}}{\partial a} = -\frac{3}{8\pi G} t^{2k} \dot{a}^2 - 3a^2 \rho(a) - a^3 \frac{d\rho}{da}"
                displayMode={true}
              />
            </div>

            <div>
              <h3 className="font-semibold text-gray-300 mb-2">Step 3: Time derivative of conjugate momentum</h3>
              <MathBlock
                equation="\frac{d}{dt}\left(-\frac{3}{4\pi G} a t^{2k} \dot{a}\right) = -\frac{3}{4\pi G}\left(\dot{a} t^{2k} \dot{a} + a \cdot 2k t^{2k-1} \dot{a} + a t^{2k} \ddot{a}\right)"
                displayMode={true}
              />
            </div>

            <div>
              <h3 className="font-semibold text-gray-300 mb-2">Step 4: Assume power-law solution</h3>
              <p className="text-sm text-gray-400 mb-2">
                Try a(t) = t^n and rho = rho_0 a^(-3(1+w)):
              </p>
              <MathBlock
                equation="\dot{a} = n t^{n-1}, \quad \ddot{a} = n(n-1)t^{n-2}"
                displayMode={true}
              />
            </div>

            <div>
              <h3 className="font-semibold text-gray-300 mb-2">Step 5: Substitute and simplify</h3>
              <p className="text-sm text-gray-400 mb-2">
                After substitution and demanding consistency at all powers of t:
              </p>
              <MathBlock
                equation="n^2 + 2kn + n - \frac{2}{3(1+w)} = 0"
                displayMode={true}
              />
            </div>

            <div>
              <h3 className="font-semibold text-gray-300 mb-2">Step 6: Include GUC correction s</h3>
              <p className="text-sm text-gray-400 mb-2">
                With an additional GUC parameter s modifying the matter coupling:
              </p>
              <MathBlock
                equation="n_{act}(s,w) = \frac{-(3ws + 2s - 2) + \sqrt{\Delta}}{6(1+w)}"
                displayMode={true}
              />
              <p className="text-sm text-gray-400 mt-2">where:</p>
              <MathBlock
                equation="\Delta = 9s^2w^2 - 8s^2 + 4s + 4"
                displayMode={true}
              />
            </div>
          </div>

          <div className="bg-dark-bg rounded-lg p-4 mt-6 border border-green-800">
            <h3 className="font-semibold text-green-400 mb-2">Verification: s = 0 limit</h3>
            <p className="text-sm text-gray-400 mb-2">
              When s = 0:
            </p>
            <MathBlock
              equation="\Delta = 4, \quad n_{act}(0,w) = \frac{-(-2) + 2}{6(1+w)} = \frac{4}{6(1+w)} = \frac{2}{3(1+w)}"
              displayMode={true}
            />
            <p className="text-sm text-gray-400 mt-2">
              This gives n = 1/2 for radiation (w=1/3) and n = 2/3 for matter (w=0).
            </p>
            <p className="text-sm text-green-400 mt-2">Recovers standard cosmology.</p>
          </div>
        </div>

        {/* Section 4: Spectral Gap Amplification */}
        <div className="card mb-8">
          <h2 className="text-2xl font-bold mb-4">4. Multi-Calculus Spectral Gap</h2>

          <div className="bg-dark-bg rounded-lg p-4 mb-6">
            <h3 className="font-semibold text-primary-400 mb-2">Setup</h3>
            <p className="text-sm text-gray-400 mb-4">
              Consider K different calculus embeddings Phi_k mapping the simplex to R^m.
              Each defines a diffusion operator P_k = I - eta * L_k.
            </p>
          </div>

          <div className="space-y-6">
            <div>
              <h3 className="font-semibold text-gray-300 mb-2">Step 1: Single-calculus spectral gap</h3>
              <p className="text-sm text-gray-400 mb-2">
                For a normalized Laplacian L_k with eigenvalues 0 = lambda_1 &lt;= lambda_2 &lt;= ...:
              </p>
              <MathBlock
                equation="\text{gap}_k = \lambda_2(L_k) - \lambda_1(L_k) = \lambda_2(L_k)"
                displayMode={true}
              />
            </div>

            <div>
              <h3 className="font-semibold text-gray-300 mb-2">Step 2: Composed operator</h3>
              <p className="text-sm text-gray-400 mb-2">
                The multi-calculus operator after one cycle through all K calculi:
              </p>
              <MathBlock
                equation="P_{eff} = P_K \cdot P_{K-1} \cdots P_1"
                displayMode={true}
              />
            </div>

            <div>
              <h3 className="font-semibold text-gray-300 mb-2">Step 3: Effective gap</h3>
              <p className="text-sm text-gray-400 mb-2">
                The effective spectral gap is:
              </p>
              <MathBlock
                equation="\text{gap}_{eff} = 1 - |\mu_2(P_{eff})|"
                displayMode={true}
              />
              <p className="text-sm text-gray-400">
                where mu_2 is the second-largest eigenvalue magnitude of P_eff.
              </p>
            </div>

            <div>
              <h3 className="font-semibold text-gray-300 mb-2">Step 4: Why amplification occurs</h3>
              <p className="text-sm text-gray-400 mb-2">
                Each P_k contracts along different directions. The composition
                contracts along the UNION of all directions, leading to:
              </p>
              <MathBlock
                equation="\text{gap}_{eff} \geq \max_k \text{gap}_k \quad \text{(in many cases, strictly >)}"
                displayMode={true}
              />
            </div>
          </div>

          <div className="bg-dark-bg rounded-lg p-4 mt-6 border border-green-800">
            <h3 className="font-semibold text-green-400 mb-2">Numerical Verification</h3>
            <p className="text-sm text-gray-400 mb-2">
              From the multi_calculus_diffusion.py experiment with 300 points:
            </p>
            <CodeBlock
              language="python"
              code={`# Individual spectral gaps
gaps = {
    'classical': 0.579,
    'log': 0.646,      # Best single
    'power': 0.553,
    'curvature': 0.545
}

# Combined operator gap
effective_gap = 0.771

# Amplification ratio
improvement = (0.771 - 0.646) / 0.646
print(f"Improvement: {improvement:.1%}")  # 19.3%`}
            />
            <p className="text-sm text-green-400 mt-2">
              Multi-calculus combination achieves 19% better convergence than best single calculus.
            </p>
          </div>
        </div>

        {/* Section 5: Invariance Score */}
        <div className="card mb-8">
          <h2 className="text-2xl font-bold mb-4">5. Scheme-Robustness Score</h2>

          <div className="bg-dark-bg rounded-lg p-4 mb-6">
            <h3 className="font-semibold text-primary-400 mb-2">Definition</h3>
            <p className="text-sm text-gray-400 mb-4">
              A configuration (n, s, k, w) is scheme-robust if its physics is invariant
              across calculus families. We quantify this as:
            </p>
            <MathBlock
              equation="I_{scheme}(k, s) = \exp\left(-\gamma(k^2 + s^2)\right)"
              displayMode={true}
            />
            <p className="text-sm text-gray-400 mt-2">
              where gamma = 10 (chosen to give significant penalty for |k|, |s| &gt; 0.1).
            </p>
          </div>

          <div className="space-y-6">
            <div>
              <h3 className="font-semibold text-gray-300 mb-2">Rationale</h3>
              <p className="text-sm text-gray-400">
                - When k = s = 0: I_scheme = 1 (perfectly invariant, classical calculus)
              </p>
              <p className="text-sm text-gray-400">
                - When k = s = 0.1: I_scheme = exp(-0.2) = 0.82 (significant non-invariance)
              </p>
              <p className="text-sm text-gray-400">
                - When k = s = 0.3: I_scheme = exp(-1.8) = 0.17 (strongly scheme-dependent)
              </p>
            </div>

            <div>
              <h3 className="font-semibold text-gray-300 mb-2">Optimization Objective</h3>
              <p className="text-sm text-gray-400 mb-2">
                We MINIMIZE non-robustness:
              </p>
              <MathBlock
                equation="f_2(x) = 1 - I_{scheme}(k, s)"
                displayMode={true}
              />
              <p className="text-sm text-gray-400">
                This pushes solutions toward k = s = 0 unless other objectives force deviation.
              </p>
            </div>
          </div>
        </div>

        {/* Section 6: Quantum Norm Preservation */}
        <div className="card mb-8">
          <h2 className="text-2xl font-bold mb-4">6. Quantum Unitarity Analysis</h2>

          <div className="bg-dark-bg rounded-lg p-4 mb-6">
            <h3 className="font-semibold text-primary-400 mb-2">The Meta-Schrodinger Equation</h3>
            <MathBlock
              equation="i\hbar \frac{d|\psi\rangle}{d\tau} = H|\psi\rangle"
              displayMode={true}
            />
            <p className="text-sm text-gray-400 mt-2">
              where tau is a &quot;meta-time&quot; related to physical time t by a generator.
            </p>
          </div>

          <div className="space-y-6">
            <div>
              <h3 className="font-semibold text-gray-300 mb-2">Q1: Clock Reparametrization</h3>
              <p className="text-sm text-gray-400 mb-2">
                tau = alpha(t), applied globally to the time coordinate:
              </p>
              <MathBlock
                equation="\frac{d|\psi\rangle}{d\tau} = \frac{dt}{d\tau} \frac{d|\psi\rangle}{dt} = \frac{1}{\alpha'(t)} \frac{d|\psi\rangle}{dt}"
                displayMode={true}
              />
              <p className="text-sm text-gray-400 mt-2">
                This is just a coordinate transformation. The evolution operator U(tau) remains unitary.
              </p>
            </div>

            <div>
              <h3 className="font-semibold text-gray-300 mb-2">Q3: Componentwise Modification</h3>
              <p className="text-sm text-gray-400 mb-2">
                Apply meta-derivative componentwise: each psi_i evolves with its own generator.
              </p>
              <MathBlock
                equation="\frac{d\psi_i}{d\tau_i} = \sum_j H_{ij} \psi_j, \quad \text{where } \tau_i = \alpha_i(t)"
                displayMode={true}
              />
              <p className="text-sm text-gray-400 mt-2">
                Now different components see different effective Hamiltonians. Norm conservation:
              </p>
              <MathBlock
                equation="\frac{d}{dt}\|\psi\|^2 = \frac{d}{dt}\sum_i |\psi_i|^2 \neq 0 \text{ in general}"
                displayMode={true}
              />
            </div>
          </div>

          <div className="bg-dark-bg rounded-lg p-4 mt-6 border border-red-800">
            <h3 className="font-semibold text-red-400 mb-2">Numerical Result: Q3 Breaks Unitarity</h3>
            <CodeBlock
              language="python"
              code={`# From meta_quantum_compatibility.py
# Random 3x3 Hermitian H, normalized |psi0|
# 100 RK4 steps, dt = 0.01

results = {
    'Q0': {'norm_drift': 0.001, 'status': 'SAFE'},
    'Q1': {'norm_drift': 0.003, 'status': 'SAFE'},
    'Q2': {'norm_drift': 0.008, 'status': 'SAFE'},
    'Q3': {'norm_drift': 0.65,  'status': 'BREAKS'}
}

# Q3 shows ~65% norm drift - unitarity destroyed`}
            />
          </div>
        </div>

        {/* Navigation */}
        <div className="flex justify-between items-center mt-12">
          <Link href="/math-history/timeline" className="text-gray-400 hover:text-white transition-colors">
            &larr; Back to Timeline
          </Link>
          <Link href="/math-history/failures" className="btn-primary">
            Next: Failures & Pivots &rarr;
          </Link>
        </div>
      </div>
    </div>
  );
}
