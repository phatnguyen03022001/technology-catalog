# Vapor — Swift / Server

**Reviewed:** 2026-11-01 · [Framework index](README.md)

## Fit
Swift server-side HTTP APIs or backends when Swift team/toolchain reuse and server deployment constraints are confirmed.

## Anti-fit
Browser frontend or iOS UI (use SwiftUI for UI); backend with mature Go/TS/Python SDKs but incomplete Swift ecosystem support; adding Swift server merely for matching mobile language.

## Compatibility
Vapor HTTP server uses SwiftNIO, supports HTTP/1 and HTTP/2; verify supported Swift toolchain, Linux/macOS build target, SDK/driver support and graceful termination on pinned versions. SwiftUI/UIKit are **not** prerequisites for Vapor on Linux.

## Maturity & maintenance
Official docs/source and server community exist; inspect releases, supported Swift compiler versions, library maintenance and security advisories before production.

## Licensing
Vapor source is **MIT**; Swift dependencies and commercial deployment terms are distinct.

## Operational / test evidence needed
HTTP contract tests, SwiftPM pinned builds, Linux CI, concurrency/cancellation, DB drivers, errors, tracing, TLS/proxy handling, container build and rollback. Compare p95/RAM/TCO on the actual workload.

## Official evidence
- [Vapor docs](https://docs.vapor.codes/)
- [Vapor HTTP server](https://docs.vapor.codes/advanced/server/)
- [Vapor source/license](https://github.com/vapor/vapor)
