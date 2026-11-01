# IBM Vault / HashiCorp

> **Provider SSOT.** Service claims and price evidence are recorded per offering below. `SOURCE_LINKED_SNAPSHOT` is not a current-price verification.

**Offerings:** 4 · **Pillars:** [07](../pillars/07-identity-security/README.md), [08](../pillars/08-devops-delivery/README.md)

| Service | Primary pillar | Free kind | Free tier/credits | Paid pricing | Caveat | Official source | Evidence status | Evidence checked |
|---|---|---|---|---|---|---|---|---|
| IBM Vault Community Edition | 07 | SELF_HOSTED | IBM Vault 2.0 is the current self-managed product; BSL 1.1 source-available license. Production grant permits internal use, not a competing hosted or embedded offering. | No OSS license fee under license terms; hosting and support cost extra. | BSL 1.1 is not OSI-approved open source. Do not merge community software with HCP Vault Dedicated pricing. | [IBM Vault 2.0](https://www.hashicorp.com/en/blog/ibm-vault-2-0-adds-ui-enhancements-and-improved-reporting-visibility) · [Vault license](https://github.com/hashicorp/vault/blob/main/LICENSE) | VERIFIED | 2026-11-01 |
| HCP Terraform | 08 | PERMANENT | Free: up to 500 managed resources; one remote run and one agent run concurrent. | Essentials PAYG bills managed resource-hours, rounding partial hours up and using peak resources within the hour. Official example: 1,000 resources × $0.0001359/hour ≈ $0.14/hour and $97.85 for 30 continuous days. Standard/Premium are sales-led. | Resource-hour is not $0.10/resource-month; use resource peaks and run concurrency for TCO. | [Plans and billing](https://developer.hashicorp.com/terraform/cloud-docs/overview) · [Cost example](https://developer.hashicorp.com/terraform/cloud-docs/overview/estimate-cost) | VERIFIED | 2026-11-01 |
| HCP Vault Dedicated | 07 | UNKNOWN | HCP trial includes $500 organization-level credit and one Vault Dedicated cluster; this is not a Vault-specific recurring free quota. Development tier is single-node, limited to 25 clients and has no Cloud SLA. | AWS/Azure tiers include Development, Essentials and Standard. Base rate varies by tier, size and region; some tiers add a monthly unique-client meter. Pay-as-you-go rates require HCP Portal/account access; no public numeric rate can be verified. | RC1/RC2/RC6 — Do not infer an hourly rate. HCP trial credit is organization-wide; production tier, region, size and billable-client definition affect total. | [Tier and feature matrix](https://developer.hashicorp.com/vault/cloud/get-started/deployment-considerations/tiers-and-features) · [HCP billing](https://developer.hashicorp.com/hcp/docs/hcp/admin/billing) · [Client billing FAQ](https://developer.hashicorp.com/vault/docs/concepts/billing/clients/faq) | UNVERIFIED | 2026-11-01 |
| HCP Vault Secrets | 07 | UNKNOWN | Discontinued 2026-06-30; no longer available. | Retired 2026-06-30; no current price or availability. Do not apply HCP Vault Dedicated pricing. | HashiCorp retirement notice and current consumption table confirm that this service ended 2026-06-30; it is distinct from active Vault Dedicated. | [Vault Secrets retirement and consumption table](https://www.hashicorp.com/en/pricing/consumption-table) | DISCONTINUED | 2026-11-01 |

## Evidence & maintenance

- Score: `NOT_EVALUATED` — workload, legal/security checks, benchmarks and price region are not yet supplied.
- Update pricing and source **here only**; pillar pages should never duplicate provider prices.
- [Evaluation matrix](../docs/01-evaluation-matrix.md) · [Lifecycle](../docs/lifecycle.md)
