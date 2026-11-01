# Gin — Go

**Reviewed:** 2026-11-01 · [Framework index](README.md)

## Fit
Go HTTP APIs requiring ergonomic route grouping, JSON binding/validation and configurable middleware beyond standard library needs.

## Anti-fit
Small Go server fully served by `net/http` and `ServeMux`; native Apple/browser UI; library-only networking that does not need a web router.

## Compatibility
Builds on Go `net/http`; verify minimum supported Go version, binding validator behavior, middleware order, proxies/timeouts and target Go toolchain for pinned Gin release.

## Maturity & maintenance
Public framework documentation and source; no fixed support promise inferred. Inspect active releases/security advisories, dependency constraints and ownership before production.

## Licensing
Gin source is **MIT**; inspect dependencies/license policy separately.

## Operational / test evidence needed
Input binding with explicit tags, error/status behavior, middleware/auth scope, timeouts, `context` cancellation, handler tests, race tests, DB connection pooling, latency/memory and deploy rollback.

## Official evidence
- [Gin middleware](https://gin-gonic.com/en/docs/middleware/using-middleware/)
- [Gin binding](https://gin-gonic.com/en/docs/binding/)
- [Gin source/license](https://github.com/gin-gonic/gin)
- [Go standard HTTP package](https://pkg.go.dev/net/http)
