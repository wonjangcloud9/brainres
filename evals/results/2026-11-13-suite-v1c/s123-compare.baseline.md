<!-- Q: REST vs gRPC: what are the trade-offs? -->

**Short version:** REST is the safer default for public and browser-facing APIs. gRPC wins for internal service-to-service traffic where performance and strict contracts matter.

## Where gRPC wins
- **Performance:** Protobuf is a compact binary format, and HTTP/2 gives multiplexing and header compression. Payloads are smaller and serialization is faster than JSON.
- **Strict contracts:** `.proto` files are the schema. You generate typed clients and servers in many languages, which removes a whole class of drift and hand-written client bugs.
- **Streaming:** Server, client, and bidirectional streaming are first-class.
- **Built-in features:** Deadlines, cancellation propagation, and interceptors for auth, tracing, and retries.
- **Evolution rules:** Field numbers give clear backward/forward compatibility guidelines.

## Where REST wins
- **Ubiquity:** Every language, tool, proxy, and browser speaks HTTP+JSON. No code generation is required to get started.
- **Debuggability:** You can use curl, browser dev tools, and read payloads by eye. Protobuf needs tooling (grpcurl, reflection).
- **Browser support:** gRPC needs grpc-web or a proxy (Envoy, Connect) because browsers can't use the full HTTP/2 gRPC protocol directly.
- **Caching and infrastructure:** HTTP caching semantics, CDNs, and standard load balancers work out of the box. gRPC needs HTTP/2-aware LBs, and per-request balancing needs extra care because of long-lived connections.
- **Lower barrier for third parties:** External developers expect REST/JSON and OpenAPI docs.

## Trade-off summary

| Concern | REST | gRPC |
|---|---|---|
| Payload | JSON, text, larger | Protobuf, binary, smaller |
| Contract | Optional (OpenAPI) | Mandatory (.proto) |
| Streaming | Awkward (SSE, WebSockets) | Native |
| Browser | Native | Needs grpc-web/proxy |
| Caching | Native HTTP caching | Limited |
| Debugging | Easy | Needs tooling |
| Codegen | Optional | Standard |
| Public API fit | Excellent | Poor |

## Rules of thumb
- **Public API, third-party consumers, or browser clients:** REST (or GraphQL).
- **Internal microservices, polyglot backends, high throughput or low latency:** gRPC.
- **Streaming or long-lived bidirectional communication:** gRPC.
- **Mixed needs:** gRPC internally with a REST/JSON gateway at the edge (grpc-gateway, or Connect, which serves both from one definition).

Also worth weighing: team familiarity and operational overhead. A gRPC migration gains little if your bottleneck is the database rather than serialization, and the added tooling and proto management are real costs for small teams.

If you tell me your use case (client types, scale, streaming needs), I can give a more specific recommendation.
