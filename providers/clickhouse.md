# ClickHouse

> **Provider SSOT.** Service claims and price evidence are recorded per offering below. `SOURCE_LINKED_SNAPSHOT` is not a current-price verification.

**Offerings:** 3 · **Pillars:** [02](../pillars/02-databases-data/README.md), [09](../pillars/09-observability-analytics/README.md)

| Service | Primary pillar | Free kind | Free tier/credits | Paid pricing | Caveat | Official source | Evidence status | Evidence checked |
|---|---|---|---|---|---|---|---|---|
| ClickHouse Cloud | 02 | ONE_TIME_CREDIT | New organizations receive $300 usage credit for 30 days; no permanent cloud free plan established. | Current N. Virginia starts: Basic $53/month, Scale $437/month; storage $25.30/TB-month; compute $0.2181/unit-hour Basic and $0.2985 Scale. Public egress starts $0.1152/GB; inter-region $0.0312/GB. | Rates are configuration-dependent starts, not fixed monthly bills. Select region/SKU and distinguish public from inter-region transfer. | [ClickHouse pricing](https://clickhouse.com/pricing) | VERIFIED | 2026-11-01 |
| ClickStack OSS | 09 | SELF_HOSTED | ClickStack is an open-source observability stack; component licenses include ClickHouse Apache-2.0, HyperDX MIT and OpenTelemetry Collector Apache-2.0. | No vendor subscription price for the self-managed OSS components; compute, storage, networking and operations are customer-provided. | ClickStack is the stack; HyperDX is its UI/component, not a separate provider. Retention, HA, upgrades and on-call operations remain in TCO. | [ClickStack product](https://clickhouse.com/clickstack) · [Repository and licenses](https://github.com/ClickHouse/ClickStack) | VERIFIED | 2026-11-01 |
| Managed ClickStack | 09 | ONE_TIME_CREDIT | New ClickHouse Cloud organizations receive $300 usage credit for 30 days; account-level credit, not a recurring observability quota. | No separate public Managed ClickStack SKU or starting monthly cost was reproduced. Its ClickHouse Cloud billing meters in N. Virginia (us-east-1) list Basic storage at $25.30/TB-month and compute at $0.2181/unit-hour; Managed ClickStack’s total depends on ingest, queries, retention and egress. Public egress starts at $0.1152/GB and inter-region transfer at $0.0312/GB. | Managed ClickStack is GA and runs on ClickHouse Cloud; the Cloud meter prices are regional reference components, not a fixed ClickStack bill. Do not use the unsupported $53/month starting amount or conflate this with separate private-preview ClickStack Cloud. | [Managed ClickStack GA](https://clickhouse.com/blog/open-house-2026-day-1) · [ClickStack product](https://clickhouse.com/clickstack) · [Cloud pricing](https://clickhouse.com/pricing) | UNVERIFIED | — |

## Evidence & maintenance

- Score: `NOT_EVALUATED` — workload, legal/security checks, benchmarks and price region are not yet supplied.
- Update pricing and source **here only**; pillar pages should never duplicate provider prices.
- [Evaluation matrix](../docs/01-evaluation-matrix.md) · [Lifecycle](../docs/lifecycle.md)
