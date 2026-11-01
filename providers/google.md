# Google

> **Provider SSOT.** Nguồn từ snapshot **2026-11-01**, có URL chính thức. Dữ liệu được chuyển nguyên từ catalog cũ, **chưa kiểm chứng lại giá trực tiếp trong lần tái cấu trúc này**. Chỉ dùng để nghiên cứu; xác minh lại trước khi mua hoặc triển khai production.

**Offerings:** 2 · **Pillars:** [10](../pillars/ai-models-agent-tools/README.md), [12](../pillars/business-extension-apis/README.md)

| Service | Primary pillar | Free kind | Free tier/credits | Paid pricing | Caveat | Official source |
|---|---|---|---|---|---|---|
| Google Gemini Developer API | 10 | `PERMANENT` | Free input/output tokens cho một số models; rate limits theo model | PAYG theo model/token | Free tier data có thể dùng cải thiện sản phẩm; kiểm tra điều khoản | [Pricing/docs](https://ai.google.dev/gemini-api/docs/pricing) |
| Google Maps Platform | 12 | `PERMANENT` | Theo SKU: Essentials 10K events/tháng, Pro 5K, Enterprise 1K | PAYG theo SKU/region | Không còn mặc định $200 credit monthly cũ | [Pricing/docs](https://developers.google.com/maps/billing-and-pricing/overview) |

## Evidence & maintenance

- Evidence: `SOURCE_LINKED_SNAPSHOT`; live re-verification required before production or budget commitments.
- Score: `NOT_EVALUATED` — workload, legal/security checks, benchmarks and price region are not yet supplied.
- Update pricing and source **here only**; pillar pages should never duplicate provider prices.
- [Evaluation matrix](../docs/01-evaluation-matrix.md) · [Lifecycle](../docs/lifecycle.md)
