# Dragonfly

> **Provider SSOT.** Service claims and price evidence are recorded per offering below. `SOURCE_LINKED_SNAPSHOT` is not a current-price verification.

**Offerings:** 2 · **Pillars:** [05](../pillars/05-cache-traditional-search/README.md)

| Service | Primary pillar | Free kind | Free tier/credits | Paid pricing | Caveat | Official source | Evidence status | Evidence checked |
|---|---|---|---|---|---|---|---|---|
| Dragonfly OSS | 05 | SELF_HOSTED | Dragonfly OSS is source-available under BSL 1.1, not OSI-approved open source; self-host license does not remove infrastructure/operations costs. | No charge for the OSS deployment license under BSL terms; Dragonfly Cloud is a distinct service. | BSL 1.1 converts to Apache 2.0 on 2030-11-01; do not conflate OSS license with managed Cloud plan. | [Dragonfly license](https://github.com/dragonflydb/dragonfly/blob/main/LICENSE.md) · [Cloud pricing](https://www.dragonflydb.io/pricing) | VERIFIED | 2026-11-01 |
| Dragonfly Cloud | 05 | `TIME_LIMITED_TRIAL` | Pricing page offers a free trial but does not publish its duration, resource allowance or payment-card requirement. | Flex starts at $36/month. On-demand starts at $8/GB-month plus cloud-provider network charges; Business starts at $2,000/month. The on-demand calculator assumes 20% compression savings versus Redis. | RC2/RC4/RC6 — Trial details are unresolved; do not treat it as a permanent free tier. Managed Dragonfly Cloud is separate from self-hosted BSL 1.1 Dragonfly OSS. | [Dragonfly Cloud pricing](https://www.dragonflydb.io/pricing) | UNVERIFIED | 2026-11-01 |

## Evidence & maintenance

- Score: `NOT_EVALUATED` — workload, legal/security checks, benchmarks and price region are not yet supplied.
- Update pricing and source **here only**; pillar pages should never duplicate provider prices.
- [Evaluation matrix](../docs/01-evaluation-matrix.md) · [Lifecycle](../docs/lifecycle.md)
