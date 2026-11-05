# Free-tier infrastructure selection — Next.js + Go + Python

**Status:** CONDITIONAL_NOT_PRODUCTION · **Verified:** 2026-11-05 · **Baseline:** `47fcb0a83ff989661f16d57f6e7df59722b021b3`.

Reference study, not an application deployment, capacity benchmark, procurement approval or new project decision. No infrastructure was provisioned. Framework/language decisions remain unchanged. [Provider profiles](../providers/README.md) remain the sole canonical source for provider prices and quotas; figures in worked calculations below are derived scenario results, not a second pricing catalog. Re-open the linked profiles and official pages before implementation.

## 1. Verdict and assumptions

**Default for a real product: Cloud Run for ordinary Next.js/Node and Go containers, Neon PostgreSQL, Better Auth in the existing Next.js app, Cloudflare R2 for audio/images, GitHub Actions for CI and repository-bound Python content builds, Resend only when verification/recovery email is required.** Use Cloud Run Jobs for actual application processing, not Actions as an online worker. Begin on recurring free allowances, but accept a small PAYG network bill. Plan around a $0–5 operating target, not a contractual cap. Upgrade one bottleneck at a time.

**Best strict-free Next.js candidate is Netlify Free**, not Vercel Hobby. Netlify wins compatibility and no-bill behavior for a small SSR app; its credit pool is a serious ceiling. **Cloud Run wins integrated runtime hosting** because it keeps the ordinary Node/Go/Python toolchains and removes a hosting vendor. This trades free CDN delivery for metered network traffic and additional cache/build responsibility. No fully evidenced, hard-capped, production-ready $0 stack is established for the English reference workload.

| Workload | Planning assumptions | What is not established |
|---|---|---|
| A: lightweight MVP | Next.js with SSR capability; Go HTTP/JSON; one PostgreSQL database; one identity system; static audio/images; GitHub CI; no worker required | Requests, SSR CPU, DB active time, payload sizes, availability/recovery objectives |
| B: three runtimes | A plus bounded Python content processing; actual asynchronous application jobs only if required | Job duration/frequency, native dependencies, retries and scheduling SLA |
| C: English reference | About 1,000 users and 50–100 peak concurrent learners; Vietnam-first, online-only; learner history; no model training | MAU vs DAU, monthly sessions, read/write amplification, p95 latency, recovery performance |

Concurrency is not a monthly consumption measurement. No statement here proves these plans can serve C. Initial placement proposal is Singapore for app and database, with R2 APAC placement hint for public media. Same city across GCP and AWS is still cross-provider networking; R2 hints are not jurisdiction guarantees. No Vietnam-only residency requirement was supplied.

## 2. Catalog audit and classification

All shortlisted providers already exist. No new provider, service ID, pillar, framework or decision record is necessary. Existing evidence dates were not blindly refreshed. Only concrete omissions/incorrect scope in selected provider rows were corrected: R2 billing/development URL; Cloud Run spend-cap scope and egress; Koyeb signup charges; Supabase backups/default SMTP; Netlify ambiguous paid floor; Neon suspension/cost controls; GitHub standard-runner and policy scope; Resend inbound/recipient quota and paid-overage behavior.

Use the [canonical classifications](lifecycle.md), not new enum values:

| Research label | Canonical kind | Interpretation |
|---|---|---|
| PERMANENT FREE | PERMANENT | Recurring allowance without a published fixed trial expiry; terms can still change |
| LIMITED FREE | LIMITED_FREE | Recurring offer with substantial eligibility/feature restrictions |
| RECURRING CREDIT | RECURRING_CREDIT | Renewed monetary credit, applied once per billing owner |
| ONE-TIME CREDIT | ONE_TIME_CREDIT | Finite signup grant, excluded from sustainable cost estimates |
| TRIAL | TIME_LIMITED_TRIAL | Fixed expiry, excluded from sustainable hosting |
| PAY-AS-YOU-GO | Attribute of paid pricing, not a new Free-kind enum | Can coexist with a permanent free allowance, as on Cloud Run/R2 |
| SELF-HOSTED | SELF_HOSTED | Software license only; hosting, database and operations remain payable |
| UNKNOWN | UNKNOWN | Evidence does not establish entitlement |

Railway retains `PERMANENT_AFTER_TRIAL`: its ongoing monetary credit must be distinguished from signup credit. Koyeb retains the existing PERMANENT record classification, but its production exclusion is material; for this selection it is **restricted free**, not an unrestricted production offer. Public pricing is not a promise that any given account/region can be provisioned.

## 3. Runtime compatibility and hosting comparison

### Next.js

| Deployment | App Router / RSC / Server Actions / SSR / routes | Node, middleware, rendering, images | Delivery/build/rollback and verdict |
|---|---|---|---|
| [Netlify](../providers/netlify.md), OpenNext | Officially supported; SSG/ISR/streaming also documented | Node functions; middleware order differs; Node middleware cannot use filesystem/C++ addons; edge SSR executes in the function region. Image CDN supported | Git builds, previews and deploy rollback; one shared credit pool also meters traffic/compute/production deploys. **Free SSR winner**, conditional on exact app test |
| [Cloudflare](../providers/cloudflare.md) Workers, vinext | Most common features supported, but vinext reimplements the Next API on Vite | Official default is now **vinext beta**; `next/*` mostly supported and image optimization partial. This is not unmodified `next build` | Edge delivery and Worker versions/rollback; verify compatibility dashboard, CPU, memory, bundle and cache bindings. **Runner-up free edge candidate**, not universal production equivalence |
| Cloudflare Workers, OpenNext | Official table supports App/Pages Router, RSC, SSR, SSG, ISR, Actions, route handlers, streaming | Manual alternate path for existing apps; Node.js middleware still listed unsupported; Images is a separate product. Native Node addons/process assumptions need review | Do not repeat the old claim that OpenNext is the current default. Existing official adapter docs and platform limits can diverge; test a pinned application/adapter pair |
| Cloudflare Pages static export | Static assets only | No request-time SSR, Actions, server routes or request middleware; dynamic functionality must move elsewhere | Excellent if the application explicitly gives up runtime SSR; **not equivalent** to the required full Next deployment |
| [Vercel](../providers/vercel.md) | First-party Next integration and managed images/caching | Best convenience for Next-specific behavior | **Hobby fails commercial gate**. Pro is a paid alternative, not a $0 default; check seats, included usage and spend settings |
| [Google Cloud Run](../providers/google.md), ordinary Node container | Normal Next.js server deployment supports full framework behavior | Native Node APIs and `next/image`; container filesystem/cache is ephemeral. Multi-instance ISR invalidation, Actions encryption keys and version skew need explicit handling | OCI image/revision rollback, no adapter replacement. Registry/build/network/logs are separate meters. **Integrated default**, not guaranteed free traffic |
| [Render](../providers/render.md) / [Koyeb](../providers/koyeb.md) | Ordinary Node or Docker can run Next | Free CPU/RAM/sleep limits apply | Provider says free compute is not for production. Not selected merely to avoid a bill |

Cloudflare's live limits page now lists a larger Worker bundle allowance than older OpenNext guidance. The exact applicability to a built app is **CONFLICTING / NOT VERIFIED** until deployed; do not use historical adapter bundle limits as current universal platform facts. CPU/memory are still independent constraints. Build success locally does not establish Worker compatibility. Free images/storage quota must not be counted as the same meter as Worker invocations.

### Go and conventional Python APIs

| Candidate / verified free class | Runtime and network fit | Availability, region, operations | Selection |
|---|---|---|---|
| Cloud Run: PERMANENT allowance + PAYG | Native Linux Go binary in OCI image; normal Python/FastAPI/ASGI; managed HTTPS, HTTP streaming/WebSocket. Services listen on injected PORT; amd64 image required by current contract | Scale to zero with cold starts; configurable concurrency/resource/request limits; Singapore available. Ephemeral local disk; outbound DB traffic and connections matter | **Go and live Python API winner**. Request billing CPU is not a license to run work after sending the response |
| Koyeb: restricted recurring free | Native Go/Python build or Docker; HTTP service only on free instance | One free instance; free regions are US/EU, sleeps after inactivity, no free worker or volume. Card/signup default can charge Pro | **Reject production Free**. Paid Singapore eco compute is an alternative only after full organization/egress quote |
| Render: LIMITED FREE | Go/Python/Docker HTTP apps; WebSocket supported | Free services spin down; startup can be slow; workspace instance-hour pool is shared; ephemeral disk and no free persistent worker. Free Postgres expires | **Reject production Free** per provider guidance. Paid compute is a runner-up when predictable always-on behavior is needed |
| [Oracle](../providers/oracle.md): PERMANENT Always Free, separate trial | ARM VM can run Go/Node/Python containers; ARM wheels/images must match | Home-region capacity can be unavailable; idle resources can be reclaimed. Requires OS patching, TLS/network/firewall, monitoring and off-instance backups | Generous VM resources do not beat managed service operational simplicity. **Not default**, especially for one maintainer |
| [Fly.io](../providers/fly.md): TRIAL then PAYG | Real containers/binaries; useful regional control | Current new-account trial is finite and stops machines; continuing requires payment | Paid alternative, **not recurring-free hosting** |
| [Railway](../providers/railway.md): PERMANENT_AFTER_TRIAL | Ordinary Go/Python/Node containers; optional sleep | Small monthly credit can fund short experiments; persistent volumes and transfer consume it too. Trial network restrictions differ from paid | Meaningful low-cost comparison, **not evidence of a free three-service production app** |
| [Northflank](../providers/northflank.md): LIMITED FREE Sandbox | Real containers, jobs and DB add-on | Always-on marketing is not production eligibility. Official billing docs exclude production Sandbox; existing catalog also flags a security incident | **Reject production Sandbox**. Incident resolution was not independently established here; do not infer current closure or reopen old secret exposure as a new finding |
| Cloudflare Workers | Go via Wasm, Python via Pyodide/CPython compiled to Wasm | Package/FFI/runtime limits differ from a Linux process; Python FastAPI support does not establish arbitrary native ML wheels | **Fails fit for an unchanged Go server / general Python process**. Containers are a distinct paid product; not free conventional compute |

For Cloud Run, set minimum instances to zero initially, bound maximum instances and DB pool size, then tune concurrency with actual load. WebSocket/SSE connections occupy billable request time; reconnect and backpressure are required. Request timeout is bounded (currently up to 60 minutes), so this is not an indefinite connection guarantee. Background work belongs in Jobs or an explicitly funded worker pool. A continuously allocated worker/minimum instance can exhaust free usage even with few users.

### Python execution by workload

| Need | First choice | Runner-up / restriction |
|---|---|---|
| Build, validate and publish editorial content associated with its software/content repository | [GitHub Actions](../providers/github.md), bounded Linux jobs | Existing authorized execution environment. Actions is not a general-purpose commercial serverless backend or content CDN |
| Scheduled editorial build | Actions schedule when delay/missed run is tolerable | Schedule can be delayed/dropped; public inactive-repo schedules disable. Use manual dispatch/retry and immutable outputs |
| Customer-triggered async processing or stronger scheduling requirement | Cloud Run Jobs; authenticated invocation and external scheduler only when needed | Reuse GCP account; durable job status/idempotency in the existing PostgreSQL database. No Redis/queue vendor by default |
| Live Python API genuinely required | Cloud Run service | Paid Render/Koyeb; do not add FastAPI merely to call a hosted model API that Go already supports |
| CPU-heavy or native ML batch beyond CI purpose | Cloud Run Jobs | [Modal](../providers/modal.md) when its compute/runtime advantages justify another vendor; compare end-to-end job cost |
| GPU inference/training | None required for A–C | Modal recurring credit is a conditional experiment budget, not free unlimited GPU. Model/license, VRAM, cold start, region and spend controls need validation |
| Demo ML space | [Hugging Face](../providers/hugging-face.md) Spaces considered, not selected | Current docs require a paid plan to create ordinary compute Spaces despite no hourly CPU Basic price. Sleep, ephemeral disk and network-port limits apply; special GPU grants are conditional |
| Persistent worker | No substantiated free default | Run-to-completion jobs are preferable when possible. If uninterrupted processing is required, budget paid compute explicitly |

Modal's Starter monetary credit is recurring, but it requires a payment method and automatically bills beyond applicable credit. Workspace budget/spend-limit controls differ from environment compute budgets; apply credit once, across the workspace. No account was inspected. Its no-fee/business/service-access terms also need exact workload review before a customer-facing ML endpoint. HF Inference Providers credit is separate from Spaces compute; neither establishes free GPU production capacity.

## 4. Data, identity, media and supporting services

| Layer / candidate | Fit, free class and exit | Main restriction and verdict |
|---|---|---|
| [Neon](../providers/neon.md) PostgreSQL | PERMANENT; ordinary PostgreSQL, pooled connections, Singapore; pg_dump/restore and standard migrations | Compute/transfer exhaustion suspends access; mandatory idle scale-to-zero. Small storage and short restore window. **Database winner** for portable SQL and a small incremental paid path |
| [Supabase](../providers/supabase.md) PostgreSQL/Auth | PERMANENT; Singapore; PostgreSQL plus hosted JWT auth and storage in one provider | Inactive project pause, shared egress and small database; Free lacks automatic daily backup. Production email needs custom SMTP. **Runner-up and managed-auth winner** if operational convenience outweighs its paid organization floor |
| [Aiven](../providers/aiven.md) PostgreSQL | Recurring free; ordinary PostgreSQL, backups and logs | Free region cannot be selected, no managed pooling, low connection cap and inactive service shutdown. Region/backup restore applicability remains UNKNOWN. Not default for Vietnam-first traffic |
| Cloudflare D1 | PERMANENT; SQLite-based SQL with export/time travel | **Fails PostgreSQL-semantics gate**; don't silently replace PostgreSQL types, extensions, locking or wire protocol |
| [Turso](../providers/turso.md) | PERMANENT; SQLite/libSQL-oriented product, attractive storage/read allowances | Also **fails required PostgreSQL semantics**. Reconsider only after product/schema explicitly accepts SQLite; no second database added |
| Better Auth in existing Next.js | SELF_HOSTED MIT library; one session authority, PostgreSQL user/session tables | **Default auth approach**, not free managed auth. Team owns updates, secure cookies/CSRF, recovery and abuse controls; use its JWT/JWKS plugin only for Go interoperability |
| Supabase Auth | Same platform as runner-up DB | Best if already choosing Supabase; then **do not add Better Auth or Clerk** for the same learners. Verify JWT and enforce ownership in Go; direct SQL does not automatically inherit browser RLS context |
| [Clerk](../providers/clerk.md) | PERMANENT recurring allowance; managed UI/session flow, Go token validation | MRU differs from MAU, export and paid authorization features need review; another vendor if database is elsewhere. Runner-up when managed auth saves more operational cost than it adds |
| Cloudflare R2 Standard | PERMANENT allowance + PAYG; S3-compatible SDKs for TS/Go/Python, private objects/presigned S3 URLs; public custom-domain CDN | **Media winner** for audio-heavy delivery. No egress fee is not no invoice: operations/storage still bill. No invoice hard cap established. Presigned S3 URL is not automatically a CDN-protected custom-domain URL |
| Supabase Storage | PERMANENT; built-in JWT policies and signed links | Simplest for a tiny library already using Supabase. Storage traffic competes in organization egress; larger audio libraries justify R2 |
| [Backblaze B2](../providers/backblaze.md) | PERMANENT allowance + PAYG; S3-compatible, alternative backup/media target | Free egress is conditional on storage ratio or partner route; not unconditional like R2 egress. Cost cap/region configuration not verified. Runner-up, especially for an independent backup copy |
| DNS/CDN | Cloudflare DNS; R2 custom-domain caching for public media; host's own TLS | No extra CDN subscription required; domain registration/renewal is a separate real cost. Don't cache private learner responses or proxy audio through application containers |
| CI, images, secrets | GitHub Actions; existing GCP registry for Cloud Run image deployment; provider secrets/IAM | Build, registry, scanning, logs and network have independent meters. Use short-lived OIDC for deployment when configured; never expose secret keys through client bundles or untrusted PR jobs |
| Email | [Resend](../providers/resend.md) only for actual verification/recovery; [Brevo](../providers/brevo.md) runner-up | Resend quota counts incoming mail and each recipient. Daily exhaustion can block onboarding before monthly quota. Verify own domain, abuse limits and delivery; no paid email activated here |
| Logs/metrics | Native platform logs, request IDs, errors and latency metrics first | Bound retention and volume; scrub tokens, emails and answer content. Google logging is separately metered, not unlimited free hosting |
| Optional external observability | [Grafana Cloud](../providers/grafana.md) Free | Explicit startup fit and separate log/trace allowances; adds export/egress and vendor operations. Use only when native tools fail a concrete need |
| Sentry / Better Stack | [Sentry](../providers/sentry.md), [Better Stack](../providers/better-stack.md) compared | Sentry current Free error quota not reproduced; existing unresolved status retained. Better Stack Free says personal projects; commercial entitlement UNKNOWN, so no default recommendation |
| Cache, queues, cron | No Redis initially; DB uniqueness/job status and platform scheduler when required | [Upstash](../providers/upstash.md) has real free offerings, but another quota/secret/failure domain is not justified. Cloud Tasks/Cloud Scheduler are optional GCP capabilities, not mandatory dependencies |

Only one identity system and one PostgreSQL database are selected. Better Auth runs in the Next.js deployment, not a separate auth service. Go verifies an issued JWT using the auth JWKS, with issuer/audience/algorithm/expiry validation, and independently enforces learner ownership and roles. Session revocation versus JWT lifetime must be tested. JWT decoding alone is not authentication; vendor admin/service-role credentials never belong in the browser.

### Account, billing and region checklist for proposed providers

These are documented plan behaviors, not observations of the owner's accounts. UNKNOWN fields are implementation blockers where material. Payment method does not necessarily mean a credit card; accepted billing arrangements differ by provider/account.

| Provider / scope | Card or billing requirement | Automatic charge / exhaustion / inactivity | Shared scope and upgrade behavior | Data/compute placement |
|---|---|---|---|---|
| Netlify Free, A/B | No card for Free; no paid account required | Free has no auto recharge; quota exhaustion pauses projects; Free can also be withdrawn under terms | Team credit pool; paid upgrade introduces subscription and optional recharge, with account-specific quote | Global CDN; functions regional. Exact default Free function region/latency remains UNKNOWN; do not assume Singapore |
| Google Cloud Run, A/B/C | Active Cloud Billing account and valid payment arrangement; trial alone is not sustainable authorization to consume paid services | Paid account automatically bills uncovered usage; scale to zero creates cold starts. Spend cap can pause new work; no universal exact invoice cap | Billing-account aggregate; separate build/registry/logs/scheduler usage. Changing billing mode/minimum instances changes eligible costs | Singapore app proposed; registry same region; secret/log retention placement must be checked |
| Neon Free, A/B/C | No card; paid Launch requires payment arrangement | Free suspends compute on usage exhaustion, not auto-overage. Idle compute suspends automatically; published Free exhaustion is not a data-deletion policy | CU/transfer per project, storage also account-wide; paid upgrade removes the Free allowance, so paid usage starts from the applicable paid meter | Singapore database proposed; management/telemetry/subprocessor geography is not identical to DB storage geography |
| Better Auth library | No provider billing account; app and PostgreSQL must already exist | No license meter; host, DB, recovery mail and maintenance consume resources | Same app/DB quotas; optional hosted Better Auth Infrastructure is a different offering and is not selected | In the Next app and selected PostgreSQL region |
| Cloudflare R2 + DNS | R2 subscription requires valid payment method; DNS Free is distinct | R2 storage/operations auto-bill beyond allowance; no verified dollar hard cap. Payment preauthorization failure can suspend access and unresolved payment may lead to deletion | R2 account allowance counted once; Workers Paid is not required merely to use S3 R2. Storage class/features change meters; existing free egress is not a freeze on all future terms | APAC hint, not guaranteed Singapore/Vietnam residency; DNS/CDN edge placement is separate |
| GitHub Actions CI | Public standard-runner CI no paid plan; private usage has included compute. Exact owner's budget/payment configuration UNKNOWN | Beyond included usage may bill if permitted; configure stop-usage budget/no paid overage. Job/runtime/storage limits remain; public inactive schedules can disable | Owner-level private compute pool, including eligible sandbox compute; paid plan/runner changes allowance and rates. No extra pool per Python script | Hosted-runner placement not guaranteed here; use repository content, not learner production data |
| Resend Free, only when email required | Free plan exists; requirement for card on the intended signup/account path was not explicitly reproduced: UNKNOWN | Daily/monthly limits apply; Free does not use paid overage. No separate production approval; sender DNS still required | Account quota combines sent/received messages and recipient fan-out; paid plan adds overage up to its documented default ceiling | Exact selected sending region, email-body retention and DPA acceptance UNKNOWN; delivery to Vietnam must be tested |
| Supabase Free, alternative only | Free signup; exact account payment requirement not inspected | Free project can pause after inactivity; quota enforcement is not a substitute for availability. Default SMTP is not production email | Organization quotas counted once; paid organization upgrades all its projects, with per-project compute and separate add-ons | Singapore DB option; Auth/Storage are tied to project; control-plane/subprocessor review still required |

No-account/no-card as an absolute requirement disqualifies the current default because of GCP/R2 billing, irrespective of whether the first invoice is zero. A requirement for guaranteed Vietnam-only storage also disqualifies the proposed placement without a different verified arrangement.

## 5. Five hard gates

PASS below means a documented capability/eligibility passes the stated **reference screen**, not production approval. Security/privacy is UNKNOWN until actual data, credentials, DPA/residency and integration controls are reviewed. Export documentation is not a successful restore drill. A single FAIL disqualifies the candidate for that scenario; UNKNOWN blocks production.

| Candidate / scenario | Functional / region | Security / privacy | Legal / commercial | Cost safety | Portability / recovery | Result |
|---|---|---|---|---|---|---|
| Netlify small full Next app | PASS subject to adapter limits; Vietnam latency UNKNOWN | UNKNOWN | PASS for ordinary commercial app under Free terms | PASS only for Free no-charge limit; availability stops at cap | UNKNOWN until artifact/rollback test | Conditional free frontend |
| Vercel Hobby monetizable app | PASS documented framework fit | UNKNOWN | FAIL: noncommercial only | PASS for capped Free use | UNKNOWN | Disqualified |
| Cloudflare Workers unchanged Next server | UNKNOWN: beta/adapter and API limits | UNKNOWN | PASS for ordinary compliant business app; no card-data collection on Free | PASS for Workers Free invocation limits; R2/Images separate | UNKNOWN | Alternative only after compatibility tests |
| Cloudflare Workers ordinary Go/Linux Python process | FAIL | UNKNOWN | PASS for compliant use | UNKNOWN for replacement architecture | UNKNOWN | Disqualified for unchanged process |
| Cloud Run A/B/C | PASS runtime and Singapore; latency/capacity unmeasured | UNKNOWN | PASS: GCP terms allow independent Customer Applications | UNKNOWN: actual meters/controls and delayed cap need validation | UNKNOWN until revision/export restore | Default candidate, conditional |
| Render/Koyeb/Northflank Free production compute | FAIL production service suitability explicitly excluded by docs | UNKNOWN | UNKNOWN: not a claim that commercial use itself is illegal | UNKNOWN | UNKNOWN | Disqualified for production Free |
| Oracle Always Free | UNKNOWN: home-region capacity/reclamation | UNKNOWN | UNKNOWN: exact account terms not fully reviewed | UNKNOWN: attached resources/account eligibility | UNKNOWN: restore and operator readiness | Not a managed-default replacement |
| Fly current new-account hosting | PASS runtime | UNKNOWN | UNKNOWN for exact account | FAIL sustainable $0: finite trial | UNKNOWN | Paid alternative only |
| Railway recurring free credit | PASS runtime; region/consumption test pending | UNKNOWN | UNKNOWN for exact project terms | UNKNOWN: credit too small to infer workload fit | UNKNOWN | Not selected |
| Neon PostgreSQL + Better Auth | PASS SQL/region/library fit | UNKNOWN | PASS reference commercial screen: Neon business-use terms + MIT library | PASS on Free stop behavior; UNKNOWN on paid TCO | UNKNOWN until full auth/data restore | Default data/identity candidate |
| Supabase consolidated data/auth | PASS documented SQL/region | UNKNOWN | PASS reference business-use screen; project-specific contract review remains | PASS no-charge Free scope; UNKNOWN paid total | UNKNOWN until export incl. auth/files | Runner-up |
| D1/Turso where PostgreSQL required | FAIL | UNKNOWN | UNKNOWN: no legal ranking needed after fit failure | UNKNOWN | UNKNOWN | Disqualified for this schema requirement |
| R2 media | PASS static audio/images; exact residency UNKNOWN if required | UNKNOWN | PASS for licensed media/business use under applicable terms | UNKNOWN: PAYG, no verified invoice cap | UNKNOWN until independent copy/restore | Default media, conditional |
| Actions repository content build/test/publish | PASS bounded CI purpose, schedule not SLA | UNKNOWN until workflow isolation | PASS only within software lifecycle terms | PASS if standard public or private allowance/budget covers usage | UNKNOWN until reproducible publication | Default batch CI |
| Actions live customer worker/API | FAIL product fit | UNKNOWN | FAIL policy scope | UNKNOWN | UNKNOWN | Disqualified |
| Modal exceptional compute | PASS Python/ML features; exact region unknown | UNKNOWN | UNKNOWN for customer-facing endpoint; internal no-fee batch scope documented | UNKNOWN until card/credits/workspace limits tested | UNKNOWN | Conditional runner-up |
| Cloudflare DNS for own product | PASS documented DNS capability | UNKNOWN account/DNS controls | PASS compliant business-use screen | PASS Free DNS scope; domain purchase separate | UNKNOWN until DNS export/recovery drill | Supporting service only |
| Resend verification/recovery mail | PASS transactional production capability; delivery unmeasured | UNKNOWN retention/credentials | PASS reference commercial transactional use; sender/content obligations remain | UNKNOWN signup/account settings; Free quota is bounded | UNKNOWN replacement sender and delivery drill | Conditional supporting service |
| Native platform observability/secrets | PASS documented platform facilities | UNKNOWN configuration/access/log data | PASS within selected platform terms | UNKNOWN actual log/secret/retention meters | UNKNOWN incident/credential recovery | Required configuration, no new platform vendor |

Neon commercial eligibility is an inference from its current product schedule incorporating business-use MCSA and published Free plan, not an individual legal approval or SLA. Supabase has business-use/end-user and tier restrictions to review; absence of a Vercel-like prohibition does not remove those obligations. Cloudflare Free prohibits collecting payment-card information on a Free-served property: if monetizing later, evaluate hosted checkout and exact payment flow/terms rather than handling card details in the app. Rights to audio/images and learner-data processing remain application blockers.

## 6. Eight-dimension comparison

Canonical weights are unchanged. Ratings and overall numeric scores are **UNKNOWN**, not zero: no equal-workload measurements, complete security review or recoverability proof exists. A fabricated weighted total would violate the catalog matrix. The following is a weighted evidence comparison with explicit selection criteria, not a benchmark ranking.

| Dimension / weight | Netlify + Cloud Run + Neon + R2 | Cloud Run for both Next/Go + Neon + R2 | Supabase data/auth variant | Evidence still needed |
|---|---|---|---|---|
| D1 Discovery / 5% | Commercial Free frontend supported | Ordinary container path supported | Consolidated managed product documented | Actual account/region entitlement |
| D2 Integration / 10% | Next adapter plus Go/container, SQL, S3 | No Next adapter; same compute control plane | JWT/RLS and pooler integration, less auth code | App-version feature contract tests |
| D3 Security / 20% | Multiple secrets/hosts and app-owned auth | Fewer hosting boundaries; app-owned auth remains | Managed auth reduces implementation scope, service-role misuse remains possible | Threat model, token/session tests, DPA/residency |
| D4 Reliability / 15% | Netlify quota suspension plus app/DB cold starts | App and DB cold starts, no free availability proof | Whole Free project can pause | Failure tests, RTO/RPO, provider outage handling |
| D5 Performance / 10% | Edge assets; function-to-Go hops can be remote | Singapore app/DB candidate; fewer internal provider hops | Singapore placement; SQL/auth API latency | Vietnam p95/p99 and peak workload |
| D6 Cost / 20% | Shared frontend credit pool; native media offloaded | No Next hosting subscription; GCP app egress bill | Shared quotas; paid organization floor less incremental | Monthly meter inventory, actual region prices and taxes |
| D7 Operations / 10% | Separate frontend and API deployment/log systems | Shared revisions/logs/IAM; self-host cache ownership | Auth/admin tooling included | Debugging and rollback drill |
| D8 Exit / 10% | Standard Next build, SQL and S3; adapter removal | Portable OCI images + PostgreSQL/S3 | Postgres portable; auth/storage metadata migration extra work | Successful isolated restore and identity migration |

Default wins on integration simplicity, runtime correctness and exit strategy, accepting some networking cost. Supabase wins when the team cannot safely operate app-owned authentication; that evidence would change the default. No weight adjustment was needed to express these trade-offs.

## 7. Three complete stacks

### Stack A — best attempt at a commercially eligible $0 MVP

**Netlify Free + Cloud Run Go + Neon Free + Better Auth + R2 + GitHub Actions; Resend when email accounts are enabled.** The goal is $0 under the allowances; a verified all-in zero invoice is **NOT ESTABLISHED** because GCP internet transfer, registry/build/logs, a domain and actual consumption remain material. Reject a promise of $0 rather than silently moving Vietnam users to a distant region or omitting backups.

| Component | Provider / free tier reference | Why selected | Main limitation | Fallback |
|---|---|---|---|---|
| Next.js SSR | [Netlify Free](../providers/netlify.md) | Commercial and capped, mature adapter route | Shared credits, adapter differences, regional function latency | Node container on Cloud Run |
| Go HTTP API | [Cloud Run recurring allowance](../providers/google.md) | Real Go process, managed HTTPS, scales to zero | Billing account, cold start, egress | Paid managed container host |
| PostgreSQL | [Neon Free](../providers/neon.md) | Standard SQL, pooler, Singapore, small paid path | Suspension and short restore window | Neon Launch; Supabase only if managed auth also needed |
| Identity | [Better Auth library](../providers/better-auth.md), in Next app | No second identity subscription/service | App owns secure operation and account recovery | Supabase Auth **instead of**, not alongside, Better Auth |
| Audio/images | [R2 Standard allowance](../providers/cloudflare.md) | Avoid app/DB media transfer meters | PAYG operations/storage, own production domain | Small Supabase library or B2 |
| Build/deploy and basic observability | [GitHub](../providers/github.md), native host logs/metrics | Existing delivery tooling, no separate monitoring vendor | Owner-shared allowance; telemetry volume and retention | Optional Grafana after demonstrated need |
| Recovery email | [Resend Free](../providers/resend.md) if required | Direct API/SMTP, no production approval wait | Daily/monthly limits and sender DNS | Brevo after own deliverability test |

Billing owners: one Netlify team, one GCP billing account, one Neon organization/project, one Cloudflare account, one GitHub owner and optionally one email account. There are five core providers, six with email; Better Auth is a library, not another provider subscription. Complexity: moderate. Production blockers: actual rate/latency/security/restore/billing tests. Domain must already exist for a zero-incremental recurring scenario; otherwise registration is additional.

### Stack B — best attempt at $0 with all three runtimes

Use A and run **Python as a bounded repository content build/test/publication job in GitHub Actions**. Do not introduce a Python API or persistent worker when none is needed. This remains the same provider count and quotas, not another free compute pool.

| Component | Provider / tier | Why selected | Main limitation | Fallback |
|---|---|---|---|---|
| Web, Go, data, identity, storage, email, telemetry | Same as A | No unnecessary component replacement | All A constraints still apply | Same A fallbacks |
| Python editorial content build | GitHub Actions existing allowance | Linux Python environment, deterministic artifacts, publication evidence | CI policy, bounded duration, shared private credit, no timing SLA | Existing authorized environment |
| Actual application async jobs, if B needs them | Cloud Run Jobs existing GCP account | Run-to-completion, Python native dependencies, no always-on worker | Separate job billing semantics, scheduling/retries/egress | Modal only after workload/terms/cost advantage |
| Actual scheduled production job, if needed | Cloud Scheduler in GCP | Uses same provider, authenticated invocation | Account-wide scheduler allowance; compute/logs separately billed | Application-driven explicit invocation if no schedule needed |

For the full version of B with learner-triggered asynchronous processing, Actions is **not** the worker. Jobs plus optional Scheduler are required; zero monthly invoice is not substantiated. Store durable status, idempotency keys and retry policy in the existing DB. A queue service is added only if measured dispatch/backpressure semantics cannot be handled safely with the existing platform and database. CPU-bound AI can consume the entire compute grant quickly; GPU not included in the default cost claim.

### Stack C — low-cost production path and default topology

**Cloud Run Next.js/Node + Cloud Run Go in Singapore; Neon Free initially, Launch only at a DB bottleneck; Better Auth in Next; R2; GitHub CI/editorial Python; Resend if required.** Add a Cloud Run Python Job only for a real application job. This removes Netlify and its frontend credit pool; it does not combine unrelated processes in one container or deploy three always-on servers.

| Component | Provider / tier | Why selected | Main limitation | Fallback |
|---|---|---|---|---|
| Next + Go | Cloud Run, separate portable images/services, recurring allowances + PAYG | Exact runtimes, one hosting control plane, same-region inter-service path | Billed traffic, cold starts and multi-instance Next cache coordination | Netlify for tested low-traffic Next; paid container host if cold starts unacceptable |
| PostgreSQL | Neon Free → Launch only when needed | Incremental compute/storage billing, standard export | Paid plan replaces free entitlements; alerts are not a dollar hard cap | Supabase Pro if managed auth/platform value justifies a larger budget |
| Auth, media, CI, editorial Python, email | Same as A/B | Stable contracts, no additional subscription migration | Team-owned auth and all relevant quota/backup limits remain | Component-specific fallbacks above |
| Production Python processing | Cloud Run Jobs only when needed | Reuses IAM/registry/logs/provider account | Job duration, CPU, retries and scheduling drive cost | Modal for measured specialized compute need |

Four core providers, five with email. Native monitoring/secrets do not add providers. Better Auth does add application maintenance; its license cost is not the same as a managed-auth price. No SLA or production approval follows from paying a small amount.

**First justified payment:** allow necessary GCP transfer/registry usage before buying a subscription. If DB compute/storage/restore is first to bind, upgrade only Neon. If Netlify is first to bind in A, migrate just Next to the C topology rather than upgrade every provider. If only R2 storage grows, pay that usage meter. An always-on requirement or stricter RPO changes the cost model and may exceed the requested bands.

## 8. Monthly cost model and boundaries

USD planning calculations, no signup credits. Infrastructure invoice excludes separately identified domain acquisition, taxes, operator labor, external LLM/TTS API charges and devices; these remain real TCO drivers, not assumed zero. A–C have no supplied measurements, so no fabricated all-in monthly total is published.

`TCO = subscriptions once per owner + aggregate post-allowance usage + compute/registry/build/network/logs + backup/restore + operator time + taxes.`

| Budget band | What can be supported by evidence | Limit |
|---|---|---|
| $0 | Stack A or B editorial-only can target the included allowances; Netlify/Neon free services stop at quota | No complete production $0 invoice demonstrated. Cloud Run/R2 are bill-enabled. A new domain, transfer or registry growth can break zero immediately |
| $0–5 | C with light, measured usage is the preferred operating target; a small Neon paid workload may fit | This is an allocation target, not an estimate or guaranteed cap. GCP internet transfer and other meters must fit the remaining budget |
| $5–20 | C with intermittent paid DB compute and additional media/job usage is plausible under a measured budget | Does not buy verified HA, 24/7 workers, unlimited email or app-owned auth operations. Persistent DB activity can consume almost the full band |

Worked calculations use the rates in the provider SSOT, **not measured product usage**:

- Netlify MVP planning example: 4 production deploys, 3 GB web transfer, 100,000 web requests and 1 GB-hour compute consume **150 credits**. The remaining pool is not separately available per meter. A second example with 4 deploys, 12 GB transfer and the same requests/compute consumes **330 credits**, beyond Free. Media must bypass Netlify; static JS/HTML and previews still have traffic consequences. These are hypothetical monthly inputs, not estimates for 1,000 learners.
- Neon Free: a fixed 0.25-CU database active 10 hours/day for a 30-day month consumes **75 CU-hours**; active 24 hours/day consumes **180 CU-hours**, which cannot fit the Free compute allowance. Cold-start/autosuspend and other branches also count; do not shard a single workload across free projects to bypass limits.
- Neon Launch: with one 1-GB database, 0.25 CU active for 100 hours costs **$3.00** for compute + database storage; 300 active hours costs **$8.30**. At 730 active hours the same subtotal is **$19.695**. Free compute is not subtracted after upgrading. These subtotals omit retained history, snapshots, other branches, network overage, tax and app hosting.
- R2 Standard: a 20-GB-month library, with operations still within included allowance, has a derived storage subtotal of **$0.15/month**. Backups occupy storage too. Read-heavy delivery can still cost operations money; no egress charge does not cap the invoice.
- Cloud Run: compare aggregate CPU time, GiB-seconds and requests across Next, Go and applicable jobs under one billing account. Free grants are spending discounts with documented reference-region rates; don't add a fresh grant for each project/service or sum billing modes into a larger allowance. No all-in Singapore price is inferred from an Iowa table or a user count.

**Hard boundaries:** Netlify Free pauses at its shared credit limit; Neon Free suspends compute at usage limits and restricts storage growth; Resend has daily as well as monthly limits; GitHub private credit is owner-shared with eligible sandbox compute and storage is separate. **Not exact invoice caps:** Cloud Run max instances, CPU limits, alert budgets, delayed spend caps and Neon approximate consumption quotas. R2 storage/operation PAYG remains a material cost-safety UNKNOWN until account controls and attack traffic are tested.

GCP now documents project/service **spend caps for Cloud Run**. It would be outdated to claim that Google has only alert budgets. It is equally wrong to call those caps exact: they use gross estimated spend before discounts, allow in-flight/delayed overage and do not cover unrelated registry, logging, scheduler, network SKUs or fixed storage. Confirm actual meter attribution; a low gross cap can pause a service even when net charges would have been covered by free credits. An alerts-only budget still never stops usage by itself.

## 9. Integrated security, reliability and exit

- Keep public immutable audio/images on R2/CDN, not streamed through Go/Next. Use cache headers, immutable object keys and checksums. Private/premium media needs authorization: Go-issued presigned S3 URLs provide expiring origin access; custom-domain edge authorization requires a separately evaluated design and can add Worker costs. This study assumes ordinary public static lesson assets, not DRM.
- Keep app and PostgreSQL near each other. Use TLS and bounded pools; pooled transaction semantics do not support every session-level feature. Use direct connections for compatible admin/migration/pg_dump tasks. Do not configure the pool for the host's theoretical maximum concurrency; total app instances × pool size must fit the database's actual capacity.
- Use one auth issuer. Store secure HttpOnly/SameSite cookies appropriately, validate CSRF/origin on mutations, rate-limit recovery/signup and avoid tokens in logs. Use separate least-privilege SQL roles and restore/admin credentials. Go owns business authorization; authenticated does not mean authorized.
- Pin and scan build inputs, deploy immutable images/artifacts, keep the prior known-good revision and use expand/contract DB migrations. A frontend rollback does not undo a destructive schema migration. Coordinate auth schema, JWT keys and asset versions across releases.
- Native logs/metrics are sufficient initially: structured request ID, error class, duration, job status and quota alerts. Configure sampling/retention; do not introduce Sentry, Grafana, Redis, Kafka, Kubernetes, a VPS or IaC just to complete a checklist.
- Recovery planning assumption: daily logical database export plus immutable media/source manifests and an independent encrypted copy, with an initial target RPO ≤24 hours and RTO ≤4 hours. **NOT VERIFIED**; no restore performed. Store database exports outside Neon, e.g. R2, and keep a second encrypted copy outside the Cloudflare account/available authorized environment. An R2 copy alone is not protection from a Cloudflare-wide outage. Scheduler/export compute and retained copies count toward cost.
- Back up auth tables, encryption/signing material through an appropriate secure process, object inventory and media binaries; pg_dump does not back up object storage. Do not assume provider restore history replaces independent backups. Test a restore into isolated PostgreSQL, verify ownership and login, compare object checksums, then rehearse app image rollback. If this cannot meet required learner-data recovery, pay for stronger backup/recovery or block release.
- Exit Cloud Run by running the same OCI images elsewhere; exit Neon via standard PostgreSQL dump/restore; exit R2 using its S3-compatible API/rclone-style tooling; exit Better Auth with its own DB and versioned migrations. Auth replacement still needs session/password-hash compatibility, possible password reset and user-ID mapping. Preserve app-owned learner IDs so provider identifiers are not the sole business key.

## 10. Adversarial review

| Question | Answer / falsification condition |
|---|---|
| 1. Temporary credits? | Default excludes GCP signup credit, Fly trial and special GPU grants; Modal credit is recurring but optional |
| 2. Commercial policy? | Vercel Hobby rejected; Netlify Free explicitly permits commercial projects; remaining selected terms scoped above |
| 3. Sleeping or pausing? | Cloud Run cold starts, Neon autosuspend/quota suspension, Netlify cap and Supabase inactivity all remain material |
| 4. Shared allowance? | GCP billing owner, Netlify team, GitHub owner, R2 account and Supabase organization must each be aggregated once |
| 5. Vietnam region? | Singapore app/DB proposed; no measured Vietnam latency. US/EU-only free compute loses regional fit |
| 6. Networking excessive? | C removes Netlify-to-Go hop/provider. GCP-to-AWS DB remains; public media direct to CDN avoids the largest app egress |
| 7. Full Next compatibility? | Ordinary Node server preferred; Netlify adapter needs tests; vinext beta is not blanket equivalence |
| 8. Always-on Go? | Not assumed. Request-based scale-to-zero first; continuous sockets/worker requirement changes cost |
| 9. Live Python required? | No for editorial content; only create Jobs/API for actual app requirements |
| 10. Actions worker replacement? | Only bounded repository builds/tests/publication; not live customer jobs, general cron hosting or an online processing service |
| 11. Separate cache? | No demonstrated need; use existing app/CDN/DB capabilities |
| 12. Correct SQL semantics? | PostgreSQL retained; D1/Turso rejected for this requirement |
| 13. Export possible? | SQL and S3 formats documented; identity/media restore still must be exercised |
| 14. Backup satisfied? | No. Independent copies and target RTO/RPO have not been demonstrated; release blocker |
| 15. Cost can grow? | Yes: Cloud Run/R2/paid Neon and optional model/email. Controls are not a universal invoice ceiling |
| 16. Auth boundary secure? | Design identified, not tested. One issuer + Go authorization; failed revocation/ownership test blocks release |
| 17. Single outage? | GCP or Neon outage disables authenticated learning; R2 outage disables media; no free multi-cloud HA claimed |
| 18. Added vendor worth it? | R2 reduces audio egress; Neon preserves SQL and small paid increments; Netlify only worth it for bounded free SSR; optional tools stay absent |
| 19. Simpler equivalent? | Supabase DB/Auth/Storage is simpler for tiny media and a team needing managed auth. It wins if its paid floor/limits fit better than auth operations |
| 20. What changes choice? | Exact app fails runtime tests, bad Vietnam latency, no card/billing allowed, strict $0 hard cap, strict data residency, recovery/SLA or sustained worker needs |

Revisit before release and when any critical meter approaches an operator-selected threshold (initial planning threshold 70–80%), when free/commercial terms change, or when cold starts/DB wake-ups breach measured UX objectives. This threshold is an operational proposal, not a provider quota. No automatic upgrade or billing activation is authorized by this research.

## 11. Official evidence ledger

All links below were opened/inspected for the specific stated scope on **2026-11-05**. Search snippets alone were not treated as current numeric pricing when live documentation disagreed. Product limits/rights outside the stated scope remain UNKNOWN. Provider profiles own canonical prices/quota amounts; this ledger owns the reasoning provenance.

| Scope | Official sources | Evidence boundary |
|---|---|---|
| Next.js ordinary server | [Self-hosting](https://nextjs.org/docs/app/guides/self-hosting) | Images, runtime environment, caching and multi-server coordination |
| Cloudflare Next paths | [Current Next guide](https://developers.cloudflare.com/workers/framework-guides/web-apps/nextjs/) · [OpenNext guide](https://developers.cloudflare.com/workers/framework-guides/web-apps/opennext/) · [Pages Next guide](https://developers.cloudflare.com/pages/framework-guides/nextjs/) | Current default vinext beta; alternate OpenNext support and middleware restriction |
| Cloudflare runtime | [Limits](https://developers.cloudflare.com/workers/platform/limits/) · [Pricing](https://developers.cloudflare.com/workers/platform/pricing/) · [Languages](https://developers.cloudflare.com/workers/languages/) · [Python execution](https://developers.cloudflare.com/workers/languages/python/how-python-workers-work/) · [Python packages](https://developers.cloudflare.com/workers/languages/python/packages/) | Isolate CPU/memory; Wasm/Pyodide, not a conventional server |
| Vercel commercial screen | [Pricing](https://vercel.com/pricing) · [Fair use](https://vercel.com/docs/limits/fair-use-guidelines) | Hobby noncommercial restriction; paid alternative only |
| Netlify runtime/cost/rights | [Next compatibility](https://docs.netlify.com/build/frameworks/framework-setup-guides/nextjs/overview/) · [Pricing](https://www.netlify.com/pricing/) · [Credit plans](https://docs.netlify.com/manage/accounts-and-billing/billing/billing-for-credit-based-plans/credit-based-pricing-plans/) · [Meters](https://docs.netlify.com/manage/accounts-and-billing/billing/billing-for-credit-based-plans/how-credits-work/) · [Current agreement](https://www.netlify.com/legal/self-serve-subscription-agreement) · [Commercial Free statement](https://www.netlify.com/blog/introducing-netlify-free-plan/) | Current credit plan; historical blog supports eligibility only, not old quota amounts. Paid account quote unresolved |
| Cloud Run capabilities | [Container contract](https://docs.cloud.google.com/run/docs/container-contract) · [Fit](https://docs.cloud.google.com/run/docs/fit-for-run) · [Request timeout](https://docs.cloud.google.com/run/docs/configuring/request-timeout) · [WebSockets](https://docs.cloud.google.com/run/docs/triggering/websockets) · [Jobs](https://docs.cloud.google.com/run/docs/execute/jobs) | Container ABI, PORT, request/job lifecycle; no app capacity benchmark |
| GCP money/terms | [Run pricing](https://cloud.google.com/run/pricing) · [Free program](https://docs.cloud.google.com/free/docs/free-cloud-features) · [Network pricing](https://cloud.google.com/vpc/network-pricing) · [Spend caps](https://docs.cloud.google.com/billing/docs/how-to/budgets-spend-caps) · [Alerts-only budgets](https://docs.cloud.google.com/billing/docs/how-to/budgets) · [Terms](https://cloud.google.com/terms) | Recurring allowance separate from trial; no global invoice hard cap |
| GCP ancillary cost | [Registry](https://cloud.google.com/artifact-registry/pricing) · [Scheduler](https://cloud.google.com/scheduler/pricing) · [Observability](https://cloud.google.com/products/observability/pricing) | Account/project scope; distinct meters, not implicit free add-ons |
| Koyeb | [Instances](https://www.koyeb.com/docs/reference/instances) · [Pricing FAQ](https://www.koyeb.com/docs/faqs/pricing) · [Organizations](https://www.koyeb.com/docs/reference/organizations) | Free production warning, region/sleep and immediate selected-plan charge |
| Render | [Free](https://render.com/docs/free) · [Compute](https://render.com/docs/compute-plans) | Shared hours, sleep, no production Free recommendation, expiring Free DB |
| OCI / Fly / Railway / Northflank | [OCI Always Free](https://docs.oracle.com/en-us/iaas/Content/FreeTier/freetier_topic-Always_Free_Resources.htm) · [Fly trial](https://docs.fly.io/about/free-trial) · [Railway trial and recurring Free](https://docs.railway.com/pricing/free-trial) · [Northflank pricing](https://northflank.com/pricing) · [Sandbox warning](https://www.northflank.ai/docs/v1/application/billing/pricing-on-northflank) | Alternative screening only; no assurance of free region capacity or security incident closure |
| Neon | [Pricing](https://neon.com/pricing) · [Plans](https://neon.com/docs/introduction/plans) · [Regions](https://neon.com/docs/introduction/regions) · [Pooling](https://neon.com/docs/guides/serverless-connection-pooling) · [Alerts](https://neon.com/docs/introduction/spending-notifications) · [Consumption limits](https://neon.com/docs/guides/consumption-limits) · [Product terms](https://neon.com/platform-terms) · [Incorporated MCSA](https://www.databricks.com/legal/mcsa) | Current live storage entitlement used over older repository snapshot; dollar alerts are not active suspension |
| Supabase | [Pricing](https://supabase.com/pricing) · [Billing](https://supabase.com/docs/guides/platform/billing-on-supabase) · [Backups](https://supabase.com/docs/guides/platform/backups) · [Free backup FAQ](https://supabase.com/kb/faqs/platform/free-plan-backups) · [SMTP](https://supabase.com/docs/guides/auth/auth-smtp) · [JWT](https://supabase.com/docs/guides/auth/jwts) · [Terms](https://supabase.com/terms) | Inactivity, shared quota, Free backup and sender restrictions |
| Other DB options | [Aiven Free](https://aiven.io/docs/products/postgresql/concepts/pg-free-tier) · [Aiven pricing](https://aiven.io/pricing/postgresql) · [D1](https://developers.cloudflare.com/d1/platform/pricing/) · [Turso](https://turso.tech/pricing) | Aiven region/pool constraints; SQLite options fail required Postgres fit |
| Identity library/hosted alternative | [Better Auth MIT license](https://github.com/better-auth/better-auth/blob/main/LICENSE.md) · [JWT/JWKS plugin](https://better-auth.com/docs/plugins/jwt) · [Clerk pricing](https://clerk.com/pricing) · [Clerk plan change](https://clerk.com/changelog/2026-02-05-new-plans-more-value) | One auth authority; no full security audit or migration proof |
| R2/media | [Pricing](https://developers.cloudflare.com/r2/pricing/) · [Billing policy](https://developers.cloudflare.com/billing/understand/billing-policy/) · [Threshold billing](https://developers.cloudflare.com/billing/threshold-billing/) · [Public delivery](https://developers.cloudflare.com/r2/buckets/public-buckets/) · [Placement](https://developers.cloudflare.com/r2/reference/data-location/) · [Terms](https://www.cloudflare.com/terms/) · [Developer terms](https://www.cloudflare.com/service-specific-terms-developer-platform/) · [B2 alternative](https://www.backblaze.com/cloud-storage/pricing) | Egress vs operation billing; production domain; region hint and payment risks |
| Python alternatives | [Modal pricing](https://modal.com/pricing) · [Billing](https://modal.com/docs/guide/billing) · [Budgets](https://modal.com/docs/guide/budgets) · [Terms](https://modal.com/legal/terms) · [HF Spaces](https://huggingface.co/docs/hub/spaces-overview) · [HF hardware](https://huggingface.co/docs/hub/main/spaces-gpus) | Recurring credit vs bill-enabled compute; paid-plan requirement to create ordinary HF compute Space |
| GitHub CI | [Current included compute](https://docs.github.com/en/billing/reference/product-usage-included) · [Limits](https://docs.github.com/en/actions/reference/limits) · [Schedules](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows) · [Product terms](https://docs.github.com/en/site-policy/github-terms/github-terms-for-additional-products-and-features) | Current monetary allowance takes precedence over legacy minute table; CI use, not online worker hosting |
| Email/monitoring/cache | [Resend quotas](https://resend.com/docs/knowledge-base/account-quotas-and-limits) · [Resend production access](https://resend.com/docs/knowledge-base/does-resend-require-production-approval) · [Brevo plan](https://help.brevo.com/hc/en-us/articles/208589409-About-Brevo-s-pricing-plans) · [Grafana](https://grafana.com/pricing/) · [Better Stack](https://betterstack.com/pricing) · [Upstash](https://upstash.com/pricing/redis) | Scoped exclusions/comparison; not a requirement to add all these services |

### Unresolved or conflicting sources

1. Netlify paid subscription display is account-dependent and current docs defer price to the page/dashboard; a universal historical base fee is not established. Free quota/meter comparison remains supported.
2. Cloudflare live bundle limits and older adapter documentation differ. Treat exact build admission as UNKNOWN, not a free-plan rejection based on obsolete bundle numbers.
3. Neon live plans/pricing agree with the current catalog entitlement, while an older upstream website snapshot differs. Current organization spending notifications explicitly remain alert-only despite older spending-limit announcements; project consumption quotas are separate.
4. GitHub current included-usage reference expresses monetary compute credit, whereas legacy Actions billing pages still show minute equivalents. Use the current reference and selected runner rate; never promise a universal number of private minutes.
5. Sentry pricing could not be reproduced directly during this review; its unresolved catalog state was not promoted. Northflank incident closure and individual provider-account entitlement remain unverified.

## 12. Release blockers and maintenance

Before production selection: benchmark pinned Next deployment and Go/DB traffic from Vietnam at expected peak; measure real monthly meters and region prices; verify token/session/authorization behavior and sender recovery; test quota exhaustion/cap behavior without production data; verify private-media access if required; complete dependency/license/data-rights/DPA/residency review; successfully restore independent DB/auth/media backups and roll back an immutable deployment. Obtain owner acceptance of measured UX, availability, RTO/RPO and billing risk. Any failed critical gate disqualifies that scenario; any UNKNOWN remains blocking.

This report does not approve a deployment or provider-account mutation. Catalog structural validation and unit tests verify record integrity; **CI SUCCESS does not verify provider pricing, actual capacity, commercial-contract applicability or production suitability**.
