# Railway

> **Provider SSOT.** Service claims and price evidence are recorded per offering below. `SOURCE_LINKED_SNAPSHOT` is not a current-price verification.

**Offerings:** 1 · **Pillars:** [01](../pillars/01-compute-runtime/README.md)

| Service | Primary pillar | Free kind | Free tier/credits | Paid pricing | Caveat | Official source | Evidence status | Evidence checked |
|---|---|---|---|---|---|---|---|---|
| Railway | 01 | `PERMANENT_AFTER_TRIAL` | New account: up to 30-day trial with one-time $5 credit, then Free plan with $1/month non-rollover credit; no card required. After trial: 1 project, 3 services, 1 vCPU, 0.5 GB RAM, 1 GB ephemeral disk, one persistent volume up to 0.5 GB. | Hobby $5/month minimum includes $5 usage; Pro $20/month minimum includes $20. Published usage rates: RAM $10/GB-month, CPU $20/vCPU-month, egress $0.05/GB, volume storage $0.00000006/GB-second. | Deployment filesystem is ephemeral; attached volume persists and is metered. Trial resources differ from Free and unverified trial accounts can have restricted outbound networking; trial volumes are deleted 30 days after credit expiry. | [Current pricing and rates](https://railway.com/pricing) · [Plan resources](https://docs.railway.com/pricing/plans) · [Free trial](https://docs.railway.com/pricing/free-trial) · [Volumes](https://docs.railway.com/volumes/reference) · [Deployment storage](https://docs.railway.com/deployments/reference) | `VERIFIED` | 2026-11-01 |

## Evidence & maintenance

- Score: `NOT_EVALUATED` — workload, legal/security checks, benchmarks and price region are not yet supplied.
- Update pricing and source **here only**; pillar pages should never duplicate provider prices.
- [Evaluation matrix](../docs/01-evaluation-matrix.md) · [Lifecycle](../docs/lifecycle.md)
