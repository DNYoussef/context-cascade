/**
 * Client-side API wrapper for calling server-side agent endpoints
 *
 * IMPORTANT: This file runs on the client and DOES NOT have access
 * to GLOBALMOO_API_KEY. All agent orchestration happens server-side.
 */

export interface AgentRequest {
  agentType: 'researcher' | 'computational' | 'validator' | 'synthesizer';
  task: string;
  parameters?: Record<string, any>;
}

export interface AgentResponse {
  success: boolean;
  data?: any;
  error?: string;
  details?: any;
}

/**
 * Trigger an AI agent task via server-side API route
 */
export async function triggerAgent(request: AgentRequest): Promise<AgentResponse> {
  try {
    const response = await fetch('/api/agents', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(request),
    });

    const result = await response.json();

    if (!response.ok) {
      throw new Error(result.error || 'Agent request failed');
    }

    return result;
  } catch (error) {
    console.error('Error triggering agent:', error);
    return {
      success: false,
      error: error instanceof Error ? error.message : 'Unknown error',
    };
  }
}

/**
 * Check if the API is configured and available
 */
export async function checkApiHealth(): Promise<{
  status: string;
  apiConfigured: boolean;
  message: string;
}> {
  try {
    const response = await fetch('/api/agents');
    const result = await response.json();
    return result;
  } catch (error) {
    return {
      status: 'error',
      apiConfigured: false,
      message: 'Failed to connect to API',
    };
  }
}
