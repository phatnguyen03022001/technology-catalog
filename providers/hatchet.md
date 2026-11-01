# Hatchet

> **Provider SSOT.** Service claims and price evidence are recorded per offering below. `SOURCE_LINKED_SNAPSHOT` is not a current-price verification.

**Offerings:** 1 · **Pillars:** [06](../pillars/06-messaging-async/README.md)

| Service | Primary pillar | Free kind | Free tier/credits | Paid pricing | Caveat | Official source | Evidence status | Evidence checked |
|---|---|---|---|---|---|---|---|---|
| Hatchet Cloud | 06 | LIMITED_FREE | The current pricing page conflicts internally: its headline, FAQ and footer say 1M runs and 1M events are free each month and that no card is needed to start, while its detailed comparison table lists a No-card tier capped at 2,000 runs/day and 2,000 events/day versus a Card-on-file tier with 1M runs/month and 1M events/month included. The same comparison lists 500 MB storage/1-day retention on No-card and 10 GB/7-day retention on Card-on-file. Confirm account-specific eligibility before relying on either quota. | Card-on-file PAYG tier: after the included 1M runs and 1M events/month, $30/M runs and $5/M events. Its comparison table includes 10 GB active storage then $0.03/GB-hour overage, and 10 GB logs/traces then $0.0004/GB-hour. | The first-party page does not reconcile its headline/FAQ with the detailed No-card/Card-on-file split; status remains UNVERIFIED pending clarification. Failed runs count, retries do not add runs, and exceeding limits drops tasks. Storage is described both as a daily payload allowance and a per-GB-hour meter; confirm the effective meter for long-running workloads. Data-plane regions: Oregon, N. Virginia, Ireland and Sydney. | [Hatchet pricing](https://hatchet.run/pricing) | UNVERIFIED | — |

## Evidence & maintenance

- Score: `NOT_EVALUATED` — workload, legal/security checks, benchmarks and price region are not yet supplied.
- Update pricing and source **here only**; pillar pages should never duplicate provider prices.
- [Evaluation matrix](../docs/01-evaluation-matrix.md) · [Lifecycle](../docs/lifecycle.md)
