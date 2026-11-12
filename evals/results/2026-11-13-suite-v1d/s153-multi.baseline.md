<!-- Q: What is a CDN, and does my small personal blog need one? -->

**A CDN (Content Delivery Network)** is a network of servers spread across many geographic locations that cache copies of your site's content (images, CSS, JS, sometimes full HTML) and serve each visitor from the server closest to them. Your origin server only handles requests the CDN can't answer from cache.

**What it gives you:**
- **Lower latency**: a visitor in Seoul gets files from a nearby edge node instead of a server in Virginia.
- **Less load on your origin**: cached requests never reach it.
- **Traffic spike resilience**: a post hitting the front page of Hacker News won't knock over a cheap VPS.
- **Extras**: free TLS, DDoS mitigation, and compression/image optimization, depending on the provider.

**Does your small blog need one?** Probably not as a deliberate step, but you may already be getting one for free.

- **If it's a static site** (Hugo, Jekyll, Astro, etc.) on Netlify, Vercel, GitHub Pages, Cloudflare Pages, or similar, it's already served through a CDN. Nothing to do.
- **If it's on a single VPS or shared hosting** with a mostly local audience and modest traffic, you don't need one. Pages will be fast enough.
- **Worth adding if**: your readers are globally distributed, you serve large images or video, you've seen slowdowns or server overload from traffic spikes, or you're on a dynamic CMS like WordPress where caching saves real CPU.

**Easy path if you do want one:** put Cloudflare's free tier in front of your domain. It takes a few minutes (change nameservers), costs nothing, and covers caching, HTTPS, and basic DDoS protection.

If you tell me how your blog is built and hosted, I can say whether you're already behind a CDN and whether anything's worth changing.
