# Upstash

> **Provider SSOT.** Nguồn từ snapshot **2026-11-01**, có URL chính thức. Dữ liệu được chuyển nguyên từ catalog cũ, **chưa kiểm chứng lại giá trực tiếp trong lần tái cấu trúc này**. Chỉ dùng để nghiên cứu; xác minh lại trước khi mua hoặc triển khai production.

**Offerings:** 2 · **Pillars:** [05](../pillars/cache-traditional-search/README.md), [06](../pillars/messaging-async/README.md)

| Service | Primary pillar | Free kind | Free tier/credits | Paid pricing | Caveat | Official source |
|---|---|---|---|---|---|---|
| Upstash Redis | 05 | `PERMANENT` | 256 MB data; 500K commands; 10 GB bandwidth/tháng | PAYG $0,20/100K commands | Không nhầm với Upstash Vector | [Pricing/docs](https://upstash.com/pricing/redis) |
| Upstash QStash | 06 | `PERMANENT` | 1.000 messages/ngày | PAYG $1/100K messages | Retry attempts cũng tính message | [Pricing/docs](https://upstash.com/pricing/qstash) |

## Evidence & maintenance

- Evidence: `SOURCE_LINKED_SNAPSHOT`; live re-verification required before production or budget commitments.
- Score: `NOT_EVALUATED` — workload, legal/security checks, benchmarks and price region are not yet supplied.
- Update pricing and source **here only**; pillar pages should never duplicate provider prices.
- [Evaluation matrix](../docs/01-evaluation-matrix.md) · [Lifecycle](../docs/lifecycle.md)
