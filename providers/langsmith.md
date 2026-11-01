# LangSmith

> **Provider SSOT.** Service claims and price evidence are recorded per offering below. `SOURCE_LINKED_SNAPSHOT` is not a current-price verification.

**Offerings:** 1 · **Pillars:** [09](../pillars/09-observability-analytics/README.md)

| Service | Primary pillar | Free kind | Free tier/credits | Paid pricing | Caveat | Official source | Evidence status | Evidence checked |
|---|---|---|---|---|---|---|---|---|
| LangSmith | 09 | PERMANENT | Developer is $0/seat (one seat max), includes 5K base traces/month then pay-as-you-go. Plus includes one free small Serverless deployment. | Plus is $39/seat/month with 10K base traces/month and unlimited seats; Enterprise is custom. Usage-metered Fleet, Engine, and Sandbox products use LangChain Standard Units (LSU) at $1/LSU, with product-specific rates. Trace overage is pay-as-you-go, but its current rate is not reproduced on the public price page. | An LSU is not a trace. The listed $1/LSU meter applies across products and must not be presented as a trace overage rate; one trace can contain many events. Base traces retain 14 days; extended traces retain 180 days for an additional, unpublished fee. | [LangChain pricing](https://www.langchain.com/pricing) | UNVERIFIED | — |

## Evidence & maintenance

- Score: `NOT_EVALUATED` — workload, legal/security checks, benchmarks and price region are not yet supplied.
- Update pricing and source **here only**; pillar pages should never duplicate provider prices.
- [Evaluation matrix](../docs/01-evaluation-matrix.md) · [Lifecycle](../docs/lifecycle.md)
