# Browserbase

> **Provider SSOT.** Service claims and price evidence are recorded per offering below. `SOURCE_LINKED_SNAPSHOT` is not a current-price verification.

**Offerings:** 2 · **Pillars:** [01](../pillars/01-compute-runtime/README.md), [10](../pillars/10-ai-models-agent-tools/README.md)

| Service | Primary pillar | Free kind | Free tier/credits | Paid pricing | Caveat | Official source | Evidence status | Evidence checked |
|---|---|---|---|---|---|---|---|---|
| Browserbase Browser Runtime | 01 | `LIMITED_FREE` | Free: 1 browser-hour, 3 concurrent browsers, 15 minutes/session and 7-day retention. | Developer $20/month includes 100 browser-hours and 25 concurrent browsers; overage $0.12/browser-hour. Includes 1 GB proxy traffic, then $12/GB. | Current pricing page does not list the former one-minute session minimum; no such minimum is asserted. Search/Fetch calls and Model Gateway tokens have separate included allowances and overage rates. | [Browserbase pricing](https://www.browserbase.com/pricing) | `VERIFIED` | 2026-11-01 |
| Browserbase Search/Fetch | 10 | LIMITED_FREE | Free: 1,000 Search and 1,000 Fetch calls, one browser-hour and three concurrent browsers. | Developer $20/month; after included allowance Search $5/1K calls and Fetch $1/1K calls. | Search/Fetch is distinct from Browser Runtime sessions/proxy; remove unsupported one-minute session minimum. | [Browserbase pricing](https://www.browserbase.com/pricing) | VERIFIED | 2026-11-01 |

## Evidence & maintenance

- Score: `NOT_EVALUATED` — workload, legal/security checks, benchmarks and price region are not yet supplied.
- Update pricing and source **here only**; pillar pages should never duplicate provider prices.
- [Evaluation matrix](../docs/01-evaluation-matrix.md) · [Lifecycle](../docs/lifecycle.md)
