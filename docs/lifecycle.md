# Lifecycle — Research → Compare → Maintain

1. **Research:** discover candidate/service, identify provider, pillar, official pricing/docs, ToS, region, license and free-tier kind. Unknown price stays watchlisted.
2. **Evaluate/Compare:** same workload + [hard gates and matrix](01-evaluation-matrix.md); measure real latency and compute TCO including retry/egress/region/retention.
3. **Select:** document decision, constraints, price verification date, backup/fallback, budget cap, commercial usage rights and exit cost.
4. **Integrate:** least-privilege secrets; timeouts, rate limits, bounded retry with jitter and idempotency; smoke tests for provider outage, billing cap and export.
5. **Operate/Monitor:** watch billing, credits, token/request usage, service errors, latency and provider pricing/ToS/deprecation changes; trigger re-evaluation on meaningful changes.
6. **Migrate/Retire:** export, cutover, rollback, delete/retain data as required, rotate/revoke keys and reconcile invoices.

## Free-tier classifications

| Kind | Meaning |
|---|---|
| PERMANENT | Ongoing quota under published terms (no SLA implied) |
| RECURRING_CREDIT | Credit replenished by period, check reset/rollover |
| ONE_TIME_CREDIT | Signup grant, not renewable |
| TIME_LIMITED_TRIAL | Expires after a fixed period |
| PERMANENT_AFTER_TRIAL | Small distinct permanent allocation after trial |
| LIMITED_FREE | Free period/eligibility needs clarification |
| NO_MONTHLY_BASE | Subscription $0 but transactions charged |
| NONE | No verified ongoing free offering |

## SSOT maintenance

Update the price and source only in `providers/<provider>.md`; pillar and research index contain references, not duplicated figures. Keep `checkedAt`, provider URL, plan/SKU, billing unit, currency, region, quota/reset, expiry, commercial restrictions and confidence when independently re-verifying.

Snapshot migration is **not** a price refresh. Do not overwrite historical dates without checking current primary evidence. Avoid placeholder files and unnecessary automations.
