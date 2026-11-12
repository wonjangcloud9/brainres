<!-- Q: What's Kubernetes, do I need it for a 2-person startup, and if not, what should I use? -->

No, a 2-person startup almost certainly doesn't need Kubernetes; start on a managed platform such as Render, Fly.io, or Railway.

**What it is:** Kubernetes (K8s) is software that runs containers (packaged apps) across a cluster of servers. It restarts crashed containers, scales them up and down, and rolls out updates without downtime. Google-style infrastructure teams built it for many services run by many engineers.

**Why it's wrong for you now:** The cluster itself becomes a system you must learn, secure, upgrade, and debug. With two people, that time comes straight out of building the product. Managed versions (EKS, GKE) remove some of the work, but you still deal with YAML, networking, and tooling. Your bottleneck is finding customers, not orchestrating 50 services.

**What to use instead:**

| Option | Fits when | Examples |
|---|---|---|
| PaaS | Web app + database, zero ops wanted | Render, Railway, Fly.io, Heroku |
| Frontend/serverless | Next.js or mostly static site + APIs | Vercel, Netlify, Cloudflare |
| Managed containers | You use Docker and live on AWS/GCP | Google Cloud Run, AWS App Runner, ECS Fargate |
| Single VPS | Cheapest, you're comfortable with Linux | Hetzner + Docker Compose (or Coolify) |

My recommendation is a PaaS plus a managed Postgres database. Put your app in a Dockerfile so you can move later without a rewrite.

**When to revisit:** you run many services (around 10+), you hire someone for infrastructure, you need multi-region or custom scheduling, or your platform bill exceeds an engineer's cost. Those thresholds are rules of thumb, not measured, so treat them as prompts to reassess.

Next step: tell me your stack (language, database, expected traffic) and I'll pick one platform and sketch the deploy.
