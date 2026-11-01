# Mistral AI

> **Provider SSOT.** Service claims and price evidence are recorded per offering below. `SOURCE_LINKED_SNAPSHOT` is not a current-price verification.

**Offerings:** 1 · **Pillars:** [10](../pillars/10-ai-models-agent-tools/README.md)

| Service | Primary pillar | Free kind | Free tier/credits | Paid pricing | Caveat | Official source | Evidence status | Evidence checked |
|---|---|---|---|---|---|---|---|---|
| Mistral API | 10 | UNKNOWN | Mistral Studio offers a no-card Free API mode; exact request/token allowance and the old 1 RPS limit are not reproduced. | Standard USD examples per 1M tokens: Small 4 `mistral-small-2603` (v26.03, GA, 256K context) $0.15 input, $0.015 cached input, $0.60 output. Large 4 `mistral-large-4` (v26.10, Public Preview, 1M context) $0.70 input, $0.07 cached, $2.10 output. Regional inference costs 1.1x Standard; Batch/Priority have separate selectors. | RC2/RC4 — Do not use retired Large 3 `mistral-large-2512` as current. Batch pricing for the named models and no-card Free-mode allowance are not reproduced; regional and EUR schedules are separate. | [Mistral pricing](https://docs.mistral.ai/inference/pricing) · [Models and lifecycle](https://docs.mistral.ai/models) · [Small 4 model card](https://docs.mistral.ai/models/mistral-small-4-0-26-03) · [Large 4 model card](https://docs.mistral.ai/models/mistral-large-4) · [Regional inference](https://docs.mistral.ai/inference/regional-inference) | UNVERIFIED | 2026-11-01 |

## Evidence & maintenance

- Score: `NOT_EVALUATED` — workload, legal/security checks, benchmarks and price region are not yet supplied.
- Update pricing and source **here only**; pillar pages should never duplicate provider prices.
- [Evaluation matrix](../docs/01-evaluation-matrix.md) · [Lifecycle](../docs/lifecycle.md)
