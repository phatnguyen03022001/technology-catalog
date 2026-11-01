# Aiven

> **Provider SSOT.** Service claims and price evidence are recorded per offering below. `SOURCE_LINKED_SNAPSHOT` is not a current-price verification.

**Offerings:** 2 · **Pillars:** [02](../pillars/02-databases-data/README.md), [05](../pillars/05-cache-traditional-search/README.md)

| Service | Primary pillar | Free kind | Free tier/credits | Paid pricing | Caveat | Official source | Evidence status | Evidence checked |
|---|---|---|---|---|---|---|---|---|
| Aiven PostgreSQL | 02 | `PERMANENT` | Permanent free, no card: 1 CPU, 1 GB RAM, 1 GB disk, max 20 connections; one service/type/org, no SLA. | Developer from $5/month; Hobbyist from $12/month; Startup from $75/month. Plan and region select resources. | Old Startup-4 ~$19 amount is obsolete. Free resources may be disabled for inactivity; exact availability/region and current plan limits matter. | [PostgreSQL free tier](https://aiven.io/docs/products/postgresql/concepts/pg-free-tier) · [Current pricing](https://aiven.io/pricing/postgresql) | `VERIFIED` | 2026-11-01 |
| Aiven Valkey | 05 | PERMANENT | Free no-card indefinitely: 1 CPU, 1 GB RAM with maxmemory at 50%; no SLA, may be stopped for inactivity. | Developer $15/month; Business HA from $70/month. Resources and region affect price. | The old $30–$60 HA estimate is withdrawn. Free is resource-limited and may be suspended; confirm current node shape/region before purchase. | [Valkey pricing](https://aiven.io/pricing/valkey) · [Free Valkey tier](https://aiven.io/docs/products/valkey/concepts/valkey-free-tier) | VERIFIED | 2026-11-01 |

## Evidence & maintenance

- Score: `NOT_EVALUATED` — workload, legal/security checks, benchmarks and price region are not yet supplied.
- Update pricing and source **here only**; pillar pages should never duplicate provider prices.
- [Evaluation matrix](../docs/01-evaluation-matrix.md) · [Lifecycle](../docs/lifecycle.md)
