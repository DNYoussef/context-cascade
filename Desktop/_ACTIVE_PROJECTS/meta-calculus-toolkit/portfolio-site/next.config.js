const withMDX = require('@next/mdx')({
  extension: /\.mdx?$/,
  options: {
    remarkPlugins: [],
    rehypePlugins: [],
  },
});

/** @type {import('next').NextConfig} */
const nextConfig = {
  pageExtensions: ['js', 'jsx', 'mdx', 'ts', 'tsx'],

  // Ensure GLOBALMOO_API_KEY is only available server-side
  serverRuntimeConfig: {
    globalmooApiKey: process.env.GLOBALMOO_API_KEY,
  },

  // Public runtime config (client-side accessible)
  publicRuntimeConfig: {
    // Add any public env vars here if needed
  },

  env: {
    // Only expose non-sensitive variables here
  },

  // Output standalone for Railway deployment
  output: 'standalone',
};

module.exports = withMDX(nextConfig);
