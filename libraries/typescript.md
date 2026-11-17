# TypeScript — curated libraries

**Reviewed:** 2026-11-16. Reusable code packages only, never framework or managed service production approvals.

## Dependency choice

- **Standard library first:** native fetch, node:test, Web Crypto and current dependencies.
- **Add:** only for a documented capability that standard library and current dependencies do not sufficiently provide.
- **Keep:** do not migrate merely because a package appears in the catalog or has a newer release.
- **Remove/replace:** prove need, test compatibility and preserve a rollback path.
- **Verify:** target toolchain, platform, license, security advisories, dependency tree and realistic workload.

## Next.js / React capability screening (reviewed 2026-11-16 UTC)

All 20 canonical capabilities were screened for Next.js App Router. **Comparison is not an installation list.** Native or already-suitable packages win unless an actual application requirement proves a gap. React packages are not presumed compatible with Server Components, Edge, static export or every Node/runtime target; test pinned versions and deployment mode. Official upstream docs were reviewed on 2026-11-16 UTC; package release recency, bundled-size and security advisory checks are not pinned workload evidence.

| Capability | Native/existing first | Conditional package choice or exclusion |
|---|---|---|
| C01 | Native semantic HTML/CSS; accessible primitives only for complex interaction | radix-ui for headless UI; @tanstack/react-table for advanced table state; shadcn/ui is copied source/registry, not a normal runtime package |
| C02 | CSS transitions, keyframes and SVG before JS animation | motion for coordinated gestures/layout; recharts for interactive charts; GSAP only for specialized timelines |
| C03 | HTML form/FormData, useActionState, Server Actions, next/link and next/navigation | react-hook-form for complex field state; do not add a router to App Router |
| C04 | Intl, lang attributes, proper semantics and keyboard support | next-intl for real locale routing/translations; no library replaces accessibility testing |
| C05 | useState, useReducer, Context, URL search parameters | zustand for small shared state; Jotai for atoms; Redux Toolkit for structured complex state; no global server store |
| C06 | Server Component fetch, React.cache, Next cache/revalidation | SWR or TanStack Query only for client sync/cache/mutations; never blindly duplicate server state |
| C07 | Existing boundary checks; zod and valibot (EVALUATE only for verified runtime/contract fit) | ArkType considered, not added: overlapping validation choice without specific contract advantage |
| C08 | Direct server-only driver/SQL or existing Kysely; Kysely includes PostgreSQL dialect and built-in Migrator | pg only for PostgreSQL + Kysely PostgresDialect on Node runtime; Edge/serverless pool and migration deployment need project validation; postgres/Postgres.js needs a separate verified Kysely dialect; Drizzle/Prisma not added without distinct schema/tooling ownership |
| C09 | Native fetch/Route Handlers; existing undici for advanced Node HTTP | Axios/ky/GraphQL clients excluded without protocol or interceptor needs |
| C10 | Next server cookies plus authorization-aware DAL and existing session layer | better-auth VERIFIED/EVALUATE for bounded Node + supported DB; authz/CSRF/session app gates remain; next-auth v5 beta not promoted |
| C11 | Server SQL indexes/full-text or local Array.filter | fuse.js only for bounded local fuzzy search, not ACL-sensitive server search |
| C12 | input type=file, FormData, next/image, platform image/file APIs | react-dropzone only for drag-drop UX; server validation mandatory |
| C13 | Route Handlers for request-scoped tasks; host scheduler or durable infrastructure when actually required | No generic queue SDK: background durability/retries are workload and deployment choices |
| C14 | error.tsx, expected errors, AbortSignal and idempotent bounded retries | No new retry/error package without demonstrated needs; never blindly retry mutations |
| C15 | Web Crypto and vetted existing auth/session layer; jose VERIFIED/EVALUATE for bounded Node/algorithms | No token use without key/issuer/audience/revocation and app authorization verification |
| C16 | Next caching, React memoization and measured rendering profiling | @tanstack/react-virtual only for measured large-list rendering bottlenecks |
| C17 | Existing vitest and @playwright/test; node:test as simple fallback | @testing-library/react for DOM interactions; async RSC require E2E coverage |
| C18 | Existing console; pino VERIFIED/EVALUATE for Node-only JSON logging, OTel API+SDK and Next instrumentation | No duplicate APM SDK absent actual incident, tracing or telemetry gap |
| C19 | TypeScript compiler, Next build/lint, established test and formatting workflow | No standalone build/lint package merely to raise catalog count |
| C20 | Existing openai, ai, official MCP client/server and native HTTP | No new provider SDK or MCP abstraction without explicit integration needs |

### Source and selection boundaries

- [Next.js Server and Client Components](https://nextjs.org/docs/app/getting-started/server-and-client-components) and [Fetching Data](https://nextjs.org/docs/app/getting-started/fetching-data): default server ownership and client boundary.
- [Next.js Forms](https://nextjs.org/docs/app/guides/forms), [Authentication](https://nextjs.org/docs/app/guides/authentication), [Testing](https://nextjs.org/docs/app/guides/testing): native and security/test fallbacks.
- [Redux App Router guidance](https://redux.js.org/usage/nextjs), [Zustand Next.js guidance](https://zustand.docs.pmnd.rs/learn/guides/nextjs), [Jotai Next.js guidance](https://jotai.org/docs/guides/nextjs): request isolation and hydration.
- [TanStack Query App Router guidance](https://tanstack.com/query/latest/docs/framework/react/guides/advanced-ssr) and [SWR Next.js guidance](https://swr.vercel.app/docs/with-nextjs): client cache vs server ownership.
- [Radix installation](https://www.radix-ui.com/primitives/docs/overview/introduction), [Motion Next.js instructions](https://motion.dev/docs/react-installation) and [Auth.js status](https://authjs.dev/getting-started/integrations): distributions, client constraints and auth maturity.

Do not treat [shadcn/ui](https://ui.shadcn.com/docs) copied/registry components as an ordinary published runtime dependency. Accessible primitives still need application-level accessibility tests; client fetching needs explicit hydration/invalidation strategy; security-sensitive auth and file uploads always require trusted server checks. Versioned license, advisory, peer dependency, Node/Edge compatibility, bundle cost and support horizon must be checked against the actual app before adoption.

### Next.js C08 driver and migration boundary (2026-11-17)

Kysely is a type-safe query builder, not a required ORM. Its built-in PostgreSQL dialect uses the `pg` driver and its built-in `Migrator` and `FileMigrationProvider` support versioned up/down migrations; a controlled runtime/driver, deployment owner and rollback plan are still required. For a Next.js app using PostgreSQL and Kysely on the Node runtime, `pg` is an optional matching driver, not a mandatory dependency. Keep credentials, tenant ownership checks, SQL parameters and transactions server-side; size and release pools deliberately for serverless hosts and proxies. No Node TCP-driver compatibility with Edge is presumed. `postgres` (Postgres.js) requires a separate Kysely dialect such as `kysely-postgres-js`; Drizzle/Drizzle Kit and Prisma are alternative ORM/migration ownership choices, not missing Kysely migration features. [Kysely driver](https://kysely.dev/docs/getting-started) · [Kysely Migrator](https://kysely.dev/docs/migrations) · [Next.js Edge runtime](https://nextjs.org/docs/app/api-reference/edge) · [node-postgres pooling](https://node-postgres.com/features/pooling).

## Entries

### `zod`
- **Package:** `zod`
- **Capability:** C07 — Data Contracts
- **Language/runtime:** TypeScript / npm
- **Fit:** Parse untrusted runtime data, when the current codebase demonstrably needs it.
- **Anti-fit:** Only compile-time types or already validated boundaries are involved.
- **Fallback:** explicit checks or current validator.
- **Compatibility:** Zod 4.6.7 supports Node.js and modern browsers; TypeScript >=5.5 tested, `strict` required; tagged manifest exports ESM/CJS. Catalog evaluation bounded to Next.js Node-runtime server boundaries and browser Client Components. Exact Edge/bundler target NOT_VERIFIED.
- **Maintenance:** Tagged 4.6.7 package and official requirements rechecked 2026-11-17; no support SLA inferred.
- **License:** MIT
- **Official source:** [official package identity](https://registry.npmjs.org/zod/latest); [official requirements](https://zod.dev/); [tagged manifest](https://github.com/colinhacks/zod/blob/v4.6.7/packages/zod/package.json); [Next Edge restrictions](https://nextjs.org/docs/app/api-reference/edge)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-17
- **Unknowns:** The original global Edge/bundler requirement was too broad for Node/browser eligibility. Validate target Next.js version, server/client boundary, Edge build separately, schema coverage, payload/bundle costs and performance. No full transitive/pinned-version vulnerability clearance; targeted advisory review found no demonstrated blocker for 4.6.7. Existing valibot remains an option.
- **Selection:** EVALUATE

### `valibot`
- **Package:** `valibot`
- **Capability:** C07 — Data Contracts
- **Language/runtime:** TypeScript / npm
- **Fit:** Composable typed validation schemas, when the current codebase demonstrably needs it.
- **Anti-fit:** Existing runtime schemas meet requirements; bundle change alone does not justify migration.
- **Fallback:** explicit checks or current validator.
- **Compatibility:** Node, Bun, Deno; TS >=5.0.2; ES2020 output per official installation docs; check deployment platform and integrations.
- **Maintenance:** npm latest 1.5.0; publish recency UNKNOWN; activity does not prove long-term support.
- **License:** MIT
- **Official source:** [official registry or upstream](https://registry.npmjs.org/valibot/latest); [upstream/manifest](https://github.com/open-circle/valibot); [official compatibility guide](https://valibot.dev/guides/installation/)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-01
- **Unknowns:** Security advisories: UNKNOWN; exact target support, comparative benchmarks and operational burden: NOT_MEASURED. Recheck before project selection.
- **Selection:** EVALUATE

### `undici`
- **Package:** `undici`
- **Capability:** C09 — API & Networking
- **Language/runtime:** TypeScript / npm
- **Fit:** Advanced Node HTTP client and pool, when the current codebase demonstrably needs it.
- **Anti-fit:** Native Node fetch or browser fetch is sufficient.
- **Fallback:** globalThis.fetch.
- **Compatibility:** Node >=22.19.0; check deployment platform and integrations.
- **Maintenance:** npm latest 8.12.3; publish recency UNKNOWN; activity does not prove long-term support.
- **License:** MIT
- **Official source:** [official registry or upstream](https://registry.npmjs.org/undici/latest); [upstream/manifest](https://github.com/nodejs/undici)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-01
- **Unknowns:** npm metadata requires Node >=22.19.0; avoid browser bundle inclusion. Security advisories: UNKNOWN; exact target support, comparative benchmarks and operational burden: NOT_MEASURED. Recheck before project selection.
- **Selection:** EVALUATE

### `pino`
- **Package:** `pino`
- **Capability:** C18 — Observability
- **Language/runtime:** TypeScript / npm
- **Fit:** Structured JSON server logging, when the current codebase demonstrably needs it.
- **Anti-fit:** Browser-only work or an existing structured logger meets needs.
- **Fallback:** console or existing telemetry.
- **Compatibility:** Pino 10.4.0 tagged CI matrix covers Node 20/22/24/25/26, while v10 dropped Node 18. EVALUATE only for maintained Node.js 22/24 server-side JSON logging; Next.js `runtime='nodejs'` only. Worker-thread transports require explicit environment/bundler verification. Edge/Workers NOT_VERIFIED.
- **Maintenance:** Tag v10.4.0 package, Node support policy, transport docs and CI matrix verified 2026-11-17; no generic runtime guarantee.
- **License:** MIT
- **Official source:** [official package identity](https://registry.npmjs.org/pino/latest); [tagged manifest](https://github.com/pinojs/pino/blob/v10.4.0/package.json); [LTS policy](https://github.com/pinojs/pino/blob/v10.4.0/docs/lts.md); [transport worker behavior](https://github.com/pinojs/pino/blob/v10.4.0/docs/transports.md); [tagged CI](https://github.com/pinojs/pino/blob/v10.4.0/.github/workflows/ci.yml)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-17
- **Unknowns:** No need to prove Edge for a Node-only logger. Console is sufficient when structured logging is unnecessary. Check target serverless log flush, graceful shutdown, PII redaction, transport worker bundling, ingestion costs and performance; browser/Edge and third-party transports remain unapproved. No complete dependency security scan.
- **Selection:** EVALUATE

### `vitest`
- **Package:** `vitest`
- **Capability:** C17 — Testing & QA
- **Language/runtime:** TypeScript / npm
- **Fit:** TS/ESM-aware unit tests, when the current codebase demonstrably needs it.
- **Anti-fit:** An established test runner handles current ESM/TS workflow.
- **Fallback:** node:test or current runner.
- **Compatibility:** Node ^22.12.0 || ^24.0.0 || >=26.0.0; check deployment platform and integrations.
- **Maintenance:** npm latest 5.0.5; publish recency UNKNOWN; activity does not prove long-term support.
- **License:** MIT
- **Official source:** [official registry or upstream](https://registry.npmjs.org/vitest/latest); [upstream/manifest](https://github.com/vitest-dev/vitest)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-01
- **Unknowns:** Check compatible Node and bundler versions, not only TypeScript. Security advisories: UNKNOWN; exact target support, comparative benchmarks and operational burden: NOT_MEASURED. Recheck before project selection.
- **Selection:** EVALUATE

### `kysely`
- **Package:** `kysely`
- **Capability:** C08 — Persistence
- **Language/runtime:** TypeScript / npm
- **Fit:** Typed SQL query builder, when the current codebase demonstrably needs it.
- **Anti-fit:** An existing database access layer provides equivalent query safety.
- **Fallback:** existing driver with SQL.
- **Compatibility:** Node >=22.0.0; check deployment platform and integrations.
- **Maintenance:** npm latest 0.29.8; publish recency UNKNOWN; activity does not prove long-term support.
- **License:** MIT
- **Official source:** [official registry or upstream](https://registry.npmjs.org/kysely/latest); [upstream/manifest](https://github.com/kysely-org/kysely)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-01
- **Unknowns:** Security advisories: UNKNOWN; exact target support, comparative benchmarks and operational burden: NOT_MEASURED. Recheck before project selection.
- **Selection:** EVALUATE

### `pg`
- **Package:** `pg`
- **Capability:** C08 — Persistence
- **Language/runtime:** TypeScript / npm; server-side Node.js PostgreSQL client
- **Fit:** Conditional PostgreSQL driver/pool for Kysely's built-in PostgresDialect or direct parameterized SQL on a Next.js Node runtime.
- **Anti-fit:** No PostgreSQL; an existing driver or database API suffices; Edge runtime or browser bundle requires a separately supported alternative.
- **Fallback:** Current PostgreSQL driver, or direct SQL with the already selected database access layer; no ORM migration by default.
- **Compatibility:** npm pg 8.23.1 supports Node.js >=16 in the upstream package manifest; Kysely currently records Node >=22. Built-in Kysely PostgresDialect uses pg Pool. Node TCP-dependent integration is not portable to Next.js Edge by default; ESM/CJS imports and TypeScript @types/pg declarations require target verification.
- **Maintenance:** npm latest 8.23.1; official npm release and upstream node-postgres package manifest reviewed; publishing activity is not a support SLA.
- **License:** MIT
- **Official source:** [npm registry](https://registry.npmjs.org/pg/latest); [upstream package manifest](https://github.com/brianc/node-postgres/blob/master/packages/pg/package.json); [Kysely PostgreSQL driver documentation](https://kysely.dev/docs/getting-started)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-17
- **Unknowns:** Application-level Node/Next deploy target, TLS trust configuration, pooled/serverless connections, transaction client affinity, parameterization, prepared statement behavior through proxies, secrets/tenant ownership enforcement, pinned-version advisories and full dependency graph NOT_VERIFIED; performance and TCO NOT_MEASURED. A driver does not implement authorization. Kysely already provides Migrator; its separately controlled migration deployment and rollback require application testing.
- **Selection:** EVALUATE

### `jose`
- **Package:** `jose`
- **Capability:** C15 — Security & Cryptography
- **Language/runtime:** TypeScript / npm
- **Fit:** JOSE token and key operations, when the current codebase demonstrably needs it.
- **Anti-fit:** Opaque sessions or an existing vetted authentication library cover requirements.
- **Fallback:** existing auth library or Web Crypto.
- **Compatibility:** jose 6.2.15 is zero-dependency tree-shakeable ESM; tagged README lists Node.js, browsers and Cloudflare Workers subject to WebCrypto and algorithm availability. Catalog evaluation limited to Node.js 22/24 with explicit algorithms and ESM imports. CJS require(esm) only where Node ^20.19.0 || ^22.12.0 || >=23.0.0 permits; Next.js Edge target unverified.
- **Maintenance:** Tag v6.2.15 manifest, runtime matrix and changelog fixes rechecked 2026-11-17; baseline not upgraded to 6.2.16.
- **License:** MIT
- **Official source:** [official package identity](https://registry.npmjs.org/jose/latest); [tagged README](https://github.com/panva/jose/blob/v6.2.15/README.md); [tagged manifest](https://github.com/panva/jose/blob/v6.2.15/package.json); [JWT verification options](https://github.com/panva/jose/blob/v6.2.15/docs/jwt/verify/interfaces/JWTVerifyOptions.md); [changelog](https://github.com/panva/jose/blob/main/CHANGELOG.md)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-17
- **Unknowns:** JWT verification is not an authentication/authorization system. Application must specify signing-algorithm allowlist, issuer, audience, expiry, not-before, key selection/rotation, JWKS trust/cache, revocation and authorization checks. Selected runtime crypto/bundle tests required. 6.2.15 includes JWE decompression limit, JWKS negative cache-duration and JWT negative clock-tolerance fixes; full transitive scan and threat model NOT_PERFORMED.
- **Selection:** EVALUATE

### `@opentelemetry/api`
- **Package:** `@opentelemetry/api`
- **Capability:** C18 — Observability
- **Language/runtime:** TypeScript / npm
- **Fit:** Telemetry instrumentation API, when the current codebase demonstrably needs it.
- **Anti-fit:** No instrumentation contract exists, or existing telemetry API suffices.
- **Fallback:** console or existing telemetry.
- **Compatibility:** Node >=8.0.0; check deployment platform and integrations.
- **Maintenance:** npm latest 1.10.0; publish recency UNKNOWN; activity does not prove long-term support.
- **License:** Apache-2.0
- **Official source:** [official registry or upstream](https://registry.npmjs.org/@opentelemetry/api/latest); [upstream/manifest](https://github.com/open-telemetry/opentelemetry-js)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-01
- **Unknowns:** API only supplies instrumentation contracts; use a compatible tracing SDK such as @opentelemetry/sdk-trace and configure exporter/collector separately. Instrumentation API alone does not export spans or metrics. Security advisories: UNKNOWN; exact target support, comparative benchmarks and operational burden: NOT_MEASURED. Recheck before project selection.
- **Selection:** EVALUATE

### `openai`
- **Package:** `openai`
- **Capability:** C20 — AI & Integrations
- **Language/runtime:** TypeScript / npm
- **Fit:** Typed OpenAI model client, when the current codebase demonstrably needs it.
- **Anti-fit:** Existing API client works or calling model APIs is unnecessary.
- **Fallback:** fetch or current SDK.
- **Compatibility:** Node >=22.0.0; check deployment platform and integrations.
- **Maintenance:** npm latest 7.47.0; publish recency UNKNOWN; activity does not prove long-term support.
- **License:** Apache-2.0
- **Official source:** [official registry or upstream](https://registry.npmjs.org/openai/latest); [upstream/manifest](https://github.com/openai/openai-node)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-01
- **Unknowns:** Keep private API keys on trusted servers; never ship secrets to browsers. Security advisories: UNKNOWN; exact target support, comparative benchmarks and operational burden: NOT_MEASURED. Recheck before project selection.
- **Selection:** EVALUATE

### `@modelcontextprotocol/server`
- **Package:** `@modelcontextprotocol/server`
- **Capability:** C20 — AI & Integrations
- **Language/runtime:** TypeScript / npm
- **Fit:** Official v2 MCP server SDK exposing tools, prompts and resources; stdio/HTTP transports, runtime adapters as needed.
- **Anti-fit:** Ordinary REST endpoints or no MCP interoperability.
- **Fallback:** Native HTTP or existing framework routing.
- **Compatibility:** npm v2.4.0 declares Node >=20; upstream documents Bun and Deno; adapter, protocol and TypeScript target must be validated.
- **Maintenance:** npm latest 2.4.0; v2 stable line implements MCP 2026-07-28.
- **License:** Apache-2.0 (npm v2.4.0; legacy v1 contributions have different licensing history).
- **Official source:** [official registry or upstream](https://registry.npmjs.org/@modelcontextprotocol/server/latest); [upstream/manifest](https://github.com/modelcontextprotocol/typescript-sdk)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-02
- **Unknowns:** For new integrations, prefer v2; monolithic @modelcontextprotocol/sdk v1 still receives bug/security fixes during the upstream migration window. Authorization, origin/host checks, SSRF, untrusted tool outputs, credential handling, body limits and cancellation remain app responsibilities. Security advisory applicability: UNKNOWN (no pinned-version OSV/GHSA review); target-specific integration, performance and TCO: NOT_MEASURED. Recheck official metadata and transitive dependencies before project adoption.
- **Selection:** EVALUATE

### `@modelcontextprotocol/client`
- **Package:** `@modelcontextprotocol/client`
- **Capability:** C20 — AI & Integrations
- **Language/runtime:** TypeScript / npm
- **Fit:** Official v2 MCP client SDK for tool/resource operations and stdio/HTTP server connectivity.
- **Anti-fit:** Only hosted model API or ordinary HTTP services without MCP.
- **Fallback:** fetch or existing model service SDK.
- **Compatibility:** npm v2.4.0 declares Node >=20; upstream documents Bun/Deno; check transport, auth and target bundler.
- **Maintenance:** npm latest 2.4.0; stable v2 supports MCP 2026-07-28 with migration from v1.
- **License:** Apache-2.0 (npm v2.4.0).
- **Official source:** [official registry or upstream](https://registry.npmjs.org/@modelcontextprotocol/client/latest); [upstream/manifest](https://github.com/modelcontextprotocol/typescript-sdk)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-02
- **Unknowns:** Do not trust server-discovered tool descriptions/outputs. Enforce user/tool permissions, OAuth boundaries, URL safety and cancellation; negotiation with older protocol versions requires tests. Security advisory applicability: UNKNOWN (no pinned-version OSV/GHSA review); target-specific integration, performance and TCO: NOT_MEASURED. Recheck official metadata and transitive dependencies before project adoption.
- **Selection:** EVALUATE

### `@playwright/test`
- **Package:** `@playwright/test`
- **Capability:** C17 — Testing & QA
- **Language/runtime:** TypeScript / npm
- **Fit:** Browser-driven cross-browser E2E and UI regression tests for real interactive applications.
- **Anti-fit:** Unit-only services, library code or static checks without browser behavior.
- **Fallback:** vitest, node:test or existing browser E2E runner.
- **Compatibility:** npm 1.64.1 declares Node >=20; browser binaries, CI platform and supported browser matrix require target review.
- **Maintenance:** npm latest 1.64.1; upstream maintained browser automation/testing.
- **License:** Apache-2.0
- **Official source:** [official registry or upstream](https://registry.npmjs.org/@playwright/test/latest); [upstream/manifest](https://github.com/microsoft/playwright)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-02
- **Unknowns:** Browser artifacts and CI time add operational cost; use accessible selectors and deterministic test fixtures; benchmarks NOT_MEASURED. Security advisory applicability: UNKNOWN (no pinned-version OSV/GHSA review); target-specific integration, performance and TCO: NOT_MEASURED. Recheck official metadata and transitive dependencies before project adoption.
- **Selection:** EVALUATE

### `@opentelemetry/sdk-trace`
- **Package:** `@opentelemetry/sdk-trace`
- **Capability:** C18 — Observability
- **Language/runtime:** TypeScript / npm
- **Fit:** Create/process trace spans, complementary to @opentelemetry/api; export requires a span exporter configured separately.
- **Anti-fit:** No distributed tracing requirement or existing telemetry SDK is sufficient.
- **Fallback:** @opentelemetry/api no-op instrumentation or existing provider.
- **Compatibility:** npm 3.0.0 declares Node >=22.15.0; bundler must support exports/imports conditions and OTel API compatibility.
- **Maintenance:** npm latest 3.0.0; October 2026 OTel JS 3.x migration supersedes sdk-trace-base/node/web.
- **License:** Apache-2.0
- **Official source:** [official registry or upstream](https://registry.npmjs.org/@opentelemetry/sdk-trace/latest); [upstream/manifest](https://github.com/open-telemetry/opentelemetry-js)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-02
- **Unknowns:** SDK != exporter != collector; 3.x migrates away from sdk-trace-base, sdk-trace-node and sdk-trace-web. Check propagation, sampling and redaction. Security advisory applicability: UNKNOWN (no pinned-version OSV/GHSA review); target-specific integration, performance and TCO: NOT_MEASURED. Recheck official metadata and transitive dependencies before project adoption.
- **Selection:** EVALUATE

### `ai`
- **Package:** `ai`
- **Capability:** C20 — AI & Integrations
- **Language/runtime:** TypeScript / npm
- **Fit:** Typed model integration, streaming and provider abstraction when several providers/use cases warrant it.
- **Anti-fit:** One provider with an existing official SDK or simple HTTP calls; migration adds unnecessary abstraction.
- **Fallback:** openai SDK or fetch and current provider client.
- **Compatibility:** npm 7.0.159 declares Node >=22; provider adapters, edge runtimes and streaming behaviors vary.
- **Maintenance:** npm latest 7.0.159; upstream Vercel AI SDK maintained.
- **License:** Apache-2.0
- **Official source:** [official registry or upstream](https://registry.npmjs.org/ai/latest); [upstream/manifest](https://github.com/vercel/ai)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-02
- **Unknowns:** Cross-provider APIs do not guarantee equivalent tools, structured output, token accounting, safety, cost, latency or error contracts. Security advisory applicability: UNKNOWN (no pinned-version OSV/GHSA review); target-specific integration, performance and TCO: NOT_MEASURED. Recheck official metadata and transitive dependencies before project adoption.
- **Selection:** EVALUATE

### `radix-ui`
- **Package:** `radix-ui`
- **Capability:** C01 — UI & Design System
- **Language/runtime:** TypeScript / npm
- **Fit:** Accessible unstyled interaction primitives (dialogs, menus, tooltips) when native HTML lacks the needed interaction semantics.
- **Anti-fit:** Simple static markup or an existing accessible component system; it does not supply an entire styled design system.
- **Fallback:** Semantic HTML, native dialog and current UI components.
- **Compatibility:** React UI primitives; interactive parts belong behind a Next.js Client Component boundary; server-only rendering is not a universal substitute.
- **Maintenance:** npm latest 1.8.1; official npm dist-tags.latest and /latest package metadata verified 2026-11-17 UTC; upstream project and integration docs inspected 2026-11-16 UTC; npm publication timestamp not verified.
- **License:** MIT
- **Official source:** [npm package identity](https://registry.npmjs.org/radix-ui/latest); [upstream](https://github.com/radix-ui/primitives); [official integration/usage](https://www.radix-ui.com/primitives/docs/overview/introduction)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-16
- **Unknowns:** Official docs recommend the tree-shakeable radix-ui distribution; individually published @radix-ui/react-* packages are separate optional choices. Accessibility still needs application-level keyboard and screen-reader testing. Pinned-version security advisory exposure: UNKNOWN; target bundle/runtime tests and performance: NOT_MEASURED.
- **Selection:** EVALUATE

### `@tanstack/react-table`
- **Package:** `@tanstack/react-table`
- **Capability:** C01 — UI & Design System
- **Language/runtime:** TypeScript / npm
- **Fit:** Headless interactive tables with multiple sorting, filtering, pagination and selection concerns.
- **Anti-fit:** Static HTML tables and simple server-paginated lists; table logic increases client complexity.
- **Fallback:** Native table markup and server-side query/pagination.
- **Compatibility:** npm 9.3.1 declares Node >=20 and React >=18; React adapter for client tables; v9 is not assumed API-compatible with v8; verify SSR hydration.
- **Maintenance:** npm latest 9.3.1; official npm dist-tags.latest and /latest package metadata verified 2026-11-17 UTC; upstream project and integration docs inspected 2026-11-16 UTC; npm publication timestamp not verified.
- **License:** MIT
- **Official source:** [npm package identity](https://registry.npmjs.org/@tanstack/react-table/latest); [upstream](https://github.com/TanStack/table); [official integration/usage](https://tanstack.com/table/latest/docs/framework/react/guide/table-state)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-16
- **Unknowns:** Headless state engine, not styled components or a database search/index. Large row counts may separately justify virtualization; avoid shipping all rows to the browser. Pinned-version security advisory exposure: UNKNOWN; target bundle/runtime tests and performance: NOT_MEASURED.
- **Selection:** EVALUATE

### `motion`
- **Package:** `motion`
- **Capability:** C02 — Animation & Visualization
- **Language/runtime:** TypeScript / npm
- **Fit:** React gesture, layout and coordinated animations beyond isolated CSS transitions.
- **Anti-fit:** Simple hover/fade/color effects, reduced-motion requirements or animations already covered by CSS.
- **Fallback:** CSS transitions/keyframes and Web Animations API.
- **Compatibility:** Official Motion React guide requires React >=18.2; Next.js App Router uses a client boundary or the documented motion/react-client entrypoint.
- **Maintenance:** npm latest 14.14.0; official npm dist-tags.latest and /latest package metadata verified 2026-11-17 UTC; upstream project and integration docs inspected 2026-11-16 UTC; npm publication timestamp not verified.
- **License:** MIT
- **Official source:** [npm package identity](https://registry.npmjs.org/motion/latest); [upstream](https://github.com/motiondivision/motion); [official integration/usage](https://motion.dev/docs/react-installation)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-16
- **Unknowns:** Account for prefers-reduced-motion, client JS and hydration; no unmeasured frame-rate or bundle improvement claims. Pinned-version security advisory exposure: UNKNOWN; target bundle/runtime tests and performance: NOT_MEASURED.
- **Selection:** EVALUATE

### `recharts`
- **Package:** `recharts`
- **Capability:** C02 — Animation & Visualization
- **Language/runtime:** TypeScript / npm
- **Fit:** Composable interactive React charts for dashboards whose requirements exceed a small static SVG.
- **Anti-fit:** Static reports, tiny sparklines and server-rendered SVG where client interaction adds no value.
- **Fallback:** Native SVG/HTML and existing visualization components.
- **Compatibility:** React chart components use client-side interactivity; upstream installation documents react-is matching the installed React version; test Next SSR and hydration.
- **Maintenance:** npm latest 3.10.1; official npm dist-tags.latest and /latest package metadata verified 2026-11-17 UTC; upstream project and integration docs inspected 2026-11-16 UTC; npm publication timestamp not verified.
- **License:** MIT
- **Official source:** [npm package identity](https://registry.npmjs.org/recharts/latest); [upstream](https://github.com/recharts/recharts); [official integration/usage](https://recharts.github.io/en-US/guide/)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-16
- **Unknowns:** Chart accessibility, data integrity, responsive sizing and chart rendering costs remain project-specific; no RSC/Edge execution guarantee. Pinned-version security advisory exposure: UNKNOWN; target bundle/runtime tests and performance: NOT_MEASURED.
- **Selection:** EVALUATE

### `react-hook-form`
- **Package:** `react-hook-form`
- **Capability:** C03 — Forms & Navigation
- **Language/runtime:** TypeScript / npm
- **Fit:** Complex interactive forms needing field state, dirty tracking, validation and controlled-component adapters.
- **Anti-fit:** Small forms handled well by native HTML validation plus React/Next Server Actions; does not provide routing.
- **Fallback:** Native form/FormData, useActionState and existing field handlers.
- **Compatibility:** React hooks operate in Client Components; Server Actions can receive submissions but server-side validation and authorization remain required.
- **Maintenance:** npm latest 7.92.0; official npm dist-tags.latest and /latest package metadata verified 2026-11-17 UTC; upstream project and integration docs inspected 2026-11-16 UTC; npm publication timestamp not verified; prerelease 8.0.0-beta.0 excluded.
- **License:** MIT
- **Official source:** [npm package identity](https://registry.npmjs.org/react-hook-form/latest); [upstream](https://github.com/react-hook-form/react-hook-form); [official integration/usage](https://react-hook-form.com/get-started)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-16
- **Unknowns:** Form schema resolvers and controlled UI components are separate optional integrations; duplicate schema systems are not required. Pinned-version security advisory exposure: UNKNOWN; target bundle/runtime tests and performance: NOT_MEASURED.
- **Selection:** EVALUATE

### `next-intl`
- **Package:** `next-intl`
- **Capability:** C04 — Accessibility & i18n
- **Language/runtime:** TypeScript / npm
- **Fit:** Multi-locale Next.js apps requiring locale-aware translations, formatting and routing.
- **Anti-fit:** Single-locale apps or built-in Intl plus small dictionaries already covering needs.
- **Fallback:** Intl, semantic HTML, lang attributes and native Next.js routing.
- **Compatibility:** Official App Router integration covers Server and Client Components; locale request configuration and routing must match deployment mode.
- **Maintenance:** npm latest 4.15.1; official npm dist-tags.latest and /latest package metadata verified 2026-11-17 UTC; upstream project and integration docs inspected 2026-11-16 UTC; npm publication timestamp not verified.
- **License:** MIT
- **Official source:** [npm package identity](https://registry.npmjs.org/next-intl/latest); [upstream](https://github.com/amannn/next-intl); [official integration/usage](https://next-intl.dev/docs/getting-started/app-router)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-16
- **Unknowns:** Internationalization is not automatic accessibility, translation review or content governance; Edge compatibility requires target build checks. Pinned-version security advisory exposure: UNKNOWN; target bundle/runtime tests and performance: NOT_MEASURED.
- **Selection:** EVALUATE

### `zustand`
- **Package:** `zustand`
- **Capability:** C05 — State Management
- **Language/runtime:** TypeScript / npm
- **Fit:** Shared mutable client UI state across several interactive components with small store APIs.
- **Anti-fit:** State local to one component, URL state, server-fetched data or context/useReducer sufficient.
- **Fallback:** useState, useReducer, React Context and searchParams.
- **Compatibility:** Official Next.js guide requires per-request store creation and stable SSR hydration; React Server Components must not read/write the mutable store.
- **Maintenance:** npm latest 5.1.0; official npm dist-tags.latest and /latest package metadata verified 2026-11-17 UTC; upstream project and integration docs inspected 2026-11-16 UTC; npm publication timestamp not verified.
- **License:** MIT
- **Official source:** [npm package identity](https://registry.npmjs.org/zustand/latest); [upstream](https://github.com/pmndrs/zustand); [official integration/usage](https://zustand.docs.pmnd.rs/learn/guides/nextjs)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-16
- **Unknowns:** Never export a singleton server store holding request/user data; persist middleware and browser storage need SSR guards. Pinned-version security advisory exposure: UNKNOWN; target bundle/runtime tests and performance: NOT_MEASURED.
- **Selection:** EVALUATE

### `@reduxjs/toolkit`
- **Package:** `@reduxjs/toolkit`
- **Capability:** C05 — State Management
- **Language/runtime:** TypeScript / npm
- **Fit:** Complex globally shared mutable client state that benefits from Redux conventions, slices, middleware and debugging.
- **Anti-fit:** Small isolated UI state, data already owned by the server, or projects not needing centralized Redux policies.
- **Fallback:** React context/reducer, Zustand or existing state solution.
- **Compatibility:** Official Redux Next.js App Router guide requires per-request store factory and Client Component Provider; React binding also needs react-redux.
- **Maintenance:** npm latest 2.14.0; official npm dist-tags.latest and /latest package metadata verified 2026-11-17 UTC; upstream project and integration docs inspected 2026-11-16 UTC; npm publication timestamp not verified.
- **License:** MIT
- **Official source:** [npm package identity](https://registry.npmjs.org/@reduxjs/toolkit/latest); [upstream](https://github.com/reduxjs/redux-toolkit); [official integration/usage](https://redux.js.org/usage/nextjs)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-16
- **Unknowns:** Never read/write Redux from RSC; avoid a module-global store and reset route-specific state on navigation where necessary. Pinned-version security advisory exposure: UNKNOWN; target bundle/runtime tests and performance: NOT_MEASURED.
- **Selection:** EVALUATE

### `jotai`
- **Package:** `jotai`
- **Capability:** C05 — State Management
- **Language/runtime:** TypeScript / npm
- **Fit:** Fine-grained shared client state composed from independent atoms and derived relationships.
- **Anti-fit:** A few isolated useState values or an existing store that covers the application.
- **Fallback:** useState/useReducer and existing Zustand/Redux if already deployed.
- **Compatibility:** npm 3.0.2 requires Node >=22.12 and React >=18; official Next.js guide requires per-request Provider and explicit hydration for server-provided atom state.
- **Maintenance:** npm latest 3.0.2; official npm dist-tags.latest and /latest package metadata verified 2026-11-17 UTC; upstream project and integration docs inspected 2026-11-16 UTC; npm publication timestamp not verified.
- **License:** MIT
- **Official source:** [npm package identity](https://registry.npmjs.org/jotai/latest); [upstream](https://github.com/pmndrs/jotai); [official integration/usage](https://jotai.org/docs/guides/nextjs)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-16
- **Unknowns:** Avoid provider-less global stores during SSR; storage atoms need browser guards to prevent hydration mismatches. Pinned-version security advisory exposure: UNKNOWN; target bundle/runtime tests and performance: NOT_MEASURED.
- **Selection:** EVALUATE

### `@tanstack/react-query`
- **Package:** `@tanstack/react-query`
- **Capability:** C06 — Remote Data & Sync
- **Language/runtime:** TypeScript / npm
- **Fit:** Interactive client data with mutation state, invalidation, retries and multiple cached query lifecycles.
- **Anti-fit:** Server Components plus native fetch already satisfy the feature or client cache is not needed.
- **Fallback:** Server-side fetch, React.cache, Next revalidation and minimal client fetch.
- **Compatibility:** Official Next.js App Router guide uses a Client Component QueryClientProvider and per-request server QueryClient for hydration.
- **Maintenance:** npm latest 5.107.1; official npm dist-tags.latest and /latest package metadata verified 2026-11-17 UTC; upstream project and integration docs inspected 2026-11-16 UTC; npm publication timestamp not verified.
- **License:** MIT
- **Official source:** [npm package identity](https://registry.npmjs.org/@tanstack/react-query/latest); [upstream](https://github.com/TanStack/query); [official integration/usage](https://tanstack.com/query/latest/docs/framework/react/guides/advanced-ssr)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-16
- **Unknowns:** Do not use Server Actions as client queryFn; manage client/server data ownership and avoid hydration leaks or cache divergence. Pinned-version security advisory exposure: UNKNOWN; target bundle/runtime tests and performance: NOT_MEASURED.
- **Selection:** EVALUATE

### `swr`
- **Package:** `swr`
- **Capability:** C06 — Remote Data & Sync
- **Language/runtime:** TypeScript / npm
- **Fit:** Lightweight browser revalidation and deduplicated fetching for frequently changing client views.
- **Anti-fit:** Server-only data fetching or a project already standardizing on TanStack Query.
- **Fallback:** Native fetch with Next cache/revalidation or existing client cache.
- **Compatibility:** SWR hooks are Client Component APIs; RSC may use documented SWRConfig/serialization/preload APIs, not useSWR hooks.
- **Maintenance:** npm latest 2.5.1; official npm dist-tags.latest and /latest package metadata verified 2026-11-17 UTC; upstream project and integration docs inspected 2026-11-16 UTC; npm publication timestamp not verified; prerelease 2.6.0-beta.0 excluded.
- **License:** MIT
- **Official source:** [npm package identity](https://registry.npmjs.org/swr/latest); [upstream](https://github.com/vercel/swr); [official integration/usage](https://swr.vercel.app/docs/with-nextjs)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-16
- **Unknowns:** Docs flag cacheData/preload server-prefetch integration as experimental in relevant versions; test exact release and streaming semantics. Pinned-version security advisory exposure: UNKNOWN; target bundle/runtime tests and performance: NOT_MEASURED.
- **Selection:** EVALUATE

### `better-auth`
- **Package:** `better-auth`
- **Capability:** C10 — Identity & Authorization
- **Language/runtime:** TypeScript / npm
- **Fit:** Self-managed credential/OAuth/session flows when an established app session layer is insufficient.
- **Anti-fit:** Guest-only apps, an existing tested identity solution or a simple provider integration already meeting policy.
- **Fallback:** Next.js server-side session/DAL pattern or the current authentication system.
- **Compatibility:** Official Next.js App Router Route Handler/RSC/server-action integration, including Next.js 16 Node.js Proxy guidance; supported database choices include built-in SQLite/PostgreSQL/MySQL and documented adapters. Scope to an explicit Node-runtime + supported database configuration; Edge middleware/community adapters NOT_PREAPPROVED. Cookie-presence checks are not session authentication.
- **Maintenance:** Stable tagged 1.7.25 package verified 2026-11-17; official November 3 security release fixed 12 issues in 1.7.16. Installed Better Auth core, plugins and adapters must be version-aligned and rechecked.
- **License:** MIT
- **Official source:** [official package identity](https://registry.npmjs.org/better-auth/latest); [Next.js integration](https://better-auth.com/docs/integrations/next); [database](https://better-auth.com/docs/concepts/database); [security/CSRF](https://better-auth.com/docs/reference/security); [2026-11-03 security fixes](https://better-auth.com/blog/security-release-2026-11-03); [tagged manifest](https://github.com/better-auth/better-auth/blob/v1.7.25/packages/better-auth/package.json)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-17
- **Unknowns:** Known GHSA-965c-763c-88jm fixed in 1.7.7 and November 3 core/plugin advisories fixed in 1.7.16 precede catalog baseline 1.7.25, not proof of complete security clearance. Application gates: pinned plugin/adapter advisories and full graph, DB migrations/ownership, secure/SameSite cookies, trusted origins, CSRF, OAuth state/redirects, secret rotation, session expiry/revocation, proxy constraints and server-side authorization. Custom `auth.api` routes bypass handler-level CSRF/origin checks; validate origin independently. No Edge or production approval.
- **Selection:** EVALUATE

### `fuse.js`
- **Package:** `fuse.js`
- **Capability:** C11 — Search & Indexing
- **Language/runtime:** TypeScript / npm
- **Fit:** Local fuzzy search over bounded in-memory lists or small preloaded catalogs.
- **Anti-fit:** Large datasets, private server indexes, ACL-filtered search or relevance requirements beyond client-side fuzzy matching.
- **Fallback:** Array filtering for simple match; server database search/index for real datasets.
- **Compatibility:** JavaScript in browser/Node; if loaded in Client Components the search corpus enters the browser bundle or network payload.
- **Maintenance:** npm latest 7.5.0; official npm dist-tags.latest and /latest package metadata verified 2026-11-17 UTC; upstream project and integration docs inspected 2026-11-16 UTC; npm publication timestamp not verified; prerelease 7.6.0-beta.0 excluded.
- **License:** Apache-2.0
- **Official source:** [npm package identity](https://registry.npmjs.org/fuse.js/latest); [upstream](https://github.com/krisk/Fuse); [official integration/usage](https://www.fusejs.io/fuzzy-search.html)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-16
- **Unknowns:** Not a hosted or persistent index; avoid loading secret records into a client-side corpus. Test corpus size and relevance with actual queries. Pinned-version security advisory exposure: UNKNOWN; target bundle/runtime tests and performance: NOT_MEASURED.
- **Selection:** EVALUATE

### `react-dropzone`
- **Package:** `react-dropzone`
- **Capability:** C12 — Media & Files
- **Language/runtime:** TypeScript / npm
- **Fit:** Drag/drop and paste UX for file selection beyond a native input.
- **Anti-fit:** Ordinary file upload controls; it does not upload files, virus-scan or enforce server-side policy.
- **Fallback:** Native input type=file, FormData and server upload handling.
- **Compatibility:** npm 20.2.0 requires Node >=22 and React >=18; browser File/drag-drop APIs require Client Components.
- **Maintenance:** npm latest 20.2.0; official npm dist-tags.latest and /latest package metadata verified 2026-11-17 UTC; upstream project and integration docs inspected 2026-11-16 UTC; npm publication timestamp not verified.
- **License:** MIT
- **Official source:** [npm package identity](https://registry.npmjs.org/react-dropzone/latest); [upstream](https://github.com/react-dropzone/react-dropzone); [official integration/usage](https://react-dropzone.org/guide/getting-started/)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-16
- **Unknowns:** Server must verify MIME, extension, size, authorization and storage safety; client accept filters are not trust boundaries. Pinned-version security advisory exposure: UNKNOWN; target bundle/runtime tests and performance: NOT_MEASURED.
- **Selection:** EVALUATE

### `@tanstack/react-virtual`
- **Package:** `@tanstack/react-virtual`
- **Capability:** C16 — Performance & Cache
- **Language/runtime:** TypeScript / npm
- **Fit:** Virtualized very large interactive lists/grids when measured DOM rendering overhead warrants it.
- **Anti-fit:** Ordinary short lists or server pagination already yielding an acceptable UI.
- **Fallback:** Server pagination, progressive rendering and normal DOM lists.
- **Compatibility:** React hook measures browser scroll/element state; use inside interactive Client Components and verify SSR/hydration sizing.
- **Maintenance:** npm latest 3.14.26; official npm dist-tags.latest and /latest package metadata verified 2026-11-17 UTC; upstream project and integration docs inspected 2026-11-16 UTC; npm publication timestamp not verified.
- **License:** MIT
- **Official source:** [npm package identity](https://registry.npmjs.org/@tanstack/react-virtual/latest); [upstream](https://github.com/TanStack/virtual); [official integration/usage](https://tanstack.com/virtual/latest/docs/framework/react/react-virtual)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-16
- **Unknowns:** Virtualization is a rendering technique, not a Next.js data cache; test accessibility and scroll restoration. Pinned-version security advisory exposure: UNKNOWN; target bundle/runtime tests and performance: NOT_MEASURED.
- **Selection:** EVALUATE

### `@testing-library/react`
- **Package:** `@testing-library/react`
- **Capability:** C17 — Testing & QA
- **Language/runtime:** TypeScript / npm
- **Fit:** Interaction-oriented React DOM component tests together with an existing runner.
- **Anti-fit:** Pure business logic without DOM or async RSC tests needing browser-level evidence.
- **Fallback:** Existing test runner and Playwright E2E for interactive flows.
- **Compatibility:** Development-time React DOM tests; official docs require peer @testing-library/dom and appropriate DOM test environment.
- **Maintenance:** npm latest 16.3.3; official npm dist-tags.latest and /latest package metadata verified 2026-11-17 UTC; upstream project and integration docs inspected 2026-11-16 UTC; npm publication timestamp not verified.
- **License:** MIT
- **Official source:** [npm package identity](https://registry.npmjs.org/@testing-library/react/latest); [upstream](https://github.com/testing-library/react-testing-library); [official integration/usage](https://testing-library.com/docs/react-testing-library/intro/)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-16
- **Unknowns:** Not a runner or an async Server Component compatibility guarantee; Next.js directs E2E coverage for async RSC. Pinned-version security advisory exposure: UNKNOWN; target bundle/runtime tests and performance: NOT_MEASURED.
- **Selection:** EVALUATE

## Selection boundary

VERIFIED is scoped to official package identity, metadata and advertised function; it is NOT a security endorsement, benchmark result or production approval. PARTIAL means essential metadata is unresolved. EVALUATE permits comparison only, BLOCKED requires filling compatibility/license gaps first. No automatic migration.

[Index](README.md) · [Languages](../languages/README.md) · [Frameworks](../frameworks/README.md) · [Decisions](../decisions/README.md)
