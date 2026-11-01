# DigitalOcean

> **Provider SSOT.** Service claims and price evidence are recorded per offering below. `SOURCE_LINKED_SNAPSHOT` is not a current-price verification.

**Offerings:** 2 · **Pillars:** [01](../pillars/01-compute-runtime/README.md), [03](../pillars/03-storage-media/README.md)

| Service | Primary pillar | Free kind | Free tier/credits | Paid pricing | Caveat | Official source | Evidence status | Evidence checked |
|---|---|---|---|---|---|---|---|---|
| DigitalOcean Droplets | 01 | `ONE_TIME_CREDIT` | Default signup credit is $5, expires 90 days after signup, and requires a valid payment method before creating Droplets; referral/promotional offers may differ and are not a recurring quota. | Basic 512 MiB/1 vCPU/10 GiB SSD with 500 GiB transfer: $4/month ($0.00595/hour); since 2026-01-01, billed per second with a 60-second/$0.01 minimum. | Unmanaged VPS; backups and traffic beyond included transfer may add cost. Confirm region and any promo eligibility on the account. | [Droplet pricing](https://www.digitalocean.com/pricing/droplets) · [Signup-credit terms](https://docs.digitalocean.com/platform/billing/signup-credit/) | `VERIFIED` | 2026-11-01 |
| DigitalOcean Spaces | 03 | `ONE_TIME_CREDIT` | New-account $200 credits are account-level promotion, eligibility/expiry apply; not recurring Spaces free tier. | Spaces $5/month includes 250 GiB storage and 1 TiB outbound transfer; overage $0.02/GiB storage and $0.01/GiB transfer. Cold Storage $0.007/GiB-month plus retrieval/retention terms. | Credit does not make Spaces permanently free; check account eligibility. Price includes monthly minimum and specified bundled capacity. | [Spaces price details](https://docs.digitalocean.com/products/spaces/details/pricing/) · [Current pricing](https://www.digitalocean.com/pricing/spaces-object-storage) | `VERIFIED` | 2026-11-01 |

## Evidence & maintenance

- Score: `NOT_EVALUATED` — workload, legal/security checks, benchmarks and price region are not yet supplied.
- Update pricing and source **here only**; pillar pages should never duplicate provider prices.
- [Evaluation matrix](../docs/01-evaluation-matrix.md) · [Lifecycle](../docs/lifecycle.md)
