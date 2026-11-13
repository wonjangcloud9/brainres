<!-- Q: What's the difference between TCP and UDP? -->

TCP and UDP are both transport-layer protocols that run on top of IP. They make opposite trade-offs between reliability and speed.

## TCP (Transmission Control Protocol)

- **Connection-oriented:** a three-way handshake (SYN → SYN-ACK → ACK) sets up the connection before any data is sent.
- **Reliable delivery:** every segment is acknowledged, and lost segments are retransmitted.
- **Ordered:** sequence numbers let the receiver reassemble data in the right order.
- **Flow control:** a sliding window keeps the sender from overwhelming the receiver.
- **Congestion control:** the sender slows down when the network is congested (Reno, CUBIC, BBR, etc.).
- **Byte stream:** there are no message boundaries. The application sees a continuous stream of bytes.
- **Higher overhead:** the header is 20–60 bytes, plus the cost of the handshake and ACKs.

## UDP (User Datagram Protocol)

- **Connectionless:** there is no handshake. You just send packets.
- **Unreliable:** there are no ACKs and no retransmission, so packets may be lost, duplicated, or arrive out of order.
- **Message-oriented:** each `send` is one datagram, and boundaries are preserved.
- **No flow or congestion control:** the application has to handle this itself, if it needs it.
- **Low overhead:** the header is a fixed 8 bytes (ports, length, checksum).

## Side-by-side

| | TCP | UDP |
|---|---|---|
| Connection | Required | None |
| Reliability | Guaranteed | Best-effort |
| Ordering | Guaranteed | Not guaranteed |
| Speed / latency | Slower to start, can stall on loss | Fast, no head-of-line blocking |
| Header size | 20–60 bytes | 8 bytes |
| Broadcast/multicast | No | Yes |

## Typical uses

- **TCP:** web (HTTP/1.1, HTTP/2), email (SMTP, IMAP), SSH, file transfer, and databases. These are cases where every byte must arrive correctly.
- **UDP:** DNS queries, VoIP, video calls, live streaming, online games, DHCP, and NTP. These are cases where a late packet is worthless, so it's better to drop it and move on.

## Modern twist

**QUIC**, the protocol under HTTP/3, is built on UDP. It reimplements reliability, ordering, and congestion control in user space, and adds per-stream ordering, which avoids TCP's head-of-line blocking. It also builds in TLS 1.3 and supports faster connection setup (0-RTT/1-RTT). This shows that UDP is often used as a minimal base for building custom transport behavior.

**Rule of thumb:** use TCP when correctness matters more than latency, and UDP when timeliness matters more than completeness, or when you want to build your own reliability layer.
