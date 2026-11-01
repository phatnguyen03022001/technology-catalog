# Amazon Web Services

> **Provider SSOT.** Nguồn từ snapshot **2026-11-01**, có URL chính thức đã qua kiểm chứng (VERIFIED). Chỉ dùng để nghiên cứu; xác minh lại trước khi mua hoặc triển khai production.

**Offerings:** 13 · **Pillars:** [01](../pillars/01-compute-runtime/README.md), [02](../pillars/02-databases-data/README.md), [03](../pillars/03-storage-media/README.md), [04](../pillars/04-networking-edge/README.md), [05](../pillars/05-cache-traditional-search/README.md), [06](../pillars/06-messaging-async/README.md), [07](../pillars/07-identity-security/README.md), [08](../pillars/08-devops-delivery/README.md), [11](../pillars/11-communications/README.md)

| Service | Primary pillar | Free kind | Free tier/credits | Paid pricing | Caveat | Official source |
|---|---|---|---|---|---|---|
| Amazon EC2 | 01 | `TIME_LIMITED_TRIAL` | 750 giờ/tháng t2.micro/t3.micro trong 12 tháng đầu; 30 GB EBS | On-Demand từ ~$3,50–$8/tháng + $0,005/giờ ($3,65/tháng) IPv4 công khai | Hết 12 tháng tính giá chuẩn; IPv4 công khai tính phí riêng; egress $0,09/GB | [AWS EC2 Pricing](https://aws.amazon.com/ec2/pricing/) |
| AWS Lambda | 01 | `PERMANENT` | 1.000.000 requests/tháng + 400.000 GB-giây compute Always Free | $0,20 / 1M requests; $0,00001667 / GB-giây; Provisioned Concurrency tính riêng | Vượt trần 400k GB-s tự động trừ tiền; không bao gồm VPC NAT Gateway hay Data Transfer out | [AWS Lambda Pricing](https://aws.amazon.com/lambda/pricing/) |
| Amazon DynamoDB | 02 | `PERMANENT` | 25 GB storage; 25 WCU; 25 RCU Always Free (~200M req/mo) | Provisioned PAYG; On-Demand PAYG | Free 25 WCU/RCU CHỈ áp dụng ở chế độ Provisioned Standard | [DynamoDB Pricing](https://aws.amazon.com/dynamodb/pricing/) |
| Amazon S3 | 03 | `TIME_LIMITED_TRIAL` | 12 tháng đầu: 5 GB Standard; 20k GET; 2k PUT/POST/LIST; 15 GB egress/tháng | Standard $0,023/GB-tháng; Class A $5,00/1M; Class B $0,40/1M; Egress $0,09/GB | Hết 12 tháng tính tiền 100%; egress trực tiếp rất đắt ($0,09/GB); nên bọc CloudFront | [AWS S3 Pricing](https://aws.amazon.com/s3/pricing/) |
| AWS CloudFront | 04 | `PERMANENT` | 1 TB/tháng DTO vĩnh viễn; 10M HTTP/HTTPS requests/tháng; 2M CloudFront Functions/tháng | Từ $0,085/GB (NA/EU), $0,0075–$0,010/10k requests | Egress ngoài 1 TB tính theo vùng; chỉ miễn phí khi đi qua CloudFront; Dedicated IP SSL $600/tháng | [Pricing/docs](https://aws.amazon.com/cloudfront/pricing/) |
| AWS Route 53 | 04 | `NONE_OR_CONDITIONAL` | Miễn phí truy vấn Alias tới AWS resources (CloudFront, ALB, S3); không có free zone vĩnh viễn | $0,50/hosted zone/tháng (25 zones đầu); $0,40/1M queries tiêu chuẩn | Phí cố định $0,50/zone/tháng dù không có traffic; endpoint ngoài AWS tính phí query chuẩn | [Pricing/docs](https://aws.amazon.com/route53/pricing/) |
| Amazon OpenSearch | 05 | `PERMANENT` | 12 tháng đầu AWS: 750h/tháng `t3.small.search` + 10 GB EBS | `t3.small` ~$26,28/tháng + storage; Serverless tối thiểu ~$700/tháng (4 OCUs) | Hết 12 tháng tính tiền 100%; `t3.small` chỉ có 2 GB RAM dễ bị OOM khi index nặng | [AWS OpenSearch Pricing](https://aws.amazon.com/opensearch-service/pricing/) |
| AWS SQS | 06 | `PERMANENT` | 1.000.000 requests/tháng Always Free vĩnh viễn (Standard/FIFO) | Standard $0,40/1M reqs; FIFO $0,50/1M reqs; egress theo vùng AWS | Mỗi API call tính 1 request; gói 64 KB; cần bật Long Polling 20s tránh cạn quota | [Pricing/docs](https://aws.amazon.com/sqs/pricing/) |
| AWS EventBridge | 06 | `PERMANENT` | 14.000.000 invocations/tháng EventBridge Scheduler; AWS management events $0 | Custom events $1,00/1M events; Scheduler sau 14M là $1,00/1M | Custom events không có free tier (tính từ event đầu tiên); Scheduler miễn phí 14M/tháng | [Pricing/docs](https://aws.amazon.com/eventbridge/pricing/) |
| AWS Secrets Manager | 07 | `NONE_OR_CONDITIONAL` | 0 free secret vĩnh viễn; trial 30 ngày | $0,40/secret/tháng; $0,05/10.000 API calls | Không có free vĩnh viễn; giải pháp thay thế free là AWS SSM Parameter Store ($0) | [aws.amazon.com/secrets-manager/pricing](https://aws.amazon.com/secrets-manager/pricing/) |
| AWS CodeBuild | 08 | `PERMANENT` | 100 build-mins/mo Always Free on `general1.small` / `arm1.small` | $0.005/min on `general1.small`; 1-min minimum per build | 100 mins is very low; S3 storage, CloudWatch logs, and egress billed extra | [AWS CodeBuild](https://aws.amazon.com/codebuild/pricing/) |
| Amazon SES | 11 | `NONE_OR_CONDITIONAL` | $0 / 0 email free (free tier 62k EC2 đã ngừng cho account mới) | À la carte $0,10/1k emails; Essentials $0,16/1k emails; Egress data $0,12/GB | Mới tạo bị khóa Sandbox (chỉ gửi tới email đã verify); cần tạo ticket xin mở prod | [AWS SES Pricing](https://aws.amazon.com/ses/pricing/) |
| AWS SNS | 11 | `PERMANENT` | 1M SNS publishes free; 1M Mobile Pushes free; 100k HTTP/HTTPS free | Mobile push $0,50/1M; HTTP $0,60/1M; Email $2,00/100k; SMS theo cước | Gói 64 KB tính 1 request; SMS không có free tier; thuần hạ tầng không có UI template | [AWS SNS Pricing](https://aws.amazon.com/sns/pricing/) |

## Evidence & maintenance

- Evidence: `VERIFIED`; live re-verification completed on 2026-11-01 via multi-agent research fanout.
- Score: `NOT_EVALUATED` — workload, legal/security checks, benchmarks and price region are not yet supplied.
- Update pricing and source **here only**; pillar pages should never duplicate provider prices.
- [Evaluation matrix](../docs/01-evaluation-matrix.md) · [Lifecycle](../docs/lifecycle.md)
