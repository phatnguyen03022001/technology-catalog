# Third-party taxonomy — WHAT / HOW / LIFECYCLE

The [programming language profiles](../languages/README.md) cover languages, runtimes, toolchains and frameworks **outside** service-offering classification. They do not create a thirteenth pillar or duplicate provider cost evidence. See [framework profiles](../frameworks/README.md) and [workload-specific decision records](../decisions/README.md); decisions without measured costs or required gates are conditional, not production-approved.

## WHAT — 12 Functional Pillars

| # | Pillar | Scope |
|---|---|---|
| 01 | [Compute & Runtime](../pillars/01-compute-runtime/README.md) | VPS, server, container, serverless, edge runtime, isolated agent sandboxes |
| 02 | [Databases & Data](../pillars/02-databases-data/README.md) | RDBMS, NoSQL, key-value, document DB, vector database |
| 03 | [Storage & Media](../pillars/03-storage-media/README.md) | Object storage, file/media processing and storage |
| 04 | [Networking & Edge](../pillars/04-networking-edge/README.md) | DNS, CDN, WAF, DDoS, load balancing |
| 05 | [Cache & Traditional Search](../pillars/05-cache-traditional-search/README.md) | Cache and traditional keyword/full-text search |
| 06 | [Messaging & Async](../pillars/06-messaging-async/README.md) | Queues, pub/sub, durable async jobs and webhooks |
| 07 | [Identity & Security](../pillars/07-identity-security/README.md) | Auth, identity, authorization, secrets, KMS |
| 08 | [DevOps & Delivery](../pillars/08-devops-delivery/README.md) | CI/CD, registries, IaC and deployment tools |
| 09 | [Observability & Analytics](../pillars/09-observability-analytics/README.md) | System telemetry, analytics and LLM/agent tracing and evaluations |
| 10 | [AI Models & Agent Tools](../pillars/10-ai-models-agent-tools/README.md) | Model, embeddings, voice, web intelligence, scraping, retrieval tools |
| 11 | [Communications](../pillars/11-communications/README.md) | Email, SMS, push and chat APIs |
| 12 | [Business & Extension APIs](../pillars/12-business-extension-apis/README.md) | Payments, billing, maps, CMS, KYC, CRM |

## HOW — 8 Evaluation Dimensions

| ID | Dimension | Questions to answer |
|---|---|---|
| D1 | Discovery & Evaluation | Market coverage, fit, availability, credible source |
| D2 | Integration & Contracts | API/SDK, schemas, versioning, webhook, compatibility |
| D3 | Security & Data Governance | Auth/secrets, privacy, isolation, data retention, region, compliance, licensing |
| D4 | Reliability & Resilience | SLA, incident history, timeout, retry, idempotency, fallback |
| D5 | Performance & Scalability | p50/p95/p99 measured latency, throughput, concurrency, cold start, quotas |
| D6 | Cost & Quota Optimization | Tier eligibility/reset, units, pricing, credits, egress, TCO |
| D7 | Observability & Operations | Logs, metrics, alerts, system and agent traces/evals |
| D8 | Lifecycle & Exit Strategy | Upgrades, deprecation, export, portability, migration, rollback |

## LIFECYCLE

`Research → Evaluate/Compare → Select → Integrate → Operate/Monitor → Migrate/Retire`.

## Primary classification & SSOT rules

1. **Unit:** Provider → Service offering → **one primary pillar** + optional capability tags. Same provider can have multiple offerings under different pillars; one provider file stores all service pricing.
2. Vector databases (Qdrant, Pinecone, pgvector, Weaviate) primary **02**; similarity search is a capability tag, not a reason for duplicate data.
3. Redis/Key-Value managed caching offering primary **05**; durable DB offering primary **02**; classify distinct service *offering*, not brand.
4. Secure agent code sandbox/runtime primary **01**, measured for isolation, network egress, secret protection, ephemeral persistence, cold-start latency and resource ceilings.
5. Agent tool / web intelligence (Tavily, Exa, Firecrawl, search/scrape APIs) primary **10**. Generic browser runtime can be **01** if it is a distinct paid offering.
6. LLM/agent tracing and eval are **09**, alongside traditional APM. Trace available tool/model calls, timings, usage and evaluation; do not imply access to hidden chain-of-thought.
7. Object storage/media is **03**, CDN/WAF/DNS **04**, messaging/queues **06**, communications delivery **11**, business APIs **12**.
8. Self-host OSS license cost $0 ≠ free hosting/operations. Provider pricing and claims remain within `providers/` exclusively.

## Source ownership

- `providers/<provider>.md`: authoritative provider-level inventory with service-level prices, free tiers, official links, risks and as-of date.
- `pillars/<id>/README.md`: navigation and watchlist, **no duplicated price data**.
- `docs/provider-candidates.md`: research summary/navigation, **no duplicated price data**.
- `docs/01-evaluation-matrix.md`: scoring and non-negotiable gates.
- `docs/lifecycle.md`: change control, verification and exit.
