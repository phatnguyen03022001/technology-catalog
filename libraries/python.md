# Python — curated libraries

**Reviewed:** 2026-11-17. Reusable code packages only, never framework or managed service production approvals.

## Dependency choice

- **Standard library first:** dataclasses, urllib, asyncio, logging, unittest and sqlite3.
- **Add:** only for a documented capability that standard library and current dependencies do not sufficiently provide.
- **Keep:** do not migrate merely because a package appears in the catalog or has a newer release.
- **Remove/replace:** prove need, test compatibility and preserve a rollback path.
- **Verify:** target toolchain, platform, license, security advisories, dependency tree and realistic workload.

## FastAPI / Python capability screening (2026-11-17)

Screened all 20 canonical capabilities. `ADDED` denotes an optional catalog record, never a mandatory install. General-purpose packages have no implied FastAPI integration certification.

| ID | Screening | Native-first / workload-specific outcome |
|---|---|---|
| C01 | NOT_APPLICABLE | API-only FastAPI has no UI/design system; serve typed contracts to clients. |
| C02 | CONDITIONAL | Return structured data first; server-side charts/images only when a specific output contract demands rendering. |
| C03 | ADDED | FastAPI routing/Form/File native; python-multipart is required only for receiving form/multipart bodies. Bound requests. |
| C04 | NATIVE_FIRST | Headers/locale negotiation and translated error DTOs only for supported languages; no mandatory translation stack. |
| C05 | NATIVE_FIRST | Depends scopes, lifespan, contextvars/asyncio and per-worker resources; never assume cross-worker shared memory. |
| C06 | EXISTING | urllib for simple sync needs, httpx for pooled async HTTP; close clients at lifespan shutdown, enforce deadlines/SSRF checks. |
| C07 | ADDED | Pydantic and FastAPI validation/OpenAPI existing; pydantic-settings only for multi-source validated configuration. |
| C08 | ADDED | sqlite3 or existing SQLAlchemy/psycopg; Alembic when versioned SQL schema migrations are owned. |
| C09 | ADDED | FastAPI/Starlette provide ASGI application; Uvicorn executes it; WebSockets/proxy/lifespan need deployment checks. |
| C10 | ADDED | FastAPI Security offers scheme extraction; Authlib only for OAuth/OIDC protocols; identity does not grant authorization. |
| C11 | NATIVE_FIRST | Database LIKE/full-text/vector extension via existing DB stack before separate search/index services. |
| C12 | CONDITIONAL | FastAPI UploadFile/StreamingResponse first; multipart parser only for forms; enforce upload limits, safe filenames and cleanup. |
| C13 | EXISTING | asyncio/AnyIO or existing Celery for durable broker-backed work; BackgroundTasks is NOT durable or cross-worker. |
| C14 | EXISTING | Timeouts/cancellation natively; existing tenacity for bounded idempotent retries; ingress rate limits when needed. |
| C15 | ADDED | secrets/hashlib/ssl and existing cryptography first; pwdlib[argon2] for application password hashing, not generic token auth. |
| C16 | ADDED | Bounded in-process state and profiling first; redis client only for justified shared Redis cache/state and its service costs. |
| C17 | ADDED | unittest/pytest + existing HTTPX; pytest-asyncio for coroutine tests; TestClient context or explicit ASGI lifespan required. |
| C18 | ADDED | logging/structlog and existing OTel SDK first; FastAPI instrumentation adds ASGI spans, not exporter/sampling policy. |
| C19 | ADDED | venv/pip/pyproject/unittest and existing typer first; Ruff if unified lint + format is wanted in CI. |
| C20 | EXISTING | Existing openai, transformers, numpy/polars and mcp VERIFIED/EVALUATE for tagged 2.3.0/Python >=3.10; choose only for real integration/inference demand. |

### Runtime, security and deployment gates

- **Contracts:** Pydantic/FastAPI validate boundary DTOs and expose OpenAPI, not internal domain invariants or a universal error schema. Separate DTOs from persistence/domain models when their contracts differ; handle response validation errors deliberately. Cap request bodies and multipart parts upstream and in application policy, validate content, quarantine unsafe uploads, clean temporary files and respect streaming cancellation.
- **Async and lifecycle:** `async def` does not make blocking DB/HTTP/file operations or CPU/GPU inference nonblocking. Use `def` for sync work dispatched to a bounded threadpool or isolate CPU/GPU work in an explicit worker/process. Own DB pools/HTTP clients in lifespan; test cancellation, clean shutdown, worker duplication and resource quotas. `BackgroundTasks` is process-local, best-effort and **NOT a durable queue**; existing Celery needs a broker and idempotent job contract.
- **Identity:** OAuth/OIDC authentication, JWT signature/issuer/audience/expiry checks, user/tenant ownership authorization and CSRF are separate obligations. Cookie sessions need Secure/HttpOnly/SameSite and CSRF threat modeling. CORS is not authorization. Validate allowed outbound destinations against SSRF, forwarded/proxy headers and trusted-host rules; redact sensitive telemetry.
- **Operations:** Bound HTTP timeouts, retries/rate limits, connection pools, upload memory, background work, migrations and cache failures. OpenTelemetry SDK alone does not configure exporters; ASGI instrumentation alone does not define sampling/privacy. Model loading can multiply memory per ASGI worker; benchmark platform wheels, CPU/GPU, inference latency and cost before selection.
- **Supply-chain/security:** `python-multipart` affected versions below 0.0.27 (part-header DoS; [GHSA](https://github.com/advisories/GHSA-pp6c-gr5w-3c5g)) and below 0.0.30 (querystring CPU DoS / parameter smuggling; [GHSA](https://github.com/advisories/GHSA-5rvq-cxj2-64vf), [GHSA](https://github.com/advisories/GHSA-6jv3-5f52-599m)) are patched in the cited versions; reviewed 0.0.34 is newer, **not** a full security clearance. Authlib advisories affect `<1.6.10` and `=1.7.0` ([open redirect](https://github.com/advisories/GHSA-w8p2-r796-3vmq); patches 1.6.10/1.7.1) and `<=1.6.8` ([OIDC token binding](https://github.com/advisories/GHSA-m344-f55w-2m6j); patch 1.6.9); reviewed 1.9.8 is newer. Scan pinned transitive graphs separately.
- **Official framework references:** [FastAPI features](https://fastapi.tiangolo.com/features/), [form parsing](https://fastapi.tiangolo.com/tutorial/request-forms/), [security and password hashes](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/), [background task caveat](https://fastapi.tiangolo.com/tutorial/background-tasks/), [deployment](https://fastapi.tiangolo.com/deployment/manually/), [Python stdlib](https://docs.python.org/3/library/), [PyPA guide](https://packaging.python.org/en/latest/).

### Evaluated but not added

- `gunicorn`: process manager only for a concrete worker/process policy; Uvicorn plus deployment orchestrator may suffice. `aiofiles`: existing UploadFile/threadpool or standard file APIs first. `orjson`: standard FastAPI/Pydantic JSON is sufficient until measured throughput wins offset native wheel cost.
- `pydantic-extra-types`, `email-validator`: add only if DTO fields actually require the specialized validation. `sqlmodel`: duplicates existing Pydantic + SQLAlchemy boundary for many services; avoid automatic ORM migration. `asyncpg`: existing psycopg/SQLAlchemy first, unless driver-level async behavior shows a specific benefit.
- `PyJWT`: appropriate narrower JWT-only alternative but not added alongside Authlib without a requirement; tokens do not provide authorization. `argon2-cffi`: use as `pwdlib[argon2]` provider when password hashing is needed rather than duplicate top-level selection. `fastapi-users`: imposes identity model/DB policy not justified across ordinary APIs.
- `cachetools`: built-in bounded caching or existing service state first. `limits`/`slowapi`: rate limiting needs a threat model and shared-state/ingress choice, not a default per-process limiter. `asgi-lifespan`: optional for async tests; Starlette TestClient context manages lifespan in simpler tests. `respx`: HTTPX MockTransport or existing test doubles first.
- `prometheus-fastapi-instrumentator`: metrics only when Prometheus scrape/export is configured; existing OTel path may already cover signals. Additional vector stores, model runtimes, agent frameworks and providers rejected without workload contracts.

## Entries

### `pydantic`
- **Package:** `pydantic`
- **Capability:** C07 — Data Contracts
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
- **Capability:** C09 — API & Networking
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
- **Capability:** C08 — Persistence
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
- **Capability:** C17 — Testing & QA
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
- **Capability:** C18 — Observability
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
- **Capability:** C14 — Resilience & Errors
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
- **Capability:** C20 — AI & Integrations
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
- **Capability:** C15 — Security & Cryptography
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
- **Capability:** C19 — Developer Tooling
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
- **Capability:** C16 — Performance & Cache
- **Tags:** `numerical-computing`
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
- **Capability:** C20 — AI & Integrations
- **Language/runtime:** Python / PyPI
- **Fit:** Official MCP Python client/server SDK for tools, resources and prompts over stdio, Streamable HTTP and legacy SSE.
- **Anti-fit:** A conventional HTTP/model client with no MCP interoperability requirement.
- **Fallback:** httpx or the established HTTP/model SDK.
- **Compatibility:** Exact mcp v2.3.0 tagged `pyproject.toml`, README and installation docs declare Python >=3.10; tag CI 37070302489 passed Python 3.10 on Ubuntu/Windows with locked and lowest-direct dependencies. Later `main` docs state 3.11+ but do not negate tagged v2.3.0 proof. v2 stdio/Streamable HTTP supported; handshake protocols through 2025-11-25 and modern 2026-07-28 per-request envelope are distinct.
- **Maintenance:** PyPI/tag 2.3.0, version-specific docs, protocol registry and successful tag CI reviewed 2026-11-17; keep version baseline unchanged.
- **License:** MIT
- **Official source:** [tag pyproject](https://github.com/modelcontextprotocol/python-sdk/blob/v2.3.0/pyproject.toml); [tag install](https://github.com/modelcontextprotocol/python-sdk/blob/v2.3.0/docs/get-started/installation.md); [protocol registry](https://github.com/modelcontextprotocol/python-sdk/blob/v2.3.0/src/mcp-types/mcp_types/version.py); [tag CI PASS](https://github.com/modelcontextprotocol/python-sdk/actions/runs/37070302489); [advisories](https://github.com/modelcontextprotocol/python-sdk/security/advisories)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-17
- **Unknowns:** Python floor discrepancy is version-specific documentation drift: exact v2.3.0 supports/tested 3.10, current `main` says 3.11+. Security GHSA-rwrf-2pqf-9j8j, GHSA-5h93-6whr-6q8j and GHSA-84m7-p3x7-pcfv patched in 2.2.0; on 2.3.0 GHSA-w4fh-qvv9-3v23 resource/audience validation still requires opt-in config. App must verify target protocol transport, untrusted outputs, auth/authorization, SSRF, credentials, cancellation, limits, transitive graph and TCO; no production/security approval.
- **Selection:** EVALUATE

### `celery`
- **Package:** `celery`
- **Capability:** C13 — Async & Messaging
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
- **Capability:** C08 — Persistence
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
- **Capability:** C16 — Performance & Cache
- **Tags:** `columnar-analytics`
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
- **Capability:** C20 — AI & Integrations
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
- **Capability:** C18 — Observability
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

### `uvicorn`
- **Package:** `uvicorn`
- **Capability:** C09 — API & Networking
- **Language/runtime:** Python / PyPI
- **Fit:** ASGI HTTP/WebSocket server for running a FastAPI app with explicit lifespan and deployment configuration.
- **Anti-fit:** No HTTP API deployment or an existing compatible ASGI server/process manager already meets runtime needs.
- **Fallback:** Existing ASGI server or current deployment runner.
- **Compatibility:** PyPI 0.54.0 requires Python >=3.10; pure Python wheel; optional [standard] adds uvloop/httptools on supported targets. FastAPI ASGI execution documented; exact HTTP/2, OS/worker and proxy behavior requires deployment tests.
- **Maintenance:** PyPI 0.54.0 released 2026-09-25; Kludex-maintained project; source and wheels listed.
- **License:** BSD-3-Clause
- **Official source:** [PyPI metadata](https://pypi.org/project/uvicorn/); [upstream/manifest](https://github.com/Kludex/uvicorn)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-17
- **Unknowns:** Exact target dependency graph, overall advisory clearance and performance/TCO NOT_MEASURED.
- **Selection:** EVALUATE

### `python-multipart`
- **Package:** `python-multipart`
- **Capability:** C03 — Forms & Navigation
- **Language/runtime:** Python / PyPI
- **Fit:** Parses multipart/form uploads and form bodies as required for FastAPI Form/File endpoints.
- **Anti-fit:** JSON-only API with no incoming multipart or form payloads.
- **Fallback:** Native JSON request parsing; omit forms/uploads when not required.
- **Compatibility:** PyPI 0.0.34 requires Python >=3.11, py3-none-any wheel; FastAPI Form/File documentation requires this distribution (not unrelated multipart). Body/part size policy still required.
- **Maintenance:** PyPI 0.0.34 released 2026-11-16; Kludex upstream and published provenance.
- **License:** Apache-2.0
- **Official source:** [PyPI metadata](https://pypi.org/project/python-multipart/); [upstream/manifest](https://github.com/Kludex/python-multipart)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-17
- **Unknowns:** Exact target dependency graph, overall advisory clearance and performance/TCO NOT_MEASURED.
- **Selection:** EVALUATE

### `pydantic-settings`
- **Package:** `pydantic-settings`
- **Capability:** C07 — Data Contracts
- **Language/runtime:** Python / PyPI
- **Fit:** Validated typed settings from environment and optional external sources for nontrivial service configuration.
- **Anti-fit:** A few explicit os.environ variables suffice, or settings ownership already exists.
- **Fallback:** os.environ plus Pydantic when necessary.
- **Compatibility:** PyPI 2.16.3 requires Python >=3.11; Pydantic v2 integration advertised; cloud-secret/TOML/YAML extras optional, with separate provider and permissions review.
- **Maintenance:** PyPI 2.16.3 released 2026-11-13; Pydantic project maintained.
- **License:** MIT
- **Official source:** [PyPI metadata](https://pypi.org/project/pydantic-settings/); [upstream/manifest](https://github.com/pydantic/pydantic-settings)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-17
- **Unknowns:** Exact target dependency graph, overall advisory clearance and performance/TCO NOT_MEASURED.
- **Selection:** EVALUATE

### `alembic`
- **Package:** `alembic`
- **Capability:** C08 — Persistence
- **Language/runtime:** Python / PyPI
- **Fit:** Versioned SQL schema migrations for services that own SQLAlchemy-backed relational database changes.
- **Anti-fit:** No relational schema migration, external migration owner, or simple immutable SQLite workload.
- **Fallback:** Existing database migration workflow or explicit reviewed SQL scripts.
- **Compatibility:** PyPI 1.20.1 requires Python >=3.10; pure Python wheel; integrates with SQLAlchemy. Migration driver/async transaction support depends on target database and deployment.
- **Maintenance:** PyPI 1.20.1 released 2026-10-22; SQLAlchemy project.
- **License:** MIT
- **Official source:** [PyPI metadata](https://pypi.org/project/alembic/); [upstream/manifest](https://github.com/sqlalchemy/alembic)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-17
- **Unknowns:** Exact target dependency graph, overall advisory clearance and performance/TCO NOT_MEASURED.
- **Selection:** EVALUATE

### `Authlib`
- **Package:** `Authlib`
- **Capability:** C10 — Identity & Authorization
- **Language/runtime:** Python / PyPI
- **Fit:** OAuth/OIDC client/server protocol handling when the API actually integrates external identity or acts as authorization server.
- **Anti-fit:** Opaque API key/session with managed identity or JWT-only verification suffices; no OAuth/OIDC protocol requirement.
- **Fallback:** FastAPI Security extraction with a trusted upstream identity provider and explicit authorization; narrower JWT library for JWT-only needs.
- **Compatibility:** PyPI Authlib 1.9.8 requires Python >=3.10; uses cryptography; OAuth/OIDC protocols advertised. FastAPI adapter selection/session integration and Pydantic/Starlette version pairing require target verification.
- **Maintenance:** PyPI 1.9.8 released 2026-11-16; authlib upstream.
- **License:** BSD-3-Clause (BSD terms for OSS; optional commercial support is separate)
- **Official source:** [PyPI metadata](https://pypi.org/project/Authlib/); [upstream/manifest](https://github.com/authlib/authlib)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-17
- **Unknowns:** Exact target dependency graph, overall advisory clearance and performance/TCO NOT_MEASURED.
- **Selection:** EVALUATE

### `pwdlib`
- **Package:** `pwdlib`
- **Capability:** C15 — Security & Cryptography
- **Language/runtime:** Python / PyPI
- **Fit:** Application password hashing/verification with modern password algorithms; FastAPI tutorial demonstrates pwdlib[argon2].
- **Anti-fit:** Federated auth, passwordless flows or an existing supported password hashing implementation eliminates a local password store.
- **Fallback:** Existing audited password provider or external identity service; never homebrew a password hash.
- **Compatibility:** PyPI 0.4.2 requires Python >=3.11; py3-none-any wrapper; [argon2] pulls argon2-cffi and its native bindings which require target wheel/ABI review.
- **Maintenance:** PyPI 0.4.2 released 2026-11-15; upstream maintained; PyPI Beta classifier, evaluate maturity.
- **License:** MIT (extra Argon2 bindings/licenses reviewed separately)
- **Official source:** [PyPI metadata](https://pypi.org/project/pwdlib/); [upstream/manifest](https://github.com/frankie567/pwdlib)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-17
- **Unknowns:** Exact target dependency graph, overall advisory clearance and performance/TCO NOT_MEASURED.
- **Selection:** EVALUATE

### `redis`
- **Package:** `redis`
- **Capability:** C16 — Performance & Cache
- **Language/runtime:** Python / PyPI
- **Fit:** Sync/async Redis protocol client for a justified shared cache, rate-limiter backend or coordination feature.
- **Anti-fit:** In-process cache, SQLite/SQL or current managed service avoids Redis operational dependency.
- **Fallback:** Bounded local memory/cache or existing database/service client.
- **Compatibility:** PyPI redis 8.1.0 requires Python >=3.10; py3-none-any wheel; redis.asyncio available, optional hiredis/native and TLS/auth configurations are deployment-specific.
- **Maintenance:** PyPI 8.1.0 released 2026-07-30; maintained by Redis Inc.
- **License:** MIT (Python client; Redis server/service has separate terms)
- **Official source:** [PyPI metadata](https://pypi.org/project/redis/); [upstream/manifest](https://github.com/redis/redis-py)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-17
- **Unknowns:** Exact target dependency graph, overall advisory clearance and performance/TCO NOT_MEASURED.
- **Selection:** EVALUATE

### `pytest-asyncio`
- **Package:** `pytest-asyncio`
- **Capability:** C17 — Testing & QA
- **Language/runtime:** Python / PyPI
- **Fit:** Pytest integration for asyncio coroutine tests when a project already uses pytest.
- **Anti-fit:** Only synchronous tests or stdlib unittest.IsolatedAsyncioTestCase meets the requirement.
- **Fallback:** unittest.IsolatedAsyncioTestCase or existing synchronous pytest tests.
- **Compatibility:** PyPI 1.5.0 requires Python >=3.10 and pytest; py3-none-any wheel; asyncio-based, not a general AnyIO/Trio harness; ASGITransport does not trigger lifespan automatically.
- **Maintenance:** PyPI 1.5.0 released 2026-11-12; pytest-asyncio project and provenance.
- **License:** Apache-2.0
- **Official source:** [PyPI metadata](https://pypi.org/project/pytest-asyncio/); [upstream/manifest](https://github.com/pytest-dev/pytest-asyncio)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-17
- **Unknowns:** Exact target dependency graph, overall advisory clearance and performance/TCO NOT_MEASURED.
- **Selection:** EVALUATE

### `opentelemetry-instrumentation-fastapi`
- **Package:** `opentelemetry-instrumentation-fastapi`
- **Capability:** C18 — Observability
- **Language/runtime:** Python / PyPI
- **Fit:** Optional OpenTelemetry FastAPI/ASGI request instrumentation on top of a configured OTel tracing setup.
- **Anti-fit:** No tracing pipeline, plain logs suffice, or manual instrumentation already covers needed spans.
- **Fallback:** Existing structlog/logging or manual OTel SDK spans.
- **Compatibility:** PyPI 0.66b2 requires Python >=3.10; official FastAPI instrumentation; OTel API/SDK, ASGI/Starlette/semantic conventions and exporters must be version-aligned.
- **Maintenance:** PyPI 0.66b2 released 2026-10-29; OpenTelemetry Python Contrib beta/pre-release line, not a stable-version guarantee.
- **License:** Apache-2.0
- **Official source:** [PyPI metadata](https://pypi.org/project/opentelemetry-instrumentation-fastapi/); [upstream/manifest](https://github.com/open-telemetry/opentelemetry-python-contrib)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-17
- **Unknowns:** Exact target dependency graph, overall advisory clearance and performance/TCO NOT_MEASURED.
- **Selection:** EVALUATE

### `ruff`
- **Package:** `ruff`
- **Capability:** C19 — Developer Tooling
- **Language/runtime:** Python / PyPI
- **Fit:** One configurable Python linter + formatter for a project that wants consistent CI/editor enforcement.
- **Anti-fit:** Existing linters/formatters already satisfy conventions or no automated lint gate is needed.
- **Fallback:** Existing quality tooling and stdlib compileall where applicable.
- **Compatibility:** PyPI 0.17.5 requires Python >=3.7 as distribution metadata; executable packaged as platform-specific Rust binary wheels (macOS/Linux/Windows ARM/x86), verify target OS/arch; not a FastAPI runtime dependency.
- **Maintenance:** PyPI 0.17.5 released 2026-11-12; Astral upstream, wheels published.
- **License:** MIT
- **Official source:** [PyPI metadata](https://pypi.org/project/ruff/); [upstream/manifest](https://github.com/astral-sh/ruff)
- **Evidence status:** VERIFIED
- **Evidence reviewed:** 2026-11-17
- **Unknowns:** Exact target dependency graph, overall advisory clearance and performance/TCO NOT_MEASURED.
- **Selection:** EVALUATE

## Selection boundary

VERIFIED is scoped to official package identity, metadata and advertised function; it is NOT a security endorsement, benchmark result or production approval. PARTIAL means essential metadata is unresolved. EVALUATE permits comparison only, BLOCKED requires filling compatibility/license gaps first. No automatic migration.

[Index](README.md) · [Languages](../languages/README.md) · [Frameworks](../frameworks/README.md) · [Decisions](../decisions/README.md)
