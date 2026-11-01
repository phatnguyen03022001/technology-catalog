# Anthropic

> **Provider SSOT.** Service claims and price evidence are recorded per offering below. `SOURCE_LINKED_SNAPSHOT` is not a current-price verification.

**Offerings:** 1 · **Pillars:** [10](../pillars/10-ai-models-agent-tools/README.md)

| Service | Primary pillar | Free kind | Free tier/credits | Paid pricing | Caveat | Official source | Evidence status | Evidence checked |
|---|---|---|---|---|---|---|---|---|
| Anthropic Claude API | 10 | `UNKNOWN` | Trang pricing không xác minh trial $5; không khẳng định free allowance | USD/1M tokens, context 1M: `claude-sonnet-5-5` $2 input / $10 output; prompt-cache write 5m $2.50, 1h $4, hit $0.10. `claude-opus-5-5` $4 / $20; writes $5 / $8, hit $0.20. `claude-haiku-5-5` (prompt ≤100k) $0.10 / $0.50; >100k $0.50 / $2.50; cache hit $0.01 / $0.05 tương ứng. | Claude 3.5 Haiku retired 2026-02-19; Claude 3.5 Sonnet retired 2025-10-28. Batch giảm 50% input/output. Giá tools và data residency phụ thuộc điều kiện; Claude API first-party dùng global mặc định. Rate limits theo tier. | [Claude API Pricing](https://platform.claude.com/docs/en/about-claude/pricing) · [Sonnet 5.5](https://platform.claude.com/docs/en/models/sonnet-5-5/overview) · [Model deprecations](https://platform.claude.com/docs/en/about-claude/model-deprecations) | `VERIFIED` | 2026-11-01 |

## Evidence & maintenance

- Score: `NOT_EVALUATED` — workload, legal/security checks, benchmarks and price region are not yet supplied.
- Update pricing and source **here only**; pillar pages should never duplicate provider prices.
- [Evaluation matrix](../docs/01-evaluation-matrix.md) · [Lifecycle](../docs/lifecycle.md)
