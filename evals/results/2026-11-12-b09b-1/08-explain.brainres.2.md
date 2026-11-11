<!-- Q: Explain how HTTPS keeps my password safe. -->

HTTPS keeps your password safe by encrypting it before it leaves your browser, so anyone watching the network (Wi-Fi owners, ISPs, attackers on the same café network) sees only scrambled bytes.

It works in three steps:

1. **Identity check.** The server sends a certificate, signed by a certificate authority your browser already trusts. Your browser verifies the certificate matches the domain, so you know you're talking to the real site and not an impostor.
2. **Key agreement.** Your browser and the server run a key exchange (in TLS 1.3, an ephemeral Diffie-Hellman exchange). Both sides derive the same secret session key without ever sending it across the network. Because the key is ephemeral, recording the traffic and stealing the server's key later still doesn't reveal your password.
3. **Encrypted transfer.** Everything after that, including the login form and your password, is encrypted with the session key (e.g., AES-GCM). That encryption also detects tampering, so an attacker can't alter the data in transit without being noticed.

**What HTTPS does not protect:**

- **The server itself.** The site still receives your password in plaintext after decrypting it. It should store only a salted hash, but HTTPS doesn't enforce that.
- **Your device.** Malware or a keylogger sees the password before encryption.
- **Phishing.** A valid certificate for `paypa1.com` is still a valid certificate. HTTPS proves *which* domain you reached, not that the domain is trustworthy.

Next step: check for the padlock and the exact domain in the address bar before typing a password, and use a password manager, which refuses to autofill on look-alike domains.
