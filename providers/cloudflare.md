# Cloudflare

> **Provider SSOT.** Nguồn từ snapshot **2026-11-01**, có URL chính thức. Dữ liệu được chuyển nguyên từ catalog cũ, **chưa kiểm chứng lại giá trực tiếp trong lần tái cấu trúc này**. Chỉ dùng để nghiên cứu; xác minh lại trước khi mua hoặc triển khai production.

**Offerings:** 4 · **Pillars:** [01](../pillars/compute-runtime/README.md), [03](../pillars/storage-media/README.md), [04](../pillars/networking-edge/README.md)

| Service | Primary pillar | Free kind | Free tier/credits | Paid pricing | Caveat | Official source |
|---|---|---|---|---|---|---|
| Cloudflare Workers | 01 | `PERMANENT` | 100.000 requests/ngày; 10 ms CPU/invocation | Paid Workers từ $5/tháng | CPU limit nghiêm ngặt ở Free | [Pricing/docs](https://developers.cloudflare.com/workers/platform/pricing/) |
| Cloudflare Pages (static) | 01 | `PERMANENT` | Static requests miễn phí không giới hạn | Functions tính theo Workers | Không đồng nghĩa unlimited Functions | [Pricing/docs](https://developers.cloudflare.com/pages/functions/pricing/) |
| Cloudflare R2 Standard | 03 | `PERMANENT` | 10 GB-month + 1M Class A + 10M Class B operations/tháng; egress miễn phí | $0,015/GB-month + operations | Không áp dụng free quota cho Infrequent Access | [Pricing/docs](https://developers.cloudflare.com/r2/pricing/) |
| Cloudflare DNS/CDN/WAF | 04 | `PERMANENT` | $0/tháng: DNS, CDN, SSL, DDoS protection và WAF cơ bản | Pro $25/tháng nếu trả tháng ($20/tháng nếu trả năm) | Không đồng nghĩa mọi WAF rule đều miễn phí | [Pricing/docs](https://www.cloudflare.com/plans/) |

## Evidence & maintenance

- Evidence: `SOURCE_LINKED_SNAPSHOT`; live re-verification required before production or budget commitments.
- Score: `NOT_EVALUATED` — workload, legal/security checks, benchmarks and price region are not yet supplied.
- Update pricing and source **here only**; pillar pages should never duplicate provider prices.
- [Evaluation matrix](../docs/01-evaluation-matrix.md) · [Lifecycle](../docs/lifecycle.md)
