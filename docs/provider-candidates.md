# Third-party provider candidates — Fullstack + AI + Agentic

> **As-of:** 2026-11-01 · **Currency:** USD unless explicitly EUR · **Status:** curated research snapshot, not a price guarantee. Numbers from linked **official** provider pages; monitor before purchasing.
>
> **Scope:** Public SaaS/PaaS/managed services and relevant self-host alternatives. **Provider ≠ service**: one provider can expose distinct service offerings under different primary pillars (e.g., Browserbase browsers vs Search API; Supabase database vs Auth vs Storage). No duplicate provider-wide profile is implied.

## Interpretation

- **PERMANENT** = provider advertises a recurring or perpetual free service, subject to quotas and policies (not a production SLA).
- **RECURRING_CREDIT** = grant replenished every billing period; **ONE_TIME_CREDIT** = trial grant that does not renew.
- **TIME_LIMITED_TRIAL** = expires by time; **PERMANENT_AFTER_TRIAL** = separate small recurring allocation starts after trial.
- **LIMITED_FREE** = free offer with unspecified renewal period/usage constraints that must be checked before budgeting.
- **NO_MONTHLY_BASE** = no base subscription, **NOT** free transactions. **NONE** = no verified perpetual free API/instance.
- Watchlist means **discovered candidate; price/free-tier not validated**. Never interpret watchlist items as free.
- Paid amounts are indicative entry/example prices, not normalized total cost of ownership. Excludes taxes, region, egress, currency conversion, add-ons, and changing plans unless explicitly noted.
- Free-tier **strongest** is use-case-specific: compare resources and duration first, then cold start, retention, SLA, commercial-use rights, data-usage/privacy, quotas, concurrency, abuse controls, and exit cost.
- Source column links to provider's first-party pricing/docs. Refresh if changing budget or choosing production vendors.

## Quick shortlist — compelling free tiers

| Need | Candidate | Why it stands out | Caveat |
|---|---|---|---|
| Edge API/static hosting | Cloudflare Workers + Pages | 100K Worker requests/day; static requests unlimited | 10 ms CPU request Free |
| PostgreSQL multi-project | Neon | 100 projects, 1 GB/project, 100 CU-h/project/month | 20 GB account cap; scale-to-zero |
| General hosted backend | Supabase | DB + auth + object storage + functions free quotas | 500 MB DB/project; free plan pause policy |
| Dedicated free vector DB | Qdrant | 0.5 vCPU, 1 GB RAM, 4 GB disk | inactivity deletion risk |
| Object storage | Cloudflare R2 | 10 GB storage; 1M writes-class A + 10M reads-class B/month; zero egress | operation costs after quota |
| Serverless Redis | Upstash Redis | 256 MB; 500K commands/month | command and bandwidth caps |
| Webhooks | Svix | 50K webhooks/month | no free SLA |
| Durable async functions | Inngest | 50K executions/month | count steps, not just runs |
| Authentication | WorkOS AuthKit | 1M MAU free | enterprise SSO billed separately |
| Public CI | GitHub Actions | free standard hosted runner minutes on public repos | private repo quota & larger runners |
| Full-stack telemetry | Grafana Cloud | 10K metric series, 50 GB logs + 50 GB traces/mo | 14-day retention |
| Product + AI analytics | PostHog | 1M analytics events + 100K AI events/mo | distinct quotas |
| LLM observability | Langfuse | 50K units/month | unit is not trace count |
| Web research | Tavily / Firecrawl | 1K API credits/month each | credits differ by endpoint |
| AI search credits | Exa | $10 recurring monthly API credit | usage model varies |
| Speech | ElevenLabs | 10K monthly credits | commercial license restriction on Free |
| Transactional email | Resend | 3K/month | 100/day |
| Email volume | Brevo | 300/day | daily reset |
| Headless CMS | Sanity | free forever; 20 users | public datasets |
| Map rendering | Mapbox | 50K map loads/month | other APIs billed separately |

## Full candidate catalog

### 01 — Compute & Runtime

**Strong free-tier fit:** Cloudflare Workers/Pages cho edge/static; Oracle OCI Always Free cho VM (rủi ro thiếu capacity); Modal cho GPU/sandbox credits tái tạo mỗi tháng.

| Service (official source) | Free classification | Free allowance | Paid pricing / floor | Risk / caveat |
|---|---|---|---|---|
| [Cloudflare Workers](https://developers.cloudflare.com/workers/platform/pricing/) | PERMANENT | 100.000 requests/ngày; 10 ms CPU/invocation | Paid Workers từ $5/tháng | CPU limit nghiêm ngặt ở Free |
| [Cloudflare Pages (static)](https://developers.cloudflare.com/pages/functions/pricing/) | PERMANENT | Static requests miễn phí không giới hạn | Functions tính theo Workers | Không đồng nghĩa unlimited Functions |
| [Vercel Hosting/Functions](https://vercel.com/pricing) | PERMANENT | Hobby $0; 1M function invocations/tháng; CDN 100 GB/tháng | Pro $20/tháng/seat + usage | Hobby chỉ cho personal/non-commercial |
| [Netlify](https://www.netlify.com/pricing/) | PERMANENT | Free $0; 300 platform credits/tháng | Personal $9/tháng; Pro $20/tháng | Phải quy đổi credit theo tác vụ |
| [Railway](https://railway.com/pricing) | PERMANENT_AFTER_TRIAL | 30 ngày trial $5; sau đó $1 credit/tháng Free | Hobby $5/tháng tối thiểu gồm $5 usage | Free có giới hạn tài nguyên |
| [Render Web Services](https://render.com/docs/free) | PERMANENT | Web service/free Postgres/Key Value cho thử nghiệm | Paid tính theo instance | Nhà cung cấp không khuyến nghị free cho production |
| [Oracle OCI Ampere A1](https://docs.oracle.com/en-us/iaas/Content/FreeTier/freetier_topic-Always_Free_Resources.htm) | PERMANENT | Always Free tương đương 2 OCPU + 12 GB RAM; 1.500 OCPU giờ/tháng | Vượt quota tính theo OCI | Capacity theo region không bảo đảm |
| [Modal Compute/Sandbox](https://modal.com/pricing) | RECURRING_CREDIT | $30 compute credit/tháng, không áp dụng Shared Endpoints | Team $250/tháng + compute | GPU/container usage tính theo giây |
| [E2B Sandbox](https://e2b.dev/) | ONE_TIME_CREDIT | $100 credit dùng một lần; tối đa 20 concurrent sandboxes | Pro $150/tháng + usage | Không gọi $100 là free monthly |
| [Browserbase Browser Runtime](https://www.browserbase.com/pricing) | LIMITED_FREE | Free 1 browser-hour, 3 concurrent browsers | Developer $20/tháng | Kiểm tra reset period trước khi dự toán |
| [DigitalOcean Droplets](https://www.digitalocean.com/pricing/droplets) | NONE | Không thấy free VM vĩnh viễn trong bảng giá | Basic từ $4/tháng (512 MiB) | VPS tự quản trị, chi phí transfer |
| [Hetzner Cloud](https://docs.hetzner.com/general/infrastructure-and-availability/price-adjustment/) | NONE | Không có permanent free trong bảng giá | CX23 €5,49/tháng từ 15/6/2026, chưa IPv4/VAT | Region, IPv4, VAT; tháng giá đã thay đổi |

**Watchlist (price not verified):** `AWS EC2/Lambda`, `Google Cloud Run/GCE`, `Fly.io Machines`, `Azure App Service/Functions`, `Koyeb`, `Northflank`.

### 02 — Databases & Data

**Strong free-tier fit:** Neon cho nhiều PostgreSQL projects; Aiven PostgreSQL cho instance 1 GB RAM/1 GB disk; Qdrant cho vector DB chuyên dụng.

| Service (official source) | Free classification | Free allowance | Paid pricing / floor | Risk / caveat |
|---|---|---|---|---|
| [Neon Postgres](https://neon.com/blog/neon-free-plan-1-gb-per-project) | PERMANENT | 100 projects; 1 GB/project, tối đa 20 GB toàn tài khoản; 100 CU-h/project/tháng | Launch/Scale theo usage | Scale-to-zero và project quotas |
| [Supabase Database](https://supabase.com/docs/guides/platform/billing-on-supabase) | PERMANENT | 2 free projects (xác minh số project riêng); 500 MB database/project, 5 GB egress | Pro theo subscription + usage | Free projects có thể pause |
| [Turso Database](https://turso.tech/pricing) | PERMANENT | $0; gói Free hiển thị 100 databases, 5 GB storage | Developer từ $4,99/tháng nếu trả năm | Đơn vị quota reads/writes cần kiểm tra khi triển khai |
| [Aiven PostgreSQL](https://aiven.io/docs/products/postgresql/concepts/pg-free-tier) | PERMANENT | 1 vCPU, 1 GB RAM, 1 GB disk; miễn phí không giới hạn thời gian | Paid theo cấu hình | Giới hạn 20 kết nối; không SLA |
| [Qdrant Cloud](https://qdrant.tech/pricing/) | PERMANENT | 1 node: 0,5 vCPU, 1 GB RAM, 4 GB disk | Standard theo tài nguyên | Có chính sách suspend/xóa cluster không hoạt động |
| [Pinecone Database](https://www.pinecone.io/pricing/) | PERMANENT | Starter $0, kèm quota index/search hạn chế | Builder $20/tháng; Standard tối thiểu $50/tháng | Quota và region theo plan |
| [Cockroach Continuum](https://www.cockroachlabs.com/pricing/) | TIME_LIMITED_TRIAL | Trial 30 ngày với $400 credit; không coi là free forever | Standard $0,092/vCPU-hour (mẫu vùng US East) | Giá Basic legacy không còn áp dụng cho khách mới từ 15/9/2026 |

**Watchlist (price not verified):** `MongoDB Atlas`, `Weaviate Cloud`, `Firebase Firestore`, `PlanetScale`, `Timescale Cloud`, `Amazon DynamoDB`, `Upstash Vector`, `Cloudflare D1`.

### 03 — Storage & Media

**Strong free-tier fit:** Cloudflare R2 nếu cần object storage và egress thấp; Cloudinary cho image/video transformation.

| Service (official source) | Free classification | Free allowance | Paid pricing / floor | Risk / caveat |
|---|---|---|---|---|
| [Cloudflare R2 Standard](https://developers.cloudflare.com/r2/pricing/) | PERMANENT | 10 GB-month + 1M Class A + 10M Class B operations/tháng; egress miễn phí | $0,015/GB-month + operations | Không áp dụng free quota cho Infrequent Access |
| [Backblaze B2](https://help.backblaze.com/hc/en-us/articles/217667478-Understanding-B2-Pricing-Structure) | PERMANENT | 10 GB storage miễn phí; egress miễn phí tới 3× average storage | Vượt ngưỡng theo GB/operations | Đọc policy egress và đối tác CDN |
| [Cloudinary Programmable Media](https://cloudinary.com/pricing) | PERMANENT | 25 monthly credits cho transformation/storage/bandwidth | Plus $99/tháng nếu trả tháng | Credit không tương đương GB cố định |
| [Uploadcare](https://uploadcare.com/pricing/) | PERMANENT | 1 GB storage, 5 GB traffic, 1.000 operations/tháng | Pro từ $79/tháng nếu trả tháng | Free personal use only |
| [Vercel Blob](https://vercel.com/pricing) | PERMANENT | 1 GB storage, 10 GB data transfer/tháng (Hobby allowance) | Storage $0,023/GB; thêm operation fees | Gói Vercel Hosting khác với Blob |
| [Supabase Storage](https://supabase.com/docs/guides/platform/billing-on-supabase) | PERMANENT | 1 GB file storage (Free plan) | 100 GB included trong Pro; sau đó $0,021/GB | RLS/egress và object operations |

**Watchlist (price not verified):** `Amazon S3`, `Google Cloud Storage`, `Azure Blob Storage`, `ImageKit`, `Bunny Storage`, `DigitalOcean Spaces`, `Cloudflare Images`, `Mux`.

### 04 — Networking & Edge

**Strong free-tier fit:** Cloudflare Free cho DNS/CDN/WAF; Bunny CDN nếu muốn PAYG đơn giản cho lưu lượng thương mại.

| Service (official source) | Free classification | Free allowance | Paid pricing / floor | Risk / caveat |
|---|---|---|---|---|
| [Cloudflare DNS/CDN/WAF](https://www.cloudflare.com/plans/) | PERMANENT | $0/tháng: DNS, CDN, SSL, DDoS protection và WAF cơ bản | Pro $25/tháng nếu trả tháng ($20/tháng nếu trả năm) | Không đồng nghĩa mọi WAF rule đều miễn phí |
| [Bunny CDN](https://bunny.net/pricing/cdn/) | TIME_LIMITED_TRIAL | Trial 14 ngày; không có perpetual free | Từ $0,01/GB EU/NA; $0,03/GB Asia; min $1/tháng | Theo vùng; tính bandwidth thực |

**Watchlist (price not verified):** `Fastly CDN`, `Akamai CDN`, `AWS CloudFront`, `AWS Route 53`, `Google Cloud CDN`, `Azure Front Door`, `Gcore CDN`, `Cloudflare Zero Trust`.

### 05 — Cache & Traditional Search

**Strong free-tier fit:** Upstash Redis cho cache serverless; Algolia Free cho search hosted; Meilisearch OSS nếu tự vận hành.

| Service (official source) | Free classification | Free allowance | Paid pricing / floor | Risk / caveat |
|---|---|---|---|---|
| [Upstash Redis](https://upstash.com/pricing/redis) | PERMANENT | 256 MB data; 500K commands; 10 GB bandwidth/tháng | PAYG $0,20/100K commands | Không nhầm với Upstash Vector |
| [Redis Cloud](https://redis.io/pricing/) | PERMANENT | 30 MB shared database | Essentials từ khoảng $5/tháng | Kích thước rất nhỏ, best-effort SLA |
| [Algolia Search](https://www.algolia.com/pricing/free-plan) | PERMANENT | 10K search requests, 50K records/tháng | Grow vượt mức $0,50/1K searches | Free plan giới hạn tính năng/records |
| [Meilisearch Cloud](https://www.meilisearch.com/pricing) | TIME_LIMITED_TRIAL | Trial 14 ngày | Cloud từ $20/tháng | OSS self-host miễn phí phần license, phải trả hạ tầng |
| [Typesense Cloud](https://cloud-help.typesense.org/article/how-does-the-free-tier-work) | ONE_TIME_CREDIT | 720 cluster-hours và 10 GB bandwidth dùng MỘT LẦN | Paid theo cluster | Không tái tạo quota hằng tháng |

**Watchlist (price not verified):** `Elastic Cloud`, `Amazon OpenSearch Service`, `Typesense OSS`, `Meilisearch OSS`, `Aiven Valkey`, `KeyDB`.

### 06 — Messaging & Async

**Strong free-tier fit:** Svix free cho webhook delivery; QStash free cho HTTP queue; Inngest free cho durable workflows.

| Service (official source) | Free classification | Free allowance | Paid pricing / floor | Risk / caveat |
|---|---|---|---|---|
| [Svix Webhooks](https://www.svix.com/pricing/) | PERMANENT | 50K messages/tháng; 7 ngày payload retention | Basic từ $20/tháng | Free không kèm uptime SLA |
| [Upstash QStash](https://upstash.com/pricing/qstash) | PERMANENT | 1.000 messages/ngày | PAYG $1/100K messages | Retry attempts cũng tính message |
| [Inngest Cloud](https://www.inngest.com/pricing) | PERMANENT | 50K executions/tháng; 5 concurrent steps; 500K events | Pro từ $99/tháng | Executions khác event count |
| [Trigger.dev](https://trigger.dev/pricing) | RECURRING_CREDIT | Free $5 usage credit/tháng; tối đa 20 concurrent runs | Hobby $10/tháng | Tính theo runtime usage |

**Watchlist (price not verified):** `AWS SQS`, `AWS EventBridge`, `Confluent Cloud`, `CloudAMQP`, `RabbitMQ OSS`, `Apache Kafka OSS`, `Google Cloud Pub/Sub`, `Azure Service Bus`, `Pusher Channels`.

### 07 — Identity & Security

**Strong free-tier fit:** WorkOS AuthKit cho user auth quy mô lớn nhưng SSO enterprise tính riêng; Clerk cho DX nhanh; Doppler cho secrets đơn giản.

| Service (official source) | Free classification | Free allowance | Paid pricing / floor | Risk / caveat |
|---|---|---|---|---|
| [WorkOS AuthKit](https://workos.com/pricing) | PERMANENT | 1M monthly active users miễn phí | Sau mốc đó $2.500/1M MAU/tháng | Enterprise SSO/Directory Sync trả riêng theo connection |
| [Clerk](https://clerk.com/pricing) | PERMANENT | 50K Monthly Retained Users/app; unlimited apps | Pro từ $20/tháng nếu trả năm + usage | MRU khác MAU |
| [Stytch](https://stytch.com/pricing) | PERMANENT | 10K MAU + AI agents; 5 SSO/SCIM connections | PAYG vượt quota | Cần kiểm tra giới hạn theo tính năng |
| [Auth0](https://auth0.com/pricing) | PERMANENT | 25K MAU; 5 organizations; 1 enterprise connection | Essentials từ $35/tháng cho cấu hình 500 MAU | B2C/B2B và feature gating khác nhau |
| [Supabase Auth](https://supabase.com/docs/guides/platform/billing-on-supabase) | PERMANENT | 50K MAU cùng Supabase Free | Pro 100K MAU included, vượt mức $0,00325/MAU | Auth gắn với Supabase project limits |
| [Doppler Secrets](https://www.doppler.com/pricing) | PERMANENT | Developer Free tối đa 3 users | Thêm user $8/tháng; Team $21/user/tháng | Access/RBAC theo plan |

**Watchlist (price not verified):** `Firebase Authentication`, `Infisical Cloud`, `HashiCorp Vault`, `AWS Secrets Manager`, `Azure Key Vault`, `Descope`, `Kinde`, `Permit.io`.

### 08 — DevOps & Delivery

**Strong free-tier fit:** GitHub Actions đặc biệt mạnh cho public repo; CircleCI có 30K credits/tháng; Docker Hub Personal đủ cho thử nghiệm nhỏ.

| Service (official source) | Free classification | Free allowance | Paid pricing / floor | Risk / caveat |
|---|---|---|---|---|
| [GitHub Actions](https://github.com/pricing) | PERMANENT | 2.000 CI minutes/tháng private trên Free; standard hosted runners public repos miễn phí | Extra minutes tùy runner/platform | Larger runners và storage có phí |
| [CircleCI](https://circleci.com/pricing/) | PERMANENT | 30K credits/tháng; tương đương tối đa 6K phút trên small Docker | Performance từ $15/tháng | Build minutes phụ thuộc resource class |
| [Docker Hub Personal](https://docs.docker.com/docker-hub/usage/pulls/) | PERMANENT | Repo public unlimited, 1 private; 200 authenticated pulls/6h | Pro/Team trả thuê bao | Pull limits và fair-use policy |
| [Expo EAS Build](https://expo.dev/pricing) | PERMANENT | 15 Android + 15 iOS builds, 60 phút workflows/tháng | Starter $19/tháng | EAS Build khác Expo Push |
| [Vercel CI](https://vercel.com/pricing) | PERMANENT | 200 CPU minutes/tháng trên Hobby | Paid usage sau allowance | Chỉ áp dụng đúng Vercel CI service |

**Watchlist (price not verified):** `GitLab CI`, `Bitbucket Pipelines`, `Terraform Cloud/HCP Terraform`, `Buildkite`, `Harness CI`, `Google Cloud Build`, `AWS CodeBuild`, `GitHub Container Registry`, `Argo CD (self-host)`.

### 09 — Observability & Analytics

**Strong free-tier fit:** Grafana Cloud cho logs/metrics/traces; PostHog cho product + AI analytics; Langfuse cho LLM traces/eval.

| Service (official source) | Free classification | Free allowance | Paid pricing / floor | Risk / caveat |
|---|---|---|---|---|
| [Grafana Cloud](https://grafana.com/pricing/) | PERMANENT | 10K metrics series; 50 GB logs; 50 GB traces mỗi tháng; 14 ngày retention | Pro từ $19/tháng + usage | Giới hạn users và retention |
| [PostHog Product/AI Observability](https://posthog.com/pricing) | PERMANENT | 1M analytics events; 100K AI observability events; 10 GB logs/tháng | PAYG vượt quota | Phân biệt đơn vị analytics và AI |
| [Langfuse Cloud](https://langfuse.com/pricing) | PERMANENT | 50K units/tháng; 30 ngày data access; 2 users | Core $29/tháng | Units khác số traces |
| [LangSmith](https://www.langchain.com/pricing) | PERMANENT | Developer 1 seat; 5K base traces/tháng | Plus $39/seat/tháng + usage | Vượt traces tính PAYG |
| [Helicone](https://www.helicone.ai/pricing) | PERMANENT | Hobby 10K requests và 1 GB storage | Pro $79/tháng + usage | Lưu ý charge storage ngoài base |
| [Honeycomb](https://www.honeycomb.io/pricing) | PERMANENT | 20M events/tháng, 100M metrics datapoints | Pro từ $150/tháng | Event billing không tương đương span 1:1 |
| [Better Stack](https://betterstack.com/pricing) | PERMANENT | 10 monitors; 3 GB logs và 3 GB traces; 3-day retention | Responder từ $34/tháng nếu trả tháng | Alert/on-call nâng cao có thể trả thêm |

**Watchlist (price not verified):** `Sentry`, `Datadog`, `New Relic`, `Axiom`, `Braintrust`, `Arize Phoenix`, `Logfire`, `OpenObserve Cloud`.

### 10 — AI Models & Agent Tools

**Strong free-tier fit:** Gemini API cho prototyping free (lưu ý data usage); DeepSeek Flash cho token cost thấp; Tavily/Firecrawl/Exa cho web intelligence; OpenRouter cho model miễn phí giới hạn.

| Service (official source) | Free classification | Free allowance | Paid pricing / floor | Risk / caveat |
|---|---|---|---|---|
| [OpenAI API — GPT-6 Luna](https://openai.com/api/) | NONE | Không giả định API free tier | Input $0,10 / 1M tokens; output $0,50 / 1M tokens | Giá theo model; tools/audio tính riêng |
| [DeepSeek API — V4.1 Flash](https://api-docs.deepseek.com/quick_start/pricing/) | NONE | Không có recurring free tier được công bố | Off-peak input miss $0,15; output $0,60 / 1M tokens; peak gấp đôi | Cached input có giá khác; theo khung UTC |
| [Google Gemini Developer API](https://ai.google.dev/gemini-api/docs/pricing) | PERMANENT | Free input/output tokens cho một số models; rate limits theo model | PAYG theo model/token | Free tier data có thể dùng cải thiện sản phẩm; kiểm tra điều khoản |
| [OpenRouter Free Models](https://openrouter.ai/pricing) | PERMANENT | Một số model $0; free variants giới hạn 50 requests/ngày, 20 RPM | PAYG + phí platform tùy gói | Model free có thể thay đổi; không SLA |
| [Tavily Search/Extract](https://www.tavily.com/pricing) | PERMANENT | 1.000 API credits/tháng | PAYG $0,008/credit | 1 basic search thường = 1 credit; advanced = 2 |
| [Firecrawl Scrape/Search](https://www.firecrawl.dev/pricing) | PERMANENT | 1.000 credits/tháng; no credit card | Hobby $19/tháng (monthly) | 1 basic scrape thường = 1 credit; endpoints khác tiêu hao khác |
| [Exa Web Search](https://exa.ai/pricing) | RECURRING_CREDIT | $10 API credits/tháng + $10 onboarding bonus | PAYG theo search/product | Credit đổi ra số query tùy endpoint |
| [Browserbase Search/Fetch API](https://www.browserbase.com/pricing) | LIMITED_FREE | Free 1.000 Search calls + 1.000 Fetch calls theo Free plan | Developer $20/tháng; vượt Search $7/1K | Đây là Search/Fetch, tách khỏi Browser Runtime ở pillar 01 |
| [ElevenLabs Voice API](https://elevenlabs.io/pricing) | PERMANENT | 10K shared credits/tháng | Starter $6/tháng; Creator $22/tháng | Free không có commercial license tương ứng |
| [Cerebras Inference](https://inference-docs.cerebras.ai/support/pricing) | PERMANENT | Có API Free tier với rate limit thấp | Paid token pricing theo model; cần kiểm tra live quote | Tài liệu giá được index cũ; không chốt rate cụ thể |

**Watchlist (price not verified):** `Anthropic Claude API`, `GroqCloud`, `Together AI`, `Fireworks AI`, `Mistral API`, `Cohere`, `Perplexity Sonar`, `Replicate`, `fal.ai`, `Hugging Face Inference`, `Composio`, `ScrapingBee`, `Apify`, `SerpAPI`.

### 11 — Communications

**Strong free-tier fit:** Brevo nếu ưu tiên số lượng email hằng ngày; Resend cho transactional email; OneSignal/Expo Push cho push.

| Service (official source) | Free classification | Free allowance | Paid pricing / floor | Risk / caveat |
|---|---|---|---|---|
| [Resend Transactional Email](https://resend.com/pricing) | PERMANENT | 3.000 email/tháng, tối đa 100/ngày | Pro $20/tháng gồm 50K emails | Free có daily cap |
| [Brevo Email](https://help.brevo.com/hc/en-us/articles/208589409-About-Brevo-s-pricing-plans) | PERMANENT | 300 email/ngày, không giới hạn thời gian | Paid theo volume/contacts | Không cộng dồn quota hàng ngày |
| [Amazon SES](https://aws.amazon.com/ses/pricing/) | NONE_OR_CONDITIONAL | Ưu đãi account tùy điều kiện, không giả định free forever | Essentials $0,16/1.000 emails giai đoạn 0–10M/tháng | Giá theo region và account |
| [OneSignal Messaging](https://onesignal.com/pricing/) | PERMANENT | Mobile push free đến 1.000 MAU; email 10.000 sends/tháng | Growth từ $19/tháng + channel fees | Web push có giới hạn subscribers/send |
| [Knock Notifications](https://knock.app/pricing) | PERMANENT | 10K messages/tháng | Starter từ $250/tháng | Tính message theo workflow/broadcast |
| [Expo Push Service](https://docs.expo.dev/push-notifications/overview/) | PERMANENT | Push service không thu phí theo message (không đồng nhất EAS Build) | Chi phí hạ tầng app riêng | Không bảo đảm deliver, phải xử lý receipts |

**Watchlist (price not verified):** `Twilio SMS`, `Postmark`, `Mailgun`, `SendGrid`, `Firebase Cloud Messaging`, `Pusher Beams`, `Novu Cloud`, `Stream Chat`, `AWS SNS`.

### 12 — Business & Extension APIs

**Strong free-tier fit:** Mapbox cho web map loads, Sanity/Contentful cho headless CMS, Stripe/Paddle/Lemon Squeezy cho thanh toán tùy thị trường.

| Service (official source) | Free classification | Free allowance | Paid pricing / floor | Risk / caveat |
|---|---|---|---|---|
| [Stripe Payments](https://stripe.com/pricing) | NO_MONTHLY_BASE | Không thu setup/monthly platform phí cơ bản; giao dịch có phí | 2,9% + $0,30 / domestic US card transaction | Quốc gia và payment method làm giá thay đổi; không coi xử lý giao dịch là free |
| [Paddle Merchant of Record](https://www.paddle.com/pricing) | NO_MONTHLY_BASE | $0 monthly base; giao dịch có phí | 5% + $0,50 / checkout transaction | Merchant of Record; điều khoản riêng |
| [Lemon Squeezy MoR](https://www.lemonsqueezy.com/pricing) | NO_MONTHLY_BASE | $0 monthly base; giao dịch có phí | 5% + $0,50 / transaction, phụ phí khả dụng | Xác minh điều kiện khu vực và loại giao dịch |
| [Mapbox GL JS](https://www.mapbox.com/pricing) | PERMANENT | 50.000 map loads/tháng | $5/1.000 loads từ 50K–100K | Web map loads khác geocoding/maps APIs |
| [Google Maps Platform](https://developers.google.com/maps/billing-and-pricing/overview) | PERMANENT | Theo SKU: Essentials 10K events/tháng, Pro 5K, Enterprise 1K | PAYG theo SKU/region | Không còn mặc định $200 credit monthly cũ |
| [Sanity Content Lake](https://www.sanity.io/pricing) | PERMANENT | Free $0; tối đa 20 users và 2 public datasets | Growth $15/seat/tháng | Private dataset và roles bị giới hạn |
| [Contentful CMS](https://www.contentful.com/pricing/) | PERMANENT | Free 10 users, 100K API calls/tháng, 50 GB CDN bandwidth | Lite $300/tháng | Khác nhau space, editor roles, locales |

**Watchlist (price not verified):** `PayPal Checkout`, `Shopify APIs`, `Polar`, `Directus Cloud`, `Strapi Cloud`, `Storyblok`, `MapTiler`, `Google Places API`, `Persona KYC`, `Cloudflare Turnstile`.

## Rules for evaluating and maintaining prices

1. **Single source of truth:** classify **service offering** under one primary pillar; add cross-cutting capability tags instead of duplicating service evaluations. Vector DBs always primary pillar **02**; cache primary **05**; model/tool calls primary **10**; all monitoring/tracing/evaluation primary **09**; agent code-execution sandboxes primary **01**.
2. **WHAT / HOW / LIFECYCLE:** 12 functional pillars; 8 evaluation dimensions = discovery, API/contracts, security/governance, reliability, performance, cost/quotas, observability/operations, lifecycle/exit; lifecycle = research → evaluate → select → integrate → operate → migrate/retire.
3. **Price fields for future records:** `provider`, `service`, `primaryPillar`, `capabilities`, `plan`, `currency`, `billingUnit`, `includedQuota`, `resetPeriod`, `hardLimit`, `overagePrice`, `trialExpiry`, `commercialUse`, `sla`, `region`, `sourceUrl`, `verifiedAt`, `confidence`. No mandatory empty files for unselected providers.
4. **No free-tier illusions:** distinguish always free, recurring credit, one-time credit, expiring trial, self-host OSS (license $0, infrastructure ≠ $0), and no-subscription transaction fees.
5. **Cost compare only with workload:** compute monthly total from request/token volume, storage, reads/writes, egress, regions, seats, retention, background workers, sandbox runtime, failure/retry amplification; report p50/p95/p99 latency as measured, not marketing claims.
6. **Security gate:** free access does not imply production suitability. Inspect allowed use (commercial vs hobby), data retention/training, geographic restrictions, DPA/SLA, key scopes, network egress, sandbox isolation, and contract renewal.
7. **Freshness gate:** re-check **official live pricing** and relevant TOS before a binding technical decision; keep this dated snapshot for historical comparisons. Watchlist prices remain intentionally blank until verified.

**Coverage:** 77 source-linked priced/free-tier service records + 103 candidates requiring price verification = **180 candidates**, spanning **12/12 pillars**. As-of 2026-11-01.
