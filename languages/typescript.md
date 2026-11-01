# TypeScript

**Evidence review:** 2026-11-01 · [Quay lại so sánh](README.md)

## Fit & trade-offs

- **Phù hợp:** browser/fullstack web, typed Node.js backend, API/agent orchestration, tools tích hợp với JS/TS SDK.
- **Lợi thế kỹ thuật:** static checking cải thiện contracts và refactoring; cùng JavaScript ecosystem cho browser/server.
- **Giới hạn:** types bị xóa khi chạy và **không validate JSON/API input**; runtime (Node/Deno/Bun), TypeScript compiler và framework (Next/Nest) là các lớp khác nhau. CPU-bound work có thể cần worker/native module/service riêng; đo thay vì đoán.

## Ecosystem và điểm xuất phát KISS

| Lớp | Mặc định | Khi nào thêm công nghệ |
|---|---|---|
| Type safety | `tsc --noEmit`, `strict`, runtime input validation | Schema library khi payload từ ngoài hoặc shared contracts cần validate |
| Runtime | **Node.js** nếu SDK/npm compatibility là ưu tiên | **Deno** nếu permission/toolchain model phù hợp; Bun là candidate cần kiểm chứng SDK/platform |
| Browser/fullstack | Browser APIs/React theo nhu cầu | **Next.js** cho App Router, SSR/server components và integrated fullstack |
| Backend/API | Node APIs/framework đang dùng | **NestJS** khi cần modules/DI conventions thật sự; cân nhắc abstraction/overhead |
| Data/agent workers | HTTP/OpenAPI, driver và SDK đã xác minh | Queue/workers cho durable job và retries nếu requirements có |

**Quality gates tham khảo:** pin runtime và lockfile, `tsc --noEmit`, lint, unit/integration/e2e tests và schema boundary tests, dependency audit. Node native TypeScript type stripping **không type-check**, vẫn phải chạy compiler checker riêng.

**Trước production:** runtime target Node/edge khác nhau, ESM/CJS, version compatibility, SDK support, server-vs-client secret boundaries, auth/session, observability, queues/timeouts, cold start, bandwidth và backend provider costs; kiểm chứng deployment thực, không suy compatibility từ tên framework.

**Không mặc định chọn:** native low-level CPU/memory-sensitive component hoặc thư viện ML chỉ có Python mà phải tạo thêm bridge.

## Official evidence

- [TypeScript handbook — type erasure](https://www.typescriptlang.org/docs/handbook/typescript-from-scratch)
- [TypeScript strict compiler option](https://www.typescriptlang.org/tsconfig/strict)
- [Node.js native TypeScript — không type-check](https://nodejs.org/learn/typescript/run-natively)
- [Deno TypeScript runtime & checking](https://docs.deno.com/runtime/fundamentals/typescript/)
- [Next.js App Router](https://nextjs.org/docs/app)
- [NestJS backend framework](https://docs.nestjs.com/recipes/documentation)
