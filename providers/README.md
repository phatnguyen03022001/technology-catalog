# Provider Profiles — Single Source of Truth

**174 provider profiles**, **226 service offering records**. Prices/free-tier amounts live **only in the provider files**. Evidence status is tracked on each service row; see the derived status summary below. Structural validation does not establish factual price accuracy.

## Evidence status by service

Derived from the provider rows by `python3 scripts/validate_catalog.py` (checked date for `VERIFIED`: 2026-11-01). `SOURCE_LINKED_SNAPSHOT` means the current value was not reproduced. Status totals must be refreshed from the validator after catalog changes.

| Evidence status | Service records |
|---|---:|
| `VERIFIED` | 37 |
| `SOURCE_LINKED_SNAPSHOT` | 188 |
| `UNVERIFIED` | 1 |
| `STALE` | 0 |
| `DISCONTINUED` | 0 |

Free-kind classifications (same derived service rows): `PERMANENT` 153; `TIME_LIMITED_TRIAL` 18; `UNKNOWN` 18; `ONE_TIME_CREDIT` 11; `NO_MONTHLY_BASE` 8; `LIMITED_FREE` 6; `RECURRING_CREDIT` 5; `SELF_HOSTED` 5; `PERMANENT_AFTER_TRIAL` 2. There are no `VARIABLE` or `NONE_OR_CONDITIONAL` values.

| Provider | Offerings | Primary pillars |
|---|---:|---|
| [Ably](./ably.md) | 1 | 11 |
| [Aiven](./aiven.md) | 2 | 02, 05 |
| [Akamai](./akamai.md) | 1 | 04 |
| [Algolia](./algolia.md) | 1 | 05 |
| [Amazon Web Services](./amazon-web-services.md) | 13 | 01, 02, 03, 04, 05, 06, 07, 08, 11 |
| [Anthropic](./anthropic.md) | 1 | 10 |
| [Apache Kafka](./apache-kafka.md) | 1 | 06 |
| [Apify](./apify.md) | 1 | 10 |
| [Argo CD](./argo-cd.md) | 1 | 08 |
| [Arize Phoenix](./arize-phoenix.md) | 1 | 09 |
| [Auth0](./auth0.md) | 1 | 07 |
| [Autumn](./autumn.md) | 1 | 12 |
| [Axiom](./axiom.md) | 1 | 09 |
| [Backblaze](./backblaze.md) | 1 | 03 |
| [Better Auth](./better-auth.md) | 1 | 07 |
| [Better Stack](./better-stack.md) | 1 | 09 |
| [Bitbucket](./bitbucket.md) | 1 | 08 |
| [Braintrust](./braintrust.md) | 1 | 09 |
| [Brevo](./brevo.md) | 1 | 11 |
| [Browserbase](./browserbase.md) | 2 | 01, 10 |
| [Buildkite](./buildkite.md) | 1 | 08 |
| [BullMQ](./bullmq.md) | 1 | 06 |
| [Bunny.net](./bunny.md) | 2 | 03, 04 |
| [Cerebras](./cerebras.md) | 1 | 10 |
| [Chargebee](./chargebee.md) | 1 | 12 |
| [Chroma](./chroma.md) | 1 | 02 |
| [CircleCI](./circleci.md) | 1 | 08 |
| [Clerk](./clerk.md) | 1 | 07 |
| [ClickHouse](./clickhouse.md) | 1 | 02 |
| [CloudAMQP](./cloudamqp.md) | 1 | 06 |
| [Cloudflare](./cloudflare.md) | 9 | 01, 02, 03, 04, 12 |
| [Cloudinary](./cloudinary.md) | 1 | 03 |
| [CockroachDB](./cockroachdb.md) | 1 | 02 |
| [Cohere](./cohere.md) | 1 | 10 |
| [Composio](./composio.md) | 1 | 10 |
| [Confluent](./confluent.md) | 1 | 06 |
| [Contentful](./contentful.md) | 1 | 12 |
| [Convex](./convex.md) | 1 | 02 |
| [Coolify](./coolify.md) | 1 | 08 |
| [Couchbase](./couchbase.md) | 1 | 02 |
| [Courier](./courier.md) | 1 | 11 |
| [Dagger](./dagger.md) | 1 | 08 |
| [Datadog](./datadog.md) | 1 | 09 |
| [Daytona](./daytona.md) | 1 | 01 |
| [DeepInfra](./deepinfra.md) | 1 | 10 |
| [DeepSeek](./deepseek.md) | 1 | 10 |
| [Deno](./deno.md) | 1 | 01 |
| [Depot](./depot.md) | 1 | 08 |
| [Descope](./descope.md) | 1 | 07 |
| [DigitalOcean](./digitalocean.md) | 2 | 01, 03 |
| [Directus](./directus.md) | 1 | 12 |
| [Docker](./docker.md) | 1 | 08 |
| [Dodo Payments](./dodo-payments.md) | 1 | 12 |
| [Doppler](./doppler.md) | 1 | 07 |
| [Dragonfly](./dragonfly.md) | 1 | 05 |
| [E2B](./e2b.md) | 1 | 01 |
| [Elastic](./elastic.md) | 1 | 05 |
| [ElevenLabs](./elevenlabs.md) | 1 | 10 |
| [Exa](./exa.md) | 1 | 10 |
| [Expo](./expo.md) | 2 | 08, 11 |
| [fal.ai](./fal-ai.md) | 1 | 10 |
| [Fastly](./fastly.md) | 1 | 04 |
| [Firecrawl](./firecrawl.md) | 1 | 10 |
| [Fireworks AI](./fireworks-ai.md) | 1 | 10 |
| [Fly.io](./fly.md) | 1 | 01 |
| [Gcore](./gcore.md) | 1 | 04 |
| [GitHub](./github.md) | 2 | 08 |
| [GitLab](./gitlab.md) | 1 | 08 |
| [Google Cloud & Firebase](./google.md) | 12 | 01, 02, 03, 04, 06, 07, 08, 10, 11, 12 |
| [Grafana](./grafana.md) | 1 | 09 |
| [Groq](./groq.md) | 1 | 10 |
| [Harness](./harness.md) | 1 | 08 |
| [HashiCorp](./hashicorp.md) | 2 | 07, 08 |
| [Hatchet](./hatchet.md) | 1 | 06 |
| [Helicone](./helicone.md) | 1 | 09 |
| [Hetzner](./hetzner.md) | 1 | 01 |
| [Honeycomb](./honeycomb.md) | 1 | 09 |
| [Hookdeck](./hookdeck.md) | 1 | 06 |
| [Hugging Face](./hugging-face.md) | 1 | 10 |
| [ImageKit](./imagekit.md) | 1 | 03 |
| [Infisical](./infisical.md) | 1 | 07 |
| [Inngest](./inngest.md) | 1 | 06 |
| [Jina AI](./jina-ai.md) | 1 | 10 |
| [KeyDB](./keydb.md) | 1 | 05 |
| [Kinde](./kinde.md) | 1 | 07 |
| [Knock](./knock.md) | 1 | 11 |
| [Koyeb](./koyeb.md) | 1 | 01 |
| [Lago](./lago.md) | 1 | 12 |
| [Langfuse](./langfuse.md) | 1 | 09 |
| [LangSmith](./langsmith.md) | 1 | 09 |
| [Lemon Squeezy](./lemon-squeezy.md) | 1 | 12 |
| [Logfire](./logfire.md) | 1 | 09 |
| [Loops](./loops.md) | 1 | 11 |
| [Mailgun](./mailgun.md) | 1 | 11 |
| [Mapbox](./mapbox.md) | 1 | 12 |
| [MapTiler](./maptiler.md) | 1 | 12 |
| [Meilisearch](./meilisearch.md) | 2 | 05 |
| [Microsoft Azure](./azure.md) | 6 | 01, 03, 04, 06, 07 |
| [MinIO](./minio.md) | 1 | 03 |
| [Mistral AI](./mistral.md) | 1 | 10 |
| [Modal](./modal.md) | 1 | 01 |
| [Momento](./momento.md) | 1 | 05 |
| [MongoDB](./mongodb.md) | 1 | 02 |
| [Mux](./mux.md) | 1 | 03 |
| [Neon](./neon.md) | 1 | 02 |
| [Netlify](./netlify.md) | 1 | 01 |
| [New Relic](./new-relic.md) | 1 | 09 |
| [Ngrok](./ngrok.md) | 1 | 04 |
| [Northflank](./northflank.md) | 1 | 01 |
| [Novu](./novu.md) | 1 | 11 |
| [OneSignal](./onesignal.md) | 1 | 11 |
| [OpenAI](./openai.md) | 1 | 10 |
| [OpenLIT](./openlit.md) | 1 | 09 |
| [OpenObserve](./openobserve.md) | 1 | 09 |
| [OpenRouter](./openrouter.md) | 1 | 10 |
| [Oracle Cloud Infrastructure](./oracle.md) | 1 | 01 |
| [Paddle](./paddle.md) | 1 | 12 |
| [PayPal](./paypal.md) | 1 | 12 |
| [Permit.io](./permit-io.md) | 1 | 07 |
| [Perplexity](./perplexity.md) | 1 | 10 |
| [Pinecone](./pinecone.md) | 1 | 02 |
| [PingCAP](./pingcap.md) | 1 | 02 |
| [PlanetScale](./planetscale.md) | 1 | 02 |
| [Plivo](./plivo.md) | 1 | 11 |
| [Polar](./polar.md) | 1 | 12 |
| [PostHog](./posthog.md) | 1 | 09 |
| [Postmark](./postmark.md) | 1 | 11 |
| [Promptfoo](./promptfoo.md) | 1 | 09 |
| [Pulumi](./pulumi.md) | 1 | 08 |
| [Pusher](./pusher.md) | 2 | 06, 11 |
| [Qdrant](./qdrant.md) | 1 | 02 |
| [Quickwit](./quickwit.md) | 1 | 05 |
| [RabbitMQ](./rabbitmq.md) | 1 | 06 |
| [Railway](./railway.md) | 1 | 01 |
| [Redis](./redis.md) | 1 | 05 |
| [Render](./render.md) | 1 | 01 |
| [Replicate](./replicate.md) | 1 | 10 |
| [Resend](./resend.md) | 1 | 11 |
| [RunPod](./runpod.md) | 1 | 01 |
| [Sanity](./sanity.md) | 1 | 12 |
| [ScrapingBee](./scrapingbee.md) | 1 | 10 |
| [SendGrid](./sendgrid.md) | 1 | 11 |
| [Sentry](./sentry.md) | 1 | 09 |
| [SerpAPI](./serpapi.md) | 1 | 10 |
| [Shopify](./shopify.md) | 1 | 12 |
| [SigNoz](./signoz.md) | 1 | 09 |
| [Storj](./storj.md) | 1 | 03 |
| [Storyblok](./storyblok.md) | 1 | 12 |
| [Strapi](./strapi.md) | 1 | 12 |
| [Stream](./stream.md) | 1 | 11 |
| [Stripe](./stripe.md) | 1 | 12 |
| [Stytch](./stytch.md) | 1 | 07 |
| [Sumsub](./sumsub.md) | 1 | 12 |
| [Supabase](./supabase.md) | 3 | 02, 03, 07 |
| [Svix](./svix.md) | 1 | 06 |
| [Tailscale](./tailscale.md) | 1 | 04 |
| [Tavily](./tavily.md) | 1 | 10 |
| [Telnyx](./telnyx.md) | 1 | 11 |
| [Temporal](./temporal.md) | 1 | 06 |
| [Tigris Data](./tigris.md) | 1 | 03 |
| [Timescale](./timescale.md) | 1 | 02 |
| [Together AI](./together-ai.md) | 1 | 10 |
| [Trigger.dev](./trigger-dev.md) | 1 | 06 |
| [Turso](./turso.md) | 1 | 02 |
| [Twilio](./twilio.md) | 1 | 11 |
| [Typesense](./typesense.md) | 2 | 05 |
| [Uploadcare](./uploadcare.md) | 1 | 03 |
| [Upstash](./upstash.md) | 3 | 02, 05, 06 |
| [Vercel](./vercel.md) | 3 | 01, 03, 08 |
| [Voyage AI](./voyage-ai.md) | 1 | 10 |
| [Wasabi](./wasabi.md) | 1 | 03 |
| [Weaviate](./weaviate.md) | 1 | 02 |
| [WorkOS](./workos.md) | 1 | 07 |
| [Zilliz](./zilliz.md) | 1 | 02 |
