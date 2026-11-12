<!-- Q: What's the difference between TCP and UDP? -->

TCP guarantees ordered, reliable delivery over a connection; UDP just sends packets with no guarantees, so it is faster and lighter.

| | TCP | UDP |
|---|---|---|
| Connection | Handshake first (SYN, SYN-ACK, ACK) | None, just send |
| Delivery | Lost packets are retransmitted | Lost packets stay lost |
| Order | Preserved | Not preserved |
| Flow/congestion control | Yes | No |
| Header size | 20+ bytes | 8 bytes |
| Unit | Byte stream (no message boundaries) | Datagrams (boundaries kept) |

**When to use which:**
- **TCP:** web (HTTP/1.1, HTTP/2), SSH, email, file transfer. Anything where missing or reordered data breaks the result.
- **UDP:** DNS lookups, live video/voice, games, QUIC (HTTP/3). Anything where a late packet is worse than a lost one, or where the app handles reliability itself.

Reliability costs latency: a lost TCP packet stalls everything behind it (head-of-line blocking) until it is resent. That stall is why QUIC builds its own reliable streams on top of UDP.
