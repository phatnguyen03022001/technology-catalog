# Daytona

> **Provider SSOT.** Service claims and price evidence are recorded per offering below. `SOURCE_LINKED_SNAPSHOT` is not a current-price verification.

**Offerings:** 1 · **Pillars:** [01](../pillars/01-compute-runtime/README.md)

| Service | Primary pillar | Free kind | Free tier/credits | Paid pricing | Caveat | Official source | Evidence status | Evidence checked |
|---|---|---|---|---|---|---|---|---|
| Daytona | 01 | `TIME_LIMITED_TRIAL` | Signup includes $200 in compute credits. The official page does not state an expiration date; do not label the credit as expiring. Tier 1 limits: 10 vCPU, 20 GiB RAM, 30 GiB storage; Tier 2 requires card and $25 top-up. | Pay per second: CPU $0.0504/vCPU-hour; RAM $0.0162/GiB-hour; storage $0.000108/GiB-hour after 5 GiB. Region and CPU class can multiply rates. | RC4/RC6 — Billing differs by release: current/default Daytona docs bill reserved disk for stopped/paused sandboxes (even if CPU/RAM stop billing); Daytona v2 ALPHA docs say stopped/paused/deleted are not metered, with CPU/RAM guarantees and measured disk while running. Do not apply v2 alpha semantics to current default/v0 accounts. Credit expiry/reset remains unestablished; verify account version, tier and region. | [Pricing](https://www.daytona.io/pricing) · [Current/default billing](https://www.daytona.io/docs/billing) · [v2 alpha billing](https://www.daytona.io/docs/en/v2/billing/) · [Limits](https://www.daytona.io/docs/limits) | UNVERIFIED | 2026-11-01 |

## Evidence & maintenance

- Score: `NOT_EVALUATED` — workload, legal/security checks, benchmarks and price region are not yet supplied.
- Update pricing and source **here only**; pillar pages should never duplicate provider prices.
- [Evaluation matrix](../docs/01-evaluation-matrix.md) · [Lifecycle](../docs/lifecycle.md)
