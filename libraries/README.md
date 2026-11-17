# Libraries — curated reusable packages

**Reviewed:** 2026-11-17. Package discovery (Awesome lists, TopGit, lib.rs) is not quality authority; records were reviewed through official registries or upstream repositories. The catalog never substitutes for project-specific acceptance.

| Language | Entries | Scope | Link |
|---|---:|---|---|
| Rust | 20 | Axum/Tower HTTP, contracts, DB, crypto, cache, testing, tracing and AI | [Rust](rust.md) |
| Go | 22 | Gin HTTP/auth, SQL, cache, resilience, QA, tracing, CLI and AI | [Go](go.md) |
| TypeScript | 30 | React UI, state, data, security, runtime and testing | [TypeScript](typescript.md) |
| Python | 26 | FastAPI ASGI, forms, contracts, SQL migrations, auth, cache, QA, tracing, tooling and AI | [Python](python.md) |
| Swift | 27 | SwiftUI-native and Vapor-server integration, DB, HTTP, security, cache, tracing and tooling | [Swift](swift.md) |

## Canonical primary capabilities

Every package has **exactly one primary capability** in its existing `Capability` field, formatted `Cxx — Name` from this table. Classify by primary engineering purpose, not popularity or every possible use. Optional `Tags` identify genuinely useful secondary functions; they never constitute another primary capability.

| ID | Primary capability |
|---|---|
| C01 | UI & Design System |
| C02 | Animation & Visualization |
| C03 | Forms & Navigation |
| C04 | Accessibility & i18n |
| C05 | State Management |
| C06 | Remote Data & Sync |
| C07 | Data Contracts |
| C08 | Persistence |
| C09 | API & Networking |
| C10 | Identity & Authorization |
| C11 | Search & Indexing |
| C12 | Media & Files |
| C13 | Async & Messaging |
| C14 | Resilience & Errors |
| C15 | Security & Cryptography |
| C16 | Performance & Cache |
| C17 | Testing & QA |
| C18 | Observability |
| C19 | Developer Tooling |
| C20 | AI & Integrations |

## Compatibility and selection semantics

- **Language vs framework vs runtime:** the language document indexes the package ecosystem. `Language/runtime` describes distribution/language, while `Compatibility` records sourced toolchain, runtime and platform restrictions. Neither proves framework-specific integration.
- **Framework applicability:** general-purpose packages remain framework-independent. Support for any framework is **NOT_VERIFIED** unless the individual package record explicitly cites official framework/integration evidence. An optional integration is not a mandatory dependency.
- **Six independent targets:** Next.js (TypeScript: Node/Edge, server/client bundle), SwiftUI (Swift: supported Apple OS and main-actor/concurrency), Axum (Rust: Tokio, async and Cargo feature flags), Gin (Go: `net/http` adapter/middleware), FastAPI (Python: ASGI, async/sync and workers), Vapor (Swift: server OS, SwiftNIO and concurrency). Each needs separate version, deployment and integration verification; a package does not inherit compatibility from a shared language.
- **Native-first:** evaluate standard-library/framework facilities and existing suitable dependencies before adding anything. Classifications are comparison filters, never installation requirements or recommendations.
- **Evidence gates:** retain official sources, dated reviews, licenses, `VERIFIED`/`PARTIAL` and `EVALUATE`/`BLOCKED`. `VERIFIED` authenticates only reviewed identity/metadata/advertised functions, **not** production suitability. Unknown advisory exposure, target platform support, performance, operations and costs remain unproven.
- **No coupling:** capability identifiers and optional tags create no build, runtime or shared dependency between frameworks.

## Discovery provenance (2026-11-02)

Discovery sampling targeted workload categories in [vinta/awesome-python](https://github.com/vinta/awesome-python), [avelino/awesome-go](https://github.com/avelino/awesome-go), [sindresorhus/awesome-nodejs](https://github.com/sindresorhus/awesome-nodejs), [enaqx/awesome-react](https://github.com/enaqx/awesome-react), [rust-unofficial/awesome-rust](https://github.com/rust-unofficial/awesome-rust), [matteocrippa/awesome-swift](https://github.com/matteocrippa/awesome-swift), and [sindresorhus/awesome](https://github.com/sindresorhus/awesome). These are **discovery references, not quality or maintenance proof**; none was exhaustively enumerated or pinned to an immutable commit in this review. The archived [dzharii/awesome-typescript](https://github.com/dzharii/awesome-typescript) is historical context only. Official registries/manifests, licenses and upstream SDK docs are the claim-level evidence in each canonical record. Popularity, stars and list membership never approve a dependency.

## Evidence and decision contract

- **VERIFIED:** official identity, metadata and advertised capability reviewed on the dated snapshot; never all aspects of production readiness.
- **PARTIAL:** one or more essential compatibility or license facts unresolved; do not recommend for a project until verified.
- **EVALUATE:** eligible for workload-specific comparison, not deployment approval.
- **BLOCKED:** unresolved metadata prohibits adoption recommendation.
- Always select standard library or an already-suitable dependency first. Never migrate on popularity or catalog appearance alone.
- Support policy, actual performance, vulnerabilities and operational costs are UNKNOWN until checked for the target project. A valid HTTPS link cannot prove truth.

## Scope ownership

[Languages](../languages/README.md) choose runtime; [Frameworks](../frameworks/README.md) choose framework; [Decisions](../decisions/README.md) own workload/stack approval; [Providers](../providers/README.md) own SaaS pricing and free tiers. Libraries cover reusable code only. ECC owns HOW.
