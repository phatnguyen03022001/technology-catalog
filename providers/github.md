# GitHub

> **Provider SSOT.** Nguồn từ snapshot **2026-11-01**, có URL chính thức đã qua kiểm chứng (VERIFIED). Chỉ dùng để nghiên cứu; xác minh lại trước khi mua hoặc triển khai production.

**Offerings:** 2 · **Pillars:** [08](../pillars/08-devops-delivery/README.md)

| Service | Primary pillar | Free kind | Free tier/credits | Paid pricing | Caveat | Official source |
|---|---|---|---|---|---|---|
| GitHub Actions | 08 | `PERMANENT` | Public: Unlimited mins; Private: 2,000 mins/mo + 500 MB storage; Self-hosted runners $0 | Team $4/user/mo (3K mins); Extra Linux $0.006/min | macOS runs burn 10x minutes; private caches count toward storage | [GitHub Pricing](https://github.com/pricing) |
| GitHub Container Registry (GHCR) | 08 | `PERMANENT` | Public images: 100% free storage & transfer; Private: shared 500 MB storage + 1 GB egress | Shared storage $0.25/GB/mo; Egress $0.50/GB | Private containers quickly blow past 500 MB; requires spending cap | [GHCR Billing](https://docs.github.com/en/billing/managing-billing-for-your-products/managing-billing-for-github-packages/about-billing-for-github-packages) |

## Evidence & maintenance

- Evidence: `VERIFIED`; live re-verification completed on 2026-11-01 via multi-agent research fanout.
- Score: `NOT_EVALUATED` — workload, legal/security checks, benchmarks and price region are not yet supplied.
- Update pricing and source **here only**; pillar pages should never duplicate provider prices.
- [Evaluation matrix](../docs/01-evaluation-matrix.md) · [Lifecycle](../docs/lifecycle.md)
