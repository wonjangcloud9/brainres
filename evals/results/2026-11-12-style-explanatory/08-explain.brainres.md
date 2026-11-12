<!-- Q: Explain how HTTPS keeps my password safe. -->

HTTPS keeps your password safe in transit by encrypting it so that anyone on the network path (Wi-Fi owner, ISP, router) sees only unreadable bytes. It does this with TLS, which runs underneath HTTP.

**How the connection is set up**

1. Your browser connects and the server sends its certificate, which proves the domain's identity. A certificate authority your device already trusts has signed it.
2. The browser checks the signature, the domain name, and the expiry date. If any check fails, you get a warning page.
3. Both sides run an ephemeral Diffie-Hellman key exchange. They end up with the same secret key without ever sending it, so someone recording the traffic cannot derive it.
4. All further traffic, including your password in the login request, is encrypted with that key (AES-GCM or ChaCha20). These ciphers also detect tampering, so an attacker can't alter the data in flight without being noticed.

`★ Insight ─────────────────────────────────────`
- Authentication (the certificate) and encryption (the session key) are separate jobs. Without the certificate check, you could be encrypting traffic straight to an attacker.
- Because the keys are ephemeral, stealing the server's private key later doesn't decrypt old recordings. This is called forward secrecy.
`─────────────────────────────────────────────────`

**What HTTPS does not protect**

- **The server still sees your password in plain text** after decrypting it. A well-built site hashes it (bcrypt or argon2) before storing it, but HTTPS doesn't ensure that.
- **Phishing sites can have valid certificates.** The padlock means "encrypted to this domain", not "this domain is the real one".
- **Malware or a malicious browser extension on your device** reads the password before it is encrypted.

If you want to see this on a real site, run `curl -v https://example.com` in your terminal. It prints the TLS version, cipher, and certificate details from the handshake.
