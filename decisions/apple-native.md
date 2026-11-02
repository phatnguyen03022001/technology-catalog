# DEC-APPLE-001 — Native iPhone/macOS app

**Status:** CONDITIONAL_NOT_PRODUCTION · **Reviewed:** 2026-11-02 · **Workload:** REFERENCE_SCENARIO_NOT_MEASURED.

## Workload & candidates
Assume app needs native Apple UI, device APIs, offline state and iOS/macOS deployment. Compare **SwiftUI**, existing UIKit/AppKit screens, and a browser/PWA where hardware integrations do not require native capabilities.

| Candidate | Evidence-backed fit | Costs/risks to verify |
|---|---|---|
| [SwiftUI](../frameworks/swiftui.md) | Apple declarative UI integrated with platform APIs | OS API availability, accessibility, state/data compatibility |
| UIKit/AppKit in existing project | Reuse established native components where SwiftUI gap exists | Integration and migration complexity |
| Web/PWA | Shared UI code and browser delivery when native device API is unnecessary | Offline, OS integration, Store/distribution constraints |

**Inference boundary (when ML is required):** [Core ML](https://developer.apple.com/documentation/coreml) is an Apple platform SDK for on-device inference: suitable when model conversion, OS/CPU/GPU/Neural Engine availability, memory/battery and offline/privacy requirements pass actual device tests. Hosted inference requires a backend API, network availability, server-owned credentials and data/privacy/usage-cost review. Hybrid may add fallback/quality but also two deployment/data paths; do not introduce it without workload evidence. This inference choice is independent of selecting SwiftUI for UI; compare on model quality, p95, power, offline support, privacy and TCO, all **NOT_MEASURED** here.

## Hard gates & unknown evidence
- Functional: **PASS conditional** for Apple-native UI; required device API/OS matrix **UNKNOWN** until test.
- Security/privacy: **UNKNOWN** — permissions, Keychain/storage and user-data lifecycle need tests.
- Legal/licensing: **UNKNOWN** for Apple developer enrollment/distribution and third-party dependencies.
- Cost/TCO: **UNKNOWN** — no device matrix, program terms, CI minutes, app usage; benchmark **NOT_MEASURED**.
- Portability/recovery: **UNKNOWN** until migration/export, rollback and minimum OS support verified.

## Decision & falsification
**Conditional choice: SwiftUI** for new Apple-native screens; preserve UIKit/AppKit interoperability for unsupported target APIs or existing implementation. Prefer PWA if native requirements evaporate and browser/offline tests pass. **Not production-approved**.

## Verification / TCO / fallback
Build target-specific Xcode app; run UI/accessibility tests on simulator **and** representative devices, test offline persistence, permissions, migration and crash recovery. If ML exists, test model compatibility/conversion, on-device resource consumption against hosted alternatives and offline behavior. Compute TCO from Apple enrollment/distribution terms, CI macOS runners, device QA, backend provider fees [providers](../providers/README.md), maintenance. Rollback via app version/release channel and reversible local migration; fallback to existing native UI if compatibility fails.

## Official evidence
- [Apple SwiftUI](https://developer.apple.com/swiftui/)
- [Apple SwiftUI documentation](https://developer.apple.com/documentation/swiftui)
- [Apple developer terms](https://developer.apple.com/support/terms/)
- [Apple Core ML](https://developer.apple.com/documentation/coreml)
