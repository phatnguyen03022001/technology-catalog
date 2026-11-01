# Neon

> **Provider SSOT.** Service claims and price evidence are recorded per offering below. `SOURCE_LINKED_SNAPSHOT` is not a current-price verification.

**Offerings:** 1 · **Pillars:** [02](../pillars/02-databases-data/README.md)

| Service | Primary pillar | Free kind | Free tier/credits | Paid pricing | Caveat | Official source | Evidence status | Evidence checked |
|---|---|---|---|---|---|---|---|---|
| Neon Lakebase Postgres | 02 | `PERMANENT` | Free: no card; up to 100 projects, each with 100 CU-hours/month, 1 GB Postgres storage, 10 branches and 5 GB public network transfer/month. If a project exceeds 1 GB Postgres storage or projects exceed 20 GB total, storage-increasing operations fail until space is freed. | Launch has no monthly minimum: $0.106/CU-hour and $0.35/GB-month Postgres storage; 500 GB public transfer/project/month included then $0.10/GB; extra branches above 10 cost $0.002/hour (~$1.50/branch-month); retained history is $0.20/GB-month; snapshots and scheduled backups are $0.09/GB-month each. Typical intermittent 1 GB workload: $15/month on Launch, estimate not a floor. | Neon now brands its database Lakebase Postgres. Free quotas stop applying after upgrade; actual cost also depends on compute sizing, autosuspend, branch/history retention and egress. | [Pricing and free-plan limits](https://neon.com/pricing) · [Plans and billing](https://neon.com/docs/introduction/about-billing) | `VERIFIED` | 2026-11-01 |

## Evidence & maintenance

- Score: `NOT_EVALUATED` — workload, legal/security checks, benchmarks and price region are not yet supplied.
- Update pricing and source **here only**; pillar pages should never duplicate provider prices.
- [Evaluation matrix](../docs/01-evaluation-matrix.md) · [Lifecycle](../docs/lifecycle.md)
