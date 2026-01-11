#!/usr/bin/env node
/**
 * Full-Page Screenshot Capture
 *
 * Captures full-page screenshots of websites for design inspiration.
 * Uses Puppeteer for reliable rendering.
 *
 * Usage: node screenshot-capture.js <url> [output-file]
 *
 * Requirements:
 * - npm install puppeteer
 */

const fs = require('fs');
const path = require('path');

// Check for puppeteer
let puppeteer;
try {
  puppeteer = require('puppeteer');
} catch (e) {
  console.log('Puppeteer not installed. Installing...');
  const { execSync } = require('child_process');
  execSync('npm install puppeteer', { stdio: 'inherit' });
  puppeteer = require('puppeteer');
}

const DEFAULT_OUTPUT = 'inspiration-screenshot.png';
const VIEWPORT = { width: 1440, height: 900 };

/**
 * Capture full-page screenshot
 */
async function captureScreenshot(url, outputFile) {
  console.log(`Capturing screenshot of: ${url}`);

  let browser;
  try {
    browser = await puppeteer.launch({
      headless: 'new',
      args: [
        '--no-sandbox',
        '--disable-setuid-sandbox',
        '--disable-dev-shm-usage'
      ]
    });

    const page = await browser.newPage();

    // Set viewport
    await page.setViewport(VIEWPORT);

    // Set user agent to avoid bot detection
    await page.setUserAgent(
      'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    );

    console.log('Loading page...');

    // Navigate with timeout
    await page.goto(url, {
      waitUntil: 'networkidle2',
      timeout: 30000
    });

    // Wait for any lazy-loaded content
    await page.evaluate(() => new Promise(resolve => setTimeout(resolve, 2000)));

    // Scroll to load lazy images
    console.log('Scrolling to load lazy content...');
    await autoScroll(page);

    // Scroll back to top
    await page.evaluate(() => window.scrollTo(0, 0));
    await page.evaluate(() => new Promise(resolve => setTimeout(resolve, 500)));

    // Get page dimensions
    const dimensions = await page.evaluate(() => ({
      width: document.documentElement.scrollWidth,
      height: document.documentElement.scrollHeight
    }));

    console.log(`Page dimensions: ${dimensions.width}x${dimensions.height}`);

    // Capture full page
    const outputPath = path.resolve(outputFile || DEFAULT_OUTPUT);

    await page.screenshot({
      path: outputPath,
      fullPage: true,
      type: 'png'
    });

    console.log(`Screenshot saved to: ${outputPath}`);
    console.log(`Dimensions: ${dimensions.width}x${dimensions.height}`);

    // Also generate metadata
    const metadata = {
      source_url: url,
      captured_at: new Date().toISOString(),
      viewport: VIEWPORT,
      page_dimensions: dimensions,
      screenshot_path: outputPath
    };

    const metadataPath = outputPath.replace('.png', '-metadata.json');
    fs.writeFileSync(metadataPath, JSON.stringify(metadata, null, 2));
    console.log(`Metadata saved to: ${metadataPath}`);

    return { screenshot: outputPath, metadata };

  } catch (error) {
    console.error('Screenshot capture failed:', error.message);
    throw error;
  } finally {
    if (browser) {
      await browser.close();
    }
  }
}

/**
 * Auto-scroll to trigger lazy loading
 */
async function autoScroll(page) {
  await page.evaluate(async () => {
    await new Promise((resolve) => {
      let totalHeight = 0;
      const distance = 500;
      const timer = setInterval(() => {
        const scrollHeight = document.documentElement.scrollHeight;
        window.scrollBy(0, distance);
        totalHeight += distance;

        if (totalHeight >= scrollHeight) {
          clearInterval(timer);
          resolve();
        }
      }, 100);
    });
  });
}

/**
 * Alternative: Use native fetch + canvas for simple screenshots
 * (Fallback when Puppeteer unavailable)
 */
async function captureSimpleScreenshot(url, outputFile) {
  console.log('Note: For full-page screenshots, install puppeteer');
  console.log('Using simplified capture method...');

  // Generate placeholder metadata
  const metadata = {
    source_url: url,
    captured_at: new Date().toISOString(),
    method: 'placeholder',
    note: 'Install puppeteer for actual screenshots: npm install puppeteer'
  };

  const outputPath = path.resolve(outputFile || DEFAULT_OUTPUT).replace('.png', '-metadata.json');
  fs.writeFileSync(outputPath, JSON.stringify(metadata, null, 2));

  console.log(`Metadata saved to: ${outputPath}`);
  console.log('');
  console.log('To capture actual screenshot:');
  console.log('  1. npm install puppeteer');
  console.log('  2. Re-run this script');
  console.log('');
  console.log('Or manually screenshot using browser DevTools:');
  console.log('  1. Open Chrome DevTools (F12)');
  console.log('  2. Press Cmd+Shift+P (Mac) or Ctrl+Shift+P (Windows)');
  console.log('  3. Type "screenshot" and select "Capture full size screenshot"');

  return { metadata };
}

// Main execution
async function main() {
  const args = process.argv.slice(2);

  if (args.length === 0) {
    console.log('Full-Page Screenshot Capture');
    console.log('============================');
    console.log('');
    console.log('Usage: node screenshot-capture.js <url> [output-file]');
    console.log('');
    console.log('Examples:');
    console.log('  node screenshot-capture.js https://apple.com/iphone');
    console.log('  node screenshot-capture.js https://stripe.com stripe-inspiration.png');
    console.log('');
    console.log('Requirements:');
    console.log('  npm install puppeteer');
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
    if (puppeteer) {
      await captureScreenshot(url, outputFile);
    } else {
      await captureSimpleScreenshot(url, outputFile);
    }
  } catch (error) {
    console.error('Screenshot failed:', error.message);

    // Fallback instructions
    console.log('');
    console.log('Manual screenshot instructions:');
    console.log('  Chrome: Cmd+Shift+P -> "Capture full size screenshot"');
    console.log('  Firefox: Ctrl+Shift+S -> Save full page');

    process.exit(1);
  }
}

main();
