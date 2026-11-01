# Auth0

> **Provider SSOT.** Service claims and price evidence are recorded per offering below. `SOURCE_LINKED_SNAPSHOT` is not a current-price verification.

**Offerings:** 1 · **Pillars:** [07](../pillars/07-identity-security/README.md)

| Service | Primary pillar | Free kind | Free tier/credits | Paid pricing | Caveat | Official source | Evidence status | Evidence checked |
|---|---|---|---|---|---|---|---|---|
| Auth0 | 07 | PERMANENT | Free $0/month supports up to 25,000 MAU (B2C and B2B). B2C/B2B paid MAU tiers are distinct; free custom domain has a separate card-verification requirement. | Official machine-readable self-serve table (USD, monthly, 500-MAU tier): B2C Essentials $35, B2C Professional $240; B2B Essentials $150, B2B Professional $800. Annual billing for the same selected tier is 11 times the monthly price; higher MAU tiers, AI Agents/M2M/SSO and other add-ons cost separately. Enterprise is custom. | Verified scope is 500-MAU public B2C/B2B self-service USD monthly price table and 25K-MAU Free plan, NOT every MAU/region or Enterprise offer. The August 2026 marketing blog says Professional 1,000 MAU in prose, contradicting its own table; the current canonical selector and machine-readable table both specify 500 for the entry price. Do not combine Free 25K allowance with paid 500-MAU prices or assume higher-tier prices scale linearly. | [Official machine-readable pricing and MAU table](https://auth0.com/pricing.md) · [Live Auth0 pricing selector](https://auth0.com/pricing) · [Marketing blog conflict](https://auth0.com/blog/whatever-you-are-building-auth0-has-a-plan/) · [Custom domain card requirement](https://support.auth0.com/center/s/article/Using-Custom-Domains-with-Free-Tenants) | VERIFIED | 2026-11-01 |

## Evidence & maintenance

- Score: `NOT_EVALUATED` — workload, legal/security checks, benchmarks and price region are not yet supplied.
- Update pricing and source **here only**; pillar pages should never duplicate provider prices.
- [Evaluation matrix](../docs/01-evaluation-matrix.md) · [Lifecycle](../docs/lifecycle.md)
