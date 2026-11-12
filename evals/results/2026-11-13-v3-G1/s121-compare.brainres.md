<!-- Q: What's the difference between TCP and UDP? -->

TCP guarantees delivery and order; UDP doesn't, but it's faster and lighter.

| | TCP | UDP |
|---|---|---|
| Connection | Handshake first (SYN, SYN-ACK, ACK) | None; just send |
| Delivery | Lost packets are retransmitted | Lost packets stay lost |
| Order | Preserved | Not guaranteed |
| Flow/congestion control | Yes | No |
| Header size | 20+ bytes | 8 bytes |
| Message model | Byte stream (no message boundaries) | Datagrams (each send is one message) |

**Use TCP** when every byte must arrive correctly: web (HTTP/1.1, HTTP/2), email, SSH, file transfer.

**Use UDP** when speed or low latency matters more than completeness, or when you want to build your own reliability: DNS, video calls, online games, VoIP. HTTP/3 runs on QUIC, which builds reliable streams on top of UDP.

The cost of TCP's guarantees is latency: a lost packet stalls everything behind it (head-of-line blocking) until it's resent. UDP skips that wait, so a game or call just drops the late data and moves on.

If you have a specific use case, tell me and I can say which fits better.
