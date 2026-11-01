# Telnyx

> **Provider SSOT.** Service claims and price evidence are recorded per offering below. `SOURCE_LINKED_SNAPSHOT` is not a current-price verification.

**Offerings:** 2 · **Pillars:** [11](../pillars/11-communications/README.md)

| Service | Primary pillar | Free kind | Free tier/credits | Paid pricing | Caveat | Official source | Evidence status | Evidence checked |
|---|---|---|---|---|---|---|---|---|
| Telnyx | 11 | NO_MONTHLY_BASE | PAYG has no platform minimum; card on file required. No permanent free SMS quota asserted. | US SMS $0.004/message part outbound/inbound plus carrier pass-through; local numbers start at $1/month. Growth $2K minimum; Enterprise $5K minimum. | Carrier, 10DLC, number, segments, retries and tax are separate. Removed unsupported percentage-cheaper comparison. | [SMS pricing](https://telnyx.com/pricing/messaging) · [Plan minimums](https://telnyx.com/pricing) | VERIFIED | 2026-11-01 |
| Telnyx Email API | 11 | NO_MONTHLY_BASE | No recurring free sending quota established. Current pricing card says $0 platform fee and no subscription/minimum, but labels its rate card Beta. | The GA announcement states $0.30/1K outbound emails at low volume, tapering to $0.15/1K at high volume. The current pricing card lists a full volume table but still labels those as Beta rates. | GA was announced 2026-08-28, but the live first-party pricing page still says “Beta rates” and “GA pricing when it ships.” Treat exact GA pricing as unresolved. Billable sends are per recipient; inbound email is free. | [GA announcement](https://telnyx.com/release-notes/email-api-now-generally-available) · [Current pricing card](https://telnyx.com/pricing/email-api) · [Email API](https://telnyx.com/products/email-api) | UNVERIFIED | — |

## Evidence & maintenance

- Score: `NOT_EVALUATED` — workload, legal/security checks, benchmarks and price region are not yet supplied.
- Update pricing and source **here only**; pillar pages should never duplicate provider prices.
- [Evaluation matrix](../docs/01-evaluation-matrix.md) · [Lifecycle](../docs/lifecycle.md)
