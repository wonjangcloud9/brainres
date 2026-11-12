<!-- Q: How do I add a custom domain to a Vercel project? -->

Add it in the dashboard under your project's **Settings → Domains**, then point your DNS at Vercel.

**Dashboard method**

1. Open your project in Vercel and go to **Settings → Domains**.
2. Enter your domain (e.g. `example.com`) and click **Add**.
3. Vercel shows the DNS records you need. Add them at your domain registrar or DNS host:
   - **Apex domain** (`example.com`): an `A` record pointing to `76.76.21.21`.
   - **Subdomain** (`www.example.com`): a `CNAME` record pointing to `cname.vercel-dns.com`.
4. Wait for DNS to propagate (minutes to a few hours). Vercel verifies it and issues an SSL certificate automatically.

Vercel may show a different, project-specific value for these records. If so, use what the dashboard displays, because those values take precedence over the generic ones above.

**CLI method**

```bash
vercel domains add example.com
```

Run it from the linked project directory, or pass the project name as a second argument: `vercel domains add example.com my-project`.

**Alternative: use Vercel nameservers.** Set your registrar's nameservers to the ones Vercel gives you (`ns1.vercel-dns.com`, `ns2.vercel-dns.com`). Vercel then manages all DNS records, which is simpler but moves every record for that domain to Vercel.

**Common tip:** add both `example.com` and `www.example.com`, and set one to redirect to the other so you don't serve duplicate sites.

Next step: open Settings → Domains for your project and add the domain, then copy the records it shows into your DNS provider.
