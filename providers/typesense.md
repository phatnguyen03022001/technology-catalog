# Typesense

> **Provider SSOT.** Service claims and price evidence are recorded per offering below. `SOURCE_LINKED_SNAPSHOT` is not a current-price verification.

**Offerings:** 2 · **Pillars:** [05](../pillars/05-cache-traditional-search/README.md)

| Service | Primary pillar | Free kind | Free tier/credits | Paid pricing | Caveat | Official source | Evidence status | Evidence checked |
|---|---|---|---|---|---|---|---|---|
| Typesense Cloud | 05 | ONE_TIME_CREDIT | One-time per-account free allowance: 720 cluster-hours and 10 GB bandwidth for selected configurations. A payment card is required to avoid interruption when the allowance ends; this does not recur monthly. | The public Typesense Cloud calculator currently shows an EXAMPLE default cluster of $0.03/hour ($21.60 for 720 hours) and $0.09/GB outbound bandwidth (first 10 GB one-time free). This is not a universal price or sufficient SKU/region-specific TCO: CPU, RAM, disk, HA, region and chosen configuration may differ; authenticated billing:read pricing API is required for exact SKU rates. | RC2/RC6 — Current public calculator example is reproducible but does not identify a universal production SKU/region; authenticated SKU pricing is still needed. The 720 cluster-hours + 10 GB bandwidth is ONE-TIME per-account allowance, not monthly. Unused but running clusters still incur instance charges. | [Current Cloud calculator](https://cloud.typesense.org/pricing/calculator) · [One-time free tier](https://cloud-help.typesense.org/article/how-does-the-free-tier-work) · [Price API authentication](https://typesense.org/docs/cloud-management-api/v1/prices.html) | UNVERIFIED | 2026-11-01 |
| Typesense OSS | 05 | SELF_HOSTED | GPL-3.0 software can be self-hosted under its license; compute and operations remain payable. | No hosted Cloud pricing applies to the self-hosted OSS distribution. | The Cloud account credit/free node-hours do not apply to OSS deployment. | [Typesense source/license](https://github.com/typesense/typesense) · [Cloud free tier](https://cloud-help.typesense.org/article/how-does-the-free-tier-work) | VERIFIED | 2026-11-01 |

## Evidence & maintenance

- Score: `NOT_EVALUATED` — workload, legal/security checks, benchmarks and price region are not yet supplied.
- Update pricing and source **here only**; pillar pages should never duplicate provider prices.
- [Evaluation matrix](../docs/01-evaluation-matrix.md) · [Lifecycle](../docs/lifecycle.md)
