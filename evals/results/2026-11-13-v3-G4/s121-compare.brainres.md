<!-- Q: What's the difference between TCP and UDP? -->

TCP is connection-oriented and reliable (ordered, retransmitted, error-checked), while UDP is connectionless and unreliable but faster and lighter.

| | TCP | UDP |
|---|---|---|
| Connection | Three-way handshake before data | None; just send packets |
| Delivery | Guaranteed, with retransmission | Best effort; packets can be lost or duplicated |
| Ordering | Preserved | Not preserved |
| Flow/congestion control | Yes | No |
| Header size | 20+ bytes | 8 bytes |
| Speed/latency | Slower, more overhead | Faster, lower latency |

**Use TCP** when every byte must arrive correctly: web (HTTP/1.1, HTTP/2), email, SSH, file transfer.

**Use UDP** when speed matters more than completeness, or you want to handle loss yourself: DNS lookups, live video/voice, online games, and QUIC (which powers HTTP/3 and builds its own reliability on top of UDP).

TCP is a stream of bytes with no message boundaries, while UDP preserves each datagram as a discrete message. So with UDP, one `send` generally maps to one `recv`, but you must handle loss and reordering yourself.

Next step: if you're choosing one for a project, tell me the use case and I'll recommend one.
