# Akamai

> **Provider SSOT.** Service claims and price evidence are recorded per offering below. `SOURCE_LINKED_SNAPSHOT` is not a current-price verification.

**Offerings:** 3 · **Pillars:** [01](../pillars/01-compute-runtime/README.md), [03](../pillars/03-storage-media/README.md), [04](../pillars/04-networking-edge/README.md)

| Service | Primary pillar | Free kind | Free tier/credits | Paid pricing | Caveat | Official source | Evidence status | Evidence checked |
|---|---|---|---|---|---|---|---|---|
| Akamai CDN | 04 | UNKNOWN | No service-specific recurring free allowance was established from current public sources. | Current price is not published in the reviewed product/documentation pages; obtain an account quote before treating a price as known. | Active CDN product; do not infer a free quota or sales-only price from other Akamai services. | [Akamai CDN](https://www.akamai.com/content-delivery-network) · [Delivery docs](https://techdocs.akamai.com/platform-basics/docs/content-delivery) | UNVERIFIED | — |
| Akamai Cloud Compute | 01 | `ONE_TIME_CREDIT` | An Akamai AI-build campaign advertises US$100 credit for eligible new Cloud customers who sign up with a valid payment method; credit expires 60 days after activation and excludes GPU services. One code per business; prior redemption disqualifies another; codes expire after one year and amount is discretionary. | Jakarta example: Nanode 1 GB, $5/month or $0.0075/hour, 1 shared CPU, 1 GB RAM, 25 GB SSD and 1 TB transfer; egress overage $0.005/GB. Prices may vary by region. | Campaign credit is conditional and not a permanent free tier; standard promo terms prohibit Marketplace/third-party services. Check product/region and transfer limits before estimating cost. | [Cloud CPU pricing](https://www.akamai.com/cloud/pricing/cpu) · [AI-build credit terms](https://www.akamai.com/lp/build-ai-apps-agents) · [Promotion rules](https://www.akamai.com/legal/promotion-redemption-rules-conditions) | `VERIFIED` | 2026-11-01 |
| Akamai Object Storage | 03 | `UNKNOWN` | No object-storage-specific free quota or confirmed eligibility for the separate Akamai Cloud signup campaign is published on the storage rate card. | $5/month, prorated, includes 250 GB; additional storage $0.02/GB-month (regional overage can vary). The account receives a 1 TB/month global outbound-transfer pool; overage $0.005/GB except Jakarta $0.015/GB and São Paulo $0.007/GB. | Storage overage and transfer depend on data center; the signup promotion is not a standing storage allowance. Verify region and account eligibility. | [Object Storage pricing](https://www.akamai.com/cloud/pricing/object-storage) · [Promotion rules](https://www.akamai.com/legal/promotion-redemption-rules-conditions) | `VERIFIED` | 2026-11-01 |

## Evidence & maintenance

- Score: `NOT_EVALUATED` — workload, legal/security checks, benchmarks and price region are not yet supplied.
- Update pricing and source **here only**; pillar pages should never duplicate provider prices.
- [Evaluation matrix](../docs/01-evaluation-matrix.md) · [Lifecycle](../docs/lifecycle.md)
