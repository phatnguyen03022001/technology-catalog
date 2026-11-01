# DEC-AI-001 — Python model API

**Status:** CONDITIONAL_NOT_PRODUCTION · **Reviewed:** 2026-11-01 · **Workload:** REFERENCE_SCENARIO_NOT_MEASURED.

## Workload & candidates
Assume an existing Python model library needs JSON inference endpoints, typed input schema and an independently deployed worker. Compare **FastAPI + compatible ASGI server** vs **NestJS gateway calling a Python worker** vs **Go net/http gateway calling a Python worker**. The model library itself remains Python; this case concerns the API boundary.

| Candidate | Evidence-backed fit | Costs/risks to verify |
|---|---|---|
| [FastAPI](../frameworks/fastapi.md) | Python types, Pydantic validation and OpenAPI in same process/stack | Model blocks event loop, ASGI workers/GPU memory, startup |
| [NestJS](../frameworks/nestjs.md) + Python worker | Node controller/DI conventions if org already TS-centric | Additional deployment, network hops, contract consistency |
| Go net/http + Python worker | Lean stdlib HTTP gateway if already Go infrastructure | Additional service, model transport/worker handling |

## Hard gates & unknown evidence
- Functional: **PASS conditional** — FastAPI exposes OpenAPI and Pydantic validation, not proof of model fit.
- Security/privacy: **UNKNOWN** — data sensitivity, auth, model retention and process isolation untested.
- Legal/licensing: **UNKNOWN** — model weights, GPU runtime and hosted inference ToS not checked.
- Cost/TCO: **UNKNOWN**; no GPU/CPU inference speed, requests/day, concurrency or pricing; benchmark **NOT_MEASURED**.
- Portability/recovery: **UNKNOWN** until model artifacts, version, rollback, architecture/ABI compatibility tested.

## Decision & falsification
**Conditional choice: FastAPI** when one Python service is enough and model calls do not violate latency/resource gates. Split gateway/worker only when independently scaling models, network security boundaries, existing platform or measured deployment behavior demands it. **Not production-approved.**

## Verification / TCO / fallback
Run equal model/version/batch-size loads at expected concurrency; record p95/p99, peak RAM/VRAM, GPU util, timeout/cancel and crash recovery. TCO = compute/GPU per runtime-hour + model/network/storage/egress + operations, with plans from [AI & agent pillars](../pillars/10-ai-models-agent-tools/README.md) and [providers](../providers/README.md). Verify identity/secrets, input constraints, worker shutdown, rollback. Fallback: keep inference as isolated Python worker with established platform gateway if in-process model invalidates gates.

## Official evidence
- [FastAPI features](https://fastapi.tiangolo.com/features/)
- [FastAPI ASGI server operation](https://fastapi.tiangolo.com/deployment/manually/)
- [Nest controllers](https://docs.nestjs.com/controllers)
- [Go HTTP standard library](https://pkg.go.dev/net/http)
