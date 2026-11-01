# LangSmith

> **Provider SSOT.** Service claims and price evidence are recorded per offering below. `SOURCE_LINKED_SNAPSHOT` is not a current-price verification.

**Offerings:** 1 · **Pillars:** [09](../pillars/09-observability-analytics/README.md)

| Service | Primary pillar | Free kind | Free tier/credits | Paid pricing | Caveat | Official source | Evidence status | Evidence checked |
|---|---|---|---|---|---|---|---|---|
| LangSmith | 09 | PERMANENT | Developer is $0/seat (one seat max), includes 5K base traces/month then pay-as-you-go. Plus includes one free small Serverless deployment. Developer plan includes 8 LSU of Sandbox usage/month and is limited to 10 sandboxes. | Developer $0/seat, one seat, 5K base traces/month; Plus $39/seat/month, 10K base traces; Enterprise custom. Plus includes one small serverless deployment. The pricing calculator values 1 LSU at $1. Fleet has 7/37 LSU included by plan and Engine uses about 7–45 LSU/run. Sandbox meters: 0.0576 LSU/vCPU-hour, 0.01845 LSU/GiB-hour memory and 0.000123 LSU/GiB-hour storage, billed per second. Trace overage and 180-day extended-trace price are not public. | RC1/RC2/RC4 — Current meter is LangChain Standard Unit (LSU), not old LCU amount; LSU is not a trace. Base traces retain 14 days; extended traces retain 180 days for an unpublished fee. No numerical trace-overage rate asserted. | [LangChain pricing](https://www.langchain.com/pricing) | UNVERIFIED | 2026-11-01 |

## Evidence & maintenance

- Score: `NOT_EVALUATED` — workload, legal/security checks, benchmarks and price region are not yet supplied.
- Update pricing and source **here only**; pillar pages should never duplicate provider prices.
- [Evaluation matrix](../docs/01-evaluation-matrix.md) · [Lifecycle](../docs/lifecycle.md)
