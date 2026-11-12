<!-- Q: What's the difference between TCP and UDP? -->

TCP guarantees ordered, reliable delivery of a byte stream; UDP sends independent packets with no guarantees, so it is faster and lighter.

| | TCP | UDP |
|---|---|---|
| Connection | Handshake first (SYN, SYN-ACK, ACK) | None; just send |
| Delivery | Lost packets are retransmitted | Lost packets stay lost |
| Order | Preserved | Not preserved |
| Flow/congestion control | Yes | No |
| Message boundaries | None (stream of bytes) | Kept (one datagram = one message) |
| Header size | 20+ bytes | 8 bytes |

**Pick TCP** when every byte must arrive correctly: web (HTTP/1.1, HTTP/2), email, SSH, file transfer, databases.

**Pick UDP** when late data is worse than lost data, or when you want to build your own reliability: live video/voice, games, DNS lookups, and QUIC (which HTTP/3 runs on top of UDP).

The cost of TCP's guarantees is latency. One lost packet blocks everything behind it until the retransmit arrives (head-of-line blocking). UDP avoids that, but your application must handle loss, reordering, and duplicates itself.

If you have a specific use case, tell me what you're sending and I'll recommend one.
