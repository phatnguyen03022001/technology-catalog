# Rust — curated libraries

**Reviewed:** 2026-11-01. Reusable code packages only, never framework or managed service production approvals.

## Dependency choice

- **Standard library first:** std networking, threads and types.
- **Add:** only for a documented capability that standard library and current dependencies do not sufficiently provide.
- **Keep:** do not migrate merely because a package appears in the catalog or has a newer release.
- **Remove/replace:** prove need, test compatibility and preserve a rollback path.
- **Verify:** target toolchain, platform, license, security advisories, dependency tree and realistic workload.

## Entries

### `tokio`
- **Package:** `tokio`
- **Capability:** Async
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
- **Capability:** Serialization
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
- **Capability:** HTTP
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
- **Capability:** Database
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
- **Capability:** Observability
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
- **Capability:** CLI
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
- **Capability:** Errors
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
- **Capability:** Testing
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
- **Capability:** Crypto
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

## Selection boundary

VERIFIED is scoped to official package identity, metadata and advertised function; it is NOT a security endorsement, benchmark result or production approval. PARTIAL means essential metadata is unresolved. EVALUATE permits comparison only, BLOCKED requires filling compatibility/license gaps first. No automatic migration.

[Index](README.md) · [Languages](../languages/README.md) · [Frameworks](../frameworks/README.md) · [Decisions](../decisions/README.md)
