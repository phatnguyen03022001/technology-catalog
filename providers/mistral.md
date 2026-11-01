# Mistral AI

> **Provider SSOT.** Service claims and price evidence are recorded per offering below. `SOURCE_LINKED_SNAPSHOT` is not a current-price verification.

**Offerings:** 1 · **Pillars:** [10](../pillars/10-ai-models-agent-tools/README.md)

| Service | Primary pillar | Free kind | Free tier/credits | Paid pricing | Caveat | Official source | Evidence status | Evidence checked |
|---|---|---|---|---|---|---|---|---|
| Mistral API | 10 | UNKNOWN | Mistral Studio offers a no-card Free API mode; exact request/token allowance and the old 1 RPS limit are not reproduced. | Current GA example mistral-small-2603 (Small 4 v26.03), 256K context: $0.15 input/$0.015 cached/$0.60 output per million tokens. Large 3 mistral-large-2512 is deprecated despite lingering in the pricing table. Large 4 mistral-large-4 v26.10 is Public Preview, 1M context: $0.70 input/$0.07 cached/$2.10 output per MTok on the current official table. | Small 4 and Large 4 standard token rates are current named examples. Keep row UNVERIFIED because Free-mode allowance and exact Small 4 batch rate are not reproduced; the preview model/rates can change. Do not generalize an advertised 50% batch discount to a model without a published price. | [Models/lifecycle](https://docs.mistral.ai/models) · [Pricing](https://docs.mistral.ai/inference/pricing) · [Large 4 card](https://docs.mistral.ai/models/mistral-large-4) · [Small 4 card](https://docs.mistral.ai/models/mistral-small-4-0-26-03) · [Free API setup](https://docs.mistral.ai/getting-started/quickstarts/studio/activate-and-generate-api-key/) | UNVERIFIED | — |

## Evidence & maintenance

- Score: `NOT_EVALUATED` — workload, legal/security checks, benchmarks and price region are not yet supplied.
- Update pricing and source **here only**; pillar pages should never duplicate provider prices.
- [Evaluation matrix](../docs/01-evaluation-matrix.md) · [Lifecycle](../docs/lifecycle.md)
