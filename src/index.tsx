import { Hono } from 'hono'
import { cors } from 'hono/cors'

const app = new Hono()

// Enable CORS for API routes
app.use('/api/*', cors())

// ============================================================
// Seedream 4.5 API Proxy
// ============================================================

const SEEDREAM_PROVIDERS = {
  aimlapi: {
    url: 'https://api.aimlapi.com/v1/images/generations',
    model: 'bytedance/seedream-4-5'
  },
  byteplus: {
    url: 'https://api.byteplus.com/v1/images/generations',
    model: 'doubao-seedream-4-5-251128'
  }
}

// Image generation proxy endpoint
app.post('/api/seedream/generate', async (c) => {
  try {
    const body = await c.req.json()

    // Get API key from header or body
    const apiKey = c.req.header('X-API-Key') || body.apiKey
    if (!apiKey) {
      return c.json({
        success: false,
        error: 'API key is required'
      }, 401)
    }

    const provider = body.provider || 'aimlapi'
    const config = SEEDREAM_PROVIDERS[provider as keyof typeof SEEDREAM_PROVIDERS]

    if (!config) {
      return c.json({
        success: false,
        error: 'Invalid provider'
      }, 400)
    }

    // Build request payload
    const payload: Record<string, any> = {
      model: config.model,
      prompt: body.prompt,
      image_size: body.image_size || '2K',
      n: body.n || 1,
      response_format: body.response_format || 'url'
    }

    if (body.image_urls && body.image_urls.length > 0) {
      payload.image_urls = body.image_urls
    }

    if (body.seed !== undefined && body.seed !== null) {
      payload.seed = body.seed
    }

    if (body.watermark) {
      payload.watermark = true
    }

    // Call Seedream API
    const response = await fetch(config.url, {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${apiKey}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(payload)
    })

    const result = await response.json()

    if (!response.ok) {
      return c.json({
        success: false,
        error: result.error?.message || `API Error: ${response.status}`,
        details: result
      }, response.status)
    }

    return c.json({
      success: true,
      data: result.data || [],
      meta: result.meta || {}
    })

  } catch (error) {
    console.error('Seedream API error:', error)
    return c.json({
      success: false,
      error: error instanceof Error ? error.message : 'Internal server error'
    }, 500)
  }
})

// Batch/Parallel generation endpoint
app.post('/api/seedream/batch', async (c) => {
  try {
    const body = await c.req.json()

    const apiKey = c.req.header('X-API-Key') || body.apiKey
    if (!apiKey) {
      return c.json({
        success: false,
        error: 'API key is required'
      }, 401)
    }

    const { tasks, prompt, provider = 'aimlapi', options = {} } = body

    if (!tasks || !Array.isArray(tasks) || tasks.length === 0) {
      return c.json({
        success: false,
        error: 'Tasks array is required'
      }, 400)
    }

    const config = SEEDREAM_PROVIDERS[provider as keyof typeof SEEDREAM_PROVIDERS]
    if (!config) {
      return c.json({
        success: false,
        error: 'Invalid provider'
      }, 400)
    }

    // Process tasks in parallel
    const results = await Promise.all(
      tasks.map(async (task: { slot: number; imageUrl?: string }) => {
        try {
          const payload: Record<string, any> = {
            model: config.model,
            prompt,
            image_size: options.image_size || '2K',
            n: 1,
            response_format: 'url'
          }

          if (task.imageUrl) {
            payload.image_urls = [task.imageUrl]
          }

          if (options.seed !== undefined) {
            payload.seed = options.seed
          }

          const response = await fetch(config.url, {
            method: 'POST',
            headers: {
              'Authorization': `Bearer ${apiKey}`,
              'Content-Type': 'application/json'
            },
            body: JSON.stringify(payload)
          })

          const result = await response.json()

          if (!response.ok) {
            return {
              slot: task.slot,
              success: false,
              error: result.error?.message || `API Error: ${response.status}`
            }
          }

          return {
            slot: task.slot,
            success: true,
            data: result.data || []
          }

        } catch (error) {
          return {
            slot: task.slot,
            success: false,
            error: error instanceof Error ? error.message : 'Unknown error'
          }
        }
      })
    )

    const successful = results.filter(r => r.success)
    const failed = results.filter(r => !r.success)

    return c.json({
      success: failed.length === 0,
      total: results.length,
      successful: successful.length,
      failed: failed.length,
      results
    })

  } catch (error) {
    console.error('Seedream batch error:', error)
    return c.json({
      success: false,
      error: error instanceof Error ? error.message : 'Internal server error'
    }, 500)
  }
})

// API Routes
app.get('/api/status', (c) => {
  return c.json({ 
    status: 'ok',
    message: 'THISGLOBAL API is running',
    timestamp: new Date().toISOString()
  })
})

// Contact form API endpoint
app.post('/api/contact', async (c) => {
  try {
    const body = await c.req.json()
    
    // Validate required fields
    const requiredFields = ['company', 'name', 'phone', 'email', 'subject', 'message']
    for (const field of requiredFields) {
      if (!body[field]) {
        return c.json({ 
          success: false, 
          error: `${field} is required` 
        }, 400)
      }
    }
    
    // In production, you would:
    // 1. Send email notification
    // 2. Store in database
    // 3. Integrate with CRM
    
    // For now, just log and return success
    console.log('Contact form submission:', body)
    
    return c.json({ 
      success: true,
      message: '문의가 성공적으로 접수되었습니다.',
      data: body
    })
  } catch (error) {
    console.error('Contact form error:', error)
    return c.json({ 
      success: false, 
      error: 'Internal server error' 
    }, 500)
  }
})

// For development, we'll serve HTML directly
// In production, Cloudflare Pages handles static files automatically
app.get('/', (c) => {
  return c.html(`<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>THISGLOBAL - Beyond of Signage Paradigm</title>
    <script>window.location.href = '/index.html';</script>
</head>
<body>
    <p>Redirecting...</p>
</body>
</html>`)
})

export default app
