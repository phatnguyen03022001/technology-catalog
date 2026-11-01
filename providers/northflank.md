# Northflank

> **Provider SSOT.** Service claims and price evidence are recorded per offering below. `SOURCE_LINKED_SNAPSHOT` is not a current-price verification.

**Offerings:** 1 · **Pillars:** [01](../pillars/01-compute-runtime/README.md)

| Service | Primary pillar | Free kind | Free tier/credits | Paid pricing | Caveat | Official source | Evidence status | Evidence checked |
|---|---|---|---|---|---|---|---|---|
| Northflank | 01 | `LIMITED_FREE` | Sandbox needs no card and includes up to $20/month in resources, 2 services, 2 jobs and 1 database/add-on; not intended for production. | PAYG: $0,01667/vCPU-hour + $0,00833/GB-hour memory, storage/egress riêng. Smallest published compute $12/tháng cho 0,5 vCPU/1 GB. | The sandbox resource allowance does not establish production eligibility. As of 2026-11-01, Northflank's status page still marks an open major security incident after reports of unauthorized use of user-provided AI API keys. Northflank advises assuming environment variables and secrets were exposed; revoke/rotate workload, secret-group and global credentials, review provider billing, and disable public add-on exposure. Do not treat the listed pricing as a production recommendation while incident remediation remains open. | [Northflank pricing](https://northflank.com/pricing) · [Billing documentation](https://northflank.com/docs/v1/application/billing/pricing-on-northflank) · [Security incident status](https://status.northflank.com/cmvv0rn5a092f14rutwccodpp) | `VERIFIED` | 2026-11-01 |

## Evidence & maintenance

- Score: `NOT_EVALUATED` — workload, legal/security checks, benchmarks and price region are not yet supplied.
- Update pricing and source **here only**; pillar pages should never duplicate provider prices.
- [Evaluation matrix](../docs/01-evaluation-matrix.md) · [Lifecycle](../docs/lifecycle.md)
