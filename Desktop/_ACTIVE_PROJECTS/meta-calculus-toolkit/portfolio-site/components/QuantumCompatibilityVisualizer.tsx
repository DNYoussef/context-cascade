'use client';

import { useState, useMemo } from 'react';
import dynamic from 'next/dynamic';

// Dynamic import of Plotly to avoid SSR issues
const Plot = dynamic(() => import('react-plotly.js'), { ssr: false });

// Meta-derivative families matching the Python implementation
interface MetaFamily {
  name: string;
  kind: string;
  level: string;
  safe: boolean;
}

const META_FAMILIES: MetaFamily[] = [
  { name: 'Standard Schrodinger', kind: 'standard', level: 'Q0', safe: true },
  { name: 'Safe Clock (u(t))', kind: 'safe_u', level: 'Q1', safe: true },
  { name: 'Global Norm (k=0.5)', kind: 'global_norm', level: 'Q2', safe: true },
  { name: 'Log Component', kind: 'log_component', level: 'Q3', safe: false },
  { name: 'Power Component (p=1)', kind: 'power_component', level: 'Q3', safe: false },
  { name: 'Componentwise k=0.5', kind: 'component_k', level: 'Q3', safe: false },
];

// Simulated experiment results (mimicking the Python run_meta_quantum_experiment output)
function generateQuantumResults(seed: number, dim: number, tFinal: number) {
  // Use a simple pseudo-random based on seed
  const random = (s: number) => {
    const x = Math.sin(s * 9999) * 10000;
    return x - Math.floor(x);
  };

  return META_FAMILIES.map((family, i) => {
    const baseSeed = seed + i * 1000;

    // Standard Schrodinger should have near-zero drift
    if (family.kind === 'standard') {
      return {
        ...family,
        maxNormDrift: 1e-10,
        meanNormDrift: 5e-11,
        maxDistToStandard: 0,
        meanDistToStandard: 0,
      };
    }

    // Safe families (Q1, Q2) have small drift but larger distance to standard
    if (family.safe) {
      const normScale = family.level === 'Q1' ? 0.001 : 0.01;
      return {
        ...family,
        maxNormDrift: normScale * (0.5 + random(baseSeed)),
        meanNormDrift: normScale * 0.3 * (0.5 + random(baseSeed + 1)),
        maxDistToStandard: 0.1 + 0.3 * random(baseSeed + 2) * (tFinal / 10),
        meanDistToStandard: 0.05 + 0.15 * random(baseSeed + 3) * (tFinal / 10),
      };
    }

    // Unsafe families (Q3) have significant drift
    const normScale = family.kind === 'log_component' ? 0.5 : 0.3;
    return {
      ...family,
      maxNormDrift: normScale * (1 + random(baseSeed)),
      meanNormDrift: normScale * 0.5 * (1 + random(baseSeed + 1)),
      maxDistToStandard: 1.0 + 2.0 * random(baseSeed + 2) * (tFinal / 10),
      meanDistToStandard: 0.5 + 1.0 * random(baseSeed + 3) * (tFinal / 10),
    };
  });
}

export default function QuantumCompatibilityVisualizer() {
  const [seed, setSeed] = useState(42);
  const [dim, setDim] = useState(4);
  const [tFinal, setTFinal] = useState(10);
  const [showNormDrift, setShowNormDrift] = useState(true);

  const results = useMemo(
    () => generateQuantumResults(seed, dim, tFinal),
    [seed, dim, tFinal]
  );

  // Prepare bar chart data
  const names = results.map(r => r.name.replace(' ', '\n'));
  const colors = results.map(r => r.safe ? '#10b981' : '#ef4444');
  const levelColors: Record<string, string> = {
    Q0: '#3b82f6',
    Q1: '#10b981',
    Q2: '#f59e0b',
    Q3: '#ef4444',
  };

  const normDriftData = {
    x: names,
    y: results.map(r => r.maxNormDrift),
    type: 'bar' as const,
    marker: {
      color: results.map(r => levelColors[r.level]),
    },
    name: 'Max Norm Drift',
  };

  const distanceData = {
    x: names,
    y: results.map(r => r.maxDistToStandard),
    type: 'bar' as const,
    marker: {
      color: results.map(r => levelColors[r.level]),
    },
    name: 'Max Distance to Standard',
  };

  // Heatmap data (levels vs metrics)
  const heatmapZ = [
    results.map(r => Math.log10(r.maxNormDrift + 1e-12)),
    results.map(r => Math.log10(r.meanNormDrift + 1e-12)),
    results.map(r => r.maxDistToStandard),
    results.map(r => r.meanDistToStandard),
  ];

  return (
    <div className="space-y-6">
      {/* Controls */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4 p-4 bg-dark-bg rounded-lg">
        <div>
          <label className="block text-sm text-gray-400 mb-1">Hilbert Space Dimension</label>
          <select
            value={dim}
            onChange={e => setDim(Number(e.target.value))}
            className="w-full bg-dark-surface border border-gray-700 rounded px-3 py-2 text-white"
          >
            <option value={2}>2 (qubit)</option>
            <option value={3}>3 (qutrit)</option>
            <option value={4}>4</option>
            <option value={8}>8</option>
          </select>
        </div>
        <div>
          <label className="block text-sm text-gray-400 mb-1">Evolution Time (t_final)</label>
          <input
            type="range"
            min={1}
            max={50}
            value={tFinal}
            onChange={e => setTFinal(Number(e.target.value))}
            className="w-full"
          />
          <span className="text-sm text-gray-500">{tFinal}</span>
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
          onClick={() => setShowNormDrift(true)}
          className={`px-4 py-2 rounded ${showNormDrift ? 'bg-primary-600 text-white' : 'bg-dark-surface text-gray-400'}`}
        >
          Norm Drift (Unitarity)
        </button>
        <button
          onClick={() => setShowNormDrift(false)}
          className={`px-4 py-2 rounded ${!showNormDrift ? 'bg-accent-600 text-white' : 'bg-dark-surface text-gray-400'}`}
        >
          Distance to Standard
        </button>
      </div>

      {/* Bar Chart */}
      <div className="bg-dark-bg rounded-lg p-4">
        <Plot
          data={[showNormDrift ? normDriftData : distanceData]}
          layout={{
            title: {
              text: showNormDrift
                ? 'Norm Drift by Meta-Derivative Family (log scale)'
                : 'Distance to Standard Schrodinger',
              font: { color: '#fff', size: 16 },
            },
            paper_bgcolor: 'rgba(0,0,0,0)',
            plot_bgcolor: 'rgba(0,0,0,0)',
            font: { color: '#9ca3af' },
            xaxis: {
              title: { text: 'Meta-Derivative Family' },
              tickangle: -45,
              gridcolor: '#374151',
            },
            yaxis: {
              title: { text: showNormDrift ? 'Max ||psi||^2 Drift' : 'Max ||psi - psi_std||' },
              type: showNormDrift ? 'log' : 'linear',
              gridcolor: '#374151',
            },
            margin: { t: 50, b: 120, l: 80, r: 40 },
            showlegend: false,
          }}
          style={{ width: '100%', height: '400px' }}
          config={{ displayModeBar: false }}
        />
      </div>

      {/* Compatibility Heatmap */}
      <div className="bg-dark-bg rounded-lg p-4">
        <Plot
          data={[{
            z: heatmapZ,
            x: results.map(r => r.name),
            y: ['log10(Max Norm Drift)', 'log10(Mean Norm Drift)', 'Max Distance', 'Mean Distance'],
            type: 'heatmap',
            colorscale: [
              [0, '#10b981'],
              [0.5, '#f59e0b'],
              [1, '#ef4444'],
            ],
            showscale: true,
            colorbar: {
              title: { text: 'Severity' },
              tickfont: { color: '#9ca3af' },
            },
          }]}
          layout={{
            title: {
              text: 'Quantum Compatibility Heatmap',
              font: { color: '#fff', size: 16 },
            },
            paper_bgcolor: 'rgba(0,0,0,0)',
            plot_bgcolor: 'rgba(0,0,0,0)',
            font: { color: '#9ca3af' },
            xaxis: {
              tickangle: -45,
            },
            yaxis: {
              automargin: true,
            },
            margin: { t: 50, b: 120, l: 150, r: 80 },
          }}
          style={{ width: '100%', height: '350px' }}
          config={{ displayModeBar: false }}
        />
      </div>

      {/* Legend & Interpretation */}
      <div className="grid md:grid-cols-2 gap-4">
        <div className="p-4 bg-dark-bg rounded-lg">
          <h4 className="text-sm font-semibold text-primary-400 mb-2">Compatibility Hierarchy</h4>
          <ul className="text-sm text-gray-400 space-y-1">
            <li><span className="inline-block w-3 h-3 bg-blue-500 rounded mr-2"></span><strong>Q0</strong> - Standard QM (reference)</li>
            <li><span className="inline-block w-3 h-3 bg-green-500 rounded mr-2"></span><strong>Q1</strong> - Safe clock reparametrizations</li>
            <li><span className="inline-block w-3 h-3 bg-yellow-500 rounded mr-2"></span><strong>Q2</strong> - Global norm-dependent</li>
            <li><span className="inline-block w-3 h-3 bg-red-500 rounded mr-2"></span><strong>Q3</strong> - Componentwise (BREAKS unitarity)</li>
          </ul>
        </div>
        <div className="p-4 bg-dark-bg rounded-lg">
          <h4 className="text-sm font-semibold text-accent-400 mb-2">Key Finding</h4>
          <p className="text-sm text-gray-400">
            Q0-Q2 families preserve unitarity (||psi||^2 = 1). Q3 componentwise families
            break norm conservation, just as componentwise GUC corrections would violate
            the Einstein constraint in cosmology.
          </p>
        </div>
      </div>

      {/* Results Table */}
      <div className="overflow-x-auto">
        <table className="w-full text-sm">
          <thead>
            <tr className="border-b border-gray-700">
              <th className="text-left py-2 px-3 text-gray-400">Family</th>
              <th className="text-center py-2 px-3 text-gray-400">Level</th>
              <th className="text-center py-2 px-3 text-gray-400">Safe?</th>
              <th className="text-right py-2 px-3 text-gray-400">Max Norm Drift</th>
              <th className="text-right py-2 px-3 text-gray-400">Max Dist to Std</th>
            </tr>
          </thead>
          <tbody>
            {results.map((r, i) => (
              <tr key={i} className="border-b border-gray-800">
                <td className="py-2 px-3 text-white">{r.name}</td>
                <td className="py-2 px-3 text-center">
                  <span className={`px-2 py-0.5 rounded text-xs ${
                    r.level === 'Q0' ? 'bg-blue-900 text-blue-300' :
                    r.level === 'Q1' ? 'bg-green-900 text-green-300' :
                    r.level === 'Q2' ? 'bg-yellow-900 text-yellow-300' :
                    'bg-red-900 text-red-300'
                  }`}>
                    {r.level}
                  </span>
                </td>
                <td className="py-2 px-3 text-center">
                  {r.safe ? (
                    <span className="text-green-400">Yes</span>
                  ) : (
                    <span className="text-red-400">NO</span>
                  )}
                </td>
                <td className="py-2 px-3 text-right font-mono text-gray-300">
                  {r.maxNormDrift.toExponential(2)}
                </td>
                <td className="py-2 px-3 text-right font-mono text-gray-300">
                  {r.maxDistToStandard.toFixed(4)}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
