#!/usr/bin/env node
/**
 * Netlify Deployment Automation
 *
 * Automates deployment to Netlify via CLI.
 * Handles authentication, site creation, and deployment.
 *
 * Usage: node netlify-deploy.js --site-name <name> --dir <directory>
 *
 * Requirements:
 * - npm install -g netlify-cli
 * - netlify login (one-time auth)
 */

const { execSync, spawn } = require('child_process');
const fs = require('fs');
const path = require('path');

// Parse command line arguments
function parseArgs(args) {
  const parsed = {
    siteName: null,
    dir: '.',
    prod: true,
    message: 'Deployed via Landing Page Generator'
  };

  for (let i = 0; i < args.length; i++) {
    switch (args[i]) {
      case '--site-name':
      case '-s':
        parsed.siteName = args[++i];
        break;
      case '--dir':
      case '-d':
        parsed.dir = args[++i];
        break;
      case '--staging':
        parsed.prod = false;
        break;
      case '--message':
      case '-m':
        parsed.message = args[++i];
        break;
    }
  }

  return parsed;
}

/**
 * Check if Netlify CLI is installed
 */
function checkNetlifyCLI() {
  try {
    execSync('netlify --version', { stdio: 'pipe' });
    return true;
  } catch (e) {
    return false;
  }
}

/**
 * Check if user is authenticated
 */
function checkAuth() {
  try {
    const result = execSync('netlify status', { stdio: 'pipe' }).toString();
    return result.includes('Logged in');
  } catch (e) {
    return false;
  }
}

/**
 * Install Netlify CLI
 */
function installNetlifyCLI() {
  console.log('Installing Netlify CLI...');
  try {
    execSync('npm install -g netlify-cli', { stdio: 'inherit' });
    return true;
  } catch (e) {
    console.error('Failed to install Netlify CLI');
    console.error('Try: npm install -g netlify-cli');
    return false;
  }
}

/**
 * Authenticate with Netlify
 */
async function authenticate() {
  console.log('');
  console.log('Netlify authentication required.');
  console.log('A browser window will open for authentication.');
  console.log('');

  return new Promise((resolve, reject) => {
    const login = spawn('netlify', ['login'], {
      stdio: 'inherit',
      shell: true
    });

    login.on('close', (code) => {
      if (code === 0) {
        resolve(true);
      } else {
        reject(new Error('Authentication failed'));
      }
    });

    login.on('error', reject);
  });
}

/**
 * Create or link Netlify site
 */
async function setupSite(siteName, dir) {
  const netlifyTomlPath = path.join(dir, 'netlify.toml');

  // Create netlify.toml if it doesn't exist
  if (!fs.existsSync(netlifyTomlPath)) {
    const netlifyConfig = `[build]
  publish = "."

[build.environment]
  NODE_VERSION = "18"

[[headers]]
  for = "/*"
  [headers.values]
    X-Frame-Options = "DENY"
    X-XSS-Protection = "1; mode=block"
    X-Content-Type-Options = "nosniff"
    Referrer-Policy = "strict-origin-when-cross-origin"
`;
    fs.writeFileSync(netlifyTomlPath, netlifyConfig);
    console.log('Created netlify.toml');
  }

  // Check if site already exists
  try {
    const sites = execSync('netlify sites:list --json', { stdio: 'pipe' }).toString();
    const siteList = JSON.parse(sites);
    const existingSite = siteList.find(s => s.name === siteName);

    if (existingSite) {
      console.log(`Site "${siteName}" already exists. Linking...`);
      execSync(`netlify link --name ${siteName}`, { cwd: dir, stdio: 'inherit' });
      return existingSite;
    }
  } catch (e) {
    // Sites list failed, continue with creation
  }

  // Create new site
  console.log(`Creating new site: ${siteName}`);
  try {
    const result = execSync(
      `netlify sites:create --name ${siteName} --with-ci`,
      { cwd: dir, stdio: 'pipe' }
    ).toString();

    console.log('Site created successfully');
    return { name: siteName };
  } catch (e) {
    // Site name might be taken
    console.log(`Site name "${siteName}" may be taken. Trying with random suffix...`);
    const randomSuffix = Math.random().toString(36).substring(2, 8);
    const newName = `${siteName}-${randomSuffix}`;

    execSync(
      `netlify sites:create --name ${newName} --with-ci`,
      { cwd: dir, stdio: 'inherit' }
    );

    console.log(`Site created as: ${newName}`);
    return { name: newName };
  }
}

/**
 * Deploy to Netlify
 */
async function deploy(options) {
  const { siteName, dir, prod, message } = options;

  console.log('');
  console.log('Starting deployment...');
  console.log(`  Directory: ${path.resolve(dir)}`);
  console.log(`  Site: ${siteName}`);
  console.log(`  Environment: ${prod ? 'Production' : 'Staging (draft)'}`);
  console.log('');

  const deployCmd = prod
    ? `netlify deploy --prod --dir="${dir}" --message="${message}"`
    : `netlify deploy --dir="${dir}" --message="${message}"`;

  return new Promise((resolve, reject) => {
    const deployProcess = spawn('netlify',
      prod
        ? ['deploy', '--prod', `--dir=${dir}`, `--message=${message}`]
        : ['deploy', `--dir=${dir}`, `--message=${message}`],
      {
        stdio: 'pipe',
        shell: true,
        cwd: dir
      }
    );

    let output = '';

    deployProcess.stdout.on('data', (data) => {
      const text = data.toString();
      output += text;
      process.stdout.write(text);
    });

    deployProcess.stderr.on('data', (data) => {
      process.stderr.write(data);
    });

    deployProcess.on('close', (code) => {
      if (code === 0) {
        // Extract URLs from output
        const urlMatch = output.match(/Website URL:\s*(https?:\/\/[^\s]+)/);
        const deployIdMatch = output.match(/Deploy ID:\s*([^\s]+)/);

        const result = {
          success: true,
          url: urlMatch ? urlMatch[1] : null,
          deployId: deployIdMatch ? deployIdMatch[1] : null,
          siteName: siteName,
          environment: prod ? 'production' : 'draft'
        };

        // Save deployment record
        const recordPath = path.join(dir, 'deployment-record.json');
        fs.writeFileSync(recordPath, JSON.stringify(result, null, 2));

        resolve(result);
      } else {
        reject(new Error(`Deployment failed with code ${code}`));
      }
    });

    deployProcess.on('error', reject);
  });
}

/**
 * Main deployment workflow
 */
async function main() {
  const args = process.argv.slice(2);

  if (args.length === 0 || args.includes('--help') || args.includes('-h')) {
    console.log('Netlify Deployment Automation');
    console.log('==============================');
    console.log('');
    console.log('Usage: node netlify-deploy.js --site-name <name> --dir <directory>');
    console.log('');
    console.log('Options:');
    console.log('  --site-name, -s  Site name (required)');
    console.log('  --dir, -d        Directory to deploy (default: current)');
    console.log('  --staging        Deploy as draft (not production)');
    console.log('  --message, -m    Deployment message');
    console.log('');
    console.log('Examples:');
    console.log('  node netlify-deploy.js --site-name my-landing-page --dir ./dist');
    console.log('  node netlify-deploy.js -s product-launch -d . --staging');
    console.log('');
    console.log('Prerequisites:');
    console.log('  1. npm install -g netlify-cli');
    console.log('  2. netlify login');
    process.exit(0);
  }

  const options = parseArgs(args);

  if (!options.siteName) {
    console.error('Error: --site-name is required');
    process.exit(1);
  }

  // Resolve directory
  options.dir = path.resolve(options.dir);

  if (!fs.existsSync(options.dir)) {
    console.error(`Error: Directory not found: ${options.dir}`);
    process.exit(1);
  }

  // Check for index.html
  const indexPath = path.join(options.dir, 'index.html');
  if (!fs.existsSync(indexPath)) {
    console.error(`Error: No index.html found in ${options.dir}`);
    process.exit(1);
  }

  try {
    // Step 1: Check/Install CLI
    if (!checkNetlifyCLI()) {
      console.log('Netlify CLI not found.');
      if (!installNetlifyCLI()) {
        process.exit(1);
      }
    }
    console.log('Netlify CLI: OK');

    // Step 2: Check/Perform Auth
    if (!checkAuth()) {
      console.log('Not authenticated with Netlify.');
      await authenticate();
    }
    console.log('Authentication: OK');

    // Step 3: Setup site
    await setupSite(options.siteName, options.dir);
    console.log('Site setup: OK');

    // Step 4: Deploy
    const result = await deploy(options);

    console.log('');
    console.log('=================================');
    console.log('DEPLOYMENT SUCCESSFUL');
    console.log('=================================');
    console.log('');
    console.log(`Live URL: ${result.url}`);
    console.log(`Deploy ID: ${result.deployId}`);
    console.log(`Environment: ${result.environment}`);
    console.log('');

    // Return result for programmatic use
    return result;

  } catch (error) {
    console.error('');
    console.error('DEPLOYMENT FAILED');
    console.error(error.message);
    console.error('');
    console.error('Troubleshooting:');
    console.error('  1. Ensure netlify-cli is installed: npm install -g netlify-cli');
    console.error('  2. Authenticate: netlify login');
    console.error('  3. Check site name availability on Netlify dashboard');
    process.exit(1);
  }
}

main();
