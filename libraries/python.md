# Python — curated libraries

**Reviewed:** 2026-11-01. Reusable code packages only, never framework or managed service production approvals.

## Dependency choice

- **Standard library first:** dataclasses, urllib, asyncio, logging, unittest and sqlite3.
- **Add:** only for a documented capability that standard library and current dependencies do not sufficiently provide.
- **Keep:** do not migrate merely because a package appears in the catalog or has a newer release.
- **Remove/replace:** prove need, test compatibility and preserve a rollback path.
- **Verify:** target toolchain, platform, license, security advisories, dependency tree and realistic workload.

## Entries

### `pydantic`
- **Package:** `pydantic`
- **Capability:** Validation
- **Language/runtime:** Python / PyPI
- **Fit:** Validated typed input contracts, when the current codebase demonstrably needs it.
- **Anti-fit:** Internal dataclasses with no untrusted runtime parsing are sufficient.
- **Fallback:** dataclasses plus manual validation.
- **Compatibility:** Python >=3.10; check deployment platform and integrations.
- **Maintenance:** PyPI latest 2.14.2; uploaded 2026-10-29; activity does not prove long-term support.
- **License:** MIT
- **Official source:** [official registry or upstream](https://pypi.org/project/pydantic/); [upstream/manifest](https://github.com/sponsors/samuelcolvin)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-01
- **Unknowns:** Security advisories: UNKNOWN; exact target support, comparative benchmarks and operational burden: NOT_MEASURED. Recheck before project selection.
- **Selection:** EVALUATE

### `httpx`
- **Package:** `httpx`
- **Capability:** HTTP
- **Language/runtime:** Python / PyPI
- **Fit:** Sync/async pooled HTTP requests, when the current codebase demonstrably needs it.
- **Anti-fit:** A few synchronous requests are adequately handled by urllib.
- **Fallback:** urllib.request.
- **Compatibility:** Python >=3.8; check deployment platform and integrations.
- **Maintenance:** PyPI latest 0.28.1; uploaded 2024-12-06; activity does not prove long-term support.
- **License:** BSD-3-Clause
- **Official source:** [official registry or upstream](https://pypi.org/project/httpx/); [upstream/manifest](https://github.com/encode/httpx/blob/master/CHANGELOG.md)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-01
- **Unknowns:** PyPI latest upload dates to 2024-12; confirm maintenance/advisories before integration. Security advisories: UNKNOWN; exact target support, comparative benchmarks and operational burden: NOT_MEASURED. Recheck before project selection.
- **Selection:** EVALUATE

### `SQLAlchemy`
- **Package:** `SQLAlchemy`
- **Capability:** Database
- **Language/runtime:** Python / PyPI
- **Fit:** SQL expression and ORM access, when the current codebase demonstrably needs it.
- **Anti-fit:** Simple sqlite3 or a working existing driver is sufficient.
- **Fallback:** sqlite3 or current database driver.
- **Compatibility:** Python >=3.11; check deployment platform and integrations.
- **Maintenance:** PyPI latest 2.1.6; uploaded 2026-10-21; activity does not prove long-term support.
- **License:** MIT
- **Official source:** [official registry or upstream](https://pypi.org/project/SQLAlchemy/); [upstream/manifest](https://github.com/sqlalchemy/sqlalchemy/discussions)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-01
- **Unknowns:** Security advisories: UNKNOWN; exact target support, comparative benchmarks and operational burden: NOT_MEASURED. Recheck before project selection.
- **Selection:** EVALUATE

### `pytest`
- **Package:** `pytest`
- **Capability:** Testing
- **Language/runtime:** Python / PyPI
- **Fit:** Fixtures and parametrized tests, when the current codebase demonstrably needs it.
- **Anti-fit:** Current unittest suite already supports the needed assertions and fixtures.
- **Fallback:** unittest.
- **Compatibility:** Python >=3.10; check deployment platform and integrations.
- **Maintenance:** PyPI latest 9.2.0; uploaded 2026-10-27; activity does not prove long-term support.
- **License:** MIT
- **Official source:** [official registry or upstream](https://pypi.org/project/pytest/); [upstream/manifest](https://github.com/pytest-dev/pytest)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-01
- **Unknowns:** Security advisories: UNKNOWN; exact target support, comparative benchmarks and operational burden: NOT_MEASURED. Recheck before project selection.
- **Selection:** EVALUATE

### `structlog`
- **Package:** `structlog`
- **Capability:** Observability
- **Language/runtime:** Python / PyPI
- **Fit:** Structured event log pipelines, when the current codebase demonstrably needs it.
- **Anti-fit:** Standard logging meets output format and privacy requirements.
- **Fallback:** logging.
- **Compatibility:** Python >=3.10; check deployment platform and integrations.
- **Maintenance:** PyPI latest 26.1.0; uploaded 2026-06-06; activity does not prove long-term support.
- **License:** MIT OR Apache-2.0
- **Official source:** [official registry or upstream](https://pypi.org/project/structlog/); [upstream/manifest](https://github.com/hynek/structlog/blob/main/CHANGELOG.md)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-01
- **Unknowns:** Security advisories: UNKNOWN; exact target support, comparative benchmarks and operational burden: NOT_MEASURED. Recheck before project selection.
- **Selection:** EVALUATE

### `tenacity`
- **Package:** `tenacity`
- **Capability:** Async
- **Language/runtime:** Python / PyPI
- **Fit:** Bounded retry and backoff policies, when the current codebase demonstrably needs it.
- **Anti-fit:** Retries are unsafe for side effects, or a small explicit loop suffices.
- **Fallback:** small explicit bounded retry.
- **Compatibility:** Python >=3.10; check deployment platform and integrations.
- **Maintenance:** PyPI latest 9.2.1; uploaded 2026-10-07; activity does not prove long-term support.
- **License:** Apache-2.0
- **Official source:** [official registry or upstream](https://pypi.org/project/tenacity/); [upstream/manifest](https://github.com/jd/tenacity)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-01
- **Unknowns:** Retry decisions require explicit idempotency and deadline guarantees. Security advisories: UNKNOWN; exact target support, comparative benchmarks and operational burden: NOT_MEASURED. Recheck before project selection.
- **Selection:** EVALUATE

### `openai`
- **Package:** `openai`
- **Capability:** AI
- **Language/runtime:** Python / PyPI
- **Fit:** Typed OpenAI model client, when the current codebase demonstrably needs it.
- **Anti-fit:** Existing model client already covers required endpoints.
- **Fallback:** existing SDK or HTTP client.
- **Compatibility:** Python >=3.10; check deployment platform and integrations.
- **Maintenance:** PyPI latest 3.42.0; uploaded 2026-10-31; activity does not prove long-term support.
- **License:** Apache-2.0
- **Official source:** [official registry or upstream](https://pypi.org/project/openai/); [upstream/manifest](https://github.com/openai/openai-python)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-01
- **Unknowns:** Security advisories: UNKNOWN; exact target support, comparative benchmarks and operational burden: NOT_MEASURED. Recheck before project selection.
- **Selection:** EVALUATE

### `cryptography`
- **Package:** `cryptography`
- **Capability:** Crypto
- **Language/runtime:** Python / PyPI
- **Fit:** Cryptographic operations and key handling, when the current codebase demonstrably needs it.
- **Anti-fit:** Standard hashlib, hmac, ssl or secrets provide the necessary primitives.
- **Fallback:** hashlib, hmac, ssl, secrets.
- **Compatibility:** Python !=3.9.0,!=3.9.1,>=3.9; check deployment platform and integrations.
- **Maintenance:** PyPI latest 50.0.2; uploaded 2026-09-30; activity does not prove long-term support.
- **License:** Apache-2.0 OR BSD-3-Clause
- **Official source:** [official registry or upstream](https://pypi.org/project/cryptography/); [upstream/manifest](https://github.com/pyca/cryptography)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-01
- **Unknowns:** Security advisories: UNKNOWN; exact target support, comparative benchmarks and operational burden: NOT_MEASURED. Recheck before project selection.
- **Selection:** EVALUATE

### `typer`
- **Package:** `typer`
- **Capability:** CLI
- **Language/runtime:** Python / PyPI
- **Fit:** Typed multi-command CLI, when the current codebase demonstrably needs it.
- **Anti-fit:** One script with small argument set is clearer with argparse.
- **Fallback:** argparse.
- **Compatibility:** Python >=3.10; check deployment platform and integrations.
- **Maintenance:** PyPI latest 0.27.3; uploaded 2026-10-06; activity does not prove long-term support.
- **License:** MIT
- **Official source:** [official registry or upstream](https://pypi.org/project/typer/); [upstream/manifest](https://github.com/fastapi/typer)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-01
- **Unknowns:** Security advisories: UNKNOWN; exact target support, comparative benchmarks and operational burden: NOT_MEASURED. Recheck before project selection.
- **Selection:** EVALUATE

### `numpy`
- **Package:** `numpy`
- **Capability:** AI
- **Language/runtime:** Python / PyPI
- **Fit:** Dense arrays and numerical operations, when the current codebase demonstrably needs it.
- **Anti-fit:** Small scalar, iterator or streaming workload does not benefit from dense arrays.
- **Fallback:** existing SDK or HTTP client.
- **Compatibility:** Python >=3.12; check deployment platform and integrations.
- **Maintenance:** PyPI latest 2.5.4; uploaded 2026-10-10; activity does not prove long-term support.
- **License:** BSD-3-Clause AND 0BSD AND MIT AND Zlib AND CC0-1.0
- **Official source:** [official registry or upstream](https://pypi.org/project/numpy/); [upstream/manifest](https://github.com/numpy/numpy)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-01
- **Unknowns:** Current Requires-Python is >=3.12; validate native wheels and CPU target. Security advisories: UNKNOWN; exact target support, comparative benchmarks and operational burden: NOT_MEASURED. Recheck before project selection.
- **Selection:** EVALUATE

## Selection boundary

VERIFIED is scoped to official package identity, metadata and advertised function; it is NOT a security endorsement, benchmark result or production approval. PARTIAL means essential metadata is unresolved. EVALUATE permits comparison only, BLOCKED requires filling compatibility/license gaps first. No automatic migration.

[Index](README.md) · [Languages](../languages/README.md) · [Frameworks](../frameworks/README.md) · [Decisions](../decisions/README.md)
