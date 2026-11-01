# Cloudflare

> **Provider SSOT.** Service claims and price evidence are recorded per offering below. `SOURCE_LINKED_SNAPSHOT` is not a current-price verification.

**Offerings:** 9 · **Pillars:** [01](../pillars/01-compute-runtime/README.md), [02](../pillars/02-databases-data/README.md), [03](../pillars/03-storage-media/README.md), [04](../pillars/04-networking-edge/README.md), [12](../pillars/12-business-extension-apis/README.md)

| Service | Primary pillar | Free kind | Free tier/credits | Paid pricing | Caveat | Official source | Evidence status | Evidence checked |
|---|---|---|---|---|---|---|---|---|
| Cloudflare Workers | 01 | `PERMANENT` | 100,000 req/day; 10 ms CPU time/invocation; $0 egress | Workers Paid $5/mo (includes 10M req + 30M CPU ms; overage $0.30/M req, $0.02/M CPU ms) | 10ms CPU limit enforced strictly on Free; stateless V8 isolate (no long processes) | [Cloudflare Workers Pricing](https://developers.cloudflare.com/workers/platform/pricing/) | `SOURCE_LINKED_SNAPSHOT` | — |
| Cloudflare Pages | 01 | `PERMANENT` | Unlimited static requests & bandwidth; 500 builds/mo; 1 concurrent build (20m timeout) | Pro $20–$25/mo (5,000 builds, 5 concurrent); Functions scale via Workers Paid ($5/mo) | Unlimited static bandwidth does NOT cover Functions; Functions draw from Workers quota | [Cloudflare Pages Pricing](https://developers.cloudflare.com/pages/platform/limits/) | `SOURCE_LINKED_SNAPSHOT` | — |
| Cloudflare D1 | 02 | `PERMANENT` | 5M rows read/day; 100k rows written/day; 5GB total storage | Workers Paid $5/mo includes 25B reads and 50M writes/month; overage $0.001/M reads and $1/M written rows | Free quotas reset daily; database 500MB maximum per DB on Free. | [D1 Pricing](https://developers.cloudflare.com/d1/platform/pricing/) | `VERIFIED` | 2026-11-01 |
| Cloudflare Vectorize | 02 | `PERMANENT` | 30M queried dimensions/month; 5M stored dimensions/month | Workers Paid $5/mo includes 50M queried and 10M stored dimensions; overage $0.01/M queried dimensions | Vectorize quotas/pricing are separate usage dimensions; $5 is the required Workers Paid plan base, not a Vectorize price. | [Vectorize Pricing](https://developers.cloudflare.com/vectorize/platform/pricing/) | `VERIFIED` | 2026-11-01 |
| Cloudflare R2 Standard | 03 | `PERMANENT` | 10 GB-tháng standard storage; 1M Class A ops; 10M Class B ops; $0,00 egress vĩnh viễn | Standard $0,015/GB-tháng ($15/TB); Class A $4,50/1M; Class B $0,36/1M; Egress $0,00 | Không áp dụng cho Infrequent Access; chuẩn S3 API, không lo hóa đơn băng thông | [Cloudflare R2 Pricing](https://developers.cloudflare.com/r2/pricing/) | `VERIFIED` | 2026-11-01 |
| Cloudflare Images | 03 | `PERMANENT` | 5.000 unique remote transformations/tháng free; 0 native storage free | Storage $5/tháng cho 100k ảnh gốc; Delivery $1/100k ảnh; Remote transforms $0,50/1k | Lưu ảnh gốc ở R2 và dùng Cloudflare Image Transformations là kiến trúc tối ưu | [Cloudflare Images Pricing](https://developers.cloudflare.com/images/pricing/) | `SOURCE_LINKED_SNAPSHOT` | — |
| Cloudflare DNS/CDN/WAF | 04 | `PERMANENT` | $0/tháng: Unmetered bandwidth & DNS, SSL, unmetered DDoS protection, 5 WAF rules | Pro $25/tháng ($20 trả năm); Business $250/tháng | Giới hạn upload 100MB; cache file max 512MB; không dùng làm pure video/storage proxy | [Pricing/docs](https://www.cloudflare.com/plans/) | `SOURCE_LINKED_SNAPSHOT` | — |
| Cloudflare Zero Trust | 04 | `PERMANENT` | Miễn phí tối đa 50 users; Cloudflare Tunnel unmetered; ZTNA Access; Gateway DNS filtering | $7/user/tháng (Pay-as-you-go); Enterprise custom | Chặn đăng nhập từ user 51; Gateway DNS giới hạn fair-use 150k queries/user/tháng; logs lưu 24h | [Pricing/docs](https://www.cloudflare.com/plans/zero-trust-services/) | `SOURCE_LINKED_SNAPSHOT` | — |
| Cloudflare Turnstile | 12 | `PERMANENT` | Unmetered verification requests, 20 widgets | Enterprise custom | Chống bot thay thế reCAPTCHA; 100% free unmetered; không cần qua proxy CF | [Cloudflare Turnstile](https://developers.cloudflare.com/turnstile/plans/) | `SOURCE_LINKED_SNAPSHOT` | — |

## Evidence & maintenance

- Score: `NOT_EVALUATED` — workload, legal/security checks, benchmarks and price region are not yet supplied.
- Update pricing and source **here only**; pillar pages should never duplicate provider prices.
- [Evaluation matrix](../docs/01-evaluation-matrix.md) · [Lifecycle](../docs/lifecycle.md)
