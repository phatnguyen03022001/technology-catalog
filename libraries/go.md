# Go — curated libraries

**Reviewed:** 2026-11-17. Reusable code packages only, never framework or managed service production approvals.

## Dependency choice

- **Standard library first:** net/http, encoding/json, sync, log/slog, testing and flag.
- **Add:** only for a documented capability that standard library and current dependencies do not sufficiently provide.
- **Keep:** do not migrate merely because a package appears in the catalog or has a newer release.
- **Remove/replace:** prove need, test compatibility and preserve a rollback path.
- **Verify:** target toolchain, platform, license, security advisories, dependency tree and realistic workload.

## Gin / Go capability screening (2026-11-17)

`NATIVE_FIRST` favors Go/Gin capabilities, `EXISTING` reuses indexed records, `CONDITIONAL` requires a specific workload, and `NOT_APPLICABLE` requires no Gin library. No selection is mandatory.

| ID | Screening | Workload-specific finding |
|---|---|---|
| C01 | NOT_APPLICABLE | UI/design-system concerns belong to clients, not a JSON-only backend. |
| C02 | NOT_APPLICABLE | Animation/visualization belongs to clients; expose data contracts. |
| C03 | NATIVE_FIRST | Gin route params, ShouldBind, multipart; validate bounded payloads and map errors. |
| C04 | NATIVE_FIRST | Locale negotiation and translated errors only for real multilingual needs. |
| C05 | NATIVE_FIRST | context, sync, channels, lifecycle ownership; no shared mutable request state. |
| C06 | NATIVE_FIRST | net/http and request deadlines; Redis sync only with a shared-state need. |
| C07 | NATIVE_FIRST | Explicit DTOs, encoding/json and Gin-integrated validator; optional sqlc/OpenAPI generation. |
| C08 | CONDITIONAL | database/sql or existing pgx first; goose for controlled SQL migrations. |
| C09 | CONDITIONAL | Gin and net/http built in; cors middleware only for browser cross-origin needs; Chi is not Gin middleware. |
| C10 | CONDITIONAL | Gin cookie sessions or jwt/v5 for different auth models; authorization separate. |
| C11 | NATIVE_FIRST | PostgreSQL full-text through existing pgx before external search infrastructure. |
| C12 | NATIVE_FIRST | Gin multipart and streaming, http.MaxBytesReader, content checks and safe storage. |
| C13 | EXISTING | Context-bound goroutines, existing x/sync; Redis-backed asynq only if durable jobs needed. |
| C14 | CONDITIONAL | Timeouts native; backoff for bounded retries and x/time/rate for per-instance limits. |
| C15 | NATIVE_FIRST | Standard crypto/TLS and existing x/crypto when required; no homemade cryptography. |
| C16 | CONDITIONAL | Bounded memory, SQL pooling/local cache first; go-redis only with justified Redis service. |
| C17 | CONDITIONAL | testing, httptest, existing testify/go-cmp; testcontainers when real integration tests needed. |
| C18 | CONDITIONAL | log/slog and existing OTel SDK; otelgin for instrumented Gin tracing. |
| C19 | EXISTING | gofmt, go vet, go test, go generate; existing Cobra for CLI hierarchies. |
| C20 | EXISTING | Existing OpenAI SDK, official MCP SDK and gRPC; net/http for simple third-party calls. |

### Critical integration gates

- **HTTP:** Gin `Bind*` writes 400 on binding error; `ShouldBind*` returns the error for handler-owned response mapping. Validate strict DTOs/unknown fields as needed, body sizes, upload types and response consistency. Middleware ordering, graceful shutdown and read/write timeouts remain application concerns.
- **Context/concurrency:** Use `c.Request.Context()` for I/O cancellation. Never retain an active `gin.Context` across goroutines; `c.Copy()` provides a read-only snapshot when necessary. Bound workers, ensure idempotency for retries/jobs, and shut them down cleanly.
- **Auth:** CORS is not CSRF or authorization. Cookie sessions require Secure/HttpOnly/SameSite, CSRF, secret rotation and trusted-proxy policy. JWT requires signature, expected algorithm, issuer, audience, expiry, key rotation and authorization checks on every protected route.
- **Operations:** Rate limiting is not complete DoS protection; Redis requires service security, pooling, outage and persistence decisions. Migration ownership, SQL transaction behavior, OpenTelemetry exporter/sampling, PII redaction and metrics are not automatically solved by packages.
- **Evaluated and not added:** go-playground/validator/v10 (Gin binding already uses it); GORM (existing pgx/database/sql first); sqlc and swaggo/gin-swagger (require an actual SQL/contract generation workflow); gin-contrib/secure (small security-header policy can be owned by Gin/proxy); gin-contrib/gzip (edge/proxy compression usually suffices); gin-contrib/requestid (small application/proxy middleware); go-sqlmock (native tests or real DB integration as appropriate); additional assertion/cache libraries without a distinct need.
- **Official framework/security references:** [Go packages](https://pkg.go.dev/std), [Gin model binding](https://gin-gonic.com/en/docs/binding/binding-and-validation/), [Gin goroutines](https://gin-gonic.com/en/docs/middleware/goroutines-inside-a-middleware/), [Go vulnerability database](https://vuln.go.dev/). Records below cite pinned module sources; metadata verification never proves safety or performance.

## Entries

### `go-chi/chi`
- **Package:** `github.com/go-chi/chi/v5`
- **Capability:** C09 — API & Networking
- **Language/runtime:** Go / Go modules
- **Fit:** Composable routing with net/http, when the current codebase demonstrably needs it.
- **Anti-fit:** net/http ServeMux already supports the required routes.
- **Fallback:** net/http.
- **Compatibility:** Go >= 1.24; check deployment platform and integrations.
- **Maintenance:** Go module v5.5.0; upstream pushed 2026-10-18; activity does not prove long-term support.
- **License:** MIT
- **Official source:** [official registry or upstream](https://pkg.go.dev/github.com/go-chi/chi/v5@v5.5.0); [upstream/manifest](https://github.com/go-chi/chi)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-01
- **Unknowns:** Security advisories: UNKNOWN; exact target support, comparative benchmarks and operational burden: NOT_MEASURED. Recheck before project selection.
- **Selection:** EVALUATE

### `jackc/pgx`
- **Package:** `github.com/jackc/pgx/v5`
- **Capability:** C08 — Persistence
- **Language/runtime:** Go / Go modules
- **Fit:** PostgreSQL wire driver and pooling, when the current codebase demonstrably needs it.
- **Anti-fit:** The workload is not PostgreSQL or an existing database/sql driver suffices.
- **Fallback:** database/sql with existing driver.
- **Compatibility:** Go >= 1.25.0; check deployment platform and integrations.
- **Maintenance:** Go module v5.12.0; upstream pushed 2026-10-31; activity does not prove long-term support.
- **License:** MIT
- **Official source:** [official registry or upstream](https://pkg.go.dev/github.com/jackc/pgx/v5@v5.12.0); [upstream/manifest](https://github.com/jackc/pgx)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-01
- **Unknowns:** PostgreSQL server feature set and pgx major-version module path require checks. Security advisories: UNKNOWN; exact target support, comparative benchmarks and operational burden: NOT_MEASURED. Recheck before project selection.
- **Selection:** EVALUATE

### `rs/zerolog`
- **Package:** `github.com/rs/zerolog`
- **Capability:** C18 — Observability
- **Language/runtime:** Go / Go modules
- **Fit:** Structured application logging, when the current codebase demonstrably needs it.
- **Anti-fit:** Built-in log/slog already meets structured logging needs.
- **Fallback:** log/slog.
- **Compatibility:** Go >= 1.23; check deployment platform and integrations.
- **Maintenance:** Go module v1.35.1; upstream pushed 2026-10-14; activity does not prove long-term support.
- **License:** MIT
- **Official source:** [official registry or upstream](https://pkg.go.dev/github.com/rs/zerolog@v1.35.1); [upstream/manifest](https://github.com/rs/zerolog)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-01
- **Unknowns:** Security advisories: UNKNOWN; exact target support, comparative benchmarks and operational burden: NOT_MEASURED. Recheck before project selection.
- **Selection:** EVALUATE

### `stretchr/testify`
- **Package:** `github.com/stretchr/testify`
- **Capability:** C17 — Testing & QA
- **Language/runtime:** Go / Go modules
- **Fit:** Assertions and test doubles, when the current codebase demonstrably needs it.
- **Anti-fit:** Standard testing comparisons are clearer and adequate.
- **Fallback:** testing.
- **Compatibility:** Go >= 1.17; check deployment platform and integrations.
- **Maintenance:** Go module v1.12.1; upstream pushed 2026-10-19; activity does not prove long-term support.
- **License:** MIT
- **Official source:** [official registry or upstream](https://pkg.go.dev/github.com/stretchr/testify@v1.12.1); [upstream/manifest](https://github.com/stretchr/testify)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-01
- **Unknowns:** Security advisories: UNKNOWN; exact target support, comparative benchmarks and operational burden: NOT_MEASURED. Recheck before project selection.
- **Selection:** EVALUATE

### `google/go-cmp`
- **Package:** `github.com/google/go-cmp`
- **Capability:** C17 — Testing & QA
- **Language/runtime:** Go / Go modules
- **Fit:** Readable structural test differences, when the current codebase demonstrably needs it.
- **Anti-fit:** Simple equality checks provide enough failure information.
- **Fallback:** testing.
- **Compatibility:** Go >= 1.21; check deployment platform and integrations.
- **Maintenance:** Go module v0.7.0; upstream pushed 2026-10-29; activity does not prove long-term support.
- **License:** BSD-3-Clause
- **Official source:** [official registry or upstream](https://pkg.go.dev/github.com/google/go-cmp@v0.7.0); [upstream/manifest](https://github.com/google/go-cmp)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-01
- **Unknowns:** Security advisories: UNKNOWN; exact target support, comparative benchmarks and operational burden: NOT_MEASURED. Recheck before project selection.
- **Selection:** EVALUATE

### `spf13/cobra`
- **Package:** `github.com/spf13/cobra`
- **Capability:** C19 — Developer Tooling
- **Language/runtime:** Go / Go modules
- **Fit:** CLI command trees and completion, when the current codebase demonstrably needs it.
- **Anti-fit:** The program has only basic flags without a command hierarchy.
- **Fallback:** flag.
- **Compatibility:** Go >= 1.15; check deployment platform and integrations.
- **Maintenance:** Go module v1.10.2; upstream pushed 2026-07-11; activity does not prove long-term support.
- **License:** Apache-2.0
- **Official source:** [official registry or upstream](https://pkg.go.dev/github.com/spf13/cobra@v1.10.2); [upstream/manifest](https://github.com/spf13/cobra)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-01
- **Unknowns:** Security advisories: UNKNOWN; exact target support, comparative benchmarks and operational burden: NOT_MEASURED. Recheck before project selection.
- **Selection:** EVALUATE

### `golang/sync`
- **Package:** `golang.org/x/sync`
- **Capability:** C13 — Async & Messaging
- **Language/runtime:** Go / Go modules
- **Fit:** errgroup and concurrency control, when the current codebase demonstrably needs it.
- **Anti-fit:** sync.WaitGroup, context and channels already cover concurrency.
- **Fallback:** sync and context.
- **Compatibility:** Go >= 1.26.0; check deployment platform and integrations.
- **Maintenance:** Go module v0.24.0; upstream pushed 2026-10-15; activity does not prove long-term support.
- **License:** BSD-3-Clause
- **Official source:** [official registry or upstream](https://pkg.go.dev/golang.org/x/sync@v0.24.0); [upstream/manifest](https://github.com/golang/sync)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-01
- **Unknowns:** Go module currently declares minimum Go 1.26; do not adopt on an older toolchain. Security advisories: UNKNOWN; exact target support, comparative benchmarks and operational burden: NOT_MEASURED. Recheck before project selection.
- **Selection:** EVALUATE

### `golang/crypto`
- **Package:** `golang.org/x/crypto`
- **Capability:** C15 — Security & Cryptography
- **Language/runtime:** Go / Go modules
- **Fit:** Additional crypto primitives, when the current codebase demonstrably needs it.
- **Anti-fit:** Standard crypto packages already provide vetted required algorithms.
- **Fallback:** crypto standard packages.
- **Compatibility:** Go >= 1.26.0; check deployment platform and integrations.
- **Maintenance:** Go module v0.58.0; upstream pushed 2026-10-30; activity does not prove long-term support.
- **License:** BSD-3-Clause
- **Official source:** [official registry or upstream](https://pkg.go.dev/golang.org/x/crypto@v0.58.0); [upstream/manifest](https://github.com/golang/crypto); [Go vulnerability database](https://vuln.go.dev/ID/GO-2026-5932.json)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-02
- **Unknowns:** Go module currently declares minimum Go 1.26. GO-2026-5932 identifies `golang.org/x/crypto/openpgp` and subpackages as unmaintained and unsafe by design, with no fixed version; do not select those packages. For other imports, review advisory applicability by imported package and symbol rather than treating a module-level match as proof of exposure. Other security advisories and exact target support: UNKNOWN; comparative benchmarks and operational burden: NOT_MEASURED. Recheck before project selection.
- **Selection:** EVALUATE

### `openai/openai-go`
- **Package:** `github.com/openai/openai-go`
- **Capability:** C20 — AI & Integrations
- **Language/runtime:** Go / Go modules
- **Fit:** Typed OpenAI API calls, when the current codebase demonstrably needs it.
- **Anti-fit:** An existing SDK or vendor-neutral protocol satisfies the API contract.
- **Fallback:** net/http or existing SDK.
- **Compatibility:** Go >= 1.21; check deployment platform and integrations.
- **Maintenance:** Go module v1.12.0; upstream pushed 2026-10-31; activity does not prove long-term support.
- **License:** Apache-2.0
- **Official source:** [official registry or upstream](https://pkg.go.dev/github.com/openai/openai-go@v1.12.0); [upstream/manifest](https://github.com/openai/openai-go)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-01
- **Unknowns:** Security advisories: UNKNOWN; exact target support, comparative benchmarks and operational burden: NOT_MEASURED. Recheck before project selection.
- **Selection:** EVALUATE

### `modelcontextprotocol/go-sdk`
- **Package:** `github.com/modelcontextprotocol/go-sdk`
- **Capability:** C20 — AI & Integrations
- **Language/runtime:** Go / Go modules
- **Fit:** Official Go SDK for MCP servers, clients, transports and protocol negotiation.
- **Anti-fit:** Only simple REST/model calls; no MCP protocol exchange required.
- **Fallback:** net/http plus existing API client.
- **Compatibility:** Go >=1.25.0 in module v1.8.0; negotiate protocol/transport with clients; v1.7.0+ documents MCP 2026-07-28 and older versions.
- **Maintenance:** Go module v1.8.0; published 2026-09-04; active official SDK.
- **License:** Apache-2.0 for new/relicensed code, MIT for legacy contributions, and CC-BY-4.0 material in the repository; inspect file-level terms before redistribution.
- **Official source:** [official registry or upstream](https://pkg.go.dev/github.com/modelcontextprotocol/go-sdk@v1.8.0); [upstream/manifest](https://github.com/modelcontextprotocol/go-sdk)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-02
- **Unknowns:** 2026-07-28 HTTP transport has stateless-mode constraints. Tool auth, URL/SSRF policy, untrusted output, secret forwarding, bounded frames and cancellation require separate security design. Security advisory applicability: UNKNOWN (no pinned-version OSV/GHSA review); target-specific integration, performance and TCO: NOT_MEASURED. Recheck official metadata and transitive dependencies before project adoption.
- **Selection:** EVALUATE

### `grpc`
- **Package:** `google.golang.org/grpc`
- **Capability:** C09 — API & Networking
- **Language/runtime:** Go / Go modules
- **Fit:** Protobuf-based typed inter-service RPC and streaming when schemas, deadlines and streaming matter.
- **Anti-fit:** Simple public CRUD endpoints with JSON and low operational complexity.
- **Fallback:** net/http + JSON/OpenAPI.
- **Compatibility:** Go >=1.26.0 in module v1.85.0; validate protoc/protobuf generation, client/server versions and network proxies.
- **Maintenance:** Go module v1.85.0; published 2026-10-27; upstream gRPC-Go.
- **License:** Apache-2.0
- **Official source:** [official registry or upstream](https://pkg.go.dev/google.golang.org/grpc@v1.85.0); [upstream/manifest](https://github.com/grpc/grpc-go)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-02
- **Unknowns:** Service discovery, TLS/mTLS, retries, backpressure, observability and deployment complexity remain application concerns. Security advisory applicability: UNKNOWN (no pinned-version OSV/GHSA review); target-specific integration, performance and TCO: NOT_MEASURED. Recheck official metadata and transitive dependencies before project adoption.
- **Selection:** EVALUATE

### `otel/sdk`
- **Package:** `go.opentelemetry.io/otel/sdk`
- **Capability:** C18 — Observability
- **Language/runtime:** Go / Go modules
- **Fit:** Go tracing SDK for processing spans in independently observed network services; metrics use the separate `go.opentelemetry.io/otel/sdk/metric` module.
- **Anti-fit:** log/slog sufficient or managed instrumentation already handles required telemetry.
- **Fallback:** log/slog or existing SDK.
- **Compatibility:** Go >=1.26.0 in module v1.47.0; align with go.opentelemetry.io/otel APIs and configured exporter.
- **Maintenance:** Go module v1.47.0; published 2026-10-02; core SDK maintained.
- **License:** Apache-2.0 and BSD-3-Clause material per Go module license index; inspect applicable files for redistribution.
- **Official source:** [official registry or upstream](https://pkg.go.dev/go.opentelemetry.io/otel/sdk@v1.47.0); [upstream/manifest](https://github.com/open-telemetry/opentelemetry-go)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-02
- **Unknowns:** Metrics require the separate SDK module; this tracing SDK does not imply configured exporter/collector, sampling, PII redaction or end-to-end propagation. Security advisory applicability: UNKNOWN (no pinned-version OSV/GHSA review); target-specific integration, performance and TCO: NOT_MEASURED. Recheck official metadata and transitive dependencies before project adoption.
- **Selection:** EVALUATE

### `hibiken/asynq`
- **Package:** `github.com/hibiken/asynq`
- **Capability:** C13 — Async & Messaging
- **Language/runtime:** Go / Go modules
- **Fit:** Redis-backed at-least-once background jobs, retries and scheduled processing.
- **Anti-fit:** Only best-effort goroutines or an established broker/managed queue suffices.
- **Fallback:** context-controlled goroutines or existing durable queue.
- **Compatibility:** Go >=1.24.0 in module v0.26.0; requires Redis and worker lifecycle management.
- **Maintenance:** Go module v0.26.0; published 2026-02-03; verify release cadence before adoption.
- **License:** MIT
- **Official source:** [official registry or upstream](https://pkg.go.dev/github.com/hibiken/asynq@v0.26.0); [upstream/manifest](https://github.com/hibiken/asynq)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-02
- **Unknowns:** Redis durability depends on Redis configuration; at-least-once means duplicate deliveries; handlers need idempotency. No exactly-once claim. Security advisory applicability: UNKNOWN (no pinned-version OSV/GHSA review); target-specific integration, performance and TCO: NOT_MEASURED. Recheck official metadata and transitive dependencies before project adoption.
- **Selection:** EVALUATE

### `gin-contrib/cors`
- **Package:** `github.com/gin-contrib/cors`
- **Capability:** C09 — API & Networking
- **Language/runtime:** Go / Go modules
- **Fit:** Browser cross-origin policy with explicit origin and credential rules.
- **Anti-fit:** Same-origin APIs; cors.Default() allows all origins and is unsafe as a credentialed-origin policy.
- **Fallback:** Native Gin/net/http or trusted reverse-proxy CORS configuration.
- **Compatibility:** v1.7.10 declares Go >=1.26.10 and Gin v1.12.0; native Gin middleware, net/http compatible.
- **Maintenance:** Tagged v1.7.10, published 2026-10-31.
- **License:** MIT
- **Official source:** [official registry](https://pkg.go.dev/github.com/gin-contrib/cors@v1.7.10); [upstream tagged manifest](https://github.com/gin-contrib/cors/tree/v1.7.10)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-17
- **Unknowns:** Credential/origin combinations, proxy headers and preflight policy are app-owned; transitive advisories NOT_VERIFIED, TCO NOT_MEASURED.
- **Selection:** EVALUATE

### `gin-contrib/sessions`
- **Package:** `github.com/gin-contrib/sessions`
- **Capability:** C10 — Identity & Authorization
- **Language/runtime:** Go / Go modules
- **Fit:** Cookie-backed browser session middleware integrated with Gin when server-side session state is required.
- **Anti-fit:** Bearer-only API; many optional storage drivers/operations may exceed requirements.
- **Fallback:** Native cookie and application-owned simple session or existing identity provider.
- **Compatibility:** v1.1.2 declares Go >=1.26.0, Gin v1.12.0 and gorilla/sessions v1.4.0; verify selected session store.
- **Maintenance:** Tagged v1.1.2, published 2026-09-20; optional store adapters require review.
- **License:** MIT
- **Official source:** [official registry](https://pkg.go.dev/github.com/gin-contrib/sessions@v1.1.2); [upstream tagged manifest](https://github.com/gin-contrib/sessions/tree/v1.1.2)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-17
- **Unknowns:** CSRF, cookie flags, secret rotation, revocation and authorization are not automatic; store/transitive advisories NOT_VERIFIED, TCO NOT_MEASURED.
- **Selection:** EVALUATE

### `golang-jwt/jwt`
- **Package:** `github.com/golang-jwt/jwt/v5`
- **Capability:** C10 — Identity & Authorization
- **Language/runtime:** Go / Go modules
- **Fit:** JWT signing and cryptographic verification in an explicitly bearer-token-authenticated API.
- **Anti-fit:** Existing identity SDK handles verification, or stateful browser cookie sessions are preferable; JWT does not implement authorization.
- **Fallback:** Existing identity-provider verifier; never hand-roll JOSE.
- **Compatibility:** v5.3.1 declares Go >=1.21; framework-independent with Gin/net/http handlers.
- **Maintenance:** Tagged v5.3.1, published 2026-01-28.
- **License:** MIT
- **Official source:** [official registry](https://pkg.go.dev/github.com/golang-jwt/jwt/v5@v5.3.1); [upstream tagged manifest](https://github.com/golang-jwt/jwt/tree/v5.3.1)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-17
- **Unknowns:** GO-2025-3553/GHSA-mh63-6h87-95cp affected v5 before v5.2.2, not reviewed v5.3.1. Other advisories, key rotation and revocation NOT_VERIFIED; TCO NOT_MEASURED.
- **Selection:** EVALUATE

### `pressly/goose`
- **Package:** `github.com/pressly/goose/v3`
- **Capability:** C08 — Persistence
- **Language/runtime:** Go / Go modules
- **Fit:** SQL/Go migration versioning through CLI or library for evolving relational schema.
- **Anti-fit:** Existing migration owner covers schema rollout; do not import driver-heavy tooling into a runtime needlessly.
- **Fallback:** Existing migration runner or reviewed versioned SQL changes.
- **Compatibility:** v3.30.1 declares Go >=1.26.0; standalone CLI/library, no Gin coupling; select target database driver.
- **Maintenance:** Tagged v3.30.1, published 2026-11-12.
- **License:** MIT
- **Official source:** [official registry](https://pkg.go.dev/github.com/pressly/goose/v3@v3.30.1); [upstream tagged manifest](https://github.com/pressly/goose/tree/v3.30.1)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-17
- **Unknowns:** Broad go.mod database drivers, transactional DDL, locks, rollback and transitive advisories NOT_VERIFIED; TCO NOT_MEASURED.
- **Selection:** EVALUATE

### `redis/go-redis`
- **Package:** `github.com/redis/go-redis/v9`
- **Capability:** C16 — Performance & Cache
- **Language/runtime:** Go / Go modules
- **Fit:** Redis-backed cache/client operations if a real shared-state Redis service is already justified.
- **Anti-fit:** Local cache or PostgreSQL suffices; do not add Redis infrastructure only for trivial caching.
- **Fallback:** Bounded local cache, existing pgx or suitable installed Redis client.
- **Compatibility:** v9.23.0 declares Go >=1.26.0; Gin-independent and context-aware; check Redis server/pool compatibility.
- **Maintenance:** Tagged v9.23.0, published 2026-10-05; upstream raised Go floor to 1.26.
- **License:** BSD-2-Clause
- **Official source:** [official registry](https://pkg.go.dev/github.com/redis/go-redis/v9@v9.23.0); [upstream tagged manifest](https://github.com/redis/go-redis/tree/v9.23.0)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-17
- **Unknowns:** Redis failover, credentials, client caching staleness, pool limits and advisory resolution NOT_VERIFIED; workload/TCO NOT_MEASURED.
- **Selection:** EVALUATE

### `cenkalti/backoff`
- **Package:** `github.com/cenkalti/backoff/v5`
- **Capability:** C14 — Resilience & Errors
- **Language/runtime:** Go / Go modules
- **Fit:** Context-aware bounded exponential backoff for idempotent transient upstream calls.
- **Anti-fit:** One simple call or existing client policy sufficient; avoid blind retries on writes.
- **Fallback:** Small application-owned context-aware retry or existing HTTP client retries.
- **Compatibility:** v5.0.3 declares Go >=1.23; independent of Gin, receives Request.Context().
- **Maintenance:** Tagged v5.0.3, published 2025-07-23; no claim of newer release.
- **License:** MIT
- **Official source:** [official registry](https://pkg.go.dev/github.com/cenkalti/backoff/v5@v5.0.3); [upstream tagged manifest](https://github.com/cenkalti/backoff/tree/v5.0.3)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-17
- **Unknowns:** Retry budgets, idempotency, overload response and advisory applicability NOT_VERIFIED; performance/TCO NOT_MEASURED.
- **Selection:** EVALUATE

### `golang/time`
- **Package:** `golang.org/x/time`
- **Capability:** C14 — Resilience & Errors
- **Language/runtime:** Go / Go modules
- **Fit:** rate.Limiter token-bucket control for in-process rate budgets.
- **Anti-fit:** Distributed quotas or edge DDoS mitigation; local limiter state is not global.
- **Fallback:** Native deadlines or already deployed reverse-proxy rate policy.
- **Compatibility:** v0.16.0 declares Go >=1.26.0; rate package is Gin-independent and needs app middleware adaptation.
- **Maintenance:** Tagged v0.16.0, published 2026-08-19.
- **License:** BSD-3-Clause
- **Official source:** [official registry](https://pkg.go.dev/golang.org/x/time@v0.16.0); [upstream tagged manifest](https://github.com/golang/time/tree/v0.16.0)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-17
- **Unknowns:** Proxy trust, cardinality/eviction, multi-replica enforcement, advisories NOT_VERIFIED; TCO NOT_MEASURED.
- **Selection:** EVALUATE

### `testcontainers/testcontainers-go`
- **Package:** `github.com/testcontainers/testcontainers-go`
- **Capability:** C17 — Testing & QA
- **Language/runtime:** Go / Go modules
- **Fit:** Real disposable database/broker containers for integration tests where mocks miss protocol behavior.
- **Anti-fit:** Standard httptest sufficient, or CI cannot safely provide Docker-compatible container runtime.
- **Fallback:** testing/httptest or existing controlled integration environment.
- **Compatibility:** v0.45.0 declares Go >=1.26.0 and toolchain go1.26.10; requires container runtime and CI permissions.
- **Maintenance:** Tagged v0.45.0, published 2026-11-05; changes to some example modules require review.
- **License:** MIT
- **Official source:** [official registry](https://pkg.go.dev/github.com/testcontainers/testcontainers-go@v0.45.0); [upstream tagged manifest](https://github.com/testcontainers/testcontainers-go/tree/v0.45.0)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-17
- **Unknowns:** Direct go.mod uses moby/go-archive v0.3.3 (above v0.3.0 fix for GHSA-hfg8-hc9c-6c3h); complete graph/runtime NOT_VERIFIED, image/CI TCO NOT_MEASURED.
- **Selection:** EVALUATE

### `otelgin`
- **Package:** `go.opentelemetry.io/contrib/instrumentation/github.com/gin-gonic/gin/otelgin`
- **Capability:** C18 — Observability
- **Language/runtime:** Go / Go modules
- **Fit:** Gin inbound HTTP tracing middleware when an OTel pipeline already exists.
- **Anti-fit:** slog alone is sufficient, or an existing instrumentation layer already owns spans.
- **Fallback:** Existing OTel SDK with explicit instrumentation or slog.
- **Compatibility:** v0.72.0 declares Go >=1.26.0 and requires Gin v1.12.0, OTel SDK v1.47.0; inspect resolved graph.
- **Maintenance:** Tagged v0.72.0, published 2026-10-02; version alignment required.
- **License:** Apache-2.0 and BSD-3-Clause material; inspect redistribution terms
- **Official source:** [official registry](https://pkg.go.dev/go.opentelemetry.io/contrib/instrumentation/github.com/gin-gonic/gin/otelgin@v0.72.0); [upstream tagged manifest](https://github.com/open-telemetry/opentelemetry-go-contrib/tree/instrumentation/github.com/gin-gonic/gin/otelgin/v0.72.0)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-17
- **Unknowns:** No automatic metrics/exporter/collector/sampling or PII redaction; full transitive advisories NOT_VERIFIED; performance/TCO NOT_MEASURED.
- **Selection:** EVALUATE

## Selection boundary

VERIFIED is scoped to official package identity, metadata and advertised function; it is NOT a security endorsement, benchmark result or production approval. PARTIAL means essential metadata is unresolved. EVALUATE permits comparison only, BLOCKED requires filling compatibility/license gaps first. No automatic migration.

[Index](README.md) · [Languages](../languages/README.md) · [Frameworks](../frameworks/README.md) · [Decisions](../decisions/README.md)
