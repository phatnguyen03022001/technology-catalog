# TypeScript — curated libraries

**Reviewed:** 2026-11-01. Reusable code packages only, never framework or managed service production approvals.

## Dependency choice

- **Standard library first:** native fetch, node:test, Web Crypto and current dependencies.
- **Add:** only for a documented capability that standard library and current dependencies do not sufficiently provide.
- **Keep:** do not migrate merely because a package appears in the catalog or has a newer release.
- **Remove/replace:** prove need, test compatibility and preserve a rollback path.
- **Verify:** target toolchain, platform, license, security advisories, dependency tree and realistic workload.

## Entries

### `zod`
- **Package:** `zod`
- **Capability:** Validation
- **Language/runtime:** TypeScript / npm
- **Fit:** Parse untrusted runtime data, when the current codebase demonstrably needs it.
- **Anti-fit:** Only compile-time types or already validated boundaries are involved.
- **Fallback:** explicit checks or current validator.
- **Compatibility:** Node.js and modern browsers per official docs; TypeScript >=5.5 tested, strict mode required. Exact edge/bundler target UNKNOWN.
- **Maintenance:** npm latest 4.6.7; publish recency UNKNOWN; activity does not prove long-term support.
- **License:** MIT
- **Official source:** [official registry or upstream](https://registry.npmjs.org/zod/latest); [upstream/manifest](https://github.com/colinhacks/zod); [Zod official requirements](https://zod.dev/)
- **Evidence status:** PARTIAL
- **Evidence reviewed:** 2026-11-02
- **Unknowns:** Upstream documents TypeScript strict mode >=5.5, but npm does not declare a universal Node engine, and the exact target edge/bundler contract remains unresolved; retain BLOCKED. Security advisories: UNKNOWN; target performance and operational burden: NOT_MEASURED. Recheck before project selection.
- **Selection:** BLOCKED

### `valibot`
- **Package:** `valibot`
- **Capability:** Validation
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
- **Capability:** HTTP
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
- **Capability:** Observability
- **Language/runtime:** TypeScript / npm
- **Fit:** Structured JSON server logging, when the current codebase demonstrably needs it.
- **Anti-fit:** Browser-only work or an existing structured logger meets needs.
- **Fallback:** console or existing telemetry.
- **Compatibility:** Pino v10 dropped Node 18 per upstream release notes; verify supported active Node LTS line, transports and target runtime. Exact edge/worker compatibility UNKNOWN.
- **Maintenance:** npm latest 10.4.0; publish recency UNKNOWN; activity does not prove long-term support.
- **License:** MIT
- **Official source:** [official registry or upstream](https://registry.npmjs.org/pino/latest); [upstream/manifest](https://github.com/pinojs/pino); [Pino support policy](https://github.com/pinojs/pino/blob/main/docs/lts.md)
- **Evidence status:** PARTIAL
- **Evidence reviewed:** 2026-11-02
- **Unknowns:** Pino LTS policy covers supported Node lines but npm 10.4.0 omits an explicit engine range and target edge/transport compatibility remains unresolved; retain BLOCKED. Security advisories: UNKNOWN; target performance and operational burden: NOT_MEASURED. Recheck before project selection.
- **Selection:** BLOCKED

### `vitest`
- **Package:** `vitest`
- **Capability:** Testing
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
- **Capability:** Database
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

### `jose`
- **Package:** `jose`
- **Capability:** Crypto
- **Language/runtime:** TypeScript / npm
- **Fit:** JOSE token and key operations, when the current codebase demonstrably needs it.
- **Anti-fit:** Opaque sessions or an existing vetted authentication library cover requirements.
- **Fallback:** existing auth library or Web Crypto.
- **Compatibility:** jose v6 documents Node, Bun, Deno, browsers, Cloudflare Workers and Electron; algorithms and ESM/CJS requirements vary by runtime. Exact target crypto compatibility UNKNOWN.
- **Maintenance:** npm latest 6.2.15; publish recency UNKNOWN; activity does not prove long-term support.
- **License:** MIT
- **Official source:** [official registry or upstream](https://registry.npmjs.org/jose/latest); [upstream/manifest](https://github.com/panva/jose); [jose supported runtimes](https://github.com/panva/jose/blob/main/README.md)
- **Evidence status:** PARTIAL
- **Evidence reviewed:** 2026-11-02
- **Unknowns:** Upstream documents ESM and multi-runtime WebCrypto but algorithm availability and bundler behavior depend on the target; retain BLOCKED pending target crypto matrix. Security advisories: UNKNOWN; performance and operations: NOT_MEASURED. Recheck before project selection.
- **Selection:** BLOCKED

### `@opentelemetry/api`
- **Package:** `@opentelemetry/api`
- **Capability:** Observability
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
- **Capability:** AI
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
- **Capability:** Agentic / MCP
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
- **Capability:** Agentic / MCP
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
- **Capability:** Browser testing
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
- **Capability:** Tracing SDK
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
- **Capability:** Multi-provider AI SDK
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

## Selection boundary

VERIFIED is scoped to official package identity, metadata and advertised function; it is NOT a security endorsement, benchmark result or production approval. PARTIAL means essential metadata is unresolved. EVALUATE permits comparison only, BLOCKED requires filling compatibility/license gaps first. No automatic migration.

[Index](README.md) · [Languages](../languages/README.md) · [Frameworks](../frameworks/README.md) · [Decisions](../decisions/README.md)
