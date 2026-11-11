<!-- Q: Explain how HTTPS keeps my password safe. -->

HTTPS encrypts your connection with TLS, so anyone between you and the server (Wi-Fi owner, ISP, attacker) sees only scrambled bytes, not your password.

**How it works when you log in:**

1. **Identity check.** The server sends a certificate signed by a trusted authority. Your browser verifies it matches the domain, for example `example.com`, so you aren't talking to an impostor.
2. **Key agreement.** Your browser and the server use an ephemeral Diffie-Hellman exchange (ECDHE) to derive a shared secret. The secret is never sent over the network, and it is new for each session. So even if the server's key leaks later, recorded traffic stays unreadable (forward secrecy).
3. **Encrypted, tamper-proof traffic.** Everything after that is encrypted and authenticated with AES-GCM or ChaCha20-Poly1305. If someone alters a single byte in transit, the check fails and the connection drops.
4. **Your password goes through that channel.** The login form's POST body, including the password, is encrypted. Observers can still see the domain name and roughly how much data moved, but not the path, headers, or body.

**What HTTPS does not protect:**

| Threat | Why it still works |
|---|---|
| Phishing site with its own valid certificate | The certificate proves the domain, not that it's the one you meant (`examp1e.com`) |
| Malware or keylogger on your device | It reads the password before encryption |
| The server mishandling it | The server receives the plaintext password and must hash it (bcrypt, argon2) |
| Weak or reused password | Encryption in transit doesn't fix a guessable password |

Next step: before typing a password, check the exact domain in the address bar, and use a password manager, because it only autofills on the real domain, which defeats most lookalike-site phishing.
