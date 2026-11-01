# SwiftUI — Swift / Apple UI

**Reviewed:** 2026-11-01 · [Framework index](README.md)

## Fit
Native iOS, macOS and other supported Apple platform apps needing declarative UI, device APIs, accessibility and integration with system frameworks.

## Anti-fit
Linux server API, browser frontend or a platform without Apple UI SDKs; do not use SwiftUI as evidence Swift server is Apple-only.

## Compatibility
Requires appropriate Apple platform SDK/Xcode and a compatible minimum deployment OS for specific APIs. UIKit/AppKit interop may be necessary. Simulator cannot prove device hardware behavior; signing, entitlements and distribution differ from pure Swift packages.

## Maturity & maintenance
Apple-maintained API and documentation; backwards compatibility, OS availability, SDK lifecycle and app review conditions **must be checked per target release**. No claim of independent cross-platform UI.

## Licensing
Apple platform SDK distribution/developer agreement governs SwiftUI development and app release; **not classified as MIT/Apache OSS**. Verify program/enrollment and distribution rules at decision time.

## Operational / test evidence needed
OS/device matrix, offline state/sync, accessibility, navigation and concurrency, UI tests on simulator and physical devices, crash reports, keychain/permissions, signing/release rollback and store terms.

## Official evidence
- [SwiftUI official product page](https://developer.apple.com/swiftui/)
- [SwiftUI documentation](https://developer.apple.com/documentation/swiftui)
- [Apple developer agreements](https://developer.apple.com/support/terms/)
