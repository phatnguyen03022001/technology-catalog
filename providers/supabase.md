# Supabase

> **Provider SSOT.** Service claims and price evidence are recorded per offering below. `SOURCE_LINKED_SNAPSHOT` is not a current-price verification.

**Offerings:** 3 · **Pillars:** [02](../pillars/02-databases-data/README.md), [03](../pillars/03-storage-media/README.md), [07](../pillars/07-identity-security/README.md)

| Service | Primary pillar | Free kind | Free tier/credits | Paid pricing | Caveat | Official source | Evidence status | Evidence checked |
|---|---|---|---|---|---|---|---|---|
| Supabase Database | 02 | `PERMANENT` | 2 projects; 500 MB DB/proj; 5 GB egress; 50k MAU | $25/tháng Pro ($10 credit = Micro VM) | Pauses sau 7 ngày không active; không có backup tự động ở Free | [Supabase Pricing](https://supabase.com/pricing) | `SOURCE_LINKED_SNAPSHOT` | — |
| Supabase Storage | 03 | `PERMANENT` | 1 GB storage; 5 GB uncached egress; 5 GB cached CDN egress; max file 50MB | Pro $25/tháng (100 GB storage, 250 GB uncached, 250 GB cached); transforms $5/1k images | Gắn liền database Supabase (pause sau 7 ngày không active); transforms cần Pro $25 | [Supabase Billing](https://supabase.com/docs/guides/platform/billing-on-supabase) | `SOURCE_LINKED_SNAPSHOT` | — |
| Supabase Auth | 07 | `PERMANENT` | 50.000 MAUs free trên Free tier; Postgres RLS tích hợp | Pro $25/tháng (gồm 100k MAU); overage cực rẻ $0,00325/MAU | Free project pause sau 7 ngày không active; SAML SSO nằm ở gói Team $599/tháng | [supabase.com/docs/guides/platform/billing-on-supabase](https://supabase.com/docs/guides/platform/billing-on-supabase) | `SOURCE_LINKED_SNAPSHOT` | — |

## Evidence & maintenance

- Score: `NOT_EVALUATED` — workload, legal/security checks, benchmarks and price region are not yet supplied.
- Update pricing and source **here only**; pillar pages should never duplicate provider prices.
- [Evaluation matrix](../docs/01-evaluation-matrix.md) · [Lifecycle](../docs/lifecycle.md)
