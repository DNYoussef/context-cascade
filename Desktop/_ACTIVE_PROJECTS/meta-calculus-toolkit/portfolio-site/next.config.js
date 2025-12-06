/** @type {import('next').NextConfig} */
const nextConfig = {
  // Ensure GLOBALMOO_API_KEY is only available server-side
  serverRuntimeConfig: {
    globalmooApiKey: process.env.GLOBALMOO_API_KEY,
  },

  // Transpile plotly for proper bundling
  transpilePackages: ['plotly.js', 'react-plotly.js'],

  // Webpack configuration for plotly
  webpack: (config, { isServer }) => {
    // Handle plotly.js which needs special treatment
    if (!isServer) {
      config.resolve.fallback = {
        ...config.resolve.fallback,
        fs: false,
        path: false,
      };
    }
    return config;
  },

  // Redirects for backward compatibility after site reorganization
  async redirects() {
    return [
      // Story pages
      { source: '/exploration', destination: '/story/hunch', permanent: true },
      { source: '/ai-journey', destination: '/story/audits', permanent: true },
      { source: '/quantum', destination: '/story/quantum', permanent: true },
      { source: '/geometry', destination: '/story/geometry', permanent: true },
      { source: '/validation', destination: '/results', permanent: true },
      // Learn pages
      { source: '/textbook', destination: '/learn/textbook', permanent: true },
      { source: '/math-history', destination: '/learn', permanent: true },
      { source: '/math-history/derivations', destination: '/learn/proofs', permanent: true },
      { source: '/math-history/failures', destination: '/learn/lessons', permanent: true },
      { source: '/math-history/timeline', destination: '/learn/textbook', permanent: true },
      { source: '/math-history/experiments', destination: '/results', permanent: true },
      // Tools pages
      { source: '/simulator', destination: '/tools/simulator', permanent: true },
      { source: '/code', destination: '/tools/code', permanent: true },
    ];
  },
};

module.exports = nextConfig;
