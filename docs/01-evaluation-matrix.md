# Evaluation matrix — evidence-based comparison

## A. Hard gates (PASS / FAIL / UNKNOWN)

**FAIL = reject**; **UNKNOWN = production selection blocked until verified**. A numeric score cannot override a hard gate.

| Gate | Evidence |
|---|---|
| Functional fit/region | Required features, APIs, quota, region |
| Security/privacy | Secrets, isolation, retention/training, DPA/compliance |
| Legal/commercial | License, ToS, free plan commercial usage rights |
| Cost safety | Hard/soft quotas, overages, egress, budget guardrails |
| Portability/recoverability | Backup, export, rollback or replacement for critical dependency |

## B. 8-dimension scoring

Rate 0–5 per dimension **only with testable criteria and sources**: 0 unacceptable; 1 major gaps; 2 limited; 3 meets; 4 exceeds; 5 verified excellent. Missing evidence is `UNKNOWN`, never 0.

| Dimension | Default weight |
|---|---:|
| D1 Discovery & Evaluation | 5% |
| D2 Integration & Contracts | 10% |
| D3 Security & Data Governance | 20% |
| D4 Reliability & Resilience | 15% |
| D5 Performance & Scalability | 10% |
| D6 Cost & Quota Optimization | 20% |
| D7 Observability & Operations | 10% |
| D8 Lifecycle & Exit Strategy | 10% |
| **Total** | **100%** |

`Score (0–100) = Σ(weight × rating / 5)`. No overall score when required evidence is `UNKNOWN`. Weights are **defaults**, not universal rankings; document workloads and adjusted weights explicitly.

## C. Comparable real-world workload

Compare candidates using equal requests/day, storage GB-month, token IO (by model), retrieval/search queries, egress, region, concurrency, seats, runtime/sandbox duration, latency, uptime, error/retry rate and data sensitivity.

`TCO = subscription + post-free quota usage + egress/storage + seats + operations + retries + taxes (when applicable)`.

Distinguish perpetual free, recurring monetary credits, one-time signup credit, expiring trial, self-host open-source license and zero subscription with transaction fees.

## Evidence classifications

- `VERIFIED`: service-row claims were checked against dated official sources; a price row includes plan/model/SKU, amount/currency/unit, region where applicable, free allowance/reset, source URL and checked date. This does not verify security, performance, or suitability.
- `SOURCE_LINKED_SNAPSHOT`: legacy catalog claim has an official source link but its current value was not independently reproduced; recheck before production.
- `UNVERIFIED`: a service's price or free-tier claim cannot be reproduced from current official evidence, or no such claim is made.
- `STALE`: evidence changed or expired; do not imply still current.
- `DISCONTINUED`: first-party evidence confirms the service has ceased operation; an announced future wind-down does not qualify.

Service evidence is recorded on each provider table row. A validator can check that status, dates and source links are present; it cannot establish that a price is factually accurate. Never infer pricing accuracy from a passing structural check.

Output: workload, gates, candidate costs, security/operational tradeoffs, score only if supported, checkedAt, evidence URLs, recommendation and fallback.
