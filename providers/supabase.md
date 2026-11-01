# Supabase

> **Provider SSOT.** Nguồn từ snapshot **2026-11-01**, có URL chính thức. Dữ liệu được chuyển nguyên từ catalog cũ, **chưa kiểm chứng lại giá trực tiếp trong lần tái cấu trúc này**. Chỉ dùng để nghiên cứu; xác minh lại trước khi mua hoặc triển khai production.

**Offerings:** 3 · **Pillars:** [02](../pillars/02-databases-data/README.md), [03](../pillars/03-storage-media/README.md), [07](../pillars/07-identity-security/README.md)

| Service | Primary pillar | Free kind | Free tier/credits | Paid pricing | Caveat | Official source |
|---|---|---|---|---|---|---|
| Supabase Database | 02 | `PERMANENT` | 2 free projects (xác minh số project riêng); 500 MB database/project, 5 GB egress | Pro theo subscription + usage | Free projects có thể pause | [Pricing/docs](https://supabase.com/docs/guides/platform/billing-on-supabase) |
| Supabase Storage | 03 | `PERMANENT` | 1 GB file storage (Free plan) | 100 GB included trong Pro; sau đó $0,021/GB | RLS/egress và object operations | [Pricing/docs](https://supabase.com/docs/guides/platform/billing-on-supabase) |
| Supabase Auth | 07 | `PERMANENT` | 50K MAU cùng Supabase Free | Pro 100K MAU included, vượt mức $0,00325/MAU | Auth gắn với Supabase project limits | [Pricing/docs](https://supabase.com/docs/guides/platform/billing-on-supabase) |

## Evidence & maintenance

- Evidence: `SOURCE_LINKED_SNAPSHOT`; live re-verification required before production or budget commitments.
- Score: `NOT_EVALUATED` — workload, legal/security checks, benchmarks and price region are not yet supplied.
- Update pricing and source **here only**; pillar pages should never duplicate provider prices.
- [Evaluation matrix](../docs/01-evaluation-matrix.md) · [Lifecycle](../docs/lifecycle.md)
