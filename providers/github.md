# GitHub

> **Provider SSOT.** Service claims and price evidence are recorded per offering below. `SOURCE_LINKED_SNAPSHOT` is not a current-price verification.

**Offerings:** 2 · **Pillars:** [08](../pillars/08-devops-delivery/README.md)

| Service | Primary pillar | Free kind | Free tier/credits | Paid pricing | Caveat | Official source | Evidence status | Evidence checked |
|---|---|---|---|---|---|---|---|---|
| GitHub Actions | 08 | PERMANENT | GitHub Free private repositories receive $12/month compute allowance, not a fixed 2,000 minutes. Public hosted runners and self-hosted runner use are free; artifact storage Free is 500 MB with separate cache quota. | For Linux 2-core at $0.006/min, $12 equals 2,000 minutes; Windows/macOS rates differ. Usage beyond included credit bills at runner-specific rates. | Monthly credit’s minute-equivalent depends on runner OS/size; artifacts and cache have separate storage limits. | [Included usage](https://docs.github.com/en/billing/reference/product-usage-included) · [Runner rates](https://docs.github.com/en/enterprise-cloud%40latest/billing/reference/actions-runner-pricing) | VERIFIED | 2026-11-01 |
| GitHub Container Registry (GHCR) | 08 | PERMANENT | Container-image storage and bandwidth on GHCR are currently free. | No current container-image storage/bandwidth price asserted; GitHub states it will provide at least one month notice before policy changes. | GitHub Packages 500 MB/1 GB limits do not apply to container images; keep image packages distinct from other packages. | [GitHub Packages billing](https://docs.github.com/en/billing/concepts/product-billing/github-packages) | VERIFIED | 2026-11-01 |

## Evidence & maintenance

- Score: `NOT_EVALUATED` — workload, legal/security checks, benchmarks and price region are not yet supplied.
- Update pricing and source **here only**; pillar pages should never duplicate provider prices.
- [Evaluation matrix](../docs/01-evaluation-matrix.md) · [Lifecycle](../docs/lifecycle.md)
