# Pusher

> **Provider SSOT.** Service claims and price evidence are recorded per offering below. `SOURCE_LINKED_SNAPSHOT` is not a current-price verification.

**Offerings:** 2 · **Pillars:** [06](../pillars/06-messaging-async/README.md), [11](../pillars/11-communications/README.md)

| Service | Primary pillar | Free kind | Free tier/credits | Paid pricing | Caveat | Official source | Evidence status | Evidence checked |
|---|---|---|---|---|---|---|---|---|
| Pusher Channels | 06 | LIMITED_FREE | Sandbox: 200K messages/day and 100 connections. | Startup $49/month includes 1M messages/day and 500 connections; Pro $99/month includes 4M/day and 2K connections. | A publish to 50 subscribers counts 51 messages. Cache channel stores only latest event in memory for up to 30 minutes; not a durable queue. | [Channels pricing](https://pusher.com/channels/pricing/) · [Quotas](https://pusher.com/legal/quotas/) · [Cache channels](https://pusher.com/docs/channels/using_channels/cache-channels/) | VERIFIED | 2026-11-01 |
| Pusher Beams | 11 | LIMITED_FREE | Sandbox includes up to 1K subscribers; plans meter subscriber count, not notifications sent. | Startup $29/10K subscribers; Pro $99/50K; Business $199/115K; Premium $399/250K. | Official pricing does not establish unlimited sends; do not describe it as unlimited notification volume. | [Beams pricing](https://pusher.com/beams/pricing/) | VERIFIED | 2026-11-01 |

## Evidence & maintenance

- Score: `NOT_EVALUATED` — workload, legal/security checks, benchmarks and price region are not yet supplied.
- Update pricing and source **here only**; pillar pages should never duplicate provider prices.
- [Evaluation matrix](../docs/01-evaluation-matrix.md) · [Lifecycle](../docs/lifecycle.md)
