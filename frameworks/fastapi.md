# FastAPI — Python / ASGI

**Reviewed:** 2026-11-01 · [Framework index](README.md)

## Fit
Python-first model/data APIs, structured request/response validation, dependency injection, JSON Schema/OpenAPI interfaces, typed endpoints.

## Anti-fit
Frontend HTML product primarily requiring rich client navigation; backend with no Python-native requirements where existing service in Go/TS suffices; heavy CPU inference mistakenly expected to scale via async alone.

## Compatibility
ASGI deployment needs compatible server (e.g. Uvicorn), supported Python and Pydantic/Starlette versions; sync vs async libraries and background tasks behave differently. Validate target GPU/worker/container compatibility.

## Maturity & maintenance
First-party docs and public source; pin framework and dependency versions, monitor breaking changes and security support. No automatic long-term maintenance guarantee.

## Licensing
FastAPI open-source code is **MIT**; Python runtime, model weights, native extensions and deployment APIs have separate terms.

## Operational / test evidence needed
Runtime schema validation, auth scopes, dependency overrides, HTTP contract tests, startup/shutdown, blocking/CPU work, worker memory, streaming/cancel, p95 and model inference cost.

## Official evidence
- [FastAPI features and validation](https://fastapi.tiangolo.com/features/)
- [FastAPI manual server deployment](https://fastapi.tiangolo.com/deployment/manually/)
- [FastAPI source/license](https://github.com/fastapi/fastapi)
