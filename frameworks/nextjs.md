# Next.js — TypeScript / React

**Reviewed:** 2026-11-01 · [Framework index](README.md)

## Fit
React-based fullstack product with server rendering, app routing, layouts, server/client component boundaries, SEO or dynamic routes. Official App Router docs describe Server Components and file-system routing.

## Anti-fit
Pure JSON API with no browser UI; completely static site where a small generator suffices; existing stable non-React UI. Do not add Next.js solely because backend is TypeScript.

## Compatibility
Next.js is **not** itself a JS runtime; target Node/server or static export/adapters separately. Official deployment docs specify full feature support on Node server and limited features for static export. Node baseline shown as 20.9 in reviewed installation docs; **recheck per chosen Next release**. Confirm edge/adapter support, ESM, native packages, secrets and route behavior on actual target.

## Maturity & maintenance
First-party documentation and source available; release/security cadence, supported versions, migration effort and specific SDK compatibility **need release-scoped review**. Avoid declaring long-term support without a verified support policy.

## Licensing
Next.js source advertises **MIT**; verify pinned release and third-party packages separately. Hosting, commercial SDKs and managed functions have separate terms.

## Operational / test evidence needed
SSR/cache correctness, auth/session, server/client data leakage, API contract tests, hydration, p95/cold starts, memory, hosting/egress and rollback. No production performance claim without workload benchmark.

## Official evidence
- [Next.js App Router](https://nextjs.org/docs/app)
- [Deployment modes](https://nextjs.org/docs/pages/getting-started/deploying)
- [Installation requirements](https://nextjs.org/docs/app/getting-started/installation)
- [Next.js source/license](https://github.com/vercel/next.js)
