<!-- Q: My fetch() call works in Postman but the browser says it's blocked by CORS policy. Why? -->

Postman never enforces CORS, but browsers do: the server's response lacks an `Access-Control-Allow-Origin` header that permits your page's origin, so the browser refuses to hand the response to your JavaScript.

The request often still reaches the server. The browser just blocks your code from reading the reply.

**Fix it on the server, not in `fetch()`.** Add the header for your page's origin. Example in Express:

```js
const cors = require('cors');
app.use(cors({ origin: 'http://localhost:3000' }));
```

Or set the headers by hand:

```
Access-Control-Allow-Origin: http://localhost:3000
Access-Control-Allow-Methods: GET, POST, PUT, DELETE
Access-Control-Allow-Headers: Content-Type, Authorization
```

**Preflight is the most common trap.** If you send JSON (`Content-Type: application/json`), a custom header like `Authorization`, or a method such as PUT or DELETE, the browser first sends an `OPTIONS` request. The server must answer it with a 2xx status and the headers above. If `OPTIONS` returns 404 or 405, you get the CORS error even though the real endpoint works.

**Other causes to check:**

- **Credentials:** with `credentials: 'include'`, the origin must be exact (not `*`), and you need `Access-Control-Allow-Credentials: true`.
- **Redirects:** a redirect that drops the CORS headers fails the request.
- **Error responses:** a 500 from a crashing server often has no CORS headers, so it shows up as a CORS error. Check the server logs.

**Workarounds when you don't control the server:** proxy the request through your own backend, or use your dev server's proxy (for example Vite's `server.proxy`). Don't use `mode: 'no-cors'`, because it returns an opaque response you cannot read.

To pin down your case, open DevTools → Network, click the failed request, and look for an `OPTIONS` call. If you paste the exact error text and the response headers, I can tell you which header is missing.
