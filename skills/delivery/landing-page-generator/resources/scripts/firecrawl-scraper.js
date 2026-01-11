#!/usr/bin/env node
/**
 * Firecrawl Branding Extractor
 *
 * Extracts branding guidelines from any URL using Firecrawl API.
 * Returns JSON with colors, fonts, buttons, spacing patterns.
 *
 * Usage: node firecrawl-scraper.js <url> [output-file]
 *
 * Requirements:
 * - FIRECRAWL_API_KEY environment variable
 * - npm install axios
 */

const https = require('https');
const fs = require('fs');
const path = require('path');

// Configuration
const FIRECRAWL_API_URL = 'https://api.firecrawl.dev/v1/scrape';
const DEFAULT_OUTPUT = 'branding.json';

/**
 * Extract branding from URL using Firecrawl
 */
async function extractBranding(url, outputFile) {
  const apiKey = process.env.FIRECRAWL_API_KEY;

  if (!apiKey) {
    console.error('Error: FIRECRAWL_API_KEY environment variable not set');
    console.error('Get your API key at: https://firecrawl.dev');
    process.exit(1);
  }

  console.log(`Extracting branding from: ${url}`);

  const requestBody = JSON.stringify({
    url: url,
    formats: ['branding'],  // CRITICAL: Only request branding format
    onlyMainContent: false
  });

  const options = {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${apiKey}`
    }
  };

  return new Promise((resolve, reject) => {
    const req = https.request(FIRECRAWL_API_URL, options, (res) => {
      let data = '';

      res.on('data', (chunk) => {
        data += chunk;
      });

      res.on('end', () => {
        try {
          const response = JSON.parse(data);

          if (res.statusCode !== 200) {
            console.error(`API Error (${res.statusCode}):`, response);
            reject(new Error(`Firecrawl API error: ${res.statusCode}`));
            return;
          }

          // Extract branding data
          const branding = response.data?.branding || response.branding || {};

          // Structure the output
          const brandingOutput = {
            source_url: url,
            extracted_at: new Date().toISOString(),
            branding: {
              theme: branding.theme || 'unknown',
              colors: {
                primary: branding.primaryColor || branding.colors?.primary || '#000000',
                secondary: branding.secondaryColor || branding.colors?.secondary || '#ffffff',
                accent: branding.accentColor || branding.colors?.accent || '#0066cc',
                background: branding.backgroundColor || branding.colors?.background || '#ffffff',
                text: branding.textColor || branding.colors?.text || '#333333'
              },
              typography: {
                primaryFont: branding.fonts?.primary || branding.primaryFont || 'system-ui',
                secondaryFont: branding.fonts?.secondary || branding.secondaryFont || 'system-ui',
                baseFontSize: branding.fontSize || '16px',
                headingWeight: branding.headingWeight || '700',
                bodyWeight: branding.bodyWeight || '400'
              },
              buttons: {
                shape: branding.buttonShape || 'rounded',
                primaryStyle: branding.buttonStyle || 'filled',
                borderRadius: branding.borderRadius || '8px'
              },
              spacing: {
                containerWidth: branding.containerWidth || '1200px',
                sectionPadding: branding.sectionPadding || '80px',
                componentGap: branding.componentGap || '24px'
              },
              images: branding.images || []
            },
            raw_response: branding
          };

          // Write to file
          const outputPath = path.resolve(outputFile || DEFAULT_OUTPUT);
          fs.writeFileSync(outputPath, JSON.stringify(brandingOutput, null, 2));

          console.log(`Branding extracted successfully!`);
          console.log(`Output saved to: ${outputPath}`);
          console.log(`\nKey colors:`);
          console.log(`  Primary: ${brandingOutput.branding.colors.primary}`);
          console.log(`  Secondary: ${brandingOutput.branding.colors.secondary}`);
          console.log(`  Accent: ${brandingOutput.branding.colors.accent}`);
          console.log(`\nFonts:`);
          console.log(`  Primary: ${brandingOutput.branding.typography.primaryFont}`);

          resolve(brandingOutput);
        } catch (parseError) {
          console.error('Error parsing response:', parseError);
          reject(parseError);
        }
      });
    });

    req.on('error', (error) => {
      console.error('Request error:', error);
      reject(error);
    });

    req.write(requestBody);
    req.end();
  });
}

/**
 * Fallback: Extract basic branding from HTML (no API needed)
 */
async function extractBrandingFallback(url, outputFile) {
  console.log('Using fallback extraction (no API key)...');
  console.log(`Fetching: ${url}`);

  return new Promise((resolve, reject) => {
    const protocol = url.startsWith('https') ? https : require('http');

    protocol.get(url, (res) => {
      let html = '';

      res.on('data', (chunk) => {
        html += chunk;
      });

      res.on('end', () => {
        // Basic color extraction from CSS
        const colorMatches = html.match(/#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3}|rgb\([^)]+\)/g) || [];
        const fontMatches = html.match(/font-family:\s*([^;]+)/g) || [];

        const brandingOutput = {
          source_url: url,
          extracted_at: new Date().toISOString(),
          extraction_method: 'fallback',
          branding: {
            colors: {
              detected: [...new Set(colorMatches.slice(0, 10))],
              primary: colorMatches[0] || '#000000',
              secondary: colorMatches[1] || '#ffffff'
            },
            typography: {
              detected: [...new Set(fontMatches.slice(0, 5))]
            }
          },
          note: 'Fallback extraction - for full branding, set FIRECRAWL_API_KEY'
        };

        const outputPath = path.resolve(outputFile || DEFAULT_OUTPUT);
        fs.writeFileSync(outputPath, JSON.stringify(brandingOutput, null, 2));

        console.log(`Basic branding extracted to: ${outputPath}`);
        console.log('Note: For complete branding extraction, set FIRECRAWL_API_KEY');

        resolve(brandingOutput);
      });
    }).on('error', reject);
  });
}

// Main execution
async function main() {
  const args = process.argv.slice(2);

  if (args.length === 0) {
    console.log('Firecrawl Branding Extractor');
    console.log('============================');
    console.log('');
    console.log('Usage: node firecrawl-scraper.js <url> [output-file]');
    console.log('');
    console.log('Examples:');
    console.log('  node firecrawl-scraper.js https://apple.com/iphone');
    console.log('  node firecrawl-scraper.js https://stripe.com branding-stripe.json');
    console.log('');
    console.log('Environment:');
    console.log('  FIRECRAWL_API_KEY - Your Firecrawl API key (get at firecrawl.dev)');
    process.exit(0);
  }

  const url = args[0];
  const outputFile = args[1] || DEFAULT_OUTPUT;

  // Validate URL
  try {
    new URL(url);
  } catch (e) {
    console.error(`Invalid URL: ${url}`);
    process.exit(1);
  }

  try {
    if (process.env.FIRECRAWL_API_KEY) {
      await extractBranding(url, outputFile);
    } else {
      await extractBrandingFallback(url, outputFile);
    }
  } catch (error) {
    console.error('Extraction failed:', error.message);
    process.exit(1);
  }
}

main();
