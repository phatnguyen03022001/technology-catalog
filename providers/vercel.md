# Vercel

> **Provider SSOT.** Service claims and price evidence are recorded per offering below. `SOURCE_LINKED_SNAPSHOT` is not a current-price verification.

**Offerings:** 3 · **Pillars:** [01](../pillars/01-compute-runtime/README.md), [03](../pillars/03-storage-media/README.md), [08](../pillars/08-devops-delivery/README.md)

| Service | Primary pillar | Free kind | Free tier/credits | Paid pricing | Caveat | Official source | Evidence status | Evidence checked |
|---|---|---|---|---|---|---|---|---|
| Vercel Hosting/Functions | 01 | LIMITED_FREE | Hobby is $0 for personal, noncommercial use: 100 GB Fast Data Transfer, 1M Serverless Invocations, 4 Active CPU-hours and up to 200 projects; exceeding hard limits can pause usage. Pro is $20/user/month with $20 usage credit. | Regional pricing (USD, varies by region): Fast Data Transfer $0.15–$0.35/GB, CDN requests $2–$3.20/million, CPU $0.128–$0.221/hour, memory $0.0106–$0.0183/GB-hour. Remove unsupported $0.60/million invocation claim. | RC2/RC4/RC7 — Hobby is not commercial-use eligible. Exact deployment cost depends on region, runtime and traffic; the row does not claim a universal invocation overage. | [Vercel pricing](https://vercel.com/pricing) · [Hobby plan](https://vercel.com/docs/plans/hobby) · [Regional pricing](https://vercel.com/docs/pricing/regional-pricing) | UNVERIFIED | 2026-11-01 |
| Vercel Blob | 03 | LIMITED_FREE | Hobby: 1 GB-month storage, 10K simple operations, 2K advanced operations and 10 GB transfer; Hobby is noncommercial and quotas are shared with other Vercel project services. No overage bill; after limit, access can be disabled for up to 30 days. | Regional on-demand rates in USD: storage $0.023–$0.041/GB-month; simple operations $0.35–$0.56/million; advanced operations $4.50–$7.00/million; Blob Data Transfer $0.05–$0.117/GB. Pro requires a $20/month platform fee (one deploying seat included) and includes $20/month of usage credit; extra deploying seats are $20/month each. | Rates depend on deployment region. This row lists Blob meters only; CDN Requests and Fast Origin Transfer are separate charges. Pro platform fee is a team-level minimum, with usage credit applied to usage; Hobby is noncommercial and the included quota is shared across services in a project. | [Blob usage and pricing](https://vercel.com/docs/vercel-blob/usage-and-pricing) · [Pro plan pricing and seats](https://vercel.com/docs/plans/pro-plan) · [Regional pricing](https://vercel.com/docs/pricing/regional-pricing) | VERIFIED | 2026-11-01 |
| Vercel CI | 08 | LIMITED_FREE | Hobby: 100 deployments/day, one concurrent build and 45-minute maximum/deploy; personal/noncommercial projects only. | Pro $20/user/month includes $20 usage credit. Standard On-Demand Concurrent Build is $0.014/minute; normal Standard build is not separately priced. Enhanced $0.030/minute; Turbo $0.126/minute. | Do not apply concurrent-build per-minute prices to all Vercel builds; plan terms and usage credit determine bill. | [Limits](https://vercel.com/docs/limits) · [Hobby](https://vercel.com/docs/plans/hobby) · [Build pricing](https://vercel.com/docs/builds/managing-builds) | VERIFIED | 2026-11-01 |

## Billing scope & TCO

- **Pro platform fee is at team scope**, not per Hosting/Functions, Blob or CI. The $20/month base includes one deploying seat and $20 monthly usage credit; additional deploying seats and separately metered product usage can add costs.
- The usage credit is applied **once** across eligible team usage; do not subtract $20 from each service or count the platform fee three times. Included allowances, regional rates, commercial Hobby restrictions and per-product meters remain distinct.
- Official evidence: [Pro plan billing](https://vercel.com/docs/plans/pro-plan).

## Evidence & maintenance

- Score: `NOT_EVALUATED` — workload, legal/security checks, benchmarks and price region are not yet supplied.
- Update pricing and source **here only**; pillar pages should never duplicate provider prices.
- [Evaluation matrix](../docs/01-evaluation-matrix.md) · [Lifecycle](../docs/lifecycle.md)
