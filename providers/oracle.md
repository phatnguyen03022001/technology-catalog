# Oracle Cloud Infrastructure

> **Provider SSOT.** Service claims and price evidence are recorded per offering below. `SOURCE_LINKED_SNAPSHOT` is not a current-price verification.

**Offerings:** 2 · **Pillars:** [01](../pillars/01-compute-runtime/README.md), [03](../pillars/03-storage-media/README.md)

| Service | Primary pillar | Free kind | Free tier/credits | Paid pricing | Caveat | Official source | Evidence status | Evidence checked |
|---|---|---|---|---|---|---|---|---|
| Oracle OCI Ampere A1 | 01 | `PERMANENT` | Always Free: 1.500 OCPU-hours + 9.000 GB-hours/tháng (tối đa 2 OCPU/12 GB), 200 GB block storage và 10 TB outbound data trong home region. | Paid A1 rates phụ thuộc region/shape; numeric paid rate chưa tái lập trong audit này. | Trial $300 là credit một lần tối đa 30 ngày, tách khỏi Always Free; hầu hết signups cần phone/card. Host-capacity failures có thể chặn provisioning; bỏ claim reclaim sau 7 ngày khi không có nguồn. | [Always Free resources](https://docs.oracle.com/en-us/iaas/Content/FreeTier/freetier_topic-Always_Free_Resources.htm) · [Free Tier/trial](https://docs.oracle.com/en-us/iaas/Content/FreeTier/freetier.htm) | `SOURCE_LINKED_SNAPSHOT` | — |
| Oracle Object Storage | 03 | UNKNOWN | OCI Always Free eligibility and object-storage allowance depend on tenancy/region; no universal quota amount asserted. | Storage, requests, retrieval and outbound transfer vary by region and meter. | Do not infer object-storage allowance from compute A1 or account credits. | [OCI storage pricing](https://www.oracle.com/cloud/storage/pricing/) · [OCI Free Tier](https://www.oracle.com/cloud/free/) | UNVERIFIED | — |

## Evidence & maintenance

- Score: `NOT_EVALUATED` — workload, legal/security checks, benchmarks and price region are not yet supplied.
- Update pricing and source **here only**; pillar pages should never duplicate provider prices.
- [Evaluation matrix](../docs/01-evaluation-matrix.md) · [Lifecycle](../docs/lifecycle.md)
