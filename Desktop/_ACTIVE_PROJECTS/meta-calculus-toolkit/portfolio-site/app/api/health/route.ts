import { NextResponse } from 'next/server';

/**
 * Health check endpoint for Railway monitoring
 */
export async function GET() {
  return NextResponse.json({
    status: 'healthy',
    timestamp: new Date().toISOString(),
    service: 'meta-calculus-portfolio',
    version: '1.0.0',
  });
}
