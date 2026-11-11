<!-- Q: Explain how HTTPS keeps my password safe. -->

HTTPS keeps your password safe by encrypting it before it leaves your browser, so anyone watching the network (Wi-Fi owners, ISPs, attackers on the same café network) sees only scrambled bytes instead of the password.

It does this in three steps:

1. **Identity check.** The server sends a certificate, signed by a certificate authority your browser already trusts. Your browser verifies that the certificate matches the domain you typed, so you are talking to the real site and not an impostor.
2. **Key agreement.** Your browser and the server run a key exchange (TLS uses Diffie-Hellman variants). Both sides end up with the same secret session key, but that key never travels over the network, so an eavesdropper cannot reconstruct it.
3. **Encrypted traffic.** Everything after that, including the login form with your password, is encrypted with the session key. It is also authenticated, so any tampering in transit is detected and the connection fails.

**What HTTPS does not protect against:**

- A phishing site with its own valid certificate (the padlock only means the connection is private, not that the site is honest).
- Malware or a malicious extension on your device, which sees the password before encryption.
- A breach on the server side, where the site stores passwords badly. Good sites store only salted hashes.
- Reusing the same password across sites.

Next action: check that the address bar shows the correct domain before typing a password, and use a password manager. It fills credentials only on the exact domain you saved, which defeats most phishing.
