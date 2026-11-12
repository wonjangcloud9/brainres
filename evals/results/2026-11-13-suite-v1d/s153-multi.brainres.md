<!-- Q: What is a CDN, and does my small personal blog need one? -->

A CDN (content delivery network) is a set of servers around the world that keep copies of your site's files and serve each visitor from the nearest one. A small blog doesn't *need* one, but it's usually free and worth having.

**Why you may not need one:** a small blog's pages are light, and a single server answers in a fraction of a second for most visitors. Traffic is low, so load isn't a problem.

**When it helps anyway:**

| Situation | Does a CDN help? |
|---|---|
| Hosted on Netlify, Vercel, GitHub Pages or Cloudflare Pages | You already have one built in. |
| Your own VPS or shared hosting | Yes, especially for readers far from your server. |
| Many large images or video | Yes, it cuts bandwidth and load time. |
| A post suddenly goes viral | Yes, it absorbs the spike so your server doesn't fall over. |

**Costs:** cached pages can show stale content after you edit (you may need to purge the cache), and it adds one more service to configure. Cloudflare's free plan is the common choice for self-hosted blogs, and setup is mostly a DNS change.

Where is your blog hosted? That decides whether you have a CDN already or should add one.
