# HashiCorp

> **Provider SSOT.** Service claims and price evidence are recorded per offering below. `SOURCE_LINKED_SNAPSHOT` is not a current-price verification.

**Offerings:** 2 · **Pillars:** [07](../pillars/07-identity-security/README.md), [08](../pillars/08-devops-delivery/README.md)

| Service | Primary pillar | Free kind | Free tier/credits | Paid pricing | Caveat | Official source | Evidence status | Evidence checked |
|---|---|---|---|---|---|---|---|---|
| HashiCorp Vault | 07 | `UNKNOWN` | Free managed-cloud plan not independently verified; self-hosted license/terms and operations are separate | HCP Vault Dedicated is billed hourly; snapshot cost is configuration-dependent and unverified | HCP Vault Secrets standalone sunset is separate from Vault Dedicated; do not treat self-hosting as a managed free tier. | [HashiCorp Vault Pricing](https://hashicorp.com/products/vault/pricing) | `SOURCE_LINKED_SNAPSHOT` | — |
| HCP Terraform | 08 | `PERMANENT` | Up to 500 Managed Resources (RUM); unlimited users; 1 concurrent run | Essentials ~$0.10/resource/mo; Standard ~$0.47/resource/mo | 500 managed resources hard boundary; counts each active state resource | [Terraform Pricing](https://www.hashicorp.com/products/terraform/pricing) | `SOURCE_LINKED_SNAPSHOT` | — |

## Evidence & maintenance

- Score: `NOT_EVALUATED` — workload, legal/security checks, benchmarks and price region are not yet supplied.
- Update pricing and source **here only**; pillar pages should never duplicate provider prices.
- [Evaluation matrix](../docs/01-evaluation-matrix.md) · [Lifecycle](../docs/lifecycle.md)
