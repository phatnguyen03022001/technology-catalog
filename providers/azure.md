# Microsoft Azure

> **Provider SSOT.** Service claims and price evidence are recorded per offering below. `SOURCE_LINKED_SNAPSHOT` is not a current-price verification.

**Offerings:** 6 · **Pillars:** [01](../pillars/01-compute-runtime/README.md), [03](../pillars/03-storage-media/README.md), [04](../pillars/04-networking-edge/README.md), [06](../pillars/06-messaging-async/README.md), [07](../pillars/07-identity-security/README.md)

| Service | Primary pillar | Free kind | Free tier/credits | Paid pricing | Caveat | Official source | Evidence status | Evidence checked |
|---|---|---|---|---|---|---|---|---|
| Azure App Service | 01 | `PERMANENT` | Gói F1 Free: 60 CPU phút/ngày; 1 GB bộ nhớ lưu trữ; tối đa 10 ứng dụng | Basic B1 từ ~$13/tháng; Standard S1 ~$73/tháng | Gói F1 không hỗ trợ Custom Domain, không có chứng chỉ SSL riêng; tắt khi hết 60 CPU phút/ngày | [Azure App Service Pricing](https://azure.microsoft.com/pricing/details/app-service/) | `SOURCE_LINKED_SNAPSHOT` | — |
| Azure Functions | 01 | `PERMANENT` | 1.000.000 executions/tháng + 400.000 GB-giây Always Free | Consumption: $0,20 / 1M executions; $0,000016 / GB-giây | Yêu cầu gắn Azure Storage Account (tính phí storage riêng cho runtime blob & metrics) | [Azure Functions Pricing](https://azure.microsoft.com/pricing/details/functions/) | `SOURCE_LINKED_SNAPSHOT` | — |
| Azure Blob Storage | 03 | `TIME_LIMITED_TRIAL` | 12 tháng đầu: 5 GB LRS Hot Block Blob; 20k read ops; 10k write ops | Hot LRS ~$0,018-$0,0208/GB-mo; Write $5,00/1M; Read $0,40/1M; Egress $0,087/GB | Không có free vĩnh viễn (chỉ 12 tháng đầu); nhiều loại meter phức tạp | [Azure Blob Pricing](https://azure.microsoft.com/en-us/pricing/details/storage/blobs/) | `SOURCE_LINKED_SNAPSHOT` | — |
| Azure Front Door | 04 | `UNKNOWN` | Free allowance riêng của Front Door chưa được xác minh; credit Azure dùng chung không phải quota của dịch vụ | Giá phụ thuộc tier, region và usage; các giá snapshot cũ cần calculator xác nhận | Không phân loại credit cấp Azure thành free plan riêng của Front Door. | [Azure Front Door Pricing](https://azure.microsoft.com/en-us/pricing/details/frontdoor/) | `SOURCE_LINKED_SNAPSHOT` | — |
| Azure Service Bus | 06 | `TIME_LIMITED_TRIAL` | 12 tháng đầu kèm Azure Free Account (750h Standard + 13M ops); KHÔNG có free vĩnh viễn | Basic $0 base + $0,05/1M ops; Standard base ~$10/tháng + $0,05/1M ops | Hết 12 tháng Standard chịu phí sàn $10/tháng dù 0 request; Basic thiếu topic/subscription | [Pricing/docs](https://azure.microsoft.com/en-us/pricing/details/service-bus/) | `SOURCE_LINKED_SNAPSHOT` | — |
| Azure Key Vault | 07 | `NO_MONTHLY_BASE` | $0 phí lưu trữ cơ bản (lưu unlimited secret, key, cert) | $0,03/10.000 operations (GET, PUT, LIST); HSM keys $1/key/tháng | Không có phí sàn nhưng cần cache client-side tránh loop query gây tăng bill | [azure.microsoft.com/en-us/pricing/details/key-vault](https://azure.microsoft.com/en-us/pricing/details/key-vault/) | `SOURCE_LINKED_SNAPSHOT` | — |

## Evidence & maintenance

- Score: `NOT_EVALUATED` — workload, legal/security checks, benchmarks and price region are not yet supplied.
- Update pricing and source **here only**; pillar pages should never duplicate provider prices.
- [Evaluation matrix](../docs/01-evaluation-matrix.md) · [Lifecycle](../docs/lifecycle.md)
