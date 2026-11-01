# Typesense

> **Provider SSOT.** Service claims and price evidence are recorded per offering below. `SOURCE_LINKED_SNAPSHOT` is not a current-price verification.

**Offerings:** 2 · **Pillars:** [05](../pillars/05-cache-traditional-search/README.md)

| Service | Primary pillar | Free kind | Free tier/credits | Paid pricing | Caveat | Official source | Evidence status | Evidence checked |
|---|---|---|---|---|---|---|---|---|
| Typesense Cloud | 05 | ONE_TIME_CREDIT | Select configurations receive the first 720 cluster-hours and 10 GB bandwidth free once per account lifetime; the allowance does not recur monthly. | Pay-as-you-go cluster fees are configuration-specific and charged per running hour; bandwidth is typically $0.09–$0.12/GB by region. The public price API requires a billing:read key, so no exact entry SKU is reproducible here. | Dedicated nodes continue to accrue hourly charges while running, even without traffic; billing is weekly by default. Do not model the allowance as recurring. | [Free-tier terms](https://cloud-help.typesense.org/article/how-does-the-free-tier-work) · [Billing process](https://cloud-help.typesense.org/article/billing-process) · [Cloud pricing API](https://typesense.org/docs/cloud-management-api/v1/prices.html) | `UNVERIFIED` | — |
| Typesense OSS | 05 | SELF_HOSTED | GPL-3.0 software can be self-hosted under its license; compute and operations remain payable. | No hosted Cloud pricing applies to the self-hosted OSS distribution. | The Cloud account credit/free node-hours do not apply to OSS deployment. | [Typesense source/license](https://github.com/typesense/typesense) · [Cloud free tier](https://cloud-help.typesense.org/article/how-does-the-free-tier-work) | VERIFIED | 2026-11-01 |

## Evidence & maintenance

- Score: `NOT_EVALUATED` — workload, legal/security checks, benchmarks and price region are not yet supplied.
- Update pricing and source **here only**; pillar pages should never duplicate provider prices.
- [Evaluation matrix](../docs/01-evaluation-matrix.md) · [Lifecycle](../docs/lifecycle.md)
