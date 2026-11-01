# NestJS — TypeScript / Node.js

**Reviewed:** 2026-11-01 · [Framework index](README.md)

## Fit
Server-side TypeScript APIs needing explicit modules, controllers, providers and dependency injection across a growing team; useful for uniform conventions over multiple feature modules.

## Anti-fit
Small API/worker where Node standard APIs or existing lightweight framework already meet requirements; pure React UI; cases where decorator/module ceremony outweighs maintenance value.

## Compatibility
Node.js server environment, TS config/decorators, package compatibility and HTTP adapter must match target. DTO types alone do **not** validate untrusted runtime JSON; configure and test runtime validation. Verify Node/TS versions against pinned Nest release.

## Maturity & maintenance
Published documentation and maintained source are available; actual release lifecycle, module interoperability, vulnerability advisories and production target must be checked at selection time. Do not derive superiority from architectural pattern.

## Licensing
Nest docs state **MIT** for framework; confirm license and compatibility of optional plugins, adapters and commercial infrastructure independently.

## Operational / test evidence needed
Module boundaries, auth/guards, request validation, injection scopes, shutdown/cancellation, contract tests, memory/throughput, logs/traces, deployment rollback and TCO for the chosen host.

## Official evidence
- [Controllers and modules](https://docs.nestjs.com/controllers)
- [Providers and dependency injection](https://docs.nestjs.com/providers)
- [Nest licensing/support](https://docs.nestjs.com/support)
