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
- **Official source:** [official registry or upstream](https://pypi.org/project/pydantic/); [upstream/manifest](https://github.com/pydantic/pydantic)
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
- **Capability:** Retry / resilience
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
- **Capability:** Numerical / data processing
- **Language/runtime:** Python / PyPI
- **Fit:** Dense arrays and numerical operations, when the current codebase demonstrably needs it.
- **Anti-fit:** Small scalar, iterator or streaming workload does not benefit from dense arrays.
- **Fallback:** Python lists/array, streaming iteration or the existing numerical stack.
- **Compatibility:** Python >=3.12; check deployment platform and integrations.
- **Maintenance:** PyPI latest 2.5.4; uploaded 2026-10-10; activity does not prove long-term support.
- **License:** BSD-3-Clause AND 0BSD AND MIT AND Zlib AND CC0-1.0
- **Official source:** [official registry or upstream](https://pypi.org/project/numpy/); [upstream/manifest](https://github.com/numpy/numpy)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-01
- **Unknowns:** Current Requires-Python is >=3.12; validate native wheels and CPU target. Security advisories: UNKNOWN; exact target support, comparative benchmarks and operational burden: NOT_MEASURED. Recheck before project selection.
- **Selection:** EVALUATE

### `mcp`
- **Package:** `mcp`
- **Capability:** Agentic / MCP
- **Language/runtime:** Python / PyPI
- **Fit:** Official MCP Python client/server SDK for tools, resources and prompts over stdio, Streamable HTTP and legacy SSE.
- **Anti-fit:** A conventional HTTP/model client with no MCP interoperability requirement.
- **Fallback:** httpx or the established HTTP/model SDK.
- **Compatibility:** PyPI `mcp` and pinned `mcp-types` 2.3.0 declare Python >=3.10, while the v2 installation guide states Python 3.11+ is required. Target Python 3.11+ until the documentation/metadata discrepancy is reconciled.
- **Maintenance:** PyPI latest 2.3.0; uploaded 2026-10-02; v2 stable release line documented.
- **License:** MIT
- **Official source:** [official registry or upstream](https://pypi.org/project/mcp/); [upstream/manifest](https://github.com/modelcontextprotocol/python-sdk)
- **Evidence status:** PARTIAL
- **Evidence reviewed:** 2026-11-02
- **Unknowns:** Published 2.3.0 metadata and v2 installation guide disagree on minimum Python version; Python 3.10 support remains unconfirmed for project selection. Exact MCP revision/transport negotiation requires target testing. Untrusted tool outputs, credentials, SSRF, authorization, cancellation and request limits are application responsibilities. Security advisory applicability: UNKNOWN (no pinned-version OSV/GHSA review); target-specific integration, performance and TCO: NOT_MEASURED. Recheck official metadata and transitive dependencies before project adoption.
- **Selection:** BLOCKED

### `celery`
- **Package:** `celery`
- **Capability:** Durable jobs
- **Language/runtime:** Python / PyPI
- **Fit:** Broker-backed distributed task queue when tasks must survive process exit and workers scale independently.
- **Anti-fit:** Short best-effort work or no broker/operations capacity.
- **Fallback:** Explicit bounded task execution or existing managed queue.
- **Compatibility:** Python >=3.9 per PyPI 5.6.3; broker/result backend and worker deployment must match workload.
- **Maintenance:** PyPI latest 5.6.3; uploaded 2026-03-26; check broker-specific lifecycle.
- **License:** BSD-3-Clause
- **Official source:** [official registry or upstream](https://pypi.org/project/celery/); [upstream/manifest](https://github.com/celery/celery)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-02
- **Unknowns:** At-least-once redelivery possible; retries require idempotency and broker acknowledgements. No exactly-once guarantee. Security advisory applicability: UNKNOWN (no pinned-version OSV/GHSA review); target-specific integration, performance and TCO: NOT_MEASURED. Recheck official metadata and transitive dependencies before project adoption.
- **Selection:** EVALUATE

### `psycopg`
- **Package:** `psycopg`
- **Capability:** PostgreSQL driver
- **Language/runtime:** Python / PyPI
- **Fit:** PostgreSQL protocol access and optional pooling where direct SQL/driver control is preferred.
- **Anti-fit:** No PostgreSQL, or an existing SQLAlchemy/driver stack already suffices.
- **Fallback:** sqlite3 for SQLite or existing DB driver.
- **Compatibility:** Python >=3.10 per PyPI 3.3.6; libpq/binary distribution, OS/CPU wheels and pool extra require review.
- **Maintenance:** PyPI latest 3.3.6; uploaded 2026-09-18; inspect chosen distribution variant.
- **License:** LGPL-3.0-only (psycopg core); inspect distribution and bundling duties.
- **Official source:** [official registry or upstream](https://pypi.org/project/psycopg/); [upstream/manifest](https://github.com/psycopg/psycopg)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-02
- **Unknowns:** Native/libpq packaging, license compliance for redistribution and pooling limits must be checked per deployment. Security advisory applicability: UNKNOWN (no pinned-version OSV/GHSA review); target-specific integration, performance and TCO: NOT_MEASURED. Recheck official metadata and transitive dependencies before project adoption.
- **Selection:** EVALUATE

### `polars`
- **Package:** `polars`
- **Capability:** Data processing
- **Language/runtime:** Python / PyPI
- **Fit:** Columnar DataFrames and lazy analytical queries for sizeable batch/data transformations.
- **Anti-fit:** Small iterators/scalars, SQL-only analytics or existing NumPy pipeline suffice.
- **Fallback:** Python iterators, SQL or existing numerical stack.
- **Compatibility:** Python >=3.11 per PyPI 2.1.0; native wheels/CPU architecture and memory constraints need target checks.
- **Maintenance:** PyPI latest 2.1.0; uploaded 2026-10-25; native engine version-specific.
- **License:** MIT (PyPI 2.1.0 distribution metadata license text).
- **Official source:** [official registry or upstream](https://pypi.org/project/polars/); [upstream/manifest](https://github.com/pola-rs/polars)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-02
- **Unknowns:** No universal speedup claim; evaluate dataset size, memory, ARM64/Linux wheel support and pandas interoperability. Security advisory applicability: UNKNOWN (no pinned-version OSV/GHSA review); target-specific integration, performance and TCO: NOT_MEASURED. Recheck official metadata and transitive dependencies before project adoption.
- **Selection:** EVALUATE

### `transformers`
- **Package:** `transformers`
- **Capability:** Model integration
- **Language/runtime:** Python / PyPI
- **Fit:** Python-native loading/running of pretrained models when local inference or training workflows demand it.
- **Anti-fit:** Only hosted API calls or an existing model runtime handles inference.
- **Fallback:** Existing hosted-model SDK, HTTP client or model runtime.
- **Compatibility:** Python >=3.11.0 per PyPI 5.22.1; backend ML framework, GPU drivers/VRAM and model format depend on deployment.
- **Maintenance:** PyPI latest 5.22.1; uploaded 2026-10-30; release alone does not validate target model.
- **License:** Apache-2.0 (library only; model weights/datasets separate).
- **Official source:** [official registry or upstream](https://pypi.org/project/transformers/); [upstream/manifest](https://github.com/huggingface/transformers)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-02
- **Unknowns:** Check model-specific license/weights, trust_remote_code and remote artifact provenance; CPU/GPU latency/VRAM NOT_MEASURED. Security advisory applicability: UNKNOWN (no pinned-version OSV/GHSA review); target-specific integration, performance and TCO: NOT_MEASURED. Recheck official metadata and transitive dependencies before project adoption.
- **Selection:** EVALUATE

### `opentelemetry-sdk`
- **Package:** `opentelemetry-sdk`
- **Capability:** Telemetry SDK
- **Language/runtime:** Python / PyPI
- **Fit:** Generate/process Python spans and metrics for distributed observability, with separately configured exporters.
- **Anti-fit:** Simple standard logging is sufficient or existing telemetry system already instrumented.
- **Fallback:** logging/structlog or existing instrumentation.
- **Compatibility:** Python >=3.10 per PyPI 1.45.2; align OTel API, instrumentation and exporter versions.
- **Maintenance:** PyPI latest 1.45.2; uploaded 2026-10-29; version synchronization required.
- **License:** Apache-2.0
- **Official source:** [official registry or upstream](https://pypi.org/project/opentelemetry-sdk/); [upstream/manifest](https://github.com/open-telemetry/opentelemetry-python)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-02
- **Unknowns:** SDK is not an exporter/collector; configure sampling, redaction, propagation and exporting separately. Security advisory applicability: UNKNOWN (no pinned-version OSV/GHSA review); target-specific integration, performance and TCO: NOT_MEASURED. Recheck official metadata and transitive dependencies before project adoption.
- **Selection:** EVALUATE

## Selection boundary

VERIFIED is scoped to official package identity, metadata and advertised function; it is NOT a security endorsement, benchmark result or production approval. PARTIAL means essential metadata is unresolved. EVALUATE permits comparison only, BLOCKED requires filling compatibility/license gaps first. No automatic migration.

[Index](README.md) · [Languages](../languages/README.md) · [Frameworks](../frameworks/README.md) · [Decisions](../decisions/README.md)
