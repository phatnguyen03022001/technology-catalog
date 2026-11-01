# Framework catalog — 5 language ecosystems

**Snapshot reviewed:** 2026-11-01. Framework ≠ language ≠ runtime ≠ cloud provider. Đây là hồ sơ **WHAT/WHY** để chọn technology, không hướng dẫn triển khai HOW. Chỉ lưu định tính có nguồn; benchmark, version security, pháp lý và fit production là **UNKNOWN** nếu chưa đo/xác minh.

| Language | Candidate | Fit | Profile |
|---|---|---|---|
| TypeScript | Next.js | Fullstack React, SSR/server rendering & routing | [Next.js](nextjs.md) |
| TypeScript | NestJS | Modular server APIs, controller/DI conventions | [NestJS](nestjs.md) |
| Python | FastAPI | Python APIs, typed request validation, OpenAPI | [FastAPI](fastapi.md) |
| Python | Django | Data-centric web apps with admin/ORM | [Django](django.md) |
| Go | Gin | Go API routing, binding and middleware | [Gin](gin.md) |
| Rust | axum | Async HTTP APIs using Tokio/hyper and Tower | [axum](axum.md) |
| Swift | SwiftUI | Apple-native declarative app UI | [SwiftUI](swiftui.md) |
| Swift | Vapor | Swift server-side HTTP APIs | [Vapor](vapor.md) |

**Default principle:** Prefer an existing framework/conventions; use standard libraries when sufficient (Go `net/http` is the primary comparator for Gin). Choosing a framework does not automatically choose hosting, DB, storage, networking or observability.

Every new `frameworks/*.md` profile must appear exactly once in the index. CI checks the required sections, ISO `**Reviewed:**` date (not in the future), and official HTTPS link structure. These tests **cannot establish that a claim is correct or that a framework is secure**.

Each profile must state **fit, anti-fit, compatibility, maturity/review risks, licensing, test/operational questions and official evidence**. Documentation claims are scoped to their source; maturity ratings and rankings are not inferred from popularity.

**Code dependency selection:** [Libraries](../libraries/README.md) is the canonical shortlist for reusable packages; frameworks stay here.

**Provider evidence SSOT:** [Providers](../providers/README.md) · [Pillars](../pillars/README.md) · [Decision records](../decisions/README.md) · [Languages](../languages/README.md).
