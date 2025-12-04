import CodeBlock from '@/components/CodeBlock';
import Link from 'next/link';

export default function CodePage() {
  return (
    <div className="section">
      <div className="mx-auto max-w-4xl">
        <div className="animate-fade-in">
          <p className="text-primary-400 font-mono text-sm mb-2">Source Code</p>
          <h1 className="text-4xl font-bold mb-4">
            <span className="gradient-text">Code & Methods</span>
          </h1>
          <p className="text-xl text-gray-300 mb-8">
            The complete Python implementation, from generators to optimization
          </p>
        </div>

        {/* Repository Structure */}
        <div className="card mb-8 animate-slide-up">
          <h2 className="text-2xl font-bold mb-4">Repository Structure</h2>
          <div className="bg-dark-bg rounded-lg p-4 font-mono text-sm text-gray-300">
            <pre>{`meta-calculus-toolkit/
|-- meta_calculus/           # Core Python library
|   |-- __init__.py
|   |-- generators.py        # Generator functions
|   |-- derivatives.py       # Meta-derivative operators
|   |-- scheme_robust.py     # Multi-calculus framework
|   |-- frw_cosmology.py     # FRW model implementation
|   |-- moo_integration.py   # pymoo + Global MOO integration
|   +-- validation.py        # Test suite
|
|-- docs/                     # Documentation
|   |-- EINSTEIN_COMPATIBILITY_HIERARCHY.md
|   |-- MULTI_CALCULUS_REFRAMING.md
|   |-- OPTIMIZER_COMPARISON_RESULTS.md
|   +-- research/            # Research notes
|
|-- simulations/             # Numerical experiments
|-- results/                 # Optimization outputs
|-- notebooks/               # Jupyter analysis
+-- portfolio-site/          # This Next.js site`}</pre>
          </div>
        </div>

        {/* Core Generator Implementation */}
        <div className="card mb-8">
          <h2 className="text-2xl font-bold mb-4">Generator Functions</h2>
          <p className="text-gray-300 mb-4">
            Generators transform coordinates to make relationships linear:
          </p>
          <CodeBlock
            language="python"
            code={`from abc import ABC, abstractmethod
import numpy as np

class Generator(ABC):
    """Base class for calculus generators."""

    @abstractmethod
    def __call__(self, x: np.ndarray) -> np.ndarray:
        """Forward transform."""
        pass

    @abstractmethod
    def inverse(self, y: np.ndarray) -> np.ndarray:
        """Inverse transform."""
        pass

    @abstractmethod
    def derivative(self, x: np.ndarray) -> np.ndarray:
        """Derivative of forward transform."""
        pass

class Identity(Generator):
    """Classical calculus generator."""
    def __call__(self, x): return x
    def inverse(self, y): return y
    def derivative(self, x): return np.ones_like(x)

class Log(Generator):
    """Logarithmic generator for multiplicative calculus."""
    def __call__(self, x): return np.log(np.abs(x) + 1e-10)
    def inverse(self, y): return np.exp(y)
    def derivative(self, x): return 1.0 / (np.abs(x) + 1e-10)

class Power(Generator):
    """Power-law generator: alpha(x) = x^p"""
    def __init__(self, p: float = 0.5):
        self.p = p

    def __call__(self, x):
        return np.sign(x) * np.abs(x) ** self.p

    def inverse(self, y):
        return np.sign(y) * np.abs(y) ** (1/self.p)

    def derivative(self, x):
        return self.p * np.abs(x) ** (self.p - 1)`}
          />
        </div>

        {/* Meta-Derivative */}
        <div className="card mb-8">
          <h2 className="text-2xl font-bold mb-4">Meta-Derivative Operator</h2>
          <p className="text-gray-300 mb-4">
            The generalized derivative with weight functions u(x) and v(y):
          </p>
          <CodeBlock
            language="python"
            code={`class MetaDerivative:
    """
    Generalized derivative: D*f/dx* = (v(f)/u(x)) * beta'(f) * f'(x) / alpha'(x)

    When alpha = beta = Identity, u = v = 1: reduces to classical d/dx
    """

    def __init__(
        self,
        alpha: Generator,
        beta: Generator,
        u: Callable = lambda x: 1.0,
        v: Callable = lambda y: 1.0
    ):
        self.alpha = alpha
        self.beta = beta
        self.u = u
        self.v = v

    def __call__(self, f: Callable, x: np.ndarray, h: float = 1e-7) -> np.ndarray:
        """Compute meta-derivative numerically."""
        # Classical derivative of f
        f_prime = (f(x + h) - f(x - h)) / (2 * h)

        # Generator derivatives
        alpha_prime = self.alpha.derivative(x)
        beta_prime = self.beta.derivative(f(x))

        # Weight factors
        weight = self.v(f(x)) / self.u(x)

        # Meta-derivative formula
        return weight * beta_prime * f_prime / alpha_prime

    def is_linear(self, f: Callable, x_range: tuple, tol: float = 0.01) -> bool:
        """Check if f is linear in transformed coordinates."""
        x = np.linspace(*x_range, 100)
        y = f(x)

        # Transform coordinates
        alpha_x = self.alpha(x)
        beta_y = self.beta(y)

        # Linear regression
        slope, intercept = np.polyfit(alpha_x, beta_y, 1)
        predicted = slope * alpha_x + intercept

        # R-squared
        ss_res = np.sum((beta_y - predicted) ** 2)
        ss_tot = np.sum((beta_y - np.mean(beta_y)) ** 2)
        r_squared = 1 - ss_res / (ss_tot + 1e-10)

        return r_squared > (1 - tol)`}
          />
        </div>

        {/* Multi-Calculus Framework */}
        <div className="card mb-8">
          <h2 className="text-2xl font-bold mb-4">Multi-Calculus Framework (v2.0)</h2>
          <p className="text-gray-300 mb-4">
            The key innovation: using families of calculi to extract scheme-robust observables:
          </p>
          <CodeBlock
            language="python"
            code={`class CalculusEnsemble:
    """Collection of calculi for scheme-robust analysis."""

    def __init__(self, calculi: List[Tuple[str, Generator, Generator]]):
        self.calculi = calculi  # [(name, alpha, beta), ...]

    def mixed_operator(self, X: np.ndarray, sigma: float = 0.5) -> np.ndarray:
        """
        Compose Markov operators: P_mix = P_n @ ... @ P_1

        Key result: gap(P_mix) ~ 4x gap(P_i)
        Structure surviving ALL calculi = "physical"
        """
        n = X.shape[0]
        P_mix = np.eye(n)

        for name, alpha, beta in self.calculi:
            # Feature map
            phi = np.column_stack([alpha(X[:, i]) for i in range(X.shape[1])])

            # Gaussian kernel
            D = pairwise_distances(phi)
            K = np.exp(-D**2 / (2 * sigma**2))

            # Markov normalization
            P = K / K.sum(axis=1, keepdims=True)

            # Compose
            P_mix = P @ P_mix

        return P_mix

    def invariance_score(self, X: np.ndarray, f: np.ndarray) -> float:
        """
        How scheme-robust is feature f?
        High score = survives all calculi = likely physical
        """
        roughness_scores = []

        for name, alpha, beta in self.calculi:
            # Laplacian in this calculus
            L = self._laplacian(X, alpha)

            # Roughness = f^T L f / f^T f
            roughness = np.dot(f, L @ f) / np.dot(f, f)
            roughness_scores.append(roughness)

        # High invariance = low roughness in ALL calculi
        return 1.0 / (1.0 + np.mean(roughness_scores))`}
          />
        </div>

        {/* MOO Integration */}
        <div className="card mb-8">
          <h2 className="text-2xl font-bold mb-4">Multi-Objective Optimization</h2>
          <p className="text-gray-300 mb-4">
            We used both pymoo and Global MOO for independent verification:
          </p>
          <CodeBlock
            language="python"
            code={`from pymoo.core.problem import Problem
from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.optimize import minimize
import os

class MetaFriedmannProblem(Problem):
    """
    Multi-objective optimization for meta-calculus cosmology.

    Decision variables: x = [n, s, k, w]
    Objectives:
        1. chi2: Fit to observations
        2. 1 - I_scheme: Scheme non-robustness
        3. constraint_tension: Distance from constraint boundaries
    """

    def __init__(self):
        super().__init__(
            n_var=4,
            n_obj=3,
            n_ieq_constr=4,
            xl=np.array([0.3, -0.1, -0.05, -1.0]),
            xu=np.array([0.9, 0.1, 0.05, 0.0]),
        )

    def _evaluate(self, X, out, *args, **kwargs):
        n, s, k, w = X[:, 0], X[:, 1], X[:, 2], X[:, 3]

        # Objective 1: Chi-squared
        n_pred = self._compute_n_act(s, w)
        chi2 = ((n - n_pred) ** 2) / 0.01

        # Objective 2: Scheme non-robustness
        invariance = np.exp(-10 * (k**2 + s**2))
        non_robust = 1.0 - invariance

        # Objective 3: Constraint tension
        tension = np.abs(s) / 0.05 + np.abs(k) / 0.03

        out["F"] = np.column_stack([chi2, non_robust, tension])
        out["G"] = np.column_stack([
            np.abs(s) - 0.05,  # BBN constraint
            np.abs(k) - 0.03,  # CMB constraint
            -w - 1.0, w        # Energy conditions
        ])

# Run optimization
algorithm = NSGA2(pop_size=100)
result = minimize(
    MetaFriedmannProblem(),
    algorithm,
    ('n_gen', 50),
    seed=42,
    verbose=True
)

# Pareto front
pareto_X = result.X  # Decision variables
pareto_F = result.F  # Objective values`}
          />
        </div>

        {/* Environment Variables */}
        <div className="card mb-8">
          <h2 className="text-2xl font-bold mb-4">Environment Configuration</h2>
          <p className="text-gray-300 mb-4">
            API keys and sensitive configuration via environment variables:
          </p>
          <CodeBlock
            language="bash"
            code={`# .env.local (NOT committed to git)
GLOBALMOO_API_KEY=your_api_key_here
GLOBALMOO_API_URL=https://app.globalmoo.com/api/

# Access in Python
import os

GLOBALMOO_API_KEY = os.environ.get('GLOBALMOO_API_KEY')
GLOBALMOO_API_URL = os.environ.get(
    'GLOBALMOO_API_URL',
    'https://app.globalmoo.com/api/'
)

# Access in Next.js (server-side only)
# next.config.js
module.exports = {
  serverRuntimeConfig: {
    globalmooApiKey: process.env.GLOBALMOO_API_KEY,
  },
}`}
          />
        </div>

        {/* Key Formulas Reference */}
        <div className="card mb-8">
          <h2 className="text-2xl font-bold mb-4">Key Formulas Reference</h2>
          <div className="space-y-4 text-sm">
            <div className="bg-dark-bg rounded-lg p-4">
              <h3 className="font-semibold text-primary-400 mb-2">n_act(s, w)</h3>
              <code className="text-gray-300 font-mono">
                n_act = [-(3ws + 2s - 2) + sqrt(Delta)] / [6(1+w)]
              </code>
              <p className="text-gray-500 mt-1">Where Delta = 9s^2*w^2 - 8s^2 + 4s + 4</p>
            </div>
            <div className="bg-dark-bg rounded-lg p-4">
              <h3 className="font-semibold text-accent-400 mb-2">Invariance Score</h3>
              <code className="text-gray-300 font-mono">
                I_scheme = exp(-10 * (k^2 + s^2))
              </code>
              <p className="text-gray-500 mt-1">Perfect invariance when k=0, s=0</p>
            </div>
            <div className="bg-dark-bg rounded-lg p-4">
              <h3 className="font-semibold text-primary-400 mb-2">Observational Constraints</h3>
              <code className="text-gray-300 font-mono">
                |s| &lt;= 0.05, |k| &lt;= 0.03, -1 &lt;= w &lt;= 0
              </code>
              <p className="text-gray-500 mt-1">BBN + CMB + energy conditions</p>
            </div>
          </div>
        </div>

        {/* Tech Stack */}
        <div className="card mb-8">
          <h2 className="text-2xl font-bold mb-4">Tech Stack</h2>
          <div className="grid gap-4 md:grid-cols-2">
            <div className="bg-dark-bg rounded-lg p-4">
              <h3 className="font-semibold text-primary-400 mb-2">Python Core</h3>
              <ul className="text-sm text-gray-400 space-y-1">
                <li>- NumPy / SciPy for numerics</li>
                <li>- pymoo for NSGA-II optimization</li>
                <li>- <a href="https://github.com/globalMOO/gmoo-sdk-suite" className="text-primary-400 hover:underline">globalmoo-sdk</a> for Global MOO API</li>
                <li>- SymPy for symbolic math</li>
              </ul>
            </div>
            <div className="bg-dark-bg rounded-lg p-4">
              <h3 className="font-semibold text-accent-400 mb-2">Web Frontend</h3>
              <ul className="text-sm text-gray-400 space-y-1">
                <li>- Next.js 14 (App Router)</li>
                <li>- Tailwind CSS</li>
                <li>- KaTeX for math rendering</li>
                <li>- Prism.js for syntax highlighting</li>
              </ul>
            </div>
          </div>
        </div>

        {/* License */}
        <div className="card">
          <h2 className="text-2xl font-bold mb-4">License & Attribution</h2>
          <div className="space-y-4 text-gray-300">
            <div>
              <h3 className="font-semibold text-primary-400 mb-2">License</h3>
              <p className="text-sm">
                MIT License - Free to use, modify, and distribute with attribution
              </p>
            </div>
            <div>
              <h3 className="font-semibold text-accent-400 mb-2">References</h3>
              <ul className="text-sm text-gray-400 space-y-1">
                <li>- Grossman & Katz (1972). Non-Newtonian Calculus</li>
                <li>- Blank (2020). An Introduction to Pythagorean Arithmetic</li>
                <li>- <a href="https://pymoo.org" className="text-accent-400 hover:underline">pymoo</a>: Multi-objective Optimization in Python</li>
                <li>- <a href="https://github.com/globalMOO/gmoo-sdk-suite" className="text-accent-400 hover:underline">Global MOO SDK Suite</a>: Cloud optimization API</li>
                <li>- <a href="https://globalmoo.gitbook.io/globalmoo-documentation" className="text-accent-400 hover:underline">Global MOO Docs</a></li>
              </ul>
            </div>
          </div>
        </div>

        {/* Navigation */}
        <div className="flex justify-between items-center mt-12">
          <Link href="/results" className="text-gray-400 hover:text-white transition-colors">
            &larr; Back to Results
          </Link>
          <Link href="/" className="btn-primary">
            Back to Home
          </Link>
        </div>
      </div>
    </div>
  );
}
