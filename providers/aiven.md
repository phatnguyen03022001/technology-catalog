# Aiven

> **Provider SSOT.** Nguồn từ snapshot **2026-11-01**, có URL chính thức đã qua kiểm chứng (VERIFIED). Chỉ dùng để nghiên cứu; xác minh lại trước khi mua hoặc triển khai production.

**Offerings:** 2 · **Pillars:** [02](../pillars/02-databases-data/README.md), [05](../pillars/05-cache-traditional-search/README.md)

| Service | Primary pillar | Free kind | Free tier/credits | Paid pricing | Caveat | Official source |
|---|---|---|---|---|---|---|
| Aiven PostgreSQL | 02 | `PERMANENT` | 1 vCPU, 1 GB RAM, 1 GB disk, 20 conns (1 svc/org) | ~$19/tháng (Startup-4) | Auto-power off nếu không có traffic; cần bật lại bằng tay | [Aiven Postgres Free](https://aiven.io/docs/products/postgresql/concepts/pg-free-tier) |
| Aiven Valkey | 05 | `PERMANENT` | Always-Free: 1 vCPU, 1 GB RAM (512 MB cache khả dụng), backups | Developer ~$15/tháng (2 vCPU, 4 GB RAM); High Availability từ $30-$60/tháng | Tự động tắt nếu không có traffic (inactivity sleep); cần bật lại qua console | [Aiven Valkey Free](https://aiven.io/valkey) |

## Evidence & maintenance

- Evidence: `VERIFIED`; live re-verification completed on 2026-11-01 via multi-agent research fanout.
- Score: `NOT_EVALUATED` — workload, legal/security checks, benchmarks and price region are not yet supplied.
- Update pricing and source **here only**; pillar pages should never duplicate provider prices.
- [Evaluation matrix](../docs/01-evaluation-matrix.md) · [Lifecycle](../docs/lifecycle.md)
