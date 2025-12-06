'use client';

import { useState, useMemo } from 'react';
import Plot from './PlotlyChart';

interface SliderProps {
  label: string;
  value: number;
  min: number;
  max: number;
  step: number;
  onChange: (value: number) => void;
  unit?: string;
  color?: string;
}

function ParameterSlider({ label, value, min, max, step, onChange, unit = '', color = 'primary' }: SliderProps) {
  return (
    <div className="space-y-2">
      <div className="flex justify-between items-center">
        <label className="text-sm font-medium text-gray-300">{label}</label>
        <div className="flex items-center gap-2">
          <input
            type="number"
            value={value}
            onChange={(e) => onChange(parseFloat(e.target.value) || 0)}
            min={min}
            max={max}
            step={step}
            className="w-20 px-2 py-1 text-sm bg-dark-bg border border-dark-border rounded text-white text-right"
          />
          {unit && <span className="text-xs text-gray-500">{unit}</span>}
        </div>
      </div>
      <input
        type="range"
        min={min}
        max={max}
        step={step}
        value={value}
        onChange={(e) => onChange(parseFloat(e.target.value))}
        className={`w-full h-2 rounded-lg appearance-none cursor-pointer bg-dark-border accent-${color}-500`}
        style={{ accentColor: color === 'primary' ? '#3b82f6' : color === 'accent' ? '#a855f7' : '#10b981' }}
      />
      <div className="flex justify-between text-xs text-gray-500">
        <span>{min}</span>
        <span>{max}</span>
      </div>
    </div>
  );
}

// Meta-Friedmann equation: compute n_act from parameters
function computeNAct(s: number, w: number): number {
  const Delta = 9 * s * s * w * w - 8 * s * s + 4 * s + 4;
  if (Delta < 0) return NaN;
  const numerator = -(3 * w * s + 2 * s - 2) + Math.sqrt(Delta);
  const denominator = 6 * (1 + w);
  if (Math.abs(denominator) < 1e-10) return NaN;
  return numerator / denominator;
}

// Compute chi-squared fit
function computeChi2(n: number, s: number, w: number): number {
  const nPredicted = computeNAct(s, w);
  if (isNaN(nPredicted)) return Infinity;
  return ((n - nPredicted) ** 2) / 0.01;
}

// Compute scheme invariance
function computeInvariance(k: number, s: number): number {
  return Math.exp(-10 * (k * k + s * s));
}

// Compute constraint tension
function computeConstraintTension(s: number, k: number): number {
  return Math.abs(s) / 0.05 + Math.abs(k) / 0.03;
}

export default function ParameterExplorer() {
  // Decision variables
  const [n, setN] = useState(0.667); // Matter-dominated expansion
  const [s, setS] = useState(0.0);   // Scale parameter
  const [k, setK] = useState(0.0);   // Calculus index
  const [w, setW] = useState(-0.33); // Equation of state (matter ~ -1/3 effective)

  // Surface resolution
  const [resolution, setResolution] = useState(25);

  // Computed values
  const metrics = useMemo(() => {
    const nAct = computeNAct(s, w);
    const chi2 = computeChi2(n, s, w);
    const invariance = computeInvariance(k, s);
    const constraintTension = computeConstraintTension(s, k);

    return {
      nAct: isNaN(nAct) ? 'Undefined' : nAct.toFixed(4),
      chi2: chi2 === Infinity ? 'Infinity' : chi2.toFixed(4),
      invariance: invariance.toFixed(4),
      constraintTension: constraintTension.toFixed(4),
      feasible: Math.abs(s) <= 0.05 && Math.abs(k) <= 0.03 && w >= -1 && w <= 0
    };
  }, [n, s, k, w]);

  // Generate surface data for chi-squared landscape
  const surfaceData = useMemo(() => {
    const sRange = [];
    const kRange = [];
    const zData = [];

    for (let i = 0; i <= resolution; i++) {
      sRange.push(-0.05 + (i / resolution) * 0.1);
    }
    for (let j = 0; j <= resolution; j++) {
      kRange.push(-0.03 + (j / resolution) * 0.06);
    }

    for (let j = 0; j <= resolution; j++) {
      const row = [];
      for (let i = 0; i <= resolution; i++) {
        const sVal = sRange[i];
        const kVal = kRange[j];
        const chi2 = computeChi2(n, sVal, w);
        const inv = computeInvariance(kVal, sVal);
        // Combined objective: weighted sum for visualization
        const combined = chi2 + (1 - inv) * 10;
        row.push(Math.min(combined, 50)); // Cap for visualization
      }
      zData.push(row);
    }

    return { sRange, kRange, zData };
  }, [n, w, resolution]);

  const traces = useMemo(() => [
    {
      type: 'surface',
      x: surfaceData.sRange,
      y: surfaceData.kRange,
      z: surfaceData.zData,
      colorscale: [
        [0, '#1e3a5f'],
        [0.25, '#3b82f6'],
        [0.5, '#8b5cf6'],
        [0.75, '#c084fc'],
        [1, '#fbbf24']
      ],
      opacity: 0.9,
      contours: {
        z: {
          show: true,
          usecolormap: true,
          highlightcolor: '#fff',
          project: { z: true }
        }
      },
      hovertemplate:
        's: %{x:.4f}<br>' +
        'k: %{y:.4f}<br>' +
        'Objective: %{z:.2f}<extra></extra>'
    },
    // Current point marker
    {
      type: 'scatter3d',
      mode: 'markers',
      x: [s],
      y: [k],
      z: [Math.min(computeChi2(n, s, w) + (1 - computeInvariance(k, s)) * 10, 50)],
      marker: {
        size: 12,
        color: metrics.feasible ? '#10b981' : '#ef4444',
        symbol: 'diamond',
        line: { width: 2, color: '#fff' }
      },
      name: 'Current Point',
      hovertemplate:
        '<b>Current Configuration</b><br>' +
        's: %{x:.4f}<br>' +
        'k: %{y:.4f}<br>' +
        'Objective: %{z:.2f}<extra></extra>'
    }
  ], [surfaceData, s, k, n, w, metrics.feasible]);

  const layout = useMemo(() => ({
    autosize: true,
    height: 450,
    margin: { l: 0, r: 0, t: 30, b: 0 },
    paper_bgcolor: 'rgba(0,0,0,0)',
    plot_bgcolor: 'rgba(0,0,0,0)',
    font: { color: '#d1d5db' },
    scene: {
      xaxis: {
        title: 's (scale)',
        range: [-0.05, 0.05],
        gridcolor: '#374151',
        zerolinecolor: '#4b5563'
      },
      yaxis: {
        title: 'k (calculus)',
        range: [-0.03, 0.03],
        gridcolor: '#374151',
        zerolinecolor: '#4b5563'
      },
      zaxis: {
        title: 'Combined Objective',
        gridcolor: '#374151',
        zerolinecolor: '#4b5563'
      },
      bgcolor: 'rgba(17, 24, 39, 0.8)',
      camera: {
        eye: { x: 1.8, y: 1.8, z: 1.0 }
      }
    },
    showlegend: false
  }), []);

  return (
    <div className="space-y-6">
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Parameter Controls */}
        <div className="lg:col-span-1 space-y-6">
          <div className="bg-dark-surface rounded-lg p-4 border border-dark-border">
            <h3 className="text-lg font-semibold text-white mb-4">Decision Variables</h3>

            <div className="space-y-4">
              <ParameterSlider
                label="n (expansion exponent)"
                value={n}
                min={0.3}
                max={0.9}
                step={0.01}
                onChange={setN}
                color="primary"
              />

              <ParameterSlider
                label="s (scale parameter)"
                value={s}
                min={-0.1}
                max={0.1}
                step={0.001}
                onChange={setS}
                color="primary"
              />

              <ParameterSlider
                label="k (calculus index)"
                value={k}
                min={-0.05}
                max={0.05}
                step={0.001}
                onChange={setK}
                color="accent"
              />

              <ParameterSlider
                label="w (equation of state)"
                value={w}
                min={-1.0}
                max={0.0}
                step={0.01}
                onChange={setW}
                color="green"
              />
            </div>

            <div className="mt-4 pt-4 border-t border-dark-border">
              <label className="text-sm text-gray-400">Surface Resolution</label>
              <input
                type="range"
                min={10}
                max={50}
                value={resolution}
                onChange={(e) => setResolution(parseInt(e.target.value))}
                className="w-full mt-2"
              />
              <div className="flex justify-between text-xs text-gray-500">
                <span>Fast (10)</span>
                <span>{resolution}</span>
                <span>Detailed (50)</span>
              </div>
            </div>
          </div>

          {/* Computed Metrics */}
          <div className="bg-dark-surface rounded-lg p-4 border border-dark-border">
            <h3 className="text-lg font-semibold text-white mb-4">Computed Objectives</h3>

            <div className="space-y-3">
              <div className="flex justify-between">
                <span className="text-gray-400">n_act (predicted)</span>
                <span className="text-primary-400 font-mono">{metrics.nAct}</span>
              </div>
              <div className="flex justify-between">
                <span className="text-gray-400">Chi-squared fit</span>
                <span className="text-primary-400 font-mono">{metrics.chi2}</span>
              </div>
              <div className="flex justify-between">
                <span className="text-gray-400">Scheme invariance</span>
                <span className="text-accent-400 font-mono">{metrics.invariance}</span>
              </div>
              <div className="flex justify-between">
                <span className="text-gray-400">Constraint tension</span>
                <span className="text-yellow-400 font-mono">{metrics.constraintTension}</span>
              </div>
              <div className="flex justify-between items-center pt-2 border-t border-dark-border">
                <span className="text-gray-400">Feasibility</span>
                <span className={`px-2 py-1 rounded text-xs font-semibold ${
                  metrics.feasible
                    ? 'bg-green-900/50 text-green-400'
                    : 'bg-red-900/50 text-red-400'
                }`}>
                  {metrics.feasible ? 'FEASIBLE' : 'INFEASIBLE'}
                </span>
              </div>
            </div>
          </div>

          {/* Preset Configurations */}
          <div className="bg-dark-surface rounded-lg p-4 border border-dark-border">
            <h3 className="text-lg font-semibold text-white mb-4">Preset Configurations</h3>
            <div className="space-y-2">
              <button
                onClick={() => { setN(0.667); setS(0); setK(0); setW(-0.33); }}
                className="w-full px-3 py-2 text-left text-sm bg-dark-bg rounded hover:bg-dark-border transition-colors"
              >
                <span className="text-primary-400">Classical (k=0)</span>
                <span className="text-gray-500 block text-xs">Standard calculus limit</span>
              </button>
              <button
                onClick={() => { setN(0.5); setS(0); setK(0); setW(0.33); }}
                className="w-full px-3 py-2 text-left text-sm bg-dark-bg rounded hover:bg-dark-border transition-colors"
              >
                <span className="text-accent-400">Radiation Era</span>
                <span className="text-gray-500 block text-xs">n=1/2, w=1/3</span>
              </button>
              <button
                onClick={() => { setN(0.6); setS(0.02); setK(0.01); setW(-0.5); }}
                className="w-full px-3 py-2 text-left text-sm bg-dark-bg rounded hover:bg-dark-border transition-colors"
              >
                <span className="text-yellow-400">Non-classical</span>
                <span className="text-gray-500 block text-xs">Alternative calculus configuration</span>
              </button>
            </div>
          </div>
        </div>

        {/* 3D Visualization */}
        <div className="lg:col-span-2">
          <div className="bg-dark-surface rounded-lg border border-dark-border overflow-hidden">
            <div className="p-3 border-b border-dark-border">
              <h3 className="text-sm font-medium text-gray-300">
                Objective Landscape (s, k) at n={n.toFixed(2)}, w={w.toFixed(2)}
              </h3>
            </div>
            <Plot
              data={traces}
              layout={layout}
              config={{
                displayModeBar: true,
                displaylogo: false,
                responsive: true
              }}
              style={{ width: '100%', height: '450px' }}
            />
          </div>

          <div className="mt-4 p-4 bg-dark-bg rounded-lg text-sm text-gray-400">
            <p>
              <strong className="text-white">How to use:</strong> Drag the sliders to explore the parameter space.
              The 3D surface shows the combined objective (chi-squared + non-robustness) for different (s, k) values.
              Lower values (blue) are better. The diamond marker shows your current configuration.
              Green = feasible (within BBN/CMB constraints), Red = infeasible.
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}
