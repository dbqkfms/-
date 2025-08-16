import { Hono } from 'hono'
import { cors } from 'hono/cors'

const app = new Hono()

// Enable CORS for API routes
app.use('/api/*', cors())

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
