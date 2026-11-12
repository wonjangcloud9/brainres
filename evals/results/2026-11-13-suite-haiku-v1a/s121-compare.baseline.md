<!-- Q: What's the difference between TCP and UDP? -->

TCP and UDP are the two main transport-layer protocols in the Internet Protocol Suite. Both carry data between applications over IP, but they make different trade-offs.

| | **TCP** (Transmission Control Protocol) | **UDP** (User Datagram Protocol) |
|---|---|---|
| **Connection** | Connection-oriented: a three-way handshake sets up the session first | Connectionless: packets are sent without setup |
| **Reliability** | Guarantees delivery. Lost packets are retransmitted, and data arrives in order | No guarantees. Packets can be lost, duplicated, or arrive out of order |
| **Ordering** | Preserves the order of bytes | No ordering |
| **Flow control** | Uses sliding windows so a fast sender doesn't overwhelm a slow receiver | None |
| **Congestion control** | Backs off when the network is congested | None; the application must handle it |
| **Overhead** | Larger header (20 bytes minimum) plus handshake and acknowledgment traffic | Small 8-byte header, no handshake |
| **Latency** | Higher, because of retransmits and head-of-line blocking | Lower, with no waiting for acknowledgments |
| **Data model** | Byte stream, with no message boundaries | Discrete datagrams, each with its own boundaries |
| **Typical uses** | Web (HTTP/1.1, HTTP/2), email, file transfer, SSH, databases | DNS, video/voice streaming, online games, VoIP, DHCP, QUIC (which builds reliability on top of UDP) |

**When to use which:**
- Use **TCP** when every byte has to arrive correctly and in order, such as with files, web pages, or transactions.
- Use **UDP** when speed or timeliness matters more than perfect delivery, such as with live video, gaming state updates, or simple request/response lookups. A lost frame is better skipped than delayed.

**A useful way to remember it:** TCP is like a phone call, where you set up the connection, confirm each piece is heard, and repeat what was missed. UDP is like mailing postcards: quick and cheap, but nothing tells you whether each one arrived.
