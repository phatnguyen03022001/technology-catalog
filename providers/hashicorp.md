# HashiCorp

> **Provider SSOT.** Nguồn từ snapshot **2026-11-01**, có URL chính thức đã qua kiểm chứng (VERIFIED). Chỉ dùng để nghiên cứu; xác minh lại trước khi mua hoặc triển khai production.

**Offerings:** 2 · **Pillars:** [07](../pillars/07-identity-security/README.md), [08](../pillars/08-devops-delivery/README.md)

| Service | Primary pillar | Free kind | Free tier/credits | Paid pricing | Caveat | Official source |
|---|---|---|---|---|---|---|
| HashiCorp Vault | 07 | `NONE_OR_CONDITIONAL` | Không có free cloud; Standalone HCP Vault Secrets đã SUNSET; OSS tự host free | HCP Vault Dedicated từ ~$0,62-$1,50+/h (~$450-$1.100+/tháng) | Không còn bản managed SaaS giá rẻ; tự host BSL tốn công vận hành unseal/Raft | [hashicorp.com/products/vault/pricing](https://hashicorp.com/products/vault/pricing) |
| HCP Terraform | 08 | `PERMANENT` | Up to 500 Managed Resources (RUM); unlimited users; 1 concurrent run | Essentials ~$0.10/resource/mo; Standard ~$0.47/resource/mo | 500 managed resources hard boundary; counts each active state resource | [Terraform Pricing](https://www.hashicorp.com/products/terraform/pricing) |

## Evidence & maintenance

- Evidence: `VERIFIED`; live re-verification completed on 2026-11-01 via multi-agent research fanout.
- Score: `NOT_EVALUATED` — workload, legal/security checks, benchmarks and price region are not yet supplied.
- Update pricing and source **here only**; pillar pages should never duplicate provider prices.
- [Evaluation matrix](../docs/01-evaluation-matrix.md) · [Lifecycle](../docs/lifecycle.md)
