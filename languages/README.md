# Programming languages — lựa chọn theo workload

**Phạm vi:** Rust, Go, TypeScript, Python và Swift. **Evidence review:** 2026-11-01. Đây là lớp **ngôn ngữ, runtime, framework và toolchain**, không phải service offering hay **pillar thứ 13**. Các liên kết nguồn hỗ trợ từng nhận định, không xác nhận chung về hiệu năng, giá hoặc production readiness.

## Bảng chọn nhanh

| Ngôn ngữ | Điểm xuất phát hợp lý | Không mặc định chọn khi | Profile |
|---|---|---|---|
| Rust | Native CLI/runtime, parsing, memory/performance-sensitive components | CRUD thông thường, tốc độ giao hàng quan trọng hơn native control | [Rust](rust.md) |
| Go | Network/backend/CLI, concurrent services, cloud tooling | UI browser/native Apple hoặc thư viện ML chuyên dụng | [Go](go.md) |
| TypeScript | Browser/fullstack web, typed Node APIs, orchestration gần JS SDKs | Low-level native / Python-native ML không có lý do cho TS | [TypeScript](typescript.md) |
| Python | ML/AI, data processing, automation, APIs quanh Python libraries | Native Apple UI, native component đã đo yêu cầu tài nguyên ngặt | [Python](python.md) |
| Swift | iOS/macOS/Apple UI, app integrations; Swift server khi phù hợp | Browser frontend hoặc đội ngũ/target không hỗ trợ Swift | [Swift](swift.md) |

Đây là **heuristic**, không phải benchmark hoặc ranking. Mặc định chọn **một ngôn ngữ cho một component**; chỉ thêm ngôn ngữ khi lợi ích đo được vượt chi phí tích hợp.

## Scope và single source of truth

- **Language:** type system, memory model, concurrency, interoperability. **Runtime/toolchain:** Node/Deno, CPython, Rust/Cargo, Go toolchain, Swift/SwiftPM/Xcode. **Framework/library:** Next.js, NestJS, FastAPI, Django, axum, Gin, SwiftUI, Vapor.
- **Infrastructure và third-party:** cloud, database, storage, networking, observability, secrets, AI API thuộc [12 pillars](../pillars/README.md). Giá, free tier, licensing terms của dịch vụ và service evidence status vẫn chỉ nằm ở [provider profiles](../providers/README.md).
- **Không copy facts sang nhiều nơi:** language profiles chỉ nêu fit, capability, compatibility, trade-offs, link chính thức và câu hỏi quyết định. Framework OSS không đồng nghĩa hosting/vận hành miễn phí.
- **Không chồng ECC:** đây là WHAT/WHY và bằng chứng chọn công nghệ; kiến trúc triển khai HOW do target project và ECC quản lý.

## Framework, infrastructure và third-party compatibility

- **Web/backend:** Next.js/NestJS (TypeScript), FastAPI/Django (Python), net/http/Gin (Go), axum/Tokio (Rust), Vapor/Hummingbird (Swift) là **candidates theo workload**; mỗi framework có version/adapter/runtime constraints riêng, không tương đương hoàn toàn.
- **Provider examples:** [Supabase](../providers/supabase.md), [Vercel](../providers/vercel.md), [Cloudflare](../providers/cloudflare.md). Trước khi chọn phải kiểm SDK theo ngôn ngữ, target runtime/region, auth model, secret handling, quotas, egress và tính portability; không suy SDK/serverless compatibility chỉ từ brand.
- **Storage/data/messaging/observability/AI:** tham khảo [pillars](../pillars/README.md) rồi mở file provider cho pricing/free tier và evidence. Không gán một provider mặc định cho cả 5 ngôn ngữ.
- **Client boundary:** app Swift hoặc browser TypeScript không được chứa server-side service secrets; xác minh token scope, data access policy, SDK version và offline behavior.

## Decision contract cho coding agents

1. **Workload:** web/mobile/CLI/API/AI/native; OS/CPU, offline, network, throughput, latency, scale, data sensitivity và integration.
2. **Smallest fit:** standard library trước, framework khi giải quyết nhu cầu thật; ghi lý do chọn và một fallback. Không thêm abstraction chỉ vì công nghệ có.
3. **Hard gates:** compiler/runtime & SDK support, target OS/ABI, maintained versions, compatibility, licensing/redistribution, security/privacy và deploy/rollback; thiếu bằng chứng đánh dấu **UNKNOWN**.
4. **Correctness/QA:** type checking khác runtime validation; test trust boundary, auth/secrets, failure/cancellation, races, retries/idempotency và cross-language contracts.
5. **Comparative evidence:** đo cùng workload p95/p99, CPU, RAM, cold start, throughput, CI/build time, cost vận hành, developer maintenance, ecosystem health. Benchmark của nhà cung cấp không phải universal result.
6. **Output:** chọn + scope, trade-offs, phương án không chọn, nguồn + ngày, assumptions/UNKNOWN, cách verify thực tế và exit strategy.

**Integration KISS:** Ưu tiên HTTP/OpenAPI hoặc protocol đã có ở boundary. Chỉ dùng FFI, native bindings hoặc đa runtime nếu có yêu cầu đo được. Mọi boundary cần schema version, auth, error contract, observability, test tương thích và ownership dữ liệu rõ ràng.

**Freshness:** Đánh giá phiên bản, SDK, platform, license và provider pricing lại trước quyết định production; ngày review chỉ là snapshot.

## Framework và decision navigation

- [Library catalog](../libraries/README.md) — curated code dependencies, standard-library fallbacks and evidence gates.
- [Framework catalog](../frameworks/README.md) — compatibility, anti-fit, licensing và operational checks.
- [Decision evidence](../decisions/README.md) — workload assumptions, hard gates, measured vs unknown costs, conditional choice/fallback.
