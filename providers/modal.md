# Modal

> **Provider SSOT.** Service claims and price evidence are recorded per offering below. `SOURCE_LINKED_SNAPSHOT` is not a current-price verification.

**Offerings:** 1 · **Pillars:** [01](../pillars/01-compute-runtime/README.md)

| Service | Primary pillar | Free kind | Free tier/credits | Paid pricing | Caveat | Official source | Evidence status | Evidence checked |
|---|---|---|---|---|---|---|---|---|
| Modal Compute/Sandbox | 01 | `RECURRING_CREDIT` | Starter has $30 recurring compute credits/month, 100 containers, 10 GPU concurrency and 1 TiB monthly network egress included; Team includes $100/month compute credits, 5,000 containers and 50 GPU concurrency. Confirm the monthly credit period; unused credit is not a cash balance. | Official USD PAYG resource meters for baseline serverless: $0.0000131/physical CPU core-second (2 vCPU equivalent), $0.00000222/GiB-second memory, Nvidia H100 SXM5 $0.001097/GPU-second. Starter platform fee $0 plus compute; Team platform fee $250/month plus compute; Sandbox CPU/memory use non-preemptible rates (3× standard). GPU, network, volumes, reservations and selected regions have separate rates. | Verified scope: published Starter/Team base fees, monthly included credits, named standard CPU/memory/H100 meters and Sandbox multiplier. Physical core is NOT one vCPU; do not triple a H100 GPU price based on the Sandbox CPU/memory multiplier. Region, instance type, quotas and credits affect workload TCO; subtract each credit only once. Avoid claiming that GPU and CPU meters are interchangeable. | [Modal pricing, workload meters and Sandbox](https://modal.com/pricing) | VERIFIED | 2026-11-01 |

## Evidence & maintenance

- Score: `NOT_EVALUATED` — workload, legal/security checks, benchmarks and price region are not yet supplied.
- Update pricing and source **here only**; pillar pages should never duplicate provider prices.
- [Evaluation matrix](../docs/01-evaluation-matrix.md) · [Lifecycle](../docs/lifecycle.md)
