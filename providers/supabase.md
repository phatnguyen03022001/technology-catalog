# Supabase

> **Provider SSOT.** Service claims and price evidence are recorded per offering below. `SOURCE_LINKED_SNAPSHOT` is not a current-price verification.

**Offerings:** 3 · **Pillars:** [02](../pillars/02-databases-data/README.md), [03](../pillars/03-storage-media/README.md), [07](../pillars/07-identity-security/README.md)

| Service | Primary pillar | Free kind | Free tier/credits | Paid pricing | Caveat | Official source | Evidence status | Evidence checked |
|---|---|---|---|---|---|---|---|---|
| Supabase Database | 02 | PERMANENT | Free: 2 active projects, 500 MB database/project, 5 GB cached plus 5 GB uncached egress; projects may pause after one week inactive. | Pro is $25/month and includes 8 GB database plus 250 GB cached and 250 GB uncached egress; extra compute, disk and egress are separately metered. | Keep cached/uncached egress and organization-shared allowances separate. Free has no automatic daily backup entitlement: the current backup docs explicitly require manual CLI exports; paid plans have documented scheduled backups. An export/restore drill remains necessary. | [Supabase pricing](https://supabase.com/pricing) · [Billing](https://supabase.com/docs/guides/platform/billing-on-supabase) · [Database-only costs](https://supabase.com/kb/faqs/platform/database-only-cost) · [Backup policy](https://supabase.com/docs/guides/platform/backups) · [Free backup clarification](https://supabase.com/kb/faqs/platform/free-plan-backups) | VERIFIED | 2026-11-05 |
| Supabase Storage | 03 | `PERMANENT` | Free: 1 GB storage, 5 GB cached + 5 GB uncached egress; max 50 MB/file; Free projects may pause after one inactive week. | Pro $25/month includes 100 GB storage, 250 GB cached + 250 GB uncached egress. Image transforms: first 100 source images included on Pro, then $5/1,000. | Overage is $0.03/GB cached and $0.09/GB uncached egress. Specify 50 MB as Free upload cap; transforms included images are a separate quota. | [Supabase billing](https://supabase.com/docs/guides/platform/billing-on-supabase) · [Egress](https://supabase.com/docs/guides/platform/manage-your-usage/egress) · [Storage pricing](https://supabase.com/docs/guides/storage/pricing) | `VERIFIED` | 2026-11-01 |
| Supabase Auth | 07 | PERMANENT | Free includes 50K MAU; Free projects may pause after one week of inactivity. Customer SAML Auth is not included on Free. | Pro $25/month includes 100K MAU then $0.00325/MAU. Customer SAML Auth: Pro/Team includes 50 SSO MAU then $0.015/SSO MAU. | The $599 Team plan includes dashboard SSO; it is not required for customer Auth SAML. Separate workforce/dashboard SSO from customer identity. Default SMTP is non-production, team-address-only and currently limited to 2 messages/hour; email verification/recovery needs custom SMTP for real learners. | [Supabase pricing](https://supabase.com/pricing) · [Billing](https://supabase.com/docs/guides/platform/billing-on-supabase) · [SSO MAU pricing](https://supabase.com/docs/guides/platform/manage-your-usage/monthly-active-users-sso) · [SMTP restrictions](https://supabase.com/docs/guides/auth/auth-smtp) | VERIFIED | 2026-11-05 |

## Billing scope & TCO

- **One subscription per organization, not per offering.** The Pro $25/month platform fee shown under Database, Storage and Auth is **one organization-level fee**, not three $25 charges. Plan quotas for Storage, egress and MAU are allocated across the organization; do not multiply each included allowance by the number of projects/services.
- **Compute is different:** each project has its own compute cost. Supabase documents a $10 monthly compute credit for a paid organization; extra projects, add-ons and usage overages are additional. Confirm applicability and current charges for the intended project count.
- **Estimate:** one organization subscription + project-level compute/add-ons + aggregate over-quota metered usage (by distinct meter) + applicable taxes. Do not subtract a credit or count a platform fee twice.
- Official evidence: [Organization billing](https://supabase.com/docs/guides/platform/billing-on-supabase) · [Billing FAQ](https://supabase.com/docs/guides/platform/billing-faq).

## Evidence & maintenance

- Score: `NOT_EVALUATED` — workload, legal/security checks, benchmarks and price region are not yet supplied.
- Update pricing and source **here only**; pillar pages should never duplicate provider prices.
- [Evaluation matrix](../docs/01-evaluation-matrix.md) · [Lifecycle](../docs/lifecycle.md)
