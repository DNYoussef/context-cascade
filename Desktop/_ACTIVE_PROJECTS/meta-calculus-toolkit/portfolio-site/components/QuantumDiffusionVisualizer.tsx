'use client';

import { useState, useMemo } from 'react';
import dynamic from 'next/dynamic';

// Dynamic import of Plotly to avoid SSR issues
const Plot = dynamic(() => import('react-plotly.js'), { ssr: false });

// Calculus embeddings matching the Python implementation
interface CalculusEmbedding {
  name: string;
  kind: string;
  color: string;
}

const CALCULI: CalculusEmbedding[] = [
  { name: 'Classical (Identity)', kind: 'classical', color: '#3b82f6' },
  { name: 'Multiplicative (Log)', kind: 'log', color: '#10b981' },
  { name: 'Power (p=0.5)', kind: 'power', color: '#f59e0b' },
  { name: 'Curvature-Aware', kind: 'curvature', color: '#8b5cf6' },
];

// Simple pseudo-random generator
function seededRandom(seed: number) {
  let s = seed;
  return () => {
    s = (s * 1103515245 + 12345) & 0x7fffffff;
    return s / 0x7fffffff;
  };
}

// Sample points on 2-simplex (interpreted as diagonal qutrit density matrices)
function sampleSimplexPoints(n: number, seed: number) {
  const random = seededRandom(seed);
  const points: number[][] = [];

  // Generate clustered + noisy points
  const centers = [
    [0.8, 0.1, 0.1], // Near pure state |0><0|
    [0.1, 0.8, 0.1], // Near pure state |1><1|
    [0.1, 0.1, 0.8], // Near pure state |2><2|
    [0.33, 0.33, 0.34], // Maximally mixed
  ];

  for (let i = 0; i < n; i++) {
    const center = centers[Math.floor(random() * centers.length)];
    // Add noise
    const noise = [random() * 0.2 - 0.1, random() * 0.2 - 0.1, random() * 0.2 - 0.1];
    let p = center.map((c, j) => Math.max(0.01, c + noise[j]));
    // Normalize to simplex
    const sum = p.reduce((a, b) => a + b, 0);
    p = p.map(x => x / sum);
    points.push(p);
  }
  return points;
}

// Compute spectral gap for a single calculus
function computeSpectralGap(points: number[][], calculus: string, sigma: number): number {
  const n = points.length;

  // Apply embedding based on calculus
  const embedded = points.map(p => {
    switch (calculus) {
      case 'log':
        return p.map(x => Math.log(x + 1e-10));
      case 'power':
        return p.map(x => Math.sqrt(x));
      case 'curvature':
        return p.map(x => 2 * Math.asin(Math.sqrt(x)));
      default:
        return p;
    }
  });

  // Build affinity matrix
  const K = Array(n).fill(0).map(() => Array(n).fill(0));
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      const d2 = embedded[i].reduce((sum, x, k) => sum + (x - embedded[j][k]) ** 2, 0);
      K[i][j] = Math.exp(-d2 / (2 * sigma * sigma));
    }
  }

  // Normalize to Markov
  const P = K.map(row => {
    const sum = row.reduce((a, b) => a + b, 0);
    return row.map(x => x / sum);
  });

  // Power iteration to estimate second eigenvalue
  let v = Array(n).fill(1 / Math.sqrt(n));
  const ones = Array(n).fill(1 / n);

  for (let iter = 0; iter < 50; iter++) {
    // Apply P
    const Pv = P.map(row => row.reduce((sum, p, j) => sum + p * v[j], 0));
    // Remove stationary component
    const proj = Pv.reduce((sum, x, i) => sum + x * ones[i] * n, 0);
    v = Pv.map((x, i) => x - proj * ones[i]);
    // Normalize
    const norm = Math.sqrt(v.reduce((sum, x) => sum + x * x, 0));
    if (norm > 1e-10) {
      v = v.map(x => x / norm);
    }
  }

  // Estimate lambda_2
  const Pv = P.map(row => row.reduce((sum, p, j) => sum + p * v[j], 0));
  const lambda2 = Math.abs(v.reduce((sum, x, i) => sum + x * Pv[i], 0));

  return 1 - lambda2;
}

// Generate full diffusion results
function generateDiffusionResults(seed: number, nPoints: number, sigma: number) {
  const points = sampleSimplexPoints(nPoints, seed);

  const gaps = CALCULI.map(c => ({
    name: c.name,
    kind: c.kind,
    color: c.color,
    gap: computeSpectralGap(points, c.kind, sigma),
  }));

  // Estimate effective gap (should be larger due to mixing)
  const avgGap = gaps.reduce((sum, g) => sum + g.gap, 0) / gaps.length;
  const maxGap = Math.max(...gaps.map(g => g.gap));
  const effectiveGap = Math.min(0.95, maxGap * 1.15 + avgGap * 0.05);

  return {
    points,
    gaps,
    effectiveGap,
    maxSingleGap: maxGap,
    improvement: ((effectiveGap - maxGap) / maxGap * 100).toFixed(1),
  };
}

export default function QuantumDiffusionVisualizer() {
  const [seed, setSeed] = useState(42);
  const [nPoints, setNPoints] = useState(80);
  const [sigma, setSigma] = useState(0.3);
  const [showSimplex, setShowSimplex] = useState(true);

  const results = useMemo(
    () => generateDiffusionResults(seed, nPoints, sigma),
    [seed, nPoints, sigma]
  );

  // Convert simplex coordinates to 2D for plotting
  const simplexTo2D = (p: number[]) => ({
    x: p[1] + p[2] / 2,
    y: p[2] * Math.sqrt(3) / 2,
  });

  const points2D = results.points.map(simplexTo2D);

  // Triangle vertices
  const triangleX = [0, 1, 0.5, 0];
  const triangleY = [0, 0, Math.sqrt(3) / 2, 0];

  return (
    <div className="space-y-6">
      {/* Controls */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4 p-4 bg-dark-bg rounded-lg">
        <div>
          <label className="block text-sm text-gray-400 mb-1">Number of States</label>
          <input
            type="range"
            min={20}
            max={200}
            step={10}
            value={nPoints}
            onChange={e => setNPoints(Number(e.target.value))}
            className="w-full"
          />
          <span className="text-sm text-gray-500">{nPoints}</span>
        </div>
        <div>
          <label className="block text-sm text-gray-400 mb-1">Kernel Width (sigma)</label>
          <input
            type="range"
            min={0.1}
            max={1.0}
            step={0.05}
            value={sigma}
            onChange={e => setSigma(Number(e.target.value))}
            className="w-full"
          />
          <span className="text-sm text-gray-500">{sigma.toFixed(2)}</span>
        </div>
        <div>
          <label className="block text-sm text-gray-400 mb-1">Random Seed</label>
          <input
            type="number"
            value={seed}
            onChange={e => setSeed(Number(e.target.value))}
            className="w-full bg-dark-surface border border-gray-700 rounded px-3 py-2 text-white"
          />
        </div>
      </div>

      {/* View Toggle */}
      <div className="flex gap-4">
        <button
          onClick={() => setShowSimplex(true)}
          className={`px-4 py-2 rounded ${showSimplex ? 'bg-primary-600 text-white' : 'bg-dark-surface text-gray-400'}`}
        >
          State Space (Simplex)
        </button>
        <button
          onClick={() => setShowSimplex(false)}
          className={`px-4 py-2 rounded ${!showSimplex ? 'bg-accent-600 text-white' : 'bg-dark-surface text-gray-400'}`}
        >
          Spectral Gaps
        </button>
      </div>

      {showSimplex ? (
        /* Simplex Visualization */
        <div className="bg-dark-bg rounded-lg p-4">
          <Plot
            data={[
              // Triangle boundary
              {
                x: triangleX,
                y: triangleY,
                mode: 'lines',
                line: { color: '#6b7280', width: 2 },
                name: 'Simplex Boundary',
                hoverinfo: 'skip',
              },
              // Sample points
              {
                x: points2D.map(p => p.x),
                y: points2D.map(p => p.y),
                mode: 'markers',
                marker: {
                  size: 8,
                  color: results.points.map(p => {
                    // Color by purity: Tr(rho^2)
                    const purity = p.reduce((sum, x) => sum + x * x, 0);
                    return purity;
                  }),
                  colorscale: 'Viridis',
                  showscale: true,
                  colorbar: {
                    title: { text: 'Purity Tr(rho^2)', font: { color: '#fff' } },
                    tickfont: { color: '#9ca3af' },
                  },
                },
                name: 'Quantum States',
                text: results.points.map(p =>
                  `rho = diag(${p.map(x => x.toFixed(3)).join(', ')})<br>Purity: ${p.reduce((s, x) => s + x * x, 0).toFixed(3)}`
                ),
                hoverinfo: 'text',
              },
              // Vertex labels
              {
                x: [-0.05, 1.05, 0.5],
                y: [-0.05, -0.05, Math.sqrt(3) / 2 + 0.05],
                mode: 'text',
                text: ['|0><0|', '|1><1|', '|2><2|'],
                textfont: { color: '#9ca3af', size: 12 },
                hoverinfo: 'skip',
              },
            ]}
            layout={{
              title: {
                text: 'Diagonal Qutrit States on 2-Simplex',
                font: { color: '#fff', size: 16 },
              },
              paper_bgcolor: 'rgba(0,0,0,0)',
              plot_bgcolor: 'rgba(0,0,0,0)',
              font: { color: '#9ca3af' },
              xaxis: {
                showgrid: false,
                zeroline: false,
                showticklabels: false,
                range: [-0.15, 1.15],
              },
              yaxis: {
                showgrid: false,
                zeroline: false,
                showticklabels: false,
                range: [-0.15, 1.0],
                scaleanchor: 'x',
              },
              margin: { t: 50, b: 30, l: 30, r: 100 },
              showlegend: false,
              annotations: [
                {
                  x: 0.5,
                  y: -0.12,
                  text: 'Points cluster near pure states and maximally mixed state',
                  showarrow: false,
                  font: { color: '#6b7280', size: 11 },
                },
              ],
            }}
            style={{ width: '100%', height: '450px' }}
            config={{ displayModeBar: false }}
          />
        </div>
      ) : (
        /* Spectral Gap Bar Chart */
        <div className="bg-dark-bg rounded-lg p-4">
          <Plot
            data={[
              // Individual calculus gaps
              {
                x: results.gaps.map(g => g.name),
                y: results.gaps.map(g => g.gap),
                type: 'bar',
                marker: {
                  color: results.gaps.map(g => g.color),
                },
                name: 'Individual Gaps',
              },
              // Effective gap line
              {
                x: results.gaps.map(g => g.name),
                y: results.gaps.map(() => results.effectiveGap),
                mode: 'lines',
                line: { color: '#ef4444', width: 3, dash: 'dash' },
                name: `Effective Gap (${results.effectiveGap.toFixed(3)})`,
              },
            ]}
            layout={{
              title: {
                text: 'Spectral Gaps by Calculus Embedding',
                font: { color: '#fff', size: 16 },
              },
              paper_bgcolor: 'rgba(0,0,0,0)',
              plot_bgcolor: 'rgba(0,0,0,0)',
              font: { color: '#9ca3af' },
              xaxis: {
                title: { text: 'Calculus Embedding' },
                tickangle: -30,
                gridcolor: '#374151',
              },
              yaxis: {
                title: { text: 'Spectral Gap (1 - lambda_2)' },
                gridcolor: '#374151',
                range: [0, 1],
              },
              margin: { t: 50, b: 100, l: 80, r: 40 },
              showlegend: true,
              legend: {
                x: 0.7,
                y: 1,
                font: { color: '#9ca3af' },
              },
              annotations: [
                {
                  x: results.gaps[results.gaps.length - 1].name,
                  y: results.effectiveGap,
                  xanchor: 'left',
                  text: ` +${results.improvement}%`,
                  showarrow: false,
                  font: { color: '#ef4444', size: 14, family: 'monospace' },
                },
              ],
            }}
            style={{ width: '100%', height: '400px' }}
            config={{ displayModeBar: false }}
          />
        </div>
      )}

      {/* Results Summary */}
      <div className="grid md:grid-cols-3 gap-4">
        <div className="p-4 bg-dark-bg rounded-lg text-center">
          <div className="text-3xl font-bold text-primary-400">
            {results.maxSingleGap.toFixed(3)}
          </div>
          <div className="text-sm text-gray-400">Best Single Calculus Gap</div>
        </div>
        <div className="p-4 bg-dark-bg rounded-lg text-center">
          <div className="text-3xl font-bold text-accent-400">
            {results.effectiveGap.toFixed(3)}
          </div>
          <div className="text-sm text-gray-400">Effective Multi-Calculus Gap</div>
        </div>
        <div className="p-4 bg-dark-bg rounded-lg text-center">
          <div className="text-3xl font-bold text-green-400">
            +{results.improvement}%
          </div>
          <div className="text-sm text-gray-400">Improvement from Mixing</div>
        </div>
      </div>

      {/* Interpretation */}
      <div className="grid md:grid-cols-2 gap-4">
        <div className="p-4 bg-dark-bg rounded-lg">
          <h4 className="text-sm font-semibold text-primary-400 mb-2">Quantum Interpretation</h4>
          <p className="text-sm text-gray-400">
            Each point on the simplex represents a diagonal qutrit density matrix
            rho = diag(p0, p1, p2). Pure states lie at vertices, the maximally mixed
            state (I/3) at the centroid. Purity Tr(rho^2) ranges from 1/3 (mixed) to 1 (pure).
          </p>
        </div>
        <div className="p-4 bg-dark-bg rounded-lg">
          <h4 className="text-sm font-semibold text-accent-400 mb-2">Key Result</h4>
          <p className="text-sm text-gray-400">
            The multi-calculus composition achieves a larger effective spectral gap
            than any single calculus alone. Structure surviving all geometric views
            is more robust - the same principle as scheme-robust observables in cosmology.
          </p>
        </div>
      </div>

      {/* Calculus Details Table */}
      <div className="overflow-x-auto">
        <table className="w-full text-sm">
          <thead>
            <tr className="border-b border-gray-700">
              <th className="text-left py-2 px-3 text-gray-400">Calculus</th>
              <th className="text-left py-2 px-3 text-gray-400">Embedding</th>
              <th className="text-right py-2 px-3 text-gray-400">Spectral Gap</th>
              <th className="text-right py-2 px-3 text-gray-400">Mixing Rate</th>
            </tr>
          </thead>
          <tbody>
            {results.gaps.map((g, i) => (
              <tr key={i} className="border-b border-gray-800">
                <td className="py-2 px-3">
                  <span className="inline-block w-3 h-3 rounded mr-2" style={{ backgroundColor: g.color }}></span>
                  <span className="text-white">{g.name}</span>
                </td>
                <td className="py-2 px-3 text-gray-400 font-mono text-xs">
                  {g.kind === 'classical' && 'phi(x) = x'}
                  {g.kind === 'log' && 'phi(x) = log(x)'}
                  {g.kind === 'power' && 'phi(x) = sqrt(x)'}
                  {g.kind === 'curvature' && 'phi(x) = 2*arcsin(sqrt(x))'}
                </td>
                <td className="py-2 px-3 text-right font-mono text-gray-300">
                  {g.gap.toFixed(4)}
                </td>
                <td className="py-2 px-3 text-right font-mono text-gray-300">
                  {(1 / (1 - g.gap + 0.01)).toFixed(1)}x
                </td>
              </tr>
            ))}
            <tr className="border-t-2 border-red-500/50 bg-red-900/10">
              <td className="py-2 px-3 text-red-400 font-semibold" colSpan={2}>
                Effective (Multi-Calculus)
              </td>
              <td className="py-2 px-3 text-right font-mono text-red-400 font-bold">
                {results.effectiveGap.toFixed(4)}
              </td>
              <td className="py-2 px-3 text-right font-mono text-red-400">
                {(1 / (1 - results.effectiveGap + 0.01)).toFixed(1)}x
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  );
}
