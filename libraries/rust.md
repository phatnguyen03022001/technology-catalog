# Rust — curated libraries

**Reviewed:** 2026-11-16 (UTC). Reusable code packages only, never framework or managed service production approvals.

## Dependency choice

- **Standard library first:** std networking, threads and types.
- **Add:** only for a documented capability that standard library and current dependencies do not sufficiently provide.
- **Keep:** do not migrate merely because a package appears in the catalog or has a newer release.
- **Remove/replace:** prove need, test compatibility and preserve a rollback path.
- **Verify:** target toolchain, platform, license, security advisories, dependency tree and realistic workload.

## Entries

### `tokio`
- **Package:** `tokio`
- **Capability:** C13 — Async & Messaging
- **Language/runtime:** Rust / Cargo
- **Fit:** Async network tasks, when the current codebase demonstrably needs it.
- **Anti-fit:** Synchronous one-shot tasks with no async boundary.
- **Fallback:** std::thread or existing runtime.
- **Compatibility:** Rust >= 1.85; check deployment platform and integrations.
- **Maintenance:** crates.io stable 1.54.1; updated 2026-10-21; activity does not prove long-term support.
- **License:** MIT
- **Official source:** [official registry or upstream](https://docs.rs/tokio/latest/tokio/); [upstream/manifest](https://github.com/tokio-rs/tokio)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-01
- **Unknowns:** Security advisories: UNKNOWN; exact target support, comparative benchmarks and operational burden: NOT_MEASURED. Recheck before project selection.
- **Selection:** EVALUATE

### `serde`
- **Package:** `serde`
- **Capability:** C07 — Data Contracts
- **Language/runtime:** Rust / Cargo
- **Fit:** Typed data interchange, when the current codebase demonstrably needs it.
- **Anti-fit:** No serialized boundary, or existing format-specific codec suffices.
- **Fallback:** existing codec or explicit types.
- **Compatibility:** Rust >= 1.56; check deployment platform and integrations.
- **Maintenance:** crates.io stable 1.0.229; updated 2026-07-18; activity does not prove long-term support.
- **License:** MIT OR Apache-2.0
- **Official source:** [official registry or upstream](https://docs.rs/serde/latest/serde/); [upstream/manifest](https://github.com/serde-rs/serde)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-01
- **Unknowns:** Security advisories: UNKNOWN; exact target support, comparative benchmarks and operational burden: NOT_MEASURED. Recheck before project selection.
- **Selection:** EVALUATE

### `reqwest`
- **Package:** `reqwest`
- **Capability:** C09 — API & Networking
- **Language/runtime:** Rust / Cargo
- **Fit:** Pooled high-level HTTP client, when the current codebase demonstrably needs it.
- **Anti-fit:** Low-level protocol work or an established HTTP client already meets needs.
- **Fallback:** current client or lower-level hyper.
- **Compatibility:** Rust >= 1.85.0; check deployment platform and integrations.
- **Maintenance:** crates.io stable 0.13.5; updated 2026-09-08; activity does not prove long-term support.
- **License:** MIT OR Apache-2.0
- **Official source:** [official registry or upstream](https://docs.rs/reqwest/latest/reqwest/); [upstream/manifest](https://github.com/seanmonstar/reqwest)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-01
- **Unknowns:** Tokio async requirement and TLS feature choice must match the surrounding stack. Security advisories: UNKNOWN; exact target support, comparative benchmarks and operational burden: NOT_MEASURED. Recheck before project selection.
- **Selection:** EVALUATE

### `sqlx`
- **Package:** `sqlx`
- **Capability:** C08 — Persistence
- **Language/runtime:** Rust / Cargo
- **Fit:** Async SQL against relational stores, when the current codebase demonstrably needs it.
- **Anti-fit:** No async SQL requirements, or existing database access is sufficient.
- **Fallback:** existing database client.
- **Compatibility:** Rust >= 1.94.0; check deployment platform and integrations.
- **Maintenance:** crates.io stable 0.9.0; updated 2026-05-21; activity does not prove long-term support.
- **License:** MIT OR Apache-2.0
- **Official source:** [official registry or upstream](https://docs.rs/sqlx/latest/sqlx/); [upstream/manifest](https://github.com/launchbadge/sqlx)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-01
- **Unknowns:** Async runtime and selected database feature flags affect deployment and compile-time checks. Security advisories: UNKNOWN; exact target support, comparative benchmarks and operational burden: NOT_MEASURED. Recheck before project selection.
- **Selection:** EVALUATE

### `tracing`
- **Package:** `tracing`
- **Capability:** C18 — Observability
- **Language/runtime:** Rust / Cargo
- **Fit:** Span-based structured diagnostics, when the current codebase demonstrably needs it.
- **Anti-fit:** A tiny tool needs only simple standard diagnostics.
- **Fallback:** current logging stack.
- **Compatibility:** Rust >= 1.65.0; check deployment platform and integrations.
- **Maintenance:** crates.io stable 0.1.44; updated 2025-12-18; activity does not prove long-term support.
- **License:** MIT
- **Official source:** [official registry or upstream](https://docs.rs/tracing/latest/tracing/); [upstream/manifest](https://github.com/tokio-rs/tracing)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-01
- **Unknowns:** Security advisories: UNKNOWN; exact target support, comparative benchmarks and operational burden: NOT_MEASURED. Recheck before project selection.
- **Selection:** EVALUATE

### `clap`
- **Package:** `clap`
- **Capability:** C19 — Developer Tooling
- **Language/runtime:** Rust / Cargo
- **Fit:** Subcommands and argument parsing, when the current codebase demonstrably needs it.
- **Anti-fit:** A command has just a few arguments and std parsing is clear.
- **Fallback:** std::env::args.
- **Compatibility:** Rust >= 1.85; check deployment platform and integrations.
- **Maintenance:** crates.io stable 4.6.7; updated 2026-09-14; activity does not prove long-term support.
- **License:** MIT OR Apache-2.0
- **Official source:** [official registry or upstream](https://docs.rs/clap/latest/clap/); [upstream/manifest](https://github.com/clap-rs/clap)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-01
- **Unknowns:** Security advisories: UNKNOWN; exact target support, comparative benchmarks and operational burden: NOT_MEASURED. Recheck before project selection.
- **Selection:** EVALUATE

### `thiserror`
- **Package:** `thiserror`
- **Capability:** C14 — Resilience & Errors
- **Language/runtime:** Rust / Cargo
- **Fit:** Typed library errors, when the current codebase demonstrably needs it.
- **Anti-fit:** Simple built-in errors are sufficient without a derive dependency.
- **Fallback:** std::error::Error.
- **Compatibility:** Rust >= 1.77; check deployment platform and integrations.
- **Maintenance:** crates.io stable 2.0.21; updated 2026-09-23; activity does not prove long-term support.
- **License:** MIT OR Apache-2.0
- **Official source:** [official registry or upstream](https://docs.rs/thiserror/latest/thiserror/); [upstream/manifest](https://github.com/dtolnay/thiserror)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-01
- **Unknowns:** Security advisories: UNKNOWN; exact target support, comparative benchmarks and operational burden: NOT_MEASURED. Recheck before project selection.
- **Selection:** EVALUATE

### `proptest`
- **Package:** `proptest`
- **Capability:** C17 — Testing & QA
- **Language/runtime:** Rust / Cargo
- **Fit:** Property testing and shrinking, when the current codebase demonstrably needs it.
- **Anti-fit:** A compact deterministic case set exercises the relevant invariant.
- **Fallback:** cargo test.
- **Compatibility:** Rust >= 1.88; check deployment platform and integrations.
- **Maintenance:** crates.io stable 1.12.0; updated 2026-10-10; activity does not prove long-term support.
- **License:** MIT OR Apache-2.0
- **Official source:** [official registry or upstream](https://docs.rs/proptest/latest/proptest/); [upstream/manifest](https://github.com/proptest-rs/proptest)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-01
- **Unknowns:** Security advisories: UNKNOWN; exact target support, comparative benchmarks and operational burden: NOT_MEASURED. Recheck before project selection.
- **Selection:** EVALUATE

### `rustls`
- **Package:** `rustls`
- **Capability:** C15 — Security & Cryptography
- **Language/runtime:** Rust / Cargo
- **Fit:** TLS protocol in Rust, when the current codebase demonstrably needs it.
- **Anti-fit:** TLS is already handled by the chosen HTTP client or platform stack.
- **Fallback:** existing TLS stack.
- **Compatibility:** Rust >= 1.71; check deployment platform and integrations.
- **Maintenance:** crates.io stable 0.23.46; updated 2026-10-14; activity does not prove long-term support.
- **License:** Apache-2.0 OR ISC OR MIT
- **Official source:** [official registry or upstream](https://docs.rs/rustls/latest/rustls/); [upstream/manifest](https://github.com/rustls/rustls)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-01
- **Unknowns:** Certificate trust roots and crypto provider configuration require review. Security advisories: UNKNOWN; exact target support, comparative benchmarks and operational burden: NOT_MEASURED. Recheck before project selection.
- **Selection:** EVALUATE

### `rmcp`
- **Package:** `rmcp`
- **Capability:** C20 — AI & Integrations
- **Language/runtime:** Rust / Cargo
- **Fit:** Official Tokio-based Rust MCP server/client SDK with tool macros and configurable transports.
- **Anti-fit:** No MCP boundary or simpler reqwest service client suffices.
- **Fallback:** reqwest or existing protocol client.
- **Compatibility:** Rust >=1.88 per tagged rmcp 3.10.0 workspace manifest; Tokio and selected transport features required; Streamable HTTP clients must use the fixed >=3.9.0 line; validate selected MCP version and transport.
- **Maintenance:** crates.io rmcp 3.10.0 released 2026-11-12 (official Rust MCP SDK); tagged upstream workspace reviewed.
- **License:** Apache-2.0
- **Official source:** [official registry or upstream](https://docs.rs/rmcp/latest/rmcp/); [upstream/manifest](https://github.com/modelcontextprotocol/rust-sdk)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-16
- **Unknowns:** Prior cited 3.8.0 is affected by [RUSTSEC-2026-0462](https://rustsec.org/advisories/RUSTSEC-2026-0462.html) in Streamable HTTP client response buffering; patched >=3.9.0. Confirm version >=3.9.0 when using affected transports. SDK does not automatically enforce tool authorization, SSRF protection, forwarded-secret rules or resource quotas. Full lockfile/advisory and deployment validation: NOT_MEASURED.
- **Selection:** EVALUATE

### `tonic`
- **Package:** `tonic`
- **Capability:** C09 — API & Networking
- **Language/runtime:** Rust / Cargo
- **Fit:** Rust async gRPC client/server based on generated typed Protobuf contracts.
- **Anti-fit:** Simple HTTP/JSON or an already-supported axum route.
- **Fallback:** axum or reqwest with HTTP/OpenAPI.
- **Compatibility:** Rust >=1.88 per crates.io tonic 0.14.9; check Tokio, prost/protoc and TLS feature versions.
- **Maintenance:** crates.io stable 0.14.9; updated 2026-10-29; official gRPC Rust repository.
- **License:** MIT
- **Official source:** [official registry or upstream](https://docs.rs/tonic/latest/tonic/); [upstream/manifest](https://github.com/grpc/grpc-rust)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-02
- **Unknowns:** Protobuf generation, HTTP/2 proxies, deployment, cancellation and telemetry are separate operational concerns. Security advisory applicability: UNKNOWN (no pinned-version OSV/GHSA review); target-specific integration, performance and TCO: NOT_MEASURED. Recheck official metadata and transitive dependencies before project adoption.
- **Selection:** EVALUATE

### `rayon`
- **Package:** `rayon`
- **Capability:** C13 — Async & Messaging
- **Language/runtime:** Rust / Cargo
- **Fit:** Data-parallel iterator and fork-join workloads that benefit from multicore CPU execution.
- **Anti-fit:** Async I/O, small workloads or already adequate sequential iteration.
- **Fallback:** std iterators/std::thread or Tokio for I/O.
- **Compatibility:** Rust >=1.80 per crates.io rayon 1.12.0; thread pool limits and target CPU require measurement.
- **Maintenance:** crates.io stable 1.12.0; updated 2026-04-14; verify maintenance before adoption.
- **License:** MIT OR Apache-2.0
- **Official source:** [official registry or upstream](https://docs.rs/rayon/latest/rayon/); [upstream/manifest](https://github.com/rayon-rs/rayon)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-02
- **Unknowns:** Parallelism can increase peak memory and contention; compare same CPU-bound workload, NOT_MEASURED. Security advisory applicability: UNKNOWN (no pinned-version OSV/GHSA review); target-specific integration, performance and TCO: NOT_MEASURED. Recheck official metadata and transitive dependencies before project adoption.
- **Selection:** EVALUATE

### `tower-http`
- **Package:** `tower-http`
- **Capability:** C09 — API & Networking
- **Language/runtime:** Rust / Cargo
- **Fit:** Opt-in HTTP-specific Tower layers for trace, CORS, body limits, compression and request IDs in Axum or compatible HTTP services.
- **Anti-fit:** Axum or Tower already supplies the needed layer; adding broad middleware stacks without a concrete HTTP concern.
- **Fallback:** Axum routing/extractors and existing Tower layers or http primitives.
- **Compatibility:** tower-http 0.7.1; Rust >=1.65 per release manifest; selected layers require Cargo features such as trace, cors, limit or compression-gzip; verify Tower and HTTP major versions against the selected Axum release.
- **Maintenance:** 0.7.1 published in crates.io/docs.rs; upstream tower-rs/tower-http maintained; support lifecycle is not guaranteed.
- **License:** MIT
- **Official source:** [docs.rs crate documentation](https://docs.rs/tower-http/latest/tower_http/); [upstream manifest](https://github.com/tower-rs/tower-http)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-16
- **Unknowns:** Exact middleware ordering, compressed-body limits, target service version resolution, RustSec applicability and workload cost require project-specific checks.
- **Selection:** EVALUATE

### `axum-extra`
- **Package:** `axum-extra`
- **Capability:** C03 — Forms & Navigation
- **Language/runtime:** Rust / Cargo
- **Fit:** Optional Axum extractors and helpers such as typed headers/routes, multipart and cookies when built-in axum extractors do not cover the use case.
- **Anti-fit:** Core Path, Query, Json, Form or Multipart extractors suffice; do not install all helpers by default.
- **Fallback:** Axum standard extractors and Router.
- **Compatibility:** axum-extra 0.12.6; Rust >=1.80 in published Cargo manifest; integrates with axum 0.8.x; optional features include typed-routing, typed-header, multipart and cookie; default enables tracing.
- **Maintenance:** 0.12.6 crate manifest and Axum upstream reviewed; no future support assurance.
- **License:** MIT
- **Official source:** [docs.rs crate documentation](https://docs.rs/axum-extra/latest/axum_extra/); [upstream manifest](https://github.com/tokio-rs/axum)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-16
- **Unknowns:** Cookie signing/encryption, CSRF, custom rejection mapping, feature combinations and target Cargo resolution require independent verification.
- **Selection:** EVALUATE

### `garde`
- **Package:** `garde`
- **Capability:** C07 — Data Contracts
- **Language/runtime:** Rust / Cargo
- **Fit:** Declarative domain and input validation on deserialized Rust structs; distinct from Serde serialization and schema documentation.
- **Anti-fit:** A few explicit validation checks are simpler, or existing validation is sufficient.
- **Fallback:** Explicit typed validation following Axum extraction with existing Serde types.
- **Compatibility:** garde 0.23.0; workspace Cargo MSRV Rust >=1.87; features derive and serde are opt-in, alongside optional regex/email/url rules; framework-independent validation API.
- **Maintenance:** 0.23.0 official workspace and package manifests reviewed; maintenance continuity not guaranteed.
- **License:** MIT OR Apache-2.0
- **Official source:** [docs.rs crate documentation](https://docs.rs/garde/latest/garde/); [upstream manifest](https://github.com/jprochazk/garde)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-16
- **Unknowns:** Axum rejection-to-HTTP mapping is application-owned; validation semantics, feature resolution and security advisories require project-specific audit.
- **Selection:** EVALUATE

### `utoipa`
- **Package:** `utoipa`
- **Capability:** C07 — Data Contracts
- **Language/runtime:** Rust / Cargo
- **Fit:** Compile-time OpenAPI contract generation for typed HTTP APIs; optional axum_extras support and separate Axum integration.
- **Anti-fit:** Small internal HTTP service without a published API contract, or existing hand-maintained OpenAPI is sufficient.
- **Fallback:** Explicit documented JSON request/response contracts and existing Serde types.
- **Compatibility:** utoipa 6.0.0; Rust >=1.88 from tagged upstream workspace; default macros; optional axum_extras feature and separate utoipa-axum adapter, whose version must be resolved with Axum.
- **Maintenance:** 6.0.0 tagged Cargo workspace and crate manifests reviewed; breaking macro behavior requires migration review.
- **License:** MIT OR Apache-2.0
- **Official source:** [docs.rs crate documentation](https://docs.rs/utoipa/latest/utoipa/); [upstream manifest](https://github.com/juhaku/utoipa)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-16
- **Unknowns:** Generated schema does not validate incoming requests or authorize them; validate version coupling, generated document accuracy and advisories before use.
- **Selection:** EVALUATE

### `argon2`
- **Package:** `argon2`
- **Capability:** C15 — Security & Cryptography
- **Language/runtime:** Rust / Cargo
- **Fit:** RustCrypto password hashing and verification with Argon2id for locally managed password authentication when required.
- **Anti-fit:** Authentication is delegated to an identity provider or no passwords are stored; never hash arbitrary short-lived request tokens as a password substitute.
- **Fallback:** Existing compliant identity service or already-reviewed password hashing implementation.
- **Compatibility:** argon2 0.6.0; Rust >=1.85 from tagged RustCrypto manifest; default alloc/getrandom/password-hash, optional parallel and zeroize; CPU/memory cost must be bounded and blocking work isolated from async handlers.
- **Maintenance:** 0.6.0 official package manifest reviewed; cryptographic policy and future maintenance require separate review.
- **License:** MIT OR Apache-2.0
- **Official source:** [docs.rs crate documentation](https://docs.rs/argon2/latest/argon2/); [upstream manifest](https://github.com/RustCrypto/password-hashes)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-16
- **Unknowns:** Password parameters, salt quality, migration/re-hash, memory exhaustion, secret storage and RustSec/transitive advisories require project-specific checks; this is not an auth system.
- **Selection:** EVALUATE

### `moka`
- **Package:** `moka`
- **Capability:** C16 — Performance & Cache
- **Language/runtime:** Rust / Cargo
- **Fit:** Concurrent in-process cache with bounded capacity and eviction/TTL for repeated local reads when measurements justify it.
- **Anti-fit:** Simple HashMap/Mutex suffices, or distributed coherence and persistence are required.
- **Fallback:** std collections with bounded state and explicit invalidation, or established cache.
- **Compatibility:** moka 0.12.16; Rust >=1.71.1 for future/sync per manifest; default enables neither, explicitly choose future for async or sync for sync; Wasm/WASI unsupported per upstream README.
- **Maintenance:** 0.12.16 published manifest and README reviewed; caching cost depends on workload and memory budgets.
- **License:** (MIT OR Apache-2.0) AND Apache-2.0
- **Official source:** [docs.rs crate documentation](https://docs.rs/moka/latest/moka/); [upstream manifest](https://github.com/moka-rs/moka)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-16
- **Unknowns:** Eviction timing, stale data, memory pressure, target support outside documented CI, legal treatment of Apache-only files and advisories require workload review.
- **Selection:** EVALUATE

### `axum-test`
- **Package:** `axum-test`
- **Capability:** C17 — Testing & QA
- **Language/runtime:** Rust / Cargo
- **Fit:** Optional high-level HTTP/WebSocket integration harness for Axum routes where repeated request assertions justify a dev dependency.
- **Anti-fit:** Simple Router tests using Tower ServiceExt oneshot or ordinary tokio test cases suffice.
- **Fallback:** Axum Router + tower::ServiceExt and cargo test; existing proptest for invariants.
- **Compatibility:** axum-test 21.1.0; Rust >=1.89; Cargo release depends on Axum 0.8.x; optional WebSocket and other testing features must match the target router.
- **Maintenance:** 21.1.0 published crate manifest reviewed; test harness does not certify service correctness.
- **License:** MIT
- **Official source:** [docs.rs crate documentation](https://docs.rs/axum-test/latest/axum_test/); [upstream manifest](https://github.com/JosephLenton/axum-test)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-16
- **Unknowns:** Socket versus in-process behavior, actual deployment stack, feature resolution and test isolation require verification; no security guarantee.
- **Selection:** EVALUATE

### `tracing-subscriber`
- **Package:** `tracing-subscriber`
- **Capability:** C18 — Observability
- **Language/runtime:** Rust / Cargo
- **Fit:** Subscriber setup, structured formatting and filtering for existing tracing spans/events in Rust services.
- **Anti-fit:** An existing subscriber or platform logging bridge already handles diagnostics.
- **Fallback:** Existing logging/subscriber implementation; tracing remains instrumentation-only.
- **Compatibility:** tracing-subscriber 0.3.23; Rust >=1.65; integrates with tracing 0.1; fmt default feature and env-filter opt-in; exporter/OpenTelemetry integration is separate.
- **Maintenance:** 0.3.23 published Cargo manifest reviewed; repository tokio-rs/tracing.
- **License:** MIT
- **Official source:** [docs.rs crate documentation](https://docs.rs/tracing-subscriber/latest/tracing_subscriber/); [upstream manifest](https://github.com/tokio-rs/tracing)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-16
- **Unknowns:** Sensitive-field redaction, log sampling/volume, structured export, telemetry costs, platform sinks and advisory applicability require application review.
- **Selection:** EVALUATE

### `jsonwebtoken`
- **Package:** `jsonwebtoken`
- **Capability:** C10 — Identity & Authorization
- **Language/runtime:** Rust / Cargo; optional Axum server-side bearer-token verification
- **Fit:** Verify or issue signed JWTs for an explicitly selected bearer/OIDC token model after server-side identity and trust boundaries are defined.
- **Anti-fit:** Existing trusted identity middleware, opaque browser sessions, or no bearer JWT model; parsing JWTs is neither a complete login system nor user/tenant authorization.
- **Fallback:** Axum extractors with existing verified identity infrastructure; for owned cookie sessions evaluate axum-login plus tower-sessions separately.
- **Compatibility:** crates.io jsonwebtoken 12.0.0 declares Rust >=1.88.0; choose one cryptographic provider feature (rust_crypto or aws_lc_rs), or explicitly install a custom CryptoProvider. Axum integration uses application extractors/middleware; serde claims and target Cargo/feature graph require verification.
- **Maintenance:** crates.io stable 12.0.0; published 2026-11-13; v12 changed crypto/provider and key validation behavior, so migration and dependency checks are required.
- **License:** MIT
- **Official source:** [docs.rs crate documentation](https://docs.rs/jsonwebtoken/latest/jsonwebtoken/); [published manifest and changelog](https://docs.rs/crate/jsonwebtoken/12.0.0/source/CHANGELOG.md); [upstream repository](https://github.com/Keats/jsonwebtoken)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-17
- **Unknowns:** Allowed algorithms, expected issuer/audience, required expiry and not-before, key lookup/JWKS fetching and caching, kid rotation, revocation, secret custody, token confusion, authorization/tenant ownership, CSRF for cookie flows, RustSec/OSV and transitive advisories NOT_VERIFIED for a concrete app. The crate does not independently provide session lifecycle or resource authorization.
- **Selection:** EVALUATE

### `tracing-opentelemetry`
- **Package:** `tracing-opentelemetry`
- **Capability:** C18 — Observability
- **Language/runtime:** Rust / Cargo; optional tracing-to-OpenTelemetry layer
- **Fit:** Bridge existing tracing spans into an OpenTelemetry tracer provider when an Axum service genuinely needs exported distributed traces.
- **Anti-fit:** Structured logs/tracing-subscriber already satisfy incident diagnostics, or there is no collector or remote trace requirement.
- **Fallback:** Existing tracing + tracing-subscriber local logging; do not configure a remote exporter.
- **Compatibility:** crates.io tracing-opentelemetry 0.34.0 declares Rust >=1.75; depends on opentelemetry ^0.33.0 and tracing-subscriber ^0.3.22, compatible with OpenTelemetry 0.33.x despite unequal versions. Default features include metrics and tracing-log; disable unnecessary features for trace-only use and verify Cargo resolution.
- **Maintenance:** crates.io stable 0.34.0; published September 2026; upstream release notes and tagged Cargo manifest reviewed.
- **License:** MIT
- **Official source:** [docs.rs crate documentation](https://docs.rs/tracing-opentelemetry/latest/tracing_opentelemetry/); [published Cargo manifest](https://docs.rs/crate/tracing-opentelemetry/0.34.0/source/Cargo.toml.orig); [upstream repository](https://github.com/tokio-rs/tracing-opentelemetry)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-17
- **Unknowns:** No exporter or collector comes with the bridge; HTTP context propagation, traceparent extraction/injection, sampling, span redaction, provider/SDK configuration, full feature resolution, RustSec/OSV advisories, performance and TCO NOT_VERIFIED.
- **Selection:** EVALUATE

### `opentelemetry_sdk`
- **Package:** `opentelemetry_sdk`
- **Capability:** C18 — Observability
- **Language/runtime:** Rust / Cargo; OpenTelemetry SDK for optional Axum trace processing
- **Fit:** Configure SdkTracerProvider, processing, sampling, resource attribution and exporter connection where real trace export is required.
- **Anti-fit:** Local tracing/logs suffice, or an existing configured SDK/provider is already owned by the application.
- **Fallback:** Existing tracing-subscriber without remote export; use an already provided telemetry SDK when suitable.
- **Compatibility:** crates.io opentelemetry_sdk 0.33.1; upstream OpenTelemetry Rust minimum supported Rust 1.75.0; API and OTLP exporter 0.33.1 belong to the same OpenTelemetry release line. Trace, runtime and batch features must be chosen and verified with Tokio and Cargo.
- **Maintenance:** crates.io stable 0.33.1; official Rust OpenTelemetry SDK documentation and release metadata reviewed; no support SLA inferred.
- **License:** Apache-2.0
- **Official source:** [docs.rs crate documentation](https://docs.rs/opentelemetry_sdk/latest/opentelemetry_sdk/); [upstream repository](https://github.com/open-telemetry/opentelemetry-rust)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-17
- **Unknowns:** Actual sampling policy, batch queue limits/backpressure, runtime scheduling, shutdown and force_flush behavior, resource attributes, context propagation, collector outage, drop counts, advisory applicability, overhead and TCO NOT_VERIFIED. API alone is a no-op without an SDK.
- **Selection:** EVALUATE

### `opentelemetry-otlp`
- **Package:** `opentelemetry-otlp`
- **Capability:** C18 — Observability
- **Language/runtime:** Rust / Cargo; optional OTLP transport/exporter
- **Fit:** Export OpenTelemetry SDK spans to an existing OTLP-compatible collector/backend using an explicitly chosen HTTP/protobuf or gRPC transport.
- **Anti-fit:** No remote trace destination, logs alone suffice, or another existing exporter is already configured.
- **Fallback:** Local tracing-subscriber output; retain the existing telemetry backend integration when suitable.
- **Compatibility:** crates.io opentelemetry-otlp 0.33.1 aligns with opentelemetry and opentelemetry_sdk 0.33.1; upstream Rust minimum 1.75.0. Select trace-only Cargo features and HTTP-protobuf or grpc-tonic transport, TLS backend, endpoint and Tokio-compatible processor deliberately; default features also enable other signal types. Upstream calls OTLP trace export beta.
- **Maintenance:** crates.io stable 0.33.1; released 2026-10-08; upstream changelog states trace exporter beta while metrics/logs exporters are stable.
- **License:** Apache-2.0
- **Official source:** [docs.rs crate documentation](https://docs.rs/opentelemetry-otlp/latest/opentelemetry_otlp/); [official OTLP changelog](https://github.com/open-telemetry/opentelemetry-rust/blob/main/opentelemetry-otlp/CHANGELOG.md)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-17
- **Unknowns:** Exporter alone does not create a tracing layer, SDK or collector. Endpoint/auth/TLS, batch buffer and retry/drop behavior, W3C propagation, graceful flush, advisories, real delivery, runtime overhead and TCO NOT_VERIFIED. Collector deployment is conditional, not a framework default.
- **Selection:** EVALUATE

## Selection boundary

VERIFIED is scoped to official package identity, metadata and advertised function; it is NOT a security endorsement, benchmark result or production approval. PARTIAL means essential metadata is unresolved. EVALUATE permits comparison only, BLOCKED requires filling compatibility/license gaps first. No automatic migration.

## Axum / Rust capability screen (UTC evidence: 2026-11-17)

An Axum HTTP-service workload is the comparator, not a requirement to install all listed crates. `NOT_APPLICABLE` is intentional; `CONDITIONAL` does not imply a missing default package. Every entry above has one primary C01–C20 capability.

| ID | Decision | Native-first finding and conditional option |
|---|---|---|
| C01 | NOT_APPLICABLE | API-only Axum does not need UI design libraries. |
| C02 | NOT_APPLICABLE | Rendering/animation is client work; server-side rendering only with a concrete requirement. |
| C03 | CONDITIONAL | Axum Path/Query/Form/Json/Multipart first; axum-extra only for missing typed routing, headers or cookie helpers. |
| C04 | CONDITIONAL | Inspect Accept-Language and explicit locale negotiation; response translation/catalog management remains application-owned. |
| C05 | NATIVE_FIRST | Axum State, Arc and Tokio synchronization; avoid long-held blocking locks, enforce ownership and scoped concurrency. |
| C06 | EXISTING | reqwest for HTTP clients; define retries, caching and distributed consistency explicitly rather than adding a sync framework. |
| C07 | ADDED | Serde for formats; garde for domain validation, utoipa for OpenAPI; neither automatically maps rejection responses nor replaces authorization. |
| C08 | EXISTING | SQLx plus its own pooling/migrations when appropriate; Diesel/SeaORM, deadpool and bb8 deferred without ORM/pool requirement. |
| C09 | ADDED | Axum routing + Tower services + Hyper/http first; tower-http opt-in HTTP middleware; existing tonic only when gRPC required. |
| C10 | CONDITIONAL | Native Axum/Tower extraction and trusted identity first; jsonwebtoken only for justified signed bearer JWT validation; axum-login/tower-sessions is an alternative for owned cookie sessions. Signature and claims checks do not provide tenant authorization. |
| C11 | CONDITIONAL | Database native full-text/indexing first; external search clients only with measured retrieval requirements. |
| C12 | NATIVE_FIRST | Axum Multipart and streaming with bounded body sizes, file type/size checks and explicit object ownership. |
| C13 | EXISTING | Tokio tasks, cancellation and shutdown; bounded channels/concurrency; Rayon solely for justified CPU parallelism. |
| C14 | EXISTING | thiserror and explicit HTTP error mapping; Tower timeouts/backpressure; retry only safe/idempotent work under budgets. |
| C15 | ADDED | Existing rustls for TLS; argon2 only when managing user passwords; authz, CSRF, SSRF and secret redaction remain separate. |
| C16 | ADDED | std collections and bounded app state first; moka for measured per-process cache needs, not distributed coherence. |
| C17 | ADDED | cargo test + Axum Router/Tower oneshot and existing proptest first; axum-test for higher-level HTTP cases. |
| C18 | CONDITIONAL | Existing tracing + tracing-subscriber suffice for local diagnostics. Remote OTLP traces optionally require compatible tracing-opentelemetry bridge (0.34), opentelemetry_sdk (0.33.1) and opentelemetry-otlp (0.33.1); API opentelemetry (0.33.x) is already transitive unless application directly imports it. |
| C19 | NATIVE_FIRST | Cargo fmt, Clippy, test, audit and feature inspection; existing clap for complex command surfaces only. |
| C20 | EXISTING | Existing reqwest, rmcp and tonic are optional protocol boundaries; enforce permissions, SSRF protection and MCP transport limits. |

### Shortlist alternatives not added

- **validator vs garde:** both perform domain validation; one optional validation library suffices for a specific workload. Serde does not do domain validation.
- **schemars vs utoipa:** JSON Schema differs from endpoint OpenAPI. Add schemars only if standalone schema generation is required.
- **sea-orm / diesel / deadpool / bb8:** existing SQLx and built-in pooling are enough to start; ORM or alternate pool is a separate workload decision.
- **axum-login / jsonwebtoken / secrecy:** jsonwebtoken now listed as a conditional JWT-specific option; axum-login plus tower-sessions remains an unadded session-based alternative. An identity model, issuer/audience/algorithm/key rotation, protected secret boundary and server authorization are required. Session CSRF and cookie security are application decisions.
- **governor / backon / Tower:** Tower already has middleware primitives; add rate-limit/backoff tools only with a defined identity key, bounded retries, idempotency and distributed topology.
- **wiremock / mockall / axum-test:** cargo test and Tower oneshot first; use an additional mock/test harness only for meaningful coverage.
- **metrics / OpenTelemetry:** tracing + tracing-subscriber first. Optional OTLP trace integration needs a bridge, SDK and exporter together, not merely an exporter; opentelemetry API is transitive unless directly imported. No collector is provisioned by the catalog.
- **Tower, Hyper, Tokio, reqwest, tonic, rmcp:** existing framework or catalog entries; do not add a duplicate primary record just to fill a category.

### Conditional Axum identity and OTLP boundaries (2026-11-17)

JWT and cookie sessions are different architectures: use application-owned extractors/Tower policy and existing identity first; `jsonwebtoken` is conditional for a service verifying signed bearer JWTs, while `axum-login`/`tower-sessions` suits owned browser cookie sessions when persistence, session expiration, CSRF and cookie flags are specified. A JWT signature alone cannot establish issuer, audience, expiry, revocation or tenant ownership. JWT signing algorithm allowlists, claim validation, key rotation and JWKS retrieval/caching remain application-specific. [JWT validation](https://docs.rs/jsonwebtoken/latest/jsonwebtoken/struct.Validation.html) · [Axum login](https://docs.rs/axum-login/latest/axum_login/).

For a trace-exporting Axum service, `tracing` instruments spans, `tracing-subscriber` composes layers, `tracing-opentelemetry` 0.34.0 bridges to `opentelemetry` 0.33.x, `opentelemetry_sdk` 0.33.1 processes telemetry, and `opentelemetry-otlp` 0.33.1 exports to an existing endpoint. The OTel API is an ordinary transitive dependency unless the application imports it directly. Tower HTTP middleware instruments requests but does not automatically guarantee propagated trace context. Choose trace-only features, HTTP or gRPC, Tokio processing, TLS/auth, resource attributes, sampling, redaction, bounded queues, backpressure and shutdown flushing per service. Official upstream identifies OTLP **trace export as beta** in 0.33.1. No real context-propagation/export/retry/collector or performance validation exists. [Bridge compatibility](https://docs.rs/tracing-opentelemetry/latest/tracing_opentelemetry/) · [OTLP changelog](https://github.com/open-telemetry/opentelemetry-rust/blob/main/opentelemetry-otlp/CHANGELOG.md).

### Axum-specific engineering boundaries

- Request body limits and middleware order matter: decompression, logging, CORS, auth, multipart and timeout placement change effective protection. Decide what layer enforces each bound.
- Send/Sync, cancellation, graceful shutdown, client disconnects, backpressure, pool exhaustion and bounded blocking work require workload tests, not a crate name.
- Password hashing uses expensive CPU/memory; isolate bounded blocking operations. CORS is not CSRF protection, TLS is not authorization, and token parsing is not policy evaluation.
- Moka is per-process. Invalidate carefully; no automatic distributed coherence or persistence. Track p95/p99, hit rate, memory, eviction and pool occupancy before adopting cache.
- `rmcp` **3.8.0** is affected by [RUSTSEC-2026-0462](https://rustsec.org/advisories/RUSTSEC-2026-0462.html) in Streamable HTTP clients; fixed from 3.9.0. Updated catalog metadata to 3.10.0; no lockfile or transitive advisory scan was performed.
- Source metadata and documented versions/features are verified, not Cargo feature-resolution tests or proof of production safety. Target OS/arch, complete dependency graph, license obligations and advisories remain project-specific.

### Sources and evidence boundaries

[Rust/Cargo features](https://doc.rust-lang.org/cargo/reference/features.html) · [Axum](https://docs.rs/axum/latest/axum/) · [Tokio](https://docs.rs/tokio/latest/tokio/) · [Tower](https://docs.rs/tower/latest/tower/) · [HTTP middleware](https://docs.rs/tower-http/latest/tower_http/) · [RustSec advisory](https://rustsec.org/advisories/RUSTSEC-2026-0462.html). Package-specific docs.rs and upstream manifests are linked in each canonical entry. Reviewed 2026-11-16 UTC; version/MSRV/feature/compatibility claims are scoped to the cited versions. No Cargo build, benchmark, deployed integration or complete vulnerability scan was executed.

[Index](README.md) · [Languages](../languages/README.md) · [Frameworks](../frameworks/README.md) · [Decisions](../decisions/README.md)
