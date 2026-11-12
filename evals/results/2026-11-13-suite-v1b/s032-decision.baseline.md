<!-- Q: Monorepo or polyrepo for 3 services and 4 developers? -->

**Monorepo.**

With 3 services and 4 developers, the coordination cost of polyrepo outweighs its benefits:

- **Atomic changes:** a change that touches an API and its consumers lands in one PR, one review, one deploy. In polyrepo you'd juggle versioned releases across repos.
- **Shared code is trivial:** types, utilities, and config live in a shared directory instead of becoming a published package with its own release cycle.
- **Less overhead:** one CI setup, one set of lint/format rules, one dependency-update process, one place to search.
- **Easy onboarding:** one clone, one setup script.

Polyrepo's main advantages don't apply at your size:

- Independent team ownership and access control: you have one small team.
- Independent release cadence: you can get this in a monorepo with path-filtered CI and per-service deploys.
- Build scaling: monorepo tooling pain only shows up with dozens of services or hundreds of developers.

**Practical setup:**
- Top-level layout like `services/a`, `services/b`, `services/c`, plus `packages/shared`.
- Path-filtered CI so only changed services build and deploy.
- CODEOWNERS if you want soft ownership boundaries.
- Skip heavy tooling (Bazel, Nx) until builds actually hurt; your language's native workspaces (npm/pnpm workspaces, Go modules, Cargo workspaces, uv) are enough.

**When I'd reconsider:** the services are in different languages with no shared code and different deploy targets, a service needs strict access isolation (compliance, contractors), or one service is being open-sourced. Otherwise, start with a monorepo. Splitting later is much easier than merging.
