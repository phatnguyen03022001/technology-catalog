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
- **Evidence reviewed:** 2026-11-01
- **Unknowns:** Security advisories: UNKNOWN; exact target support, comparative benchmarks and operational burden: NOT_MEASURED. Recheck before project selection.
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
- **Evidence reviewed:** 2026-11-01
- **Unknowns:** Security advisories: UNKNOWN; exact target support, comparative benchmarks and operational burden: NOT_MEASURED. Recheck before project selection.
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
- **Maintenance:** npm latest 6.2.14; publish recency UNKNOWN; activity does not prove long-term support.
- **License:** MIT
- **Official source:** [official registry or upstream](https://registry.npmjs.org/jose/latest); [upstream/manifest](https://github.com/panva/jose); [jose supported runtimes](https://github.com/panva/jose/blob/main/README.md)
- **Evidence status:** PARTIAL
- **Evidence reviewed:** 2026-11-01
- **Unknowns:** Security advisories: UNKNOWN; exact target support, comparative benchmarks and operational burden: NOT_MEASURED. Recheck before project selection.
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
- **Unknowns:** Instrumentation API alone does not export spans or metrics. Security advisories: UNKNOWN; exact target support, comparative benchmarks and operational burden: NOT_MEASURED. Recheck before project selection.
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

## Selection boundary

VERIFIED is scoped to official package identity, metadata and advertised function; it is NOT a security endorsement, benchmark result or production approval. PARTIAL means essential metadata is unresolved. EVALUATE permits comparison only, BLOCKED requires filling compatibility/license gaps first. No automatic migration.

[Index](README.md) · [Languages](../languages/README.md) · [Frameworks](../frameworks/README.md) · [Decisions](../decisions/README.md)
