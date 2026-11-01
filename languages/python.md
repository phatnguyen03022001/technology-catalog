# Python

**Evidence review:** 2026-11-01 · [Quay lại so sánh](README.md)

## Fit & trade-offs

- **Phù hợp:** ML/AI và data tooling, ETL, automation/scripts, API dựa vào Python-native libraries, inference orchestration.
- **Lợi thế kỹ thuật:** hệ sinh thái data/ML; standard library; dependency/packaging tools, type annotations và productivity.
- **Đổi lại:** dynamic typing; type hints không tự validate runtime; CPU-bound execution, interpreter, native dependencies, GPU drivers và wheel/ABI compatibility cần kiểm chứng. Không gộp mọi Python version/implementation dưới một giả định GIL hoặc async duy nhất.

## Ecosystem và điểm xuất phát KISS

| Lớp | Mặc định | Khi nào thêm công nghệ |
|---|---|---|
| Environment | `venv`, `pip`, `pyproject.toml` | **uv** nếu muốn thống nhất environment, lock, Python/tool management; không bắt buộc migrate |
| Web/API | Existing project framework hoặc tối giản | **FastAPI** cho typed endpoints, OpenAPI và request validation; **Django** cho ORM/admin/fullstack app |
| ML/data | Library đúng workload và model | Inference worker/queue khi CPU/GPU/memory trở thành bottleneck đã đo |
| Concurrency | Sync hoặc async theo I/O behavior | `asyncio` cho I/O concurrency; process/worker riêng khi workloads yêu cầu |

**Quality gates tham khảo:** `pytest` hoặc `unittest`, Ruff/type checker theo project, lock/dependency audit, tests trên target OS/arch. Type checker không thay input validation, auth, serialization hoặc schema checks tại trust boundaries.

**Trước production:** Python implementation/version, macOS ARM64 wheels vs Linux containers, CPU/GPU support, native binary dependencies, worker/concurrency model, timeout/cancel/retry/idempotency, observability, performance measurement, migrations, inference API cost và hosting. Giá từ [provider profiles](../providers/README.md).

**Không mặc định chọn:** native Apple UI; viết lại service Go/TS đang ổn chỉ vì có một AI feature — cân nhắc worker Python hẹp scope.

## Official evidence

- [Python standard documentation](https://docs.python.org/3/)
- [PyPA packaging user guide](https://packaging.python.org/en/latest/)
- [Python virtual environments](https://docs.python.org/3/library/venv.html)
- [uv documentation](https://docs.astral.sh/uv/)
- [FastAPI features](https://fastapi.tiangolo.com/features/)
- [Django documentation](https://docs.djangoproject.com/)
