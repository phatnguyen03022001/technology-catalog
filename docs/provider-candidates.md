# Provider candidates — discovery register and research disposition

**As of 2026-11-01:** 300 service offerings in 198 provider profiles; 1 active discovery-only watchlist candidate. Seven deferred candidates were reviewed: six were promoted into the catalog and ClickStack Cloud private preview remains deferred. Prices and current evidence stay in provider profiles. Service evidence status does not imply that every independently priced plan is verified.

## Pillar coverage

| Pillar | Service offerings | Non-VERIFIED offerings |
|---|---:|---:|
| [01 — Compute & Runtime](../pillars/01-compute-runtime/README.md) | 31 | 7 |
| [02 — Databases & Data](../pillars/02-databases-data/README.md) | 27 | 3 |
| [03 — Storage & Media](../pillars/03-storage-media/README.md) | 24 | 4 |
| [04 — Networking & Edge](../pillars/04-networking-edge/README.md) | 14 | 1 |
| [05 — Cache & Traditional Search](../pillars/05-cache-traditional-search/README.md) | 22 | 6 |
| [06 — Messaging & Async](../pillars/06-messaging-async/README.md) | 25 | 7 |
| [07 — Identity & Security](../pillars/07-identity-security/README.md) | 23 | 7 |
| [08 — DevOps & Delivery](../pillars/08-devops-delivery/README.md) | 30 | 2 |
| [09 — Observability & Analytics](../pillars/09-observability-analytics/README.md) | 22 | 2 |
| [10 — AI Models & Agent Tools](../pillars/10-ai-models-agent-tools/README.md) | 30 | 5 |
| [11 — Communications](../pillars/11-communications/README.md) | 24 | 6 |
| [12 — Business & Extension APIs](../pillars/12-business-extension-apis/README.md) | 28 | 3 |

Non-VERIFIED is a service-level evidence disposition. It does not count the number of separate price, quota or model claims within a row.

## Accepted market additions

71 market-discovery service offerings are recorded after comparing mainstream, specialized, lower-cost and self-hosted options against the existing taxonomy: 65 from the prior review and six promoted from the current discovery watchlist. MinIO AIStor is tracked as a lifecycle successor in the reconciliation section below, not counted as a market-discovery addition. Rationale is capability-based; each linked provider profile contains current official source URLs, explicit free-tier classification, paid-price qualification and evidence status. A row can be included while some claims remain unresolved.

| Pillar | Candidate | Why included | Provider SSOT / evidence | Evidence status |
|---|---|---|---|---|
| 01 | Akamai Cloud Compute | Adds a regional cloud compute alternative. | [Akamai](../providers/akamai.md) | `VERIFIED` |
| 01 | AWS Fargate | Adds managed container capacity alongside VM and function options. | [Amazon Web Services](../providers/amazon-web-services.md) | `VERIFIED` |
| 01 | AWS Lightsail | Adds a simpler VPS path for predictable small-server workloads. | [Amazon Web Services](../providers/amazon-web-services.md) | `VERIFIED` |
| 01 | Azure Container Apps | Adds managed container and scale-to-zero runtime coverage. | [Microsoft Azure](../providers/azure.md) | `VERIFIED` |
| 01 | Google Kubernetes Engine (GKE) | Adds managed Kubernetes for teams needing cluster control. | [Google Cloud & Firebase](../providers/google.md) | `VERIFIED` |
| 01 | Scaleway Instances | Adds a European cloud provider with self-service compute. | [Scaleway](../providers/scaleway.md) | `VERIFIED` |
| 01 | Vultr Cloud Compute | Adds a broad-region VPS option with a published low-entry SKU; promotion eligibility and regional invoice remain scoped. | [Vultr](../providers/vultr.md) | `UNVERIFIED` |
| 02 | Amazon Aurora DSQL | Adds a serverless distributed SQL architecture. | [Amazon Web Services](../providers/amazon-web-services.md) | `VERIFIED` |
| 02 | Amazon Aurora PostgreSQL Serverless | Adds elastic managed PostgreSQL for variable demand. | [Amazon Web Services](../providers/amazon-web-services.md) | `VERIFIED` |
| 02 | Azure Cosmos DB | Adds globally distributed multi-model NoSQL. | [Microsoft Azure](../providers/azure.md) | `VERIFIED` |
| 02 | Google Cloud SQL for PostgreSQL | Adds mainstream managed PostgreSQL with conventional SQL compatibility. | [Google Cloud & Firebase](../providers/google.md) | `VERIFIED` |
| 02 | Koyeb Serverless Postgres | Adds a small limited-free serverless PostgreSQL option with per-second paid compute. | [Koyeb](../providers/koyeb.md) | `VERIFIED` |
| 03 | Akamai Object Storage | Adds S3-compatible object storage from a global edge provider. | [Akamai](../providers/akamai.md) | `VERIFIED` |
| 03 | Cloudflare Stream | Adds managed video upload, encoding and delivery. | [Cloudflare](../providers/cloudflare.md) | `VERIFIED` |
| 03 | Oracle Object Storage | Adds a major cloud’s object storage and archive option. | [Oracle Cloud Infrastructure](../providers/oracle.md) | `VERIFIED` |
| 03 | Hetzner Object Storage | Adds S3-compatible object storage in European regions; its exact current base-price cap remains unresolved. | [Hetzner](../providers/hetzner.md) | `UNVERIFIED` |
| 03 | SeaweedFS | Adds an Apache-licensed, self-hosted distributed object/file store. | [SeaweedFS](../providers/seaweedfs.md) | `VERIFIED` |
| 04 | AWS WAF | Adds managed application-layer filtering to edge/network choices. | [Amazon Web Services](../providers/amazon-web-services.md) | `VERIFIED` |
| 04 | Google Cloud DNS | Adds authoritative DNS from a major cloud provider. | [Google Cloud & Firebase](../providers/google.md) | `VERIFIED` |
| 05 | Amazon ElastiCache for Valkey | Adds managed Valkey on AWS for teams already using its cloud. | [Amazon Web Services](../providers/amazon-web-services.md) | `VERIFIED` |
| 05 | Apache Solr | Adds an Apache-licensed self-hosted search engine. | [Apache Solr](../providers/apache-solr.md) | `VERIFIED` |
| 05 | Azure AI Search | Adds hosted full-text, vector and hybrid search. | [Microsoft Azure](../providers/azure.md) | `SOURCE_LINKED_SNAPSHOT` |
| 05 | Azure Managed Redis | Adds managed Redis-compatible cache for Azure workloads. | [Microsoft Azure](../providers/azure.md) | `UNVERIFIED` |
| 05 | Cloudflare Workers KV | Adds globally distributed edge key-value storage. | [Cloudflare](../providers/cloudflare.md) | `VERIFIED` |
| 05 | Dragonfly Cloud | Adds a managed, Redis-compatible cache alternative. | [Dragonfly](../providers/dragonfly.md) | `UNVERIFIED` |
| 05 | Google Memorystore for Valkey | Adds managed Valkey on Google Cloud. | [Google Cloud & Firebase](../providers/google.md) | `VERIFIED` |
| 05 | OpenSearch OSS | Adds Apache-licensed self-hosted search and analytics. | [OpenSearch Project](../providers/opensearch-project.md) | `VERIFIED` |
| 06 | AWS Step Functions | Adds managed durable orchestration with Standard and Express execution modes. | [Amazon Web Services](../providers/amazon-web-services.md) | `VERIFIED` |
| 06 | Azure Durable Task Scheduler | Adds stateful durable execution for Azure Functions and Durable Task SDKs; numeric regional scheduler rates remain unresolved. | [Microsoft Azure](../providers/azure.md) | `UNVERIFIED` |
| 06 | Azure Event Grid | Adds managed event routing and serverless event delivery. | [Microsoft Azure](../providers/azure.md) | `UNVERIFIED` |
| 06 | Azure Event Hubs | Adds managed high-throughput event streaming. | [Microsoft Azure](../providers/azure.md) | `UNVERIFIED` |
| 06 | Cloudflare Queues | Adds managed queueing near Workers runtimes. | [Cloudflare](../providers/cloudflare.md) | `VERIFIED` |
| 06 | Google Cloud Tasks | Adds managed HTTP task queues with retry scheduling. | [Google Cloud & Firebase](../providers/google.md) | `VERIFIED` |
| 06 | Google Cloud Workflows | Adds managed service orchestration and stateful steps. | [Google Cloud & Firebase](../providers/google.md) | `VERIFIED` |
| 06 | Synadia Cloud NATS | Adds managed NATS messaging for low-latency pub/sub. | [Synadia](../providers/synadia.md) | `VERIFIED` |
| 07 | Amazon Cognito | Adds a first-party managed authentication option for AWS apps. | [Amazon Web Services](../providers/amazon-web-services.md) | `VERIFIED` |
| 07 | Better Auth Infrastructure | Adds hosted infrastructure for the Better Auth ecosystem. | [Better Auth](../providers/better-auth.md) | `VERIFIED` |
| 07 | Keycloak | Adds a widely used Apache-licensed, self-hostable identity provider. | [Keycloak](../providers/keycloak.md) | `VERIFIED` |
| 07 | Microsoft Entra External ID | Adds Microsoft’s customer identity service. | [Microsoft Azure](../providers/azure.md) | `UNVERIFIED` |
| 07 | Permit MCP Gateway | Adds authorization and policy controls for MCP/agent tool calls. | [Permit.io](../providers/permit-io.md) | `VERIFIED` |
| 07 | Ory Network | Adds API-first hosted identity with production and development plans. | [Ory](../providers/ory.md) | `VERIFIED` |
| 08 | Amazon ECR Private | Adds private container image registry with AWS integration. | [Amazon Web Services](../providers/amazon-web-services.md) | `VERIFIED` |
| 08 | Amazon ECR Public | Adds public container image distribution from AWS. | [Amazon Web Services](../providers/amazon-web-services.md) | `VERIFIED` |
| 08 | AWS CodePipeline | Adds AWS-native release orchestration. | [Amazon Web Services](../providers/amazon-web-services.md) | `VERIFIED` |
| 08 | Azure Artifacts | Adds hosted package feeds for Azure DevOps. | [Microsoft Azure](../providers/azure.md) | `VERIFIED` |
| 08 | Azure Pipelines | Adds hosted CI/CD with Microsoft ecosystem integration. | [Microsoft Azure](../providers/azure.md) | `VERIFIED` |
| 08 | Bitrise Mobile CI | Adds managed mobile build pipelines, including Apple platforms. | [Bitrise](../providers/bitrise.md) | `VERIFIED` |
| 08 | Codemagic Mobile CI | Adds managed Flutter/mobile CI with macOS build capacity. | [Codemagic](../providers/codemagic.md) | `VERIFIED` |
| 08 | Docker Desktop | Adds the mainstream local container development workflow. | [Docker](../providers/docker.md) | `VERIFIED` |
| 08 | Google Artifact Registry | Adds hosted OCI and language package registries for Google Cloud. | [Google Cloud & Firebase](../providers/google.md) | `VERIFIED` |
| 08 | Jenkins | Adds a widely deployed self-hosted CI automation option. | [Jenkins](../providers/jenkins.md) | `VERIFIED` |
| 08 | OpenTofu | Adds an MPL-licensed, open-source Terraform-compatible IaC tool. | [OpenTofu](../providers/opentofu.md) | `VERIFIED` |
| 08 | Harbor Container Registry | Adds a self-hosted OCI registry with signing and vulnerability-scanning integrations. | [Harbor](../providers/harbor.md) | `VERIFIED` |
| 09 | ClickStack OSS | Adds a self-hostable OpenTelemetry observability stack with ClickHouse, HyperDX and the OTel Collector. | [ClickHouse](../providers/clickhouse.md) | `VERIFIED` |
| 09 | Dash0 Observability | Adds an OpenTelemetry-native managed observability option. | [Dash0](../providers/dash0.md) | `VERIFIED` |
| 09 | GlitchTip Cloud | Adds a Sentry-compatible error monitoring option with self-host lineage. | [GlitchTip](../providers/glitchtip.md) | `UNVERIFIED` |
| 09 | Managed ClickStack | Adds a GA managed observability service on ClickHouse Cloud with compute/storage billing. | [ClickHouse](../providers/clickhouse.md) | `VERIFIED` |
| 10 | Amazon Bedrock | Adds AWS-hosted third-party model inference with AWS billing and governance. | [Amazon Web Services](../providers/amazon-web-services.md) | `VERIFIED` |
| 10 | Gemini Enterprise Agent Platform | Adds managed Google agent/model platform coverage. | [Google Cloud & Firebase](../providers/google.md) | `VERIFIED` |
| 10 | Microsoft Foundry Models | Adds Azure-hosted model inference under Microsoft’s enterprise platform. | [Microsoft Azure](../providers/azure.md) | `VERIFIED` |
| 11 | Apple Push Notification service (APNs) | Adds the required first-party push channel for Apple devices. | [Apple](../providers/apple.md) | `UNVERIFIED` |
| 11 | Telnyx Email API | Adds transactional and bulk email on Telnyx communication APIs; GA is announced but current pricing still carries a Beta label. | [Telnyx](../providers/telnyx.md) | `UNVERIFIED` |
| 11 | WhatsApp Business Platform Cloud API | Adds official WhatsApp messaging for business communication. | [Meta](../providers/meta.md) | `UNVERIFIED` |
| 11 | ntfy.sh Hosted Notifications | Adds a low-friction HTTP pub/sub notification service with a no-signup hosted tier and self-hosted option. | [ntfy](../providers/ntfy.md) | `VERIFIED` |
| 12 | HubSpot CRM | Adds an accessible CRM and extension API for small teams. | [HubSpot](../providers/hubspot.md) | `VERIFIED` |
| 12 | Plaid Link and Data API | Adds financial-account connectivity for fintech integrations. | [Plaid](../providers/plaid.md) | `UNVERIFIED` |
| 12 | Salesforce CRM | Adds an enterprise CRM and extension API baseline. | [Salesforce](../providers/salesforce.md) | `VERIFIED` |
| 12 | Square Payments API | Adds payments APIs with commerce and point-of-sale ecosystem coverage. | [Square](../providers/square.md) | `VERIFIED` |
| 12 | Stripe Tax | Adds transaction and tax calculation APIs adjacent to payments. | [Stripe](../providers/stripe.md) | `VERIFIED` |
| 12 | Zoho CRM | Adds a lower-cost CRM and extension API alternative. | [Zoho](../providers/zoho.md) | `VERIFIED` |
| 12 | Persona Identity Verification (KYC) | Adds configurable identity checks and an application-based startup program; production per-check scope remains unresolved. | [Persona](../providers/persona.md) | `UNVERIFIED` |

## Product-name and lifecycle reconciliation

These changes retain identity/history for the original catalog while separating rebrands or distinct product lifecycle states. They are not counted as market additions.

| Original record | Current record(s) | Disposition | Provider SSOT |
|---|---|---|---|
| HashiCorp Vault | IBM Vault Community Edition; HCP Vault Dedicated; HCP Vault Secrets | Separate source-available community software, paid hosted vault, and retired secrets service. | [HashiCorp / IBM](../providers/hashicorp.md) |
| MinIO | MinIO OSS; MinIO AIStor | Mark the legacy OSS service discontinued and track its maintained successor separately. | [MinIO](../providers/minio.md) |
| Neon Postgres | Neon Lakebase Postgres | Updated product naming and boundary under the same provider. | [Neon](../providers/neon.md) |
| Timescale Cloud | Tiger Cloud (TimescaleDB) | Updated product naming under the same provider. | [Timescale](../providers/timescale.md) |

## Deferred and rejected candidates

Deferred items remain watchlist records with no public-price assertion. Rejected items were reviewed for this catalog cycle and are not active watchlist candidates. Revisit if first-party product terms or a material capability change.

| Candidate | Decision | Reason | First-party discovery source |
|---|---|---|---|
| ClickStack Cloud (private preview) | Deferred | The distinct hosted endpoint remains private preview and its price is not finalized; Managed ClickStack is GA and listed separately. | [Official site](https://clickhouse.com/blog/clickstack-cloud-private-preview) |
| Manticore Search | Rejected for this cycle | Overlaps with indexed search choices and no distinct, evidence-backed cost or capability advantage was established. | [Official site](https://manticoresearch.com/) |
| Sphinx Search | Rejected for this cycle | Current release and licensing terms were not sufficiently reproducible for a maintained-service profile. | [Official site](https://sphinxsearch.com/) |

[Provider SSOT](../providers/README.md) · [Taxonomy](00-taxonomy.md) · [Evaluation matrix](01-evaluation-matrix.md) · [Lifecycle](lifecycle.md).
