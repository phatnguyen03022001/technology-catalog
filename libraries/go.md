# Go — curated libraries

**Reviewed:** 2026-11-01. Reusable code packages only, never framework or managed service production approvals.

## Dependency choice

- **Standard library first:** net/http, encoding/json, sync, log/slog, testing and flag.
- **Add:** only for a documented capability that standard library and current dependencies do not sufficiently provide.
- **Keep:** do not migrate merely because a package appears in the catalog or has a newer release.
- **Remove/replace:** prove need, test compatibility and preserve a rollback path.
- **Verify:** target toolchain, platform, license, security advisories, dependency tree and realistic workload.

## Entries

### `go-chi/chi`
- **Package:** `github.com/go-chi/chi/v5`
- **Capability:** HTTP
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
- **Capability:** Database
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
- **Capability:** Observability
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
- **Capability:** Testing
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
- **Capability:** Testing
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
- **Capability:** CLI
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
- **Capability:** Async
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
- **Capability:** Crypto
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
- **Capability:** AI
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
- **Capability:** Agentic / MCP
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
- **Capability:** RPC / streaming
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
- **Capability:** Telemetry SDK
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
- **Capability:** Durable jobs
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

## Selection boundary

VERIFIED is scoped to official package identity, metadata and advertised function; it is NOT a security endorsement, benchmark result or production approval. PARTIAL means essential metadata is unresolved. EVALUATE permits comparison only, BLOCKED requires filling compatibility/license gaps first. No automatic migration.

[Index](README.md) · [Languages](../languages/README.md) · [Frameworks](../frameworks/README.md) · [Decisions](../decisions/README.md)
