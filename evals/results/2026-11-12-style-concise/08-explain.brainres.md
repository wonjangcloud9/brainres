<!-- Q: Explain how HTTPS keeps my password safe. -->

HTTPS encrypts everything between your browser and the website, so anyone on the network path (Wi-Fi owner, ISP, attacker) sees only scrambled bytes instead of your password.

It works in three parts, all part of TLS, the protocol underneath HTTPS:

1. **Identity check.** The server sends a certificate, signed by a certificate authority (CA) your browser already trusts. It proves you are talking to the real `example.com`, not an impostor. If the check fails, the browser shows a warning.
2. **Key agreement.** Your browser and the server run a key exchange (usually ephemeral Diffie-Hellman). Both sides derive the same secret key without ever sending it over the wire. Because the key is temporary, recording the traffic and stealing the server's long-term key later still doesn't decrypt it.
3. **Encrypted, tamper-proof traffic.** Every request, including the one carrying your password, is encrypted with that shared key (e.g. AES-GCM). The same step adds an integrity check, so any modification in transit is detected and rejected.

**What it doesn't protect against:**
- Malware or a malicious browser extension on your device, which sees the password before encryption.
- Phishing: a fake site with a valid certificate for its own domain. Check the domain name, not just the padlock.
- The website itself mishandling your password. HTTPS only covers the trip, not storage. Sites should store a salted hash (e.g. Argon2 or bcrypt), not the password.

Next step: if you're building a login form, serve it over HTTPS only, redirect HTTP to HTTPS, and enable HSTS so browsers never try plain HTTP. I can show the config for your server if you tell me which one you use.
