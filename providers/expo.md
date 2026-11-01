# Expo

> **Provider SSOT.** Nguồn từ snapshot **2026-11-01**, có URL chính thức đã qua kiểm chứng (VERIFIED). Chỉ dùng để nghiên cứu; xác minh lại trước khi mua hoặc triển khai production.

**Offerings:** 2 · **Pillars:** [08](../pillars/08-devops-delivery/README.md), [11](../pillars/11-communications/README.md)

| Service | Primary pillar | Free kind | Free tier/credits | Paid pricing | Caveat | Official source |
|---|---|---|---|---|---|---|
| Expo EAS Build | 08 | `PERMANENT` | 15 Android + 15 iOS cloud builds/mo; local builds `eas build --local` unlimited free | Starter $19/mo ($45 build credits); Production $199/mo | Free queue has lower priority & wait times; no overages on Free | [Expo Pricing](https://expo.dev/pricing) |
| Expo Push Service | 11 | `PERMANENT` | 100% Free, không giới hạn push notifications tới iOS và Android | $0 transport (Expo kiếm tiền từ EAS Build/Update) | Rate limit 600 req/s; quy trình 2 bước: lấy PushTicket rồi truy vấn getReceipts | [Expo Push Docs](https://docs.expo.dev/push-notifications/overview/) |

## Evidence & maintenance

- Evidence: `VERIFIED`; live re-verification completed on 2026-11-01 via multi-agent research fanout.
- Score: `NOT_EVALUATED` — workload, legal/security checks, benchmarks and price region are not yet supplied.
- Update pricing and source **here only**; pillar pages should never duplicate provider prices.
- [Evaluation matrix](../docs/01-evaluation-matrix.md) · [Lifecycle](../docs/lifecycle.md)
