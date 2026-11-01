# Swift — curated libraries

**Reviewed:** 2026-11-01. Reusable code packages only, never framework or managed service production approvals.

## Dependency choice

- **Standard library first:** Foundation, Swift Concurrency, OSLog and CryptoKit.
- **Add:** only for a documented capability that standard library and current dependencies do not sufficiently provide.
- **Keep:** do not migrate merely because a package appears in the catalog or has a newer release.
- **Remove/replace:** prove need, test compatibility and preserve a rollback path.
- **Verify:** target toolchain, platform, license, security advisories, dependency tree and realistic workload.

## Entries

### `apple/swift-collections`
- **Package:** `apple/swift-collections`
- **Capability:** Data structures
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
- **Capability:** Data structures
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
- **Capability:** CLI
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
- **Capability:** Observability
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
- **Capability:** Crypto
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
- **Capability:** HTTP
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
- **Capability:** Async
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
- **Capability:** Database
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
- **Capability:** Systems
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

## Selection boundary

VERIFIED is scoped to official package identity, metadata and advertised function; it is NOT a security endorsement, benchmark result or production approval. PARTIAL means essential metadata is unresolved. EVALUATE permits comparison only, BLOCKED requires filling compatibility/license gaps first. No automatic migration.

[Index](README.md) · [Languages](../languages/README.md) · [Frameworks](../frameworks/README.md) · [Decisions](../decisions/README.md)
