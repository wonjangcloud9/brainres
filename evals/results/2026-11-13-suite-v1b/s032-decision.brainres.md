<!-- Q: Monorepo or polyrepo for 3 services and 4 developers? -->

Monorepo. With 4 developers and 3 services, one repo gives you atomic cross-service changes, a single CI config, and shared code without publishing packages, while polyrepo's main benefits (independent team ownership, separate access control, isolated deploy pipelines) only pay off with more teams than you have.

**Why polyrepo costs more at your size:**
- A change touching a shared type or API contract across services needs 2-3 PRs, merged in the right order.
- Shared libraries need versioning and publishing, or they get copy-pasted and drift.
- Three CI/CD setups, three dependency-update streams, three sets of repo settings.

**What the monorepo costs you:**
- CI must run only what changed (path filters, or a tool like Nx, Turborepo, or Bazel if you outgrow filters). Without that, every push builds all three services.
- Each service still needs its own deploy job, so deploys stay independent even though the code lives together.

**When I'd pick polyrepo instead:**
- The services use different languages with no shared code.
- One service needs restricted access (contractors, compliance).
- A service will soon be owned by a separate team.

If none of those apply, start with a monorepo using `services/<name>/` plus a `packages/` folder for shared code. Splitting a repo later with `git filter-repo` is easier than merging three histories.

Next step: tell me the languages and whether the services share code, and I can sketch the directory layout and CI path filters.
