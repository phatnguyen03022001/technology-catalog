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
- **Official source:** [official registry or upstream](https://pkg.go.dev/golang.org/x/crypto@v0.58.0); [upstream/manifest](https://github.com/golang/crypto)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-01
- **Unknowns:** Go module currently declares minimum Go 1.26; review cryptographic advisories. Security advisories: UNKNOWN; exact target support, comparative benchmarks and operational burden: NOT_MEASURED. Recheck before project selection.
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

## Selection boundary

VERIFIED is scoped to official package identity, metadata and advertised function; it is NOT a security endorsement, benchmark result or production approval. PARTIAL means essential metadata is unresolved. EVALUATE permits comparison only, BLOCKED requires filling compatibility/license gaps first. No automatic migration.

[Index](README.md) · [Languages](../languages/README.md) · [Frameworks](../frameworks/README.md) · [Decisions](../decisions/README.md)
