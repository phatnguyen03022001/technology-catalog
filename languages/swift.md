# Swift

**Evidence review:** 2026-11-01 · [Quay lại so sánh](README.md)

## Fit & trade-offs

- **Phù hợp:** native iOS/macOS/watchOS/tvOS/visionOS UI, device/Apple platform APIs, offline apps; Swift CLI/server cũng có khả năng chạy trên những platform được hỗ trợ.
- **Lợi thế kỹ thuật:** strong typing, optionals, ARC, structured concurrency với actors, Swift Package Manager; SwiftUI có declarative UI cho các Apple platforms.
- **Đổi lại:** Apple UI, Xcode, signing/provisioning, entitlement, minimum target OS và distribution có yêu cầu riêng. Swift có thể chạy trên Linux/Windows **không có nghĩa** SwiftUI/UIKit/AppKit được hỗ trợ tại đó. Server Swift chỉ nên chọn khi ecosystem, CI/deploy và maintenance fit.

## Ecosystem và điểm xuất phát KISS

| Lớp | Mặc định | Khi nào thêm công nghệ |
|---|---|---|
| Toolchain | Xcode + Swift, **SwiftPM** | Pin language mode, SDK và deployment target; CI cần đúng Apple toolchain nếu build app |
| Native UI | **SwiftUI** nếu target đáp ứng | UIKit/AppKit interoperability khi API/legacy UI yêu cầu, không ép migrate |
| Local data | Foundation, persistence hợp nhu cầu | **SwiftData** khi version support, schema migration và offline sync phù hợp |
| Async | `async/await`, actors, `Sendable` | Kiểm chứng isolation, cancellation, task lifecycle, blocking behavior |
| Server/API | Standard libraries và HTTP stack cần thiết | **Vapor** hoặc **Hummingbird** nếu cần server Swift với routing/middleware |

**Quality gates tham khảo:** `swift test` cho Swift packages, Swift Testing/XCTest theo target; UI tests trong Xcode/Simulator/device; static/concurrency checks và release signing validation. Linux CI cho pure Swift **không thay** iOS app testing trên macOS/Xcode.

**Trước production:** minimum OS/SDK versions, signing/notarization, privacy permissions, data storage/backup/migrations, app review/distribution terms & cost, crash analytics, accessibility, Linux server binary/dependency compatibility, provider SDK parity. Swift backend không mặc định tốt hơn Go/TS/Python chỉ vì app client viết Swift.

**Không mặc định chọn:** web browser frontend hoặc backend khi team/runtime/SDK fit không đủ; không thêm Swift server để tránh chia sẻ một HTTP schema.

## Official evidence

- [Swift platform support](https://www.swift.org/platform-support/)
- [Swift concurrency](https://docs.swift.org/latest/documentation/the-swift-programming-language/concurrency/)
- [Swift Package Manager](https://docs.swift.org/main/documentation/packagemanagerdocs/)
- [SwiftUI](https://developer.apple.com/documentation/swiftui)
- [SwiftData](https://developer.apple.com/documentation/swiftdata)
- [Swift Testing và XCTest](https://developer.apple.com/documentation/xcode/adding-tests-to-your-xcode-project)
- [Swift on Server — Vapor và Hummingbird](https://www.swift.org/documentation/server/)
