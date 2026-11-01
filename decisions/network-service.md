# DEC-NET-001 — HTTP gateway / network service

**Status:** CONDITIONAL_NOT_PRODUCTION · **Reviewed:** 2026-11-01 · **Workload:** REFERENCE_SCENARIO_NOT_MEASURED.

## Workload & candidates
Assume a small HTTP gateway with auth, request validation, timeout, retries and modest traffic; team already knows Go. Compare **Go net/http**, **Gin**, **Rust axum**.

| Candidate | Evidence-backed fit | Costs/risks to verify |
|---|---|---|
| Go `net/http` | Standard routing/handlers; minimal dependencies | Explicit middleware, validation and testing burden |
| [Gin](../frameworks/gin.md) | Binding, route grouping, middleware for Go APIs | Extra dependency and behavioral conventions |
| [axum](../frameworks/axum.md) | Rust routing/extractors, Tower middleware, Tokio/hyper | Different language/toolchain, migration and maintainability cost |

## Hard gates & unknown evidence
- Functional: **PASS conditional** for basic HTTP routing (stdlib).
- Security/privacy: **UNKNOWN** — auth/secrets, request limits, outbound network policy unverified.
- Legal/licensing: **UNKNOWN** — full deployed dependency/license matrix.
- Cost/TCO: **UNKNOWN**, no workload request rate, CPU/RAM benchmark or hosting quote; benchmark **NOT_MEASURED**.
- Portability/recovery: **UNKNOWN** until binary/target validation and rollback tested.

## Decision & falsification
**Conditional choice: Go net/http first**, add Gin only if its middleware/binding substantially reduces repeated project code. Choose axum when Rust-native components, native performance constraints or a measured platform requirement justify multi-language ownership. No claim that Go outperforms Rust; **not production-approved**.

## Verification / TCO / fallback
Compare equal auth+fanout+retry payloads at concurrency and error injection, p95/p99/RAM, cancellation and shutdown. Include engineer time, CPU/memory hosting, egress, observability and operations from [provider SSOT](../providers/README.md). Block deploy on race/timeout/idempotency regression tests; rollback to previous image/binary. If stdlib service accumulates duplicated routing/validation, revisit Gin before adding a new runtime.

## Official evidence
- [Go net/http](https://pkg.go.dev/net/http)
- [Gin middleware](https://gin-gonic.com/en/docs/middleware/using-middleware/)
- [Gin binding](https://gin-gonic.com/en/docs/binding/)
- [axum documentation](https://docs.rs/axum/latest/axum/)
