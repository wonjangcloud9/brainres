<!-- Q: REST vs gRPC: what are the trade-offs? -->

REST wins on reach and simplicity; gRPC wins on speed and strict contracts, so use REST for public APIs and gRPC for internal service-to-service calls.

| | REST (JSON over HTTP) | gRPC (Protobuf over HTTP/2) |
|---|---|---|
| Payload | Text JSON, larger, slower to parse | Binary, smaller, faster |
| Contract | Optional (OpenAPI) | Required (`.proto`), generates typed clients |
| Streaming | Awkward (SSE, WebSockets) | Built in: server, client, bidirectional |
| Browser support | Native | Needs gRPC-Web plus a proxy |
| Debugging | `curl`, browser, any tool | Needs `grpcurl` or similar; payload is unreadable |
| Caching | HTTP caching and CDNs work | Poor; calls are POSTs |
| Evolution | Flexible, but drift is easy | Safe field numbering, but needs discipline |

**Pick REST when:**
- Third parties or browsers call your API.
- You want CDN caching or easy debugging.
- Your team is small and wants minimal tooling.

**Pick gRPC when:**
- Many internal microservices call each other at high volume, where latency and bandwidth matter.
- You need streaming.
- You have several languages and want generated clients that stay in sync.

Many systems use both: gRPC inside, a REST gateway at the edge. Tools like grpc-gateway or Envoy can generate the REST layer from your `.proto` files.

The speed gain depends on your workload. For low-traffic APIs, network and database time usually dominate, so measure before switching for performance alone.

If you tell me your setup (who the clients are, call volume, languages), I can give a firmer recommendation.
