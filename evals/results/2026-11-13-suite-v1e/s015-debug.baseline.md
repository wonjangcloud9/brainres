<!-- Q: My fetch() call works in Postman but the browser says it's blocked by CORS policy. Why? -->

**CORS is enforced by the browser, not the server.** Postman isn't a browser, so it never checks CORS. It just sends the request and shows you the response. The browser sends the request too, but then refuses to hand the response to your JavaScript unless the server opts in via headers.

## What's actually happening

Your page's origin (e.g. `http://localhost:3000`) differs from the API's origin (different scheme, host, or port). The browser requires the response to include:

```
Access-Control-Allow-Origin: http://localhost:3000   (or *)
```

If it's missing, you get the CORS error, even though the request itself succeeded server-side.

## Preflight

If your request is "non-simple" (custom headers like `Authorization`, `Content-Type: application/json`, or methods like PUT/DELETE), the browser first sends an `OPTIONS` request. The server must answer it with:

```
Access-Control-Allow-Origin: <your origin>
Access-Control-Allow-Methods: GET, POST, PUT, DELETE
Access-Control-Allow-Headers: Content-Type, Authorization
```

A common cause: the server returns 404/405 for `OPTIONS`, or the preflight is blocked by auth middleware.

## Fixes (you need control of the server)

- **Add CORS headers on the server.** Examples:
  - Express: `app.use(require('cors')({ origin: 'http://localhost:3000' }))`
  - FastAPI: `CORSMiddleware` with `allow_origins=[...]`
  - Flask: `flask-cors`
- **Use a dev proxy** so the browser sees same-origin (Vite `server.proxy`, CRA `proxy`, Next.js `rewrites`).
- **Call the API from your own backend** instead of from the browser.

## Things that don't fix it

- `fetch(url, { mode: 'no-cors' })`: this gives you an opaque response you can't read. It just hides the error.
- Browser extensions that disable CORS: fine for quick testing only.

## Gotchas

- With `credentials: 'include'`, `Access-Control-Allow-Origin` can't be `*`; it must be the exact origin, plus `Access-Control-Allow-Credentials: true`.
- Redirects on preflight requests fail.
- Check the Network tab: look at the `OPTIONS` request and the response headers to see exactly what's missing.

If you tell me the API (yours or third-party), your frontend origin, and the exact error text, I can pinpoint which case you're in. If the code is in this directory, I can also look at the server setup.
