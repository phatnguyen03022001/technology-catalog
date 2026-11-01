# OpenAI

> **Provider SSOT.** Service claims and price evidence are recorded per offering below. `SOURCE_LINKED_SNAPSHOT` is not a current-price verification.

**Offerings:** 1 · **Pillars:** [10](../pillars/10-ai-models-agent-tools/README.md)

| Service | Primary pillar | Free kind | Free tier/credits | Paid pricing | Caveat | Official source | Evidence status | Evidence checked |
|---|---|---|---|---|---|---|---|---|
| OpenAI API | 10 | `UNKNOWN` | Official current pricing page does not establish a general free API quota | Standard, short-context, USD/1M tokens: `gpt-6-luna` $0.10 input / $0.50 output (cached input $0.01; cache writes $0.125/30m, $0.25/12h); `gpt-6.1-terra` $1 / $5 (cached $0.05); `gpt-6.1-sol` $2 / $10 (cached $0.10); `gpt-6-astra` $10 / $50 (cached $1). | GPT-6 Luna là model API thật. Giá thay đổi theo context length và processing mode; regional processing +10% cho model đủ điều kiện phát hành từ 2026-03-05; FedRAMP +10% từ 2026-11-01. Web search $10/1k calls + model tokens; `gpt-realtime-2.1` audio $32/$64 per 1M input/output tokens (cached $0.40); `gpt-live-1` $0.05/min; transcription $0.003–$0.006/min; containers $0.03–$1.92/20-min session. | [OpenAI API Pricing](https://developers.openai.com/api/docs/pricing) | `VERIFIED` | 2026-11-01 |

## Evidence & maintenance

- Score: `NOT_EVALUATED` — workload, legal/security checks, benchmarks and price region are not yet supplied.
- Update pricing and source **here only**; pillar pages should never duplicate provider prices.
- [Evaluation matrix](../docs/01-evaluation-matrix.md) · [Lifecycle](../docs/lifecycle.md)
