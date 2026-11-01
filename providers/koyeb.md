# Koyeb

> **Provider SSOT.** Service claims and price evidence are recorded per offering below. `SOURCE_LINKED_SNAPSHOT` is not a current-price verification.

**Offerings:** 2 · **Pillars:** [01](../pillars/01-compute-runtime/README.md), [02](../pillars/02-databases-data/README.md)

| Service | Primary pillar | Free kind | Free tier/credits | Paid pricing | Caveat | Official source | Evidence status | Evidence checked |
|---|---|---|---|---|---|---|---|---|
| Koyeb | 01 | `PERMANENT` | One free web service/organization in Frankfurt or Washington, D.C.: 512 MB RAM, 0.1 vCPU, 2 GB SSD; 100 GB outbound bandwidth/month. | Pay per second. Eco nano (0.1 vCPU/256 MB/2 GB SSD) $1.61/month; Eco micro (0.25 vCPU/512 MB/4 GB SSD) $2.68/month. | Free instance is not for production; no Worker Services, custom scaling or volumes, and scales to zero after 1 hour without traffic. Koyeb requires a card and places a refundable $29 verification authorization. Bandwidth is not currently charged; Koyeb says usage above 100 GB will be $0.04/GB after notice. Koyeb announced a definitive agreement to join Mistral AI; no shutdown schedule is announced. | [Pricing FAQ](https://www.koyeb.com/docs/faqs/pricing) · [Instances and rates](https://www.koyeb.com/docs/reference/instances) · [Koyeb/Mistral announcement](https://www.koyeb.com/blog/koyeb-is-joining-mistral-ai-to-build-the-future-of-ai-infrastructure) | `VERIFIED` | 2026-11-01 |
| Koyeb Serverless Postgres | 02 | `LIMITED_FREE` | One free PostgreSQL database/organization: 0.25 vCPU, 1 GB RAM, up to 5 active compute hours/month and 1 GB stored data. Database regions: Frankfurt, Washington, D.C. and Singapore. | Starter organization plan has no monthly base fee: Small $0.04/instance-hour plus $0.50/GB-month storage ($29.76 compute for 744 hours); Medium $0.08/instance-hour. Pro is $29/month and includes $10/month compute usage. Database usage bills by the second. | A free database is limited to 5 active hours and 1 GB. Signup defaults to Pro and starts a prorated plan charge until downgraded to Starter; card verification places a refundable $29 authorization. Paid compute pauses while inactive, but storage continues billing; taxes are included on the invoice. | [Database pricing and limits](https://www.koyeb.com/docs/databases) · [Pricing FAQ](https://www.koyeb.com/docs/faqs/pricing) · [Organization plans](https://www.koyeb.com/docs/reference/organizations) · [Pricing page](https://www.koyeb.com/pricing) | `VERIFIED` | 2026-11-01 |

## Evidence & maintenance

- Score: `NOT_EVALUATED` — workload, legal/security checks, benchmarks and price region are not yet supplied.
- Update pricing and source **here only**; pillar pages should never duplicate provider prices.
- [Evaluation matrix](../docs/01-evaluation-matrix.md) · [Lifecycle](../docs/lifecycle.md)
