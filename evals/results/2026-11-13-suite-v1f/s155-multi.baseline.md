<!-- Q: What's Kubernetes, do I need it for a 2-person startup, and if not, what should I use? -->

**What Kubernetes is:** An open-source system (originally from Google) that runs and manages containers across a cluster of machines. You describe what you want ("run 3 copies of this app, expose it on port 80, restart if it crashes"), and Kubernetes makes it happen: scheduling, scaling, rolling deploys, self-healing, service discovery, and config/secrets management.

**Do you need it as a 2-person startup?** Almost certainly not. It solves problems you don't have yet:

- Running dozens of services across many machines
- Large teams needing standardized deployment
- Complex autoscaling or multi-region needs

The cost is real: a steep learning curve, lots of YAML, networking and debugging complexity, and ongoing cluster maintenance (or a hefty managed-service bill). With two people, that time is better spent on your product.

**What to use instead (pick by your situation):**

1. **PaaS (my default recommendation):** Render, Railway, Fly.io, Heroku, or Vercel (for frontend/Next.js). Push code, get a running app with a database, TLS, and logs. Minimal ops work.
2. **Serverless/managed containers:** Google Cloud Run, AWS App Runner, or AWS ECS Fargate. Give them a container image, they run and scale it. You get cloud-provider flexibility without managing a cluster.
3. **A single VPS with Docker Compose:** Hetzner, DigitalOcean, or similar, plus something like Kamal, Coolify, or Dokploy for deploys. Cheapest option, and surprisingly capable for a long time. You own more of the maintenance (updates, backups).

**Practical advice:**

- Use a **managed database** (Postgres on Neon, Supabase, RDS, etc.) regardless of the compute choice. Don't self-host your database early on.
- **Containerize with Docker** anyway. It keeps you portable, so moving to Kubernetes later is feasible if you ever need it.
- Set up **CI/CD** (GitHub Actions) and basic monitoring/error tracking (Sentry, uptime checks).

**When to reconsider Kubernetes:** when you have many services, a dedicated infra/platform person, specific scaling or compliance needs, or you're hitting real limits on a PaaS (cost or flexibility). That's typically well past the 2-person stage.

If you tell me your stack (language/framework, database, expected traffic), I can recommend a specific setup.
