# axum — Rust / Tokio

**Reviewed:** 2026-11-01 · [Framework index](README.md)

## Fit
Async HTTP APIs in Rust requiring extractors, routing and Tower middleware atop Tokio/hyper, especially for Rust-native services.

## Anti-fit
CPU-only native application without HTTP interface; sync CLI; team lacking Rust requirements where simpler existing framework suffices.

## Compatibility
axum documentation describes Tokio/hyper integration, not generic-runtime independence. Check the selected crate version’s **MSRV**, feature flags, Tokio, Tower and Rust target; build/release artifact characteristics vary by OS/toolchain.

## Maturity & maintenance
Published Rustdoc, source and MIT license; inspect release cadence, advisory history, async dependency graph, migration/breaking changes and maintainer support before committing production.

## Licensing
axum repository is **MIT**; audit its dependencies and optional native/TLS crates separately.

## Operational / test evidence needed
Extractors reject malformed data, request body limits, authorization, backpressure, cancellation and timeouts, blocking code off async executors, memory and p99, structured tracing and graceful shutdown.

## Official evidence
- [axum docs / runtime requirements](https://docs.rs/axum/latest/axum/)
- [axum source/license](https://github.com/tokio-rs/axum)
- [Tokio runtime](https://tokio.rs/tokio/tutorial)
