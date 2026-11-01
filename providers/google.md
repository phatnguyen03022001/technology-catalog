# Google Cloud & Firebase

> **Provider SSOT.** Nguồn từ snapshot **2026-11-01**, có URL chính thức đã qua kiểm chứng (VERIFIED). Chỉ dùng để nghiên cứu; xác minh lại trước khi mua hoặc triển khai production.

**Offerings:** 12 · **Pillars:** [01](../pillars/01-compute-runtime/README.md), [02](../pillars/02-databases-data/README.md), [03](../pillars/03-storage-media/README.md), [04](../pillars/04-networking-edge/README.md), [06](../pillars/06-messaging-async/README.md), [07](../pillars/07-identity-security/README.md), [08](../pillars/08-devops-delivery/README.md), [10](../pillars/10-ai-models-agent-tools/README.md), [11](../pillars/11-communications/README.md), [12](../pillars/12-business-extension-apis/README.md)

| Service | Primary pillar | Free kind | Free tier/credits | Paid pricing | Caveat | Official source |
|---|---|---|---|---|---|---|
| Google Cloud Run | 01 | `PERMANENT` | 2.000.000 requests/tháng; 180.000 vCPU-giây; 360.000 GiB-giây; 1 GB egress Always Free | $0,40 / 1M requests; $0,00002400 / vCPU-giây; $0,00000250 / GiB-giây | Egress ngoài 1 GB tính theo biểu giá GCP; cold start nếu không cấu hình min-instances | [Cloud Run Pricing](https://cloud.google.com/run/pricing) |
| Google Compute Engine (GCE) | 01 | `PERMANENT` | 1 máy ảo e2-micro (2 vCPU burstable, 1 GB RAM); 30 GB standard persistent disk; 1 GB egress/tháng Always Free | Sau quota: e2-micro ~$6–$8/tháng tùy zone; egress $0,08–$0,12/GB | Chỉ áp dụng tại US regions (us-central1, us-west1, us-east1); IP ngoại vi tĩnh nếu không gán sẽ tính phí | [GCP Always Free](https://cloud.google.com/free/docs/free-cloud-features) |
| Firebase Firestore | 02 | `PERMANENT` | 1 GiB; 50k reads/ngày; 20k writes/ngày; 10 GiB egress | Blaze PAYG (cùng quota free hàng ngày) | Chặn cứng khi chạm giới hạn ngày ở gói Spark | [Firebase Pricing](https://firebase.google.com/pricing) |
| Google Cloud Storage (GCS) | 03 | `PERMANENT` | 5 GB-tháng Standard Always Free; 5k Class A; 50k Class B; 100 GB egress từ NA | Standard $0,020/GB-tháng; Class A $5,00/1M; Class B $0,40/1M; Egress $0,12/GB | Always Free bị giới hạn vùng ở US (`us-east1`, `us-central1`, `us-west1`); egress sau đó đắt | [GCS Pricing](https://cloud.google.com/storage/pricing) |
| Google Cloud CDN | 04 | `NONE_OR_CONDITIONAL` | Không có free tier riêng; dùng chung $300 credit 90 ngày của GCP | Phí bắt buộc Load Balancer (~$18–$20/tháng) + Cache lookup $0,0075/10k req + Cache egress $0,02–$0,08/GiB | Bắt buộc phải gắn kèm Global External HTTP(S) Load Balancer; sàn chi phí tối thiểu cao | [Pricing/docs](https://cloud.google.com/cdn/pricing) |
| Google Cloud Pub/Sub | 06 | `PERMANENT` | 10 GiB throughput/tháng Always Free (~10M-40M messages/tháng) | $40/TiB (~$0,04/GiB); snapshot/storage $0,27/GB-tháng | Đo lường theo byte (min 256 bytes); push tới non-GCP chịu phí internet egress | [Pricing/docs](https://cloud.google.com/pubsub/pricing) |
| Firebase Authentication | 07 | `PERMANENT` | 50.000 MAUs free (Spark); 10 SMS verification/ngày free | Blaze (PAYG): 50k đầu free, sau đó $0,0055/MAU; SAML $0,015/MAU; SMS theo vùng | Phone auth cần bật Blaze; rủi ro SMS toll fraud; multi-tenant cần Identity Platform | [firebase.google.com/pricing](https://firebase.google.com/pricing) |
| Google Cloud Build | 08 | `PERMANENT` | 2,500 build-mins/mo on default `e2-standard-2` (2 vCPU, 8 GB RAM) | $0.006/min on `e2-standard-2` (~$0.36/hr); billed by the second | Applies only to default pool with e2-standard-2; requires GCP billing account | [Cloud Build Pricing](https://cloud.google.com/build/pricing) |
| Google Gemini Dev API | 10 | `PERMANENT` | Gemini 2.0 Flash: 15 RPM, 1.5k RPD, 1M TPM ($0) | PAYG: Flash $0,10 in / $0,40 out; Flash-Lite $0,075 in / 1M tokens | Dữ liệu Free tier dùng để train model Google; prod nhạy cảm cần bật Cloud Billing | [Gemini API Pricing](https://ai.google.dev/gemini-api/docs/pricing) |
| Firebase Cloud Messaging (FCM) | 11 | `PERMANENT` | 100% Free, không giới hạn notifications trên iOS, Android, Web | $0 | Hạ tầng truyền tải cốt lõi của Google; tự quản lý token thiết bị trên backend | [Firebase Pricing](https://firebase.google.com/pricing) |
| Google Maps Platform | 12 | `PERMANENT` | Essentials 10k/tháng, Pro 5k/tháng theo SKU | Dynamic Maps: $7,00 / 1.000 loads | Bỏ credit $200 gộp; chuyển sang cap độc lập từng SKU; cần thẻ tín dụng | [Google Maps Pricing](https://developers.google.com/maps/billing-and-pricing/overview) |
| Google Places API | 12 | `PERMANENT` | Essentials 10k/tháng, Pro 5k/tháng, IDs free | Details $5–$25/1k; Search $32–$40/1k | Bắt buộc field mask `X-Goog-FieldMask`; 1 field Enterprise làm tăng cước cả req | [Google Places Pricing](https://developers.google.com/maps/documentation/places/web-service/usage-and-billing) |

## Evidence & maintenance

- Evidence: `VERIFIED`; live re-verification completed on 2026-11-01 via multi-agent research fanout.
- Score: `NOT_EVALUATED` — workload, legal/security checks, benchmarks and price region are not yet supplied.
- Update pricing and source **here only**; pillar pages should never duplicate provider prices.
- [Evaluation matrix](../docs/01-evaluation-matrix.md) · [Lifecycle](../docs/lifecycle.md)
