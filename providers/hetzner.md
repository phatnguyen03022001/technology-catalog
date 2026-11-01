# Hetzner

> **Provider SSOT.** Service claims and price evidence are recorded per offering below. `SOURCE_LINKED_SNAPSHOT` is not a current-price verification.

**Offerings:** 2 · **Pillars:** [01](../pillars/01-compute-runtime/README.md), [03](../pillars/03-storage-media/README.md)

| Service | Primary pillar | Free kind | Free tier/credits | Paid pricing | Caveat | Official source | Evidence status | Evidence checked |
|---|---|---|---|---|---|---|---|---|
| Hetzner Cloud | 01 | `UNKNOWN` | Free credits or allowances not independently verified | Instance and storage rates vary by product and region; prior CX23 amount is an unrechecked snapshot | RC2/RC3/RC6 — Prices may exclude VAT and region adjustments; check current product calculator. | [Hetzner Cloud Pricing](https://www.hetzner.com/cloud) | STALE | 2026-11-01 |
| Hetzner Object Storage | 03 | `NONE` | No free tier: the current pricing description says an hourly account base fee applies whenever any bucket is active. The base includes 1 TB of storage (up to 744 TB-hours in a 31-day month) and 1 TB of egress per account/month. Ingress, S3 requests and internal eu-central traffic are free. Unused monthly quota expires. | Current English FAQ displays a base rate of €0.0104 per active-bucket hour, excluding VAT, capped monthly; the cap amount is omitted from the page text. The 2024 launch card lists $5.99/€4.99 monthly and excess storage at $0.0080/€0.0067 per TB-hour plus egress $1.20/€1 per TB. Treat those launch rates as historical until the current cap is reproduced. | RC2/RC3/RC6 — Live FAQ hourly price and older fixed monthly card do not establish one current cap; the page varies by selected currency/VAT. Included quota is confirmed, but the current cap/excess schedule is not fully rendered. Locations: FSN1, NBG1, HEL1; small objects have a 64 KB billing minimum. | [Current Object Storage pricing](https://www.hetzner.com/storage/object-storage/) · [Pricing and usage units](https://docs.hetzner.com/storage/object-storage/overview/) · [Launch rate card (2024)](https://www.hetzner.com/pressroom/object-storage/) · [June 2026 adjustment scope](https://www.hetzner.com/pressroom/standardization-and-price-adjustment-of-our-server-products/) | `UNVERIFIED` | 2026-11-01 |

## Evidence & maintenance

- Score: `NOT_EVALUATED` — workload, legal/security checks, benchmarks and price region are not yet supplied.
- Update pricing and source **here only**; pillar pages should never duplicate provider prices.
- [Evaluation matrix](../docs/01-evaluation-matrix.md) · [Lifecycle](../docs/lifecycle.md)
