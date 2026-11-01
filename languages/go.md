# Go

**Evidence review:** 2026-11-01 · [Quay lại so sánh](README.md)

## Fit & trade-offs

- **Phù hợp:** HTTP/gRPC backends, network services, cloud/infra CLIs, distributed workers và services có nhiều I/O đồng thời.
- **Lợi thế kỹ thuật:** compiled/static typing, GC, goroutines/channels; standard library hỗ trợ HTTP, JSON, SQL, tests và profiling; Go modules thống nhất workflow.
- **Đổi lại:** GC và latency/RAM phải đo; goroutines vẫn có race/leak; cgo làm cross-build phức tạp. Go không phải framework ML hoặc giải pháp browser UI.

## Ecosystem và điểm xuất phát KISS

| Lớp | Mặc định | Khi nào thêm công nghệ |
|---|---|---|
| Build/packages | `go mod`, `go build`, `gofmt` | Pin toolchain, modules, verify dependency integrity |
| Web/API | `net/http` + `ServeMux` (method/path patterns) | **Gin** khi cần binding, middleware, conventions mà stdlib chưa đáp ứng |
| Data/interop | `database/sql`, `encoding/json`, `context` | Driver/migration/gRPC/queue theo target workload |
| Concurrency | Goroutines, channels, `context` | Bounded workers, backpressure, tracing, cancellation khi cần |

**Quality gates tham khảo:** `gofmt`, `go vet ./...`, `go test ./...`, `go test -race ./...` trong environment hỗ trợ, fuzz tests và `govulncheck ./...` nếu policy/capabilities phù hợp. Race detector chỉ thấy paths đã chạy, không chứng minh mọi race đều vắng mặt.

**Trước production:** propagate deadlines và cancellation qua `context`, retries/idempotency, graceful shutdown, DB pools, CGO và cross-target support, goroutine count, heap/GC profile, observability, CPU/RAM/p99. Chi phí các dịch vụ cloud tra trong [provider profiles](../providers/README.md).

**Không mặc định chọn:** SwiftUI/iOS UI, TS browser frontend, Python-native ML workloads.

## Official evidence

- [Go docs: language, modules và toolchain](https://go.dev/doc/)
- [Go ServeMux routing enhancements](https://go.dev/doc/go1.22)
- [Go race detector](https://go.dev/doc/articles/race_detector)
- [Go vulnerability management](https://go.dev/doc/security/vuln/)
- [Gin web framework](https://gin-gonic.com/en/docs/)
