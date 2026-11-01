# Oracle Cloud Infrastructure

> **Provider SSOT.** Service claims and price evidence are recorded per offering below. `SOURCE_LINKED_SNAPSHOT` is not a current-price verification.

**Offerings:** 1 · **Pillars:** [01](../pillars/01-compute-runtime/README.md)

| Service | Primary pillar | Free kind | Free tier/credits | Paid pricing | Caveat | Official source | Evidence status | Evidence checked |
|---|---|---|---|---|---|---|---|---|
| Oracle OCI Ampere A1 | 01 | `PERMANENT` | 1,500 OCPU-hrs + 9,000 GB-hrs/month (= 2 OCPUs + 12 GB RAM 24/7); 200 GB block storage; 10 TB egress | PAYG Ampere A1 rates: ~$0.01/OCPU-hr, $0.0015/GB-hr | Quota cut from 4 OCPU/24GB to 2 OCPU/12GB; "Out of host capacity" common; idle instances reclaimed after 7 days | [Oracle Always Free](https://docs.oracle.com/en-us/iaas/Content/FreeTier/freetier_topic-Always_Free_Resources.htm) | `SOURCE_LINKED_SNAPSHOT` | — |

## Evidence & maintenance

- Score: `NOT_EVALUATED` — workload, legal/security checks, benchmarks and price region are not yet supplied.
- Update pricing and source **here only**; pillar pages should never duplicate provider prices.
- [Evaluation matrix](../docs/01-evaluation-matrix.md) · [Lifecycle](../docs/lifecycle.md)
