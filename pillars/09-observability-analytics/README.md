# 09 — Observability & Analytics

**Scope:** System telemetry, analytics and LLM/agent tracing and evaluations.

[Taxonomy](../../docs/00-taxonomy.md) · [Evaluation matrix](../../docs/01-evaluation-matrix.md)

## Discover by measurement purpose

These are **distinct use cases within the existing pillar**, not additional pillars or duplicate provider records.

| Purpose | What to evaluate | Existing entry points |
|---|---|---|
| Operational observability | Application logs, metrics, traces, errors, alerts, performance and reliability | [Grafana Cloud](../../providers/grafana.md), [Sentry](../../providers/sentry.md), [Honeycomb](../../providers/honeycomb.md) |
| Product analytics and feedback | Explicit user events, feature usage/adoption, funnels, retention, cohorts and product outcomes | [PostHog Product/AI Obs](../../providers/posthog.md) |
| AI/agent observability and evaluation | Model/tool traces, usage, failures and evaluation of agent behavior | [Langfuse](../../providers/langfuse.md), [LangSmith](../../providers/langsmith.md), [Braintrust](../../providers/braintrust.md) |

**Boundary:** Operational telemetry shows whether software works reliably; product analytics measures how product features are used and whether intended outcomes occur. Neither proves the other. Product events do not require replacing application logs, and telemetry packages under [Libraries — C18 Observability](../../libraries/README.md) do not mandate a hosted analytics provider or imply complete product instrumentation.

**Product measurement gates, not verified provider features:** Define meaningful events and success metrics before tracking; assess event schemas, attribution, funnels/retention, experimentation or A/B tests, feature flags (only if needed), privacy and consent, data minimization, access controls, retention and deletion. Verify each required feature and its pricing against current official evidence for the selected offering; this index does **not** assert that every tool supports all of them. Do not enable tracking by default or infer product success from event volume.

## Service index (facts in providers/)

| Service offering | Provider SSOT |
|---|---|
| Arize Phoenix | [Arize Phoenix](../../providers/arize-phoenix.md) |
| Axiom | [Axiom](../../providers/axiom.md) |
| Better Stack | [Better Stack](../../providers/better-stack.md) |
| Braintrust | [Braintrust](../../providers/braintrust.md) |
| ClickStack OSS | [ClickHouse](../../providers/clickhouse.md) |
| Dash0 Observability | [Dash0](../../providers/dash0.md) |
| Datadog | [Datadog](../../providers/datadog.md) |
| GlitchTip Cloud | [GlitchTip](../../providers/glitchtip.md) |
| Grafana Cloud | [Grafana](../../providers/grafana.md) |
| Helicone | [Helicone](../../providers/helicone.md) |
| Honeycomb | [Honeycomb](../../providers/honeycomb.md) |
| Langfuse Cloud | [Langfuse](../../providers/langfuse.md) |
| LangSmith | [LangSmith](../../providers/langsmith.md) |
| Logfire (Pydantic) | [Logfire](../../providers/logfire.md) |
| Managed ClickStack | [ClickHouse](../../providers/clickhouse.md) |
| New Relic | [New Relic](../../providers/new-relic.md) |
| OpenLIT | [OpenLIT](../../providers/openlit.md) |
| OpenObserve | [OpenObserve](../../providers/openobserve.md) |
| PostHog Product/AI Obs | [PostHog](../../providers/posthog.md) |
| Promptfoo | [Promptfoo](../../providers/promptfoo.md) |
| Sentry | [Sentry](../../providers/sentry.md) |
| SigNoz | [SigNoz](../../providers/signoz.md) |

## Watchlist — 1 chưa xác minh giá/free tier

| Candidate | Status | Note |
|---|---|---|
| ClickStack Cloud (private preview) | Deferred | Separate waitlist-only hosted endpoint remains in private preview and has no finalized public price; ClickStack OSS and GA Managed ClickStack are cataloged separately. |
