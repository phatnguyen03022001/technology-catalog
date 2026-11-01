# Vercel

> **Provider SSOT.** Service claims and price evidence are recorded per offering below. `SOURCE_LINKED_SNAPSHOT` is not a current-price verification.

**Offerings:** 3 · **Pillars:** [01](../pillars/01-compute-runtime/README.md), [03](../pillars/03-storage-media/README.md), [08](../pillars/08-devops-delivery/README.md)

| Service | Primary pillar | Free kind | Free tier/credits | Paid pricing | Caveat | Official source | Evidence status | Evidence checked |
|---|---|---|---|---|---|---|---|---|
| Vercel Hosting/Functions | 01 | `PERMANENT` | Hobby $0/mo: 100 GB Fast Data Transfer, 1M Serverless Invocations, 4 Active CPU-hrs, 200 projects | Pro $20/user/mo (includes $20 usage credit, then PAYG: bandwidth $0.15/GB, $0.60/M invocations) | Non-commercial only (strict ToS); monetized sites require Pro ($20/seat/mo); hard cutoff on overages | [Vercel Pricing](https://vercel.com/pricing) | `SOURCE_LINKED_SNAPSHOT` | — |
| Vercel Blob | 03 | `PERMANENT` | 1 GB storage/tháng; 10k Simple Ops; 2k Advanced Ops; 10 GB data transfer | Pro $20/seat/tháng base + usage (Storage $0,023/GB, Simple $0,40/1M, Egress $0,05/GB) | Hobby strictly non-commercial; hết quota bị dừng operations; Pro cần trả $20/seat/tháng | [Vercel Blob Pricing](https://vercel.com/docs/storage/vercel-blob/usage-and-pricing) | `SOURCE_LINKED_SNAPSHOT` | — |
| Vercel CI | 08 | `PERMANENT` | 100 deployments/day; 1 concurrent build; 45-min max timeout | Pro $20/seat/mo + usage ($0.007–$0.014/build min) | Strictly non-commercial on Hobby; tied to Vercel deployment targets | [Vercel Pricing](https://vercel.com/pricing) | `SOURCE_LINKED_SNAPSHOT` | — |

## Evidence & maintenance

- Score: `NOT_EVALUATED` — workload, legal/security checks, benchmarks and price region are not yet supplied.
- Update pricing and source **here only**; pillar pages should never duplicate provider prices.
- [Evaluation matrix](../docs/01-evaluation-matrix.md) · [Lifecycle](../docs/lifecycle.md)
