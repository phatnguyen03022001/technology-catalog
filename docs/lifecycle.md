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
| LIMITED_FREE | A real free allowance with a stated eligibility or usage restriction; state the restriction |
| NO_MONTHLY_BASE | Subscription $0 but transactions charged |
| SELF_HOSTED | Software license is $0; user pays hosting and operations, subject to license terms |
| NONE | Current evidence confirms no free allowance or credit for this offering |
| UNKNOWN | Available evidence does not establish whether a free allowance exists; never imply NONE |

Free kind describes the offer type, not the evidence quality. Keep it separate from service evidence status. A service scheduled to wind down is still available until the announced cutoff occurs; record the dates and current state in its caveat.

## SSOT maintenance

Update price and source only in `providers/<provider>.md`; pillar and research indexes contain references, not duplicated figures. Evidence is recorded on each service row. For `VERIFIED` rows, the service and pricing cells must identify the exact verified scope: plan/model/SKU, price amount/currency/unit **when a numeric price is asserted**, region where applicable, allowance/reset or expiry, official source URL and verification date. Quote-only, variable/no-universal-price and verified no-direct-fee claims remain distinct; unquantified `VERIFIED` paid-pricing rows must carry `TCO_UNKNOWN` or `NO_DIRECT_FEE` in their Caveat, and do not establish workload cost. If a claim cannot be reproduced, use `SOURCE_LINKED_SNAPSHOT`, `UNVERIFIED`, or `STALE` as applicable. A provider-level badge never verifies all its services.

Snapshot migration is **not** a price refresh. Do not overwrite historical dates without checking current primary evidence. Avoid placeholder files and unnecessary automations.

The `Evidence checked` date is the last review date (UTC calendar date) for every evidence status. Active unresolved rows include one or more `RC1`–`RC7` cause codes in the Caveat cell; see the [evaluation matrix](01-evaluation-matrix.md). `DISCONTINUED` means the provider ended the offering. If only maintenance or distribution ended, say so and state whether existing installations remain usable. A future shutdown announcement remains an active lifecycle state until its effective date.

## Review and enforcement boundary

- Run the local validator and mutation tests before every catalog change: `python3 scripts/validate_catalog.py` and `python3 -m unittest discover -s tests -v`. GitHub Actions runs the same stdlib-only checks on pushes to `main`.
- Validation is **not** web research. Re-open official primary-source pages during a dated price review; record what was checked, not just whether the page responded. Reassess price, ToS, region, quota resets and provenance before production selection.
- For providers with shared subscriptions (e.g. Supabase, Vercel, Workers Paid), follow the billing scope in their provider SSOT. Never sum repeated per-offering descriptions of the same platform subscription, shared quotas or credits.
