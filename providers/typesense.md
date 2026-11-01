# Typesense

> **Provider SSOT.** Service claims and price evidence are recorded per offering below. `SOURCE_LINKED_SNAPSHOT` is not a current-price verification.

**Offerings:** 2 · **Pillars:** [05](../pillars/05-cache-traditional-search/README.md)

| Service | Primary pillar | Free kind | Free tier/credits | Paid pricing | Caveat | Official source | Evidence status | Evidence checked |
|---|---|---|---|---|---|---|---|---|
| Typesense Cloud | 05 | ONE_TIME_CREDIT | One-time per-account free allowance: 720 cluster-hours and 10 GB bandwidth for selected configurations. A payment card is required to avoid interruption when the allowance ends; this does not recur monthly. | Cluster price is determined by region, RAM, vCPU, GPU, disk, HA and network; exact SKU pricing API requires an authenticated `billing:read` key. Published Oregon sample is illustrative, not a current universal rate. | RC2/RC6 — The free quota is a one-time account lifetime allowance. Current region/SKU rate cannot be reproduced without billing access; running clusters bill by hour even with no traffic. | [Free tier](https://cloud-help.typesense.org/article/how-does-the-free-tier-work) · [Billing process](https://cloud-help.typesense.org/article/billing-process) · [Cloud price API](https://typesense.org/docs/cloud-management-api/v1/prices.html) | UNVERIFIED | 2026-11-01 |
| Typesense OSS | 05 | SELF_HOSTED | GPL-3.0 software can be self-hosted under its license; compute and operations remain payable. | No hosted Cloud pricing applies to the self-hosted OSS distribution. | The Cloud account credit/free node-hours do not apply to OSS deployment. | [Typesense source/license](https://github.com/typesense/typesense) · [Cloud free tier](https://cloud-help.typesense.org/article/how-does-the-free-tier-work) | VERIFIED | 2026-11-01 |

## Evidence & maintenance

- Score: `NOT_EVALUATED` — workload, legal/security checks, benchmarks and price region are not yet supplied.
- Update pricing and source **here only**; pillar pages should never duplicate provider prices.
- [Evaluation matrix](../docs/01-evaluation-matrix.md) · [Lifecycle](../docs/lifecycle.md)
