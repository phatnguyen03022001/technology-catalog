# Hookdeck

> **Provider SSOT.** Service claims and price evidence are recorded per offering below. `SOURCE_LINKED_SNAPSHOT` is not a current-price verification.

**Offerings:** 1 · **Pillars:** [06](../pillars/06-messaging-async/README.md)

| Service | Primary pillar | Free kind | Free tier/credits | Paid pricing | Caveat | Official source | Evidence status | Evidence checked |
|---|---|---|---|---|---|---|---|---|
| Hookdeck | 06 | PERMANENT | Developer: 10K events/month, 3-day retention, 1 user and 5 events/sec/destination; retries are free and configured by user. | Current official plan rates: Developer $0/month (10K events); Team from $39/month; Growth from $499/month. Pay-as-you-go over 10,000 included events: first 5M events tier $3 per additional 100K delivered events, then published graduated tiers down to $0.35/100K above 500M. Additional discarded requests cost $2.50/million; extra destination throughput is priced separately. | RC3/RC4 — The published PAYG table and some interactive/FAQ pricing surfaces disagree on examples (e.g. $1 vs $3 per 100K); retain UNVERIFIED until the vendor reconciles the selector/FAQ. The visible price-table tier is specifically $3/100K up to 5M events, not a universal all-volume rate. Retries are included in event pricing; delivery throughput/retention remain separate. | [Hookdeck pricing](https://hookdeck.com/pricing) · [Retries](https://hookdeck.com/docs/hookdeck-basics) | UNVERIFIED | 2026-11-01 |

## Evidence & maintenance

- Score: `NOT_EVALUATED` — workload, legal/security checks, benchmarks and price region are not yet supplied.
- Update pricing and source **here only**; pillar pages should never duplicate provider prices.
- [Evaluation matrix](../docs/01-evaluation-matrix.md) · [Lifecycle](../docs/lifecycle.md)
