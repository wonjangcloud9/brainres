<!-- Q: What's the difference between TCP and UDP? -->

TCP delivers data reliably and in order over a connection, while UDP sends independent packets with no delivery guarantee, so UDP is faster and lighter but can lose or reorder data.

| | TCP | UDP |
|---|---|---|
| Connection | Handshake first (SYN, SYN-ACK, ACK) | None; just send |
| Reliability | Retransmits lost segments, acknowledges receipt | Lost packets stay lost |
| Ordering | Reassembles bytes in order | Packets may arrive out of order |
| Data model | Continuous byte stream | Discrete datagrams (message boundaries kept) |
| Flow/congestion control | Yes; slows down when the network or receiver is overloaded | None built in |
| Header size | 20–60 bytes | 8 bytes |
| Latency | Higher: handshake, plus waiting on retransmits (head-of-line blocking) | Lower |

**When to use each:**
- **TCP:** web pages (HTTP/1.1, HTTP/2), email, SSH, file transfer, where every byte must arrive intact.
- **UDP:** DNS lookups, video calls, live streaming, online games, where a late packet is worse than a missing one.

The line has blurred somewhat. QUIC (the transport under HTTP/3) runs on UDP but adds its own reliability, ordering per stream, and encryption. It gets TCP-like guarantees without TCP's head-of-line blocking, because a lost packet only stalls its own stream.

Here's a quick way to see the difference on your Mac. Run `nc -l 9000` in one terminal and `nc localhost 9000` in another for TCP. Then repeat with `-u` added to both commands for UDP. With UDP, the "connection" succeeds even if no listener exists.
