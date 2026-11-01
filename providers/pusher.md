# Pusher

> **Provider SSOT.** Nguồn từ snapshot **2026-11-01**, có URL chính thức đã qua kiểm chứng (VERIFIED). Chỉ dùng để nghiên cứu; xác minh lại trước khi mua hoặc triển khai production.

**Offerings:** 2 · **Pillars:** [06](../pillars/06-messaging-async/README.md), [11](../pillars/11-communications/README.md)

| Service | Primary pillar | Free kind | Free tier/credits | Paid pricing | Caveat | Official source |
|---|---|---|---|---|---|---|
| Pusher Channels | 06 | `PERMANENT` | Sandbox: 200.000 messages/ngày (~6M/tháng); 100 concurrent connections | Startup $49/tháng (1M msgs/ngày, 500 conns); Pro $99/tháng (4M msgs/ngày) | Chặn từ connection 101; fan-out nhân số lượng client nhận; in-memory không có hàng đợi | [Pricing/docs](https://pusher.com/channels/pricing/) |
| Pusher Beams | 11 | `PERMANENT` | Tối đa 1.000 active devices/subscribers; unlimited push notifications | Startup $29/tháng (10k devices); Pro $99/tháng (50k devices) | Tính theo số thiết bị nhận push trong tháng, không tính theo số lượng push | [Pusher Beams Pricing](https://pusher.com/beams/pricing) |

## Evidence & maintenance

- Evidence: `VERIFIED`; live re-verification completed on 2026-11-01 via multi-agent research fanout.
- Score: `NOT_EVALUATED` — workload, legal/security checks, benchmarks and price region are not yet supplied.
- Update pricing and source **here only**; pillar pages should never duplicate provider prices.
- [Evaluation matrix](../docs/01-evaluation-matrix.md) · [Lifecycle](../docs/lifecycle.md)
