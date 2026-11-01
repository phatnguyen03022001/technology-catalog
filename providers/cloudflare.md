# Cloudflare

> **Provider SSOT.** Nguồn từ snapshot **2026-11-01**, có URL chính thức đã qua kiểm chứng (VERIFIED). Chỉ dùng để nghiên cứu; xác minh lại trước khi mua hoặc triển khai production.

**Offerings:** 9 · **Pillars:** [01](../pillars/01-compute-runtime/README.md), [02](../pillars/02-databases-data/README.md), [03](../pillars/03-storage-media/README.md), [04](../pillars/04-networking-edge/README.md), [12](../pillars/12-business-extension-apis/README.md)

| Service | Primary pillar | Free kind | Free tier/credits | Paid pricing | Caveat | Official source |
|---|---|---|---|---|---|---|
| Cloudflare Workers | 01 | `PERMANENT` | 100,000 req/day; 10 ms CPU time/invocation; $0 egress | Workers Paid $5/mo (includes 10M req + 30M CPU ms; overage $0.30/M req, $0.02/M CPU ms) | 10ms CPU limit enforced strictly on Free; stateless V8 isolate (no long processes) | [Cloudflare Workers Pricing](https://developers.cloudflare.com/workers/platform/pricing/) |
| Cloudflare Pages | 01 | `PERMANENT` | Unlimited static requests & bandwidth; 500 builds/mo; 1 concurrent build (20m timeout) | Pro $20–$25/mo (5,000 builds, 5 concurrent); Functions scale via Workers Paid ($5/mo) | Unlimited static bandwidth does NOT cover Functions; Functions draw from Workers quota | [Cloudflare Pages Pricing](https://developers.cloudflare.com/pages/platform/limits/) |
| Cloudflare D1 | 02 | `PERMANENT` | 5M reads/ngày (150M/tháng); 100k writes/ngày; 5 GB storage | $5/tháng Workers Paid (25B reads inc.) | 500 MB mỗi DB ở Free; tối ưu đọc tại Edge | [Cloudflare D1 Pricing](https://developers.cloudflare.com/d1/platform/pricing/) |
| Cloudflare Vectorize | 02 | `PERMANENT` | 30M queried dims/tháng; 5M stored dims/tháng | $5/tháng Workers Paid ($0,01/1M queried) | Đo lường theo dimension; tích hợp sâu Workers | [Vectorize Pricing](https://developers.cloudflare.com/vectorize/platform/pricing/) |
| Cloudflare R2 Standard | 03 | `PERMANENT` | 10 GB-tháng standard storage; 1M Class A ops; 10M Class B ops; $0,00 egress vĩnh viễn | Standard $0,015/GB-tháng ($15/TB); Class A $4,50/1M; Class B $0,36/1M; Egress $0,00 | Không áp dụng cho Infrequent Access; chuẩn S3 API, không lo hóa đơn băng thông | [Cloudflare R2 Pricing](https://developers.cloudflare.com/r2/pricing/) |
| Cloudflare Images | 03 | `PERMANENT` | 5.000 unique remote transformations/tháng free; 0 native storage free | Storage $5/tháng cho 100k ảnh gốc; Delivery $1/100k ảnh; Remote transforms $0,50/1k | Lưu ảnh gốc ở R2 và dùng Cloudflare Image Transformations là kiến trúc tối ưu | [Cloudflare Images Pricing](https://developers.cloudflare.com/images/pricing/) |
| Cloudflare DNS/CDN/WAF | 04 | `PERMANENT` | $0/tháng: Unmetered bandwidth & DNS, SSL, unmetered DDoS protection, 5 WAF rules | Pro $25/tháng ($20 trả năm); Business $250/tháng | Giới hạn upload 100MB; cache file max 512MB; không dùng làm pure video/storage proxy | [Pricing/docs](https://www.cloudflare.com/plans/) |
| Cloudflare Zero Trust | 04 | `PERMANENT` | Miễn phí tối đa 50 users; Cloudflare Tunnel unmetered; ZTNA Access; Gateway DNS filtering | $7/user/tháng (Pay-as-you-go); Enterprise custom | Chặn đăng nhập từ user 51; Gateway DNS giới hạn fair-use 150k queries/user/tháng; logs lưu 24h | [Pricing/docs](https://www.cloudflare.com/plans/zero-trust-services/) |
| Cloudflare Turnstile | 12 | `PERMANENT` | Unmetered verification requests, 20 widgets | Enterprise custom | Chống bot thay thế reCAPTCHA; 100% free unmetered; không cần qua proxy CF | [Cloudflare Turnstile](https://developers.cloudflare.com/turnstile/plans/) |

## Evidence & maintenance

- Evidence: `VERIFIED`; live re-verification completed on 2026-11-01 via multi-agent research fanout.
- Score: `NOT_EVALUATED` — workload, legal/security checks, benchmarks and price region are not yet supplied.
- Update pricing and source **here only**; pillar pages should never duplicate provider prices.
- [Evaluation matrix](../docs/01-evaluation-matrix.md) · [Lifecycle](../docs/lifecycle.md)
