# Swift — curated libraries

**Reviewed:** 2026-11-17 (SwiftUI research); 12 existing package records preserve their individual earlier evidence dates. Reusable code packages only, never framework or managed service production approvals.

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
- **Evidence reviewed:** 2026-11-17
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
- **Evidence reviewed:** 2026-11-17
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
- **Evidence reviewed:** 2026-11-17
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
- **Evidence reviewed:** 2026-11-17
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
- **Evidence reviewed:** 2026-11-17
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
- **Evidence reviewed:** 2026-11-17
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
- **Evidence reviewed:** 2026-11-17
- **Unknowns:** Vendor pricing, privacy, entitlement consistency, offline operation, StoreKit/App Store policy, Swift 6 strict concurrency and vendor exit unverified. No pricing/production approval; advisory and TCO work pending.
- **Selection:** EVALUATE

## Selection boundary

VERIFIED is scoped to official package identity, metadata and advertised function; it is NOT a security endorsement, benchmark result or production approval. PARTIAL means essential metadata is unresolved. EVALUATE permits comparison only, BLOCKED requires filling compatibility/license gaps first. No automatic migration.

[Index](README.md) · [Languages](../languages/README.md) · [Frameworks](../frameworks/README.md) · [Decisions](../decisions/README.md)
