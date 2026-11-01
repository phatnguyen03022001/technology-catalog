# DigitalOcean

> **Provider SSOT.** Nguồn từ snapshot **2026-11-01**, có URL chính thức đã qua kiểm chứng (VERIFIED). Chỉ dùng để nghiên cứu; xác minh lại trước khi mua hoặc triển khai production.

**Offerings:** 2 · **Pillars:** [01](../pillars/01-compute-runtime/README.md), [03](../pillars/03-storage-media/README.md)

| Service | Primary pillar | Free kind | Free tier/credits | Paid pricing | Caveat | Official source |
|---|---|---|---|---|---|---|
| DigitalOcean Droplets | 01 | `NONE` | No permanent free VM ($200 60-day promotional credit only) | Basic Droplets from $4/mo (512 MiB RAM, 1 vCPU, 10 GB SSD, 500 GiB transfer) | Unmanaged VPS; user patches OS/security; transfer overage $0.01/GiB; backups +20% | [DigitalOcean Droplets Pricing](https://www.digitalocean.com/pricing/droplets) |
| DigitalOcean Spaces | 03 | `NONE` | Không có free tier; $200 credit 60 ngày cho tài khoản mới | $5,00/tháng cố định (gồm 250 GiB storage, 1 TiB egress, free CDN, unlimited API calls) | Không có free tier nhưng giá $5/tháng cực kỳ dễ dự toán và rộng rãi | [DO Spaces Pricing](https://www.digitalocean.com/pricing/spaces) |

## Evidence & maintenance

- Evidence: `VERIFIED`; live re-verification completed on 2026-11-01 via multi-agent research fanout.
- Score: `NOT_EVALUATED` — workload, legal/security checks, benchmarks and price region are not yet supplied.
- Update pricing and source **here only**; pillar pages should never duplicate provider prices.
- [Evaluation matrix](../docs/01-evaluation-matrix.md) · [Lifecycle](../docs/lifecycle.md)
