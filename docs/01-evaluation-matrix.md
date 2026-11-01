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
- `SOURCE_LINKED_SNAPSHOT`: a legacy claim has an official source link, but its current value was not fully reproduced; recheck before production.
- `UNVERIFIED`: a service's price or free-tier claim cannot be reproduced from current official evidence, or no such claim is made.
- `STALE`: evidence changed or expired; do not imply still current.
- `DISCONTINUED`: first-party evidence confirms the provider ended the offering. For software, state separately whether existing installations remain usable after upstream distribution or maintenance ends; an announced future wind-down does not qualify.

Service evidence is recorded on each provider table row. A validator can check that status, dates and source links are present; it cannot establish that a price is factually accurate. Never infer pricing accuracy from a passing structural check.

### Unresolved evidence root causes

For an active `SOURCE_LINKED_SNAPSHOT`, `UNVERIFIED`, or `STALE` row, put one or more root-cause codes in its Caveat cell. These codes describe the current evidence blocker:

- `RC1` — Price is not public or requires a quote.
- `RC2` — Price depends on a selected region, SKU, plan, meter, currency, or billing term.
- `RC3` — Official sources conflict and applicability is unresolved.
- `RC4` — Only part of the material claims (price, quota, limit, or tier) is verified.
- `RC5` — A prior claim is historical, deprecated, or affected by a lifecycle change.
- `RC6` — Evidence requires login, account entitlement, an inaccessible calculator, or sales access.
- `RC7` — A claim lacks adequate supporting evidence and must be removed, qualified, or rechecked.

`Evidence checked` records the date the row's evidence was reviewed for every status. It does not imply that an unresolved price is verified.

Output: workload, gates, candidate costs, security/operational tradeoffs, score only if supported, checkedAt, evidence URLs, recommendation and fallback.
