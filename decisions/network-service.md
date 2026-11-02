# DEC-NET-001 — HTTP gateway / network service

**Status:** CONDITIONAL_NOT_PRODUCTION · **Reviewed:** 2026-11-02 · **Workload:** REFERENCE_SCENARIO_NOT_MEASURED.

## Workload & candidates
Assume a small HTTP gateway with auth, request validation, timeout, retries and modest traffic; team already knows Go. Compare **Go net/http**, **Gin**, **Rust axum**.

| Candidate | Evidence-backed fit | Costs/risks to verify |
|---|---|---|
| Go `net/http` | Standard routing/handlers; minimal dependencies | Explicit middleware, validation and testing burden |
| [Gin](../frameworks/gin.md) | Binding, route grouping, middleware for Go APIs | Extra dependency and behavioral conventions |
| [axum](../frameworks/axum.md) | Rust routing/extractors, Tower middleware, Tokio/hyper | Different language/toolchain, migration and maintainability cost |
| Go gRPC (`google.golang.org/grpc`) | Typed Protobuf inter-service contracts and bidirectional streaming when needed | Schema/codegen, HTTP/2 proxy/load balancer, TLS, deadlines, debugging, reflection, versioning and operations |

For HTTP/JSON clients and modest request/response workloads, `net/http` is the default; OpenAPI can provide typed contracts without gRPC. Add gRPC only for a concrete typed cross-service or streaming requirement after testing protocol compatibility, streaming backpressure, observability, and deployment environment. Neither HTTP nor gRPC inherently guarantees lower latency or better scalability. [gRPC-Go library record](../libraries/go.md) owns package metadata.

## Hard gates & unknown evidence
- Functional: **PASS conditional** for basic HTTP routing (stdlib).
- Security/privacy: **UNKNOWN** — auth/secrets, request limits, outbound network policy unverified.
- Legal/licensing: **UNKNOWN** — full deployed dependency/license matrix.
- Cost/TCO: **UNKNOWN**, no workload request rate, CPU/RAM benchmark or hosting quote; benchmark **NOT_MEASURED**.
- Portability/recovery: **UNKNOWN** until binary/target validation and rollback tested.

## Decision & falsification
**Conditional choice: Go net/http first**, add Gin only if its middleware/binding substantially reduces repeated project code. Choose axum when Rust-native components, native performance constraints or a measured platform requirement justify multi-language ownership. No claim that Go outperforms Rust; **not production-approved**.

## Verification / TCO / fallback
Compare equivalent HTTP/JSON vs Protobuf/gRPC request/response and real streaming loads (when needed), with matching authentication, error handling, compression and proxies. Compare auth+fanout+retry payloads at concurrency and error injection, p95/p99/RAM, cancellation and shutdown. Include engineer time, CPU/memory hosting, egress, observability and operations from [provider SSOT](../providers/README.md). Block deploy on race/timeout/idempotency regression tests; rollback to previous image/binary. If stdlib service accumulates duplicated routing/validation, revisit Gin before adding a new runtime.

## Official evidence
- [Go net/http](https://pkg.go.dev/net/http)
- [Gin middleware](https://gin-gonic.com/en/docs/middleware/using-middleware/)
- [Gin binding](https://gin-gonic.com/en/docs/binding/)
- [axum documentation](https://docs.rs/axum/latest/axum/)
