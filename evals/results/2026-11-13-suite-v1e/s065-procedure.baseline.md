<!-- Q: How do I add a custom domain to a Vercel project? -->

## Adding a custom domain to a Vercel project

**Via the dashboard**

1. Open your project in the Vercel dashboard and go to **Settings → Domains**.
2. Enter your domain (e.g. `example.com`) and click **Add**.
3. Vercel will suggest adding the `www.` variant too and redirecting one to the other. Pick whichever you prefer as primary.
4. Configure DNS at your registrar or DNS provider (see below).
5. Vercel checks automatically; once the records resolve, the domain shows as valid and an SSL certificate is issued.

**Via the CLI**

```bash
vercel domains add example.com
# or attach to the linked project:
vercel domains add example.com my-project
```

**DNS records**

- **Apex/root domain** (`example.com`): add an `A` record pointing to `76.76.21.21`.
- **Subdomain** (`www.example.com`, `app.example.com`): add a `CNAME` record pointing to `cname.vercel-dns.com`.
- **Alternative:** change your domain's nameservers to Vercel's (`ns1.vercel-dns.com` and `ns2.vercel-dns.com`). This lets Vercel manage all DNS, and is required for wildcard domains.

Vercel's dashboard shows the exact values for your project, and newer projects may be given project-specific records, so use those if they differ from the above.

**Notes**

- DNS propagation can take from a few minutes up to 48 hours.
- If you buy the domain through Vercel, DNS is configured for you.
- To assign a domain to a specific branch or environment (e.g. staging), edit the domain in Settings → Domains and set its Git branch.
- If the domain is already used on another Vercel account, you may need to add a TXT verification record that the dashboard will show you.

If you tell me your registrar, I can give more specific steps.
