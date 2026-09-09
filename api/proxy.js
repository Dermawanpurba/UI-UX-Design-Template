// Vercel Serverless Function: AI CORS Proxy
// Endpoint: /api/proxy
// Enterprise PRD Studio

module.exports = async function handler(req, res) {
  // 1. CORS Headers for Web Browser Access
  res.setHeader('Access-Control-Allow-Credentials', 'true');
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET,OPTIONS,POST');
  res.setHeader(
    'Access-Control-Allow-Headers',
    'X-CSRF-Token, X-Requested-With, Accept, Accept-Version, Content-Length, Content-MD5, Content-Type, Date, X-Api-Version, Authorization'
  );

  // 2. Handle CORS Preflight
  if (req.method === 'OPTIONS') {
    res.status(200).end();
    return;
  }

  // 3. Handle Health Check Ping (GET)
  if (req.method === 'GET') {
    return res.status(200).json({
      status: 'ok',
      proxy: 'Enterprise PRD Studio Vercel Serverless Proxy',
      platform: 'Vercel Serverless (Node.js)',
      time: Date.now()
    });
  }

  // 4. Only Accept POST
  if (req.method !== 'POST') {
    return res.status(405).json({
      error: { message: 'Method Not Allowed. Only POST is supported.' }
    });
  }

  try {
    const body = req.body || {};
    const { endpoint, apiKey, body: aiPayload } = body;

      let endpointUrl;
      try {
        endpointUrl = new URL(endpoint);
      } catch {
        return res.status(400).json({ error: { message: 'Invalid endpoint URL.' } });
      }
      if (!['http:', 'https:'].includes(endpointUrl.protocol)) {
        return res.status(400).json({ error: { message: 'Only HTTP(S) endpoint URLs are allowed.' } });
      }
  
      if (!endpoint || typeof endpoint !== 'string' || !endpoint.trim()) {
      return res.status(400).json({
        error: { message: 'Missing or invalid "endpoint" in request payload.' }
      });
    }

    const headers = {
      'Content-Type': 'application/json',
      'Accept': 'application/json',
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) EnterprisePRDStudio/2.0'
    };

    if (apiKey && typeof apiKey === 'string' && apiKey.trim()) {
      headers['Authorization'] = `Bearer ${apiKey.trim()}`;
    }

    // Abort after 55 seconds to gracefully return before Vercel 60s hard kill
    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), 55000);

    const upstreamResponse = await fetch(endpointUrl.toString(), {
      method: 'POST',
      headers,
      body: JSON.stringify(aiPayload || {}),
      signal: controller.signal
    });

    clearTimeout(timeoutId);

    const contentType = upstreamResponse.headers.get('content-type') || '';
    if (contentType.includes('application/json')) {
      const json = await upstreamResponse.json();
      return res.status(upstreamResponse.status).json(json);
    } else {
      const text = await upstreamResponse.text();
      return res.status(upstreamResponse.status).send(text);
    }

  } catch (error) {
    if (error.name === 'AbortError') {
      return res.status(504).json({
        error: {
          message: 'Vercel Serverless Timeout (55 detik). Model AI memerlukan waktu terlalu lama untuk merancang seluruh dokumen sekaligus. Solusi: Gunakan fitur "Isi Per Step" yang hanya memerlukan 5-15 detik.'
        }
      });
    }

    return res.status(502).json({
      error: {
        message: 'Vercel Proxy Error: ' + (error.message || 'Gagal menghubungi endpoint AI target')
      }
    });
  }
};
