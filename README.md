# technology-catalog

Evidence-based technology catalog for **Fullstack + AI + Agentic** software engineering: programming languages and third-party services.

## Navigation

| Layer | Responsibility | Link |
|---|---|---|
| LANGUAGES | Rust, Go, TypeScript, Python, Swift: toolchains, frameworks, fit, trade-offs and decision gates | [languages/](languages/README.md) |
| LIBRARIES | Curated reusable packages, fit/anti-fit, compatibility, licensing, evidence and fallback | [libraries/](libraries/README.md) |
| FRAMEWORKS | Framework fit, anti-fit, compatibility, licensing, maturity/review risk and sources | [frameworks/](frameworks/README.md) |
| DECISIONS | Workload-based comparisons, hard gates, conditional decisions, TCO unknowns and fallback | [decisions/](decisions/README.md) |
| WHAT | 12 functional pillars, service classifications, research watchlists | [pillars/](pillars/README.md) |
| HOW | 8 evaluation criteria and comparison matrix | [taxonomy](docs/00-taxonomy.md) · [matrix](docs/01-evaluation-matrix.md) |
| LIFECYCLE | Research → Compare → Select → Integrate → Operate → Retire | [lifecycle](docs/lifecycle.md) |
| PROVIDERS | Single Source of Truth for multi-service provider facts, free tier, prices, sources | [providers/](providers/README.md) |
| DISCOVERY | Summary and pending candidates | [research index](docs/provider-candidates.md) |
| STACK RESEARCH | Conditional free-tier selection for Next.js + Go + Python; billing, runtime and recovery limits | [free-tier stack selection](docs/free-tier-stack-selection.md) |

**Catalog snapshot:** 2026-11-01 — 12 pillars; 198 provider profiles; 300 service offerings; 1 discovery-only watchlist candidate.

**Scope boundary:** Languages, libraries and frameworks are separate from the 12 service pillars, not additional offerings. Profiles do not duplicate provider prices/free tiers or override ECC implementation guidance.

**Governance:** One provider profile, multiple service offerings (each exactly one primary pillar). Prices live in provider files only. Each service row carries its own evidence status and verification date. Read `VERIFIED` as confirmation of the specific listed claims only; structural validation does not prove pricing accuracy. Re-check live limits, quota period, commercial restrictions, privacy and tax/region before procurement/production. No unsupported ranking.

## Validation

`python3 scripts/validate_catalog.py` and `python3 -m unittest discover -s tests -v`; GitHub Actions enforces both on `main` pushes. These are deterministic integrity/evidence-hygiene checks, **not** proof of current pricing or production suitability. Freshness warnings: `python3 scripts/monitor_upstream.py`; live read-only release and advisory checks: `python3 scripts/monitor_upstream.py --check-upstream --security`. [Freshness governance](docs/lifecycle.md#evidence-freshness-and-upstream-change-monitoring-utc). See [cost decision readiness](docs/01-evaluation-matrix.md#cost-decision-readiness-separate-from-evidence-status).
