# MinIO

> **Provider SSOT.** Service claims and price evidence are recorded per offering below. `SOURCE_LINKED_SNAPSHOT` is not a current-price verification.

**Offerings:** 2 · **Pillars:** [03](../pillars/03-storage-media/README.md)

| Service | Primary pillar | Free kind | Free tier/credits | Paid pricing | Caveat | Official source | Evidence status | Evidence checked |
|---|---|---|---|---|---|---|---|---|
| MinIO OSS | 03 | `SELF_HOSTED` | Legacy AGPLv3 self-hosted code. MinIO ended upstream maintenance and distribution in September 2025; existing installations remain usable, but the source is frozen and receives no vendor maintenance. | No current price for the ended vendor-distributed OSS offering. Hosting/operations remain the operator’s cost; AIStor is a separate successor. | DISCONTINUED describes MinIO upstream distribution/maintenance, not that installed copies stopped working. Do not present this as maintained or downloadable from MinIO. | [MinIO EOL and legal](https://www.min.io/legal) · [AIStor pricing](https://www.min.io/pricing) | `DISCONTINUED` | 2026-11-01 |
| MinIO AIStor | 03 | LIMITED_FREE | AIStor Free is a single-node deployment; it excludes distributed/multi-node deployments, replication, object tiering/lifecycle transitions and encryption at rest. The AIStor Free agreement permits independent production use but restricts redistribution, resale and distributed-node use. | AIStor Enterprise Lite and Enterprise are capacity-based/quote-based; no public universal per-GB production price is asserted. | AIStor Free is not feature-complete: official license documentation also lists version-specific deletion, profiling/diagnostics, performance testing, telemetry, healing/lock visibility and `mc support` commands as excluded. No SLA/SLO is included; encryption-at-rest writes and KMS configuration are not permitted under the free license. | [AIStor pricing](https://www.min.io/pricing) · [AIStor Free Agreement](https://www.min.io/legal/aistor-free-agreement) · [AIStor license feature limits](https://docs.min.io/aistor/operations/licenses/) · [MinIO legal and OSS EOL](https://www.min.io/legal) | VERIFIED | 2026-11-01 |

## Evidence & maintenance

- Score: `NOT_EVALUATED` — workload, legal/security checks, benchmarks and price region are not yet supplied.
- Update pricing and source **here only**; pillar pages should never duplicate provider prices.
- [Evaluation matrix](../docs/01-evaluation-matrix.md) · [Lifecycle](../docs/lifecycle.md)
