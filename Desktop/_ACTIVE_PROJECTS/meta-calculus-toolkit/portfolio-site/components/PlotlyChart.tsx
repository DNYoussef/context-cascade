'use client';

import { useEffect, useState } from 'react';

// Props type for Plotly
interface PlotlyProps {
  data: any[];
  layout?: any;
  config?: any;
  style?: React.CSSProperties;
  onInitialized?: (figure: any, graphDiv: any) => void;
  onUpdate?: (figure: any, graphDiv: any) => void;
}

export default function PlotlyChart({ data, layout, config, style }: PlotlyProps) {
  const [Plot, setPlot] = useState<any>(null);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    // Only import Plotly on client side
    import('react-plotly.js').then((mod) => {
      setPlot(() => mod.default);
      setIsLoading(false);
    }).catch((err) => {
      console.error('Failed to load Plotly:', err);
      setIsLoading(false);
    });
  }, []);

  if (isLoading || !Plot) {
    return (
      <div
        className="flex items-center justify-center bg-dark-surface rounded-lg"
        style={style || { height: '400px', width: '100%' }}
      >
        <div className="text-center">
          <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-primary-400 mx-auto mb-2"></div>
          <span className="text-gray-400 text-sm">Loading visualization...</span>
        </div>
      </div>
    );
  }

  return (
    <Plot
      data={data}
      layout={layout}
      config={config}
      style={style}
    />
  );
}
