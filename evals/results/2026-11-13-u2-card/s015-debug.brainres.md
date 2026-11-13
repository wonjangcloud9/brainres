<!-- Q: My fetch() call works in Postman but the browser says it's blocked by CORS policy. Why? -->

Postman isn't a browser, so it doesn't enforce CORS; the browser does, and it blocks your response because the server didn't send an `Access-Control-Allow-Origin` header that permits your page's origin.

The request usually reaches the server and gets a response. The browser then refuses to hand that response to your JavaScript. Postman just shows whatever comes back.

**Fix it on the server** (the only real fix). Add headers like these to the API's responses:

```
Access-Control-Allow-Origin: https://your-site.com
Access-Control-Allow-Methods: GET, POST, PUT, DELETE, OPTIONS
Access-Control-Allow-Headers: Content-Type, Authorization
```

If your request uses a non-simple method or header (e.g. `Authorization`, `Content-Type: application/json`, `PUT`, `DELETE`), the browser first sends an `OPTIONS` preflight. The server must answer it with a 2xx status and the headers above, or the real request never goes out.

**Common gotchas:**
- Using `credentials: 'include'` requires a specific origin (not `*`) plus `Access-Control-Allow-Credentials: true`.
- Redirects (e.g. http→https or a trailing-slash 301) on the preflight request fail CORS.
- An error response (401/500) without CORS headers shows up as a CORS error, hiding the real status.

**If you don't control the server:** proxy the call through your own backend, or use a dev proxy (Vite `server.proxy`, webpack `devServer.proxy`). Don't use `mode: 'no-cors'`; it gives you an opaque response you can't read.

To pin down the cause, open DevTools → Network, click the failed request (and its `OPTIONS` twin), and check which `Access-Control-*` header is missing. If you paste the exact console error and the server framework (Express, Django, etc.), I can give you the exact config.
