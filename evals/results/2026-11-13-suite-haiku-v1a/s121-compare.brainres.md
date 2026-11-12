<!-- Q: What's the difference between TCP and UDP? -->

TCP guarantees delivery, order, and no duplicates. UDP sends datagrams with no such guarantees, so it is faster and has less overhead.

| | TCP | UDP |
|---|---|---|
| Connection | Connection-oriented (3-way handshake) | Connectionless |
| Reliability | Retransmits lost packets, acknowledges receipt | No retransmission, no acknowledgment |
| Ordering | Delivers bytes in order | No ordering; packets can arrive out of order |
| Flow/congestion control | Yes | No |
| Header size | 20 bytes minimum | 8 bytes |
| Speed | Slower due to overhead | Faster, lower latency |
| Data unit | Byte stream | Discrete datagrams (messages) |

**Typical uses**

- **TCP:** web pages (HTTP/HTTPS), email, file transfer, SSH, database connections. Any case where every byte must arrive intact.
- **UDP:** DNS lookups, video and voice calls, online games, live streaming, VPNs. Any case where a late packet is worse than a lost one, or where the application handles its own reliability (QUIC, which powers HTTP/3, builds reliability on top of UDP).

**Rule of thumb:** choose TCP when correctness matters more than latency. Choose UDP when latency matters more than correctness.
