# Upstash

> **Provider SSOT.** Service claims and price evidence are recorded per offering below. `SOURCE_LINKED_SNAPSHOT` is not a current-price verification.

**Offerings:** 3 · **Pillars:** [02](../pillars/02-databases-data/README.md), [05](../pillars/05-cache-traditional-search/README.md), [06](../pillars/06-messaging-async/README.md)

| Service | Primary pillar | Free kind | Free tier/credits | Paid pricing | Caveat | Official source | Evidence status | Evidence checked |
|---|---|---|---|---|---|---|---|---|
| Upstash Vector | 02 | `PERMANENT` | 10k req/ngày; 10k vectors (200M dim units); 100 ns | $0,40 / 100K requests (không có phí sàn) | Giới hạn 10k req/ngày; dung lượng 10k vector (1536 dim) | [Upstash Vector Pricing](https://upstash.com/pricing/vector) | `SOURCE_LINKED_SNAPSHOT` | — |
| Upstash Redis | 05 | `PERMANENT` | 500k commands/month; 256MB storage; 10GB bandwidth | PAYG $0.20/100k commands; 1GB storage allowance on PAYG; Fixed plan $10/month | Monthly command quota resets monthly; actual usage depends on plan. | [Upstash Redis Pricing](https://upstash.com/pricing/redis) | `VERIFIED` | 2026-11-01 |
| Upstash QStash | 06 | `PERMANENT` | 1.000 messages/ngày (~30k/tháng); rate limit 100 req/s; payload max 1MB | Pay-as-you-go: $0 base, $1,00/100k msgs; Fixed 1M $180/tháng | Quota reset theo ngày không cộng dồn; mỗi lần retry tự động tính là 1 message | [Pricing/docs](https://upstash.com/pricing/qstash) | `SOURCE_LINKED_SNAPSHOT` | — |

## Evidence & maintenance

- Score: `NOT_EVALUATED` — workload, legal/security checks, benchmarks and price region are not yet supplied.
- Update pricing and source **here only**; pillar pages should never duplicate provider prices.
- [Evaluation matrix](../docs/01-evaluation-matrix.md) · [Lifecycle](../docs/lifecycle.md)
