# DEC-WEB-001 — React fullstack web product

**Status:** CONDITIONAL_NOT_PRODUCTION · **Reviewed:** 2026-11-01 · **Workload:** REFERENCE_SCENARIO_NOT_MEASURED.

## Workload & candidates
Assume product needs React UI, SEO/server rendering, forms, auth and some server-side routes; team can maintain TypeScript. Compare **Next.js** vs **NestJS API + separate React UI**. A simpler static frontend remains a fallback when dynamic SSR is not needed.

| Candidate | Evidence-backed fit | Costs/risks to verify |
|---|---|---|
| [Next.js](../frameworks/nextjs.md) | App Router with server/client components; Node deployment supports feature set | SSR caching, server/client secrets, adapter support, rendering CPU, egress |
| [NestJS](../frameworks/nestjs.md) + separate UI | Explicit controllers/modules/DI for standalone API | Two deployables, contracts, auth/cookies, tracing, coordination |
| Static UI / existing stack | Smaller footprint when SSR unnecessary | Dynamic SEO, auth flows and content freshness |

## Hard gates & unknown evidence
- Functional: **PASS conditional on SSR need**; Next official docs support rendering/routing.
- Security/privacy: **UNKNOWN** until auth, server/client boundary and data retention tested.
- Legal/licensing: **UNKNOWN** for full dependency graph and provider terms (framework MIT alone insufficient).
- Cost/TCO: **UNKNOWN** — no traffic, region, request/compute or hosting SKU; benchmark **NOT_MEASURED**.
- Portability/recovery: **UNKNOWN** until deployment, export, rebuild and rollback on target are tested.

## Decision & falsification
**Conditional choice: Next.js** for one product with combined web UI + routes. Choose NestJS + separate React frontend if business requires independently scaled backend or team-module boundaries demonstrated in actual workload. Choose static UI when SSR/dynamic needs disappear. **Not production-approved.**

## Verification / TCO / fallback
Measure same auth+render+API traffic across candidates, p95/p99, memory, build/deploy and server/edge costs. TCO = one host account fee + metered compute/storage/egress + any separately hosted API + ops; obtain pricing from [Vercel](../providers/vercel.md) or alternative [provider records](../providers/README.md), not this decision. Gate release on secrets isolation, integration tests, CI/deploy rollback, monitored error budget. Preserve API/data migration path; fallback to existing frontend/backend if gate fails.

## Official evidence
- [Next App Router](https://nextjs.org/docs/app)
- [Next deployment modes](https://nextjs.org/docs/pages/getting-started/deploying)
- [Nest controllers/modules](https://docs.nestjs.com/controllers)
