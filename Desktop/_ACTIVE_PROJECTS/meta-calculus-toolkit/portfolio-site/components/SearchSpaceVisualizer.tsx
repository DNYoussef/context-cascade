'use client';

import { useState, useMemo, useCallback } from 'react';
import Plot from './PlotlyChart';

type ObjectiveType = 'chi2' | 'invariance' | 'combined' | 'constraint';

interface Config {
  n: number;
  w: number;
  objective: ObjectiveType;
  showContours: boolean;
  showOptimaPaths: boolean;
}

// Objective functions
function computeChi2(n: number, s: number, w: number): number {
  const Delta = 9 * s * s * w * w - 8 * s * s + 4 * s + 4;
  if (Delta < 0) return 50;
  const numerator = -(3 * w * s + 2 * s - 2) + Math.sqrt(Delta);
  const denominator = 6 * (1 + w);
  if (Math.abs(denominator) < 1e-10) return 50;
  const nPredicted = numerator / denominator;
  return Math.min(((n - nPredicted) ** 2) / 0.01, 50);
}

function computeInvariance(k: number, s: number): number {
  return Math.exp(-10 * (k * k + s * s));
}

function computeConstraintTension(s: number, k: number): number {
  return Math.abs(s) / 0.05 + Math.abs(k) / 0.03;
}

export default function SearchSpaceVisualizer() {
  const [config, setConfig] = useState<Config>({
    n: 0.667,
    w: -0.33,
    objective: 'combined',
    showContours: true,
    showOptimaPaths: true
  });

  const [animating, setAnimating] = useState(false);
  const [animationFrame, setAnimationFrame] = useState(0);

  // Generate heatmap data
  const heatmapData = useMemo(() => {
    const resolution = 50;
    const sRange: number[] = [];
    const kRange: number[] = [];
    const zData: number[][] = [];

    for (let i = 0; i <= resolution; i++) {
      sRange.push(-0.05 + (i / resolution) * 0.1);
      kRange.push(-0.03 + (i / resolution) * 0.06);
    }

    for (let j = 0; j <= resolution; j++) {
      const row: number[] = [];
      for (let i = 0; i <= resolution; i++) {
        const s = sRange[i];
        const k = kRange[j];

        let value: number;
        switch (config.objective) {
          case 'chi2':
            value = computeChi2(config.n, s, config.w);
            break;
          case 'invariance':
            value = 1 - computeInvariance(k, s); // Invert so lower is better
            break;
          case 'constraint':
            value = computeConstraintTension(s, k);
            break;
          case 'combined':
          default:
            value = computeChi2(config.n, s, config.w) +
                    (1 - computeInvariance(k, s)) * 5 +
                    computeConstraintTension(s, k) * 2;
        }
        row.push(Math.min(value, 50));
      }
      zData.push(row);
    }

    return { sRange, kRange, zData };
  }, [config.n, config.w, config.objective]);

  // Generate optimizer paths (simulated gradient descent trajectories)
  const optimizerPaths = useMemo(() => {
    const pymooPath: { s: number[]; k: number[] } = { s: [], k: [] };
    const globalMooPath: { s: number[]; k: number[] } = { s: [], k: [] };

    // Simulate pymoo: starts wide, converges quickly to k=0
    let ps = 0.04, pk = 0.02;
    for (let i = 0; i < 20; i++) {
      pymooPath.s.push(ps);
      pymooPath.k.push(pk);
      ps *= 0.85;
      pk *= 0.7;
      ps += (Math.random() - 0.5) * 0.005;
      pk += (Math.random() - 0.5) * 0.003;
    }

    // Simulate Global MOO: explores more broadly
    let gs = -0.03, gk = -0.02;
    for (let i = 0; i < 30; i++) {
      globalMooPath.s.push(gs);
      globalMooPath.k.push(gk);
      gs += (Math.random() - 0.3) * 0.01;
      gk += (Math.random() - 0.4) * 0.006;
      gs = Math.max(-0.05, Math.min(0.05, gs));
      gk = Math.max(-0.03, Math.min(0.03, gk));
    }

    return { pymooPath, globalMooPath };
  }, []);

  const traces = useMemo(() => {
    const result: any[] = [];

    // Main heatmap
    result.push({
      type: 'heatmap',
      x: heatmapData.sRange,
      y: heatmapData.kRange,
      z: heatmapData.zData,
      colorscale: [
        [0, '#0f172a'],
        [0.2, '#1e3a5f'],
        [0.4, '#3b82f6'],
        [0.6, '#8b5cf6'],
        [0.8, '#c084fc'],
        [1, '#fbbf24']
      ],
      colorbar: {
        title: {
          text: config.objective === 'chi2' ? 'Chi-sq' :
                config.objective === 'invariance' ? '1 - Inv' :
                config.objective === 'constraint' ? 'Tension' : 'Combined',
          side: 'right'
        },
        tickfont: { color: '#9ca3af' }
      },
      hovertemplate:
        's: %{x:.4f}<br>' +
        'k: %{y:.4f}<br>' +
        'Value: %{z:.3f}<extra></extra>'
    });

    // Contour lines
    if (config.showContours) {
      result.push({
        type: 'contour',
        x: heatmapData.sRange,
        y: heatmapData.kRange,
        z: heatmapData.zData,
        contours: {
          coloring: 'lines',
          showlabels: true
        },
        line: { color: 'rgba(255,255,255,0.3)', width: 1 },
        showscale: false,
        hoverinfo: 'skip'
      });
    }

    // Optimizer paths
    if (config.showOptimaPaths) {
      const frameLimit = animating ? animationFrame : 100;

      result.push({
        type: 'scatter',
        mode: 'lines+markers',
        name: 'pymoo trajectory',
        x: optimizerPaths.pymooPath.s.slice(0, Math.floor(frameLimit / 5)),
        y: optimizerPaths.pymooPath.k.slice(0, Math.floor(frameLimit / 5)),
        line: { color: '#60a5fa', width: 3 },
        marker: { size: 6, color: '#60a5fa' }
      });

      result.push({
        type: 'scatter',
        mode: 'lines+markers',
        name: 'Global MOO trajectory',
        x: optimizerPaths.globalMooPath.s.slice(0, Math.floor(frameLimit / 3)),
        y: optimizerPaths.globalMooPath.k.slice(0, Math.floor(frameLimit / 3)),
        line: { color: '#c084fc', width: 3 },
        marker: { size: 6, color: '#c084fc' }
      });
    }

    // Constraint boundaries
    result.push({
      type: 'scatter',
      mode: 'lines',
      name: 'BBN constraint (|s| = 0.05)',
      x: [-0.05, -0.05, NaN, 0.05, 0.05],
      y: [-0.03, 0.03, NaN, -0.03, 0.03],
      line: { color: '#ef4444', width: 2, dash: 'dash' },
      hoverinfo: 'name'
    });

    result.push({
      type: 'scatter',
      mode: 'lines',
      name: 'CMB constraint (|k| = 0.03)',
      x: [-0.05, 0.05, NaN, -0.05, 0.05],
      y: [-0.03, -0.03, NaN, 0.03, 0.03],
      line: { color: '#f59e0b', width: 2, dash: 'dash' },
      hoverinfo: 'name'
    });

    // Optimal point marker (k=0, s=0)
    result.push({
      type: 'scatter',
      mode: 'markers',
      name: 'Classical optimum',
      x: [0],
      y: [0],
      marker: {
        size: 15,
        color: '#10b981',
        symbol: 'star',
        line: { width: 2, color: '#fff' }
      }
    });

    return result;
  }, [heatmapData, config.showContours, config.showOptimaPaths, optimizerPaths, animating, animationFrame]);

  const layout = useMemo(() => ({
    autosize: true,
    height: 550,
    margin: { l: 60, r: 100, t: 40, b: 60 },
    paper_bgcolor: 'rgba(0,0,0,0)',
    plot_bgcolor: 'rgba(17, 24, 39, 1)',
    font: { color: '#d1d5db' },
    xaxis: {
      title: 's (scale parameter)',
      range: [-0.055, 0.055],
      gridcolor: '#374151',
      zerolinecolor: '#4b5563'
    },
    yaxis: {
      title: 'k (calculus index)',
      range: [-0.035, 0.035],
      gridcolor: '#374151',
      zerolinecolor: '#4b5563'
    },
    legend: {
      x: 1.02,
      y: 1,
      bgcolor: 'rgba(17, 24, 39, 0.9)',
      bordercolor: '#374151',
      borderwidth: 1,
      font: { size: 10 }
    },
    annotations: [
      {
        x: 0,
        y: 0,
        text: 'k=0',
        showarrow: true,
        arrowhead: 2,
        arrowcolor: '#10b981',
        font: { color: '#10b981', size: 12 },
        ax: 30,
        ay: -30
      }
    ]
  }), []);

  // Animation control
  const startAnimation = useCallback(() => {
    setAnimating(true);
    setAnimationFrame(0);
    let frame = 0;
    const interval = setInterval(() => {
      frame += 2;
      setAnimationFrame(frame);
      if (frame >= 100) {
        clearInterval(interval);
        setAnimating(false);
      }
    }, 50);
  }, []);

  return (
    <div className="space-y-4">
      {/* Controls */}
      <div className="flex flex-wrap gap-4 items-center justify-between">
        <div className="flex flex-wrap gap-4 items-center">
          <div className="flex items-center gap-2">
            <span className="text-sm text-gray-400">Objective:</span>
            <select
              value={config.objective}
              onChange={(e) => setConfig({ ...config, objective: e.target.value as ObjectiveType })}
              className="px-3 py-1.5 rounded bg-dark-surface border border-dark-border text-sm text-white"
            >
              <option value="combined">Combined (weighted sum)</option>
              <option value="chi2">Chi-squared fit only</option>
              <option value="invariance">Scheme invariance only</option>
              <option value="constraint">Constraint tension only</option>
            </select>
          </div>

          <div className="flex items-center gap-4">
            <label className="flex items-center gap-2 cursor-pointer text-sm">
              <input
                type="checkbox"
                checked={config.showContours}
                onChange={(e) => setConfig({ ...config, showContours: e.target.checked })}
                className="w-4 h-4 accent-primary-500"
              />
              <span className="text-gray-300">Contours</span>
            </label>
            <label className="flex items-center gap-2 cursor-pointer text-sm">
              <input
                type="checkbox"
                checked={config.showOptimaPaths}
                onChange={(e) => setConfig({ ...config, showOptimaPaths: e.target.checked })}
                className="w-4 h-4 accent-primary-500"
              />
              <span className="text-gray-300">Optimizer Paths</span>
            </label>
          </div>
        </div>

        <button
          onClick={startAnimation}
          disabled={animating}
          className={`px-4 py-2 rounded text-sm font-medium transition-colors ${
            animating
              ? 'bg-gray-600 text-gray-400 cursor-not-allowed'
              : 'bg-primary-600 text-white hover:bg-primary-700'
          }`}
        >
          {animating ? 'Animating...' : 'Animate Search'}
        </button>
      </div>

      {/* Parameter sliders */}
      <div className="grid grid-cols-2 gap-4">
        <div className="bg-dark-surface rounded-lg p-3 border border-dark-border">
          <label className="text-sm text-gray-400">n (expansion exponent): {config.n.toFixed(2)}</label>
          <input
            type="range"
            min={0.3}
            max={0.9}
            step={0.01}
            value={config.n}
            onChange={(e) => setConfig({ ...config, n: parseFloat(e.target.value) })}
            className="w-full mt-2"
          />
        </div>
        <div className="bg-dark-surface rounded-lg p-3 border border-dark-border">
          <label className="text-sm text-gray-400">w (equation of state): {config.w.toFixed(2)}</label>
          <input
            type="range"
            min={-1}
            max={0}
            step={0.01}
            value={config.w}
            onChange={(e) => setConfig({ ...config, w: parseFloat(e.target.value) })}
            className="w-full mt-2"
          />
        </div>
      </div>

      {/* Heatmap */}
      <div className="bg-dark-surface rounded-lg border border-dark-border overflow-hidden">
        <Plot
          data={traces}
          layout={layout}
          config={{
            displayModeBar: true,
            displaylogo: false,
            responsive: true
          }}
          style={{ width: '100%', height: '550px' }}
        />
      </div>

      {/* Legend */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4 text-sm">
        <div className="bg-dark-bg rounded-lg p-3 flex items-center gap-3">
          <div className="w-4 h-4 rounded-full bg-green-500"></div>
          <span className="text-gray-300">Classical optimum (k=0, s=0) - lowest objective</span>
        </div>
        <div className="bg-dark-bg rounded-lg p-3 flex items-center gap-3">
          <div className="w-4 h-1 bg-red-500"></div>
          <span className="text-gray-300">BBN constraint: |s| must be less than 0.05</span>
        </div>
        <div className="bg-dark-bg rounded-lg p-3 flex items-center gap-3">
          <div className="w-4 h-1 bg-yellow-500"></div>
          <span className="text-gray-300">CMB constraint: |k| must be less than 0.03</span>
        </div>
      </div>
    </div>
  );
}
