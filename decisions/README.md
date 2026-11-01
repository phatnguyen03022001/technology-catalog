# Technology decisions — evidence by workload

**Reviewed:** 2026-11-01. Decision record = workload assumptions + hard gates + candidate comparison + conditional choice/fallback + evidence + validation to unlock production. **Không khẳng định đã triển khai, đo benchmark hoặc xác minh TCO** nếu chưa có dữ liệu.

| Case | Workload giả định | Conditional choice | Gate |
|---|---|---|---|
| [Web content product](web-fullstack.md) | Web UI, SSR/SEO, forms, authenticated users | Next.js | CONDITIONAL; deploy/SSR workload test pending |
| [Python AI API](python-ai-api.md) | Existing Python inference code, JSON API, model worker | FastAPI | CONDITIONAL; inference/concurrency/TCO pending |
| [Network API / gateway](network-service.md) | Go-friendly HTTP gateway, modest routing and retries | Go net/http initially | CONDITIONAL; traffic/memory benchmark pending |
| [Native Apple app](apple-native.md) | iPhone/macOS app, device integrations, offline UI | SwiftUI | CONDITIONAL; SDK/device/test/distribution pending |

## Decision evidence contract

1. **Scope + constraints:** actual application, workload volumes and nonfunctional requirements. In these four reference cases inputs are **assumed**, not verified production data.
2. **Alternatives:** include standard library or existing stack; explicit fit/anti-fit and sources.
3. **Hard gates:** functional, security/privacy, legal/licensing, cost and portability/recovery are PASS/FAIL/**UNKNOWN** independently; an UNKNOWN critical gate blocks production.
4. **TCO:** one owner/account subscription + included quotas consumed once + compute/storage/egress + usage overage + engineering/operations + taxes. No dollar total without region, unit rates, measured consumption and time horizon. Provider prices remain exclusively in [provider SSOT](../providers/README.md).
5. **Empirical verification:** compare candidates on identical realistic workload, version+region+hardware, with p95/p99, throughput, peak memory, failures/retry and build/deploy costs. Mark **NOT_MEASURED** when missing; do not invent advantages.
6. **Recommendation:** candidate, alternative, trigger to revisit, rollback/exit, dated source URLs. Decision is **APPROVED_FOR_PRODUCTION** only after an owner fills all non-negotiable gates and measured input.

## CI contract và quyền phê duyệt

- Mọi `decisions/*.md` (trừ README) phải được liên kết **đúng một lần** trong bảng index và có một `**Status:**` hợp lệ. Cột `Gate` tại index phải khớp `CONDITIONAL` hoặc `APPROVED`.
- `CONDITIONAL_NOT_PRODUCTION` không được chứa `APPROVED_FOR_PRODUCTION` ở bất kỳ vị trí nào. Các hard gates hiện thiếu bằng chứng vẫn là `UNKNOWN`; không được suy production approval từ CI.
- `APPROVED_FOR_PRODUCTION` chỉ được ghi khi **đã có project và workload thật**, năm hard gates (Functional, Security/privacy, Legal/licensing, Cost/TCO, Portability/recovery) đều ghi `**PASS**` và dẫn link evidence riêng trên mỗi dòng, không có `UNKNOWN`, `NOT_MEASURED`, `REFERENCE_SCENARIO_NOT_MEASURED` hoặc nhãn conditional. Dùng heading `## Hard gates` (không dùng `## Hard gates & unknown evidence`).
- Phải có `## Approval evidence` với các dòng `- Owner:`, `- Project:`, `- Workload ID:`, `- Benchmark evidence: [artifact](https://...)`, `- TCO evidence: [artifact](https://...)` và `- Approval date: YYYY-MM-DD`; đây là yêu cầu **cấu trúc tối thiểu**, không chứng minh các artifact là thật.
- Owner phải xác minh độc lập các nguồn, bằng chứng thực nghiệm, legal/commercial và chi phí, sau đó mới phê duyệt. **CI PASS không cấp quyền tự động phê duyệt production**. Các URL/tài liệu có thể bị thay đổi hoặc ngụy tạo và cần kiểm tra thủ công ở thời điểm chọn stack.

[Library candidates](../libraries/README.md) · [Evaluation matrix](../docs/01-evaluation-matrix.md) · [Language profiles](../languages/README.md) · [Framework profiles](../frameworks/README.md).

New real-project decisions can be added **only when a real workload and evidence exist**, not to make the folder look bigger.
