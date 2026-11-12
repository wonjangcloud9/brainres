<!-- Q: Should I use REST or GraphQL for a small internal API used by one frontend? -->

For a small internal API used by one frontend, **use REST** unless you have a specific reason not to.

**Why REST fits here:**
- **Less setup.** No schema definition, resolver layer, or codegen step. You can ship endpoints quickly.
- **Simpler caching and debugging.** Plain HTTP GETs work with browser caching, logs, and tools like curl without extra tooling.
- **GraphQL's main benefit is mostly moot.** It shines when many clients with different data needs share one API, or when over-fetching is a real problem. With one frontend you control both sides, so you can shape endpoints to match its screens.
- **Fewer moving parts.** No N+1 query issues to guard against with DataLoader, no query-depth or complexity limits to configure.

**Consider GraphQL if:**
- The frontend has many views with deeply nested, varied data needs, and you're spending a lot of time adding one-off endpoints.
- You want strong typing and autocomplete across the stack and are willing to invest in tooling (e.g., Apollo, urql, codegen).
- You expect more clients (mobile app, other internal tools) soon.

**A practical middle ground:** if you are on TypeScript, consider tRPC. It gives you end-to-end type safety with the simplicity of RPC-style endpoints and no separate schema language, which suits a single-frontend internal tool well.

If you tell me the stack (language, framework, frontend) and roughly how many screens and entities you have, I can give a more specific recommendation.
