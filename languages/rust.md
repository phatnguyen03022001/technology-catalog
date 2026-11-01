# Rust

**Evidence review:** 2026-11-01 · [Quay lại so sánh](README.md)

## Fit & trade-offs

- **Phù hợp:** native CLI, agent runtime/sandbox components, parsers, networking, native libraries và phần mềm có ràng buộc rõ về memory/CPU.
- **Lợi thế kỹ thuật:** ownership/borrowing bảo vệ memory safety trong safe Rust mà không cần tracing GC; Cargo có dependency/build/test; Tokio là async runtime cho network I/O.
- **Đổi lại:** ownership/lifetimes và compile/build complexity; `unsafe`, FFI, dependencies native vẫn cần kiểm toán. Không tuyên bố Rust nhanh/an toàn hơn tất cả trong mọi workload.

## Ecosystem và điểm xuất phát KISS

| Lớp | Mặc định | Khi nào thêm công nghệ |
|---|---|---|
| Toolchain | `rustup`, `cargo`, `rustfmt`, `clippy` | Pin toolchain và cross-target khi CI/release cần reproducibility |
| Web/API | Standard library khi đủ | **axum** cho routing, extractors, middleware; tương thích Tokio/hyper |
| Async/network | Threads/channels cho đơn giản | **Tokio** khi thật sự có async I/O, nhiều connections, backpressure |
| Data/interop | SQL driver/HTTP/JSON theo nhu cầu | Native FFI/C ABI khi protocol boundary không đủ; audit `unsafe` |

**Quality gates tham khảo:** `cargo fmt --check`, `cargo clippy`, `cargo test`; dependency/advisory checks và benchmarks khi có requirement. Rule cảnh báo lint tuỳ chính sách dự án.

**Trước production:** kiểm tra target OS/arch (Linux/macOS/ARM64), libc/static linking, binary size, TLS/crypto, memory profile, panic/error policy, blocking inside async, cancellation, shutdown, licensing, observability, build cache và release artifacts.

**Không mặc định chọn:** CRUD nhỏ cần delivery nhanh, notebook/data science, Apple-native UI; không dùng FFI chỉ vì muốn chia nhỏ thành nhiều ngôn ngữ.

## Official evidence

- [Rust Book — ownership](https://doc.rust-lang.org/book/ch04-00-understanding-ownership.html)
- [Cargo documentation](https://doc.rust-lang.org/cargo/)
- [Rust tooling: fmt, clippy, test](https://rust-lang.org/tools/)
- [Tokio asynchronous runtime](https://tokio.rs/tokio/tutorial)
- [axum HTTP library](https://docs.rs/axum/latest/axum/)
