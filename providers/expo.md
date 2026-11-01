# Expo

> **Provider SSOT.** Service claims and price evidence are recorded per offering below. `SOURCE_LINKED_SNAPSHOT` is not a current-price verification.

**Offerings:** 2 · **Pillars:** [08](../pillars/08-devops-delivery/README.md), [11](../pillars/11-communications/README.md)

| Service | Primary pillar | Free kind | Free tier/credits | Paid pricing | Caveat | Official source | Evidence status | Evidence checked |
|---|---|---|---|---|---|---|---|---|
| Expo EAS Build | 08 | PERMANENT | Free includes 15 Android and 15 iOS builds/month, low-priority queue; no paid overage, wait for reset. Workflows include 60 minutes/month. | Starter $19/month includes $45 build credit. Production $199/month includes $225 credit and concurrency 15. | Free build allowance and Workflows minutes are separate; local builds use customer compute and do not incur EAS service build charges. | [Expo pricing](https://expo.dev/pricing) · [Plans](https://docs.expo.dev/billing/plans/) | VERIFIED | 2026-11-01 |
| Expo Push Service | 11 | PERMANENT | Expo does not charge for push relay. Limit: 600 notifications/second/project; up to 100 notification objects/request and 1,000 receipts/request. | No per-notification fee asserted for Expo push relay. | Best-effort, at-least-once handoff to FCM/APNs; duplicates or failed device delivery are possible. Payload is queued only until downstream handoff. | [Push FAQ/limits](https://docs.expo.dev/push-notifications/faq/) · [Sending API](https://docs.expo.dev/push-notifications/sending-notifications/) | VERIFIED | 2026-11-01 |

## Evidence & maintenance

- Score: `NOT_EVALUATED` — workload, legal/security checks, benchmarks and price region are not yet supplied.
- Update pricing and source **here only**; pillar pages should never duplicate provider prices.
- [Evaluation matrix](../docs/01-evaluation-matrix.md) · [Lifecycle](../docs/lifecycle.md)
