<!-- Q: What's the difference between TCP and UDP? -->

**TCP** (Transmission Control Protocol) and **UDP** (User Datagram Protocol) are both transport-layer protocols, but they make opposite tradeoffs.

| | TCP | UDP |
|---|---|---|
| **Connection** | Connection-oriented (3-way handshake) | Connectionless |
| **Reliability** | Guaranteed delivery via ACKs and retransmission | Best-effort; lost packets are not resent |
| **Ordering** | Data arrives in order | No ordering guarantee |
| **Flow/congestion control** | Yes | No |
| **Overhead** | Higher (20+ byte header, state tracking) | Lower (8 byte header) |
| **Speed/latency** | Slower, can stall on retransmits | Faster, minimal latency |
| **Data model** | Byte stream (no message boundaries) | Discrete datagrams (boundaries preserved) |

**Use TCP when** correctness matters more than speed: web (HTTP/1.1, HTTP/2), email, file transfer, SSH, databases.

**Use UDP when** low latency matters or you can tolerate or handle loss yourself: DNS lookups, live video/voice, online games, streaming, VPNs. QUIC (HTTP/3) is built on UDP, adding its own reliability and congestion control on top.

**Rule of thumb:** TCP gives you a reliable pipe at the cost of latency; UDP gives you raw speed and leaves reliability up to the application.
