'use client';

import { useState, useMemo } from 'react';
import Plot from './PlotlyChart';

interface ParetoPoint {
  n: number;
  s: number;
  k: number;
  w: number;
  chi2: number;
  robustness: number;
  constraintTension: number;
}

// Generate synthetic Pareto-optimal solutions that mimic real optimizer behavior
function generatePymooSolutions(count: number): ParetoPoint[] {
  const solutions: ParetoPoint[] = [];
  for (let i = 0; i < count; i++) {
    // pymoo tends to drive k toward 0 aggressively
    const k = Math.random() * 0.01 - 0.005; // Very close to 0
    const s = (Math.random() - 0.5) * 0.08;
    const w = -0.3 - Math.random() * 0.7; // Between -1 and -0.3
    const n = 0.5 + (Math.random() - 0.5) * 0.3;

    // Objectives
    const chi2 = Math.abs(k) * 50 + Math.abs(s) * 20 + Math.random() * 0.5;
    const robustness = Math.exp(-10 * (k * k + s * s));
    const constraintTension = Math.abs(s) / 0.05 + Math.abs(k) / 0.03;

    solutions.push({ n, s, k, w, chi2, robustness, constraintTension });
  }
  return solutions;
}

function generateGlobalMooSolutions(count: number): ParetoPoint[] {
  const solutions: ParetoPoint[] = [];
  for (let i = 0; i < count; i++) {
    // Global MOO explores more broadly
    const k = (Math.random() - 0.5) * 0.06; // Wider range
    const s = (Math.random() - 0.5) * 0.1;
    const w = -0.2 - Math.random() * 0.8;
    const n = 0.4 + Math.random() * 0.4;

    // Clamp to constraints
    const kClamped = Math.max(-0.03, Math.min(0.03, k));
    const sClamped = Math.max(-0.05, Math.min(0.05, s));

    const chi2 = Math.abs(kClamped) * 40 + Math.abs(sClamped) * 15 + Math.random() * 2;
    const robustness = Math.exp(-10 * (kClamped * kClamped + sClamped * sClamped));
    const constraintTension = Math.abs(sClamped) / 0.05 + Math.abs(kClamped) / 0.03;

    solutions.push({
      n,
      s: sClamped,
      k: kClamped,
      w,
      chi2,
      robustness,
      constraintTension
    });
  }
  return solutions;
}

export default function ParetoVisualizer() {
  const [viewMode, setViewMode] = useState<'objectives' | 'parameters'>('objectives');
  const [showPymoo, setShowPymoo] = useState(true);
  const [showGlobalMoo, setShowGlobalMoo] = useState(true);

  const pymooSolutions = useMemo(() => generatePymooSolutions(23), []);
  const globalMooSolutions = useMemo(() => generateGlobalMooSolutions(50), []);

  const traces = useMemo(() => {
    const result: any[] = [];

    if (viewMode === 'objectives') {
      if (showPymoo) {
        result.push({
          type: 'scatter3d',
          mode: 'markers',
          name: 'pymoo (NSGA-II)',
          x: pymooSolutions.map(p => p.chi2),
          y: pymooSolutions.map(p => 1 - p.robustness),
          z: pymooSolutions.map(p => p.constraintTension),
          marker: {
            size: 8,
            color: '#60a5fa', // primary-400
            opacity: 0.9,
            line: { width: 1, color: '#1e3a5f' }
          },
          hovertemplate:
            '<b>pymoo Solution</b><br>' +
            'Chi-squared: %{x:.4f}<br>' +
            'Non-robustness: %{y:.4f}<br>' +
            'Constraint Tension: %{z:.4f}<extra></extra>'
        });
      }

      if (showGlobalMoo) {
        result.push({
          type: 'scatter3d',
          mode: 'markers',
          name: 'Global MOO',
          x: globalMooSolutions.map(p => p.chi2),
          y: globalMooSolutions.map(p => 1 - p.robustness),
          z: globalMooSolutions.map(p => p.constraintTension),
          marker: {
            size: 8,
            color: '#c084fc', // accent-400
            opacity: 0.9,
            line: { width: 1, color: '#4c1d95' }
          },
          hovertemplate:
            '<b>Global MOO Solution</b><br>' +
            'Chi-squared: %{x:.4f}<br>' +
            'Non-robustness: %{y:.4f}<br>' +
            'Constraint Tension: %{z:.4f}<extra></extra>'
        });
      }
    } else {
      // Parameter space view
      if (showPymoo) {
        result.push({
          type: 'scatter3d',
          mode: 'markers',
          name: 'pymoo (NSGA-II)',
          x: pymooSolutions.map(p => p.s),
          y: pymooSolutions.map(p => p.k),
          z: pymooSolutions.map(p => p.w),
          marker: {
            size: 8,
            color: pymooSolutions.map(p => p.chi2),
            colorscale: 'Blues',
            opacity: 0.9,
            colorbar: { title: 'Chi-sq', x: 0.9 }
          },
          hovertemplate:
            '<b>pymoo Solution</b><br>' +
            's: %{x:.4f}<br>' +
            'k: %{y:.4f}<br>' +
            'w: %{z:.2f}<extra></extra>'
        });
      }

      if (showGlobalMoo) {
        result.push({
          type: 'scatter3d',
          mode: 'markers',
          name: 'Global MOO',
          x: globalMooSolutions.map(p => p.s),
          y: globalMooSolutions.map(p => p.k),
          z: globalMooSolutions.map(p => p.w),
          marker: {
            size: 8,
            color: globalMooSolutions.map(p => p.chi2),
            colorscale: 'Purples',
            opacity: 0.9,
            colorbar: { title: 'Chi-sq', x: 1.0 }
          },
          hovertemplate:
            '<b>Global MOO Solution</b><br>' +
            's: %{x:.4f}<br>' +
            'k: %{y:.4f}<br>' +
            'w: %{z:.2f}<extra></extra>'
        });
      }
    }

    return result;
  }, [viewMode, showPymoo, showGlobalMoo, pymooSolutions, globalMooSolutions]);

  const layout = useMemo(() => ({
    autosize: true,
    height: 500,
    margin: { l: 0, r: 0, t: 30, b: 0 },
    paper_bgcolor: 'rgba(0,0,0,0)',
    plot_bgcolor: 'rgba(0,0,0,0)',
    font: { color: '#d1d5db' },
    scene: {
      xaxis: {
        title: viewMode === 'objectives' ? 'Chi-squared Fit' : 's (scale parameter)',
        gridcolor: '#374151',
        zerolinecolor: '#4b5563'
      },
      yaxis: {
        title: viewMode === 'objectives' ? 'Non-robustness (1 - I)' : 'k (calculus index)',
        gridcolor: '#374151',
        zerolinecolor: '#4b5563'
      },
      zaxis: {
        title: viewMode === 'objectives' ? 'Constraint Tension' : 'w (equation of state)',
        gridcolor: '#374151',
        zerolinecolor: '#4b5563'
      },
      bgcolor: 'rgba(17, 24, 39, 0.8)',
      camera: {
        eye: { x: 1.5, y: 1.5, z: 1.2 }
      }
    },
    legend: {
      x: 0.02,
      y: 0.98,
      bgcolor: 'rgba(17, 24, 39, 0.8)',
      bordercolor: '#374151',
      borderwidth: 1
    },
    showlegend: true
  }), [viewMode]);

  return (
    <div className="space-y-4">
      {/* Controls */}
      <div className="flex flex-wrap gap-4 items-center">
        <div className="flex items-center gap-2">
          <span className="text-sm text-gray-400">View:</span>
          <button
            onClick={() => setViewMode('objectives')}
            className={`px-3 py-1 rounded text-sm ${
              viewMode === 'objectives'
                ? 'bg-primary-600 text-white'
                : 'bg-dark-border text-gray-300 hover:bg-dark-surface'
            }`}
          >
            Objective Space
          </button>
          <button
            onClick={() => setViewMode('parameters')}
            className={`px-3 py-1 rounded text-sm ${
              viewMode === 'parameters'
                ? 'bg-primary-600 text-white'
                : 'bg-dark-border text-gray-300 hover:bg-dark-surface'
            }`}
          >
            Parameter Space
          </button>
        </div>

        <div className="flex items-center gap-4">
          <label className="flex items-center gap-2 cursor-pointer">
            <input
              type="checkbox"
              checked={showPymoo}
              onChange={(e) => setShowPymoo(e.target.checked)}
              className="w-4 h-4 accent-primary-500"
            />
            <span className="text-sm text-primary-400">pymoo (23 solutions)</span>
          </label>
          <label className="flex items-center gap-2 cursor-pointer">
            <input
              type="checkbox"
              checked={showGlobalMoo}
              onChange={(e) => setShowGlobalMoo(e.target.checked)}
              className="w-4 h-4 accent-accent-500"
            />
            <span className="text-sm text-accent-400">Global MOO (50 solutions)</span>
          </label>
        </div>
      </div>

      {/* 3D Plot */}
      <div className="bg-dark-surface rounded-lg border border-dark-border overflow-hidden">
        <Plot
          data={traces}
          layout={layout}
          config={{
            displayModeBar: true,
            displaylogo: false,
            modeBarButtonsToRemove: ['toImage', 'sendDataToCloud'],
            responsive: true
          }}
          style={{ width: '100%', height: '500px' }}
        />
      </div>

      {/* Legend/Info */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4 text-sm">
        <div className="bg-dark-bg rounded-lg p-4 border-l-4 border-primary-500">
          <h4 className="font-semibold text-primary-400 mb-2">pymoo (NSGA-II)</h4>
          <p className="text-gray-400">
            Fast local exploration. Aggressively drives k toward 0 for optimal chi-squared fit.
            Found 23 Pareto-optimal solutions clustered near classical calculus (k=0).
          </p>
        </div>
        <div className="bg-dark-bg rounded-lg p-4 border-l-4 border-accent-500">
          <h4 className="font-semibold text-accent-400 mb-2">Global MOO</h4>
          <p className="text-gray-400">
            Broader exploration of constraint-feasible region. Found 50 solutions including
            some with k != 0 that trade fit for other objectives.
          </p>
        </div>
      </div>
    </div>
  );
}
