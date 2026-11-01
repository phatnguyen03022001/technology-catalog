# Anthropic

> **Provider SSOT.** Service claims and price evidence are recorded per offering below. `SOURCE_LINKED_SNAPSHOT` is not a current-price verification.

**Offerings:** 1 · **Pillars:** [10](../pillars/10-ai-models-agent-tools/README.md)

| Service | Primary pillar | Free kind | Free tier/credits | Paid pricing | Caveat | Official source | Evidence status | Evidence checked |
|---|---|---|---|---|---|---|---|---|
| Anthropic Claude API | 10 | UNKNOWN | No general free API token quota established. | Selected current model IDs, standard USD per million tokens: claude-sonnet-5-5 $2 input/$10 output; claude-opus-5-5 $4/$20; claude-haiku-5-5 <=100K prompt $0.10/$0.50 and >100K $0.50/$2.50; claude-fable-5-1 $10/$50. 5m/1h cache-write rates: Sonnet $2.50/$4; Opus $5/$8; Haiku $0.125/$0.20 or $0.625/$1 above 100K; Fable $12.50/$20. Cache reads: Sonnet $0.10, Opus $0.20, Haiku $0.01 or $0.05 above 100K, Fable $0.25. Batch is 50% of standard. | This is a selected-model comparison, not an exhaustive active-model list. Fable 5.1 has 1M context and 128K max output; included cache-write/read rates above. Sonnet and Opus lifecycle supported at least through 2027-09-28 and 2027-09-22. No separate reasoning token price; thinking tokens bill as output. Long-context, media and tool charges are separate. | [Pricing](https://platform.claude.com/docs/en/about-claude/pricing) · [Fable 5.1 model card](https://platform.claude.com/docs/en/models/fable-5-1/overview) · [Sonnet card](https://platform.claude.com/docs/en/models/sonnet-5-5/overview) · [Lifecycle](https://platform.claude.com/docs/en/about-claude/model-deprecations) · [Thinking billing](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) | VERIFIED | 2026-11-01 |

## Evidence & maintenance

- Score: `NOT_EVALUATED` — workload, legal/security checks, benchmarks and price region are not yet supplied.
- Update pricing and source **here only**; pillar pages should never duplicate provider prices.
- [Evaluation matrix](../docs/01-evaluation-matrix.md) · [Lifecycle](../docs/lifecycle.md)
