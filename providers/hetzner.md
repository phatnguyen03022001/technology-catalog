# Hetzner

> **Provider SSOT.** Service claims and price evidence are recorded per offering below. `SOURCE_LINKED_SNAPSHOT` is not a current-price verification.

**Offerings:** 2 · **Pillars:** [01](../pillars/01-compute-runtime/README.md), [03](../pillars/03-storage-media/README.md)

| Service | Primary pillar | Free kind | Free tier/credits | Paid pricing | Caveat | Official source | Evidence status | Evidence checked |
|---|---|---|---|---|---|---|---|---|
| Hetzner Cloud | 01 | `UNKNOWN` | Free credits or allowances not independently verified | Instance and storage rates vary by product and region; prior CX23 amount is an unrechecked snapshot | RC2/RC3/RC6 — Prices may exclude VAT and region adjustments; check current product calculator. | [Hetzner Cloud Pricing](https://www.hetzner.com/cloud) | STALE | 2026-11-01 |
| Hetzner Object Storage | 03 | NONE | No free tier: an account with any active bucket pays a base fee, including empty buckets. Base includes 1 TB storage (up to 744 TB-hours in 31 days) and 1 TB egress/account/month; unused quota does not carry over. Ingress and S3 API requests are free. | EUR (excluding VAT): €0.0104 per active-bucket hour, capped at €6.49/month/account. Includes 1 TB storage and 1 TB egress monthly; overage storage €0.0087/TB-hour and external egress €1.00/TB. Applies to eligible European Object Storage locations (FSN1/NBG1/HEL1). | The €6.49 monthly cap is for the account base fee, not an unlimited-storage bill. Usage over included storage/egress, monthly VAT, and bucket-active hours remain separate; billing is hourly, and quota does not roll over. 64 KB minimum billable size for small objects. Previous 2024 €4.99/$5.99 prices are historical. | [Current Object Storage pricing and FAQ](https://www.hetzner.com/storage/object-storage/) · [Billing/quotas](https://docs.hetzner.com/storage/object-storage/overview/) | VERIFIED | 2026-11-01 |

## Evidence & maintenance

- Score: `NOT_EVALUATED` — workload, legal/security checks, benchmarks and price region are not yet supplied.
- Update pricing and source **here only**; pillar pages should never duplicate provider prices.
- [Evaluation matrix](../docs/01-evaluation-matrix.md) · [Lifecycle](../docs/lifecycle.md)
