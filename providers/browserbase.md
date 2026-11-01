# Browserbase

> **Provider SSOT.** Nguồn từ snapshot **2026-11-01**, có URL chính thức. Dữ liệu được chuyển nguyên từ catalog cũ, **chưa kiểm chứng lại giá trực tiếp trong lần tái cấu trúc này**. Chỉ dùng để nghiên cứu; xác minh lại trước khi mua hoặc triển khai production.

**Offerings:** 2 · **Pillars:** [01](../pillars/01-compute-runtime/README.md), [10](../pillars/10-ai-models-agent-tools/README.md)

| Service | Primary pillar | Free kind | Free tier/credits | Paid pricing | Caveat | Official source |
|---|---|---|---|---|---|---|
| Browserbase Browser Runtime | 01 | `LIMITED_FREE` | Free 1 browser-hour, 3 concurrent browsers | Developer $20/tháng | Kiểm tra reset period trước khi dự toán | [Pricing/docs](https://www.browserbase.com/pricing) |
| Browserbase Search/Fetch API | 10 | `LIMITED_FREE` | Free 1.000 Search calls + 1.000 Fetch calls theo Free plan | Developer $20/tháng; vượt Search $7/1K | Đây là Search/Fetch, tách khỏi Browser Runtime ở pillar 01 | [Pricing/docs](https://www.browserbase.com/pricing) |

## Evidence & maintenance

- Evidence: `SOURCE_LINKED_SNAPSHOT`; live re-verification required before production or budget commitments.
- Score: `NOT_EVALUATED` — workload, legal/security checks, benchmarks and price region are not yet supplied.
- Update pricing and source **here only**; pillar pages should never duplicate provider prices.
- [Evaluation matrix](../docs/01-evaluation-matrix.md) · [Lifecycle](../docs/lifecycle.md)
