import MathBlock from '@/components/MathBlock';
import CodeBlock from '@/components/CodeBlock';
import Link from 'next/link';

export default function ExplorationPage() {
  return (
    <div className="section">
      <div className="mx-auto max-w-4xl">
        <div className="animate-fade-in">
          <p className="text-primary-400 font-mono text-sm mb-2">Chapter 01</p>
          <h1 className="text-4xl font-bold mb-4">
            <span className="gradient-text">The Hunch</span>
          </h1>
          <p className="text-xl text-gray-300 mb-8">
            What if some of the weirdness in modern physics is an artifact of using the wrong calculus?
          </p>
        </div>

        {/* The Initial Hunch */}
        <div className="card mb-8 animate-slide-up border-l-4 border-primary-500">
          <h2 className="text-2xl font-bold mb-4">The Initial Hunch</h2>
          <p className="text-gray-300 mb-4">
            Modern physics is full of puzzles: dark energy, the cosmological constant problem,
            the tension between quantum mechanics and general relativity. What if at least
            some of this weirdness is not fundamental physics - but an artifact of the
            mathematical framework we use to describe it?
          </p>
          <p className="text-gray-300">
            This hunch led to exploring <strong className="text-primary-400">non-Newtonian calculus</strong>,
            a framework developed by Grossman and Katz in the 1970s, where operations
            like multiplication replace addition as the fundamental operation. Could a different
            lens reveal different aspects of the same physical reality?
          </p>
        </div>

        {/* Time Series Geometry */}
        <div className="card mb-8">
          <h2 className="text-2xl font-bold mb-4">Time Series Geometry</h2>
          <p className="text-gray-300 mb-6">
            The first step was recognizing that physical observables often live on
            manifolds with natural geometric structure. Time series data - like the
            scale factor a(t) in cosmology - has intrinsic properties that depend on
            how we measure change:
          </p>

          <div className="space-y-6">
            <div className="bg-dark-bg rounded-lg p-4">
              <p className="text-gray-400 text-sm mb-2">Additive change (classical calculus):</p>
              <MathBlock
                equation="\frac{da}{dt} = \lim_{h \to 0} \frac{a(t+h) - a(t)}{h}"
                displayMode={true}
              />
            </div>

            <div className="bg-dark-bg rounded-lg p-4">
              <p className="text-gray-400 text-sm mb-2">Multiplicative change (geometric calculus):</p>
              <MathBlock
                equation="\frac{d^*a}{dt^*} = \lim_{h \to 0} \left(\frac{a(t+h)}{a(t)}\right)^{1/h}"
                displayMode={true}
              />
            </div>
          </div>

          <p className="text-gray-300 mt-6">
            For exponential growth (like compound interest or radioactive decay),
            multiplicative calculus gives constant derivatives - exactly what you would expect
            for a natural description of exponential processes.
          </p>
        </div>

        {/* The Framework */}
        <div className="card mb-8">
          <h2 className="text-2xl font-bold mb-4">The Meta-Calculus Framework</h2>
          <p className="text-gray-300 mb-6">
            We generalized this idea into a meta-calculus framework where the choice of
            calculus becomes a parameter. Different generators produce different calculi:
          </p>

          <div className="space-y-6">
            <div>
              <p className="text-gray-400 text-sm mb-2">The meta-derivative with generators alpha and beta:</p>
              <MathBlock
                equation="D^*f/dx^* = \frac{v(f(x))}{u(x)} \cdot \frac{\beta'(f(x)) \cdot f'(x)}{\alpha'(x)}"
                displayMode={true}
              />
            </div>

            <div>
              <p className="text-gray-400 text-sm mb-2">When alpha = beta = Identity, this reduces to standard calculus:</p>
              <MathBlock
                equation="D^*f/dx^* = \frac{df}{dx}"
                displayMode={true}
              />
            </div>
          </div>
        </div>

        {/* Application to Cosmology */}
        <div className="card mb-8">
          <h2 className="text-2xl font-bold mb-4">Application to Cosmology</h2>
          <p className="text-gray-300 mb-6">
            We applied this framework to the Friedmann equations of cosmology.
            The scale factor evolution a(t) = t^n gets modified:
          </p>

          <div className="bg-dark-bg rounded-lg p-4 mb-6">
            <p className="text-gray-400 text-sm mb-2">Classical Friedmann:</p>
            <MathBlock
              equation="H^2 = \frac{8\pi G}{3}\rho"
              displayMode={true}
            />
          </div>

          <div className="bg-dark-bg rounded-lg p-4 mb-6">
            <p className="text-gray-400 text-sm mb-2">Meta-Friedmann with GUC corrections:</p>
            <MathBlock
              equation="\mathcal{L}_{meta} = -\frac{3}{8\pi G} a \cdot t^{2k} \cdot \dot{a}^2 - a^3 \rho(a)"
              displayMode={true}
            />
          </div>

          <p className="text-gray-300">
            The parameter <code className="text-primary-400">k</code> represents
            the meta-weight - how much the GUC (Generalized Uncertainty Calculus)
            corrections affect the dynamics.
          </p>
        </div>

        {/* The Einstein Compatibility Hierarchy */}
        <div className="card mb-8">
          <h2 className="text-2xl font-bold mb-4">Einstein Compatibility Hierarchy</h2>
          <p className="text-gray-300 mb-4">
            We discovered a hierarchy of compatibility levels between
            meta-calculus and General Relativity:
          </p>

          <div className="space-y-4">
            <div className="bg-dark-bg rounded p-4 border-l-2 border-green-500">
              <h3 className="font-semibold text-green-400">Level 1: Geodesic Limit</h3>
              <p className="text-sm text-gray-400">
                Particles on geodesics: Always compatible, any calculus works
              </p>
            </div>
            <div className="bg-dark-bg rounded p-4 border-l-2 border-yellow-500">
              <h3 className="font-semibold text-yellow-400">Level 2: Weak Field</h3>
              <p className="text-sm text-gray-400">
                Linearized GR: Requires constraints on generator functions
              </p>
            </div>
            <div className="bg-dark-bg rounded p-4 border-l-2 border-orange-500">
              <h3 className="font-semibold text-orange-400">Level 3: Full Nonlinear</h3>
              <p className="text-sm text-gray-400">
                Full Einstein equations: Strong constraints, only specific calculi work
              </p>
            </div>
            <div className="bg-dark-bg rounded p-4 border-l-2 border-red-500">
              <h3 className="font-semibold text-red-400">Level 4: Observational</h3>
              <p className="text-sm text-gray-400">
                BBN/CMB constraints: |s| &lt; 0.05, |k| &lt; 0.03
              </p>
            </div>
          </div>
        </div>

        {/* Initial Code */}
        <div className="card mb-8">
          <h2 className="text-2xl font-bold mb-4">Initial Implementation</h2>
          <p className="text-gray-300 mb-4">
            The core generator and meta-derivative classes:
          </p>
          <CodeBlock
            language="python"
            code={`import numpy as np
from abc import ABC, abstractmethod

class Generator(ABC):
    """Base class for calculus generators."""

    @abstractmethod
    def __call__(self, x: np.ndarray) -> np.ndarray:
        pass

    @abstractmethod
    def inverse(self, y: np.ndarray) -> np.ndarray:
        pass

    @abstractmethod
    def derivative(self, x: np.ndarray) -> np.ndarray:
        pass

class Log(Generator):
    """Logarithmic generator for multiplicative calculus."""

    def __call__(self, x):
        return np.log(x)

    def inverse(self, y):
        return np.exp(y)

    def derivative(self, x):
        return 1.0 / x

class MetaDerivative:
    """Generalized derivative operator."""

    def __init__(self, alpha: Generator, beta: Generator):
        self.alpha = alpha
        self.beta = beta

    def __call__(self, f, x, h=1e-7):
        # Numerical approximation
        f_plus = f(x + h)
        f_minus = f(x - h)

        # Transform through generators
        beta_f_plus = self.beta(f_plus)
        beta_f_minus = self.beta(f_minus)
        alpha_plus = self.alpha(x + h)
        alpha_minus = self.alpha(x - h)

        return (beta_f_plus - beta_f_minus) / (alpha_plus - alpha_minus)`}
          />
        </div>

        {/* The Key Insight */}
        <div className="card mb-8 bg-gradient-to-r from-primary-900/30 to-accent-900/30">
          <h2 className="text-2xl font-bold mb-4">The Key Insight</h2>
          <p className="text-gray-300 mb-4">
            After weeks of exploration, a crucial realization emerged:
          </p>
          <blockquote className="border-l-4 border-primary-500 pl-4 py-2 my-4">
            <p className="text-xl text-primary-300 italic">
              The geometry is real; the calculus is a lens.
            </p>
          </blockquote>
          <p className="text-gray-300">
            Instead of asking which calculus is correct, we should ask
            what structure survives <em>all</em> calculi? This led to the
            v2.0 reframing: <strong className="text-primary-400">scheme-robust observables</strong>.
          </p>
        </div>

        {/* Navigation */}
        <div className="flex justify-between items-center mt-12">
          <Link href="/story" className="text-gray-400 hover:text-white transition-colors">
            &larr; Back to Story
          </Link>
          <Link href="/story/audits" className="btn-primary">
            Next: AI & Audits &rarr;
          </Link>
        </div>
      </div>
    </div>
  );
}
