# Vercel

> **Provider SSOT.** Service claims and price evidence are recorded per offering below. `SOURCE_LINKED_SNAPSHOT` is not a current-price verification.

**Offerings:** 3 · **Pillars:** [01](../pillars/01-compute-runtime/README.md), [03](../pillars/03-storage-media/README.md), [08](../pillars/08-devops-delivery/README.md)

| Service | Primary pillar | Free kind | Free tier/credits | Paid pricing | Caveat | Official source | Evidence status | Evidence checked |
|---|---|---|---|---|---|---|---|---|
| Vercel Hosting/Functions | 01 | `PERMANENT` | Hobby $0/mo: 100 GB Fast Data Transfer, 1M Serverless Invocations, 4 Active CPU-hours and up to 200 projects; Hobby is noncommercial only. | Pro $20/user-month includes $20 usage credit; Serverless Functions overage $0.60/M invocations. Fast Data Transfer is regional, published at $0.15–$0.35/GB depending on region, rather than a universal $0.15/GB. | Commercial sites require a paid plan. Hard usage limits/overages and region-specific transfer pricing affect TCO; verify the target deployment regions. | [Vercel pricing](https://vercel.com/pricing) · [Hobby terms](https://vercel.com/docs/plans/hobby) · [Regional pricing](https://vercel.com/docs/pricing/regional-pricing) | `SOURCE_LINKED_SNAPSHOT` | — |
| Vercel Blob | 03 | `PERMANENT` | Hobby: 1 GB-month storage, 10K simple ops, 2K advanced ops and 10 GB transfer; service limited by plan and region. | Pro has per-seat floor plus regional usage. Published example meters include Advanced Ops $5/M; transfer, Edge Requests and Fast Origin Transfer are separate. | Hobby is noncommercial and has no paid overage; blob access can be restricted after quota breach. Region and complete line items are unresolved in this row. | [Blob usage and pricing](https://vercel.com/docs/vercel-blob/usage-and-pricing) · [Regional pricing](https://vercel.com/docs/pricing/regional-pricing) | `SOURCE_LINKED_SNAPSHOT` | — |
| Vercel CI | 08 | LIMITED_FREE | Hobby: 100 deployments/day, one concurrent build and 45-minute maximum/deploy; personal/noncommercial projects only. | Pro $20/user/month includes $20 usage credit. Standard On-Demand Concurrent Build is $0.014/minute; normal Standard build is not separately priced. Enhanced $0.030/minute; Turbo $0.126/minute. | Do not apply concurrent-build per-minute prices to all Vercel builds; plan terms and usage credit determine bill. | [Limits](https://vercel.com/docs/limits) · [Hobby](https://vercel.com/docs/plans/hobby) · [Build pricing](https://vercel.com/docs/builds/managing-builds) | VERIFIED | 2026-11-01 |

## Evidence & maintenance

- Score: `NOT_EVALUATED` — workload, legal/security checks, benchmarks and price region are not yet supplied.
- Update pricing and source **here only**; pillar pages should never duplicate provider prices.
- [Evaluation matrix](../docs/01-evaluation-matrix.md) · [Lifecycle](../docs/lifecycle.md)
