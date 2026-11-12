<!-- Q: What's the difference between TCP and UDP? -->

TCP guarantees ordered, reliable delivery over a connection; UDP just sends packets with no guarantees, so it is faster and lighter.

| | TCP | UDP |
|---|---|---|
| Connection | Handshake first (SYN, SYN-ACK, ACK) | None, just send |
| Delivery | Retransmits lost packets, so nothing is missing | Lost packets stay lost |
| Order | Preserved | Not preserved |
| Control | Flow and congestion control | None |
| Header size | 20+ bytes | 8 bytes |
| Boundaries | Byte stream, no message edges | Each datagram is a separate message |

TCP pays for its guarantees with extra round trips and head-of-line blocking: one lost packet stalls everything behind it until it is resent. UDP avoids that cost, but the application must handle loss, ordering, and duplicates itself if it cares.

**Use TCP** when every byte must arrive correctly: web pages (HTTP/1.1 and HTTP/2), email, file transfer, SSH, databases.

**Use UDP** when speed matters more than completeness, or when you want your own reliability logic: DNS lookups, live video and voice, online games, and QUIC (which HTTP/3 runs on, adding its own reliability on top of UDP).

If you tell me what you are building, I can say which fits better.
