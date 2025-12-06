import { NextRequest, NextResponse } from 'next/server';

/**
 * API Route for GlobalMoo Agent Orchestration
 *
 * SECURITY: GLOBALMOO_API_KEY is only accessible server-side.
 * This route handles communication with GlobalMoo API without
 * exposing credentials to the client.
 */
export async function POST(request: NextRequest) {
  try {
    // Get API key from environment (server-side only)
    const apiKey = process.env.GLOBALMOO_API_KEY;

    if (!apiKey) {
      console.error('GLOBALMOO_API_KEY not configured in environment');
      return NextResponse.json(
        { error: 'API key not configured' },
        { status: 500 }
      );
    }

    // Parse request body
    const body = await request.json();
    const { agentType, task, parameters } = body;

    if (!agentType || !task) {
      return NextResponse.json(
        { error: 'Missing required fields: agentType and task' },
        { status: 400 }
      );
    }

    // Call GlobalMoo API
    // CORRECT URL per https://globalmoo.gitbook.io/globalmoo-documentation
    const response = await fetch('https://app.globalmoo.com/api/v1/agents', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${apiKey}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        agent: agentType,
        task: task,
        parameters: parameters || {},
      }),
    });

    if (!response.ok) {
      const errorData = await response.json();
      console.error('GlobalMoo API error:', errorData);
      return NextResponse.json(
        { error: 'Agent orchestration failed', details: errorData },
        { status: response.status }
      );
    }

    const result = await response.json();

    return NextResponse.json({
      success: true,
      data: result,
    });
  } catch (error) {
    console.error('Error in agent API route:', error);
    return NextResponse.json(
      { error: 'Internal server error', message: error instanceof Error ? error.message : 'Unknown error' },
      { status: 500 }
    );
  }
}

/**
 * GET endpoint to check API availability
 */
export async function GET() {
  const apiKey = process.env.GLOBALMOO_API_KEY;

  return NextResponse.json({
    status: 'ok',
    apiConfigured: !!apiKey,
    message: apiKey
      ? 'GlobalMoo API is configured'
      : 'GlobalMoo API key not configured',
  });
}
