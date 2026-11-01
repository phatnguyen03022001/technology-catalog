# Stripe

> **Provider SSOT.** Service claims and price evidence are recorded per offering below. `SOURCE_LINKED_SNAPSHOT` is not a current-price verification.

**Offerings:** 2 · **Pillars:** [12](../pillars/12-business-extension-apis/README.md)

| Service | Primary pillar | Free kind | Free tier/credits | Paid pricing | Caveat | Official source | Evidence status | Evidence checked |
|---|---|---|---|---|---|---|---|---|
| Stripe Payments | 12 | NO_MONTHLY_BASE | No monthly or setup fee for standard US domestic online-card processing. | US domestic online card 2.9% + $0.30/transaction; international adds 1.5%, currency conversion adds 1%. | Stripe Payments is a gateway, not Merchant of Record; merchant retains tax and dispute responsibilities. | [Stripe pricing](https://stripe.com/pricing) | VERIFIED | 2026-11-01 |
| Stripe Tax | 12 | NO_MONTHLY_BASE | Tax Basic has no recurring platform fee; no free recurring production transaction allowance asserted. | No-code Tax Basic is 0.5% per transaction. API is $0.50/transaction in registered jurisdictions; includes 10 calculations then $0.05/call. Tax Complete starts $90/month with annual contract. | Tax calculation, registrations, filing and payment processing are separate. Exact rate depends on integration and location of tax registration. | [Stripe Tax pricing](https://stripe.com/tax/pricing) · [Stripe Tax docs](https://docs.stripe.com/tax) | VERIFIED | 2026-11-01 |

## Evidence & maintenance

- Score: `NOT_EVALUATED` — workload, legal/security checks, benchmarks and price region are not yet supplied.
- Update pricing and source **here only**; pillar pages should never duplicate provider prices.
- [Evaluation matrix](../docs/01-evaluation-matrix.md) · [Lifecycle](../docs/lifecycle.md)
