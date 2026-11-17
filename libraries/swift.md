# Swift — curated libraries

**Reviewed:** 2026-11-17 (SwiftUI and Vapor research); 12 existing package records preserve their individual earlier evidence dates. Reusable code packages only, never framework or managed service production approvals.

## Dependency choice

- **Standard library first:** Foundation, Swift Concurrency, OSLog and CryptoKit.
- **Add:** only for a documented capability that standard library and current dependencies do not sufficiently provide.
- **Keep:** do not migrate merely because a package appears in the catalog or has a newer release.
- **Remove/replace:** prove need, test compatibility and preserve a rollback path.
- **Verify:** target toolchain, platform, license, security advisories, dependency tree and realistic workload.

## SwiftUI capability screening (2026-11-17)

SwiftUI is an **Apple app frontend**, Vapor is a **separate server backend**. Shared Swift/SwiftPM language does not imply framework compatibility or mandatory dependencies. Native solutions are the default, and availability must be checked for each deployment target. This matrix is a screening decision, **not a build or production endorsement**.

Native references: [SwiftUI](https://developer.apple.com/documentation/swiftui/) · [Observation](https://developer.apple.com/documentation/observation) · [SwiftData](https://developer.apple.com/documentation/swiftdata) · [Swift Charts](https://developer.apple.com/documentation/charts) · [StoreKit](https://developer.apple.com/documentation/storekit/) · [Swift Testing](https://developer.apple.com/documentation/testing/).

| Capability | Native-first comparator | External package decision |
|---|---|---|
| C01 | SwiftUI views, layouts, native controls | No generic UI library; app-owned components first. |
| C02 | SwiftUI animation, Canvas, Swift Charts | Lottie only for authored vector-motion assets. |
| C03 | Form, NavigationStack and presentation | Native navigation; no obligatory router. |
| C04 | Accessibility APIs, String Catalogs, FormatStyle | Native accessibility/localization; no package. |
| C05 | State, Binding, Observation, environment | TCA for complex composition, effects and state testing. |
| C06 | URLSession, URLCache, async/await, optional CloudKit | No generic sync dependency; Nuke is image-specific. |
| C07 | Codable, JSONEncoder/Decoder | Existing apple/swift-openapi-generator for maintained OpenAPI contracts. |
| C08 | SwiftData, Core Data, SQLite | Existing groue/GRDB.swift when lower-level SQL is needed. |
| C09 | URLSession, URLRequest, URLProtocol | Alamofire not required; swift-nio is not default app HTTP. |
| C10 | AuthenticationServices, Sign in with Apple, Keychain | Native auth; RevenueCat entitlements are not authentication. |
| C11 | searchable, Core Spotlight, system search | Native indexing unless measured requirements differ. |
| C12 | AsyncImage, PhotosUI, AVFoundation, fileImporter | Nuke for advanced image pipeline; swift-system remains low-level. |
| C13 | Task, actors, AsyncSequence, AsyncStream | Existing swift-async-algorithms for needed combinators. |
| C14 | Cancellation, error handling, app-owned retry/backoff | No universal retry package. |
| C15 | Keychain, CryptoKit, Secure Enclave where available | Existing swift-crypto only for justified cross-platform needs. |
| C16 | Native collections, NSCache, Instruments | Existing swift-collections/algorithms for measured gaps. |
| C17 | Swift Testing, XCTest, XCUITest | SnapshotTesting in test target; real-device/accessibility separate. |
| C18 | OSLog, MetricKit, Instruments | Existing swift-log/tracing are not automatic app dependencies. |
| C19 | Compiler diagnostics and Xcode/SwiftPM tooling | SwiftLint for lint, SwiftFormat for formatting; separate decisions. |
| C20 | Core ML, Apple AI APIs where available, StoreKit | RevenueCat for managed IAP; MCP SDK remains PARTIAL/BLOCKED. |

**Evaluated, not added:** [Kingfisher](https://github.com/onevcat/Kingfisher) and [SDWebImageSwiftUI](https://github.com/SDWebImage/SDWebImageSwiftUI) overlap Nuke for the screened remote-image use case; revisit for concrete format/integration needs. [Alamofire](https://github.com/Alamofire/Alamofire) needs a demonstrated gap beyond URLSession. [ViewInspector](https://github.com/nalexn/ViewInspector) is a conditional test-introspection alternative, not device-UI proof. [swiftlang/swift-format](https://github.com/swiftlang/swift-format) is an alternative formatter; do not impose both formatters. These are conditional exclusions, **not universal rejection**.

**Evidence boundary:** Tagged SwiftPM manifests, tagged licenses, upstream releases and repository metadata reviewed 2026-11-17. Swift tools version does not prove strict Swift 6 concurrency compliance; declared platforms do not establish target integration, performance, accessibility or App Store acceptance. Swift compilation, Xcode/physical-device testing, pinned transitive dependency security review and TCO benchmarking were **NOT_PERFORMED**. No dependency is required merely because listed.

## Vapor capability screening (2026-11-17)

**Scope:** Vapor 4.122.3 is the reviewed **stable tag**, not Vapor 5 beta or its main-branch manifest. Vapor is a SwiftNIO server framework, SwiftUI is an Apple frontend; shared language does not mean shared runtime dependencies. This matrix is native-first catalog guidance only. Sources: [official Vapor docs](https://docs.vapor.codes/), [Vapor 4.122.3 tagged manifest](https://github.com/vapor/vapor/blob/4.122.3/Package.swift), [Swift server ecosystem](https://www.swift.org/packages/server.html), [queues documentation](https://docs.vapor.codes/advanced/queues/).

| Capability | Decision | Vapor / Swift Server assessment |
|---|---|---|
| C01 | NOT_APPLICABLE | JSON APIs have no Apple UI; Leaf/HTML rendering conditional. |
| C02 | NOT_APPLICABLE | No animation or visualization in API-only services; SwiftUI/Lottie remain Apple-only. |
| C03 | NATIVE_FIRST | Vapor routes, Content/Codable, form/multipart and body-size limits. |
| C04 | NATIVE_FIRST | Foundation locale, Accept-Language and translated server errors; frontend accessibility separate. |
| C05 | NATIVE_FIRST | Vapor Application storage and lifecycle; actor isolation, Sendable and request-scoped state. |
| C06 | ADDED | Use Vapor Client first; direct AsyncHTTPClient for special outbound pooling, timeouts or streaming. |
| C07 | ADDED | Codable first; OpenAPIVapor transport only with maintained generated OpenAPI contracts. |
| C08 | ADDED | Fluent ORM and one chosen PostgreSQL driver when actually needed; SQL/SQLite alternatives. |
| C09 | EXISTING | Vapor + SwiftNIO handle routing, HTTP/2 and WebSockets; verify EventLoop/backpressure. |
| C10 | ADDED | Vapor sessions/authentication first; JWT only when justified; audience and authorization distinct. |
| C11 | NATIVE_FIRST | DB full-text index and queries before external search. |
| C12 | NATIVE_FIRST | Multipart, streaming, files; enforce upload caps, path checks and retention. |
| C13 | CONDITIONAL | A Task is not durable; Redis queue driver PARTIAL/BLOCKED until Swift 6/queue integration verified. |
| C14 | NATIVE_FIRST | Vapor middleware/errors; application-specific timeouts, idempotency, bounded retries and rate limits. |
| C15 | EXISTING | swift-crypto and swift-nio-ssl are transitive; manage secrets, TLS/proxy and SSRF boundaries. |
| C16 | ADDED | In-memory cache first; Vapor Redis for proven cross-worker cache/session needs. |
| C17 | NATIVE_FIRST | VaporTesting and XCTVapor are products of Vapor; XCTest/Swift Testing, no extra repo. |
| C18 | ADDED | SwiftLog/Metrics/Tracing already integrated; swift-otel only when exporters and collectors required. |
| C19 | EXISTING | SwiftPM, compiler, current lint/format tools; separate Linux CI and Xcode workflows. |
| C20 | EXISTING | AI HTTP integration as needed; existing MCP Swift SDK remains PARTIAL/BLOCKED. |

**Runtime and operations:** Pin Swift/Vapor/package graph and verify strict Swift 6 concurrency, actor isolation, Sendable, EventLoopFuture/async interop, no blocking EventLoops, bounded work, cancellation and graceful shutdown. Verify HTTP/1.1/2, WebSockets, body limits, backpressure, client disconnects, TLS termination/proxy trust, outbound SSRF controls, retry/idempotency and failure handling. Test DB connection pools, migrations, transaction scope, file upload/streaming and storage lifecycle. Durable jobs require a real queue/driver and operating model; metrics/tracing API does not automatically export telemetry. Redis, PostgreSQL, queues and collectors are conditional infrastructure, never defaults.

**Evaluated, not added:** [vapor/queues](https://github.com/vapor/queues) is the framework behind a queue driver; official docs tell applications to install the driver instead. [vapor/fluent-sqlite-driver](https://github.com/vapor/fluent-sqlite-driver) is the SQLite alternative, not an additional default database; [vapor/postgres-nio](https://github.com/vapor/postgres-nio) offers raw PostgreSQL instead of the Fluent choice. [vapor/jwt-kit](https://github.com/vapor/jwt-kit) is the core library under the Vapor JWT integration, not an extra default. [vapor/leaf](https://github.com/vapor/leaf) suits HTML server rendering, not JSON-only APIs. [swift-server/swift-service-lifecycle](https://github.com/swift-server/swift-service-lifecycle) can manage independent services, but should not duplicate Vapor lifecycle. [apple/swift-nio-ssl](https://github.com/apple/swift-nio-ssl) and [apple/swift-metrics](https://github.com/apple/swift-metrics) are already transitively declared in Vapor 4.122.3; direct dependencies require a distinct need. [apple/swift-openapi-runtime](https://github.com/apple/swift-openapi-runtime) is generated-code support, not a Vapor server transport. `VaporTesting` comes from `vapor/vapor`, not a separate repository. SwiftUI-only packages do not inherit Vapor/Linux support.

**Security/evidence gates:** [Vapor's JWTKit 5.8.0 security release notice (2026-10-28)](https://blog.vapor.codes/posts/jwt-kit-5-8-0/) describes vulnerable audience handling, headers and X.509 checks; `vapor/jwt` 5.2.0 integrates the fix, but callers must still use expected-audience verification. Tagged SwiftPM manifests, tagged licenses and release metadata reviewed **2026-11-17 UTC**. No native Swift compilation, SwiftPM dependency-resolution test, Linux/macOS binary verification, Swift 6 strict-concurrency test, full pinned advisory clearance, actual Vapor integration, benchmarks or TCO measurements were run (**NOT_VERIFIED**).

## Entries

### `apple/swift-collections`
- **Package:** `apple/swift-collections`
- **Capability:** C16 — Performance & Cache
- **Tags:** `collections`
- **Language/runtime:** Swift / SwiftPM
- **Fit:** Deque and specialized collections, when the current codebase demonstrably needs it.
- **Anti-fit:** Array, Set, Dictionary and native collection types suffice.
- **Fallback:** Swift Array/Dictionary/Set and Sequence.
- **Compatibility:** Swift tools >= 6.4 (tag 1.7.5); check deployment platform and integrations.
- **Maintenance:** GitHub tag 1.7.5; upstream pushed 2026-10-27; activity does not prove long-term support.
- **License:** Apache-2.0
- **Official source:** [official registry or upstream](https://github.com/apple/swift-collections); [upstream/manifest](https://github.com/apple/swift-collections/blob/1.7.5/Package.swift)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-01
- **Unknowns:** The latest tagged manifest requires Swift tools 6.4; OS deployment matrix must be checked separately. Security advisories: UNKNOWN; exact target support, comparative benchmarks and operational burden: NOT_MEASURED. Recheck before project selection.
- **Selection:** EVALUATE

### `apple/swift-algorithms`
- **Package:** `apple/swift-algorithms`
- **Capability:** C16 — Performance & Cache
- **Tags:** `collection-algorithms`
- **Language/runtime:** Swift / SwiftPM
- **Fit:** Sequence and collection algorithms, when the current codebase demonstrably needs it.
- **Anti-fit:** Standard Sequence APIs or a clear loop solve the task.
- **Fallback:** Swift Array/Dictionary/Set and Sequence.
- **Compatibility:** Swift tools >= 5.7 (tag 1.2.1); check deployment platform and integrations.
- **Maintenance:** GitHub tag 1.2.1; upstream pushed 2026-09-25; activity does not prove long-term support.
- **License:** Apache-2.0
- **Official source:** [official registry or upstream](https://github.com/apple/swift-algorithms); [upstream/manifest](https://github.com/apple/swift-algorithms/blob/1.2.1/Package.swift)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-01
- **Unknowns:** Security advisories: UNKNOWN; exact target support, comparative benchmarks and operational burden: NOT_MEASURED. Recheck before project selection.
- **Selection:** EVALUATE

### `apple/swift-argument-parser`
- **Package:** `apple/swift-argument-parser`
- **Capability:** C19 — Developer Tooling
- **Language/runtime:** Swift / SwiftPM
- **Fit:** Typed Swift command line parsing, when the current codebase demonstrably needs it.
- **Anti-fit:** Small CLI options need only CommandLine.arguments.
- **Fallback:** CommandLine.arguments.
- **Compatibility:** Swift tools >= 6.0 (tag 1.8.2); check deployment platform and integrations.
- **Maintenance:** GitHub tag 1.8.2; upstream pushed 2026-10-30; activity does not prove long-term support.
- **License:** Apache-2.0
- **Official source:** [official registry or upstream](https://github.com/apple/swift-argument-parser); [upstream/manifest](https://github.com/apple/swift-argument-parser/blob/1.8.2/Package.swift)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-01
- **Unknowns:** Security advisories: UNKNOWN; exact target support, comparative benchmarks and operational burden: NOT_MEASURED. Recheck before project selection.
- **Selection:** EVALUATE

### `apple/swift-log`
- **Package:** `apple/swift-log`
- **Capability:** C18 — Observability
- **Language/runtime:** Swift / SwiftPM
- **Fit:** Common Swift logging API, when the current codebase demonstrably needs it.
- **Anti-fit:** Apple-only app already uses adequate OSLog instrumentation.
- **Fallback:** OSLog.
- **Compatibility:** Swift tools >= 6.2 (tag 1.16.2); check deployment platform and integrations.
- **Maintenance:** GitHub tag 1.16.2; upstream pushed 2026-10-26; activity does not prove long-term support.
- **License:** Apache-2.0
- **Official source:** [official registry or upstream](https://github.com/apple/swift-log); [upstream/manifest](https://github.com/apple/swift-log/blob/1.16.2/Package.swift)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-01
- **Unknowns:** Security advisories: UNKNOWN; exact target support, comparative benchmarks and operational burden: NOT_MEASURED. Recheck before project selection.
- **Selection:** EVALUATE

### `apple/swift-crypto`
- **Package:** `apple/swift-crypto`
- **Capability:** C15 — Security & Cryptography
- **Language/runtime:** Swift / SwiftPM
- **Fit:** CryptoKit-like cross-platform APIs, when the current codebase demonstrably needs it.
- **Anti-fit:** Apple CryptoKit covers the supported target platforms.
- **Fallback:** CryptoKit.
- **Compatibility:** Swift tools >= 6.2 (tag 5.0.3); check deployment platform and integrations.
- **Maintenance:** GitHub tag 5.0.3; upstream pushed 2026-10-23; activity does not prove long-term support.
- **License:** Apache-2.0
- **Official source:** [official registry or upstream](https://github.com/apple/swift-crypto); [upstream/manifest](https://github.com/apple/swift-crypto/blob/5.0.3/Package.swift)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-01
- **Unknowns:** Cross-platform crypto backend differs from Apple CryptoKit integration. Security advisories: UNKNOWN; exact target support, comparative benchmarks and operational burden: NOT_MEASURED. Recheck before project selection.
- **Selection:** EVALUATE

### `apple/swift-nio`
- **Package:** `apple/swift-nio`
- **Capability:** C09 — API & Networking
- **Language/runtime:** Swift / SwiftPM
- **Fit:** Custom event-loop networking, when the current codebase demonstrably needs it.
- **Anti-fit:** URLSession handles normal Apple app HTTP traffic.
- **Fallback:** Foundation URLSession.
- **Compatibility:** Swift tools >= 6.1 (tag 2.104.0); check deployment platform and integrations.
- **Maintenance:** GitHub tag 2.104.0; upstream pushed 2026-10-19; activity does not prove long-term support.
- **License:** Apache-2.0
- **Official source:** [official registry or upstream](https://github.com/apple/swift-nio); [upstream/manifest](https://github.com/apple/swift-nio/blob/2.104.0/Package.swift)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-01
- **Unknowns:** Event loop lifecycle, backpressure and shutdown are application responsibilities. Security advisories: UNKNOWN; exact target support, comparative benchmarks and operational burden: NOT_MEASURED. Recheck before project selection.
- **Selection:** EVALUATE

### `apple/swift-async-algorithms`
- **Package:** `apple/swift-async-algorithms`
- **Capability:** C13 — Async & Messaging
- **Language/runtime:** Swift / SwiftPM
- **Fit:** AsyncSequence combinators, when the current codebase demonstrably needs it.
- **Anti-fit:** Basic AsyncSequence iteration and transformation suffice.
- **Fallback:** AsyncSequence.
- **Compatibility:** Swift tools >= 6.2 (tag 1.1.7); check deployment platform and integrations.
- **Maintenance:** GitHub tag 1.1.7; upstream pushed 2026-10-05; activity does not prove long-term support.
- **License:** Apache-2.0
- **Official source:** [official registry or upstream](https://github.com/apple/swift-async-algorithms); [upstream/manifest](https://github.com/apple/swift-async-algorithms/blob/1.1.7/Package.swift)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-01
- **Unknowns:** Security advisories: UNKNOWN; exact target support, comparative benchmarks and operational burden: NOT_MEASURED. Recheck before project selection.
- **Selection:** EVALUATE

### `groue/GRDB.swift`
- **Package:** `groue/GRDB.swift`
- **Capability:** C08 — Persistence
- **Language/runtime:** Swift / SwiftPM
- **Fit:** SQLite data persistence, when the current codebase demonstrably needs it.
- **Anti-fit:** Existing SwiftData/Core Data/SQLite stack satisfies persistence needs.
- **Fallback:** current SQLite/SwiftData stack.
- **Compatibility:** Swift tools >= 6.1 (tag v7.11.1); check deployment platform and integrations.
- **Maintenance:** GitHub tag v7.11.1; upstream pushed 2026-09-29; activity does not prove long-term support.
- **License:** MIT
- **Official source:** [official registry or upstream](https://github.com/groue/GRDB.swift); [upstream/manifest](https://github.com/groue/GRDB.swift/blob/v7.11.1/Package.swift)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-01
- **Unknowns:** SQLite schema migration and concurrency must be tested on device. Security advisories: UNKNOWN; exact target support, comparative benchmarks and operational burden: NOT_MEASURED. Recheck before project selection.
- **Selection:** EVALUATE

### `apple/swift-system`
- **Package:** `apple/swift-system`
- **Capability:** C12 — Media & Files
- **Tags:** `file-descriptors`
- **Language/runtime:** Swift / SwiftPM
- **Fit:** Typed system and file descriptors, when the current codebase demonstrably needs it.
- **Anti-fit:** Foundation FileManager and FileHandle cover filesystem operations.
- **Fallback:** Foundation FileManager and FileHandle.
- **Compatibility:** Swift tools >= 6.1 (tag 1.8.1); check deployment platform and integrations.
- **Maintenance:** GitHub tag 1.8.1; upstream pushed 2026-10-21; activity does not prove long-term support.
- **License:** Apache-2.0
- **Official source:** [official registry or upstream](https://github.com/apple/swift-system); [upstream/manifest](https://github.com/apple/swift-system/blob/1.8.1/Package.swift)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-01
- **Unknowns:** Security advisories: UNKNOWN; exact target support, comparative benchmarks and operational burden: NOT_MEASURED. Recheck before project selection.
- **Selection:** EVALUATE

### `modelcontextprotocol/swift-sdk`
- **Package:** `modelcontextprotocol/swift-sdk`
- **Capability:** C20 — AI & Integrations
- **Language/runtime:** Swift / SwiftPM
- **Fit:** Official Swift MCP client/server SDK using SwiftPM for Apple-native or compatible Swift server tools.
- **Anti-fit:** No MCP interoperability; a normal app HTTP client via URLSession suffices.
- **Fallback:** Foundation URLSession or existing API SDK.
- **Compatibility:** Swift tools >=6.1 in tag 0.12.1; tag manifest lists macOS 13+, iOS 16+; README advertises Swift 6.0+/Xcode 16+. No verified support for MCP 2026-07-28.
- **Maintenance:** GitHub tag 0.12.1; inspected 2026-11-02; repository active 2026-10-31.
- **License:** Mixed Apache-2.0 for new/relicensed code and MIT for legacy contributions (upstream LICENSE transition).
- **Official source:** [official registry or upstream](https://github.com/modelcontextprotocol/swift-sdk); [upstream/manifest](https://github.com/modelcontextprotocol/swift-sdk/blob/0.12.1/Package.swift)
- **Evidence status:** PARTIAL
- **Evidence reviewed:** 2026-11-02
- **Unknowns:** README states MCP 2025-11-25 and differs from tagged tools-version. Check protocol negotiation, stdio/HTTP transport, pinned tag license and Apple deployment; never claim support for 2026-07-28. Tool permissions, untrusted tool output, SSRF, credential forwarding, cancellation and resource limits must be enforced independently. Security advisory applicability: UNKNOWN (no pinned-version OSV/GHSA review); target-specific integration, performance and TCO: NOT_MEASURED. Recheck official metadata and transitive dependencies before project adoption.
- **Selection:** BLOCKED

### `apple/swift-openapi-generator`
- **Package:** `apple/swift-openapi-generator`
- **Capability:** C07 — Data Contracts
- **Language/runtime:** Swift / SwiftPM
- **Fit:** Generate Swift client/server API models from OpenAPI when cross-language contracts are maintained.
- **Anti-fit:** Simple few-endpoint Codable + URLSession app; no shared OpenAPI schema.
- **Fallback:** Codable + URLSession or established generated client.
- **Compatibility:** Swift tools >=6.2 in tag 1.14.3; generator runs on supported macOS/Linux/Windows hosts (not iOS app runtime); generated clients need a distinct runtime library and transport.
- **Maintenance:** GitHub tag 1.14.3; upstream pushed 2026-10-26.
- **License:** Apache-2.0
- **Official source:** [official registry or upstream](https://github.com/apple/swift-openapi-generator); [upstream/manifest](https://github.com/apple/swift-openapi-generator/blob/1.14.3/Package.swift)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-02
- **Unknowns:** Generator is a build tool, not HTTP transport; verify OpenAPI 3.x feature support, SwiftPM plugin, target OS and generated API runtime compatibility. Security advisory applicability: UNKNOWN (no pinned-version OSV/GHSA review); target-specific integration, performance and TCO: NOT_MEASURED. Recheck official metadata and transitive dependencies before project adoption.
- **Selection:** EVALUATE

### `apple/swift-distributed-tracing`
- **Package:** `apple/swift-distributed-tracing`
- **Capability:** C18 — Observability
- **Language/runtime:** Swift / SwiftPM
- **Fit:** Swift server/service-context tracing and instrumentation interfaces, with a separately configured backend/exporter.
- **Anti-fit:** Apple-only app already adequately instrumented with OSLog; no cross-service trace requirement.
- **Fallback:** OSLog or existing service instrumentation.
- **Compatibility:** Swift tools >=6.2 in tag 1.7.3; check Swift concurrency, server runtime and exporter package separately.
- **Maintenance:** GitHub tag 1.7.3; upstream pushed 2026-10-28.
- **License:** Apache-2.0
- **Official source:** [official registry or upstream](https://github.com/apple/swift-distributed-tracing); [upstream/manifest](https://github.com/apple/swift-distributed-tracing/blob/1.7.3/Package.swift)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-02
- **Unknowns:** Tracing API alone does not export telemetry; validate context propagation, privacy redaction, sampling and operational overhead. Security advisory applicability: UNKNOWN (no pinned-version OSV/GHSA review); target-specific integration, performance and TCO: NOT_MEASURED. Recheck official metadata and transitive dependencies before project adoption.
- **Selection:** EVALUATE

### `pointfreeco/swift-composable-architecture`
- **Package:** `pointfreeco/swift-composable-architecture`
- **Capability:** C05 — State Management
- **Tags:** `SwiftUI`, `state`, `composition`
- **Language/runtime:** Swift / SwiftPM
- **Fit:** Complex feature state, structured side effects and deterministic reducer tests at sufficient scale.
- **Anti-fit:** Simple views already fit State, Binding and Observation.
- **Fallback:** Native Observation, environment and feature-owned models.
- **Compatibility:** Tag 1.26.2: Swift tools 6.4 and Swift 6 language mode; iOS 16+, macOS 13+, tvOS 16+, watchOS 9+; visionOS not explicitly in manifest. SwiftUI integration documented.
- **Maintenance:** Release 1.26.2 on 2026-08-28; upstream pushed 2026-11-05. Numerous macro and SwiftPM dependencies.
- **License:** MIT
- **Official source:** [upstream](https://github.com/pointfreeco/swift-composable-architecture); [tag manifest](https://github.com/pointfreeco/swift-composable-architecture/blob/1.26.2/Package.swift); [tag license](https://github.com/pointfreeco/swift-composable-architecture/blob/1.26.2/LICENSE)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-16
- **Unknowns:** Compiler/toolchain macro support, strict concurrency, MainActor isolation, reducer cancellation, transitive swift-syntax constraints and target build not tested. Advisory and overhead measurements pending.
- **Selection:** EVALUATE

### `kean/Nuke`
- **Package:** `kean/Nuke`
- **Capability:** C12 — Media & Files
- **Tags:** `SwiftUI`, `NukeUI`, `remote-images`
- **Language/runtime:** Swift / SwiftPM
- **Fit:** NukeUI loading, processing, caching and prefetching for media-heavy feeds with measurable need.
- **Anti-fit:** A few remote images work with AsyncImage.
- **Fallback:** AsyncImage, URLSession and URLCache.
- **Compatibility:** Tag 13.2.3: Swift tools 6.0; iOS 15+, macOS 12+, tvOS 15+, watchOS 8+, visionOS 1+; NukeUI product. Upstream Nuke 13 guidance specifies Swift 6.2 / Xcode 26.
- **Maintenance:** Release 13.2.3 on 2026-11-08; upstream pushed 2026-11-09.
- **License:** MIT
- **Official source:** [upstream](https://github.com/kean/Nuke); [tag manifest](https://github.com/kean/Nuke/blob/13.2.3/Package.swift); [tag license](https://github.com/kean/Nuke/blob/13.2.3/LICENSE)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-16
- **Unknowns:** Actor isolation, cancellation during cell reuse, cache size, image privacy, accessibility, exact Xcode build and device performance not tested; advisory exposure pending.
- **Selection:** EVALUATE

### `airbnb/lottie-ios`
- **Package:** `airbnb/lottie-ios`
- **Capability:** C02 — Animation & Visualization
- **Tags:** `SwiftUI`, `Lottie`, `vector-animation`
- **Language/runtime:** Swift / SwiftPM
- **Fit:** Designer-supplied Bodymovin animations not economical to reproduce in native code.
- **Anti-fit:** Simple transitions and normal charts need only SwiftUI/Swift Charts.
- **Fallback:** SwiftUI animations, Canvas or static accessible artwork.
- **Compatibility:** Tag 4.6.1: Swift tools 6.0, target language mode Swift 5; iOS 13+, macOS 10.15+, tvOS 13+, visionOS 1+; watchOS not declared. SwiftUI integration documented.
- **Maintenance:** Release 4.6.1 on 2026-06-13; upstream pushed 2026-10-06. Source distribution differs from lottie-spm prebuilt binary distribution.
- **License:** Apache-2.0
- **Official source:** [upstream](https://github.com/airbnb/lottie-ios); [tag manifest](https://github.com/airbnb/lottie-ios/blob/4.6.1/Package.swift); [tag license](https://github.com/airbnb/lottie-ios/blob/4.6.1/LICENSE)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-16
- **Unknowns:** Animation asset rights, reduced-motion alternatives, VoiceOver, MainActor, binary provenance, size and real-device animation cost not tested; security advisory exposure pending.
- **Selection:** EVALUATE

### `pointfreeco/swift-snapshot-testing`
- **Package:** `pointfreeco/swift-snapshot-testing`
- **Capability:** C17 — Testing & QA
- **Tags:** `SwiftUI`, `test-target`, `snapshots`
- **Language/runtime:** Swift / SwiftPM
- **Fit:** Deterministic image/model regression snapshots with controlled environment and reviewed baselines.
- **Anti-fit:** Simple assertions suffice or screenshots would be flaky/unreviewed.
- **Fallback:** Swift Testing, XCTest, XCUITest and accessibility/device tests.
- **Compatibility:** Tag 1.19.7: Swift tools 6.0, Swift 5 language mode; iOS 13+, macOS 10.15+, tvOS 13+, watchOS 6+; visionOS not declared. Test targets only.
- **Maintenance:** Release 1.19.7 on 2026-10-21; upstream pushed 2026-10-21; swift-custom-dump and swift-syntax dependencies.
- **License:** MIT
- **Official source:** [upstream](https://github.com/pointfreeco/swift-snapshot-testing); [tag manifest](https://github.com/pointfreeco/swift-snapshot-testing/blob/1.19.7/Package.swift); [tag license](https://github.com/pointfreeco/swift-snapshot-testing/blob/1.19.7/LICENSE)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-16
- **Unknowns:** Cross-OS/font/dynamic-type snapshot parity, physical device, Swift 6 test isolation, CI consistency and accessibility are unverified; advisory and runtime costs pending.
- **Selection:** EVALUATE

### `realm/SwiftLint`
- **Package:** `realm/SwiftLint`
- **Capability:** C19 — Developer Tooling
- **Tags:** `lint`, `SwiftPM-plugin`, `host-tool`
- **Language/runtime:** Swift / SwiftPM (developer host tool)
- **Fit:** Automated enforceable Swift lint policy on source changes and CI.
- **Anti-fit:** Compiler warnings and current code review already satisfy quality needs.
- **Fallback:** Xcode and compiler diagnostics.
- **Compatibility:** Tag 0.65.1: Swift tools 5.9; manifest macOS 13+ applies to tooling host, not iOS app runtime; executable and SwiftPM plugins. Tagged manifest pins prerelease swift-syntax.
- **Maintenance:** Release 0.65.1 on 2026-08-21; upstream pushed 2026-11-13; multiple compiler-tool dependencies.
- **License:** MIT
- **Official source:** [upstream](https://github.com/realm/SwiftLint); [tag manifest](https://github.com/realm/SwiftLint/blob/0.65.1/Package.swift); [tag license](https://github.com/realm/SwiftLint/blob/0.65.1/LICENSE)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-16
- **Unknowns:** Swift 6 rule compatibility, exact Xcode/SwiftSyntax builds, plugin sandbox and CI integration not tested; advisories and run-time cost pending.
- **Selection:** EVALUATE

### `nicklockwood/SwiftFormat`
- **Package:** `nicklockwood/SwiftFormat`
- **Capability:** C19 — Developer Tooling
- **Tags:** `formatter`, `SwiftPM-plugin`, `host-tool`
- **Language/runtime:** Swift / SwiftPM (developer host tool)
- **Fit:** Consistent auto-formatting when shared source style is actually enforced.
- **Anti-fit:** No format drift or existing formatter is already authoritative.
- **Fallback:** Xcode formatting or existing formatter, including swiftlang/swift-format.
- **Compatibility:** Tag 0.64.7: Swift tools 5.7; executable and SwiftPM command plugin. No platform minimum in manifest; tool is not an iOS app runtime dependency.
- **Maintenance:** Release 0.64.7 on 2026-11-14; upstream pushed 2026-11-16; plugin needs write permission for package source files.
- **License:** MIT
- **Official source:** [upstream](https://github.com/nicklockwood/SwiftFormat); [tag manifest](https://github.com/nicklockwood/SwiftFormat/blob/0.64.7/Package.swift); [tag license](https://github.com/nicklockwood/SwiftFormat/blob/0.64.7/LICENSE.md)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-16
- **Unknowns:** Swift 6 syntax handling, exact host/CI compiler and destructive rewrite review not tested; advisory and operational costs pending.
- **Selection:** EVALUATE

### `RevenueCat/purchases-ios`
- **Package:** `RevenueCat/purchases-ios`
- **Capability:** C20 — AI & Integrations
- **Tags:** `StoreKit`, `subscriptions`, `SwiftUI`, `vendor-integration`
- **Language/runtime:** Swift / SwiftPM
- **Fit:** Managed subscription entitlements, paywalls and cross-platform purchase state when that vendor service is justified.
- **Anti-fit:** No IAP, or simple Apple-only subscriptions work using StoreKit 2; SDK is not identity/auth.
- **Fallback:** StoreKit 2 and StoreKit views with app-owned transaction logic.
- **Compatibility:** Tag 5.103.0: Swift tools 5.9; iOS 13+, macOS 10.15+, tvOS 13+, watchOS 6.2+, visionOS 1+; SwiftPM RevenueCat and RevenueCatUI products.
- **Maintenance:** Release 5.103.0 on 2026-11-11; upstream pushed 2026-11-16; manifest includes additional test-only dependencies.
- **License:** MIT
- **Official source:** [upstream](https://github.com/RevenueCat/purchases-ios); [tag manifest](https://github.com/RevenueCat/purchases-ios/blob/5.103.0/Package.swift); [tag license](https://github.com/RevenueCat/purchases-ios/blob/5.103.0/LICENSE)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-16
- **Unknowns:** Vendor pricing, privacy, entitlement consistency, offline operation, StoreKit/App Store policy, Swift 6 strict concurrency and vendor exit unverified. No pricing/production approval; advisory and TCO work pending.
- **Selection:** EVALUATE

### `vapor/fluent`
- **Package:** `vapor/fluent`
- **Capability:** C08 — Persistence
- **Language/runtime:** Swift / SwiftPM (Server-side Swift)
- **Fit:** Typed Fluent ORM models, queries and migrations for services that need an ORM.
- **Anti-fit:** No database; direct SQL is smaller or better suited.
- **Fallback:** Vapor without ORM or selected SQL client.
- **Compatibility:** Tag 4.13.0: Swift tools 6.0; macOS 10.15+/iOS 13+ declared; tagged dependencies vapor/vapor 4.117.0+ and fluent-kit 1.52.2+; Linux build not performed.
- **Maintenance:** Release 2025-09-25; upstream pushed 2026-08-25. No support SLA inferred.
- **License:** MIT ([tagged license](https://github.com/vapor/fluent/blob/4.13.0/LICENSE)).
- **Official source:** [upstream](https://github.com/vapor/fluent); [tagged manifest](https://github.com/vapor/fluent/blob/4.13.0/Package.swift)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-17
- **Unknowns:** Swift 6 isolation, Linux runtime, ORM migration rollback, database pooling, security advisories and TCO NOT_VERIFIED.
- **Selection:** EVALUATE

### `vapor/fluent-postgres-driver`
- **Package:** `vapor/fluent-postgres-driver`
- **Capability:** C08 — Persistence
- **Language/runtime:** Swift / SwiftPM (Server-side Swift)
- **Fit:** PostgreSQL driver for chosen Fluent ORM and actual PostgreSQL deployment.
- **Anti-fit:** No PostgreSQL; prefer one DB driver, or direct PostgresNIO when appropriate.
- **Fallback:** Direct SQL/PostgresNIO or the already selected DB driver.
- **Compatibility:** Tag 2.14.1: Swift tools 6.2; macOS 10.15+/iOS 13+ declared; fluent-kit 1.52.2+, postgres-kit 2.17.0+, postgres-nio 1.33.1+ and service-lifecycle 2.12.0+ dependencies.
- **Maintenance:** Release 2026-11-10; pushed 2026-11-10. No support SLA inferred.
- **License:** MIT ([tagged license](https://github.com/vapor/fluent-postgres-driver/blob/2.14.1/LICENSE)).
- **Official source:** [upstream](https://github.com/vapor/fluent-postgres-driver); [tagged manifest](https://github.com/vapor/fluent-postgres-driver/blob/2.14.1/Package.swift)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-17
- **Unknowns:** Vapor/Fluent graph co-resolution, Swift 6/Linux binary, pooling, TLS, transaction/cancellation and advisories NOT_VERIFIED.
- **Selection:** EVALUATE

### `vapor/jwt`
- **Package:** `vapor/jwt`
- **Capability:** C10 — Identity & Authorization
- **Language/runtime:** Swift / SwiftPM (Server-side Swift)
- **Fit:** Vapor JWT integration for a justified bearer-token or identity-token model.
- **Anti-fit:** Vapor sessions suffice, or JWT verification is being confused with authorization.
- **Fallback:** Vapor authenticators/sessions and server-side authorization.
- **Compatibility:** Tag 5.2.0: Swift tools 6.2; macOS 13+/iOS 16+ declared; vapor/vapor 4.110.2+ and jwt-kit 5.8.0+. Vapor 4 integration declared, Linux untested.
- **Maintenance:** Security release 2026-10-28; underlying jwt-kit 5.9.0 released 2026-11-10. No support SLA inferred.
- **License:** MIT ([tagged license](https://github.com/vapor/jwt/blob/5.2.0/LICENSE)).
- **Official source:** [upstream](https://github.com/vapor/jwt); [tagged manifest](https://github.com/vapor/jwt/blob/5.2.0/Package.swift)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-17
- **Unknowns:** GHSA-gxx9-vxm7-hgrq, GHSA-hfm2-66rr-3mcf, GHSA-jhmq-wqhf-47x2 and GHSA-pfgx-7g34-46fm are material. Verify expected audience, issuer, keys, token lifecycle, ownership and security advisories on the pinned graph; not production-cleared.
- **Selection:** EVALUATE

### `vapor/queues-redis-driver`
- **Package:** `vapor/queues-redis-driver`
- **Capability:** C13 — Async & Messaging
- **Language/runtime:** Swift / SwiftPM (Server-side Swift)
- **Fit:** Redis-backed delayed/durable jobs and workers for demonstrated async delivery needs.
- **Anti-fit:** Request-scoped tasks suffice or Redis/worker operations unjustified.
- **Fallback:** Swift structured concurrency for non-durable tasks, or an existing managed queue.
- **Compatibility:** Tag 1.1.2: Swift tools 5.8; macOS 10.15+/iOS 13+ declared; vapor/vapor 4.76.3+, queues 1.12.1+, redis 4.8.0+. Current Queues 1.18.0, Redis 4.14.0 and Swift 6 strict-concurrency compatibility unresolved.
- **Maintenance:** Last stable release 2024-09-19; repository pushed 2026-07-17; maintenance does not prove compatibility. No support SLA inferred.
- **License:** MIT ([tagged license](https://github.com/vapor/queues-redis-driver/blob/1.1.2/LICENSE)).
- **Official source:** [upstream](https://github.com/vapor/queues-redis-driver); [tagged manifest](https://github.com/vapor/queues-redis-driver/blob/1.1.2/Package.swift)
- **Evidence status:** PARTIAL
- **Evidence reviewed:** 2026-11-17
- **Unknowns:** BLOCKED until current Swift 6/Linux graph, worker/retry integration, Redis recovery, idempotency and advisories tested. No exactly-once guarantee.
- **Selection:** BLOCKED

### `vapor/redis`
- **Package:** `vapor/redis`
- **Capability:** C16 — Performance & Cache
- **Language/runtime:** Swift / SwiftPM (Server-side Swift)
- **Fit:** Vapor Redis integration for proven distributed cache, sessions or coordination.
- **Anti-fit:** Small single-instance cache works; Redis adds a needless network and outage dependency.
- **Fallback:** Bounded application memory/cache or already approved cache.
- **Compatibility:** Tag 4.14.0: Swift tools 5.10; macOS 10.15+/iOS 13+ declared; vapor/vapor 4.100.0+, swift-server/RediStack 1.4.1+.
- **Maintenance:** Release 2025-09-12; repository pushed 2026-07-17. No support SLA inferred.
- **License:** MIT ([tagged license](https://github.com/vapor/redis/blob/4.14.0/LICENSE)).
- **Official source:** [upstream](https://github.com/vapor/redis); [tagged manifest](https://github.com/vapor/redis/blob/4.14.0/Package.swift)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-17
- **Unknowns:** Redis TLS/auth, pooling, TTL, invalidation, failure recovery, Swift 6/Linux binary and advisory/TCO checks NOT_VERIFIED.
- **Selection:** EVALUATE

### `swift-server/async-http-client`
- **Package:** `swift-server/async-http-client`
- **Capability:** C06 — Remote Data & Sync
- **Language/runtime:** Swift / SwiftPM (Server-side Swift)
- **Fit:** Advanced outbound HTTP, pooling, streaming and deadlines when Vapor Client is insufficient.
- **Anti-fit:** Vapor Client already covers the workload; duplicate HTTP client lifecycle is harmful.
- **Fallback:** Vapor's native Client using transitive AsyncHTTPClient.
- **Compatibility:** Tag 1.37.0: Swift tools 6.2; swift-nio 2.100.0+, swift-nio-ssl 2.30.0+, NIO HTTP/2; Vapor 4.122.3 already depends on this package from 1.24.0; exact co-resolution untested.
- **Maintenance:** Release 2026-11-02; pushed 2026-11-16. No support SLA inferred.
- **License:** Apache-2.0 ([tagged license](https://github.com/swift-server/async-http-client/blob/1.37.0/LICENSE.txt)).
- **Official source:** [upstream](https://github.com/swift-server/async-http-client); [tagged manifest](https://github.com/swift-server/async-http-client/blob/1.37.0/Package.swift)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-17
- **Unknowns:** TLS, SSRF/redirects, DNS, connection limits, backpressure, blocking EventLoops, cancellation, Linux SwiftPM graph and advisories NOT_VERIFIED.
- **Selection:** EVALUATE

### `vapor/swift-openapi-vapor`
- **Package:** `vapor/swift-openapi-vapor`
- **Capability:** C07 — Data Contracts
- **Language/runtime:** Swift / SwiftPM (Server-side Swift)
- **Fit:** Generate and register Vapor server handlers from a maintained OpenAPI contract.
- **Anti-fit:** Hand-written routes and Codable suffice; unnecessary generator/transport drift.
- **Fallback:** Vapor Content/Codable; existing apple/swift-openapi-generator only if needed.
- **Compatibility:** Tag 1.2.0: Swift tools 6.1 with StrictConcurrency=complete setting; macOS 10.15+/iOS 13+ declared; vapor/vapor 4.106.7+, swift-openapi-runtime 1.11.0+, atomics and NIO extras. Linux unbuilt.
- **Maintenance:** Stable 1.2.0 released 2026-09-02; 2.0 beta released 2026-10-15, not used for this comparison. No support SLA inferred.
- **License:** Apache-2.0 ([tagged license](https://github.com/vapor/swift-openapi-vapor/blob/1.2.0/LICENSE.txt)).
- **Official source:** [upstream](https://github.com/vapor/swift-openapi-vapor); [tagged manifest](https://github.com/vapor/swift-openapi-vapor/blob/1.2.0/Package.swift)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-17
- **Unknowns:** Generator/runtime and transport version alignment, API schema coverage, request isolation, streaming, Swift 6 build, Linux and CI NOT_VERIFIED.
- **Selection:** EVALUATE

### `swift-otel/swift-otel`
- **Package:** `swift-otel/swift-otel`
- **Capability:** C18 — Observability
- **Language/runtime:** Swift / SwiftPM (Server-side Swift)
- **Fit:** OTLP telemetry exporter when tracing/metrics/logging needs collectors and operational dashboards.
- **Anti-fit:** SwiftLog/Metrics/Tracing APIs alone suffice; no exporter or collector.
- **Fallback:** Already available Vapor SwiftLog/Metrics/Distributed Tracing.
- **Compatibility:** Tag 1.6.0: Swift tools 6.2; OTel product and optional OTLPHTTP/OTLPGRPC traits; swift-distributed-tracing 1.7.2+, swift-metrics 2.4.1+ and service-lifecycle 2.4.1+. Transport traits have distinct dependency costs.
- **Maintenance:** Release 2026-10-16; pushed 2026-11-06. No support SLA inferred.
- **License:** Apache-2.0 ([tagged license](https://github.com/swift-otel/swift-otel/blob/1.6.0/LICENSE.txt)).
- **Official source:** [upstream](https://github.com/swift-otel/swift-otel); [tagged manifest](https://github.com/swift-otel/swift-otel/blob/1.6.0/Package.swift)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-17
- **Unknowns:** Trace/metric propagation, collector integration, private data redaction, sampling, backpressure, Swift 6/Linux execution, advisories and operational cost NOT_VERIFIED.
- **Selection:** EVALUATE

## Selection boundary

VERIFIED is scoped to official package identity, metadata and advertised function; it is NOT a security endorsement, benchmark result or production approval. PARTIAL means essential metadata is unresolved. EVALUATE permits comparison only, BLOCKED requires filling compatibility/license gaps first. No automatic migration.

[Index](README.md) · [Languages](../languages/README.md) · [Frameworks](../frameworks/README.md) · [Decisions](../decisions/README.md)
