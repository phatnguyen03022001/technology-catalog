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

## Evidence freshness and upstream change monitoring (UTC)

Four separate dimensions: **evidence status** (claim scope), **freshness** (days since real verification), **upstream change** (machine-readable signals), and **production readiness** (workload-specific hard gates). Never equate them.

- **CURRENT** = 0–30 UTC calendar days after real evidence review; **REVERIFY_REQUIRED** = over 30 days; report a warning but do not downgrade or delete existing VERIFIED claims. **STALE** = a confirmed invalid claim, no current recommendation. **UNKNOWN** = missing date or unsupported source signal. **CHECK_FAILED** = API unreachable/malformed; do not infer no change. **UPSTREAM_CHANGED** = new release, version mismatch or newly published advisory; **SECURITY_REVIEW_REQUIRED** = an advisory matching a referenced version that pre-dates the last review and still requires checking affected symbols; requires impact review. A newer release is not evidence that older installs are unsafe.
- Frozen tests use `--as-of`; production uses the UTC day. Invalid/future verification dates fail. Keep the current **180-day hard gate** for VERIFIED provider claims. Age >30 alone never fails CI.
- `python3 scripts/monitor_upstream.py` computes all evidence freshness without network, reading the existing Markdown SSOT. `python3 scripts/monitor_upstream.py --check-upstream --security` queries supported official registries/releases and OSV for version-scoped advisory signals, without changing any file or verification timestamp. Add `--all-unknown` to print per-record sources when inspecting complete manual-review coverage.
- GitHub Actions push checks freshness; Tuesday 03:17 UTC schedule and manual `workflow_dispatch` also perform upstream checks and publish GitHub Actions Step Summary. No automated commits, package bumps, issues, or notifications; schedule timing can slip or be disabled in inactive repositories.
- **Monitored:** Rust crates.io, Go module proxy, npm registry, PyPI and Swift upstream GitHub releases, comparing library versions recorded in the canonical entries; frameworks with upstream GitHub release APIs compare latest publication date to their review day (signals only after that day, not claimed version compatibility). OSV is version-scoped for Rust/Go/npm/PyPI. Swift advisory mapping is currently UNKNOWN. A module-level OSV match (notably Go modules) does not prove the project imports an affected subpackage or symbol; use project-specific dependency and symbol checks.
- **Not reliably automatically monitored:** provider pricing, quotas, free tiers, Terms of Service; languages/toolchain docs, decision workload facts; frameworks without a GitHub release feed. These need real manual source re-verification. A successful HTTP request is not claim review. Release-only comparisons cannot detect all breaking changes, license changes, deprecations, vulnerabilities or documentation updates.
- **Agent consumption:** select exact workload and canonical record; inspect claim status, age ≤30, change signal, runtime compatibility, security advisories, licensing and relevant hard gates. If any material claim is REVERIFY_REQUIRED, UPSTREAM_CHANGED, SECURITY_REVIEW_REQUIRED, STALE, CHECK_FAILED or UNKNOWN, verify current primary source before a production recommendation; log assumptions, evidence URLs, UNKNOWNs, fallback and exit strategy. Even CURRENT/VERIFIED/CI SUCCESS does not grant production approval.
- **Safe updates:** upstream signal → determine affected claims → inspect official release notes, changelog, runtime/platform support, licensing and security → evaluate trade-offs against existing dependency → update only affected SSOT Markdown after actual review, including review date as appropriate → run validator and regression → commit. Never automatically refresh review date based on 200 OK or blindly migrate/bump a dependency.
